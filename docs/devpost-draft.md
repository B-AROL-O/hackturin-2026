# Devpost submission draft

Status: Draft of 2026-10-10 for issue #39 (WBS 6.4), refreshed on 2026-10-11
for release 0.2.0 (phone inspection slice, video kit). The description was
written from [project status](project-status.md) and the repository readme. Re-check
every claim against the repository on the day you submit; the checklist at the
end lists what is likely to change.

## Fields to fill in

| Devpost field | Value                                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Project name  | PoopVolt                                                                                                                  |
| Tagline       | Edge AI maintenance evidence for older solar plants                                                                       |
| Challenge     | **Beyond Solar**                                                                                                          |
| Built with    | Arduino UNO Q, Arduino Bridge, Seeed Grove (AHT20, light, ACS70331 current, LCD, PN532 NFC), Python, FastAPI, OpenCV, ONNX, uv, pytest, KiCad |
| GitHub        | <https://github.com/B-AROL-O/hackturin-2026>, release <https://github.com/B-AROL-O/hackturin-2026/releases/tag/v0.2.0>    |
| Video         | Link to the 2-minute video (issue #37); script and cards in [docs/video](video/README.md)                                 |
| Team          | Giacomo Lisita, Gianpaolo Macario, Lorenzo Palloni, Federico Nebuloni                                                     |
| Images        | Wiring schematic (`docs/architecture/diagrams/pv-wiring.svg`), system diagram (from the readme), a photo of the prototype |

## Short fields (paste into Devpost)

Devpost's elevator pitch field is limited to 200 characters; check the count
in the form.

- **Elevator pitch (181 characters):** Is your old solar plant producing
  what it should? PoopVolt compares expected and observed output on an Arduino
  UNO Q, so a service company can show the owner why to clean or repair.
- **Shorter alternative (94 characters):** Edge AI on an Arduino UNO Q
  that turns a gap in solar output into evidence an owner can judge.
- **Tagline:** Edge AI maintenance evidence for older solar plants.

## Description (paste into Devpost)

### Inspiration

Your solar plant is covered in bird droppings. Literally. The real question is
how much that matters.

Take an owner whose photovoltaic plant was installed years ago. It still
produces, but nobody can tell whether it produces as much as it should. The
service company that looks after it has the mirror-image problem: how do you
persuade an owner to inspect or clean a plant that apparently works? Dust, wear
and droppings are possible causes, but an intervention needs evidence the owner
can understand and judge for themselves.

### What it does

PoopVolt is a proposed maintenance aid built around an Arduino UNO Q. It turns
a gap in production into a proposal an owner can understand:

- **Expected versus observed production.** Compare what a plant produced with an
  expectation over the same period and show the gap with its uncertainty. Today
  we demonstrate a peer-relative version on replayed data (each inverter against
  its peers); a weather-adjusted theoretical reference is the proposed next
  step. The gap is a place to look, not a diagnosis, and not guaranteed
  recoverable energy.
- **Visible soiling from a phone photo.** Classify clean, dust or droppings on a
  panel and mark the affected region. A phone RGB camera replaces the thermal
  camera we could not get, so we make no claim about hotspots or lost energy.
  The phone-to-board upload, inspection page and image comparison work in
  software; the trained classifier is still pending.
- **A technician-reviewed proposal.** A short evidence summary a service
  company can use to explain a cleaning, a repair or a replacement.

On the device itself, the UNO Q reads temperature, humidity, light and panel
current, shows the latest values on a small LCD, and exposes them as NFC tag
text that a technician's phone can read without any network.

### How we built it

- **Hardware:** UNO Q 4GB with a Seeed Grove Base Shield, an AHT20 temperature
  and humidity sensor, a light sensor, an ACS70331 current sensor, a 16x2 LCD
  and a PN532 NFC module, plus a separate solar charging path (mini panel,
  Waveshare solar manager, LiPo). We drew an editable KiCad schematic of the
  prototype as built.
- **Firmware:** an Arduino sketch reads the sensors, drives the LCD, acts as an
  NFC tag, and streams readings once per second to the board's Linux side over
  the Bridge.
- **Software:** a Python package (`poopvolt`) imports and replays historical
  inverter logs from SOLARMA's open data (MIT licence): units checked, missing
  values kept missing (never turned into zero), outages reported rather than
  filled, and a replay that steps through the history in time order. On top of
  it, a comparison fits each inverter's typical ratio to its peers on the first
  part of the season and checks it on the later part (never overlapping), with
  an uncertainty band.
- **Phone inspection:** a FastAPI service takes a JPEG from a phone over the
  local network, validates and stores it with bounded retention, runs an OpenCV
  ONNX detection adapter on the CPU, and shows the original beside an annotated
  view on an inspection page. The trained model is a placeholder: the adapter
  stays unavailable until a model passes a startup check, no result is mocked,
  and the home-page demo is labelled and never saved as inference. Tests use a
  synthetic untrained graph, so they check the plumbing, not accuracy.
- **Evidence we measured or replayed:**
  - CPU-only inference on the UNO Q: NanoDet-Plus at 416x416 in 258 ms and
    YOLOX-S at 640x640 in 2.27 s (reference models, not our own).
  - The SOLARMA export loads as 58,687 detail rows from 13 inverters, with
    1,157 communication outages and no irradiance values.
  - **Replayed:** of the 12 inverters with a baseline, 2 are flagged as
    producing unusually little compared with their peers (one stopped
    producing in late July; one fell about 25 % below its peers). Why is not
    in the data.
  - **Replayed, the improvement over today:** inverter 1 kept logging but
    produced nothing from 21 July to the end of the record on 3 October,
    except on one day. Nothing in the data shows the output being restored in
    those 75 days. On the 30 days with a peer reference, it fell about 550 kWh
    short of its peers (a lower bound, because days without a reference are
    not counted). A daily peer check puts it below 70 % of its expected output
    on 21 July, its first day without production.
  - **Simulated:** injecting a synthetic loss into the other inverters, it is
    flagged in all 10 tested cases from 8 % upwards, in 4 of 10 at 4 to 6 %,
    and mostly not at 2 %. We chose the flag threshold after seeing the data,
    so this is a demonstration of the method, not an independent validation.
    Charts and method: [comparison results](comparison-results.md).
  - Approximate prototype cost: about 145, from single-unit list prices. This
    is a prototype cost, not a production cost.

### What works, and what does not (yet)

Working at bring-up level: sensors, LCD and NFC on the UNO Q; readings
streamed to the Linux side; the SOLARMA importer and replay; the schematic and
bill of materials. Working as a scoped demo on replayed data: the peer
comparison with its uncertainty band, plus a labelled synthetic-loss test.
Working in software: the phone upload API, local image store and inspection
page.

Not implemented at the time of writing: a weather-adjusted theoretical
expected production (the replayed data has no irradiance), a trained soiling
classifier (no accuracy or UNO Q latency figure exists yet), the wider
maintenance output and the 3D-printable enclosure. Where the video or the demo
shows these, they are labelled as simulations. The solar charging path is wired
but not yet verified in sunlight.

### Challenges

Our thermal camera and one solar charger were unavailable, so we switched to a
phone RGB camera and a different charger. The historical data has no
irradiance and no verified string layout, so it cannot support a
weather-adjusted baseline or any claim about individual strings; we say so
instead of inventing one. We also kept phone-photo simulation and historical
replay apart: they come from different plants and times and are not evidence
of each other.

### What we learned

Doing less honestly beats claiming more. Tracking whether each number is
measured, replayed or simulated shaped the design as much as any sensor
choice.

### What is next

Define a weather-adjusted expected-production reference with a service
company, run the comparison on our own panel as well as on replayed data, train
and evaluate a soiling classifier on a labelled phone photo set, and add a
technician-reviewed output to the operator UI.

### Built with and reuse

We built the firmware, the importer and replay, the peer comparison, the phone
inspection service and page, the wiring record, the schematic and the
documentation during the hackathon. We reuse the Arduino UNO Q tooling and
libraries, the Adafruit and Grove drivers, SOLARMA's MIT-licensed data (notice
kept in `data/solarma/NOTICE.md`), and open tools such as FastAPI, OpenCV,
ONNX, KiCad, uv and pytest. The full list is in [project status](project-status.md). The
repository is MIT licensed.

