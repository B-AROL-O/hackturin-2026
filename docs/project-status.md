# PoopVolt project status and reuse disclosure

- Status: Snapshot of 2026-10-10, for the Devpost description and the pitch Q&A.
  Update it when a feature changes state.
- Scope: What the team built, what it reuses, and what works today. The
  architecture views in [docs/architecture/](architecture/README.md) stay
  proposals until the matching row below says "working".

## Working versus incomplete

<!-- markdownlint-disable MD013 -->

| Area                                | State                | Evidence and limits                                                                                                                                                      |
| ----------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Grove sensors, LCD, NFC on UNO Q    | Working (bring-up)   | AHT20, light sensor, 16x2 LCD and PN532 verified by the author in PR #49; see [wiring](hardware-connections.md). Light is relative, not calibrated irradiance.           |
| `station` firmware                  | Working (bring-up)   | Shows readings on the LCD and exposes them as an NFC tag text read by a phone ([setup](uno-q-setup.md)). Not yet fed by the Linux side.                                  |
| Electrical schematic                | Working              | Editable KiCad source with verified exports; shows the USB-powered prototype only ([hardware](../hardware/README.md)).                                                   |
| SOLARMA log importer                | Working              | [`poopvolt/solarma.py`](../poopvolt/solarma.py) parses the pinned export with tests. Irradiance is empty and string topology is unknown ([data plan](data-plan.md)).     |
| UNO Q compute budget                | Measured             | CPU-only inference figures in the [model budget](uno-q-model-budget.md); no PoopVolt model has been run yet.                                                             |
| Expected-vs-observed comparison     | Not implemented      | Model, inputs and uncertainty are undecided. Use a labelled simulation in any demo.                                                                                      |
| RGB soiling detection (phone image) | Not implemented      | No trained model, labelled photo set or phone-to-board transfer yet.                                                                                                     |
| Current sensor (ACS70331), power chain | Not integrated    | Secured but not wired; panel, charger, battery and converter untested ([hardware](hardware.md)).                                                                         |
| MCU to Linux data path              | Not implemented      | The Bridge link exists on the board; no PoopVolt message format yet.                                                                                                     |
| Operator UI and maintenance output  | Not implemented      | Proposed in the [architecture](architecture/README.md).                                                                                                                  |
| STL enclosure concept               | Not delivered        | Planned for the pitch; no file committed.                                                                                                                                |
| Thermal imaging, hotspot detection  | Out of scope         | Thermal camera unavailable; the phone RGB camera replaces it.                                                                                                            |
| Pitch deck                          | Plan only            | HTML deck not implemented ([presentation](../presentation/README.md)).                                                                                                   |

<!-- markdownlint-enable MD013 -->

## Built by the team during the hackathon

- Product concept, pitch narrative, architecture views and Coesa context in
  `docs/`.
- Arduino sketches in [`firmware/`](../firmware/README.md): `sensor_diag`,
  `station` and the `imu_bridge` placeholder.
- Prototype wiring record and KiCad schematic in `hardware/`.
- SOLARMA importer and its tests in `poopvolt/` and `tests/`.
- Measurements of the UNO Q's resources.

## Pre-existing components

<!-- markdownlint-disable MD013 -->

| Component                                            | Role                                                | Licence / note                                                            |
| ---------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------- |
| Arduino UNO Q, Zephyr core, `arduino-cli`, Bridge    | Board, toolchain and MCU to Linux link              | Arduino/Zephyr licences; see [setup](uno-q-setup.md)                      |
| Adafruit AHTX0 and PN532, Grove LCD libraries        | Sensor, NFC and display drivers used by sketches    | Upstream library licences, installed through `arduino-cli`                |
| Seeed Grove modules and Base Shield                  | Sensors, LCD, NFC reader                            | Commercial parts                                                          |
| SOLARMA `pv-analysis-tools` data (revision `fc96313`) | Historical inverter logs for replay                | MIT; notice in [`data/solarma/NOTICE.md`](../data/solarma/NOTICE.md)      |
| OpenCV, NanoDet-Plus and YOLOX-S demos              | Preinstalled on the board / used only for timing    | Upstream licences; benchmark only, not shipped                            |
| KiCad, uv, pytest, Mermaid                          | Tooling                                             | Upstream licences                                                         |

<!-- markdownlint-enable MD013 -->

The repository is MIT licensed ([LICENSE](../LICENSE)). Any dependency added
later must be listed here with its licence.
