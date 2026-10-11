# Demo video (issue #37)

Status: Script and assets for the two-minute Devpost video, agreed on
2026-10-11. English narration; the opening line stays in Italian with an
English subtitle. Every scene shows only what exists today and labels whether
it is staged, replayed or a prototype at bring-up level. Features that are not
built appear only on the "Not built yet" card.

## Timeline

<!-- markdownlint-disable MD013 -->

| Time      | Scene            | On screen                                                                                 | Label on screen                        |
| --------- | ---------------- | ----------------------------------------------------------------------------------------- | -------------------------------------- |
| 0:00–0:12 | Hook             | Mini panel with fake droppings, close-up                                                  | `cards/01-staged-label.png` overlay    |
| 0:12–0:22 | Problem: owner   | `cards/02-owner.png`                                                                      | none                                   |
| 0:22–0:32 | Problem: company | `cards/03-company.png`                                                                    | none                                   |
| 0:32–0:42 | Evidence: run    | Screen recording of the command below                                                     | none (the output names its source)     |
| 0:42–1:12 | Evidence: result | `cards/04-evidence.png` (chart and figures)                                               | built into the card ("REPLAYED")       |
| 1:12–1:35 | Prototype        | Phone footage: UNO Q with Grove sensors, the LCD readings, a phone tapping the NFC reader | `cards/05-prototype-label.png` overlay |
| 1:35–1:50 | Not built yet    | `cards/06-next.png`                                                                       | built into the card                    |
| 1:50–2:00 | Close            | `cards/07-close.png`                                                                      | none                                   |

<!-- markdownlint-enable MD013 -->

The narration is about 210 words, roughly 1:45 at a calm pace, which leaves
margin for pauses. Keep the cut at or below 2:00.

## Narration

**0:00 Hook.** _Il tuo impianto è sporco di merda._ (pause) _Letteralmente._
But the real question is: how much is it costing you?

**0:12 Problem.** Owners of older solar plants can't tell whether they still
produce what they should. The companies that maintain them have the mirror
problem: how do you convince an owner to inspect a plant that apparently works?
They need evidence the owner can understand.

**0:32 Evidence.** PoopVolt compares what each inverter produced with what its
peers say it should have produced. We replayed a real plant's 2019 logs:
thirteen inverters, about fifty-nine thousand records. Inverter one kept
reporting, but produced nothing from the twenty-first of July until the record
ends in October: seventy-five days, about five hundred and fifty kilowatt-hours
short of its peers. A daily peer check points at it on day one. A flag is not a
diagnosis; it tells the technician where to look.

**1:12 Prototype.** On site, an Arduino UNO Q reads temperature, humidity,
light and panel current, shows them on a display, and hands them to a
technician's phone over NFC, with no network needed.

**1:35 Not built yet.** Next: a weather-adjusted expected production, and
soiling detection from a phone photo. We have not built those yet.

**1:50 Close.** PoopVolt turns a production gap into a proposal an owner can
understand. Team B-AROL-O, hackTurin 2026.

If the comparison has been run on the UNO Q before filming, add to the
prototype scene: "The same analysis runs on the board's Linux side." Do not say
it otherwise.

## Screen recording for the evidence scene

From the repository root, in a terminal with a large font:

```bash
uv run python docs/video/show_evidence.py
```

It prints one line per inverter for the evaluation window and marks inverters
1 and 9 for inspection; it writes nothing. The 292 kWh it shows for inverter 1
covers 1 August to 17 September only; the card's 550 kWh counts from 21 July.
It needs the pinned data in `data/solarma/raw/`; download it first with
`uv run python -c "from poopvolt import solarma; solarma.fetch('data/solarma/raw')"`.

## Shot list for the phone footage

1. Hook: the mini panel with fake droppings, close and steady, 5 seconds.
2. Prototype, wide: the UNO Q, Base Shield and Grove sensors on the bench.
3. Prototype, close: the LCD showing live readings.
4. Prototype, NFC: a phone tapping the PN532 and showing the readings text.

Film landscape, 1920x1080, in good light. Do not show the thermal camera, a
cloud dashboard or anything that suggests features that do not exist.

## Assets

- `cards/*.svg`: card sources, 1920x1080, in the presentation's draft palette
  ([visual design](../../.agent/visual-design.md)).
- `cards/*.png`: rendered cards. The two `*-label.png` files are transparent
  overlays.
- `cards/chart-inverter-1.svg`: copy of
  `docs/images/comparison-inverter-1-replayed.svg`, made by the build script.
- `subtitles.srt`: English subtitles for the whole video. Re-time them to the
  final cut.

Rebuild the PNG files after changing a card or the chart:

```bash
docs/video/build.sh
```

The script needs Docker; it renders with `rsvg-convert` and DejaVu Sans.

## Upload

Upload as unlisted or public on YouTube or Vimeo, then check that the link
opens in a logged-out browser and add it to the
[Devpost draft](../devpost-draft.md).

<!-- EOF -->
