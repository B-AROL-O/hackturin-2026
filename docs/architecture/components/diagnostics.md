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
    thermal["Thermal anomaly analysis / optional future input"]
    electrical["Channel and whole-plant anomaly analysis"]
    history[("Local storage")]
    trends["Trend analysis / predictive maintenance development"]
    fusion["Finding aggregation within compatible evidence"]
    maintenance["Maintenance"]
    acquisition -->|RGB frames and image-to-asset mapping| rgb
    acquisition -->|Thermal frames if available| thermal
    acquisition -->|Electrical observations, quality and topology| electrical
    electrical -->|Scoped performance features| trends
    history -->|History and verified intervention or failure outcomes| trends
    rgb -->|Visible class and image region| fusion
    thermal -->|Measured thermal findings| fusion
    electrical -->|Channel anomalies and coverage limits| fusion
    trends -->|Trend or forecast with validation scope| fusion
    fusion -->|Findings, location scope, evidence and uncertainty| maintenance
```

## Explanation

For one mapped string, RGB analysis targets visible clean, dust-like,
droppings-like, mixed, or unknown observations and deposit regions. Final classes
and model selection depend on collected labels. A region identifies visible
contamination, not a measured open circuit or hotspot. Physical localization
depends on a verified image-to-panel/string map.

For multiple channels, electrical analysis targets persistent deviations against
a historical baseline and compatible peers. Inverter inputs may contain multiple
strings. Unequal capacities, orientation, shade, weather, operating state, and
logger outages can explain differences. Aggregate power cannot localize a module.

Edge ML for anomaly/trend detection is proposed. A current anomaly is not a
validated future-failure forecast. Predictive maintenance needs representative
longitudinal data, labeled outcomes, a warning horizon, and held-out evaluation.
Degradation estimation requires sufficient history and an environmental baseline;
the inspected SOLARMA export lacks populated irradiance values.

Finding aggregation preserves provenance and does not fuse the unrelated phone
demo and SOLARMA replay. Thermal confirmation requires a thermal measurement;
RGB soiling alone supports at most a hotspot-risk inspection request.
Unsupported classification or mapping yields unknown/review-required.
Models, thresholds, calibration, edge resource budgets, and metrics remain open.

## Related Views

[Data plan](../../data-plan.md) · [Maintenance](maintenance.md) ·
[Soiling flow](../flows/detect-soiling.md) ·
[Whole-plant flow](../flows/monitor-plant.md) · [Architecture index](../README.md)
