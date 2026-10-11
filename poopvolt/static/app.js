"use strict";

const $ = (id) => document.getElementById(id);
const names = {
  dust: "Dust",
  bird_dropping: "Bird dropping",
  visible_damage: "Visible damage",
};
let file = null;
let inspection = null;
let isDemo = true;
let ready = false;
let uploading = false;
let previewUrl = null;
let overlaysVisible = true;
let viewRevision = 0;

function status(message, error = false) {
  $("status").textContent = message;
  $("status").classList.toggle("error", error);
}

function updateControls() {
  $("run").disabled = !file || !ready || uploading;
  for (const id of ["camera", "library"]) {
    $(id).disabled = uploading;
    $(id).parentElement.classList.toggle("disabled", uploading);
  }
  $("demo").disabled = uploading;
  $("new").disabled = uploading;
}

function setMode(demo) {
  isDemo = demo;
  for (const [id, active] of [
    ["demo", demo],
    ["new", !demo],
  ]) {
    $(id).classList.toggle("active", active);
    $(id).setAttribute("aria-pressed", String(active));
  }
  $("demo-watermark").hidden = !demo;
  $("capture-tools").hidden = demo || inspection !== null;
  $("overlay-toggle").disabled = !inspection;
}

async function readResponse(response) {
  const result = await response.json();
  if (!response.ok)
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : "The request could not be processed.",
    );
  return result;
}

async function checkHealth() {
  try {
    const response = await fetch("/api/health", { cache: "no-store" });
    const health = await response.json();
    ready = health.model_ready === true;
    $("health").textContent = ready
      ? health.busy
        ? "Edge busy"
        : "Edge ready"
      : "Model pending";
    $("health").classList.toggle("ready", ready);
    if (!isDemo && !inspection && !file && !uploading)
      status(
        ready
          ? file
            ? "Ready to run your inspection."
            : "Choose a photograph to begin."
          : "Photo preview is available. Real inspection needs the trained model.",
      );
  } catch {
    ready = false;
    $("health").textContent = "Edge unreachable";
    $("health").classList.remove("ready");
    if (!isDemo && !inspection && !file && !uploading)
      status("Cannot reach the edge. Check your Wi-Fi connection.", true);
  }
  updateControls();
}

function clearPreview() {
  if (previewUrl) URL.revokeObjectURL(previewUrl);
  previewUrl = null;
}

function newInspection() {
  viewRevision += 1;
  file = null;
  inspection = null;
  clearPreview();
  setMode(false);
  history.replaceState(null, "", "/?mode=capture");
  $("results").hidden = true;
  $("share").hidden = true;
  $("overlay").replaceChildren();
  $("original").hidden = true;
  $("photo").hidden = true;
  $("original-empty").hidden = false;
  $("processed-empty").hidden = false;
  $("source-tag").textContent = "Your photograph";
  $("filename").textContent = "No photograph selected";
  $("dimensions").textContent = "";
  $("processed-caption").textContent = "Waiting for an inspection";
  $("latency").textContent = "";
  $("view-label").textContent = "New inspection";
  $("view-description").textContent =
    "Capture or choose a photograph to get started.";
  status(
    ready
      ? "Choose a photograph to begin."
      : "Photo preview is available. Real inspection needs the trained model.",
  );
  updateControls();
}

function chooseFile(event) {
  const selected = event.target.files[0];
  if (!selected) return;
  if (selected.size > 12 * 1024 * 1024) {
    status("Choose a photograph smaller than 12 MiB.", true);
    event.target.value = "";
    return;
  }
  newInspection();
  file = selected;
  previewUrl = URL.createObjectURL(selected);
  $("original").src = previewUrl;
  $("original").hidden = false;
  $("original-empty").hidden = true;
  $("filename").textContent = selected.name;
  $("source-tag").textContent = "Original";
  $("view-description").textContent =
    "Your original photo. Run an inspection to see the processed view.";
  status(
    ready
      ? "Photograph selected. Ready for inspection."
      : "Photograph selected. The trained model is still pending.",
  );
  updateControls();
  event.target.value = "";
}

