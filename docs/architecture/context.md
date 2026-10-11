# System Context

- Diagram ID: `pv-context`
- Level: System context
- Status: Proposed draft; product, integration, and business model unverified.
- Parent: [Parent view](overview.md)

## Diagram

```mermaid
flowchart LR
    company["Service company / Coesa candidate buyer"]
    owner["Plant owner / customer"]
    operator["Operator / company technician"]
    installation["Customer photovoltaic installation"]
    subgraph boundary["PoopVolt proposed system boundary"]
        edge["Customer-site edge device"]
        platform["Company service platform"]
    end
    company -->|Buys devices and offers them free to customers| owner
    installation -->|Mapped telemetry and image observations| edge
    edge -->|Findings, coverage and history when connected| platform
    platform -->|Portfolio findings and service review| operator
    platform -->|Own-plant evidence and proposals| owner
    operator -->|Reviewed service proposal| owner
    owner -->|Accepts intervention| operator
    operator -->|Cleaning, inspection, repair or revamping| installation
    operator -->|Intervention records| platform
    platform -->|Reviewed records and configuration when connected| edge
```

## Explanation

The company is the buyer and service provider; the owner receives the device
under the proposed free-device offer. Technicians review findings and owners
accept service work. This is a proposed distribution model, not a Coesa agreement.

Local diagnostics work without continuous connectivity. Remote portfolio review
requires synchronization and displays last-seen time and channel coverage.
The platform is part of the proposed product boundary, with technology and
integration still undecided. Grid-connected systems are in scope; off-grid and
second-life systems are potential extensions.

## Related Views

[Architecture](architecture.md) · [Deployment](deployment.md) ·
[Company context](../company/coesa-energy.md) · [Architecture index](README.md)
