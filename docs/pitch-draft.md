# PoopVolt — turn production gaps into understandable intervention proposals

Status: Proposed product and commercial model. This PR supplies documentation,
not an implemented MVP, validated theoretical model, field benefit, or Coesa
partnership.

## The story: a working plant with unknown performance

An owner installed a photovoltaic plant years ago. It still produces
electricity, but the owner cannot see how each mapped string performs or whether
the plant produces as expected. Dust, wear, and pigeon droppings are possible
contributors to investigate, not causes proved by a chart or a visible deposit.

PoopVolt proposes a comparison between observed and expected production. The
intended theoretical reference must be defined using plant characteristics and
adequate operating/environmental inputs. Compare the same period and compatible
conditions, reporting missing inputs and uncertainty.

A deviation points to something worth inspecting. It does not alone establish a
failure, historical degradation, or recoverable energy. String-level conclusions
require measured coverage and a verified channel-to-string map.

A photovoltaic service company can use that evidence to explain what needs
inspection and propose a justified intervention that the owner can understand
and assess. Cleaning, repair, component replacement, and wider revamping are
options to evaluate. Comparable measurements after an intervention test its
benefit. Increased service uptake remains a hypothesis, not a guaranteed result.

The approved spoken opening is: "Il tuo impianto è sporco di merda.
Letteralmente. Ma il problema è capire quanto sta influendo sulla produzione."
This is an illustrative hook, not measured evidence of contamination loss. The
central message is: "PoopVolt trasforma uno scostamento produttivo in una
proposta di intervento comprensibile."

The canonical Italian story is the [three-minute narrative](pitch-narrative.md),
adapted from the team's `pitch-narrative2.md`.

## The hackathon presentation

The agreed talk is three minutes, including a software demonstration and an STL
design view. Follow the approved hook, company problem, expected/observed
comparison, physical concept, software case, and technician-reviewed proposal.
Explain how the company uses the product and how the owner assesses an
intervention. Do not lead with the distribution offer.

The team's MVP software and STL are presentation materials whose files and
verified functions must be linked before making implemented claims. This
documentation change does not implement either artifact.

If the theoretical reference, mapped strings, or software comparison are not
available, use a clearly labeled simulation or narrow the demonstration. State
provenance, period, units, reference method, and actual coverage.

## Proposed system and separate evidence paths

Acquisition, Diagnostics, and Maintenance remain local logical modules with
`Local storage` and an Operator interface on the intended Arduino UNO Q
platform. The [hardware inventory](hardware.md) records secured components;
availability does not establish assembly, compatible measurements, or successful
inference.

- **Production review:** Telemetry and a proposed expected-production reference
  support deviation review. The theoretical model, inputs, and calibration
  remain decisions, not an established baseline.
- **Visible inspection:** Phone RGB with simulated deposits can illustrate
  visible contamination on a declared panel/string. It cannot measure hotspots
  or lost kWh.
- **Historical replay:** SOLARMA inverter logs are a separate source for channel
  plots and anomaly development. They lack verified string mapping and populated
  irradiance, so they do not validate the theoretical model or the phone scene.

Keep these evidence scopes separate. Thermal acquisition remains deferred.
Predictive maintenance requires longitudinal outcomes and evaluation beyond a
current deviation. The [data plan](data-plan.md) records input and source
limits.

The proposed company platform supplies portfolio and own-plant views through
queued synchronization. Remote freshness depends on connection and record
synchronization; the static presentation is not that service platform.

## Coesa and the commercial hypothesis

The existing business proposal remains a hypothesis: sell an edge device to a
photovoltaic service company, which could offer it to customers at no upfront
device charge. Pricing, ownership, installation, support, and recurring fees are
open. The three-minute narrative emphasizes owner value; explain the
distribution model in questions or the appendix rather than treating it as an
agreed partnership.

Coesa is a potential technical/service counterpart. Its existing monitoring and
O&M activities provide context; Edge AI alone is not an established
differentiator. Read the [company context](company/coesa-energy.md) for sources
and hypotheses.

Revamping is one option beside cleaning, repair, and continued operation. No
measured savings, payback, service conversion, or full recovery of the
production gap is established. Economic estimates need costs, baseline
production, incremental energy, energy value, and uncertainty.

## Next validation

Define and evaluate the expected-production reference, verify channel mapping,
and run a reproducible software case with clear provenance. Link the STL concept
and implemented MVP separately from this architecture draft.

A field pilot should record operating conditions, intervention details,
comparable before/after production, and technician usefulness. Off-grid,
second-life, forecasting, and battery scheduling remain possible extensions.

See the [architecture index](architecture/README.md) for proposed system views.
