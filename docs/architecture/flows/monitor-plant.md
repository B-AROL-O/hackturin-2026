# Whole-Plant Monitoring Flow

- Diagram ID: `pv-flow-plant`
- Level: Runtime flow
- Status: Proposed draft; replay, model, and synchronization unimplemented.
- Parent: [Parent view](../components/diagnostics.md)

## Diagram

```mermaid
sequenceDiagram
    participant L as Logger or historical replay
    participant A as Acquisition
    participant D as Diagnostics
    participant S as Local storage
    participant M as Maintenance
    participant P as Company service platform
    L->>A: Timestamped device/channel samples and source identity
    A->>S: Normalize and retain observations, mapping and coverage
    A->>D: Quality-checked samples and operating context
    D->>S: Read compatible history and channel topology
    S-->>D: Historical baseline and known limitations
    D->>D: Assess deviations and persistent trends on edge
    alt Adequate evidence
        D->>M: Candidate anomaly, location scope and uncertainty
    else Missing history, mapping or reliable inputs
        D->>M: Coverage limitation or inspection request
    end
    M->>S: Recommendation and evidence references
    alt Connected
        S-->>P: Synchronize queued summaries, coverage and findings
    else Disconnected
        Note over D,S: Local analysis continues and outgoing records remain queued
        Note over P: Remote view retains last-seen time and stale status
    end
```

## Explanation

Historical replay retains its original timestamps and a replay label. It is
independent of the phone scene. Field ingestion would use a verified adapter.
An anomaly's scope cannot exceed the known plant/channel/string mapping.
This flow demonstrates the proposed path toward predictive maintenance; a
current deviation is not proof that a future failure has been predicted.

## Related Views

[Data plan](../../data-plan.md) · [Diagnostics](../components/diagnostics.md) ·
[Maintenance flow](recommend-maintenance.md) · [Architecture index](../README.md)
