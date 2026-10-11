import io
import json
from concurrent.futures import ThreadPoolExecutor
from threading import Event
from uuid import uuid4

import numpy as np
import pytest
from fastapi.testclient import TestClient
from PIL import Image

from poopvolt.inference import Detector, recommendation
from poopvolt.server import Settings, create_app
from poopvolt.storage import InspectionStore


def photograph(fmt="JPEG", size=(128, 64), exif=None):
    output = io.BytesIO()
    options = {"exif": exif} if exif else {}
    Image.new("RGB", size, (40, 100, 150)).save(output, format=fmt, **options)
    return output.getvalue()


def upload(client, data=None, content_type="image/jpeg"):
    return client.post(
        "/api/inspect",
        files={
            "image": (
                "photo.jpg",
                data if data is not None else photograph(),
                content_type,
            )
        },
    )


def test_real_opencv_upload_read_and_reload(model_settings):
    with TestClient(create_app(model_settings)) as client:
        health = client.get("/api/health")
        assert health.status_code == 200
        assert health.json()["model_ready"] is True
        assert client.get("/").status_code == 200
        assert 'capture="environment"' in client.get("/").text
        assert client.get("/static/app.js").status_code == 200
        original = photograph()
        response = upload(client, original)
        assert response.status_code == 201, response.text
        record = response.json()
        assert record["width"] == 128 and record["height"] == 64
        assert record["inference_ms"] > 0
        predictions = record["predictions"]
        assert {item["kind"] for item in predictions} == {
            "panel",
            "dust",
            "visible_damage",
        }
        panel = next(item for item in predictions if item["kind"] == "panel")
        dust = next(item for item in predictions if item["kind"] == "dust")
        assert panel["box"] == pytest.approx([0, 0, 128, 64])
        assert dust["box"] == pytest.approx([24, 8, 16, 16])
        assert dust["panel_id"] == panel["id"]
        assert dust["confidence"] == pytest.approx(0.8)
        assert "technician inspection" in record["recommendation"]
        assert client.get(f"/api/inspections/{record['id']}").json() == record
        assert client.get(record["image_url"]).content == original
        assert client.get(record["url"]).status_code == 200
    # Persistence survives model/API reload and works from a second client.
    with TestClient(create_app(model_settings)) as client:
        assert client.get(f"/api/inspections/{record['id']}").json() == record


def test_model_placeholder_still_serves_ui_and_no_predictions(tmp_path):
    settings = Settings(
        model=tmp_path / "absent.onnx",
        config=tmp_path / "absent.json",
        storage=tmp_path / "data",
    )
    with TestClient(create_app(settings)) as client:
        health = client.get("/api/health")
        assert health.status_code == 503
        assert health.json()["api_ready"] and not health.json()["model_ready"]
        assert health.json()["capabilities"] == []
        assert upload(client).status_code == 503
        assert client.get("/").status_code == 200
        assert client.get(f"/api/inspections/{uuid4()}").status_code == 404
        assert client.get("/api/inspections/../../secret").status_code != 200
        assert not list(settings.storage.iterdir())


def test_invalid_model_contract_not_ready(model_settings):
    config = json.loads(model_settings.config.read_text())
    config["classes"] = config["classes"][:1]
    model_settings.config.write_text(json.dumps(config))
    with TestClient(create_app(model_settings)) as client:
        assert client.get("/api/health").status_code == 503
        assert upload(client).status_code == 503


def test_upload_validation_and_limits(model_settings):
    model_settings.max_upload_bytes = 2048
    model_settings.max_pixels = 10_000
    with TestClient(create_app(model_settings)) as client:
        assert upload(client, b"not an image").status_code == 422
        assert upload(client, b"").status_code == 422
        assert upload(client, photograph("GIF")).status_code == 415
        assert upload(client, photograph(), "text/plain").status_code == 415
        assert upload(client, b"a" * 2049).status_code == 413
        assert upload(client, photograph(size=(200, 100))).status_code == 413
        assert upload(client, photograph()[:100]).status_code == 422
        assert client.post("/api/inspect", json={"image": "bad"}).status_code == 415
        assert (
            client.post(
                "/api/inspect",
                files={"wrong": ("photo.jpg", photograph(), "image/jpeg")},
            ).status_code
            == 422
        )
        response = client.post(
            "/api/inspect",
            files=[
                ("image", ("a.jpg", photograph(), "image/jpeg")),
                ("image", ("b.jpg", photograph(), "image/jpeg")),
            ],
        )
        assert response.status_code == 400
        assert (
            client.post(
                "/api/inspect", content=b"x", headers={"content-length": "99999999"}
            ).status_code
            == 413
        )
        # Streaming bodies cannot bypass Content-Length enforcement.
        chunks = [
            b'--x\r\nContent-Disposition: form-data; name="image"; filename="a.jpg"\r\nContent-Type: image/jpeg\r\n\r\n',
            b"x" * 70000,
            b"\r\n--x--\r\n",
        ]
        response = client.post(
            "/api/inspect",
            content=iter(chunks),
            headers={"content-type": "multipart/form-data; boundary=x"},
        )
        assert response.status_code == 413
        # Failed validation releases the inference gate.
        assert upload(client).status_code == 201


