# Delivery QA and verification review

Reviewed on 2026-10-11 against baseline `3956585`.
Records the automated verification and export checks for the implemented
120-second English Remotion motion graphics pitch.

## Verification results

### 1. Timeline, frame count, and dimensions
- **Duration**: Exactly 120.00 seconds (3600 frames at 30 fps).
- **Resolution**: 1920 × 1080 (16:9 editorial canvas).
- **Scene structure**: Six continuous scenes matching [timing.json](timing.json).
- **Reading holds**:
  - Replay chart reading hold (85–93 s, 240 frames): mean pixel diff < 0.002 (still frame hold verified).
  - Closing composition hold (117–120 s, 90 frames): mean pixel diff < 0.0001 (completely still hold verified).
- **Seek determinism**: Arbitrary seeks reproduce byte-identical render outputs.

### 2. Audio and loudness
- **Voice synthesis**: English narration synthesized via Kokoro v1.0 `af_heart` (236 words, 6 scenes).
- **Score**: Programmatic 120 BPM minimalist score with phrase ducking and 85–93 s rest.
- **Mastered loudness**: -16.44 LUFS (EBU R128 / web delivery standard).
- **True Peak**: -4.46 dBFS (no clipping or distortion).

### 3. Typography and brand assets
- **Font**: Bundled Source Sans 3 Regular and Semibold under SIL Open Font License 1.1.
- **Brand palette**: #0D2D44 (navy), #F5C329 (solar yellow), approved neutral greys.
- **Canonical assets**: Original logo, electrical schematic, three prototype photos, and SOLARMA historical replay chart preserved byte-identical.
- **Captions**: SRT exported to `captions/poopvolt-120-en.srt` and burned into `out/poopvolt-120-en-captioned.mp4`. Maximum caption rate: 18.57 characters/second.

### 4. Export hashes

| Export | Duration | Size | SHA-256 |
|---|---|---|---|
| `poopvolt-120-en.mp4` | 120.00 s (3600 frames) | 1920 × 1080 | `294837a85408c27e5b3ef8a62e664dba2028d55f94bb074c0d08ca53443912e4` |
| `poopvolt-120-en-captioned.mp4` | 120.00 s (3600 frames) | 1920 × 1080 | `4036822e6d470806bde1da2d7c0bc181ab3521dfc53f3832133fae5edfd7a9cb` |

## Reproducibility

All rendering and verification commands are documented in [implementation.md](implementation.md).
Run `npm run check` and `python scripts/verify-export.py` to re-verify.
