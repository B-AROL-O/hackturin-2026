# Reference Index

Use this index to locate external documentation and datasets for PoopVolt. Each entry includes a stable identifier, a canonical URL, and retrieval keywords for AI agents and contributors.
Open the linked source before relying on hardware specifications, setup
instructions, or example code. External sources are linked rather than copied;
the company context entry also provides a dated local research summary.

## coesa-energy-context

- Title: Coesa Energy — evaluator context for PoopVolt
- Publisher of external sources: Coesa Energy / COESA Srl
- Canonical URL: <https://coesaenergy.it/>
- Local context: [Company research and source register](company/coesa-energy.md)
- Source type: Dated local synthesis of official company pages and
  company-authored posts, with separately labeled team analysis
- Researched on: 2026-10-10
- Language: English synthesis; primarily Italian source material
- Project relevance: Company identified by the user as evaluating our idea;
  background for PoopVolt's pitch and pilot design.
- Retrieve when: Preparing the Coesa pitch, comparing existing monitoring
  capabilities, or exploring company-funded devices, maintenance services,
  customer profitability, revamping, and later second-life/off-grid use cases.
- Search keywords: Coesa, COESA Srl, evaluator, hackTurin, Federico Sandrone,
  Matteo Stoppa, ESCo, EPC, O&M, KeepTheSun, JuaKit, SPARC, off-grid, soiling,
  predictive maintenance, circular economy, PoopVolt.
- Retrieval note: Start with the local context and its linked sources. Treat
  suggested product fit as hypotheses, and refresh changing company facts before
  external use.

## pv-data-plan

- Title: PoopVolt data and demonstration plan
- Local source: [Data plan](data-plan.md)
- Source type: Proposed ingestion/evaluation design and inspected external inventory
- Reviewed on: 2026-10-10
- Retrieve when: Planning phone capture, SOLARMA replay, string/channel mapping,
  anomaly evaluation, or predictive-maintenance data requirements.
- Search keywords: phone RGB, simulated dust, pigeon droppings, SOLARMA, string,
  inverter channel, provenance, localization, held-out evaluation, predictive maintenance.

## pv-hardware

- Title: PoopVolt hardware availability
- Local source: [Hardware inventory](hardware.md)
- Source type: Team-reported secured/unavailable parts and prototype substitutions
- Updated on: 2026-10-10
- Retrieve when: Planning prototype assembly or describing what hardware is available.
- Search keywords: UNO Q 4GB, Media Carrier, Seeed Studio Base Shield, AHT20,
  Light Sensor P v1.1, ACS70331, Grove LCD, LiPo, HRS1358, R1123, HAS4966,
  breadboards, Waveshare, phone RGB, unavailable thermal camera.
- Limits: Availability is reported by the team. Interfaces, power, assembly,
  phone transfer, and sensor acquisition are not validated by this inventory.

## solarma-pv-analysis-tools

- Title: PV analysis tools and SOLPEV inverter logs
- Publisher: SOLARMA snc
- Canonical URL: <https://github.com/SOLARMA/pv-analysis-tools>
- Inspected revision: `fc96313e453978fc89211322a8afb966b85f7913`
- Pinned data: <https://github.com/SOLARMA/pv-analysis-tools/tree/fc96313e453978fc89211322a8afb966b85f7913/data>
- Source type: Historical Danfoss Comlynx Weblogger exports and plotting notebook
- Inspected on: 2026-10-10, through GitHub API and raw files
- License: Repository-level MIT; retain the notice when reusing files.
- Project relevance: Proposed multi-channel/whole-plant replay source.
- Retrieve when: Building a telemetry importer or assessing inverter input coverage.
- Search keywords: SOLARMA, SOLPEV, Danfoss, Comlynx, details.txt, summary.txt,
  events.txt, inverter, DC channel, telemetry, historical replay.
- Limits: One plant, overlapping exports, no panel map or contamination/thermal
  labels, missing values, and empty irradiance fields in the larger summary.
  Event codes need interpretation. See the [data plan](data-plan.md) for the
  parsed inventory and evaluation constraints.

## arduino-uno-q-user-manual

The [hardware inventory](hardware.md) records the secured UNO Q 4GB with Media
Carrier and supporting parts. It is a team availability report, not a hardware
compatibility assessment. The phone RGB camera replaces the unavailable thermal
camera in the current prototype.

