# Soiling Detection Flow

- Diagram ID: `pv-flow-soiling`
- Level: Runtime flow
- Status: Proposed draft; implementation and hardware choices are unverified.
- Parent: [Parent view](../components/diagnostics.md)

## Diagram

```mermaid
sequenceDiagram
    participant A as Acquisition
    participant D as Diagnostics
    participant S as Local storage
    participant M as Maintenance
    A->>D: Image and aligned measurements with quality flags
    D->>D: Check input quality and run soiling detection
    alt Adequate evidence
        D->>S: Store soiling finding and supporting observation
        D->>M: Finding with uncertainty and evidence reference
    else Missing or unreliable input
        D->>S: Store quality issue
        D->>M: Request inspection or new observation
    end
```

## Explanation

A proposed soiling inference begins with quality-checked observations. Diagnostics preserves evidence and communicates uncertainty. An unreliable observation leads to a review request rather than an unsupported contamination finding.

## Related Views

[Acquisition](../components/acquisition.md) · [Maintenance recommendation](recommend-maintenance.md) · [Architecture index](../README.md)
