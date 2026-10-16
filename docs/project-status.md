# PoopVolt project status and reuse disclosure

- Status: Snapshot of 2026-10-16, release 0.3.0. Written for the Devpost
  description and the pitch Q&A. Update it when a feature changes state.
- Scope: What the team built, what it reuses, and what works today. The
  architecture views in [docs/architecture/](architecture/README.md) stay
  proposals until the matching row below says "working".

## Working versus incomplete

<!-- markdownlint-disable MD013 -->

| Area                                  | State                                                                                            | Evidence and limits                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Grove sensors, LCD, NFC on UNO Q      | Working (bring-up)                                                                               | AHT20, light sensor, 16x2 LCD and PN532 verified by the author in PR #49; see [wiring](hardware-connections.md). Light is relative, not calibrated irradiance.                                                                                                                                                                                                                                                                                                     |
| `station` firmware                    | Working (bring-up)                                                                               | Shows readings and the performance index (`P…%`) on the LCD, exposes them as NFC tag text read by a phone (with `perf=` and the dashboard address), and streams them once per second to the Linux side ([setup](uno-q-setup.md)).                                                                                                                                                                                                                                  |
| Electrical schematic                  | Working                                                                                          | Editable KiCad source with verified exports; shows the USB-powered prototype only ([hardware](../hardware/README.md)).                                                                                                                                                                                                                                                                                                                                             |
| SOLARMA log importer                  | Working                                                                                          | [`poopvolt/solarma.py`](../poopvolt/solarma.py) parses the pinned export with tests. Irradiance is empty and string topology is unknown ([data plan](data-plan.md)).                                                                                                                                                                                                                                                                                               |
| UNO Q compute budget                  | Measured                                                                                         | CPU-only inference figures in the [model budget](uno-q-model-budget.md). The off-the-shelf test model takes about 0.8 s per photo on the board ([test model](../models/offtheshelf/README.md)); no PoopVolt model has been run yet.                                                                                                                                                                                                                                |
| Expected-vs-observed comparison       | Working (scoped demo on replayed data)                                                           | [`poopvolt/comparison.py`](../poopvolt/comparison.py): each inverter is compared with its peers on daily energy, with a band and a chronological fit/evaluation split; results in [comparison results](comparison-results.md). It is **not** the weather-adjusted theoretical model (SOLARMA has no irradiance), orientation and capacity are unknown, and a deviation is a candidate for inspection, not a diagnosis. Injected losses are simulated and labelled. |
| RGB soiling detection (phone image)   | Pipeline working on the UNO Q with a test model; PoopVolt model pending                          | Phone photo → UNO Q → detections on the dashboard works over Wi-Fi from a Samsung S23 Ultra, using a public YOLOv8n defect detector (mAP50 0.27, MIT) as a [pipeline test](../models/offtheshelf/README.md). It does not detect our staged soiling (paper on the mini panel). No PoopVolt model accuracy is claimed. See [phone inspection](phone-inspection.md).                                                                                                  |
| Current sensor (ACS70331), solar path | Wired; no usable current measured                                                                | Zero offset verified in the dark (266.5 mV); panel, sensor, Waveshare manager and LiPo wired ([setup guide](replicate-uno-q-setup.md)). In the 2026-10-11 field test the mini panel could not drive the charger (it needs at least 6 V), and readings stayed within the sensor's temperature drift of about 18 mA ([field logs](../data/field-2026-10-11/README.md)). Needs a stronger panel.                                                                      |
| Panel performance index               | Implemented; not validated on a panel                                                            | [`station_rx.py`](../firmware/station/linux/station_rx.py) divides panel current by the clear-sky irradiance from [`solar_model.py`](../firmware/station/linux/solar_model.py) and compares it with a clean-panel baseline. Sun position is within 0.02° of pvlib; the remaining drift of about 8 % means it flags losses of roughly 10–15 % or more ([setup](uno-q-setup.md)). No real baseline exists yet, because the panel current is unusable.                |
| MCU to Linux data path                | Working (bring-up)                                                                               | `station` sends readings once per second over the Bridge to [`station_rx.py`](../firmware/station/linux/station_rx.py), which logs CSV, writes the latest reading for the dashboard and starts at boot from a user crontab ([demo runbook](demo-runbook.md)). No agreed message format document yet ([#22](https://github.com/B-AROL-O/hackturin-2026/issues/22)).                                                                                                 |
| Operator UI and maintenance output    | Dashboard working on the UNO Q; wider maintenance proposed                                       | Original/annotated image comparison, panel selection, shared inspection URLs, a live station strip (temperature, humidity, light, panel current, performance index) and delete / clear-all buttons, served by the board in Docker ([demo runbook](demo-runbook.md)). Home-page demo is labeled and never saved as inference. Detection-based review rules do not implement full maintenance or energy-loss prediction.                                             |
| STL enclosure concept                 | Not delivered                                                                                    | Planned for the pitch; no file committed.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Thermal imaging, hotspot detection    | Out of scope                                                                                     | Thermal camera unavailable; the phone RGB camera replaces it.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Pitch deck                            | Plan only                                                                                        | HTML deck not implemented ([presentation](../presentation/README.md)).                                                                                                                                                                                                                                                                                                                                                                                             |
| Demo video                            | 120-second film implemented; [published on YouTube](https://www.youtube.com/watch?v=iN8QtD9RLIk) | Remotion source, synthesized English narration, music and captions are in [`presentation/video`](../presentation/video/README.md), with [delivery checks](../presentation/video/review.md). Rendered MP4 files are build output and are not committed. The earlier kit stays in [`docs/video`](video/README.md).                                                                                                                                                   |

<!-- markdownlint-enable MD013 -->

## Phone-to-edge inspection

The FastAPI API, phone capture/upload page, SVG inspection dashboard, CPU OpenCV
adapter, and bounded local JPEG/JSON retention are implemented in `poopvolt/`.
The frontend is browser-ready static content packaged with the Python service;
it shares the backend URL. No independent frontend service is required.
The minimal dashboard now opens a labeled visual demo, showing an original sample
photo alongside an annotated view, with a PoopVolt SVG logo. Illustrative demo
annotations never enter the inference API or appear on uploaded photographs.

The PoopVolt model is not delivered yet. Until it is, the board runs a public
[off-the-shelf test model](../models/offtheshelf/README.md), a YOLOv8n solar
panel defect detector exported to ONNX. It proves the pipeline, not soiling
detection: it does not detect our staged soiling. The decoder supports the
explicit YOLOv8 detection contract documented in
[phone inspection setup](phone-inspection.md), and still needs aligning with the
team model's one-target `affected_panel` output. Inference stays unavailable
until a configured model passes a startup execution/shape check. No results are
mocked.

Software tests use a synthetic, untrained ONNX graph with real OpenCV 4.12;
they verify API/storage/decoder behavior, not trained-model accuracy. On
2026-10-11 the dashboard ran on the UNO Q in Docker and was tested from a Samsung
S23 Ultra over Wi-Fi, at about 0.8 s per photo with the test model
([demo runbook](demo-runbook.md)). Board benchmark measurements remain in
[UNO Q model budget](uno-q-model-budget.md).

## Built by the team during the hackathon

- Product concept, pitch narrative, architecture views and Coesa context in
  `docs/`.
- Arduino sketches in [`firmware/`](../firmware/README.md): `sensor_diag`,
  `station` and the `imu_bridge` placeholder.
- Station receiver, clear-sky sun model and panel performance index in
  `firmware/station/linux/`.
- Prototype wiring record and KiCad schematic in `hardware/`.
- SOLARMA importer, replay and the peer comparison with its tests in `poopvolt/` and `tests/`.
- Measurements of the UNO Q's resources.
- Phone inspection API, CPU ONNX adapter, local image store, UI, and software tests.
  Demo imagery/annotations are disclosed separately from model predictions.
- UNO Q dashboard with the live station strip, and the demo runbook.
- PoopVolt logo and [brand guidelines](../brand-guidelines.md).
- 120-second Remotion pitch film: scenes, captions, programmatic music and
  timing in `presentation/video/`.

## Pre-existing components

<!-- markdownlint-disable MD013 -->

| Component                                             | Role                                                                                  | Licence / note                                                                                       |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Arduino UNO Q, Zephyr core, `arduino-cli`, Bridge     | Board, toolchain and MCU to Linux link                                                | Arduino/Zephyr licences; see [setup](uno-q-setup.md)                                                 |
| Adafruit AHTX0 and PN532, Grove LCD libraries         | Sensor, NFC and display drivers used by sketches                                      | Upstream library licences, installed through `arduino-cli`                                           |
| Seeed Grove modules and Base Shield                   | Sensors, LCD, NFC reader                                                              | Commercial parts                                                                                     |
| SOLARMA `pv-analysis-tools` data (revision `fc96313`) | Historical inverter logs for replay                                                   | MIT; notice in [`data/solarma/NOTICE.md`](../data/solarma/NOTICE.md)                                 |
| OpenCV, NanoDet-Plus and YOLOX-S demos                | Preinstalled on the board / used only for timing                                      | Upstream licences; benchmark only, not shipped                                                       |
| KiCad, uv, pytest, Mermaid                            | Tooling                                                                               | Upstream licences                                                                                    |
| FastAPI                                               | Inspection API                                                                        | MIT                                                                                                  |
| Starlette, Uvicorn                                    | ASGI routing and HTTP server                                                          | BSD-3-Clause                                                                                         |
| python-multipart                                      | Bounded image-upload parsing                                                          | Apache-2.0                                                                                           |
| Pillow                                                | Image validation, orientation and JPEG normalization                                  | MIT-CMU (locked version)                                                                             |
| numpy, opencv-python-headless                         | Optional desktop test/runtime extra                                                   | BSD-3-Clause / Apache-2.0                                                                            |
| HTTPX, ONNX                                           | Development HTTP tests and synthetic graph fixtures only                              | BSD-3-Clause / Apache-2.0                                                                            |
| `mtahajawad/solar-panel-defect-detector` (YOLOv8n)    | Off-the-shelf test model, downloaded by `models/offtheshelf/export.sh`, not committed | MIT, as stated by its author                                                                         |
| Ultralytics                                           | Exports the test model to ONNX in `export.sh` only; not shipped                       | AGPL-3.0                                                                                             |
| Remotion 4.0.534, React                               | Pitch film rendering in `presentation/video/`                                         | Remotion License, free licence: non-commercial hackTurin 2026 project by a team of individuals / MIT |
| Kokoro v1.0, `kokoro-onnx` 0.4.7                      | Synthesized English narration of the pitch film                                       | Apache-2.0 / MIT; notices in `presentation/video/audio/`                                             |
| Source Sans 3                                         | Pitch film typeface                                                                   | SIL OFL 1.1; notice in `presentation/video/fonts/`                                                   |

<!-- markdownlint-enable MD013 -->

The repository is MIT licensed ([LICENSE](../LICENSE)). Any dependency added
later must be listed here with its licence.
