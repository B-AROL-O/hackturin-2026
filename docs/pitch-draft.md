# PoopVolt — from a pigeon to a plant service opportunity

Status: Proposed product and commercial model. No working edge pipeline,
validated model, field benefit, or Coesa partnership is established yet.

**PoopVolt is an Edge AI device sold to photovoltaic service companies such as
Coesa. The company can provide it free of charge to plant owners, turning
installation observations into targeted maintenance and evidence-based
revamping proposals.**

## The story: one pigeon, one affected string

A pigeon leaves droppings on a photovoltaic panel. Localized contamination can
shade cells, reduce output, and contribute to hotspot risk. Dust introduces a
broader soiling problem. The useful question is: where should a technician look,
what might be wrong, and which intervention is worth considering?

PoopVolt aims to identify the affected string and, where mapped imagery provides
enough detail, the visible contaminated region on a panel. It proposes a problem
class with supporting evidence and uncertainty. An RGB image does not establish
a thermal hotspot, an electrical interruption, or the amount of lost energy.
Those claims require appropriate thermal or electrical measurements.

## The product: one edge device, two observation paths

The intended Arduino UNO Q edge platform runs Acquisition, Diagnostics, and
Maintenance locally and retains observations in `Local storage`.

- **Single-string demonstration:** A phone camera supplies RGB images of a
  mapped panel/string with simulated dust or droppings. The target is visible
  contamination classification and image-region localization. Electrical loss
  and hotspot confirmation are separate validation steps.
- **Multi-string and whole-plant monitoring:** Inverter or logger telemetry feeds
  historical and cross-channel analysis. Edge ML aims to detect persistent
  underperformance and prioritize inspection; predictive maintenance requires
  representative history and intervention/failure outcomes. SOLARMA's public
  inverter logs supply a proposed replay source, not a proven prediction model.

Local analysis should continue during a connectivity outage. When connected,
the device synchronizes summaries, findings, coverage, and intervention history
to a proposed company service platform. Coesa can review a portfolio of customer
plants; each customer sees the evidence and recommendations for their own plant.
Remote portfolio visibility depends on synchronization and must show freshness.

Whole-plant coverage requires all relevant channels to be connected and mapped.
Aggregate power alone cannot identify an exact module or distinguish every cause.

## The offer: company pays, customer receives the device

PoopVolt sells the device to the service company. The proposed distribution
model lets that company give it to a customer at no upfront device charge.
Pricing, ownership, installation, support, and any recurring platform fee remain
to be agreed. Free to the customer still leaves a cost for the company to recover.

The company gains a proposed path from observed underperformance to a service:

1. Review a localized finding and its uncertainty.
2. Offer cleaning, inspection, or repair where the evidence supports it.
3. Reassess production after the intervention.
4. Compare continued operation, maintenance, and revamping when persistent
   losses justify a technical and economic review.

For the owner, the intended value is an understandable explanation of plant
condition and whether an intervention could improve profitability. Revamping
is an option to evaluate alongside maintenance and continued operation. Estimates
must disclose baseline production, expected incremental energy, energy value,
intervention cost, and uncertainty; no savings or payback is measured today.

## Why this fits Coesa

Coesa already advertises monitoring and O&M, including washing and replacement
of underperforming modules. The proposed fit is a device distribution channel
and an evidence-to-service workflow within those activities. Coesa also discusses
local analytics, so Edge AI alone is not an established differentiator.
See the [company context](company/coesa-energy.md) for sources and hypotheses.
Off-grid and second-life systems remain possible later applications rather than
the primary market constraint.

## What the hackathon should demonstrate

Demonstrate the phone-to-localization path and the independent historical
telemetry replay path, with provenance, mapped scope, and uncertain-input handling.
Show an illustrative company finding and a customer maintenance/revamping review.
Do not present the phone scene as paired with the historical plant or call an
anomaly detector a validated failure predictor.

The next step is a company-led pilot to measure detection quality, field mapping,
device cost and power draw, service usefulness, and post-intervention production.
The [data plan](data-plan.md) defines source limits and the
[architecture index](architecture/README.md) defines the proposed system.

## Short Italian pitch

Un piccione sporca un pannello: dove interveniamo, e quanto conviene farlo?
PoopVolt è un dispositivo Edge AI che vendiamo all'azienda di servizi energetici,
che può offrirlo gratuitamente ai propri clienti. Su una singola stringa puntiamo
a localizzare e classificare lo sporco visibile; su più stringhe analizziamo i
dati dell'impianto per individuare anomalie e sviluppare manutenzione predittiva.
L'azienda riceve evidenze per proporre pulizia, manutenzione o una valutazione
di revamping; il proprietario può capire il possibile beneficio economico.
Per il prototipo useremo una fotocamera del telefono con sporco simulato e,
separatamente, log storici SOLARMA. Hotspot, perdita elettrica e ritorno economico
richiedono misure dedicate: sono obiettivi da validare, non risultati già ottenuti.