function svgElement(tag, attributes) {
  const element = document.createElementNS("http://www.w3.org/2000/svg", tag);
  for (const [key, value] of Object.entries(attributes))
    element.setAttribute(key, value);
  return element;
}

function renderFindings() {
  if (!inspection) return;
  const selected = $("panel-select").value;
  const predictions = inspection.predictions.filter(
    (item) => !selected || item.id === selected || item.panel_id === selected,
  );
  const overlay = $("overlay");
  overlay.replaceChildren();
  overlay.setAttribute(
    "viewBox",
    `0 0 ${inspection.width} ${inspection.height}`,
  );
  overlay.toggleAttribute("hidden", !overlaysVisible);
  const fontSize = inspection.width / 42;
  const ordered = [...predictions].sort(
    (a, b) => (a.kind !== "panel") - (b.kind !== "panel"),
  );
  for (const item of ordered) {
    const [x, y, width, height] = item.box;
    const group = svgElement("g", {
      class: `detection ${item.kind}${item.id === selected ? " selected" : ""}`,
    });
    group.append(svgElement("rect", { x, y, width, height, rx: 5 }));
    if (item.kind !== "panel") {
      const text = svgElement("text", {
        x: x + 6,
        y: Math.max(fontSize + 5, y - 10),
        "font-size": fontSize,
      });
      text.textContent = isDemo
        ? item.label
        : `${item.label} ${Math.round(item.confidence * 100)}%`;
      group.append(text);
    }
    if (item.kind === "panel") {
      group.setAttribute("tabindex", "0");
      group.setAttribute("role", "button");
      group.setAttribute("aria-label", `Select panel ${item.id}`);
      const select = () => {
        $("panel-select").value = item.id;
        renderFindings();
      };
      group.addEventListener("click", select);
      group.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          select();
        }
      });
    } else group.style.pointerEvents = "none";
    overlay.append(group);
  }
  const defects = predictions.filter((item) => names[item.kind]);
  $("findings-title").textContent = isDemo
    ? selected
      ? "One example area to review."
      : "Two areas worth a look."
    : `${defects.length} area${defects.length === 1 ? "" : "s"} to review.`;
  $("capabilities").replaceChildren();
  for (const [kind, name] of Object.entries(names)) {
    const count = predictions.filter((item) => item.kind === kind).length;
    const supported = inspection.capabilities.includes(kind);
    if (isDemo && supported && count === 0) continue;
    const chip = document.createElement("span");
    chip.className = `finding-chip ${kind}${supported ? "" : " unsupported"}`;
    chip.textContent = isDemo
      ? supported
        ? `${name} · example`
        : `${name} · not illustrated`
      : supported
        ? `${name} · ${count}`
        : `${name} · unsupported`;
    $("capabilities").append(chip);
  }
  $("predictions").replaceChildren();
  for (const item of predictions) {
    const row = document.createElement("span");
    row.className = "prediction";
    row.textContent = isDemo
      ? `${item.label} · illustrative box`
      : `${item.label} · ${(item.confidence * 100).toFixed(1)}%`;
    $("predictions").append(row);
  }
  if (!predictions.length)
    $("predictions").textContent =
      "No detections above the threshold. This does not establish a clean or undamaged panel.";
  $("recommendation").textContent =
    inspection.recommendation ||
    "No supported defect detections. Review the photograph before deciding on an intervention.";
  $("recommendation-note").textContent = isDemo
    ? "Example next step for this visual demo. No model inference or maintenance assessment has run."
    : "Detection-based review rule, not a model maintenance score.";
}

