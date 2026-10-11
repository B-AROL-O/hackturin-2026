"""Small filesystem store; metadata is the commit marker for each inspection."""

import json
from pathlib import Path
from uuid import UUID


class InspectionStore:
    def __init__(self, root: Path, max_count: int, max_bytes: int):
        self.root = root
        self.max_count, self.max_bytes = max_count, max_bytes
        root.mkdir(parents=True, exist_ok=True)
        # One process owns this directory. Remove interrupted writes on startup.
        for path in root.glob("*.tmp"):
            path.unlink()
        for path in root.glob("*.jpg"):
            if not path.with_suffix(".json").exists():
                path.unlink()
        self.prune()

    def paths(self, inspection_id: UUID):
        base = self.root / str(inspection_id)
        return base.with_suffix(".json"), base.with_suffix(".jpg")

    def save(self, metadata: dict, jpeg: bytes):
        record, image = self.paths(UUID(metadata["id"]))
        payload = json.dumps(metadata, allow_nan=False).encode()
        if len(payload) + len(jpeg) > self.max_bytes:
            raise ValueError("Image exceeds the storage budget")
        try:
            image.with_suffix(".jpg.tmp").write_bytes(jpeg)
            image.with_suffix(".jpg.tmp").replace(image)
            record.with_suffix(".json.tmp").write_bytes(payload)
            record.with_suffix(".json.tmp").replace(record)
        except OSError:
            for path in (
                image,
                record,
                image.with_suffix(".jpg.tmp"),
                record.with_suffix(".json.tmp"),
            ):
                path.unlink(missing_ok=True)
            raise
        self.prune()

    def get(self, inspection_id: UUID) -> dict:
        record, _ = self.paths(inspection_id)
        return json.loads(record.read_text())

    def prune(self):
        records = sorted(
            self.root.glob("*.json"), key=lambda path: path.stat().st_mtime_ns
        )
        sizes = [
            record.stat().st_size
            + (
                record.with_suffix(".jpg").stat().st_size
                if record.with_suffix(".jpg").exists()
                else 0
            )
            for record in records
        ]
        total, count = sum(sizes), len(records)
        for record, size in zip(records, sizes):
            if count <= self.max_count and total <= self.max_bytes:
                break
            record.unlink(missing_ok=True)
            record.with_suffix(".jpg").unlink(missing_ok=True)
            total -= size
            count -= 1
