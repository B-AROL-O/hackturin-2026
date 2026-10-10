# Visual and asset plan

Status: Proposed visuals. No images, figures, or charts have been produced.
Apply [visual guidelines](../../.agent/visual-design.md) when implementing.

## Main visuals

<!-- markdownlint-disable MD013 -->

| Slide ID        | Primary visual                                                                        | Source or provenance                                      | Visible qualification                             |
| --------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------- |
| `pv-title`      | Panel and restrained pigeon cue, with company-to-customer offer                       | Original/licensed image or labeled generated illustration | Proposed product                                  |
| `pv-problem`    | Deposit region on one panel; localized shading and possible heating relationship      | `pv-soiling-background`, `pv-hotspot-background`          | Mechanism illustration; no measured loss/hotspot  |
| `pv-context`    | Buyer, owner, technician, site device, and company platform                           | Canonical `pv-context`; `coesa-energy-context`            | Proposed free-device offer; no partnership        |
| `pv-pipeline`   | Edge flow, local history, queued sync, company/own-plant views                        | `pv-architecture`, `pv-overview`                          | Local operation; remote freshness depends on sync |
| `pv-quality`    | Phone RGB image, deposit region, declared string/panel map, unknown-input alternative | `pv-acquisition`, `pv-flow-soiling`, `pv-data-plan`       | Simulated capture; visible contamination only     |
| `pv-evidence`   | Separate telemetry pathway with channel coverage and history                          | `pv-diagnostics`, `pv-flow-plant`, pinned SOLARMA source  | Historical replay; mapping/prediction unverified  |
| `pv-decision`   | Continued operation, cleaning/repair, and revamping comparison with economic inputs   | `pv-maintenance`, `pv-flow-maintenance`                   | Illustrative options; no invented ROI             |
| `pv-validation` | Existing docs/logs versus planned phone, edge, platform, and field checks             | `pv-index`, `pv-deployment`, `pv-data-plan`               | Results pending                                   |
| `pv-close`      | Company pilot connecting observations, reviewed work, and reassessment                | `pv-pitch`, `coesa-energy-context`                        | Proposed pilot and intended benefit               |

<!-- markdownlint-enable MD013 -->

## Diagrams and imagery

Keep the same illustrative panel/deposit in the pigeon and phone-camera story.
Use readable string and panel labels, a mapping-status label, and an image-region
outline. Do not display phone RGB as a measured thermal view. If a thermal risk
illustration is used, keep it separate and explicitly illustrative.

Keep the historical SOLARMA plant visually separate from the phone scene. Any
real replay plot must come from pinned files with units, time range, device/input
identity, missing-data treatment, and reproducible generation. Do not rename
inverters as panels or show channels as verified strings.

Generate full canonical Mermaid exports for the appendix and concise main-deck
excerpts with parent diagram IDs, proposed status, and omission notes. Preserve
module names and boundaries, including the new company platform and sync path.
Technical figures use diagram/chart tools and retain source hashes.

## Image and data acquisition

Create `assets/README.md` during implementation with creator, source, license,
retrieval date, modifications, and intended use for every bundled asset.
Sponsor status does not establish logo rights. Phone captures record simulation
method and session provenance as defined in the [data plan](../../docs/data-plan.md).

No project performance results currently support a quantitative benefit chart.
Economic review can show required inputs and an unavailable estimate when inputs
are missing. Do not invent ROI, recovered kWh, accuracy, or service-margin values.

The optional phone scenario has usable-evidence and uncertain-input cases.
Render both in print/handout, retaining the simulated and illustrative labels.
