"""Single-process phone-to-edge inspection service."""

import io
import json
import logging
import os
import time
from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from threading import Lock
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageOps, UnidentifiedImageError
from starlette.concurrency import run_in_threadpool
from starlette.datastructures import UploadFile

from poopvolt.inference import Detector, recommendation
from poopvolt.storage import InspectionStore

LOGGER = logging.getLogger(__name__)
STATIC = Path(__file__).parent / "static"


@dataclass
class Settings:
    model: Path = Path("models/inspection.onnx")
    config: Path = Path("models/inspection.json")
    storage: Path = Path("data/inspections")
    max_upload_bytes: int = 12 * 1024 * 1024
    max_pixels: int = 24_000_000
    max_count: int = 100
    max_storage_bytes: int = 250 * 1024 * 1024
    # Latest station reading, written by firmware/station/linux/station_rx.py --latest.
    station: Path = Path("data/station/latest.json")
    station_max_age_s: float = 10.0

    @classmethod
    def from_env(cls):
        return cls(
            model=Path(os.getenv("POOPVOLT_MODEL", "models/inspection.onnx")),
            config=Path(os.getenv("POOPVOLT_MODEL_CONFIG", "models/inspection.json")),
            storage=Path(os.getenv("POOPVOLT_STORAGE", "data/inspections")),
            station=Path(os.getenv("POOPVOLT_STATION", "data/station/latest.json")),
        )


class UploadLimit:
    """Bound the entire multipart body, including chunked requests, before spooling."""

    def __init__(self, app, limit: int):
        self.app, self.limit = app, limit

    async def __call__(self, scope, receive, send):
        if (
            scope["type"] != "http"
            or scope["method"] != "POST"
            or scope["path"] != "/api/inspect"
        ):
            return await self.app(scope, receive, send)
        headers = dict(scope["headers"])
        try:
            declared = int(headers.get(b"content-length", b"0"))
            if declared < 0:
                raise ValueError
        except ValueError:
            return await JSONResponse(
                {"detail": "Invalid Content-Length"}, status_code=400
            )(scope, receive, send)
        if declared > self.limit:
            return await JSONResponse(
                {"detail": "Upload exceeds 12 MiB limit"}, status_code=413
            )(scope, receive, send)
        received = 0

        async def limited_receive():
            nonlocal received
            message = await receive()
            received += len(message.get("body", b""))
            if received > self.limit:
                raise HTTPException(413, "Upload exceeds the request size limit")
            return message

        await self.app(scope, limited_receive, send)


def decode_image(data: bytes, settings: Settings):
    try:
        with Image.open(io.BytesIO(data)) as source:
            if source.format not in {"JPEG", "PNG", "WEBP"}:
                raise HTTPException(
                    415, "Use a JPEG, PNG or WebP photograph (HEIC is unsupported)"
                )
            width, height = source.size
            if width * height > settings.max_pixels or max(width, height) > 10_000:
                raise HTTPException(
                    413, "Image exceeds 24 megapixels or 10,000 pixels per side"
                )
            if getattr(source, "n_frames", 1) != 1:
                raise HTTPException(415, "Animated images are unsupported")
            source.verify()
        with Image.open(io.BytesIO(data)) as source:
            keep_original = (
                source.format == "JPEG" and source.getexif().get(274, 1) == 1
            )
            image = ImageOps.exif_transpose(source).convert("RGB")
            image.load()
        if keep_original:
            return image, data
        output = io.BytesIO()
        image.save(output, format="JPEG", quality=90)
        return image, output.getvalue()
    except (UnidentifiedImageError, OSError, ValueError, SyntaxError) as exc:
        raise HTTPException(422, "Invalid or truncated image") from exc
    except (Image.DecompressionBombError, Image.DecompressionBombWarning) as exc:
        raise HTTPException(413, "Image dimensions are too large") from exc


