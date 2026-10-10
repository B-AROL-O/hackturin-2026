# Coesa Energy — evaluator context for PoopVolt

- Document ID: `coesa-energy-context`
- Entity: Coesa Energy / COESA Srl, Torino, Italy
- Official website: <https://coesaenergy.it/>
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
spin-off, COESA Engineering Srl, established in 2019. Its registered website
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

The [repository README](../../README.md) also lists Sandrone as a kickoff
presenter and Stoppa as a confirmed mentor. These links establish relevant
people and event involvement; they do not establish that either individual will
personally judge PoopVolt or has approved an integration.

## PoopVolt fit — team hypotheses to validate

The following are proposed connections between the company context above and the
[PoopVolt pitch](../pitch-draft.md). None is a confirmed Coesa partnership,
product requirement or pilot commitment.

<!-- markdownlint-disable MD013 -->

| Company context | Proposed PoopVolt contribution | Evidence to bring to a discussion |
| --- | --- | --- |
| JuaKit and second-life off-grid panels | Assess panel condition and recommend useful local maintenance despite intermittent connectivity. | A disconnected demonstration, representative used-panel data, and a measured power budget. |
| Existing O&M activities | Help distinguish a cleaning opportunity from a fault requiring inspection. | Labeled examples, false-alert rates, intervention cost, and performance before/after cleaning. |
| Panel reuse and circular economy | Support decisions about continued use, targeted repair or replacement. | A defensible baseline and decision rule; distinguish short-term soiling detection from long-term degradation prediction. |
| Small-system monitoring constraints | Offer a device whose cost, energy use and usability fit a small installation. | Bill of materials, installation steps, standby/inference consumption and an understandable alert. |
| MVP and market validation process | Present a working subsystem and a practical next experiment. | What works today, what remains proposed, the pilot owner, success criteria and required data. |

<!-- markdownlint-enable MD013 -->

### Suggested pitch emphasis

Frame PoopVolt as a proposed maintenance decision aid for small off-grid and
second-life photovoltaic systems. Show a concrete path from sensor evidence to
an action, such as cleaning or technician inspection, and explain the
uncertainty in that recommendation. Connect the proposed benefits to energy
availability, intervention cost and continued panel use.

Describe the Arduino UNO Q as an implementation choice and support that choice
with measurements. Treat lifetime extension, avoided replacement, recovered
energy and savings as hypotheses until field evidence supports them. A short
hackathon demonstration can establish detection and local operation; it cannot
by itself establish a multi-year degradation forecast.

### Suggested pilot measurements

These are team-proposed evaluation dimensions, not Coesa's judging criteria:

- Detection quality: precision/recall on representative contamination and fault
  examples, including false alarms caused by shade or changing weather.
- Decision value: whether a recommended action restores useful energy relative
  to its labor and travel cost.
- Offline behavior: decision latency, data retained during disconnection and
  recovery after reconnection.
- Deployment burden: total hardware cost, installation effort and measured
  device energy consumption.
- Lifecycle evidence: condition observations over time and the limits of any
  replacement recommendation.

### Questions for Coesa or a mentor

1. Is the best first pilot a JuaKit installation, another off-grid system, or an
   industrial maintenance case?
2. What panel-condition, inverter, battery or maintenance-history data can be
   made available?
3. What monitoring already exists, and which decisions still require expensive
   site visits?
4. What device cost and energy budget are acceptable for the target
   installation?
5. Who receives recommendations, and what evidence is required before cleaning,
   repair or replacement?
6. What integrations and field-validation access would be available for a pilot?

## Source register

All entries were researched on **2026-10-10**. Sources are first-party company
publications, primarily in Italian. Summaries above are paraphrases. An indexed
page may lag the live website.

<!-- markdownlint-disable MD013 -->

| Source ID | Source and canonical URL | Retrieve for | Access during research |
| --- | --- | --- | --- |
| `coesa-home` | [Official homepage](https://coesaenergy.it/) | Service areas, workflow, published scale counters | Search-indexed text; direct fetch failed. |
| `coesa-about` | [Chi siamo](https://coesaenergy.it/chi-siamo/) | Identity, founders, history, ESCo/EPC positioning | Direct page text read. |
| `coesa-industrial-pv` | [Fotovoltaico per imprese](https://coesaenergy.it/fotovoltaico/fotovoltaico-per-imprese/) | Commercial arrangements, washing, monitoring, module replacement | Search-indexed text; direct fetch timed out. |
| `coesa-pa-services` | [Public-administration services](https://coesaenergy.it/efficientamento-energetico/efficientamento-energetico-pubblica-amministrazione/) | Company-listed certifications and public-sector offer | Search-indexed text read. |
| `coesa-monitoring` | [Sistemi di monitoraggio](https://coesaenergy.it/sistemi-di-monitoraggio/) | Monitoring perspective, local/cloud analysis, small-system constraints | Direct page text read. |
| `coesa-innovation` | [Innovazione e ricerca energetica](https://coesaenergy.it/innovazione-ricerca-energetica/) | KeepTheSun, JuaKit, SPARC, innovation process | Search-indexed text; direct fetch timed out. |
| `coesa-hackturin` | [Company hackTurin announcement](https://it.linkedin.com/posts/coesa-srl_hackturin-challenge-activity-7510670035141627904-gUKs) | Sponsorship, CEO identification, prototype emphasis | Search-indexed company-post text read. |
| `coesa-innovation-outreach` | [Company innovation outreach post](https://it.linkedin.com/posts/coesa-srl_formazione-its-itspeano-activity-7460677442442182656-x8eN) | Stoppa's company-published role and portfolio presentation | Search-indexed company-post text read. |

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
