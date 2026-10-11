# PoopVolt Architecture Index

This is the entry point for architectural questions about PoopVolt. The views
follow a C4-inspired hierarchy with additional physical deployment and runtime
views. The system-design views are proposed drafts. They describe intended
behavior, not a verified implementation or measured performance. The
[phone inspection implementation](phone-inspection.md) records the implemented
software slice; its trained model and UNO Q validation are pending.

The [two-minute owner narrative](../pitch-narrative.md) starts with an older
plant whose performance is unclear to its owner. It proposes an
expected/observed comparison, separating an available historical peer replay
from a future theoretical reference. It shows the prototype electrical schematic
in a dedicated motion graphics scene. The theoretical model, required inputs,
and string mapping remain unverified; see the data plan and scoped comparison
results before making quantitative claims.

The secondary commercial proposal sells an edge device to a photovoltaic service
company, which can offer it free to customers. Local string-level observations
and multi-channel plant history support company maintenance services and
customer revamping assessments. A proposed company service platform adds
portfolio views; offline diagnostics remain local, while remote visibility
requires synchronization. Read the [pitch](../pitch-draft.md),
[company context](../company/coesa-energy.md), and [data plan](../data-plan.md)
together with these views.

The [hardware inventory](../hardware.md) records the secured UNO Q 4GB with
Media Carrier, Seeed Studio Base Shield, sensors, LCD, and candidate power
components. The current prototype uses a phone RGB camera in place of the
unavailable Grove thermal camera. Thermal acquisition is deferred; hardware
availability does not establish tested integration. The electrical wiring view
separately records the prototype connections reported in PR #49.

## Diagram Registry

<!-- markdownlint-disable MD013 -->

| Diagram ID            | View                                                              | Scope                                                                 |
| --------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| `pv-overview`         | [System overview](overview.md)                                    | Purpose, processing stages, and intended outcomes                     |
| `pv-context`          | [System context](context.md)                                      | Operator, installation, and system boundary                           |
| `pv-architecture`     | [Application architecture](architecture.md)                       | Application modules, storage, and information flow                    |
| `pv-deployment`       | [Physical deployment](deployment.md)                              | Intended devices and execution environments                           |
| `pv-wiring`           | [Prototype electrical wiring](../hardware-connections.md)         | As-built USB power, Grove ports, and module pinouts                   |
| `pv-acquisition`      | [Acquisition](components/acquisition.md)                          | Input normalization, quality checks, and alignment                    |
| `pv-diagnostics`      | [Diagnostics](components/diagnostics.md)                          | Soiling, thermal, electrical, and degradation analysis                |
| `pv-maintenance`      | [Maintenance](components/maintenance.md)                          | Evidence assessment and operator recommendations                      |
| `pv-flow-soiling`     | [Soiling detection flow](flows/detect-soiling.md)                 | Observation-to-finding sequence                                       |
| `pv-flow-maintenance` | [Maintenance recommendation flow](flows/recommend-maintenance.md) | Finding-to-intervention sequence                                      |
| `pv-flow-plant`       | [Whole-plant monitoring flow](flows/monitor-plant.md)             | Multi-channel analysis, coverage, and synchronization                 |
| `pv-phone-inspection` | [Phone inspection implementation](phone-inspection.md)            | Implemented HTTP upload, CPU inference adapter, storage and dashboard |

<!-- markdownlint-enable MD013 -->

## How to Navigate

Start at the overview for project purpose, context for boundaries, or
architecture for engineering work. Follow Parent links to zoom out and Related
Views links to zoom in. Deployment and runtime flows supplement the hierarchy;
they are not deeper abstraction levels. Implementation diagrams should be added
only when concrete algorithms, interfaces, or state machines exist. Link those
pages to actual code and their parent component.

## Diagram Conventions

- Keep one canonical Mermaid source per logical diagram in its Markdown page.
  The electrical schematic `pv-wiring` uses the native
  [`hardware/poopvolt.kicad_sch`](../../hardware/poopvolt.kicad_sch) source
  instead; regenerate its exports with the documented KiCad workflow. Link from
  pitches and other documents; do not edit generated exports independently.
- Preserve stable diagram IDs and component names across levels. Update this
  registry when a view is added or moved.
- State scope, status, and a text explanation on each page. Use proposed,
  partially implemented, or implemented status based on evidence.
- Label arrows with the information exchanged. Document protocols and hardware
  interfaces only once selected and verified.
- Keep each diagram within its stated abstraction level. Explain colors or
  symbols when they carry meaning.
- Update affected diagrams in the same change as architectural code or hardware
  changes.
- Before publishing, check Markdown formatting, Mermaid rendering, and relative
  links. Automated diagram and link checks are recommended future CI work; the
  current workflow is a general linter.

## Retrieval for AI Agents

Use the registry to select a view by scope or stable ID, then read its
explanation and linked component pages. Treat proposed decisions as assumptions,
not implementation facts. Search terms: PoopVolt, Coesa, free customer device,
Edge AI, Arduino UNO Q, Acquisition, Diagnostics, Maintenance, string, inverter
channel, SOLARMA, phone camera, soiling, localization, predictive maintenance,
revamping, profitability, company platform, portfolio, synchronization,
deployment. Use the [reference index](../references.md) for hardware sources and
dataset versions. Consult the canonical source before relying on specifications
or example code.

## Open Decisions

The [prototype wiring](../hardware-connections.md) records selected and
reported-tested sensor/display interfaces.

- Field logger compatibility, channel/string topology, image-to-panel mapping,
  phone transfer, secured-part interfaces, power, and MCU/Linux
  responsibilities.
- Theoretical expected-production reference, plant metadata, weather inputs,
  reference uncertainty, matched periods, and independent validation.
- Observation contracts, retention, model selection, edge resource budget,
  evaluation labels, prediction horizon, and environmental baselines.
- Company platform technology, identity and plant access, transport, queue
  reconciliation, customer views, and Coesa integration opportunities.
- Device price and ownership, free-distribution economics, installation/support
  responsibility, pilot scope, intervention costs, and revamping assumptions.

The [data plan](../data-plan.md) identifies which demo data exist and which
additional measurements are needed. Battery-aware scheduling is a later off-grid
extension rather than a requirement of the primary commercial proposal.

Phone inspection selects LAN HTTP operator access and bounded JPEG/JSON
retention for that software slice. Secure deployment, wider-system storage,
trained-model evaluation and plant/string mapping still need validation.

## Method References

- [C4 diagram hierarchy](https://c4model.com/diagrams)
- [C4 deployment views](https://c4model.com/diagrams/deployment)
- [C4 runtime views](https://c4model.com/diagrams/dynamic)
