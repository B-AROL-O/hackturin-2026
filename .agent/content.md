# Content and evidence guidelines

## Narrative

Use the [Italian owner story](../docs/pitch-narrative.md) as the canonical
spoken brief. Begin with an older plant that still produces but whose owner
cannot assess performance. Follow problem, proposed expected/observed
comparison, STL concept, one software case, and technician-reviewed
regeneration.

The main pitch is six slides and 180 seconds including demonstrations. Do not
open with the company sales/free-device offer; it remains a commercial
hypothesis for supporting discussion or the appendix. Coesa is a possible
service counterpart, not an established partner. Define Edge AI only if needed.

Pigeon droppings explain the name and a possible contributor alongside dust and
wear. A visible deposit or compromised cell does not prove a measured
whole-string loss. Use the
[background registry](../presentation/sources/README.md) for mechanisms, not
cause frequency or project-performance claims.

The theoretical production model is proposed. Its inputs, implementation,
uncertainty, and validation are unresolved. The expected/observed comparison
needs matching period, units, operating conditions, and verified scope. Missing
inputs produce unavailable or limited conclusions, not invented estimates. A
deviation is not historical degradation, a diagnosis, or guaranteed recovery.

Use one clear claim per slide. Put source detail and reasoning in notes without
hiding limitations that change the claim. Keep Italian audience copy and English
contributor documentation, stable retained anchors, and canonical module/diagram
IDs.

## Claim status

<!-- markdownlint-disable MD013 -->

| Status       | Required treatment                                                            |
| ------------ | ----------------------------------------------------------------------------- |
| Proposed     | Use intended behavior and visibly label unimplemented architecture and models |
| Illustrative | Label scenarios, simulations, design overlays, and UI examples                |
| Implemented  | Link concrete code or artifact and describe its verified scope                |
| Measured     | Cite a recorded test with method, units, data/hardware, and revision          |

<!-- markdownlint-enable MD013 -->

This PR supplies documentation, not an MVP implementation or STL artifact.
Complete the demo from actual team evidence. If code, model, or mapped string
outputs are absent, narrow the claim or show a clearly labeled simulation.

The [hardware inventory](../docs/hardware.md) records secured parts and the
phone replacement for the unavailable thermal camera. Secured, selected,
assembled, and measured are different states. The STL is a physical design
concept until fabrication and operation are verified.

## Semantic guardrails

- Preserve Acquisition, Diagnostics, Maintenance, `Local storage`, and Operator
  interface.
- Distinguish power, energy, environmental input, estimated reference, and
  observed data.
- Use string labels only with verified topology; otherwise show device/channel
  scope.
- Keep phone RGB simulation and SOLARMA replay independent.
- RGB does not confirm hotspots, electrical interruption, or lost kWh.
- Degradation needs comparable history; anomaly detection is not validated
  forecasting.
- Cleaning is an option for dirt; replacement and revamping require technical
  review.
- Owners choose interventions after technician review; do not guarantee a
  service request.
- Compare continued operation, cleaning/repair, and regeneration without
  invented ROI.
- Verify post-intervention benefit under comparable conditions; full gap
  recovery is not assured.
- Keep local operation, queued synchronization, and remote freshness as proposed
  responsibilities.
- Commercial distribution, predictive maintenance, and battery scheduling remain
  hypotheses or future work.

## Provenance

Use the [source registry](../presentation/sources/README.md) and manifest.
Record source state, revision, checksum, and asset rights. Uncommitted reviewed
bytes require working-tree state, null revision/URL, and a base revision.
Replace provisional records with immutable revisions when committed.

Record the actual MVP code, execution, dataset, and STL source when supplied. Do
not infer their existence from planned filenames. Synthetic examples carry an
illustrative label both visibly and in their data records. Do not invent
recovered kWh, accuracy, latency, confidence, savings, or thresholds.
