# PoopVolt data and demonstration plan

Status: Proposed ingestion and evaluation plan. External files were inspected on
2026-10-10. Since then the SOLARMA importer, replay and a scoped peer comparison
have been implemented ([comparison results](comparison-results.md)); no trained
model or phone dataset exists yet.

## Expected-production reference for the owner narrative

The [three-minute story](pitch-narrative.md) adds a proposed theoretical
expected/observed production comparison. No selected model, implementation,
calibration, or evaluation is established by this PR.

Define the reference's inputs, model/version, plant capacity, orientation,
inclination, operating period, and required weather/environment data. Record
their source, units, uncertainty, and missingness. Compare like-for-like power
or energy over matching periods; rated power alone is not an energy forecast.

The existing SOLARMA replay lacks populated irradiance and verified string
topology. It cannot independently validate a weather-adjusted theoretical model
or establish string-level loss. Obtain the missing metadata/data, limit the
result to a scoped channel comparison, or show a labeled simulation. Relative
light from the secured sensor is not a calibrated irradiance measurement.

Keep observed, estimated, and simulated values distinct. A deviation is not a
confirmed cause, historical degradation, or guaranteed recoverable energy.
Validation needs independent observations and comparable post-intervention data.

Before presenting the MVP, link its actual implementation, dataset, executed
revision, and output. An STL view shows a design concept; link the file and
identify its purpose when supplied. Neither artifact is implemented by this PR.

## Two independent supporting evidence paths

The single-string scene comes from a phone camera. Whole-plant replay comes from
historical SOLARMA inverter logs. These sources describe different plants and
times. Demonstrate them separately; do not attach a replay anomaly to the
phone's simulated deposit or infer its production loss from the historical logs.

In this proposal, a **line** means a PV string. An inverter input/channel is not
necessarily one string. A physical wiring map must establish that relationship.

## Whole-plant source: SOLARMA

