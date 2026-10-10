# System Overview

- Diagram ID: `pv-overview`
- Level: Overview
- Status: Proposed draft; outcomes and implementation unverified.
- Parent: [Parent view](README.md)

## Diagram

```mermaid
flowchart TB
    plant["Customer PV plant / mapped strings"]
    images["Single-string RGB observations"]
    telemetry["Multi-channel electrical history"]
    expected["Proposed theoretical production reference / inputs to verify"]
    edge["PoopVolt edge device / intended Arduino UNO Q"]
    diagnostics["Local classification, localization and trend analysis"]
    local["Local maintenance review"]
    platform["Company service platform / sync when connected"]
    service["Technician and owner review"]
    maintenance["Targeted cleaning, inspection or repair"]
    revamping["Evidence-based revamping assessment"]
    value["Goal: improved plant profitability and useful services"]
    plant -->|Visible contamination| images
    plant -->|Inverter or logger observations| telemetry
    images --> edge
    telemetry --> edge
    expected -->|Estimated reference with scope and uncertainty| diagnostics
    edge --> diagnostics
    diagnostics --> local
    diagnostics --> platform
    platform --> service
    service --> maintenance
    service --> revamping
    maintenance --> value
    revamping --> value
```

## Explanation

The owner narrative starts from uncertain plant performance. A proposed
theoretical reference and observed production support scoped deviation review,
subject to input quality and verified mapping. This comparison alone does not
identify the cause or guarantee recoverable energy.

The commercial hypothesis sells an edge device to a service company, which can
distribute it free to its customers. One observation path targets visible
contamination on a mapped string; another targets whole-plant underperformance
using multi-channel history. Both support a service decision. Predictive
maintenance is a development goal, requiring longitudinal validation beyond
detecting a current anomaly.

The phone-camera demo and SOLARMA replay are independent evidence paths. Neither
establishes complete plant coverage, confirmed hotspots, or economic returns.
The [data plan](../data-plan.md) defines their limits.

## Related Views

[System context](context.md) · [Project pitch](../pitch-draft.md) ·
[Architecture index](README.md)
