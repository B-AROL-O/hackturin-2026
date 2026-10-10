# Physical Deployment

- Diagram ID: `pv-deployment`
- Level: Deployment
- Status: Proposed draft; hardware and transport require verification.
- Parent: [Parent view](architecture.md)

## Diagram

```mermaid
flowchart TB
    phone["Phone camera / simulated single-string contamination"]
    replay["Historical SOLARMA replay / separate demo source"]
    plant["Customer PV plant"]
    logger["Inverter or logger / field adapter TBD"]
    sensors["Optional electrical, environmental and thermal sensors"]
    power["Regulated device power / design pending"]
    subgraph uno["Intended Arduino UNO Q edge device"]
        mcu["MCU acquisition if required / split TBD"]
        app["Linux edge application / proposed"]
        storage[("Local storage")]
    end
    local["Local access device"]
    platform["Company service platform / hosting TBD"]
    users["Company technician and plant owner access devices"]
    phone -->|Image transfer TBD| app
    replay -->|Offline import or replay adapter TBD| app
    plant -->|Telemetry| logger
    plant -->|Physical observations| sensors
    sensors -->|Selected interfaces TBD| mcu
    logger -->|Verified read-only interface TBD| app
    mcu -->|Observation bridge TBD| app
    power -->|Supply compatibility pending| uno
    app <-->|Records, mappings and queue| storage
    app -->|Local interface TBD| local
    app <-->|Authenticated synchronization when connected| platform
    platform -->|Role-scoped remote views| users
```

## Explanation

The intended UNO Q runs local inference and history analysis. A phone supplies
RGB frames for the hackathon; no permanent phone installation or thermal camera
is assumed. Historical replay is imported independently of the phone scene.

A field device needs verified logger compatibility or instrumentation for each
claimed channel. One inverter input can represent several parallel strings;
channel topology must be verified before promising string-level coverage.
Exact module location needs a surveyed image-to-panel/string mapping or additional
measurements. Device count and electrical interfaces depend on plant topology.

Power supply, enclosure, network provisioning, MCU/Linux split, resource budget,
and installation cost remain open. Battery-aware operation is only relevant to
future off-grid deployments. No arrows specify wiring or voltage compatibility.

## Related Views

[UNO Q references](../references.md) · [Data plan](../data-plan.md) ·
[Acquisition](components/acquisition.md) · [Architecture index](README.md)
