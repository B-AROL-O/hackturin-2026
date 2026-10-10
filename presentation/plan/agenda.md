# Proposed pitch agenda

Status: Documentation plan for the team's three-minute PoopVolt pitch. Audience
language: Italian. The budget includes software and STL demonstrations.
Narrative source: [Italian owner story](../../docs/pitch-narrative.md).

## Main sequence

Follow an owner of an older photovoltaic plant who cannot assess its
performance. Introduce the proposed expected/observed comparison, then the STL
concept and one software case. End with a technician-reviewed regeneration
assessment and post-intervention verification. Coesa is a possible service
counterpart. The existing free-device offer is an appendix hypothesis, not the
opening claim.

<!-- markdownlint-disable MD013 -->

| Slide | Stable ID      | Draft title                               | Seconds | Purpose                                                                                | Source IDs                                               |
| ----- | -------------- | ----------------------------------------- | ------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 1     | `pv-title`     | Il tuo impianto produce quanto dovrebbe?  | 25      | Introduce the owner and the apparently working older plant                             | `pv-narrative`, `pv-pitch`                               |
| 2     | `pv-problem`   | Funziona, ma non sai come rende           | 25      | Explain missing string visibility; dust, wear, and droppings are possible contributors | `pv-narrative`, `pv-soiling-background`                  |
| 3     | `pv-pipeline`  | Produzione attesa e osservata a confronto | 30      | Explain the proposed theoretical reference, compatible period, and mapped scope        | `pv-narrative`, `pv-diagnostics`, `pv-data-plan`         |
| 4     | `pv-prototype` | Il concetto fisico di PoopVolt            | 15      | Show the STL concept without presenting it as assembled or tested hardware             | `pv-narrative`, `pv-hardware`                            |
| 5     | `pv-evidence`  | Dal dato a una verifica concreta          | 40      | Show one actual software case or labeled simulation with provenance and limitations    | `pv-narrative`, `pv-data-plan`, `pv-flow-plant`          |
| 6     | `pv-decision`  | Dalla scoperta alla rigenerazione         | 45      | Explain owner/technician review, alternative interventions, and benefit verification   | `pv-narrative`, `pv-maintenance`, `coesa-energy-context` |

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
