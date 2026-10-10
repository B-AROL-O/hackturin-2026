# Acquisition Components

- Diagram ID: `pv-acquisition`
- Level: Components
- Status: Proposed draft; implementation and hardware choices are unverified.
- Parent: [Parent view](../architecture.md)

## Diagram

```mermaid
flowchart LR
    inputs["Electrical, environmental and image inputs"]
    adapters["Input adapters"]
    validate["Timestamp and quality checks"]
    align["Observation alignment"]
    diagnostics["Diagnostics"]
    storage[("Local storage")]
    inputs -->|Raw samples and frames| adapters
    adapters -->|Normalized observations| validate
    validate -->|Valid observations and quality flags| align
    align -->|Aligned observation bundle| diagnostics
    align -->|Observation records| storage
```

## Explanation

Input adapters normalize source measurements. Quality checks identify missing, stale, or invalid inputs. Alignment associates measurements and frames in time before Diagnostics consumes them. Sample rates, units, timestamp tolerance, retention, and degraded-input behavior remain open decisions.

## Related Views

[Diagnostics](diagnostics.md) · [Deployment](../deployment.md) · [Architecture index](../README.md)
