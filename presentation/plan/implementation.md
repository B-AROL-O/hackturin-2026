# Implementation sequence

Status: Proposed backlog. This change implements the architecture documentation,
planning corpus, and source registry only.

## Ordered work

<!-- markdownlint-disable MD013 -->

| Step | Work | Depends on | Reviewable result and acceptance |
| --- | --- | --- | --- |
| P0 | Review audience language, time budget, evidence status, and visual direction | Current draft | Updated agenda and accepted defaults recorded |
| P1 | Add `talk.qmd`, `_quarto.yml`, initial theme, and local preview instructions | P0 | Nine stable main anchors, four appendix anchors, notes, one local render |
| P2 | Render canonical diagrams and acquire local images and fonts with provenance | P1 | Readable figures, recorded licenses, matching source hashes |
| P3 | Compose every slide and notes using the speaking and visual plans | P1, P2 | Complete static narrative, readable at 1280 by 720, 300-second budget |
| P4 | Add reduced-motion handling, print/reading layouts, and optional scenario controls | P3 | Complete static fallback, usable keyboard controls, both scenario states |
| P5 | Implement source, timing, rendered-link, and packaging checks | P3 | Meaningful failures for stale sources, duplicate anchors, missing dependencies |
| P6 | Build portable audience and presenter bundles | P4, P5 | Local assets and references, audience notes absent, network-free HTTP preview |
| P7 | Review all slides, rehearse, and choose hosting integration | P6 | Reviewed portable bundle and documented host/base-path choice |

<!-- markdownlint-enable MD013 -->

Complete a good static deck before adding the scenario enhancement. The scenario
is useful only if it makes evidence quality and operator review easier to explain.
The deck remains suitable for a pitch when that optional feature is omitted.

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

| Planned helper | Contract |
| --- | --- |
| `render_diagrams.py` | Extract named canonical Mermaid blocks, render figures, retain text alternatives and provenance |
| `check_presentation.py` | Check manifest hashes, source IDs, main/appendix anchors, 300-second timing, local links, assets, and note-exclusion mode |
| `build_share.py` | Package validated output with assets, fixture, and complete referenced documentation; verify copied links |

<!-- markdownlint-enable MD013 -->

A render-stage checker must inspect the generated HTML, not merely match strings
in the source. A packaging-stage check must inspect the portable bundle after
copying. Avoid hard-coding reference slide counts or deployment identifiers.

Future local build sequence: verify sources, generate figures, render the selected
profile, validate HTML, package, and serve the output over HTTP. Detailed commands
belong in the README when the helpers exist. Quarto render by itself will not
establish that the planned portable packaging or source checks are implemented.

## Product prototype work that can supply later evidence

These are proposed PoopVolt engineering steps, separate from the deck build.
Track implementation status against actual code and hardware artifacts.

1. Select and verify sensors, cameras, power, and the MCU/Linux responsibilities.
2. Define observation units, timestamps, quality flags, alignment, and retention.
3. Implement acquisition and a replayable local observation record.
4. Evaluate an initial soiling detector on pinned data and installation samples.
5. Produce findings with evidence references and uncertainty handling.
6. Add a maintenance policy and operator intervention history.
7. Test the observation-to-recommendation chain, including missing/stale input.
8. Measure defined detection, latency, resource, and energy-use outcomes on the
   intended hardware, with a baseline and reproducible protocol.

Thermal fusion, long-term degradation forecasting, and battery-aware scheduling
need separate validation. A mocked UI or example dataset does not complete those
steps. Incorporate measured outcomes into the presentation only when the source
registry can link them to an evaluated implementation and recorded results.

## Draft completion and implementation completion

This draft is complete when its links, timing, and provenance are consistent and
the proposed stack and work sequence are clear. A presentation implementation is
complete when the [validation criteria](../../.agent/validation.md) pass on the
portable bundle and the complete talk has been visually reviewed and rehearsed.
