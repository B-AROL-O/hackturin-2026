# PoopVolt Architecture Index

This is the entry point for architectural questions about PoopVolt. The views follow a C4-inspired hierarchy with additional physical deployment and runtime views.
All views are proposed drafts. They describe intended behavior, not a verified implementation or measured performance.

The renewed proposal sells an edge device to a photovoltaic service company,
which can offer it free to customers. Local string-level observations and
multi-channel plant history support company maintenance services and customer
revamping assessments. A proposed company service platform adds portfolio views;
offline diagnostics remain local, while remote visibility requires synchronization.
Read the [pitch](../pitch-draft.md), [company context](../company/coesa-energy.md),
and [data plan](../data-plan.md) together with these views.

## Diagram Registry

| Diagram ID            | View                                                              | Scope                                                  |
| --------------------- | ----------------------------------------------------------------- | ------------------------------------------------------ |
| `pv-overview`         | [System overview](overview.md)                                    | Purpose, processing stages, and intended outcomes      |
| `pv-context`          | [System context](context.md)                                      | Operator, installation, and system boundary            |
| `pv-architecture`     | [Application architecture](architecture.md)                       | Application modules, storage, and information flow     |
| `pv-deployment`       | [Physical deployment](deployment.md)                              | Intended devices and execution environments            |
| `pv-acquisition`      | [Acquisition](components/acquisition.md)                          | Input normalization, quality checks, and alignment     |
| `pv-diagnostics`      | [Diagnostics](components/diagnostics.md)                          | Soiling, thermal, electrical, and degradation analysis |
| `pv-maintenance`      | [Maintenance](components/maintenance.md)                          | Evidence assessment and operator recommendations       |
| `pv-flow-soiling`     | [Soiling detection flow](flows/detect-soiling.md)                 | Observation-to-finding sequence                        |
| `pv-flow-maintenance` | [Maintenance recommendation flow](flows/recommend-maintenance.md) | Finding-to-intervention sequence                       |
| `pv-flow-plant`       | [Whole-plant monitoring flow](flows/monitor-plant.md)             | Multi-channel analysis, coverage, and synchronization  |

## How to Navigate

Start at the overview for project purpose, context for boundaries, or architecture for engineering work. Follow Parent links to zoom out and Related Views links to zoom in.
Deployment and runtime flows supplement the hierarchy; they are not deeper abstraction levels.
Implementation diagrams should be added only when concrete algorithms, interfaces, or state machines exist. Link those pages to actual code and their parent component.

## Diagram Conventions

- Keep one canonical Mermaid source per diagram in its Markdown page. Link from pitches and other documents; generate exports from that source.
- Preserve stable diagram IDs and component names across levels. Update this registry when a view is added or moved.
- State scope, status, and a text explanation on each page. Use proposed, partially implemented, or implemented status based on evidence.
- Label arrows with the information exchanged. Document protocols and hardware interfaces only once selected and verified.
- Keep each diagram within its stated abstraction level. Explain colors or symbols when they carry meaning.
- Update affected diagrams in the same change as architectural code or hardware changes.
- Before publishing, check Markdown formatting, Mermaid rendering, and relative links. Automated diagram and link checks are recommended future CI work; the current workflow is a general linter.

## Retrieval for AI Agents

Use the registry to select a view by scope or stable ID, then read its explanation and linked component pages. Treat proposed decisions as assumptions, not implementation facts.
Search terms: PoopVolt, Coesa, free customer device, Edge AI, Arduino UNO Q,
Acquisition, Diagnostics, Maintenance, string, inverter channel, SOLARMA,
phone camera, soiling, localization, predictive maintenance, revamping,
profitability, company platform, portfolio, synchronization, deployment.
Use the [reference index](../references.md) for hardware sources and dataset versions. Consult the canonical source before relying on specifications or example code.

## Open Decisions

- Field logger compatibility, channel/string topology, image-to-panel mapping,
  phone transfer, optional sensors, power, and MCU/Linux responsibilities.
- Observation contracts, retention, model selection, edge resource budget,
  evaluation labels, prediction horizon, and environmental baselines.
- Company platform technology, identity and plant access, transport, queue
  reconciliation, customer views, and Coesa integration opportunities.
- Device price and ownership, free-distribution economics, installation/support
  responsibility, pilot scope, intervention costs, and revamping assumptions.

The [data plan](../data-plan.md) identifies which demo data exist and which
additional measurements are needed. Battery-aware scheduling is a later off-grid
extension rather than a requirement of the primary commercial proposal.

## Method References

- [C4 diagram hierarchy](https://c4model.com/diagrams)
- [C4 deployment views](https://c4model.com/diagrams/deployment)
- [C4 runtime views](https://c4model.com/diagrams/dynamic)
