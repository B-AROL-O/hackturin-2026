# Physical Deployment

- Diagram ID: `pv-deployment`
- Level: Deployment
- Status: Proposed draft; implementation and hardware choices are unverified.
- Parent: [Parent view](architecture.md)

## Diagram

```mermaid
flowchart TB
    pv["Photovoltaic installation"]
    power["Battery and power subsystem"]
    sensors["Electrical and environmental sensors"]
    cameras["RGB and thermal cameras"]
    subgraph uno["Arduino UNO Q 4GB"]
        mcu["MCU-side acquisition - proposed"]
        app["Linux-side edge application - proposed"]
        storage[("Local storage")]
    end
    operator["Operator access device"]
    pv -->|Measured electrical behavior| sensors
    pv -->|Visible and thermal observations| cameras
    power -->|Regulated supply - design pending| uno
    sensors -->|Sensor interfaces - TBD| mcu
    mcu -->|Observation bridge - TBD| app
    cameras -->|Image interfaces - TBD| app
    app <-->|Records and history| storage
    app -->|Local interface - TBD| operator
```

## Explanation

The UNO Q is the intended edge platform. The MCU/Linux responsibility split, sensor and camera connections, regulated power supply, storage medium, and operator access method need hardware verification. Arrows show intended connections and do not specify wiring or voltage compatibility.

The [prototype electrical wiring](../hardware-connections.md) records the
USB-powered assembly reported in PR #49, including selected Grove interfaces.
It does not establish the battery/solar supply or the full deployment above.

## Related Views

[UNO Q references](../references.md) · [Acquisition](components/acquisition.md) · [Architecture index](README.md)
