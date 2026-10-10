# Maintenance Recommendation Flow

- Diagram ID: `pv-flow-maintenance`
- Level: Runtime flow
- Status: Proposed draft; service and economic review unimplemented.
- Parent: [Parent view](../components/maintenance.md)

## Diagram

```mermaid
sequenceDiagram
    participant D as Diagnostics
    participant M as Maintenance
    participant S as Local storage
    participant P as Company service platform
    participant O as Operator / technician
    participant C as Customer / owner
    D->>M: Scoped findings, evidence and uncertainty
    M->>S: Read baseline, intervention history and cost assumptions
    S-->>M: Available inputs and missing-data flags
    M->>M: Compare no action, maintenance and revamping review
    M->>S: Recommendation and qualified economic scenario
    S-->>P: Synchronize queued records when connected
    P-->>O: Evidence, coverage, freshness and proposed options
    O->>C: Reviewed service proposal and assumptions
    C-->>O: Accept or decline quoted intervention
    opt Owner accepts work
        O->>O: Perform approved physical intervention
        O->>P: Record action, cost and outcome
        P-->>S: Synchronize intervention record
    end
    Note over D,C: Later comparable observations assess results, benefit is not assumed
```

## Explanation

The company reviews evidence before offering cleaning, inspection, repair, or
revamping. The owner accepts service work. Economic scenarios need explicit
inputs and cannot be derived from a visible deposit alone. Local operator review
remains available offline; remote company and customer views require connection
and expose record freshness. This draft automates no physical intervention.

## Related Views

[Soiling flow](detect-soiling.md) · [Whole-plant flow](monitor-plant.md) ·
[System context](../context.md) · [Architecture index](../README.md)
