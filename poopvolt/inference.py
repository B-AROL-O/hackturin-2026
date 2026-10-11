"""CPU-only ONNX detection with an explicit, verified export contract."""

import json
from pathlib import Path
from time import perf_counter
from typing import Literal

from PIL import Image
from pydantic import BaseModel, ConfigDict, Field, model_validator


class ModelClass(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: str = Field(min_length=1)
    kind: Literal["panel", "dust", "bird_dropping", "visible_damage", "other"]


class ModelConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(min_length=1)
    output_format: Literal["yolov8"]
    input_size: int = Field(ge=32, le=1280, multiple_of=32)
    classes: list[ModelClass] = Field(min_length=1, max_length=1000)
    confidence_threshold: float = Field(default=0.4, gt=0, lt=1)
    nms_threshold: float = Field(default=0.45, gt=0, lt=1)

    @model_validator(mode="after")
    def unique_labels(self):
        if len({entry.label for entry in self.classes}) != len(self.classes):
            raise ValueError("Class labels must be unique and follow export order")
        return self


class Detector:
    """One OpenCV Net. Caller must serialize infer() calls."""

    def __init__(self, model_path: Path, config_path: Path):
        import cv2
        import numpy as np

        self.cv2, self.np = cv2, np
        self.config = ModelConfig.model_validate(json.loads(config_path.read_text()))
        cv2.setNumThreads(4)
        self.net = cv2.dnn.readNetFromONNX(str(model_path))
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
        # Validate graph execution and output shape before declaring readiness.
        self.infer(Image.new("RGB", (self.config.input_size,) * 2))

    def infer(self, image: Image.Image) -> tuple[list[dict], float]:
        started = perf_counter()
        cv2, np = self.cv2, self.np
        width, height = image.size
        size = self.config.input_size
        scale = min(size / width, size / height)
        resized_w, resized_h = (
            max(1, round(width * scale)),
            max(1, round(height * scale)),
        )
        left, top = (size - resized_w) // 2, (size - resized_h) // 2
        rgb = np.asarray(image.convert("RGB"))
        resized = cv2.resize(rgb, (resized_w, resized_h))
        padded = np.full((size, size, 3), 114, dtype=np.uint8)
        padded[top : top + resized_h, left : left + resized_w] = resized
        # PIL already supplies RGB. Do not swap channels again.
        blob = cv2.dnn.blobFromImage(padded, 1 / 255.0, (size, size))
        self.net.setInput(blob)
        outputs = self.net.forward(self.net.getUnconnectedOutLayersNames())
        if len(outputs) != 1:
            raise ValueError(
                "Expected one raw detection output; segmentation is unsupported"
            )
        output = outputs[0]
        channels = 4 + len(self.config.classes)
        if output.ndim != 3 or output.shape[0] != 1 or output.shape[1] != channels:
            raise ValueError(
                f"Expected YOLOv8 [1,{channels},N], received {output.shape}"
            )
        if not np.isfinite(output).all():
            raise ValueError("Model returned non-finite values")
        rows = output[0].T
        scores = rows[:, 4:]
        if np.any(scores < 0) or np.any(scores > 1):
            raise ValueError("Expected class probabilities in [0,1]")
        class_ids = scores.argmax(axis=1)
        detections = []
        # Per-class NMS preserves overlapping panels and defects.
        for class_id, entry in enumerate(self.config.classes):
            candidates = rows[class_ids == class_id]
            candidates = candidates[
                candidates[:, 4 + class_id] >= self.config.confidence_threshold
            ]
            boxes, confidences = [], []
            for row in candidates:
                cx, cy, box_w, box_h = map(float, row[:4])
                if box_w <= 0 or box_h <= 0:
                    continue
                x1 = max(0.0, min(width, (cx - box_w / 2 - left) / scale))
                y1 = max(0.0, min(height, (cy - box_h / 2 - top) / scale))
                x2 = max(0.0, min(width, (cx + box_w / 2 - left) / scale))
                y2 = max(0.0, min(height, (cy + box_h / 2 - top) / scale))
                if x2 <= x1 or y2 <= y1:
                    continue
                boxes.append([x1, y1, x2 - x1, y2 - y1])
                confidences.append(float(row[4 + class_id]))
            kept = cv2.dnn.NMSBoxes(
                boxes,
                confidences,
                self.config.confidence_threshold,
                self.config.nms_threshold,
            )
            for index in np.asarray(kept, dtype=int).reshape(-1):
                detections.append(
                    {
                        "label": entry.label,
                        "kind": entry.kind,
                        "confidence": confidences[index],
                        "box": boxes[index],
                        "panel_id": None,
                    }
                )
        detections.sort(key=lambda item: item["confidence"], reverse=True)
        detections = detections[:100]
        for index, item in enumerate(detections):
            item["id"] = f"d{index + 1}"
        panels = [item for item in detections if item["kind"] == "panel"]
        for item in detections:
            if item["kind"] in {"panel", "other"}:
                continue
            x, y, w, h = item["box"]
            matches = [
                panel
                for panel in panels
                if panel["box"][0] <= x + w / 2 <= panel["box"][0] + panel["box"][2]
                and panel["box"][1] <= y + h / 2 <= panel["box"][1] + panel["box"][3]
            ]
            if matches:
                item["panel_id"] = min(
                    matches, key=lambda panel: panel["box"][2] * panel["box"][3]
                )["id"]
        return detections, (perf_counter() - started) * 1000


def recommendation(predictions: list[dict]) -> str | None:
    """Conservative rules triggered only by emitted defect detections."""
    kinds = {item["kind"] for item in predictions}
    if "visible_damage" in kinds:
        return "Visible damage detected: arrange a technician inspection."
    if kinds & {"dust", "bird_dropping"}:
        return "Surface soiling detected: review the photograph and consider cleaning."
    return None
