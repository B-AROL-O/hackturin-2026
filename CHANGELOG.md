# Changelog

<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the
project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.1.0 - 2026-10-11

First PoopVolt prototype from the hackTurin 2026 hackathon. See the
[project status](docs/project-status.md) for what works today and what remains
a proposal.

### Added

- SOLARMA inverter log importer: replay, unit and timestamp checks, and
  communication outage gaps (#54, #55).
- Peer-relative expected-versus-observed comparison on the SOLARMA replay, with
  [results](docs/comparison-results.md). It is a scoped demo, not the
  weather-adjusted model (#61).
- `station` sketch: solar panel current on A1 and readings streamed to Linux
  over the Bridge, received by `station_rx.py`.
- Hardware: solar path in the KiCad schematic, sensor wiring as CSV, bill of
  materials (#12) and a replication guide.
- Project status and reuse disclosure, readme sections and a Devpost
  description draft with submission checklist (#36, #39).

### Changed

- Company offer, architecture and pitch aligned with the owner narrative, the
  approved hook and the three-minute demo; the phone RGB camera replaces the
  thermal camera.
- Linter configurations for isort, Pylint, Ruff and Biome so the codebase
  passes super-linter v9.
- Copyright holder set to B-AROL-O Team, years 2026-2027.

## 0.0.1 - 2026-10-10

First tagged release of PoopVolt, built for HackTuring 2026.

### Added

- Python project skeleton managed with uv (package `poopvolt`).
- Firmware for the Arduino UNO Q: Grove sensor diagnostic, PN532 NFC fallback
  over shield UART, IMU bridge placeholder, and a station sketch exposing live
  readings as an NFC tag.
- Hardware documentation: prototype parts and substitutions, as-built wiring,
  editable KiCad schematic with verified exports, measured UNO Q storage, RAM
  and CPU budget.
- HTML pitch presentation draft, architecture, and CoESA evaluator context.
- Devcontainer with Claude Code, GitHub CLI, and a post-create script.

### Changed

- Replaced Poetry with uv in the devcontainer and docs.
- Super-linter runs only on pull requests to `main`.
