# Visual and asset plan

Status: Proposed motion graphics storyboard for the two-minute company-use
pitch. Existing wiring and replay exports are available; the new video,
illustrations, overlays, and HTML deck have not been produced. Apply
[visual guidelines](../../.agent/visual-design.md).

The [Remotion handoff](../video/README.md) now supplies brand-aligned illustrative
assets and faithful local copies of the existing logo, three prototype photos,
electrical schematic, and replay chart. Its
[asset inventory](../video/assets/README.md) and [storyboard](../video/storyboard.md)
assign each to the same six beats. Audio and animated scenes remain future work.

## Main visuals

<!-- markdownlint-disable MD013 -->

| Scene ID       | Primary visual                                     | Source or provenance                     | Visible qualification                               |
| -------------- | -------------------------------------------------- | ---------------------------------------- | --------------------------------------------------- |
| `pv-title`     | Typographic hook, panel, restrained pigeon cue     | Original illustration and `pv-narrative` | Illustrative scene                                  |
| `pv-problem`   | Same installation with owner and technician        | `pv-narrative`, `pv-pitch`               | Question, no established cause                      |
| `pv-pipeline`  | Comparison labels and deviation-to-inspection flow | `pv-comparison`, `pv-data-plan`          | Peer comparison available; theoretical model future |
| `pv-prototype` | Full electrical schematic with two focused views   | `pv-wiring`, `pv-wiring-svg`             | Prototype; USB supply; current-under-light pending  |
| `pv-evidence`  | Original inverter 1 chart and inspection flag      | `pv-comparison`, `pv-comparison-chart`   | Historical replay, period, units, inverter scope    |
| `pv-decision`  | Technician, owner, four-step review sequence       | `pv-narrative`, `pv-maintenance`         | Proposed workflow; benefit unmeasured               |

<!-- markdownlint-enable MD013 -->

## Motion and timing

Use the exact scene cues in the [script](../../docs/pitch-narrative.md), on a
1920 × 1080 video canvas. Keep role positions stable and use the brand's dark
blue, solar yellow, white, and greys. Prefer short entrances, highlights, and
200–300 ms transitions; hold each composition while it is read.

The 25-second wiring scene uses 5 seconds for the full sheet, 10 seconds for UNO
Q/Grove interfaces, 7 seconds for the solar branch and A1, and 3 seconds for the
complete sheet. Ensure labels are readable in the close views. Overlay outlines
and captions without altering the canonical export. Never draw a power
connection from Waveshare USB OUT to UNO Q: it is not connected.

Keep the replay chart static for at least eight seconds, with axes, legend,
period, source, and units continuously visible. Cut between hardware and replay
rather than morphing one into the other. The final logo/message hold occupies
the last three seconds; it does not extend the 120-second budget.

## Evidence and asset rules

Use the existing `pv-wiring` SVG/PDF generated from
[`hardware/poopvolt.kicad_sch`](../../hardware/poopvolt.kicad_sch). Crops retain
the parent diagram ID and connection semantics; electrical edits must follow the
[KiCad export workflow](../../docs/hardware-connections.md).

Use the original inverter 1 chart from the
[comparison results](../../docs/comparison-results.md). Do not redraw its data,
animate KPI counts, invent a theoretical curve, or show a recovered-energy plot.
The replay is not prototype telemetry, a mapped-string result, or a diagnosis.

An STL concept can join appendix material only when its actual file and function
are supplied. Phone RGB, soiling detection, theoretical modeling, and measured
field benefits must retain their own source and implementation status.

Record creator, source, rights, modifications, and intended use for new assets.
Keep subtitles synchronized with the final cut. The existing English Devpost
cards and subtitles remain separate; do not label them as this Italian video's
finished assets. HTML adaptations must provide complete static content, reduced
motion, and readable print output.
