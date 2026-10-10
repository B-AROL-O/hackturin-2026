# Application Architecture

- Diagram ID: `pv-architecture`
- Level: Architecture
- Status: Proposed draft; implementation and hardware choices are unverified.
- Parent: [Parent view](context.md)

## Diagram

```mermaid
flowchart LR
    sensors["Sensors and cameras"]
    subgraph edge["PoopVolt edge application"]
        acquisition["Acquisition"]
        diagnostics["Diagnostics"]
        maintenance["Maintenance"]
        interface["Operator interface"]
    end
    storage[("Local storage")]
    sensors -->|Measurements and images| acquisition
    acquisition -->|Validated observations| diagnostics
    acquisition -->|Observation records| storage
    storage -->|Historical observations| diagnostics
    diagnostics -->|Findings and uncertainty| maintenance
    storage -->|Intervention history| maintenance
    maintenance -->|Recommendations| interface
    interface -->|Intervention records| storage
```

## Explanation

Acquisition, Diagnostics, and Maintenance are logical modules within a proposed edge application, not confirmed independent services. The `Local storage` component preserves observations and intervention history. The Operator interface exposes recommendations; its technology is undecided.

## Related Views

[Acquisition](components/acquisition.md) · [Diagnostics](components/diagnostics.md) · [Maintenance](components/maintenance.md) · [Deployment](deployment.md) · [Architecture index](README.md)
