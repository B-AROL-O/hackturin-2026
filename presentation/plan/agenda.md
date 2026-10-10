# Proposed pitch agenda

Status: Draft. Assumed audience: hackathon judges and potential technical partners.
Assumed duration: five minutes. Assumed audience language: Italian.
These defaults need confirmation against the actual pitch requirements.

## Main sequence

Follow one panel through the pigeon-droppings story: contamination, a suspected
thermal hotspot, evidence quality, and an operator's maintenance review.
Use dust and hail to widen the problem beyond the narrative device, distinguishing
soiling from physical damage. Keep all observations and outcomes illustrative.

<!-- markdownlint-disable MD013 -->

| Slide | Stable ID       | Draft title                                     | Seconds | Purpose                                                                               | Source IDs                                                                  |
| ----- | --------------- | ----------------------------------------------- | ------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 1     | `pv-title`      | PoopVolt                                        | 20      | Introduce local maintenance support for off-grid photovoltaics                        | `pv-pitch`                                                                  |
| 2     | `pv-problem`    | Dal piccione al sospetto hotspot                | 35      | Introduce pigeon droppings as the story device, then dust soiling and hail damage     | `pv-pitch`, `pv-diagnostics`, `pv-soiling-background`, `pv-hail-background` |
| 3     | `pv-context`    | L'operatore decide l'intervento                 | 30      | Establish the installation, system boundary, and human responsibility                 | `pv-context`                                                                |
| 4     | `pv-pipeline`   | PoopVolt elabora le osservazioni sul posto      | 45      | Explain the proposed acquisition, diagnostics, and maintenance flow                   | `pv-architecture`, `pv-overview`                                            |
| 5     | `pv-quality`    | Ogni osservazione porta anche la sua qualità    | 40      | Make validation, alignment, and missing inputs understandable                         | `pv-acquisition`, `pv-flow-soiling`                                         |
| 6     | `pv-evidence`   | La diagnosi combina evidenze diverse            | 45      | Compare deposit imagery with an illustrative hotspot; explain uncertainty and history | `pv-diagnostics`, `pv-hotspot-background`                                   |
| 7     | `pv-decision`   | La raccomandazione dipende dalle evidenze       | 40      | Compare an illustrative cleaning review with an inspection request                    | `pv-maintenance`, `pv-flow-maintenance`                                     |
| 8     | `pv-validation` | Il prototipo deve verificare la catena completa | 25      | Separate today's design from the next integration and evaluation work                 | `pv-deployment`, `pv-index`                                                 |
| 9     | `pv-close`      | La manutenzione parte da una scelta motivata    | 20      | Restate the goal and propose a concrete field-validation next step                    | `pv-pitch`, `pv-maintenance`                                                |

<!-- markdownlint-enable MD013 -->

Total: 300 seconds. The implementation checker should read this table and compare
IDs, order, and duration with `talk.qmd`. Main IDs are slide anchors, while source
IDs refer to the registry. `pv-context` names both the context source and its slide
intentionally. Keep those namespaces separate in the checker.

## Appendix

<!-- markdownlint-disable MD013 -->

| Stable ID         | Subject                                                               | Canonical sources                                    |
| ----------------- | --------------------------------------------------------------------- | ---------------------------------------------------- |
| `pv-a-deployment` | Intended UNO Q deployment and unresolved hardware interfaces          | `pv-deployment`, `pv-references`                     |
| `pv-a-components` | Full acquisition, diagnostics, and maintenance views                  | `pv-acquisition`, `pv-diagnostics`, `pv-maintenance` |
| `pv-a-flows`      | Soiling and operator maintenance runtime sequences                    | `pv-flow-soiling`, `pv-flow-maintenance`             |
| `pv-a-sources`    | Source registry, candidate datasets, and current evidence limitations | `pv-index`, `pv-references`                          |

<!-- markdownlint-enable MD013 -->

Appendix material is for questions and does not extend the five-minute pitch.
Avoid an automatic title slide or section dividers that silently increase the
main count. If the event requires another duration, revise this agenda and the
speaking plan together before authoring or rendering slides.
