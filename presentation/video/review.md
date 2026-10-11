# Delivery QA and verification review

Reviewed on 2026-10-11 against `develop` at `b4d2b0e`, after the layout,
caption and narration-sync revision. Records the automated verification and
export checks for the implemented 120-second English Remotion pitch.

## Verification results

### 1. Timeline, frame count, and dimensions

- **Duration**: exactly 120.00 seconds (3600 frames at 30 fps).
- **Resolution**: 1920 × 1080 (16:9 editorial canvas).
- **Scene structure**: six contiguous scenes matching [timing.json](timing.json).
- **Reading holds** (maximum mean grey-level difference against the first frame):
  - Replay chart, 85–93 s (240 frames): 0.0019; the chart stays still.
  - Closing composition, 117–120 s (90 frames): 0.0; completely still.
- **Seek determinism**: frames 0, 2670 and 3599 rendered out of order are
  byte-identical on repeat.
- **Visual review**: 79 beat and scene-boundary frames inspected in
  `out/contact-sheet.png`; no text collisions, clipped schematic labels or
  overflowing boxes.

### 2. Audio and loudness

- **Voice synthesis**: English narration synthesized with Kokoro v1.0
  `af_heart` (236 words, 6 scenes). Audio is unchanged by this revision.
- **Score**: programmatic 120 BPM score with phrase ducking and an 85–93 s rest.
- **Integrated loudness**: −16.44 LUFS (ITU-R BS.1770 measurement; the
  production target is −16 LUFS, not the −23 LUFS EBU R128 broadcast level).
- **True peak**: −4.46 dBTP.

### 3. Typography, brand assets, and captions

- **Font**: bundled Source Sans 3 Regular and Semibold under SIL OFL 1.1.
- **Brand palette**: `#0D2D44` navy, `#F5C329` solar yellow, approved greys.
- **Canonical assets**: original logo, electrical schematic, three prototype
  photos and SOLARMA replay chart are byte-identical (hash-checked). The logo's
  near-white ground is whitened at render time only; see
  [implementation](implementation.md).
- **Captions**: SRT in `captions/poopvolt-120-en.srt`, burned into
  `out/poopvolt-120-en-captioned.mp4`. At most two lines of 42 characters,
  phrase-aware breaks, numerals for dates and quantities, typographic
  apostrophes. Timing is unchanged from the aligned audio.
- **Caption rate**: maximum 18.6 characters per second (V06 “PoopVolt turns a
  production gap”). Six cues exceed the ~17 cps guideline because they follow
  the recorded speech rate; fixing them requires a slower narration take.

### 4. Export hashes

<!-- markdownlint-disable MD013 -->

| Export                          | Duration               | Size        | SHA-256                                                            |
| ------------------------------- | ---------------------- | ----------- | ------------------------------------------------------------------ |
| `poopvolt-120-en.mp4`           | 120.00 s (3600 frames) | 1920 × 1080 | `5121095ed8bc15986d111562814b03393a43d5a65f792502bc2baac8069cc9fe` |
| `poopvolt-120-en-captioned.mp4` | 120.00 s (3600 frames) | 1920 × 1080 | `90264e1dbd4a7161f4c96a81e958fafc5eefa9d9190f0326df969216fac8fe3c` |

<!-- markdownlint-enable MD013 -->

## Known limitations

- Narration wording is fixed by the recorded takes. Clearer phrasing (for
  example “The sensor's zero offset has been checked” and “This is a historical
  replay”) needs re-synthesis with `scripts/voice.py`.

## Reproducibility

All rendering and verification commands are documented in
[implementation.md](implementation.md). Run `npm run check` and
`python scripts/verify-export.py` to re-verify. The verifier needs a full
FFmpeg build on `PATH` (null muxer and rawvideo output).