## Beyond Solar requirements check

Each challenge requirement, the evidence in this draft, and what is still weak.
Adapted from the requirement mapping of the earlier SunCheck work breakdown.

- **A PV panel with at least one other component.** Covered: mini panel, solar
  manager and LiPo, with panel current read by the ACS70331 on A1. The charging
  path is not yet verified in sunlight.
- **Collect data from the system or the environment.** Covered: temperature,
  humidity, light and panel current on the UNO Q, plus the replayed SOLARMA
  inverter logs.
- **Interpret data locally and produce a concrete response.** Partly covered.
  The board shows readings on the LCD and as NFC tag text, but does not
  interpret them yet. The peer comparison uses only the Python standard
  library, so it can run on the board's Linux side, but it has not been run
  there. Its response is a list of inverters to inspect. Run it on the board
  before submitting, or say in the description where it runs.
- **Start from a well-defined user, context and problem.** Covered: the owner
  of an older plant and the service company that maintains it. We showed our
  progress to Matteo Stoppa (Coesa) on 10 and 11 October; he told us they have
  no data at all today ([notes](company/coesa-energy.md)). That supports the
  problem but is not an approval of our solution, so say "discussed with", not
  "validated by". The questions on the reference model, data access and the
  free-device model are still unanswered (issue #13).
- **Show the improvement with a practical test and numbers.** Covered on replayed data. The
  evidence list now states it for the replay: inverter 1 produced nothing for
  75 days without being restored, and a daily peer check points at it on the
  first day. It is still one inverter in one plant, and the 70 % rule was
  chosen after seeing the data. Issue #35 should carry the same number.

## Before you submit

Hard deadline: Sunday 11 October 2026, 16:00 CEST; aim for 15:30.

- [ ] Run `python3 -m poopvolt.report` on the UNO Q (the package needs only
      the standard library), or say in the description where the comparison
      runs.
- [ ] Copy the improvement number into the headline summary (issue #35).
- [ ] Update "What works" and "Not implemented" to match
      [project status](project-status.md) on the day.
- [ ] Add the video link, and check it opens in a logged-out browser.
- [ ] Add a photo of the prototype and the two diagrams; a screenshot of the
      inspection page is optional and must keep its "demo" label.
- [ ] Re-run `uv run python -m poopvolt.report` if the comparison changes, and
      re-copy the numbers into the evidence list (issue #35); keep each one
      labelled as measured, replayed or simulated.
- [ ] If the video shows the comparison, show the chart with its "replayed" or
      "simulated" label visible.
- [ ] Confirm that every link, including the GitHub repository, opens logged
      out.
- [ ] Select the challenge **Beyond Solar** and add all four team members.
- [ ] Submit, then keep a dated screenshot of the confirmation.

<!-- EOF -->
