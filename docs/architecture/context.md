# System Context

- Diagram ID: `pv-context`
- Level: System context
- Status: Proposed draft; implementation and hardware choices are unverified.
- Parent: [Parent view](overview.md)

## Diagram

```mermaid
flowchart LR
    operator["Operator"]
    installation["Off-grid photovoltaic installation"]
    subgraph boundary["PoopVolt system boundary"]
        system["PoopVolt"]
    end
    operator -->|Reviews findings and records interventions| system
    installation -->|Electrical, environmental and image observations| system
    system -->|Diagnostics and maintenance recommendations| operator
    operator -->|Cleaning and targeted repairs| installation
```

## Explanation

PoopVolt observes the installation and advises an operator. Physical maintenance remains an operator action in this draft. Continuous cloud connectivity is not required; cloud services are not part of the proposed core boundary.

## Related Views

[Architecture](architecture.md) · [Deployment](deployment.md) · [Architecture index](README.md)
