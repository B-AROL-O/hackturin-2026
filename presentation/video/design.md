# Brand, motion, and sound direction

Production decision (2026-10-11): the latest user direction requires the supplied
**original replay chart and canonical technical-insert colors**. That instruction
supersedes earlier brand-export requirements below. The film uses the original
chart unchanged, with local Source Sans 3 for external graphics. Both original
series are visible from the hard cut; external result labels appear together at
80 s. The chart stays completely still, including 85–93 s. See
[implementation](implementation.md) for the implemented workflow.


Status: Production direction for the six-scene English film. Follow the supplied
[brand guidelines](../../brand-guidelines.md), which the user explicitly selected.
They govern identity; the current pitch and architecture govern factual claims.

## Brand application

Use exactly these colors for newly authored graphic elements:

| Token         | Value     | Role                                              |
| ------------- | --------- | ------------------------------------------------- |
| PoopVolt blue | `#0D2D44` | Main text, observed series, occasional dark field |
| Solar yellow  | `#F5C329` | Selected evidence and investigation callouts      |
| White         | `#FFFFFF` | Logo canvas and primary surfaces                  |
| Light grey    | `#F4F5F7` | Secondary surfaces, uncertainty regions           |
| Text grey     | `#52606D` | Captions and estimated references                 |
| Divider grey  | `#D8DEE4` | Nonessential dividers                             |

Use mostly white/light surfaces with blue text. Use blue text on yellow; never
small yellow text on white. Previous teal, rust, amber, and ivory colors are
excluded from this film's authored graphics. Keep photographic colors natural.
The electrical schematic retains its native functional colors for wires and pin
labels as a documented engineering-source convention, not decorative accents.
Do not recolor engineering nets by hand. The replay chart must receive a verified
brand export through its generator before the final film is delivered.

Use the exact `Logo_PoopVolt.png` supplied by the user. Show the full composition
on white in V01 and V06. Preserve aspect ratio, all elements, original colors,
and useful resolution. Do not replace its lettering with a font, recolor its
panel, remove the white background, split off its pigeon, add shadows, or use an
unreviewed dark/inverted variant. Keep at least half the visible letter P's height
as clear space around the visible composition, checking the graphic itself rather
than the PNG border. A small fade/translation of the entire logo is acceptable;
no rotation, warping, or animation of its internal parts.

Use **PoopVolt** for the product and **Suncheckers** for the team. Attribution
reads **Suncheckers · hackTurin 2026**. Do not infer an official meaning for the
fragmented yellow cell. Logo provenance and unresolved trademark permissions
remain as recorded in the brand asset documentation; code licensing is separate.

## Type and layout

Use local Source Sans 3 regular and semibold for graphics and subtitles, with
its license. Keep the logo typography inside its original image. Until fonts
are acquired, use one explicitly documented sans-serif fallback for all new
text. Existing Devpost cards use DejaVu and are not brand-aligned source artwork.

Design on 1920 × 1080. Use 96 px safe margins; headlines 72–88 px, body/diagram
callouts 38–44 px, status/source text 28–32 px. Reserve y=860–1010 for captions,
with status labels above that band. Technical inserts may contain smaller detail;
zoom to make the specific labels being discussed readable at 1280 × 720.
Recompose rather than shrinking important copy.

Use one primary claim and at most two columns per scene. Keep technician left
and owner right across V02 and V06. Full narration belongs in subtitles, not in a
paragraph pasted on the canvas. Preserve visible replay axes, units, source,
period, and limitations while highlighting the inspection flag.

## Motion vocabulary

Connect the illustrative hook to the owner's question, then the question to
comparison and review. Cut cleanly between the prototype and historical replay:
they are independent evidence sources. Use matched positions only for the
illustrative panel and recurring roles, not to imply paired measurements.

| Action                    | Initial budget                      |
| ------------------------- | ----------------------------------- |
| Text/callout entrance     | 12–18 frames; 16–32 px movement     |
| Relationship reveal       | 18–24 frames                        |
| Schematic reframing       | 24–36 frames, then held             |
| Cut/dissolve              | 6–9 frames inside fixed scene slots |
| Important claim hold      | At least 60 frames after settling   |
| Replay chart still hold   | At least 240 frames                 |
| Closing logo/message hold | Final 90 frames                     |

Use restrained easing with little or no overshoot for technical material. The
pigeon gets one gentle entrance. Avoid loops, particles, spinning boards,
wall-clock animation, flashing alarms, racing “live” data, and KPI count-ups.
Never animate energy flow as though it were measured prototype behavior.

The film is prerecorded; Reveal.js interaction and presenter builds do not
apply. A reduced-motion export is optional, using cuts/brief dissolves and frozen
camera moves. A standard MP4 cannot dynamically follow browser motion preferences.
Keep every claim readable when movement stops.

## Photos and technical inserts

Include all three supplied prototype photographs, using the assignments in
[the storyboard](storyboard.md). Preserve power connections and evidence context.
Do not remove the laptop USB cable or replace LCD readings. Do not treat a still
photograph as a live stream or annotate unvalidated electrical readings.

The schematic is mandatory for its full 25-second scene. Start and finish with
the complete sheet; focused views show UNO Q/Grove and then the separate solar
branch/current input. Add external large captions without modifying symbols or
nets. The source remains the native KiCad schematic and canonical export.

The SOLARMA chart is mandatory in V05. Preserve original values and geometry,
axes, units, date range, and legend. Update its generator with a video-brand
export profile: observed blue/solid/filled points, expected grey/dashed with an
estimate label, light-grey uncertainty/context regions, and yellow investigation
callouts. Verify underlying data and plotted coordinates unchanged. The canonical
chart can appear in an early animatic; the final film requires the reviewed
brand export. No old Devpost chart card is substituted.

## Voice, music, and effects

Record the exact English script from the storyboard. Aim for composed delivery,
roughly 125–145 words per minute, with pauses at claim changes. Record or generate
narration through available authorized means and record its source and permitted
use. Do not imitate a named person's voice. Final narration is production work.

Music is optional: one restrained instrumental bed without lyrics. Start well
below voice, duck during speech, and use short fades. A practical initial mix
target is approximately −16 LUFS integrated and true peak below −1 dBTP; those
are production targets, not event/platform rules. Check laptop and headphone
intelligibility. Use only a few quiet interface cues, without comedy splats or
alarms implying an established fault. Finish speech by 117 s and fade audio before
120 s.

If final narration is unavailable, deliver a clearly named silent animatic with
draft subtitles and retain audio as an open item. A silent draft is not a voiced
final film.

## Captions and accessibility

Deliver aligned English SRT and a captioned MP4. Use at most two subtitle lines,
approximately 42 characters per line, phrase-aware breaks, and no more than about
17 characters per second. Use white text on an opaque blue caption panel. Verify
PoopVolt, UNO Q, SOLARMA, NFC, and kWh manually against actual audio.

Status labels survive captions and transitions. Check normal text contrast at
4.5:1 and large text at 3:1. Use words, symbols, and line patterns in addition to
color. Inspect at 1280 × 720 and on a 390 CSS px player, using a full-screen
mobile view for detailed diagram reading. Supply the readable transcript for
people reviewing without audio or video.

Export one settled frame per scene and the final card as a poster. Watch the full
film with sound and once muted: both should convey the owner/company problem,
prototype limits, replay provenance, and technician/owner responsibilities.