def create_app(settings: Settings | None = None, detector_factory=Detector):
    settings = settings or Settings.from_env()
    if (
        min(
            settings.max_upload_bytes,
            settings.max_pixels,
            settings.max_count,
            settings.max_storage_bytes,
        )
        <= 0
    ):
        raise ValueError("Upload and retention limits must be positive")
    busy = Lock()

    @asynccontextmanager
    async def lifespan(app):
        app.state.store = InspectionStore(
            settings.storage, settings.max_count, settings.max_storage_bytes
        )
        app.state.detector, app.state.model_error = None, None
        try:
            app.state.detector = await run_in_threadpool(
                detector_factory, settings.model, settings.config
            )
        except Exception as exc:  # noqa: BLE001
            # Model startup failures must not hide saved inspections.
            LOGGER.warning("Inspection model not ready: %s", exc)
            app.state.model_error = str(exc)
        yield

    app = FastAPI(title="PoopVolt inspection", lifespan=lifespan)
    app.add_middleware(UploadLimit, limit=settings.max_upload_bytes + 64 * 1024)

    @app.get("/api/health")
    async def health():
        detector = app.state.detector
        return JSONResponse(
            {
                "api_ready": True,
                "model_ready": detector is not None,
                "model": detector.config.name if detector else None,
                "model_error": app.state.model_error,
                "busy": busy.locked(),
                "max_upload_bytes": settings.max_upload_bytes,
                "capabilities": (
                    sorted({entry.kind for entry in detector.config.classes})
                    if detector
                    else []
                ),
            },
            status_code=200 if detector else 503,
        )

    @app.get("/api/station")
    async def station():
        """Latest UNO Q station reading; unavailable when missing or stale."""
        try:
            age = time.time() - settings.station.stat().st_mtime
            reading = json.loads(settings.station.read_text())
        except (OSError, ValueError):
            return JSONResponse({"available": False, "age_s": None, "reading": None})
        return JSONResponse(
            {
                "available": age <= settings.station_max_age_s,
                "age_s": round(age, 1),
                "reading": reading,
            }
        )

    def process(data):
        image, jpeg = decode_image(data, settings)
        try:
            predictions, latency = app.state.detector.infer(image)
        except Exception as exc:
            LOGGER.exception("Inspection inference failed")
            # Stop accepting work after an incompatible or failed model execution.
            app.state.model_error = str(exc)
            app.state.detector = None
            raise HTTPException(
                503, "Model inference failed; check server logs and restart"
            ) from exc
        inspection_id = str(uuid4())
        metadata = {
            "id": inspection_id,
            "created_at": datetime.now(UTC).isoformat(),
            "width": image.width,
            "height": image.height,
            "image_url": f"/api/inspections/{inspection_id}/image",
            "url": f"/inspections/{inspection_id}",
            "model": app.state.detector.config.name,
            "capabilities": sorted(
                {entry.kind for entry in app.state.detector.config.classes}
            ),
            "inference_ms": round(latency, 2),
            "predictions": predictions,
            "recommendation": recommendation(predictions),
            "recommendation_source": (
                "Detection-based review rule; not a model maintenance score"
            ),
            "panel_association": (
                "Defect box center inside smallest detected panel; geometric heuristic"
            ),
        }
        try:
            app.state.store.save(metadata, jpeg)
        except ValueError as exc:
            raise HTTPException(413, str(exc)) from exc
        except OSError as exc:
            LOGGER.exception("Inspection storage failed")
            raise HTTPException(
                507, "Could not save inspection; check available storage"
            ) from exc
        return metadata

    @app.post("/api/inspect", status_code=201)
    async def inspect(request: Request):
        if app.state.detector is None:
            raise HTTPException(
                503, "Model not ready; configure the trained ONNX model and restart"
            )
        if not busy.acquire(blocking=False):
            raise HTTPException(
                429,
                "An inspection is already running; retry when it finishes",
                headers={"Retry-After": "2"},
            )
        try:
            if (
                request.headers.get("content-type", "").split(";")[0].strip().lower()
                != "multipart/form-data"
            ):
                raise HTTPException(
                    415, "Send multipart/form-data with one image field"
                )
            async with request.form(max_files=1, max_fields=0) as form:
                items = form.multi_items()
                if (
                    len(items) != 1
                    or items[0][0] != "image"
                    or not isinstance(items[0][1], UploadFile)
                ):
                    raise HTTPException(422, "Supply exactly one image file")
                upload = items[0][1]
                if upload.content_type not in {"image/jpeg", "image/png", "image/webp"}:
                    raise HTTPException(415, "Use a JPEG, PNG or WebP photograph")
                data = await upload.read(settings.max_upload_bytes + 1)
                if len(data) > settings.max_upload_bytes:
                    raise HTTPException(413, "Image exceeds 12 MiB limit")
                if not data:
                    raise HTTPException(422, "Image is empty")
                return await run_in_threadpool(process, data)
        finally:
            busy.release()

    @app.get("/api/inspections/{inspection_id}")
    async def get_inspection(inspection_id: UUID):
        try:
            return await run_in_threadpool(app.state.store.get, inspection_id)
        except FileNotFoundError as exc:
            raise HTTPException(
                404, "Inspection not found or removed by retention"
            ) from exc

    @app.get("/api/inspections/{inspection_id}/image")
    async def get_image(inspection_id: UUID):
        _, path = app.state.store.paths(inspection_id)
        try:
            data = await run_in_threadpool(path.read_bytes)
        except FileNotFoundError as exc:
            raise HTTPException(
                404, "Inspection image not found or removed by retention"
            ) from exc
        return Response(
            data, media_type="image/jpeg", headers={"Cache-Control": "no-store"}
        )

    def exclusive(operation, *args):
        """Run a storage change only while no inspection is being saved."""
        if not busy.acquire(blocking=False):
            raise HTTPException(
                429,
                "An inspection is running; retry when it finishes",
                headers={"Retry-After": "2"},
            )
        try:
            return operation(*args)
        finally:
            busy.release()

    @app.delete("/api/inspections/{inspection_id}", status_code=204)
    async def delete_inspection(inspection_id: UUID):
        if not await run_in_threadpool(
            exclusive, app.state.store.delete, inspection_id
        ):
            raise HTTPException(404, "Inspection not found or already removed")
        return Response(status_code=204)

    @app.delete("/api/inspections")
    async def clear_inspections():
        removed = await run_in_threadpool(exclusive, app.state.store.clear)
        return {"removed": removed}

    app.mount("/static", StaticFiles(directory=STATIC), name="static")

    @app.get("/")
    @app.get("/inspections/{inspection_id}")
    async def dashboard(inspection_id: UUID | None = None):
        return FileResponse(
            STATIC / "index.html", headers={"Cache-Control": "no-store"}
        )

    return app


app = create_app()


def main():
    import uvicorn

    # More workers would each load a model and defeat the inference gate.
    uvicorn.run("poopvolt.server:app", host="0.0.0.0", port=8000, workers=1)


if __name__ == "__main__":
    main()
