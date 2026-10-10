# Physical Deployment

- Diagram ID: `pv-deployment`
- Level: Deployment
- Status: Proposed integration; secured hardware is recorded, interfaces unverified.
- Parent: [Parent view](architecture.md)

## Diagram

```mermaid
flowchart LR
    phone["Phone RGB camera / replaces unavailable thermal camera"]
    replay["Historical SOLARMA replay / separate demo source"]
    plant["Customer PV plant"]
    logger["Inverter or logger / field adapter TBD"]
    mini["Secured mini panel R1123 / small test fixture"]
    sensors["Secured AHT20, Light Sensor P v1.1 and ACS70331"]
    shield["Secured Seeed Studio Base Shield / interfaces TBD"]
    lcd["Secured Grove 16x2 LCD / local status proposed"]
    power["HRS1358, 1000mAh LiPo and HAS4966 / supply design pending"]
    subgraph uno["Secured Arduino UNO Q 4GB + Media Carrier"]
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
    mini -->|Candidate current test after verification| sensors
    sensors -->|Connections and pin mapping TBD| shield
    shield -->|Acquisition interface TBD| mcu
    mcu -->|Display path TBD| lcd
    logger -->|Verified read-only interface TBD| app
    mcu -->|Observation bridge TBD| app
    power -->|Supply compatibility pending| uno
    app <-->|Records, mappings and queue| storage
    app -->|Local interface TBD| local
    app <-->|Authenticated synchronization when connected| platform
    platform -->|Role-scoped remote views| users
```

## Explanation

The UNO Q 4GB with Media Carrier is secured for proposed local inference and
history analysis. The selected phone RGB camera replaces the unavailable Grove
thermal camera. Phone transfer is unverified; no permanent phone installation or
thermal acquisition is in the current prototype scope. Historical replay is
imported independently of the phone scene.

The [hardware inventory](../hardware.md) records all secured and missing items.
The Seeed Studio Base Shield is selected instead of the Grove shield v2. Sensor
and LCD paths are logical integration intentions, not verified wiring. No
breadboards are available; cables, adapters, and pin mapping still need checking.

HRS1358 replaces the unavailable Waveshare charger as the charging candidate.
The battery, mini panel, and step-down converter are secured components, not an
assembled or validated supply. The diagram does not establish their wiring order
or sufficient power for the UNO Q. AHT20/light readings supply context, and the
current sensor targets a compatible small test circuit. These are not thermal
imaging or full-plant instrumentation.

A field device needs verified logger compatibility or instrumentation for each
claimed channel. One inverter input can represent several parallel strings;
channel topology must be verified before promising string-level coverage.
Exact module location needs a surveyed image-to-panel/string mapping or additional
measurements. Device count and electrical interfaces depend on plant topology.

Power supply, enclosure, network provisioning, MCU/Linux split, resource budget,
and installation cost remain open. Battery-aware operation is only relevant to
future off-grid deployments. No arrows specify wiring or voltage compatibility.

The [prototype electrical wiring](../hardware-connections.md) records the
USB-powered assembly reported in PR #49, including selected Grove interfaces.
It does not establish the battery/solar supply or the full deployment above.

## Related Views

[UNO Q references](../references.md) · [Data plan](../data-plan.md) ·
[Hardware inventory](../hardware.md) · [Acquisition](components/acquisition.md) ·
[Architecture index](README.md)
