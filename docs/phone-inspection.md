# Phone-to-edge inspection

Status: implemented software slice with placeholder model artifacts. The trained
model, export configuration, accuracy, and UNO Q latency still require testing.
No trained ONNX artifact, existing inference utility, or dashboard was present in
this checkout. Model placeholders are intentional; the API emits no predictions
until a configured graph loads and passes a startup forward/decoder check.

## Start on the UNO Q Linux side

Run in the Python environment that already provides OpenCV 4.12 and numpy.
The phone and laptop must be on the same Wi-Fi network as the UNO Q. The board
must have a reachable LAN address; access-point client isolation must be off.

From a checkout on the board:

```sh
cd hackturin-2026
python3 -c 'import cv2, numpy; print(cv2.__version__, numpy.__version__)'
python3 -m venv --system-site-packages .venv-uno
.venv-uno/bin/python -m pip install .
```

If the board lacks venv/ensurepip, install that Debian prerequisite first:

```sh
sudo apt-get update
sudo apt-get install python3-venv
```

The `--system-site-packages` option reuses the board's cv2/numpy installation.
Do not install the `desktop` extra on the board. If the import check fails,
locate the existing OpenCV-enabled Python interpreter before proceeding; this
service does not require Docker or install a replacement CV runtime.

Start the service, including before model delivery:

```sh
POOPVOLT_MODEL="$PWD/models/inspection.onnx" \
POOPVOLT_MODEL_CONFIG="$PWD/models/inspection.json" \
POOPVOLT_STORAGE="$PWD/data/inspections" \
  .venv-uno/bin/poopvolt-inspect
```

The process binds `0.0.0.0:8000`, with one worker and one model instance. Keep
this terminal running. Do not add `--workers`, a second process using the same
storage directory, or a reload watcher. Model loading includes one startup
validation forward pass; inference otherwise runs only for submitted photos.

Find the board's Wi-Fi IPv4 address:

```sh
hostname -I
```

Open `http://<UNO-Q-WIFI-IP>:8000/` on the phone. The frontend is shipped as
plain, browser-ready HTML/CSS/JavaScript inside the Python package, served by
FastAPI at the same origin. There is no Node build or frontend runtime to install.
Camera capture uses the file input; it works on a LAN HTTP URL without requesting
browser streaming-camera permission. **Choose photo** uses a separate input
without the capture hint. Browser/OS camera behavior varies; HEIC needs conversion
to JPEG, PNG, or WebP before upload.

## Tested route on our UNO Q: Arduino's Python image, no sudo

On our board the system Python has neither OpenCV nor numpy, and `python3-venv`
needs sudo, so the venv route above does not work as written. Arduino's
preinstalled image `ghcr.io/arduino/app-bricks/python-apps-base:0.5.0` already
has Python 3.13, OpenCV 4.12, numpy, FastAPI, uvicorn and Pillow. Only
`python-multipart` is missing, and it is a pure-Python wheel. The `arduino` user
can run Docker without sudo. Tested 2026-10-11 over the venue Wi-Fi.

1. Join the board to Wi-Fi (no sudo needed). Keep passwords out of the repository.
   `nmcli device wifi connect "<SSID>" password "<password>"`, then `hostname -I`.
2. From the laptop, copy the package (`ADB` is the adb bundled with the Arduino core):

   ```sh
   uvx pip download "python-multipart>=0.0.20,<1" --only-binary=:all: --no-deps -d /tmp/wh
   $ADB shell mkdir -p /home/arduino/hackturin-2026/data/inspections
   $ADB push poopvolt models /tmp/wh/python_multipart-*.whl /home/arduino/hackturin-2026/
   $ADB shell 'cd ~/hackturin-2026 && python3 -m zipfile -e python_multipart-*.whl vendor-web'
   ```

3. On the board, start the station receiver so the dashboard gets live
   readings (see [UNO Q setup](uno-q-setup.md)), then the server:

   ```sh
   cd ~/station && setsid nohup python3 -u station_rx.py --csv station.csv \
     --latest latest.json > station_rx.log 2>&1 < /dev/null &
   docker run -d --name poopvolt --restart unless-stopped -p 8000:8000 \
     -v /home/arduino/hackturin-2026:/app -v /home/arduino/station:/station:ro \
     -w /app -e PYTHONPATH=/app:/app/vendor-web \
     -e POOPVOLT_STATION=/station/latest.json \
     -e POOPVOLT_STORAGE=/app/data/inspections \
     -e POOPVOLT_MODEL=/app/models/inspection.onnx \
     -e POOPVOLT_MODEL_CONFIG=/app/models/inspection.json \
     --entrypoint python3 ghcr.io/arduino/app-bricks/python-apps-base:0.5.0 \
     -m poopvolt.server
   ```

