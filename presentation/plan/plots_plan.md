# Visual and asset plan

Status: Proposed visuals. No images, figures, or charts have been produced.
Apply [visual guidelines](../../.agent/visual-design.md) when implementing.

## Main visuals

<!-- markdownlint-disable MD013 -->

| Slide ID        | Primary visual                                                   | Source or provenance                                             | Visible qualification                                     |
| --------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------- |
| `pv-title`      | One solar-panel image on a graphite title canvas                 | Original, licensed photograph, or labeled generated illustration | Proposed system in subtitle                               |
| `pv-problem`    | Panel contamination detail with a restrained annotation          | Verified image with rights, or clearly illustrative image        | No claimed production-loss value                          |
| `pv-context`    | Operator, installation, and PoopVolt boundary                    | Canonical `pv-context` diagram                                   | Proposed architecture                                     |
| `pv-pipeline`   | Horizontal edge flow and `Local storage` connection              | `pv-architecture` with canonical names                           | Proposed architecture, intended platform                  |
| `pv-quality`    | Valid observation contrasted with a missing or stale observation | `pv-acquisition` and `pv-flow-soiling`                           | Illustrative observations                                 |
| `pv-evidence`   | Aligned RGB, thermal, and electrical/history evidence groups     | `pv-diagnostics`; actual assets still needed                     | Illustrative modalities, history required for degradation |
| `pv-decision`   | Evidence, finding, recommendation, and operator review           | `pv-maintenance`, `pv-flow-maintenance`                          | Illustrative recommendation                               |
| `pv-validation` | Compact integration and evaluation roadmap                       | Open decisions in `pv-index` and `pv-deployment`                 | Work planned, results pending                             |
| `pv-close`      | Simple return to the operator decision loop                      | `pv-context` and `pv-maintenance`                                | Intended benefit                                          |

<!-- markdownlint-enable MD013 -->

## Canonical diagram exports

Build a full export from each Mermaid page used in the appendix. For the main
pitch, create concise excerpts from `pv-context`, `pv-architecture`, and the two
runtime flows. Export names should include the diagram ID. Label an excerpt as
a presentation view derived from its parent and explain omitted detail in notes.

The extraction tool should read the canonical fenced block, apply presentation
theme configuration, render a static asset, and retain a source hash. It should
fail if the page has no unique expected diagram. Keep the complete source and
diagram text available as a readable alternative in the bundled references.

Use consistent module positions across pipeline and decision slides. Emphasize
the stage being discussed with a label and optional short reveal. Avoid dense
nested diagrams on the main canvas. Put unverified physical interfaces in the
deployment appendix with their existing TBD status.

## Image and data acquisition

Create `assets/README.md` during implementation. For every image or font, record
its source, creator, license, retrieval date, modifications, and intended use.
Keep original rights information next to locally bundled assets. Sponsor listing
in the repository readme does not itself establish usable logo artwork or rights.

No quantitative results are currently available for a performance chart.
The first deck can use conceptual diagrams and illustrative observation examples.
Later plots require recorded data, units, evaluation scope, uncertainty, and
reproducible generation. Avoid decorative pseudo-charts and invented KPI tiles.

The optional scenario needs two fixture cases. Default to the static adequate
evidence view, with both cases rendered in the handout and print layout.
