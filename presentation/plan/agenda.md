# Proposed pitch agenda

Status: Draft for hackathon judges and Coesa as a potential buyer/service partner.
Assumed duration: five minutes. Assumed audience language: Italian.
These defaults remain subject to the event's actual pitch requirements.

## Main sequence

Follow the pigeon story into a business offer: company buys the edge device,
owner receives it free, and evidence supports maintenance or revamping review.
Demonstrate phone-based single-string localization and independent whole-plant
telemetry replay. Keep capabilities proposed and simulations illustrative.

<!-- markdownlint-disable MD013 -->

| Slide | Stable ID       | Draft title                                          | Seconds | Purpose                                                                                              | Source IDs                                                                     |
| ----- | --------------- | ---------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 1     | `pv-title`      | PoopVolt                                             | 20      | Introduce the device sold to a company and offered free to its customers                             | `pv-pitch`                                                                     |
| 2     | `pv-problem`    | Un piccione, una stringa da controllare              | 35      | Explain localized soiling, lost-output risk, and possible hotspots without claiming confirmation     | `pv-pitch`, `pv-soiling-background`, `pv-hotspot-background`                   |
| 3     | `pv-context`    | L'azienda acquista, il cliente riceve il dispositivo | 30      | Establish Coesa as proposed buyer, owner as beneficiary, and technician responsibility               | `pv-context`, `coesa-energy-context`                                           |
| 4     | `pv-pipeline`   | Analisi locale, visibilità per l'azienda             | 45      | Explain edge modules, local history, queued sync, and company/customer views                         | `pv-architecture`, `pv-overview`                                               |
| 5     | `pv-quality`    | Una foto localizza lo sporco visibile                | 40      | Explain phone simulation, mapped string/panel, classification, region, and unknown-input branch      | `pv-acquisition`, `pv-flow-soiling`, `pv-data-plan`                            |
| 6     | `pv-evidence`   | Più canali raccontano la salute dell'impianto        | 45      | Explain independent SOLARMA replay, anomaly/trend analysis, and predictive-validation needs          | `pv-diagnostics`, `pv-flow-plant`, `pv-data-plan`, `solarma-pv-analysis-tools` |
| 7     | `pv-decision`   | Manutenzione o revamping: valutiamo il beneficio     | 40      | Compare options for the owner and show the company's evidence-to-service opportunity                 | `pv-maintenance`, `pv-flow-maintenance`, `pv-pitch`                            |
| 8     | `pv-validation` | Due percorsi da validare, un pilota da costruire     | 25      | Separate current docs/data from planned phone capture, edge inference, platform, and field economics | `pv-deployment`, `pv-index`, `pv-data-plan`                                    |
| 9     | `pv-close`      | Dal dato a un servizio utile al cliente              | 20      | Ask for a company-led pilot with channel access, intervention history, and commercial validation     | `pv-pitch`, `coesa-energy-context`                                             |

<!-- markdownlint-enable MD013 -->

Total: 300 seconds. The future checker compares IDs, order, and duration with
`talk.qmd`. Main IDs are slide anchors; source IDs resolve in the registry.
`pv-context` deliberately exists in both namespaces.

## Appendix

<!-- markdownlint-disable MD013 -->

| Stable ID         | Subject                                                                   | Canonical sources                                         |
| ----------------- | ------------------------------------------------------------------------- | --------------------------------------------------------- |
| `pv-a-deployment` | Intended UNO Q, phone transfer, logger coverage, synchronization          | `pv-deployment`, `pv-references`                          |
| `pv-a-components` | Full edge modules, localization limits, and economic inputs               | `pv-acquisition`, `pv-diagnostics`, `pv-maintenance`      |
| `pv-a-flows`      | Single-string, whole-plant, and owner-approved service sequences          | `pv-flow-soiling`, `pv-flow-plant`, `pv-flow-maintenance` |
| `pv-a-sources`    | SOLARMA inventory, phone capture plan, Coesa context, and evidence status | `pv-data-plan`, `coesa-energy-context`, `pv-references`   |

<!-- markdownlint-enable MD013 -->

Appendix material does not extend the main pitch. Preserve anchors; revise agenda
and speaking times together if the event requires a different duration.
