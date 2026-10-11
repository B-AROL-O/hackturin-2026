# Six-scene storyboard and English narration

Production decision (2026-10-11): the latest user direction requires the supplied
**original replay chart and canonical technical-insert colors**. That instruction
supersedes earlier brand-export requirements below. The film uses the original
chart unchanged, with local Source Sans 3 for external graphics. Both original
series are visible from the hard cut; external result labels appear together at
80 s. The chart stays completely still, including 85–93 s. See
[implementation](implementation.md) for the implemented workflow.

Timing decision (2026-10-11): on-screen reveals in V01, V04, and V06 follow the
recorded narration, so visuals no longer run ahead of or behind the voice. Scene
windows, narration, and all shots and copy are unchanged; the film stays 120 s.

Status: English adaptation of [the current pitch](../../docs/pitch-narrative.md),
with user-selected English voiceover. Preserve the canonical six intervals.
[Timing data](timing.json) is authoritative for frame arithmetic. Intervals are
start-inclusive, end-exclusive. Read only the quoted narration when recording.
Beat times are local to each scene. All visible copy is English.

Use [the supplied media](assets/README.md), the exact original logo, and
[brand rules](../../brand-guidelines.md). Full logo composition appears on white
in the opening and closing, with attribution **Suncheckers · hackTurin 2026**.

## V01 — The hook

**00:00–00:12 · frames 0–359 · pitch anchor `pv-title`**

Narration:

> Your solar plant is covered in shit. Literally. But how much is that affecting
> production? That is the question behind PoopVolt.

Screen copy: **How much is it affecting production?**
Visible status: **Illustrative scene**.
Assets: `panel-rgb.svg`, `pigeon.svg`, `Logo_PoopVolt.png`.
Sources: `pv-narrative`, `pv-brand`, `pv-logo`.

0–3 s: white canvas, a stylized panel, one restrained pigeon entrance. The panel's
`deposit` layer appears once; pause on “Literally.” 4–7 s: the panel reduces
beside the production question. 7–12 s: settle the complete original logo on
white, preserving all its elements, aspect ratio, and clear space. Keep the
illustrative label attached to the separate panel artwork. The cartoon is not
the logo: never detach or animate the bird inside the official composition.

Do not attach a loss number to the deposit. Translate the approved strong hook
faithfully, without extending that tone into the technical explanation.
Transition: the separate panel illustration becomes the owner's installation.

## V02 — The company and owner's problem

**00:12–00:30 · frames 360–899 · pitch anchor `pv-problem`**

Narration:

> An older solar plant still works. But its owner cannot tell whether it produces
> as much as it should. The maintenance company needs clear evidence to explain
> why an inspection is worth considering.

Screen copy: **It works. But is it performing as expected?**
Role labels: **Owner**, **Maintenance company / technician**.
Assets: `plant-owner.svg` as a conceptual setting.
Sources: `pv-narrative`, `pv-pitch`, `pv-context`.

0–5 s: panel expands into a simple plant composition. 5–10 s: owner enters on the
right, technician on the left. 10–15 s: the question connects to the technician's
inspection request. 15–18 s: hold the two roles and the need for understandable
evidence. Use one generous composition; no dashboard or free-device sales offer.

Visible qualification: **Illustrative owner scenario**. The roles are proposed
users, not a confirmed customer or Coesa partnership.
Transition: the question becomes the comparison frame in V03.

## V03 — Make the production gap understandable

**00:30–00:50 · frames 900–1499 · pitch anchor `pv-pipeline`**

Narration:

> PoopVolt compares observed production with an expected reference over the same
> period. Today, we have a comparison between inverters. A theoretical reference
> adjusted for environmental conditions is the next step. A deviation tells us
> where to investigate, not what caused it.

Screen copy: **Observed / Expected**, **Peer comparison: available**,
**Environmental theoretical reference: future work**, and
**Deviation → Investigate**.
Sources: `pv-narrative`, `pv-comparison`, `pv-data-plan`.

0–5 s: introduce observed/expected labels with a shared **Same period** bracket.
5–11 s: show the available peer-comparison method using plain labeled inverter
symbols, without drawing a pretend time series. 11–16 s: show the theoretical
reference as a dashed future-work region. 16–20 s: hold **A flag is not a diagnosis**.
No numerical result appears until the separate replay scene.

Blue means observed; grey dashed means expected/estimated; yellow outlines the
question to investigate. Labels carry the meaning too. Define Edge AI only if a
later technical cut needs it; it is not the central value proposition here.
Transition: clean cut to real prototype media, keeping its scope label visible.

## V04 — Show the actual electrical schematic

**00:50–01:15 · frames 1500–2249 · pitch anchor `pv-prototype`**

Narration:

> The prototype uses Arduino UNO Q with temperature, humidity, light, a display,
> and NFC. The schematic also shows the current sensor between the panel and the
> charging system. Zero current has been checked; measurements under light still
> need validation. The board runs on USB power, separate from the solar branch.

Screen copy: **Prototype electrical schematic**, **UNO Q: USB-powered**,
**Current: zero checked; under-light measurement pending**.
Persistent status: **Prototype / reported bring-up**.
Assets: `pv-wiring.svg`, `prototype-bench-01.jpg`, `prototype-bench-02.jpg`,
`prototype-outdoor.jpg`. Sources: `pv-narrative`, `pv-wiring`, `pv-wiring-svg`.

