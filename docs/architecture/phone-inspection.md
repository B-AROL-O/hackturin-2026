# Phone Inspection Implementation

- Diagram ID: `pv-phone-inspection`
- Level: Runtime implementation
- Status: Implemented software; trained-model and UNO Q validation pending.
- Parent: [Application architecture](architecture.md)

```mermaid
sequenceDiagram
    actor Phone as Technician phone browser
    participant API as FastAPI on UNO Q Linux
    participant CV as Single OpenCV DNN model (CPU)
    participant Disk as JPEG + JSON storage
    actor Laptop as Laptop browser
    Phone->>API: GET / (same-origin static dashboard)
    Phone->>API: POST /api/inspect (multipart image)
    API->>API: Reject if busy or model unavailable; validate image
    API->>CV: Serialized preprocessing, forward, decoding
    CV-->>API: Detections + measured inference latency
    API->>Disk: Persist UUID-named JPEG and metadata; prune oldest
    API-->>Phone: Inspection ID, predictions and shared URL
    Phone->>API: GET /api/inspections/{id}/image
    Phone->>Phone: Render photograph + SVG overlays
    Laptop->>API: GET /inspections/{id}
    Laptop->>API: GET metadata + image
    Laptop->>Laptop: Render the same stored inspection
```

The code is [API](../../poopvolt/server.py),
[inference](../../poopvolt/inference.py),
[storage](../../poopvolt/storage.py), and
[dashboard](../../poopvolt/static/index.html).
This slice implements the RGB Acquisition/Diagnostics/Operator interface path.
It runs without the MCU, streaming cameras, sensor fusion, or remote services.
The eventual trained model and export settings are placeholders; no inference
results are emitted while unavailable. A model-based readiness check runs at
startup. Successful inspections run once per submitted photograph.

The detector's supported format, geometric panel association and conservative
recommendation rules are explicit in the
[setup/contract guide](../phone-inspection.md). These rules do not implement the
wider predictive-maintenance design. The data directory is single-process, bounded
to 100 records/250 MiB, and served at the same origin as the browser-ready UI.
Phone and laptop use the board's LAN HTTP address. Model accuracy, actual latency,
and phone/UNO Q hardware acceptance remain unverified.

The home page also includes a clearly labeled visual demo for UI review, with
an AI-generated sample photograph and hand-placed SVG annotations. It is static
frontend content, performs no inference, and writes no inspection record.
Real inspections retain the runtime sequence above. Original/annotated images
are shown together; the processed view uses the stored original plus SVG boxes.
