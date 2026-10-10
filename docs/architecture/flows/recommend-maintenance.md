# Maintenance Recommendation Flow

- Diagram ID: `pv-flow-maintenance`
- Level: Runtime flow
- Status: Proposed draft; implementation and hardware choices are unverified.
- Parent: [Parent view](../components/maintenance.md)

## Diagram

```mermaid
sequenceDiagram
    participant D as Diagnostics
    participant M as Maintenance
    participant S as Local storage
    participant O as Operator
    D->>M: Findings, evidence and uncertainty
    M->>S: Read intervention history
    S-->>M: Historical interventions and outcomes
    M->>M: Assess evidence and choose recommendation
    M-->>O: Recommendation through Operator interface
    O->>O: Review and perform approved physical intervention
    O->>S: Record action and outcome through Operator interface
    Note over D,O: Later observations support reassessment without assuming improvement
```

## Explanation

The operator reviews a recommendation before physical maintenance. Recorded actions and later observations support reassessment. This draft does not automate cleaning, switching, or component replacement.

## Related Views

[Soiling detection](detect-soiling.md) · [System context](../context.md) · [Architecture index](../README.md)