function showImages(result) {
  clearPreview();
  for (const id of ["original", "photo"]) {
    $(id).src = result.image_url;
    $(id).hidden = false;
  }
  $("original-empty").hidden = true;
  $("processed-empty").hidden = true;
  $("results").hidden = false;
  $("capture-tools").hidden = true;
  $("overlay-toggle").disabled = false;
  $("dimensions").textContent = `${result.width} × ${result.height}`;
  $("panel-select").replaceChildren(new Option("All panels", ""));
  let panelNumber = 0;
  for (const item of result.predictions.filter(
    (prediction) => prediction.kind === "panel",
  ))
    $("panel-select").append(new Option(`Panel ${++panelNumber}`, item.id));
  overlaysVisible = true;
  $("overlay-toggle").textContent = "Annotations on";
  $("overlay-toggle").setAttribute("aria-pressed", "true");
  $("details").open = false;
  renderFindings();
}

async function showDemo() {
  const revision = ++viewRevision;
  file = null;
  inspection = null;
  setMode(true);
  updateControls();
  $("share").hidden = true;
  history.replaceState(null, "", "/");
  $("view-label").textContent = "Visual demo";
  $("view-description").textContent =
    "Sample photograph · illustrative annotations · no model run";
  const image = new Image();
  image.src = "/static/demo-panel.png";
  try {
    await image.decode();
  } catch {
    if (revision === viewRevision)
      status(
        "The sample photograph could not load. Choose Your photo to preview your own image.",
        true,
      );
    return;
  }
  if (revision !== viewRevision) return;
  const width = image.naturalWidth,
    height = image.naturalHeight;
  // Design-only annotations. Never returned by the API or applied to uploaded photos.
  const examples = [
    ["panel-a", "Panel 1", "panel", [0.015, 0.025, 0.475, 0.9], null],
    ["panel-b", "Panel 2", "panel", [0.52, 0.025, 0.47, 0.9], null],
    ["demo-dust", "Dust", "dust", [0.025, 0.49, 0.16, 0.4], "panel-a"],
    [
      "demo-bird",
      "Bird dropping",
      "bird_dropping",
      [0.65, 0.25, 0.06, 0.11],
      "panel-b",
    ],
  ];
  inspection = {
    image_url: image.src,
    width,
    height,
    capabilities: ["panel", "dust", "bird_dropping"],
    predictions: examples.map(([id, label, kind, box, panel_id]) => ({
      id,
      label,
      kind,
      panel_id,
      box: [box[0] * width, box[1] * height, box[2] * width, box[3] * height],
    })),
    recommendation: "Review the marked areas and consider cleaning.",
  };
  showImages(inspection);
  $("source-tag").textContent = "Sample photo";
  $("filename").textContent = "solar-panels-demo.png";
  $("processed-caption").textContent = "Illustrative overlays";
  $("latency").textContent = "No inference run";
  $("model").textContent =
    "AI-generated sample photograph with hand-placed annotations for layout review. No trained model, confidence scores, or measured latency.";
  $("association-note").textContent =
    "This demo is never saved as an inspection. Your uploaded photographs use only real model outputs.";
  status("Explore the demo, select a panel, or turn annotations off.");
}

function showInspection(result) {
  viewRevision += 1;
  inspection = result;
  setMode(false);
  showImages(result);
  $("source-tag").textContent = "Original";
  $("filename").textContent = `Inspection ${result.id.slice(0, 8)}`;
  $("processed-caption").textContent = "Model detections";
  $("latency").textContent = `${result.inference_ms.toFixed(2)} ms`;
  $("model").textContent =
    `${result.model} · ${new Date(result.created_at).toLocaleString()} · measured preprocessing, inference and postprocessing`;
  $("association-note").textContent =
    "Defects are associated by box-center containment, using the smallest containing panel. Unsupported categories do not have predictions.";
  $("view-label").textContent = "Saved inspection";
  $("view-description").textContent =
    "Original photograph and real model detections.";
  history.replaceState(null, "", result.url);
  $("share-url").value = new URL(result.url, location.origin).href;
  $("share").hidden = false;
  status(`Inspection saved. ${result.predictions.length} model detections.`);
}

