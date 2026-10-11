# Supplied video assets

Production decision (2026-10-11): the latest user direction requires the supplied
**original replay chart and canonical technical-insert colors**. That instruction
supersedes earlier brand-export requirements below. The film uses the original
chart unchanged, with local Source Sans 3 for external graphics. Both original
series are visible from the hard cut; external result labels appear together at
80 s. The chart stays completely still, including 85–93 s. See
[implementation](../implementation.md) for the implemented workflow.


Status: Local production media, prepared on 2026-10-11. Use the exact logo,
prototype photographs, electrical schematic, and replay chart in the film.
[manifest.json](manifest.json) records hashes, source revisions, modifications,
creator information, and rights status.

## Mandatory source media

<!-- markdownlint-disable MD013 -->

| Local asset                                                                                                          | Canonical source                                                                  | Scene / treatment                               |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------- |
| [Logo_PoopVolt.png](Logo_PoopVolt.png)                                                                               | [Original team logo](../../../assets/brand/Logo_PoopVolt.png)                     | V01 and V06, complete composition on white      |
| [prototype-bench-01.jpg](prototype-bench-01.jpg)                                                                     | [Existing photo](../../../docs/video/assets/prototype-bench-01.jpg)               | V04, wide prototype context                     |
| [prototype-bench-02.jpg](prototype-bench-02.jpg)                                                                     | [Existing photo](../../../docs/video/assets/prototype-bench-02.jpg)               | V04, complementary close view                   |
| [prototype-outdoor.jpg](prototype-outdoor.jpg)                                                                       | [Existing photo](../../../docs/video/assets/prototype-outdoor.jpg)                | V04, setup context with USB supply visible      |
| [pv-wiring.svg](pv-wiring.svg) / [PNG](pv-wiring.png)                                                                | [Canonical electrical export](../../../docs/architecture/diagrams/pv-wiring.svg)  | V04, full sheet and readable focused views      |
| [comparison-inverter-1-replayed.svg](comparison-inverter-1-replayed.svg) / [PNG](comparison-inverter-1-replayed.png) | [Canonical replay chart](../../../docs/images/comparison-inverter-1-replayed.svg) | V05, scoped result and eight-second static hold |

<!-- markdownlint-enable MD013 -->

Copies preserve original bytes. PNG versions of the technical SVGs are faithful
2400 px wide raster exports. SVGs are preferable when zooming. Keep original
photo colors and image aspect ratios. Their presence does not establish a
field-ready device, validated current under light, or an off-grid power test.

## Logo identity and provenance

Use the exact file requested by the user:
[Logo_PoopVolt.png on develop](https://github.com/B-AROL-O/hackturin-2026/blob/develop/assets/brand/Logo_PoopVolt.png).
Its immutable source revision and SHA-256 are recorded in the local manifest.
Use [brand-guidelines.md](../../../brand-guidelines.md) for the full composition,
white background, proportions, clear space, and prohibited alterations.

The team asset was supplied by GitHub user `fedenebu`. Its creator and
brand-specific permissions remain unconfirmed in
[the canonical brand asset record](../../../assets/brand/README.md). Do not infer
logo/trademark rights from the code's MIT license. This package preserves the
original; it does not create a transparent, recolored, monochrome, cropped, or
vector logo variant. A fade of the complete image is allowed; do not animate
its internal pigeon or panel cells.

The existing photos are repository-supplied prototype images. Their photographer
and explicit permissions were not recorded in the source folder. Retain this
status in the production provenance and record any subsequently supplied details.
Do not treat this metadata gap as a reason to omit the user-requested local
production assets; publication and third-party reuse should follow the actual
team rights record.

## Electrical scope and focus views

The electrical SVG is byte-identical to the current canonical KiCad export.
Its native source is
[hardware/poopvolt.kicad_sch](../../../hardware/poopvolt.kicad_sch); the
[connection record](../../../docs/hardware-connections.md) defines test scope.
The current sheet is A3, with viewBox `0 0 419.9890 297.0022`.

Follow the canonical 25-second schematic choreography: complete sheet for five
seconds, UNO Q/Grove focuses for ten, solar branch/A1 for seven, complete sheet
for three. Determine crop bounds from this current source, accounting for
captions and readable technical labels at 720p. Use several closely framed
regions if the whole Grove section is too dense. Preserve connection context
and use large external captions for the interfaces discussed.

The solar path is panel → current sensor → Waveshare → LiPo, with current input
on A1. UNO Q remains powered by USB; Waveshare USB OUT is unconnected. Current
zero is reported checked, while current under light still needs validation.
Do not add new wires, rewrite values, or recolor nets by hand. Electrical
changes start in KiCad and regenerate the canonical exports first.

## Historical replay scope

Use the canonical inverter-1 chart for **1 August–17 September 2019**.
Observed energy is **0 kWh**, with approximately **292 kWh expected from peers**.
Read [the comparison results](../../../docs/comparison-results.md) for the method
and limits. Keep axes, units, dates, legend, and historical-replay label visible.
Do not substitute the older Devpost card showing roughly 550 kWh over another
window. No recorded dirt/photo is causally paired with this historical replay.

The canonical chart is the content and geometry source. Brand migration must update
its generator, `poopvolt/report.py`, with an explicit export profile and verify
data unchanged. Retain the original default scientific export. The final video
uses a reviewed brand export with its own provenance/hash and the same parent
source ID; an initial animatic may use the supplied original. Do not make a new
curve by copying SVG path shapes or editing the SVG manually.

## Original explanatory illustrations

- [panel-rgb.svg](panel-rgb.svg) / [PNG](panel-rgb.png): the illustrative hook,
  with `panel-frame`, `panel-cells`, and independently revealable `deposit` groups.
- [pigeon.svg](pigeon.svg) / [PNG](pigeon.png): a transparent separate narrative
  illustration; not an official logo element or brand-mark replacement.
- [plant-owner.svg](plant-owner.svg) / [PNG](plant-owner.png): conceptual plant
  and owner setting, with room for a separate technician role.

These use only the selected brand palette. The panel canvas is 1200 × 760;
its rectangle is `x=180, y=135, width=840, height=490`. The deposit anchor is
`x=743, y=292`. Apply scale/crop transformations to callouts as well as artwork.
The drawings are original explanatory assets authored with Codex, under the
[repository MIT license](../../../LICENSE). They are not captured observations,
thermal measurements, inferred detections, or official brand variants.

## Reproduction and remaining production assets

[build_illustrations.py](build_illustrations.py) generates the original art,
copies the canonical logo/photos/figures unchanged, renders PNGs, and records
provenance. Run from the repository root with Python 3 and librsvg:

```sh
python3 presentation/video/assets/build_illustrations.py
```

Prepared with librsvg 2.61.2. SVG art and copied bytes are deterministic; PNG
rasterization may vary with tool/library versions. Deliberately refresh hashes
and inspect imagery after tool changes. Do not edit copied originals or PNGs.
The script performs no network requests.

Source Sans 3 fonts, final English narration, optional music/SFX, and aligned
captions remain production work. Record creator, source, acquisition date,
permitted use, modifications, and hashes for each addition. Rendering uses
locally staged media and should not fetch brand or image URLs at runtime.
