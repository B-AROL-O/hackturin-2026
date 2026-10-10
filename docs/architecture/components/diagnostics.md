# Diagnostics Components

- Diagram ID: `pv-diagnostics`
- Level: Components
- Status: Proposed draft; implementation and hardware choices are unverified.
- Parent: [Parent view](../architecture.md)

## Diagram

```mermaid
flowchart TB
    acquisition["Acquisition"]
    rgb["Soiling detection"]
    thermal["Thermal anomaly analysis"]
    electrical["Electrical performance analysis"]
    history[("Local storage")]
    degradation["Degradation estimation"]
    fusion["Finding aggregation"]
    maintenance["Maintenance"]
    acquisition -->|RGB frames| rgb
    acquisition -->|Thermal frames| thermal
    acquisition -->|Electrical and environmental observations| electrical
    electrical -->|Performance estimates| degradation
    history -->|Historical observations| degradation
    rgb -->|Soiling findings| fusion
    thermal -->|Thermal findings| fusion
    electrical -->|Electrical findings| fusion
    degradation -->|Trend estimates| fusion
    fusion -->|Findings, evidence and uncertainty| maintenance
```

## Explanation

Diagnostics combines image findings with electrical performance and historical trends. Degradation estimation requires sufficient history and an environmental baseline; a single image does not establish irreversible degradation. Model choices, calibration, fusion logic, thresholds, and evaluation metrics are not yet selected.

## Related Views

[Datasets](../../references.md#datasets) · [Maintenance](maintenance.md) · [Soiling detection flow](../flows/detect-soiling.md) · [Architecture index](../README.md)