async function runInspection() {
  if (!file || !ready || uploading || isDemo) return;
  uploading = true;
  updateControls();
  status("Uploading and inspecting your photograph…");
  const body = new FormData();
  body.append("image", file);
  try {
    showInspection(
      await readResponse(await fetch("/api/inspect", { method: "POST", body })),
    );
  } catch (error) {
    status(
      error.message || "Upload failed. Check your Wi-Fi connection.",
      true,
    );
  } finally {
    uploading = false;
    updateControls();
    await checkHealth();
  }
}

$("demo").addEventListener("click", showDemo);
$("new").addEventListener("click", newInspection);
$("camera").addEventListener("change", chooseFile);
$("library").addEventListener("change", chooseFile);
$("panel-select").addEventListener("change", renderFindings);
$("run").addEventListener("click", runInspection);
$("overlay-toggle").addEventListener("click", () => {
  overlaysVisible = !overlaysVisible;
  $("overlay").toggleAttribute("hidden", !overlaysVisible);
  $("overlay-toggle").textContent = overlaysVisible
    ? "Annotations on"
    : "Annotations off";
  $("overlay-toggle").setAttribute("aria-pressed", String(overlaysVisible));
});
$("copy").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText($("share-url").value);
    status("Inspection link copied.");
  } catch {
    $("share-url").focus();
    $("share-url").select();
    status(
      "Copy the selected link and open it on another device on this network.",
    );
  }
});
$("original").addEventListener("load", () => {
  if (!inspection)
    $("dimensions").textContent =
      `${$("original").naturalWidth} × ${$("original").naturalHeight}`;
});
for (const id of ["original", "photo"])
  $(id).addEventListener("error", () =>
    status(
      "Could not display the photograph. Use JPEG, PNG or WebP; saved images may have expired.",
      true,
    ),
  );

const fmt = (value, digits, unit) =>
  value === null || value === undefined || Number.isNaN(value)
    ? "–"
    : `${Number(value).toFixed(digits)} ${unit}`;

async function pollStation() {
  let data = { available: false };
  try {
    data = await (await fetch("/api/station", { cache: "no-store" })).json();
  } catch {
    data = { available: false };
  }
  const r = data.reading;
  $("station").classList.toggle("stale", !data.available);
  $("station-age").textContent = !r
    ? "No station data"
    : data.available
      ? `Updated ${data.age_s}s ago`
      : `Stale · last update ${Math.round(data.age_s)}s ago`;
  $("st-temp").textContent = fmt(r?.temp_c, 1, "°C");
  $("st-rh").textContent = fmt(r?.rh_pct, 0, "%");
  $("st-light").textContent = r ? String(r.light_raw) : "–";
  $("st-current").textContent = fmt(r?.pv_ma, 0, "mA");
  $("st-perf").textContent = fmt(r?.perf_pct, 0, "%");
  $("st-perf-note").textContent = !r
    ? "relative to a clean panel"
    : !r.calibrated
      ? "not calibrated yet"
      : r.perf_pct === null
        ? r.sun_elev_deg < 25
          ? "sun too low for the model"
          : "no panel current"
        : "vs. clean panel · clear-sky model";
}

async function start() {
  pollStation();
  setInterval(pollStation, 2000);
  await checkHealth();
  const match = location.pathname.match(/^\/inspections\/([0-9a-f-]+)$/i);
  if (match) {
    newInspection();
    try {
      showInspection(
        await readResponse(await fetch(`/api/inspections/${match[1]}`)),
      );
    } catch (error) {
      status(error.message, true);
    }
  } else if (new URLSearchParams(location.search).get("mode") === "capture")
    newInspection();
  else await showDemo();
}
start();
