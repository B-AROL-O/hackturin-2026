# Implementation sequence

Status: Proposed backlog. This change implements the architecture documentation,
planning corpus, and source registry only.

Follow the [owner narrative](../../docs/pitch-narrative.md): an older plant,
unknown performance, proposed expected/observed comparison, STL concept,
software case, and regeneration review. Implement the static three-minute story
before enhancing the comparison scenario. Keep company distribution and separate
phone/replay sources as appendix context. Preserve the revised agenda's six
anchors.

## Ordered work

<!-- markdownlint-disable MD013 -->

| Step | Work                                                                               | Depends on    | Reviewable result and acceptance                                               |
| ---- | ---------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------ |
| P0   | Review audience language, time budget, evidence status, and visual direction       | Current draft | Updated agenda and accepted defaults recorded                                  |
| P1   | Add `talk.qmd`, `_quarto.yml`, initial theme, and local preview instructions       | P0            | Six stable main anchors, four appendix anchors, notes, one local render        |
| P2   | Render canonical diagrams and acquire local images and fonts with provenance       | P1            | Readable figures, recorded licenses, matching source hashes                    |
| P3   | Compose every slide and notes using the speaking and visual plans                  | P1, P2        | Complete static narrative, readable at 1280 by 720, 180-second budget          |
| P4   | Add reduced-motion handling, print/reading layouts, and optional scenario controls | P3            | Complete static fallback, usable keyboard controls, both scenario states       |
| P5   | Implement source, timing, rendered-link, and packaging checks                      | P3            | Meaningful failures for stale sources, duplicate anchors, missing dependencies |
| P6   | Build portable audience and presenter bundles                                      | P4, P5        | Local assets and references, audience notes absent, network-free HTTP preview  |
| P7   | Review all slides, rehearse, and choose hosting integration                        | P6            | Reviewed portable bundle and documented host/base-path choice                  |

<!-- markdownlint-enable MD013 -->

Complete a good static deck before adding the scenario enhancement. The scenario
is useful only if it makes evidence quality and operator review easier to
explain. The deck remains suitable for a pitch when that optional feature is
omitted.

## Rendering configuration to implement

Use a 1600 by 900 Reveal.js canvas, explicit slide level, linear navigation,
stable hashes, overview, speaker notes, visible controls, and a restrained
transition. Configure local theme and font resources. Avoid an automatic cover
that duplicates the explicitly authored `pv-title` slide.

Add presenter and audience profiles. Verify audience note exclusion in generated
HTML, rather than relying on CSS. Render Mermaid figures at build time and copy
all runtime dependencies locally. Do not reuse the reference's branding filter.
Record the exact tested Quarto and diagram-rendering versions in build guidance.

## Helpers to implement

<!-- markdownlint-disable MD013 -->

| Planned helper          | Contract                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `render_diagrams.py`    | Extract named canonical Mermaid blocks, render figures, retain text alternatives and provenance                           |
| `check_presentation.py` | Check manifest hashes, source IDs, main/appendix anchors, 180-second timing, local links, assets, and note-exclusion mode |
| `build_share.py`        | Package validated output with assets, fixture, and complete referenced documentation; verify copied links                 |

<!-- markdownlint-enable MD013 -->

A render-stage checker must inspect the generated HTML, not merely match strings
in the source. A packaging-stage check must inspect the portable bundle after
copying. Avoid hardcoding reference slide counts or deployment identifiers.

Future local build sequence: verify sources, generate figures, render the
selected profile, validate HTML, package, and serve the output over HTTP.
Detailed commands belong in the readme when the helpers exist. Quarto render by
itself will not establish that the planned portable packaging or source checks
are implemented.

## Product prototype work that can supply later evidence

These are proposed PoopVolt engineering steps, separate from the deck build.
Track implementation status against actual code and hardware artifacts.

Start from the [reported hardware inventory](../../docs/hardware.md). The UNO Q
4GB with Media Carrier, Seeed Studio Base Shield, sensors, LCD, and candidate
power components are secured. Use phone RGB instead of the unavailable thermal
camera. Use the Base Shield instead of the Grove shield v2 and HRS1358 instead
of the Waveshare charger. Breadboards are unavailable; confirm a connection plan
and required cables/adapters before assembly. Availability is not integration.

Before these supporting data paths, select and document the proposed theoretical
production reference, required plant/weather inputs, missing-data behavior,
comparison scope, and evaluation. Link actual MVP code and the STL artifact
before using them as implemented evidence. The inspected replay alone cannot
validate the expected-production model.

1. Pin the inspected SOLARMA revision and downloaded file hashes; implement a
   replay importer with units, missing values, observation time, and coverage.
2. Capture phone scenes with clean, simulated dust/droppings, and controls;
   annotate visible regions and declare demo plant/string/panel mapping.
3. Define scoped observation/finding contracts, source identity, topology, and
   retention. Keep phone simulation and historical plant data separate.
4. Select an initial visible-contamination detector and a telemetry anomaly
   baseline; evaluate separately on held-out capture sessions and time periods.
5. Verify secured-part interfaces, phone transfer, the local LCD status path,
   and device supply. Run the paths on the UNO Q and measure quality,
   localization scope, latency, memory, and power draw. Keep any small-panel
   sensor test distinct from phone simulation and historical replay.
6. Add maintenance review and intervention history, with explicit unknown inputs
   for economic scenarios and no unsupported hotspot/loss claim.
7. Prototype queued synchronization and company/own-plant views; test outages,
   freshness, duplicate records, and plant access boundaries.
8. Agree a field pilot with mapped logger channels, production/environment data,
   verified interventions, costs, and buyer/owner responsibilities.
9. Validate predictive maintenance using outcomes and a warning horizon;
   evaluate customer maintenance/revamping benefit and company free-device
   economics.

Thermal acquisition and confirmation are deferred because the thermal camera is
unavailable. Multi-year degradation needs separate measurements and validation.
Battery-aware scheduling is a later off-grid extension. A replay anomaly, phone
simulation, or mocked platform does not complete these steps. Only recorded
evaluations can supply measured presentation claims.

## Draft completion and implementation completion

This draft is complete when its links, timing, and provenance are consistent and
the proposed stack and work sequence are clear. A presentation implementation is
complete when the [validation criteria](../../.agent/validation.md) pass on the
portable bundle and the complete talk has been visually reviewed and rehearsed.