4. Open `http://<board-ip>:8000/` on the phone. `docker logs poopvolt` shows the
   server log; `docker rm -f poopvolt` stops it. The container restarts with the
   board.

The dashboard's **UNO Q station** strip polls `GET /api/station` every 2 s. The
endpoint returns `{"available", "age_s", "reading"}` from the JSON file that
`station_rx.py --latest` rewrites once per second (`POOPVOLT_STATION`). The
reading is reported unavailable when it is older than 10 s.

Stored inspections can be removed from the dashboard: **Delete inspection** on a
saved result (`DELETE /api/inspections/{id}`), or **Clear all photos on the
board** (`DELETE /api/inspections`, returns `{"removed": n}`). Both ask for
confirmation and are refused with 429 while an inspection is running. Without
them, storage still prunes the oldest inspections beyond 100 or 250 MB.

## Supply the actual trained model

`models/inspection.onnx` and `models/inspection.json` are placeholders and are
not supplied. `models/inspection.example.json` demonstrates the configuration
schema; it is not the trained model's class list or a claim of supported classes.

1. Copy the actual trained ONNX artifact to `models/inspection.onnx`.
2. Copy the example JSON to `models/inspection.json`, then replace the name,
   input size, and **entire class list in exactly the training/export order**.
3. Map each real class to `panel`, `dust`, `bird_dropping`, `visible_damage`, or
   `other`. Only configured kinds appear as supported capabilities. Do not add
   categories absent from the model merely to populate the dashboard.
4. Verify that the export matches the contract below, then restart the server.

The initial adapter deliberately supports one contract: an Ultralytics-style
YOLOv8 **detection** export, batch 1, square fixed input, raw float32 tensor
`[1, 4 + class_count, detection_count]`. Coordinates are decoded
`center_x, center_y, width, height` in input pixels, followed by class
probabilities with no separate objectness. There is one output, and no embedded
NMS, segmentation masks, or keypoints. RGB pixels are normalized by `1/255`,
aspect-ratio preserving resize uses centered padding of 114, and the input size
must match the export. Predictions are mapped back to stored photograph pixels,
clipped, filtered, and subject to per-class NMS. At most 100 detections are saved.

