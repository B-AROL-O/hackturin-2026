# Inspection model placeholders

Supply `inspection.onnx` and its verified `inspection.json` here before hardware
testing. Neither is included yet. The API never substitutes a model or fake
predictions. `inspection.example.json` is a schema example with placeholder
labels, not an adopted class list. The current adapter supports only the explicit
YOLOv8 detection contract in [the setup guide](../docs/phone-inspection.md).

Actual class order, input size, preprocessing and output layout must come from
the trained exporter. Map only real supported classes to dashboard categories.
Restart the API after providing/changing the model/configuration.
