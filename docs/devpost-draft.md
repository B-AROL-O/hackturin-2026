# Devpost submission draft

Status: Draft of 2026-10-10 for issue #39 (WBS 6.4). The description was written
from [project status](project-status.md) and the repository readme. Re-check
every claim against the repository on the day you submit; the checklist at the
end lists what is likely to change.

## Fields to fill in

| Devpost field | Value                                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Project name  | PoopVolt                                                                                                                  |
| Tagline       | Edge AI maintenance evidence for older solar plants                                                                       |
| Challenge     | **Beyond Solar**                                                                                                          |
| Built with    | Arduino UNO Q, Arduino Bridge, Seeed Grove (AHT20, light, ACS70331 current, LCD, PN532 NFC), Python, uv, pytest, KiCad    |
| GitHub        | <https://github.com/B-AROL-O/hackturin-2026> (check it opens logged out)                                                  |
| Video         | Link to the 2-minute video (issue #37)                                                                                    |
| Team          | Giacomo Lisita, Gianpaolo Macario, Lorenzo Palloni, Federico Nebuloni                                                     |
| Images        | Wiring schematic (`docs/architecture/diagrams/pv-wiring.svg`), system diagram (from the readme), a photo of the prototype |

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
- **Evidence we measured or replayed:**
  - CPU-only inference on the UNO Q: NanoDet-Plus at 416x416 in 258 ms and
    YOLOX-S at 640x640 in 2.27 s (reference models, not our own).
  - The SOLARMA export loads as 58,687 detail rows from 13 inverters, with
    1,157 communication outages and no irradiance values.
  - **Replayed:** of the 12 inverters with a baseline, 2 are flagged as
    producing unusually little compared with their peers (one stopped
    producing in late July; one fell about 25 % below its peers). Why is not
    in the data.
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

Not implemented at the time of writing: a weather-adjusted theoretical
expected production (the replayed data has no irradiance), phone-photo soiling
detection, the operator UI and the 3D-printable enclosure. Where the video or
the demo shows these, they are labelled as simulations. The solar charging path is wired but not yet verified in
sunlight.

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

We built the firmware, the importer and replay, the wiring record, the
schematic and the documentation during the hackathon. We reuse the Arduino UNO
Q tooling and libraries, the Adafruit and Grove drivers, SOLARMA's MIT-licensed
data (notice kept in `data/solarma/NOTICE.md`), and open tools such as KiCad,
uv and pytest. The full list is in [project status](project-status.md). The
repository is MIT licensed.

## Before you submit

Hard deadline: Sunday 11 October 2026, 16:00 CEST; aim for 15:30.

- [ ] Update "What works" and "Not implemented" to match
      [project status](project-status.md) on the day.
- [ ] Add the video link, and check it opens in a logged-out browser.
- [ ] Add a photo of the prototype and the two diagrams.
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
