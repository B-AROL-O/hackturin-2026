# UNO Q budget for the CV model

Measured on our board on 2026-10-10, with nothing else running.

| Resource                            | Value                                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Free storage                        | 2.9 GB (eMMC, shared by OS, apps, Docker). Another 2.5 GB is held by preinstalled Docker images (incl. the Edge Impulse runner) |
| RAM                                 | 3.6 GB total, about 3.2 GB available, plus 1.8 GB swap                                                                          |
| CPU                                 | 4× Kryo-V2 (Cortex-A53 class) at 2.0 GHz. NEON, but no dot-product or fp16 extensions                                           |
| Accelerators                        | No NPU. Adreno GPU via DRM only (untested), so plan for **CPU-only** inference                                                  |
| Preinstalled (Arduino Python image) | Python 3.13, numpy 2.2, OpenCV 4.12 (`cv2.dnn` runs ONNX), Pillow. No onnxruntime, TFLite or torch                              |

## Measured inference (OpenCV DNN, fp32, 4 threads)

| Model                             | Input   | Latency                |
| --------------------------------- | ------- | ---------------------- |
| NanoDet-Plus (OpenCV zoo, 3.8 MB) | 416×416 | 258 ms (about 4 FPS)   |
| YOLOX-S (OpenCV zoo, 36 MB)       | 640×640 | 2.27 s (about 0.4 FPS) |

That's roughly 4 GFLOPS effective. Estimate latency as model GFLOPs ÷ 4. For example, YOLOv8n is about 2 s at 640 and about 0.5 s at 320. These are estimates: int8 TFLite with XNNPACK or onnxruntime may be faster, but neither is installed yet.

## Guidance

- Model file size is not the constraint (anything under about 100 MB is fine); latency is.
- Panels change slowly, so one frame every few seconds is enough. A nano/small detector at 320–640 fits.
- Edge Impulse's runner image is already on the board (`ei-models-runner`), so an EI-exported model needs no extra install.
