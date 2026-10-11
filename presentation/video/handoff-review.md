# Production handoff review

Reviewed on 2026-10-11 against repository baseline `3956585`.
This records documentation and supplied-media checks, not a completed film.

- Six contiguous scene slots total 3600 frames at 30 fps: exactly 120 seconds.
- English narration has 236 words. Estimated scene delivery fits the planned
  windows at approximately 116–138 words per minute; recording rehearsal is pending.
- All 24 canonical source entries match local bytes and their committed revisions.
- Scene source IDs resolve; relative links in the changed documentation resolve.
- All 14 image assets match their recorded hashes; asset rebuild reproduces them.
- Logo, photos, schematic, and chart copies preserve their original source bytes.
- Original illustrations use only the selected brand palette.
- Logo, three prototype photos, illustrations, wiring, and replay chart were
  visually inspected. Final crops and composed scenes still need video review.
- Markdownlint CLI 0.45.0, Prettier 3.6.2, Ruff 0.17.0, and whitespace checks pass
  for the scoped handoff files. PNG exports use librsvg 2.61.2.

Remaining production work: Remotion scaffolding, font acquisition, reviewed
brand chart export, English voice recording, caption alignment, animation,
full-video rendering, and visual/audio review. No final MP4 or voiceover is
delivered by this handoff. That work has since been implemented; see the
[implementation](implementation.md) and the [delivery review](review.md).