- Title: Arduino UNO Q User Manual
- Publisher: Arduino
- Canonical URL: <https://docs.arduino.cc/tutorials/uno-q/user-manual/>
- Source type: Official hardware documentation
- Language: English
- Project relevance: Reference for the Arduino UNO Q used as PoopVolt's Edge AI processing unit.
- Retrieve when: Investigating UNO Q hardware, board setup, interfaces, or integration constraints.
- Search keywords: Arduino, UNO Q, UNO Q 4GB, user manual, hardware, setup, sensors, Edge AI, PoopVolt.
- Retrieval note: Fetch the canonical URL when needed. If the page requires JavaScript, open it in a browser; do not infer specifications from this entry.

## arduino-uno-q-apps

- Title: Arduino Uno Q Apps
- Maintainer: akash73 on GitHub
- Canonical URL: <https://github.com/akash73/arduino-uno-q-apps>
- Source type: Community example application repository
- Language: English
- Project relevance: Implementation examples to explore when prototyping PoopVolt's UNO Q applications.
- Retrieve when: Looking for UNO Q object detection, monitoring, relay control, App Lab interfaces, or Linux-to-MCU communication examples.
- Search keywords: Arduino, UNO Q, apps, sketches, App Lab, Linux, MCU, RPC, object detection, monitoring, relay, Modulino, Edge AI, PoopVolt.
- Example directories: `detect-objects-to-sketch`, `monitor-example`, `4-relay-shield`, `4-relay-ui`, `double-bridge`, `rpc-call-buzz`.
- Retrieval note: Start with the repository readme, then inspect the relevant example directory and its hardware requirements. Record the commit SHA when referencing code so it can be retrieved reproducibly.

## Datasets

### roboflow-dusty-bird-droppings-v1

- Title: dusty and bird-droppings (solar-panel-soiling)
- Publisher: MRE Projects on Roboflow Universe
- Canonical URL: <https://universe.roboflow.com/mre-projects/dusty-and-bird-droppings-oeavs/dataset/1>
- Version: 1
- Task: Object detection
- License listed by source: CC BY 4.0
- Dataset size: 1,910 images in the generated version; 1,800 training, 60 validation, and 50 test images.
- Preprocessing: Auto-orientation and resize to 640 by 640 pixels with reflected-edge padding; training augmentation is included.
- Project relevance: Candidate data for detecting photovoltaic soiling and bird droppings.
- Search keywords: solar panel, photovoltaic, dust, bird droppings, pigeon excrement, soiling, contamination, object detection, Roboflow, PoopVolt.
- Retrieval note: Open the pinned version and choose an annotation export format. Inspect class labels and sample images before use; preserve version, split, preprocessing, and attribution metadata with the export.

### roboflow-solar-panel-dust-v2

- Title: solar panel dust detection
- Publisher: well done on Roboflow Universe
- Canonical URL: <https://universe.roboflow.com/well-done/solar-panel-dust-detection-7frc5/dataset/2>
- Version: 2
- Task: Object detection
- License listed by source: CC BY 4.0
- Dataset size: 1,899 images in the generated version; 1,662 training, 158 validation, and 79 test images.
- Preprocessing: Auto-orientation and stretch resize to 640 by 640 pixels; training augmentation is included.
- Project relevance: Candidate data for detecting dust contamination on photovoltaic panels.
- Search keywords: solar panel, photovoltaic, dust detection, soiling, contamination, object detection, Roboflow, PoopVolt.
- Retrieval note: Open the pinned version and choose an annotation export format. Inspect class labels and sample images before use; preserve version, split, preprocessing, and attribution metadata with the export.

### raptormaps-infrared-solar-modules

- Title: InfraredSolarModules
- Publisher: Raptor Maps
- Canonical URL: <https://github.com/RaptorMaps/InfraredSolarModules>
- Source type: Labeled infrared image dataset
- Task: Solar module anomaly classification
- License listed by repository: MIT
- Dataset size: 20,000 infrared images, each 24 by 40 pixels, across 12 classes: 11 anomaly classes and No-Anomaly.
- Project relevance: Candidate data for thermal anomaly classification, including hot spots, diode anomalies, shadowing, and soiling.
- Search keywords: infrared, thermal imaging, photovoltaic, solar module, anomaly classification, hot spot, diode, shadowing, soiling, Raptor Maps, PoopVolt.
- Retrieval note: Start with the readme, then retrieve `2020-02-14_InfraredSolarModules.zip`, which contains images and `module_metadata.json` labels. Record the repository commit SHA and archive checksum for reproducibility.