- Repository:
  [SOLARMA/pv-analysis-tools](https://github.com/SOLARMA/pv-analysis-tools).
- Inspected revision: `fc96313e453978fc89211322a8afb966b85f7913`.
- [Pinned data tree](https://github.com/SOLARMA/pv-analysis-tools/tree/fc96313e453978fc89211322a8afb966b85f7913/data).
- Source: SOLPEV Danfoss Comlynx Weblogger exports. The repository contains two
  overlapping export folders and a plotting notebook. These are observations
  from one installation, not a labeled collection of independent plants.
- License: Repository-level MIT license. Preserve its notice when reusing files;
  confirm the intended use of identifiable plant records before a field pilot.

The following inventory comes from parsing the actual tab-separated files, not
the logger's advertised full historical range. Record counts exclude headers.

<!-- markdownlint-disable MD013 -->

| Export folder                         | Details records / devices       | Details timestamp range              | Summary records | Event records |
| ------------------------------------- | ------------------------------- | ------------------------------------ | --------------- | ------------- |
| `2019-09-26-solpev-danfoss-weblogger` | 9,477 / 13 inverter device IDs  | 2019-09-01 17:40 to 2019-09-25 23:10 | 438             | 2,353         |
| `2019-10-05-solpev-danfoss-weblogger` | 58,687 / 13 inverter device IDs | 2019-07-01 12:10 to 2019-10-05 12:50 | 4,067           | 19,018        |

<!-- markdownlint-enable MD013 -->

Use the larger export as the first replay candidate; the smaller one overlaps
and is not an independent test set. The details contain inverter power, daily
energy, temperature, AC measurements, three DC voltage/current input pairs,
status/error fields, and device identity. Summary files contain plant power and
daily energy. Events contain logger messages and inverter reports.

### Limits found in the inspected files

- Parse as tab-separated text with Latin-1 decoding; trim header whitespace and
  verify units and timestamps. The irradiance unit header has an encoding
  artifact.
- Irradiance and irradiance-energy values in the larger summary are empty. They
  cannot supply a weather normalization baseline.
- DC input coverage differs by inverter: the third input is zero for some
  devices and active for others. Its physical configuration is unverified; zero
  is not evidence of a failed string.
- Missing values occur, including AC frequency and entirely empty fields. Keep
  missing distinct from measured zero. The example notebook fills missing values
  with zero; that behavior is unsuitable for fault inference.
- Thirteen device IDs refer to inverters, not thirteen panels or strings. The
  files do not provide a surveyed panel/string layout or RGB/thermal images.
- Error/event messages are contextual observations, not verified soiling,
  hotspot, failure-time, or repair-outcome labels. Check message semantics
  before using them as targets. Nighttime zeros and communication outages need
  handling.
- The supplied time span does not establish multi-year degradation or economic
  returns. Whole-plant summary and details have different timestamp coverage.

### Proposed telemetry evaluation

Pin downloaded bytes and preserve source file hashes in an ingestion record.
Start with parsing, coverage checks, device/channel plots, and a simple
baseline. Compare compatible channels only after accounting for capacity,
orientation, weather, operating state, and known downtime. Where these are
unknown, label underperformance as a candidate requiring inspection rather than
assigning cause.

Develop a lightweight edge ML anomaly/trend model only against a defined
baseline. Split evaluation chronologically, with separate fitting and held-out
periods; do not randomly mix neighboring samples or overlapping exports. Any
injected fault is synthetic and measures behavior on that injection only.
Predictive maintenance needs later failure/intervention records, a forecast
horizon, and evaluation of advance warning and false alerts. One plant cannot
establish fleet generalization.

## Single-string source: phone RGB capture

The phone RGB camera is the selected replacement for the unavailable Grove
thermal camera. The [hardware inventory](hardware.md) records secured parts and
missing equipment. Thermal acquisition is deferred from the current prototype;
phone model and image transfer remain to be selected.

Capture a panel or clearly labeled panel mockup in clean, simulated dust,
simulated droppings, and mixed conditions. Keep simulation method and ground
truth separate from the inference input. Include shade, reflections, blur,
different angles, and no visible contamination as controls. Use a reversible
simulation on a mockup or removable surface; record which surface was actually
photographed.

Assign a demo plant/string/panel ID manually and annotate image regions for
visible deposits. The mapping is declared setup information, not a string ID
inferred from pixels. Split evaluation by capture session/scene so neighboring
frames of the same deposit cannot appear in both training and evaluation.

The proposed outputs are visible contamination class, image-region location,
mapped asset identity, and an uncertainty/review state. Evaluate classification
and localization separately, including incorrect classes and missed deposits. A
phone RGB image cannot measure heat, electrical continuity, or lost kWh.
Thermal/electrical claims require separately acquired, aligned observations.

The secured AHT20, light sensor, and ACS70331 current sensor provide proposed
additional prototype context once integrated. Ambient temperature is not thermal
imagery, relative light is not a calibrated irradiance baseline, and current
alone is not power or energy. Keep any small-panel test observations separate
from the historical SOLARMA plant and label their actual capture/setup
provenance.

## Proposed observation and finding contract

Keep this design contract separate from the presentation's illustrative fixture.

- Identity: observation ID, plant ID, inverter/channel ID when known, optional
  string/panel ID, and mapping version with verification status.
- Provenance: phone simulation, historical replay, or field measurement; source
  revision/file hash or capture session; observation time and ingestion time.
- Payload: modality, units, measured values or image reference, quality flags,
  missingness, coverage, and operating context. Timestamp/timezone rules remain
  to be verified against each source.
- Finding: class or unknown, evidence references, uncertainty, localization
  scope (plant/channel/string/panel/image region), and model/rule version.
- Recommendation: action and reason, missing evidence, operator review required,
  owner acceptance for service work, and economic assumptions if available.

Unknown string mapping must remain unknown. Whole-plant coverage reports include
configured, observed, stale, and unmapped channels. Replay time is distinct from
wall-clock time and remote views visibly identify historical observations.

## Acceptance for the next prototype

Demonstrate each path on the intended edge hardware, including missing/stale
inputs and unknown mapping. Record evaluated code/model revision, held-out data,
classification/localization or anomaly results, latency, memory and power draw.
Then demonstrate queued synchronization, own-plant versus company access, and
intervention recording. These are planned checks, not completed experiments.

See [Diagnostics](architecture/components/diagnostics.md),
[Maintenance](architecture/components/maintenance.md), and the
[reference index](references.md).
