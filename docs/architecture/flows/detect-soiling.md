# Soiling Detection Flow

- Diagram ID: `pv-flow-soiling`
- Level: Runtime flow
- Status: Proposed draft; phone capture and inference unimplemented.
- Parent: [Parent view](../components/diagnostics.md)

## Diagram

```mermaid
sequenceDiagram
    participant P as Phone camera
    participant A as Acquisition
    participant D as Diagnostics
    participant S as Local storage
    participant M as Maintenance
    P->>A: RGB frame, capture session and declared demo asset
    A->>D: Frame, mapping status, provenance and quality
    D->>D: Check quality and classify/localize visible contamination
    alt Adequate visible evidence and known mapping
        D->>S: Class, image region, mapped asset and uncertainty
        D->>M: Visible soiling finding for cleaning review
    else Unreliable input or unknown asset mapping
        D->>S: Quality or mapping limitation
        D->>M: Request new observation or asset inspection
    end
    Note over P,M: RGB does not confirm a hotspot, electrical interruption or lost energy
```

## Explanation

The phone demonstration targets a visible region on a declared panel/string
with simulated dust or droppings. Known mapping means known for that setup;
field mapping needs separate verification. Usable images with unknown mapping
can still support image-region findings, but not a claimed physical string.
Unreliable observations lead to review rather than unsupported classification.

## Related Views

[Data plan](../../data-plan.md) · [Acquisition](../components/acquisition.md) ·
[Maintenance flow](recommend-maintenance.md) · [Architecture index](../README.md)
