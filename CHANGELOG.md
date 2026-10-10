# Changelog

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
