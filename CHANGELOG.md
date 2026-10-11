# Changelog

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the
project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.1.0 - 2026-10-11

First PoopVolt prototype from the hackTurin 2026 hackathon. See the
[project status](docs/project-status.md) for what works today and what remains
a proposal.

### Added

- `poopvolt` Python package managed with uv, with pytest tests.
- SOLARMA inverter log importer: replay, unit and timestamp checks, and
  communication outage gaps (#54, #55).
- Peer-relative expected-versus-observed comparison on the SOLARMA replay, with
  [results](docs/comparison-results.md). It is a scoped demo, not the
  weather-adjusted model (#61).
- Arduino UNO Q firmware: `sensor_diag` Grove sensor diagnostic with a PN532
  fallback over UART, `station` sketch showing readings on the LCD, as an NFC
  tag and streamed to Linux over the Bridge, and an `imu_bridge` placeholder.
- Solar panel current reading on A1 in the `station` sketch.
- Hardware records: as-built connections, wiring diagram, editable KiCad
  schematic with exports, bill of materials and a replication guide (#12).
- Measured UNO Q storage, RAM and CPU budget for a computer vision model.
- Product documentation: pitch narrative, proposed architecture views, company
  context, data plan, references, project status and reuse disclosure (#36,
  #40).
- Devpost description draft and submission checklist (#39).
- Presentation plan and agent guidelines for the HTML pitch (#43).
- Claude Code in the dev container (#50).

### Changed

- Super-linter runs only on pull requests to `main` (#52) and is now at v9.
- Linter configurations for isort, Pylint, Ruff and Biome so the codebase
  passes super-linter v9.
- Copyright holder set to B-AROL-O Team, years 2026-2027.

## 0.0.1 - 2026-10-10

Repository set up from the hackathon template, with the team readme and a uv
based dev container (#51).