def test_orientation_png_and_retention(model_settings):
    model_settings.max_count = 1
    with TestClient(create_app(model_settings)) as client:
        exif = Image.Exif()
        exif[274] = 6
        first = upload(client, photograph(size=(64, 128), exif=exif)).json()
        assert (first["width"], first["height"]) == (128, 64)
        stored = Image.open(io.BytesIO(client.get(first["image_url"]).content))
        assert stored.size == (128, 64) and stored.getexif().get(274, 1) == 1
        second = upload(client, photograph("PNG"), "image/png").json()
        image_response = client.get(second["image_url"])
        assert image_response.headers["content-type"] == "image/jpeg"
        assert Image.open(io.BytesIO(image_response.content)).format == "JPEG"
        assert client.get(first["image_url"]).status_code == 404
        assert client.get(f"/api/inspections/{first['id']}").status_code == 404
        assert len(list(model_settings.storage.glob("*.jpg"))) == 1


def test_single_model_instance_and_busy_rejection(model_settings):
    started, release = Event(), Event()
    instances = []

    def factory(model, config):
        detector = Detector(model, config)
        infer = detector.infer

        def blocking_infer(image):
            started.set()
            assert release.wait(5)
            return infer(image)

        detector.infer = blocking_infer
        instances.append(detector)
        return detector

    with (
        TestClient(create_app(model_settings, factory)) as client,
        ThreadPoolExecutor() as executor,
    ):
        first = executor.submit(upload, client)
        try:
            assert started.wait(5)
            assert client.get("/api/health").json()["busy"]
            assert upload(client).status_code == 429
        finally:
            release.set()
        assert first.result().status_code == 201
        assert upload(client).status_code == 201
        assert len(instances) == 1


def test_inference_failure_disables_model(model_settings):
    def factory(model, config):
        detector = Detector(model, config)

        def fail(image):
            raise ValueError("incompatible output")

        detector.infer = fail
        return detector

    with TestClient(create_app(model_settings, factory)) as client:
        assert upload(client).status_code == 503
        assert client.get("/api/health").status_code == 503
        assert upload(client).status_code == 503
        assert not list(model_settings.storage.iterdir())


def test_storage_byte_budget_and_interrupted_write_cleanup(tmp_path):
    root = tmp_path / "store"
    store = InspectionStore(root, max_count=10, max_bytes=250)
    ids = [str(uuid4()), str(uuid4())]
    for inspection_id in ids:
        store.save({"id": inspection_id}, b"x" * 120)
    assert len(list(root.glob("*.json"))) == 1
    with pytest.raises(ValueError):
        store.save({"id": str(uuid4())}, b"x" * 300)
    (root / "orphan.jpg").write_bytes(b"x")
    (root / "partial.tmp").write_bytes(b"x")
    InspectionStore(root, 10, 250)
    assert not (root / "orphan.jpg").exists()
    assert not (root / "partial.tmp").exists()


def test_recommendation_requires_emitted_defects():
    assert recommendation([]) is None
    assert recommendation([{"kind": "panel"}]) is None
    assert "cleaning" in recommendation([{"kind": "dust"}])


def test_rgb_normalization_padding_and_extreme_aspect_ratio(model_settings):
    detector = Detector(model_settings.model, model_settings.config)

    class CaptureInput:
        def __init__(self, net):
            self.net = net
            self.blob = None

        def __getattr__(self, name):
            return getattr(self.net, name)

        def setInput(self, blob):  # pylint: disable=invalid-name
            self.blob = blob.copy()
            self.net.setInput(blob)

    detector.net = CaptureInput(detector.net)
    detector.infer(Image.open(io.BytesIO(photograph("PNG"))))
    blob = detector.net.blob
    assert blob.shape == (1, 3, 64, 64)
    assert blob[0, :, 32, 32] == pytest.approx(np.array([40, 100, 150]) / 255)
    assert blob[0, :, 0, 0] == pytest.approx(np.full(3, 114 / 255))
    predictions, latency = detector.infer(Image.new("RGB", (1, 10_000)))
    assert latency > 0
    assert isinstance(predictions, list)