Check these settings against the trained exporter before hardware testing.
Output shape validation cannot establish that class order, preprocessing, or
coordinate semantics are correct. If the delivered model uses another contract
(such as a classifier or NanoDet), implement its actual preprocessing/decoder;
changing the JSON format name alone will not work. No generic model is substituted.
The preprocessing/output distinctions follow the
[OpenCV YOLO guidance](https://docs.opencv.org/4.12.0/da/d9d/tutorial_dnn_yolo.html).

## API and storage

| Endpoint                          | Behavior                                                                        |
| --------------------------------- | ------------------------------------------------------------------------------- |
| `POST /api/inspect`               | Exactly one multipart `image` file; 201 with persisted metadata and predictions |
| `GET /api/inspections/{id}`       | Metadata, model name/capabilities, pixel boxes, confidence and latency          |
| `GET /api/inspections/{id}/image` | Stored JPEG photograph                                                          |
| `GET /api/health`                 | API/model readiness, model error, busy state and supported categories           |

API smoke check once the actual model is configured:

```sh
curl http://127.0.0.1:8000/api/health
curl -F 'image=@panel.jpg;type=image/jpeg' http://127.0.0.1:8000/api/inspect
```

An absent/incompatible model returns 503 for health and inspection; the dashboard
and existing saved inspections remain available. Concurrent uploads/inference
receive 429 and `Retry-After: 2`; there is no background queue. The busy gate is
held during upload, decoding, inference, and persistence. CPU work runs outside
the API event loop so reads/health remain responsive.

Uploads allow JPEG, PNG, and single-frame WebP only, checked by both MIME and
decoded format. Files are capped at 12 MiB, multipart bodies at 12 MiB + 64 KiB,
and images at 24 million pixels and 10,000 pixels per side. Streamed requests
are bounded too. Corrupt/empty uploads, unsupported formats and excessive sizes
receive 422, 415 and 413 respectively. Invalid multipart forms may receive 400.

Ordinary JPEG bytes are preserved. EXIF-rotated JPEGs and other accepted formats
are normalized to an upright RGB JPEG before inference/storage so overlay
coordinates agree across browsers. There is no crop or resize of the stored
photograph. PNG transparency is flattened by conversion to RGB.

Metadata is a JSON file paired with a UUID-named JPEG. Startup cleans interrupted
writes. Retention runs at startup and after each successful save, deleting the
oldest records until both limits are met: **100 inspections and 250 MiB total**.
Expired records/images return 404. Store paths and limits live in
`poopvolt/server.py`; only model/config/storage paths have environment overrides.
This is a single-process local tool without authentication; anyone who can reach
its LAN port can upload and retrieve inspection IDs they know. Keep it on the
intended local network.

## Reading the dashboard

The home page opens a visual demo for UI review: an AI-generated panel photo is
shown beside the same image with illustrative SVG annotations. The demo is
marked both above the images and on the annotated view. It has no confidence
scores or latency, makes no inference request, and is never saved as an
inspection. Choose **Your photo**, **Choose photo**, or **Camera** to leave the
demo and use your own photograph. A new photo is never assigned demo annotations.

The inspection UI uses the lightweight `poopvolt/static/logo.svg`.
The SVG is a provisional inspection-UI concept mark; the supplied team logo in
`assets/brand/` and its [provenance](../assets/brand/README.md) remain intact.
The sample photo is `poopvolt/static/demo-panel.png`, created with the built-in
image-generation
tool from this prompt: a natural smartphone photo of two rooftop photovoltaic
panels, with dust on the lower left panel and a small bird dropping on the right,
daylight, visible cells, and no text, labels, boxes, or logos. The exact prompt is
saved in [demo-panel.prompt.txt](../poopvolt/static/demo-panel.prompt.txt).

Original and processed views appear side by side on desktop and stack on phones.
The processed view renders the original photo with SVG annotations rather than
storing a second bitmap. Annotations can be toggled off; inspection details are
collapsed by default to keep the primary image comparison minimal.

An inspection's permanent path is `/inspections/<id>` until retention removes it.
Copy the displayed URL to open the same persisted image/results on the laptop.
Clipboard access may be unavailable on plain HTTP; the page then selects the
link for manual copying. No re-inference is needed on a second device.

SVG boxes use stored photograph dimensions. Choose a detected panel in the
dropdown or select its box; defects are associated by box-center containment,
using the smallest containing panel when boxes overlap. This geometric heuristic
is disclosed and is not a model panel-identity prediction. Unassigned defects
remain visible in the entire-photograph view. No panel boxes are invented if
the model only detects defects.

Scores are real detector confidences, not severity, percentage soiling, power
loss, thermal faults, or electrical degradation. Unsupported categories are
explicitly labeled. Zero detections do not establish a clean or undamaged panel.
The suggested next step is an explicitly labeled review rule: emitted visible
damage recommends a technician inspection; dust/bird droppings suggest reviewing
the photo and considering cleaning. Without defect detections there is no
intervention recommendation. Recommendations apply to the whole inspection.

`inference_ms` measures preprocessing, OpenCV forward, and postprocessing with a
monotonic clock. It excludes upload, JPEG decode/normalization, persistence and
startup loading. The dashboard displays the stored measured value. UNO Q latency
is unmeasured for the eventual model; see the existing
[board budget](uno-q-model-budget.md) for previous benchmark context.

## Development and verification

On a laptop:

```sh
uv sync --extra desktop
uv run --extra desktop poopvolt-inspect
uv run --extra desktop pytest -q
```

Tests execute a tiny **synthetic, untrained ONNX graph** through actual OpenCV
4.12 to verify the decoder, API, pixel coordinates, NMS, orientation, persistence,
limits, retention and serialization. It exists only in pytest temporary storage
and is never a production model or dashboard fallback. Hardware/model validation
remains pending: supply the artifact, check known images against the exporter,
then perform the phone capture → POST → UNO Q inference → SVG review → laptop
link acceptance sequence and record actual CPU latency.