0–3.3 s: show the complete electrical sheet. In a narrow adjacent photo strip,
show `prototype-bench-01.jpg` for 0–1.8 s, then `prototype-bench-02.jpg` for
1.8–3.3 s. Labels say **Prototype photo**, without inventing measurements.
3.3–8 s: move to readable focused schematic views of UNO Q/Grove connections:
I2C to AHT20/LCD, then UART to NFC with A0 to light. Use external large
captions; preserve the original symbols and nets.
8–19.5 s: focus on **Panel → Current sensor → Waveshare → LiPo**: the sensor in
series on the panel wire, the charger, then A1.
Use `prototype-outdoor.jpg` as a small context insert for at least 3 seconds,
marked **Prototype setup photo · USB connected**, while the solar path remains
legible. 19.5–25 s: return to the complete sheet and hold the integration
limits.

The two bench photographs are similar, so use the second for a purposeful close
view, not a second identical full-screen shot. Photos retain their natural colors.
Show the laptop USB supply; do not crop it out to imply a self-powered board.
Do not draw or animate Waveshare USB OUT feeding UNO Q: it is not connected.
Do not treat LCD text visible in a photograph as a validated solar-current test.
The schematic, connection record, and captions determine the claim scope.

Transition: hard cut to the independent historical replay. Do not turn this
prototype's panel or LCD into SOLARMA inverter data.

## V05 — One concrete software result

**01:15–01:40 · frames 2250–2999 · pitch anchor `pv-evidence`**

Narration:

> In a replay of SOLARMA's historical data, we compare thirteen inverters. From
> August first to September seventeenth, twenty nineteen, inverter one reports
> zero energy against roughly two hundred and ninety-two kilowatt-hours expected
> from its peers. The software flags it for inspection. This is historical replay,
> not our panel's measurement or a soiling diagnosis.

Screen copy: **HISTORICAL REPLAY · SOLARMA · 13 inverters**,
**1 Aug–17 Sep 2019 · Inverter 1**, **Observed: 0 kWh**,
**Expected from peers: ≈292 kWh**, **Candidate for inspection**.
Asset: `comparison-inverter-1-replayed.svg`.
Sources: `pv-narrative`, `pv-comparison`, `pv-comparison-chart`.

0–5 s: introduce the actual chart with axes, units, legend, period, and provenance
visible from its first frame. 5–10 s: reveal both original series together,
without changing or accumulating their values. 10–18 s: hold the graph completely
still for at least eight seconds. 18–22 s: add a restrained yellow outline and
external **Candidate for inspection** callout. 22–25 s: hold
**Historical data · cause unconfirmed · benefit unmeasured**.

Use the original data/geometry; migrate chart styling through its generator,
not by hand-editing the exported SVG. The canonical chart can support an initial
animatic; validate a brand export before delivering the final film. Never reuse
legacy `cards/04-evidence.png`: its 550 kWh figure has a different window.
The reference is estimated from peers, not the future theoretical model.
No confidence percentage, string label, causal dirt overlay, or recovered-energy
curve belongs here.

Transition: the inspection flag becomes a technician review, keeping owner and
technician positions consistent with V02.

## V06 — From inspection to an understandable proposal

**01:40–02:00 · frames 3000–3599 · pitch anchor `pv-decision`**

Narration:

> The technician investigates and proposes cleaning, repair, or replacement where
> needed. The owner decides. Afterward, comparable measurements must verify the
> benefit; the full gap may not be recoverable. PoopVolt turns a production gap
> into an understandable intervention proposal.

Screen copy: **Investigate → Propose → Choose → Measure**.
Closing descriptor: **Evidence for photovoltaic maintenance**.
Attribution: **Suncheckers · hackTurin 2026**.
Sources: `pv-narrative`, `pv-maintenance`, `pv-brand`, `pv-logo`.

0–3 s: return to technician and owner; the technician's proposal is explicitly
human-reviewed. 3–6 s: reveal cleaning/repair/replacement as options, then owner
choice. 7–14 s: show a next-measurement placeholder labeled **Verify benefit**,
not an invented improvement. 14–17 s: settle the complete original logo on white
with the descriptor and team attribution outside its clear space. 17–20 s: hold
all final content still; narration finishes by 117 s and audio fades before 120 s.

Visible qualification while describing the workflow: **Proposed workflow · field
benefit unmeasured**. End without an invented URL, QR code, sponsor adoption,
ROI claim, or automatic intervention. The final message is the brand proposition,
not a promise that the replay produced a service order.

## Voice recording and subtitles

Record six separate narration takes, identified V01–V06. Pronounce PoopVolt as
“poop volt,” UNO Q as “oo-no cue,” NFC as letters, SOLARMA as “so-lar-ma,” and
kilowatt-hours in full. Keep the hook deadpan and the explanation composed.
Begin speech around 0.3–0.6 s into a scene; finish at least 0.5 s before the next
boundary. V06 must finish by local 17 s for the three-second closing hold.

These are recording windows, not subtitle timestamps. Align captions to actual
chosen audio after editing. Re-record an overlong take before changing the fixed
120-second schedule. Do not reuse the old Devpost SRT: it describes a different
cut, language treatment, and replay window.
