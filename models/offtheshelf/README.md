# Off-the-shelf test model (pipeline test, not the PoopVolt model)

A public YOLOv8n solar-panel defect detector, used to test the phone → UNO Q →
dashboard pipeline until Giacomo's trained model is ready.

- Source: Hugging Face Space
  [mtahajawad/solar-panel-defect-detector](https://huggingface.co/spaces/mtahajawad/solar-panel-defect-detector),
  file `best.pt`. Licence: MIT.
- Trained by its author on 700 images of the Roboflow "Solar Panel Defects"
  dataset, mostly aerial, thermal and electroluminescence imagery. Reported
  mAP50 0.27 (mAP50-95 0.15). Classes: Bird-Drop, Clean, Defective, Dusty, plus
  Electrical-Damage, Physical-Damage and Snow, which have no training data.
- Mapping in [`inspection.json`](inspection.json): Bird-Drop → bird_dropping,
  Dusty → dust, the damage classes → visible_damage, Clean → panel,
  Snow → other. Confidence threshold 0.25.

## Build and deploy

```sh
models/offtheshelf/export.sh   # needs uv; downloads torch the first time
$ADB push models/offtheshelf/inspection.onnx /home/arduino/hackturin-2026/models/inspection.onnx
$ADB push models/offtheshelf/inspection.json /home/arduino/hackturin-2026/models/inspection.json
$ADB shell docker restart poopvolt
```

## What we measured (2026-10-11, UNO Q)

- Inference about 0.8 s per photo on the UNO Q CPU (OpenCV DNN).
- The pipeline works from a Samsung S23 Ultra over Wi-Fi: photo upload, detection
  on the board, result on the dashboard.
- On our mini panel: a clean photo gives no detections. When the photo is cropped
  to the panel, the model recognises it as Clean (0.70).
- It does **not** detect white paper placed on the panel, as fake droppings: scores
  stay at noise level (about 0.1). Treat it as a pipeline test, not a soiling
  detector.
