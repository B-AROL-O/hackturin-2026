# Content and evidence guidelines

## Narrative

Start with the buyer and distribution model: sell the device to the service
company, which can offer it free to customers. Explain the owner's maintenance
and profitability question, then how Acquisition, Diagnostics, and Maintenance
support technician review and an owner-approved service proposal.

Use a pigeon leaving droppings on a photovoltaic panel as the recurring narrative
device. Follow the same panel from visible contamination to possible hotspot
risk, evidence assessment, and an operator's cleaning review.
Explain the proposed causal story as localized soiling, partial shading, and
possible localized heating. A visible deposit alone does not confirm a hotspot.
Use simulated dust/droppings in the phone RGB demonstration. Show historical
SOLARMA telemetry as an independent multi-channel path. Hail can remain appendix
background for physical-damage inspection. Do not claim cause frequency without
supporting field data. Keep the pigeon story illustrative and
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

Use the [hardware inventory](../docs/hardware.md) for reported availability:
UNO Q 4GB with Media Carrier, Seeed Studio Base Shield, sensors, LCD, and candidate
power parts are secured. The phone RGB camera replaces the unavailable Grove
thermal camera; thermal acquisition is deferred. Keep secured, selected, assembled,
and measured status distinct. Do not depict a thermal camera in the current demo
path or treat the AHT20/light sensor as thermal imaging.

## Semantic guardrails

- Preserve Acquisition, Diagnostics, Maintenance, `Local storage`, and Operator interface.
- Distinguish soiling, thermal anomalies, electrical behavior, and degradation.
- Explain that degradation needs history and an environmental baseline.
- Show missing or unreliable input leading to inspection or a new observation.
- Keep cleaning, repairs, and replacement review under operator responsibility.
- Describe production and profitability improvements as goals. Compare continued
  operation, maintenance, and revamping rather than prioritize avoidance.
- Keep battery-aware scheduling and forecasting as future design work.
- Preserve local operation during outages and the proposed company platform for
  remote portfolio views; remote freshness depends on synchronization.
- Keep phone RGB simulation separate from historical telemetry replay. Visible
  region, electrical channel, string, and panel locations are different scopes.
- No phone RGB hotspot confirmation, inferred lost kWh, or electrical continuity.
- Keep anomaly/trend detection distinct from validated future-failure prediction.
- Treat free-device distribution, service revenue, and revamping economics as
  hypotheses; disclose costs, baseline, input sources, and uncertainty.

## Provenance

Use [the source registry](../presentation/sources/README.md) and its manifest to
trace slide claims to canonical pages. Update the registry when adding a source.
Record external URLs, retrieval dates, revisions where available, and asset rights.
For reviewed uncommitted canonical bytes, record working-tree state, a null
revision/URL, base revision, and checksum. A base revision does not contain those
bytes; replace the provisional record with an immutable source revision when available.
Freeze measured reports with checksums before deriving quantitative figures.

Synthetic examples must carry their illustrative label both on the slide and in
the data record. Do not invent savings, accuracy, latency, energy yield, confidence
percentages, before/after improvements, or replacement thresholds.
Translate visible copy without changing the technical scope of the source.
