# System Overview

- Diagram ID: `pv-overview`
- Level: Overview
- Status: Proposed draft; implementation and hardware choices are unverified.
- Parent: [Parent view](README.md)

## Diagram

```mermaid
flowchart TB
    A["Off-Grid Photovoltaic System"]

    B["Data Collection<br/>Electrical · Environmental · Thermal / RGB"]

    C["Arduino UNO Q 4GB<br/>Edge AI"]

    D["Intelligent Diagnostics<br/>Fault Detection · Soiling · Degradation"]

    E["Predictive Maintenance<br/>& Lifecycle Optimization"]

    F["Optimized Energy Production"]
    G["Extended System Lifetime"]
    H["Revamping Avoidance"]

    A --> B
    B --> C
    C --> D
    D --> E

    E --> F
    E --> G
    E --> H

    classDef source fill:#dbeafe,stroke:#2563eb,color:#1e40af
    classDef ai fill:#dcfce7,stroke:#16a34a,color:#166534
    classDef result fill:#fef3c7,stroke:#d97706,color:#92400e

    class A,B source
    class C,D,E ai
    class F,G,H result
```

## Explanation

Electrical, environmental, and image measurements feed local Edge AI diagnostics. Maintenance and lifecycle recommendations aim to improve energy availability and avoid unnecessary replacement. These outcomes are goals, not measured results.

## Related Views

[System context](context.md) · [Project pitch](../pitch-draft.md) · [Architecture index](README.md)
