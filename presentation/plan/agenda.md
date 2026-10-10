# Proposed pitch agenda

Status: Documentation plan for the team's three-minute PoopVolt pitch. Audience
language: Italian. The budget includes software and STL demonstrations.
Narrative source: [Italian company-use story](../../docs/pitch-narrative.md).

## Main sequence

Open with the approved "Il tuo impianto è sporco di merda. Letteralmente" hook,
then ask how much contamination affects production. Explain how a photovoltaic
service company uses evidence to propose an intervention the owner can
understand and assess. Show the proposed comparison, STL, and one software case.
End with technician review and benefit verification. Coesa is a possible
counterpart; no partnership or guaranteed service conversion is claimed. The
free-device distribution remains an appendix hypothesis.

<!-- markdownlint-disable MD013 -->

| Slide | Stable ID      | Draft title                                      | Seconds | Purpose                                                                                    | Source IDs                                                      |
| ----- | -------------- | ------------------------------------------------ | ------- | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| 1     | `pv-title`     | Il tuo impianto è sporco di merda                | 25      | Deliver the approved hook and connect immediately to the production-impact question        | `pv-narrative`, `pv-pitch`                                      |
| 2     | `pv-problem`   | Come motivare un intervento al cliente?          | 25      | Explain the company's need for evidence a plant owner can understand and assess            | `pv-narrative`, `pv-soiling-background`, `coesa-energy-context` |
| 3     | `pv-pipeline`  | Dai dati a una proposta comprensibile            | 30      | Explain scoped expected/observed comparison as support for a justified company proposal    | `pv-narrative`, `pv-diagnostics`, `pv-data-plan`                |
| 4     | `pv-prototype` | Il concetto fisico di PoopVolt                   | 15      | Show the STL concept without presenting it as assembled or tested hardware                 | `pv-narrative`, `pv-hardware`                                   |
| 5     | `pv-evidence`  | Mostrare il problema, spiegare il prossimo passo | 40      | Show one software case and distinguish software output from a technician's proposed action | `pv-narrative`, `pv-data-plan`, `pv-flow-plant`                 |
| 6     | `pv-decision`  | Proporre, scegliere, verificare                  | 45      | Company explains options, owner assesses them, and comparable measurements verify benefit  | `pv-narrative`, `pv-maintenance`, `coesa-energy-context`        |

<!-- markdownlint-enable MD013 -->

Total: 180 seconds. The future checker compares IDs, order, and duration with
`talk.qmd`. Main IDs are slide anchors; source IDs resolve in the registry. The
new `pv-prototype` anchor identifies the STL segment. Removed main anchors are
not required by this revised plan; no deck implementation exists yet.

## Appendix

<!-- markdownlint-disable MD013 -->

| Stable ID         | Subject                                                                   | Canonical sources                                         |
| ----------------- | ------------------------------------------------------------------------- | --------------------------------------------------------- |
| `pv-a-deployment` | Secured parts, STL evidence, intended UNO Q, and unresolved integration   | `pv-deployment`, `pv-hardware`, `pv-narrative`            |
| `pv-a-components` | Local modules, theoretical-reference inputs, and unknown-data handling    | `pv-acquisition`, `pv-diagnostics`, `pv-maintenance`      |
| `pv-a-flows`      | Separate phone/replay paths, mapping, and intervention reassessment       | `pv-flow-soiling`, `pv-flow-plant`, `pv-flow-maintenance` |
| `pv-a-sources`    | SOLARMA limits, company offer hypothesis, provenance, and model decisions | `pv-data-plan`, `coesa-energy-context`, `pv-references`   |

<!-- markdownlint-enable MD013 -->

Appendix material does not extend the three-minute pitch. Update agenda,
speaking times, visuals, and validation together if the team changes the budget.
