# Visual and asset plan

Status: Proposed visuals for the three-minute owner story. Apply
[visual guidelines](../../.agent/visual-design.md) during implementation.

## Main visuals

<!-- markdownlint-disable MD013 -->

| Slide ID       | Primary visual                                                        | Source or provenance                                              | Visible qualification                                   |
| -------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| `pv-title`     | Older plant and the owner's question                                  | Original/licensed image and `pv-narrative`                        | Illustrative scene                                      |
| `pv-problem`   | Plant/string schematic with a subtle dust or pigeon cue               | `pv-narrative`, `pv-soiling-background`                           | Possible contributors; no established cause             |
| `pv-pipeline`  | Observed and expected production, same period and units               | `pv-diagnostics`, `pv-data-plan`                                  | Proposed reference; unknown inputs visible              |
| `pv-prototype` | STL viewport or labeled design export                                 | Team STL when supplied; `pv-hardware` for secured kit             | Design concept, not working hardware                    |
| `pv-evidence`  | One software comparison with asset scope and provenance               | Executed MVP evidence when linked; otherwise illustrative fixture | Measured, simulated, or replayed status; mapping limits |
| `pv-decision`  | Owner and technician review followed by intervention and reassessment | `pv-maintenance`, `coesa-energy-context`                          | Options to evaluate; benefit unmeasured                 |

<!-- markdownlint-enable MD013 -->

## Chart and evidence rules

Label the theoretical reference as estimated. Keep observed values, estimated
values, and illustrative values visually distinct with text and line patterns,
not color alone. Use common periods and units. Never fabricate a quantitative
gap. Show missing reference inputs as unavailable rather than drawing an
invented curve.

String labels require verified topology. An unknown mapping stays an inverter or
channel view. The SOLARMA replay has its own plant/time identity and lacks
populated irradiance; phone images cannot supply its missing weather baseline.

The pigeon cue explains the name and a possible inspection issue. It is not the
recurring protagonist. Keep phone RGB capture separate from electrical plots and
never represent RGB as measured thermal imagery.

## STL and hardware

Record the STL's filename, creator, revision, intended function, and actual
status when supplied. A viewport shows a proposed design, not proof of
fabrication. Use `pv-hardware` to distinguish secured parts, unavailable
equipment, and integration work. The phone replaces the unavailable thermal
camera for visible inspection.

## Appendix and asset acquisition

Use canonical Mermaid exports with parent IDs and proposed status. Put full
company distribution, local architecture, synchronization, and independent
phone/replay paths in the appendix when they exceed the main story.

Create `assets/README.md` during implementation with source, creator, license,
modifications, and intended use. Record data/figure generation and source
hashes. Phone capture provenance follows the
[data plan](../../docs/data-plan.md).

Economic figures require explicit inputs. No measured savings, recovered kWh,
accuracy, or conversion rate currently supports a benefit chart. The optional
comparison scenario has usable-input and missing-input states; both need a
complete static and print fallback.
