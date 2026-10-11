"""Synthetic ONNX graph for transport/decoder tests, never a deployed model."""

import json

import numpy as np
import onnx
import pytest
from onnx import TensorProto, helper, numpy_helper

from poopvolt.server import Settings


@pytest.fixture
def model_settings(tmp_path):
    pytest.importorskip("cv2", reason="Install the desktop extra for OpenCV tests")
    # [cx,cy,w,h,panel,dust,bird,damage] in 64x64 input coordinates.
    # Duplicate dust boxes exercise NMS; the bird box lies in letterbox padding.
    rows = np.array(
        [
            [32, 32, 64, 32, 0.95, 0, 0, 0],
            [16, 24, 8, 8, 0, 0.8, 0, 0],
            [16, 24, 8, 8, 0, 0.7, 0, 0],
            [4, 4, 4, 4, 0, 0, 0.9, 0],
            [48, 36, 4, 4, 0, 0, 0, 0.9],
        ],
        dtype=np.float32,
    )
    weights = np.zeros((40, 3), dtype=np.float32)
    graph = helper.make_graph(
        [
            helper.make_node("GlobalAveragePool", ["images"], ["pooled"]),
            helper.make_node("Flatten", ["pooled"], ["flat"], axis=1),
            helper.make_node("Gemm", ["flat", "weights", "bias"], ["values"], transB=1),
            helper.make_node("Reshape", ["values", "shape"], ["predictions"]),
        ],
        "synthetic-test-detector",
        [helper.make_tensor_value_info("images", TensorProto.FLOAT, [1, 3, 64, 64])],
        [helper.make_tensor_value_info("predictions", TensorProto.FLOAT, [1, 8, 5])],
        [
            numpy_helper.from_array(weights, "weights"),
            numpy_helper.from_array(rows.T.reshape(-1), "bias"),
            numpy_helper.from_array(np.array([1, 8, 5], dtype=np.int64), "shape"),
        ],
    )
    model = helper.make_model(
        graph, opset_imports=[helper.make_opsetid("", 13)], ir_version=8
    )
    onnx.checker.check_model(model)
    model_path, config_path = tmp_path / "test.onnx", tmp_path / "test.json"
    onnx.save(model, model_path)
    config_path.write_text(
        json.dumps(
            {
                "name": "synthetic-test-only",
                "output_format": "yolov8",
                "input_size": 64,
                "classes": [
                    {"label": kind, "kind": kind}
                    for kind in ["panel", "dust", "bird_dropping", "visible_damage"]
                ],
            }
        )
    )
    return Settings(
        model=model_path, config=config_path, storage=tmp_path / "inspections"
    )
