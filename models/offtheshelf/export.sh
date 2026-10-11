#!/usr/bin/env sh
# Fetch the off-the-shelf YOLOv8n solar-defect model (MIT) and export it to the
# ONNX contract the inspection server expects ([1, 4 + 7, 8400], no NMS).
# Output: models/offtheshelf/inspection.onnx (not committed; about 12 MB).
set -eu
cd "$(dirname "$0")"
curl -sSfL -o best.pt \
  https://huggingface.co/spaces/mtahajawad/solar-panel-defect-detector/resolve/main/best.pt
uv run --python 3.12 --with ultralytics --with "onnx<1.18" --with onnxslim \
  --index https://download.pytorch.org/whl/cpu --index-strategy unsafe-best-match \
  python -c "from ultralytics import YOLO; YOLO('best.pt').export(format='onnx', imgsz=640, opset=12, dynamic=False, simplify=True, nms=False)"
mv best.onnx inspection.onnx
rm -f best.pt
echo "Wrote $(pwd)/inspection.onnx"
