# PoopVolt project status and reuse disclosure

- Status: Snapshot of 2026-10-11, for the Devpost description and the pitch Q&A.
  Update it when a feature changes state.
- Scope: What the team built, what it reuses, and what works today. The
  architecture views in [docs/architecture/](architecture/README.md) stay
  proposals until the matching row below says "working".

## Working versus incomplete

<!-- markdownlint-disable MD013 -->

| Area                                  | State                                  | Evidence and limits                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Grove sensors, LCD, NFC on UNO Q      | Working (bring-up)                     | AHT20, light sensor, 16x2 LCD and PN532 verified by the author in PR #49; see [wiring](hardware-connections.md). Light is relative, not calibrated irradiance.                                                                                                                                                                                                                                                                                                     |
| `station` firmware                    | Working (bring-up)                     | Shows readings on the LCD, exposes them as NFC tag text read by a phone, and streams them once per second to the Linux side ([setup](uno-q-setup.md)).                                                                                                                                                                                                                                                                                                             |
| Electrical schematic                  | Working                                | Editable KiCad source with verified exports; shows the USB-powered prototype only ([hardware](../hardware/README.md)).                                                                                                                                                                                                                                                                                                                                             |
| SOLARMA log importer                  | Working                                | [`poopvolt/solarma.py`](../poopvolt/solarma.py) parses the pinned export with tests. Irradiance is empty and string topology is unknown ([data plan](data-plan.md)).                                                                                                                                                                                                                                                                                               |
| UNO Q compute budget                  | Measured                               | CPU-only inference figures in the [model budget](uno-q-model-budget.md); no PoopVolt model has been run yet.                                                                                                                                                                                                                                                                                                                                                       |
| Expected-vs-observed comparison       | Working (scoped demo on replayed data) | [`poopvolt/comparison.py`](../poopvolt/comparison.py): each inverter is compared with its peers on daily energy, with a band and a chronological fit/evaluation split; results in [comparison results](comparison-results.md). It is **not** the weather-adjusted theoretical model (SOLARMA has no irradiance), orientation and capacity are unknown, and a deviation is a candidate for inspection, not a diagnosis. Injected losses are simulated and labelled. |
| RGB soiling detection (phone image) | Software slice implemented; model/hardware testing pending | HTTP upload, CPU OpenCV ONNX adapter and local image storage are implemented. Trained artifact/configuration remain placeholders; no PoopVolt model accuracy or UNO Q latency is claimed. See [phone inspection](phone-inspection.md). |
| Current sensor (ACS70331), solar path | Wired, not verified under light        | Zero offset verified in the dark (266.5 mV); panel, sensor, Waveshare manager and LiPo wired ([setup guide](replicate-uno-q-setup.md)). Current under sunlight and charging are untested; the panel read 4.55 V open-circuit at dusk, below the charger's 6 V input.                                                                                                                                                                                               |
| MCU to Linux data path                | Working (bring-up)                     | `station` sends readings once per second over the Bridge to [`station_rx.py`](../firmware/station/linux/station_rx.py), as reported by the firmware author; no agreed message format document yet ([#22](https://github.com/B-AROL-O/hackturin-2026/issues/22)).                                                                                                                                                                                                   |
| Operator UI and maintenance output | Inspection UI implemented; wider maintenance proposed | Original/annotated image comparison, panel selection and shared inspection URLs work in software. Home-page demo is labeled and never saved as inference. Detection-based review rules do not implement full maintenance or energy-loss prediction. |
| STL enclosure concept                 | Not delivered                          | Planned for the pitch; no file committed.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Thermal imaging, hotspot detection    | Out of scope                           | Thermal camera unavailable; the phone RGB camera replaces it.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Pitch deck                            | Plan only                              | HTML deck not implemented ([presentation](../presentation/README.md)).                                                                                                                                                                                                                                                                                                                                                                                             |

<!-- markdownlint-enable MD013 -->

## Phone-to-edge inspection

The FastAPI API, phone capture/upload page, SVG inspection dashboard, CPU OpenCV
adapter, and bounded local JPEG/JSON retention are implemented in `poopvolt/`.
The frontend is browser-ready static content packaged with the Python service;
it shares the backend URL. No independent frontend service is required.
The minimal dashboard now opens a labeled visual demo, showing an original sample
photo alongside an annotated view, with a PoopVolt SVG logo. Illustrative demo
annotations never enter the inference API or appear on uploaded photographs.

The trained ONNX artifact and its export/class configuration are intentional
placeholders, pending delivery and testing. No pre-existing model or inference
utility was found in this checkout. The first decoder supports the explicit
YOLOv8 detection contract documented in
[phone inspection setup](phone-inspection.md). Inference stays unavailable until
a configured model passes a startup execution/shape check. No results are mocked.

Software tests use a synthetic, untrained ONNX graph with real OpenCV 4.12;
they verify API/storage/decoder behavior, not trained-model accuracy. Smartphone
capture, delivered-model accuracy, actual UNO Q deployment and inference latency
are pending hardware validation. Existing board benchmark measurements remain
in [UNO Q model budget](uno-q-model-budget.md).

## Built by the team during the hackathon

- Product concept, pitch narrative, architecture views and Coesa context in
  `docs/`.
- Arduino sketches in [`firmware/`](../firmware/README.md): `sensor_diag`,
  `station` and the `imu_bridge` placeholder.
- Prototype wiring record and KiCad schematic in `hardware/`.
- SOLARMA importer, replay and the peer comparison with its tests in `poopvolt/` and `tests/`.
- Measurements of the UNO Q's resources.
- Phone inspection API, CPU ONNX adapter, local image store, UI, and software tests.
  Demo imagery/annotations are disclosed separately from model predictions.

## Pre-existing components

<!-- markdownlint-disable MD013 -->

| Component                                             | Role                                             | Licence / note                                                       |
| ----------------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------- |
| Arduino UNO Q, Zephyr core, `arduino-cli`, Bridge     | Board, toolchain and MCU to Linux link           | Arduino/Zephyr licences; see [setup](uno-q-setup.md)                 |
| Adafruit AHTX0 and PN532, Grove LCD libraries         | Sensor, NFC and display drivers used by sketches | Upstream library licences, installed through `arduino-cli`           |
| Seeed Grove modules and Base Shield                   | Sensors, LCD, NFC reader                         | Commercial parts                                                     |
| SOLARMA `pv-analysis-tools` data (revision `fc96313`) | Historical inverter logs for replay              | MIT; notice in [`data/solarma/NOTICE.md`](../data/solarma/NOTICE.md) |
| OpenCV, NanoDet-Plus and YOLOX-S demos                | Preinstalled on the board / used only for timing | Upstream licences; benchmark only, not shipped                       |
| KiCad, uv, pytest, Mermaid                            | Tooling                                          | Upstream licences                                                    |
| FastAPI | Inspection API | MIT |
| Starlette, Uvicorn | ASGI routing and HTTP server | BSD-3-Clause |
| python-multipart | Bounded image-upload parsing | Apache-2.0 |
| Pillow | Image validation, orientation and JPEG normalization | MIT-CMU (locked version) |
| numpy, opencv-python-headless | Optional desktop test/runtime extra | BSD-3-Clause / Apache-2.0 |
| HTTPX, ONNX | Development HTTP tests and synthetic graph fixtures only | BSD-3-Clause / Apache-2.0 |

<!-- markdownlint-enable MD013 -->

The repository is MIT licensed ([LICENSE](../LICENSE)). Any dependency added
later must be listed here with its licence.
