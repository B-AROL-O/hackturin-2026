# Content and evidence guidelines

## Narrative

Start with the operator's maintenance decision. Explain why electrical,
environmental, and image observations contribute different evidence. Show how
Acquisition validates those inputs, Diagnostics produces findings, and Maintenance
proposes an intervention for an operator to review.

Use a pigeon leaving droppings on a photovoltaic panel as the recurring narrative
device. Follow the same panel from visible contamination to an illustrative
thermal hotspot candidate, evidence assessment, and an operator's cleaning review.
Explain the proposed causal story as localized soiling, partial shading, and
possible localized heating. A visible deposit alone does not confirm a hotspot.
Introduce dust as a broader soiling example and hail as a separate physical-damage
example that calls for inspection. Do not claim that these are the most frequent
causes without supporting field data. Keep the pigeon story illustrative and
trace its background to the [source registry](../presentation/sources/README.md).

Use one clear claim per slide. Put reasoning, source details, and caveats in
speaker notes without hiding a limitation that changes the visible claim.
Use short declarative titles and concrete verbs. Avoid slogans, feature inventories,
unsupported superlatives, and repeating the pitch document verbatim.

The draft assumes an Italian hackathon pitch and English contributor documentation.
Treat language and the five-minute budget as adjustable planning assumptions.
Preserve module names, source titles, code identifiers, and diagram IDs. Define
Edge AI once as processing observations locally on the installation.

## Claim status

<!-- markdownlint-disable MD013 -->

| Status       | Required treatment                                                               |
| ------------ | -------------------------------------------------------------------------------- |
| Proposed     | Use intended behavior and visibly mark architecture or deployment as proposed    |
| Illustrative | Label a scenario, image overlay, chart, or UI example as illustrative            |
| Implemented  | Link to concrete code and describe its verified scope                            |
| Measured     | Cite a recorded evaluation with method, units, dataset or hardware, and revision |

<!-- markdownlint-enable MD013 -->

All current system views are proposed. The repository has no evidence of an
implemented sensor pipeline, trained model, live dashboard, or measured benefit.
Dataset entries identify candidates, not adopted models or validated coverage.
The intended UNO Q platform does not establish sensor compatibility or a working
MCU/Linux bridge. Consult the official sources before introducing specifications.

## Semantic guardrails

- Preserve Acquisition, Diagnostics, Maintenance, `Local storage`, and Operator interface.
- Distinguish soiling, thermal anomalies, electrical behavior, and degradation.
- Explain that degradation needs history and an environmental baseline.
- Show missing or unreliable input leading to inspection or a new observation.
- Keep cleaning, repairs, and replacement review under operator responsibility.
- Describe energy production, longer lifetime, and revamping avoidance as goals.
- Keep battery-aware scheduling and forecasting as future design work.
- Preserve the optional role of cloud services and the local processing boundary.

## Provenance

Use [the source registry](../presentation/sources/README.md) and its manifest to
trace slide claims to canonical pages. Update the registry when adding a source.
Record external URLs, retrieval dates, revisions where available, and asset rights.
Freeze measured reports with checksums before deriving quantitative figures.

Synthetic examples must carry their illustrative label both on the slide and in
the data record. Do not invent savings, accuracy, latency, energy yield, confidence
percentages, before/after improvements, or replacement thresholds.
Translate visible copy without changing the technical scope of the source.
