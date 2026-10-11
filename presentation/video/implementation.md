# Remotion implementation and reproduction

Status: Implemented local React/TypeScript production. See [review.md](review.md)
for the exported media checks and any remaining review limitations.

The concept is **From question to evidence to action**. [storyboard.md](storyboard.md)
remains the exact narration/copy contract; [timing.json](timing.json) supplies all
six scene boundaries, 1920 × 1080, 30 fps, and 3600 frames. The shot-level
[beat map](beat-map.json) records entrances and reading holds at 120 BPM.

## Toolchain

Tested with Node 22.22.2, npm 10.9.7, React/React DOM 19.2.4, TypeScript 5.9.3,
and Remotion / CLI / renderer / bundler / fonts 4.0.534. Versions are exact in
`package.json` and `package-lock.json`. Runtime assets are local; the first render
may download Remotion's matching Chrome Headless Shell. Subsequent renders use
that cached browser. FFmpeg is required only for optional audio regeneration and
media QA; Remotion includes its rendering media tools.

Official documentation checked during implementation:
[renderMedia](https://www.remotion.dev/docs/renderer/render-media),
[Sequence](https://www.remotion.dev/docs/sequence),
[loadFont](https://www.remotion.dev/docs/fonts-api/load-font), and
[still rendering](https://www.remotion.dev/docs/stills).
The installed 4.0.534 declarations and a successful render verify the selected APIs.

## Run locally

From `presentation/video/`:

```sh
npm ci
npm run prepare:assets
npm run check
npm run dev
npm run stills
node scripts/render.mjs beats
npm run render
npm run render:captioned
```

`render` produces `out/poopvolt-120-en.mp4`; `render:captioned` produces
`out/poopvolt-120-en-captioned.mp4`. Both use the same mastered local audio.
The SRT is `captions/poopvolt-120-en.srt`, with the same cue source as the burned
captions. The readable narration is [transcript.md](transcript.md).

Create the contact sheets after rendering stills, using Python with Pillow:

```sh
python scripts/contact-sheet.py stills
python scripts/contact-sheet.py beats
```

The second command writes `out/contact-sheet.png`. The final frame is copied to
`out/poster.png`. `out/`, staged `public/`, browser caches, dependencies, and local
voice-model environments are ignored by the package's own `.gitignore`.
The existing repository-root `.gitignore` was preserved.

## Source layout

- `src/Root.tsx`: composition, timing import, font loading, audio, captions.
- `src/scenes.tsx`: six scenes and editorial reframing.
- `src/components.tsx`: original logo, shared panel/roles, evidence viewports.
- `src/motion.ts`: bounded exponential and analytic critically damped functions.
- `src/art.ts`: extracted authored illustration layers; rebuild with
  `node scripts/art.mjs`. Original assets remain byte-identical.
- `scripts/prepare.mjs`: verifies supplied hashes, then stages local media.
- `scripts/captions.mjs`: caption display text (written numerals, typographic
  apostrophes, phrase-aware two-line breaks) and the SRT, keeping aligned timing.
- `scripts/check.mjs`: timeline, provenance IDs, exact script, captions and assets.
- `scripts/render.mjs`: settled layouts, beat/boundary stills, and both MP4s.
- `audio/`: six takes, mastered voice, original score, final mix and provenance.
- `fonts/`: Source Sans 3 regular/semibold with the SIL OFL.

All animation is a direct function of frame. No timers, CSS animations,
unseeded randomness, or accumulated spring state are used. The pigeon alone
receives a bounded horizontal SVG motion blur during its fast entrance.
Evidence, captions and source labels remain sharp. No temporal supersampling is
used; every export contains 3600 canonical frames.

## Editorial decisions

The latest user direction preserves the **original SOLARMA chart**, including
canonical technical-insert colors. This supersedes the earlier draft's required
brand export. The supplied PNG is a faithful rasterization of its canonical SVG;
no chart paths, values, labels, axes, dates or styling were edited. `poopvolt/report.py`
and the canonical exports remain untouched. Authored typography uses local
Source Sans 3; technical inserts and the complete logo preserve source typography.

The entire replay figure is visible from the first hard-cut frame. Its paired
results appear at 80 seconds; its chart never moves. This replaces the earlier
suggestion to progressively reveal original series. An external inspection flag
enters at 93 seconds. The eight-second 85–93 reading hold is preserved exactly.

The V04 source viewport masks only the selected crop; original symbols and nets
are unchanged. Each focus follows its narration phrase: the complete sheet at
50–53.3 and 69.5–75, Grove I2C then UART/A0/A1 at 53.3–58, the current sensor in
series and the Waveshare charger at 58–64, and A1 at 64–69.5. Zoom interpolates
size geometrically; the viewport resizes with the same easing, and photos leave
before it grows and arrive after it settles. The outdoor photograph shows the
laptop USB connection.

The supplied logo PNG has a noisy near-white ground (250–254) that showed as a
box on the white canvas. At render time an SVG filter whitens only pixels whose
three channels are all at least 250, the treatment documented for the dashboard
copy in `assets/brand/README.md`. The PNG bytes and all other pixels, including
the brand navy and yellow, are unchanged.

## Local voice and score reproduction

The delivered voice is synthesized English, Kokoro v1.0 `af_heart`, through
`kokoro-onnx` 0.4.7. The model weights are Apache-2.0; the wrapper is MIT.
No named-person imitation or external synthesis service is used. See
[audio/provenance.json](audio/provenance.json) for hashes and acquisition sources.
All audio required to render is bundled; model weights are unnecessary to render.

To regenerate speech, create a Python environment with
`scripts/voice-requirements.txt`, acquire the pinned model files listed in
provenance into `.voice-model/`, then run:

```sh
python scripts/voice.py
python scripts/retake-hook.py
node scripts/captions.mjs
sh scripts/mix.sh
npm run prepare:assets
```

The hook has a separate timed retake for the deadpan pause. Overlong takes are
re-synthesized at adjusted model speed, not stretched into a changed scene window.
Caption cues are sample-aligned to each actual synthesized phrase, including
pronunciation-only substitutions for PoopVolt, UNO Q, NFC and SOLARMA. Written
narration remains exactly the storyboard text. Captions then show dates and
quantities as numerals (for example **1 August to 17 September 2019** and
**292 kWh**); `check.mjs` compares them with the narration after the same
documented substitutions in `scripts/captions.mjs`.

The original instrumental bed uses `OfflineAudioContext` in headless Chromium,
with sine oscillators on the half-second grid, sparse scene accents, voice
sidechain ducking, and a deliberate replay rest. It has no sampled music or
random components. Speech finishes at 116.5 seconds; the mix fades to silence
before 120. Final encoding is H.264/yuv420p with AAC audio.
