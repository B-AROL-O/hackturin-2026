# Changelog

<!-- markdownlint-configure-file { "MD024": { "siblings_only": true } } -->

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the
project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.3.0 - 2026-10-15

Phone-to-edge inspection dashboard, the UNO Q station performance index, the
PoopVolt brand and the two-minute pitch film.

### Added

- Phone-to-edge inspection: a technician takes or picks a photo in the browser,
  the edge runs CPU-only OpenCV ONNX inference and saves the photo and
  detections (at most 100 inspections or 250 MiB). See the
  [phone inspection](docs/phone-inspection.md) guide (#73).
- Dashboard on the UNO Q: a live station strip (temperature, humidity, light,
  panel current, performance index), buttons to delete one inspection or clear
  all, and an off-the-shelf test model in `models/offtheshelf/` that is not
  trained for panel defects (#80).
- Relative panel performance index from a clear-sky sun model, computed on the
  Linux side and shown on the LCD and the NFC tag (#69).
- `station_rx.py` starts at boot, and the NFC text holds the dashboard
  address (#80, #83).
- [Demo runbook](docs/demo-runbook.md) for the UNO Q prototype (#80).
- PoopVolt logo and [brand guidelines](brand-guidelines.md) (#70).
- 120-second Remotion pitch film in `presentation/video/`, with English
  voice-over, music and captions. The pitch narrative now fits a two-minute
  video (#75, #79, #82).
- Prototype photos for the video (#72, #74).
- Field-test logs from 2026-10-11 in `data/field-2026-10-11/` (#76).
- Coesa mentor feedback and a refreshed Devpost draft (#71, #77).

### Changed

- The readme is shorter. Event information, quick links and sponsors are now
  in [docs/hackturin-2026.md](docs/hackturin-2026.md) (#83).
- Lint configuration updated so `develop` passes super-linter v9. The
  Remotion project is excluded (#81, #83).

### Fixed

- PN532 start-up is reliable (#69).
- Panel current below a 10 mA noise floor is reported as 0 (#69).
- NUL bytes left by board power loss are removed from the field logs (#76).
- Pitch film layout, captions and narration sync (#82).

## 0.2.0 - 2026-10-11

Material for the Devpost submission and the demo video.

### Added

- Demo video kit in [docs/video](docs/video/README.md): two-minute script with
  timeline and shot list, 1920x1080 cards and label overlays, English
  subtitles, a card build script and a read-only script that prints the
  comparison for the screen recording (#66).
- Chart of inverter 1 on the SOLARMA replay, the clearest replayed case (#66).
- Replayed improvement in the readme and the Devpost draft: inverter 1 produced
  nothing for 75 days, about 550 kWh short of its peers, and a daily peer check
  points at it on the first day (#64, #65).
- Beyond Solar requirements check in the Devpost draft (#64).

### Fixed

- The last date on the comparison charts' time axis was clipped (#66).
- Removed a dead seller link from the bill of materials (#65).

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
