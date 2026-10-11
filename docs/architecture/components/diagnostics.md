# Diagnostics Components

- Diagram ID: `pv-diagnostics`
- Level: Components
- Status: Proposed draft; no trained model or evaluation is established.
- Parent: [Parent view](../architecture.md)

## Diagram

```mermaid
flowchart TB
    acquisition["Acquisition"]
    rgb["Visible contamination classification and localization"]
    electrical["Channel and whole-plant anomaly analysis"]
    reference["Theoretical expected production / proposed and unvalidated"]
    history[("Local storage")]
    trends["Trend analysis / predictive maintenance development"]
    fusion["Finding aggregation within compatible evidence"]
    maintenance["Maintenance"]
    acquisition -->|RGB frames and image-to-asset mapping| rgb
    acquisition -->|Electrical observations, quality and topology| electrical
    reference -->|Matched period, scope and uncertainty| electrical
    electrical -->|Scoped performance features| trends
    history -->|History and verified intervention or failure outcomes| trends
    rgb -->|Visible class and image region| fusion
    electrical -->|Channel anomalies and coverage limits| fusion
    trends -->|Trend or forecast with validation scope| fusion
    fusion -->|Findings, location scope, evidence and uncertainty| maintenance
```

## Explanation

For one mapped string, RGB analysis targets visible clean, dust-like,
droppings-like, mixed, or unknown observations and deposit regions. Final
classes and model selection depend on collected labels. A region identifies
visible contamination, not a measured open circuit or hotspot. Physical
localization depends on a verified image-to-panel/string map.

For the revised owner story, a theoretical production reference is proposed. Its
model, input availability, uncertainty, and evaluation are unresolved. Compare
reference and observed values over matching periods and asset scopes. A
deviation is not a historical decline, proved cause, or guaranteed recoverable
yield.

For multiple channels, electrical analysis can also target deviations against a
historical baseline and compatible peers. Inverter inputs may contain multiple
strings. Unequal capacities, orientation, shade, weather, operating state, and
logger outages can explain differences. Aggregate power cannot localize a
module.

Edge ML for anomaly/trend detection is proposed. A current anomaly is not a
validated future-failure forecast. Predictive maintenance needs representative
longitudinal data, labeled outcomes, a warning horizon, and held-out evaluation.
Degradation estimation requires sufficient history and an environmental
baseline; the inspected SOLARMA export lacks populated irradiance values.

Finding aggregation preserves provenance and does not fuse the unrelated phone
demo and SOLARMA replay. The
[Grove thermal camera is unavailable](../../hardware.md), so thermal analysis is
deferred and the current diagram omits that branch. The selected phone RGB
camera supports visible contamination analysis; RGB soiling alone supports at
most a hotspot-risk inspection request. AHT20 ambient temperature cannot confirm
a panel hotspot. Unsupported classification or mapping yields
unknown/review-required. Models, thresholds, calibration, edge resource budgets,
and metrics remain open.

The [phone inspection implementation](../phone-inspection.md) now supplies the
RGB detector adapter and browser review path. Model artifacts/class metadata
remain placeholders. Dust, bird-dropping and visible-damage categories are exposed
only if present in the delivered model; unsupported categories are labeled.
Detection confidences and conservative review rules do not establish thermal,
electrical, degradation or fused maintenance findings.

## Related Views

[Data plan](../../data-plan.md) · [Maintenance](maintenance.md) ·
[Soiling flow](../flows/detect-soiling.md) ·
[Whole-plant flow](../flows/monitor-plant.md) ·
[Architecture index](../README.md)
