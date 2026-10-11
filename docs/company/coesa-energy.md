# Coesa Energy — evaluator context for PoopVolt

- Document ID: `coesa-energy-context`
- Entity: Coesa Energy / COESA Srl, Torino, Italy
- Official site: <https://coesaenergy.it/>
- Researched on: 2026-10-10
- Language: English summary of primarily Italian sources
- Purpose: Give contributors and AI models retrievable company context when
  developing or pitching PoopVolt for hackTurin 2026.
- Retrieval keywords: Coesa, COESA Srl, Coesa Energy, evaluator, judge,
  hackTurin, Federico Sandrone, Matteo Stoppa, ESCo, EPC, O&M, photovoltaic,
  fotovoltaico, predictive maintenance, manutenzione predittiva, soiling,
  off-grid, KeepTheSun, Keep The Sun, JuaKit, SPARC, circular economy, economia
  circolare, second-life panels, PoopVolt.

## How to use this document

Read the company facts and existing capabilities before suggesting product
positioning. The PoopVolt fit and evaluation suggestions below are **team
analysis**, not statements of Coesa's requirements or an official judging
rubric. The user identifies Coesa as the company evaluating our idea; public
evidence separately confirms its sponsorship of hackTurin.

This Markdown document contains a local summary suitable for text indexing or
retrieval. Each factual section links its sources, and the source register
records access limitations. Refresh changing information before using it in a
final pitch. For the project's proposed capabilities, read the
[pitch](../pitch-draft.md) and [architecture](../architecture/README.md); those
documents describe goals, not evidence of completed validation.

## Company identity and business

