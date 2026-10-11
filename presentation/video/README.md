# PoopVolt Remotion video handoff

Status: Implemented local Remotion production with bundled synthesized English
narration. See [implementation.md](implementation.md) for working commands and
[review.md](review.md) for delivery verification.

Create exactly **120 seconds with English voiceover**, following the current
[pitch narrative](../../docs/pitch-narrative.md). These duration and language
requirements were selected by the user. Follow
[brand-guidelines.md](../../brand-guidelines.md), use the exact supplied
PoopVolt logo, include the existing prototype photographs, and give the
canonical electrical diagram its dedicated scene.

## Read and implement

1. [Storyboard](storyboard.md): complete English narration, screen copy, shot
   choreography, sources, and qualifications.
2. [Timing data](timing.json): authoritative six-scene frame schedule.
3. [Design and sound](design.md): brand, typography, motion, captions, audio.
4. [Asset inventory](assets/README.md): logo, photographs, illustrations,
   electrical schematic, replay chart, rights, and reproduction.
5. [Implementation](implementation.md): implemented Remotion structure,
   commands, reproduction steps, and editorial decisions.
6. [Coding-agent task](agent-task.md): ready-to-use implementation instruction.

[Handoff review](handoff-review.md) records the pre-production handoff checks;
[delivery review](review.md) records the implemented film's verification.

## The story

**A production gap becomes an understandable intervention proposal.**

Keep the six beats of the current pitch, in their existing order:

- A pigeon and an illustrative deposit open the production question.
- An older plant works, but its owner cannot assess whether it performs well.
- The maintenance company needs clear observed-versus-expected evidence.
- The electrical schematic shows the prototype and its actual integration limits.
- One scoped SOLARMA historical replay flags an inverter for inspection.
- The technician investigates and proposes; the owner decides; later comparable
  measurements verify whether the intervention helped.

The main audience is the plant owner and the photovoltaic maintenance company.
The opening humor establishes the name; evidence drives the rest. Keep the
company/technician and owner as separate recurring roles. Off-grid use,
forecasting, free-device distribution, and Coesa adoption are supporting
hypotheses, not the central pitch or established partnerships.

## Fixed requirements and production defaults

<!-- markdownlint-disable MD013 -->

| Property                | Requirement or default                                                          |
| ----------------------- | ------------------------------------------------------------------------------- |
| Duration                | Exactly 120 seconds, including transitions and final hold                       |
| Voiceover / screen copy | English, including an English translation of the approved hook                  |
| Canvas                  | 1920 × 1080, 16:9                                                               |
| Frame rate              | 30 fps; 3600 frames, numbered 0–3599                                            |
| Story                   | Six scenes from the current narrative; 12, 18, 20, 25, 25, 20 seconds           |
| Brand                   | Blue/yellow/white/greys; original full logo on white                            |
| Team attribution        | Suncheckers; keep product, team, and event names separate                       |
| Mandatory media         | Three supplied prototype photos, electrical schematic, replay chart, exact logo |
| Output                  | Full HD voiced MP4, captioned MP4, SRT, transcript, poster, QA record           |

<!-- markdownlint-enable MD013 -->

The current canonical script is Italian. This handoff translates it into the
user-requested English film while retaining its timing, narrative, and evidence
scope. The older [English Devpost package](../../docs/video/README.md) contains
useful photographs but a different script and evaluation window. Do not combine
its 550 kWh extended-window claim or existing subtitles with this video's
292 kWh evaluation-window example.

## Evidence authority

Resolve claims against the [architecture index](../../docs/architecture/README.md)
and [source registry](../sources/README.md). The comparison exists as a historical
peer replay; the environmental theoretical model remains future work. The
prototype wiring records USB-powered UNO Q bring-up and a separate solar
charging path. Current-sensor zero is reported checked; current under light still
needs validation. Do not imply the solar branch powers the board.

Use the recorded replay window, **1 August–17 September 2019**, with
**inverter 1: observed 0 kWh, approximately 292 kWh expected from peers**.
A flag requests inspection. It does not identify dirt, confirm a fault's cause,
establish mapped-string behavior, or promise recoverable energy.

Keep the illustrative deposit, prototype photos, and replay graph visibly
independent. The software supplies the peer flag; the technician supplies the
intervention proposal. Do not fabricate forecasts, thermal readings, field
savings, recovery curves, or a working automatic maintenance policy.

## Current delivery status

The project, pinned lockfile, local Source Sans 3 fonts, synthesized English
narration, captions, score and render commands are implemented. Outputs live in
`out/`; [review.md](review.md) records the actual checks. The exact transcript is
[transcript.md](transcript.md), and the timeline is [beat-map.json](beat-map.json).

The latest direction preserves the supplied original replay chart and canonical
technical colors. Earlier requirements to restyle that chart are superseded;
the source generator and evidence exports are unchanged. A finished communication
artifact does not establish validated PoopVolt field performance.