COESA Srl is a Turin-based energy services and engineering company, founded in
2012 by Dario Costanzo and Federico Sandrone. It describes itself as an Energy
Service Company (ESCo) operating as an Engineering, Procurement and Construction
(EPC) contractor. Its customers include businesses, public administrations,
condominiums and third-sector organizations. It reports a separate engineering
spin-off, COESA Engineering Srl, established in 2019. Its registered site
details identify Via Beaumont 7, 10143 Torino, and VAT/tax code 10734760019.
[Company overview](https://coesaenergy.it/chi-siamo/).

Its offer covers industrial photovoltaics, utility-scale solar, renewable energy
communities (CER), and building energy efficiency. It coordinates analysis,
permits, design, incentives, installation, commissioning and ongoing support.
The homepage reports 25 MW installed, 136 municipalities served and 330
condominiums/third-sector organizations made more efficient. These are
company-published counters observed during research, with no common measurement
period established here. [Official homepage](https://coesaenergy.it/).

The public-administration service page lists ESCo UNI 11352, ISO 9001, ISO
14001, ISO 45001 and SOA credentials. This document records company disclosures;
it does not independently establish certificate scope or expiry.
[Public-administration services](https://coesaenergy.it/efficientamento-energetico/efficientamento-energetico-pubblica-amministrazione/).

## Commercial model and existing maintenance services

Coesa advertises three industrial solar arrangements: direct purchase, a
long-term fixed-price PPA, and PPA Easy with a fixed rental payment and a
purchase option. Its offer includes app access, continuous performance
monitoring, scheduled and extraordinary maintenance. Its stated Operations and
Maintenance service explicitly includes panel washing, efficiency monitoring and
replacement of underperforming modules.
[Industrial photovoltaic services](https://coesaenergy.it/fotovoltaico/fotovoltaico-per-imprese/).

**Team interpretation:** Maintenance recommendations could support an existing
service activity. A pilot should establish who pays, who acts on an alert, and
whether the recovered energy and avoided visits cover hardware, installation and
support costs. Integration options remain unverified; the sources do not
establish available APIs or protocols.

## Existing monitoring perspective

Coesa's monitoring article discusses IoT sensing, inverter connections, local
analysis before cloud communication, machine learning, dashboards and predictive
maintenance. It identifies soiling, module mismatch, hotspots and degradation as
operational concerns. It also describes connectivity, cybersecurity, skills,
equipment expense and monitoring-system power consumption as constraints,
particularly for small installations. This is an explanatory company article; it
does not prove deployment of every described feature in a Coesa product.
[Monitoring article](https://coesaenergy.it/sistemi-di-monitoraggio/).

**Team interpretation:** Generic sensor collection, AI dashboards and predictive
maintenance will need a clear comparison with existing approaches. PoopVolt
should demonstrate a specific improvement, such as a useful local maintenance
decision during a connectivity outage, with measured device cost and power draw.
Do not assert that Coesa's current systems require continuous cloud access: its
article already describes local analysis.

## Innovation portfolio and development process

Coesa describes a process spanning technology/business analysis, MVP design and
market validation, then testing, revision and go-to-market planning, with
research and technology partners.

- **KeepTheSun / Keep The Sun:** A marketplace for used photovoltaic panels; its
  second iteration emphasizes reuse in off-grid kits.
- **JuaKit:** An off-grid initiative using functioning second-life panels to
  address energy poverty. The page names Matteo Stoppa, PhD, as project leader
  and reports recognition at Impact Prototypes Labs 2025.
- **SPARC:** A mobile, AI-guided photovoltaic-panel recycling factory concept
  intended to reduce transport and end-of-life handling costs.

These descriptions are company claims, not independently verified maturity or
deployment assessments. The innovation page displays both 1–3 kW
configurable-system figures and an 800 W example; confirm the relevant JuaKit
configuration before sizing a PoopVolt integration.
[Innovation and research](https://coesaenergy.it/innovazione-ricerca-energetica/).

## People and hackTurin connection

Coesa's hackTurin announcement identifies Federico Sandrone as CEO, confirms
official sponsorship and participation in developing three challenges, and calls
for functioning prototypes at the 10–11 October event. It does not publish a
scoring rubric in the retrieved text.
[Coesa hackTurin announcement](https://it.linkedin.com/posts/coesa-srl_hackturin-challenge-activity-7510670035141627904-gUKs).

A separate company post identifies Matteo Stoppa, PhD, as Chief Innovation
Officer and describes his presentation of KeepTheSun, JuaKit and SPARC.
[Coesa innovation outreach post](https://it.linkedin.com/posts/coesa-srl_formazione-its-itspeano-activity-7460677442442182656-x8eN).

The [repository readme](../../README.md) also lists Sandrone as a kickoff
presenter and Stoppa as a confirmed mentor. These links establish relevant
people and event involvement; they do not establish that either individual will
personally judge PoopVolt or has approved an integration.

## PoopVolt fit — team hypotheses to validate

The renewed team proposal is to **sell edge devices to Coesa, which can offer
them free to its plant-owner customers**. The company uses the resulting
evidence to prioritize maintenance and explain when revamping could improve
profitability. This is a team commercial hypothesis, not a Coesa requirement,
partnership, integration agreement, or commitment to distribute devices.

The primary scope now includes grid-connected customer plants, single-string
visual diagnosis, and multi-channel plant monitoring. Off-grid and second-life
applications remain possible extensions. See the [pitch](../pitch-draft.md),
[architecture](../architecture/README.md), and [data plan](../data-plan.md).

<!-- markdownlint-disable MD013 -->

| Company context                            | Proposed PoopVolt contribution                                                                           | Evidence needed                                                                                                      |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Existing monitoring and O&M                | Connect mapped findings to cleaning, inspection, repair, and follow-up services.                         | Comparison with current monitoring, useful localization, false alerts, and verified outcomes.                        |
| Industrial and customer-plant services     | Provide an edge device that Coesa can distribute at no upfront device cost to the owner.                 | Device, installation, connectivity, and support costs versus incremental service margin; agreed ownership and terms. |
| Maintenance and module replacement         | Explain continued operation, targeted maintenance, and revamping alternatives with explicit assumptions. | Production baseline, technical assessment, intervention quotes, energy-use/value assumptions, and uncertainty.       |
| Local analytics already discussed by Coesa | Add a tested evidence-to-service workflow rather than claim Edge AI alone is new to Coesa.               | Measured local inference, mapped scope, synchronization freshness, and practical technician feedback.                |
| JuaKit and second-life panels              | Explore later off-grid or reuse pilots where hardware and power budgets fit.                             | Representative field data and an appropriate deployment budget; no assumed JuaKit integration.                       |
| MVP and market validation process          | Show phone-based contamination localization separately from historical telemetry replay.                 | Reproducible prototype scope, clear provenance, held-out evaluation, pilot owner, and next data requirements.        |

<!-- markdownlint-enable MD013 -->

### Suggested pitch emphasis

Follow the [three-minute owner narrative](../pitch-narrative.md): an older plant
still works, but the owner cannot assess its performance. After the approved
strong opening, emphasize the company's use of evidence to motivate an
intervention the owner can understand and assess. Explain the comparison, STL,
software case, technical review, and benefit verification without promising
service conversion. The theoretical reference and its inputs remain to define
and validate.

The company buys/free-device proposal is a secondary commercial hypothesis for
questions or the appendix, not the opening. Coesa is a potential service
counterpart, not an agreed partner. Mention droppings as a possible inspection
issue and keep phone imagery separate from multi-channel replay. Phone RGB
images do not confirm a hotspot, lost kWh, or an electrical interruption.
Whole-plant coverage depends on mapped channel access.

Describe maintenance and revamping as alternatives to assess for the owner.
Device distribution must have viable economics for Coesa; customer profitability
needs measured production and explicit costs, not invented savings. Generic AI
dashboards and offline analysis do not establish differentiation from Coesa's
existing activities. Test whether the proposed workflow makes service decisions
more useful, specific, and economical.

### Suggested pilot measurements

These are team-proposed dimensions, not Coesa's judging criteria:

- Single-string image classification and localization on held-out capture
  sessions, including shade, reflections, blur, and uncertain mapping.
- Multi-channel anomaly quality against a baseline, operating context, and
  verified events; later predictive evaluation with outcomes and a warning
  horizon.
- Service usefulness: technician assessment, avoided unnecessary work, and
  comparable production observations after intervention.
- Device/distribution economics: hardware, installation, operation, and support
  costs versus incremental service margin; no assumed conversion rate.
- Customer review: understandable maintenance/revamping scenarios, their cost
  assumptions, and whether the expected benefit is supported.
- Offline and remote behavior: local operation, queue recovery, coverage,
  last-seen timestamps, and company/own-plant access separation.

### Mentor feedback

Reported by Gianpaolo Macario on 2026-10-11 (issue #13). The team met Matteo
Stoppa (Coesa) on Saturday 2026-10-10 and Sunday 2026-10-11 and showed him the
progress so far. Only the points below were relayed; this is a paraphrase, not
a transcript, and it is not Coesa's position on PoopVolt or an approval of it.

- **Evidence available today:** Stoppa said that Coesa has no fine-grained data
  from photovoltaic plants it has not developed and commissioned. Because of
  that, it cannot provide optimized proposals for revamping those plants. This
  is consistent with its public pages, which describe monitoring for its own
  plants; it says nothing about the plants it built.

What this means for the team (analysis, not mentor feedback): the target is the
older plant that Coesa did not build, where the owner has no evidence and Coesa
cannot size a revamping offer. That supports the problem and the purpose of
PoopVolt's evidence, and it makes revamping proposals, not only cleaning, a
use of it. It also means the SOLARMA replay is the only plant history we can
point to, and the "multi-channel plant history" must not be presented as
available from Coesa: the device would have to produce that data. Whether the
evidence we produce is good enough to size a revamping offer is not yet
validated.

### Questions for Coesa or a mentor

1. Which customer segment and existing O&M workflow should host the first pilot?
2. What would justify paying for devices and providing them free to owners?
3. Which inverter/loggers expose useful channels, and is a string/panel map
   available?
4. What failure, cleaning, repair, revamping, and production history can be
   shared?
5. Which monitoring decisions still require site visits, and what improvement
   would be useful compared with the tools already used?
6. What ownership, installation/support responsibilities, integration options,
   and evidence are required before quoting customer work?

## Source register

All entries were researched on **2026-10-10**. Sources are first-party company
publications, primarily in Italian. Summaries above are paraphrases. An indexed
page may lag the live site.

<!-- markdownlint-disable MD013 -->

| Source ID                   | Source and canonical URL                                                                                                                 | Retrieve for                                                           | Access during research                       |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------- |
| `coesa-home`                | [Official homepage](https://coesaenergy.it/)                                                                                             | Service areas, workflow, published scale counters                      | Search-indexed text; direct fetch failed.    |
| `coesa-about`               | [Chi siamo](https://coesaenergy.it/chi-siamo/)                                                                                           | Identity, founders, history, ESCo/EPC positioning                      | Direct page text read.                       |
| `coesa-industrial-pv`       | [Fotovoltaico per imprese](https://coesaenergy.it/fotovoltaico/fotovoltaico-per-imprese/)                                                | Commercial arrangements, washing, monitoring, module replacement       | Search-indexed text; direct fetch timed out. |
| `coesa-pa-services`         | [Public-administration services](https://coesaenergy.it/efficientamento-energetico/efficientamento-energetico-pubblica-amministrazione/) | Company-listed certifications and public-sector offer                  | Search-indexed text read.                    |
| `coesa-monitoring`          | [Sistemi di monitoraggio](https://coesaenergy.it/sistemi-di-monitoraggio/)                                                               | Monitoring perspective, local/cloud analysis, small-system constraints | Direct page text read.                       |
| `coesa-innovation`          | [Innovazione e ricerca energetica](https://coesaenergy.it/innovazione-ricerca-energetica/)                                               | KeepTheSun, JuaKit, SPARC, innovation process                          | Search-indexed text; direct fetch timed out. |
| `coesa-hackturin`           | [Company hackTurin announcement](https://it.linkedin.com/posts/coesa-srl_hackturin-challenge-activity-7510670035141627904-gUKs)          | Sponsorship, CEO identification, prototype emphasis                    | Search-indexed company-post text read.       |
| `coesa-innovation-outreach` | [Company innovation outreach post](https://it.linkedin.com/posts/coesa-srl_formazione-its-itspeano-activity-7460677442442182656-x8eN)    | Stoppa's company-published role and portfolio presentation             | Search-indexed company-post text read.       |

<!-- markdownlint-enable MD013 -->

### Additional official material to retrieve later

The
[2026 company profile PDF](https://coesaenergy.it/wp-content/uploads/2026/01/COESA_Company_Profile_2026.pdf)
was located, but direct retrieval exceeded the web tool's size limit
(approximately 44.8 MB). Its full contents were not reviewed or used to
substantiate this document. Open it separately if more detailed corporate
information is needed.

## Boundaries and refresh guidance

- The user's evaluator context is distinct from publicly documented event
  sponsorship; no official judging rubric was retrieved.
- Public descriptions do not establish Coesa's internal technical stack,
  deployed models, datasets, API access or willingness to adopt PoopVolt.
- Company marketing figures and forecasts are not PoopVolt validation evidence.
  Financial returns and incentive eligibility depend on the actual installation
  and current rules.
- Confirm JuaKit specifications, current staff roles, portfolio maturity and
  company counters before quoting them externally.
- Keep Coesa Energy / COESA Srl distinct from similarly named entities,
  including Coesia and Coesa cooperatives.
