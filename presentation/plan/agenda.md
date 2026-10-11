# Proposed pitch agenda

Status: Documentation plan for a two-minute motion graphics pitch. Audience
language: Italian. Narration, diagram holds, transitions, and closing fit inside
120 seconds. Source: [Italian company-use story](../../docs/pitch-narrative.md).
No video or HTML deck is implemented by this plan.

The user-selected [English Remotion adaptation](../video/storyboard.md) preserves
these six anchors and durations. Its [frame schedule](../video/timing.json)
totals 3600 frames at 30 fps. Use the same technical scope, with translated
English copy, supplied media, original logo, and the selected brand rules.

## Main sequence

Keep the approved opening and company/owner framing. Show the available peer
comparison, distinguish the future theoretical reference, give the prototype
wiring its own scene, then present one historical replay and technician review.
The schematic replaces the undelivered STL in the main sequence.

<!-- markdownlint-disable MD013 -->

| Scene | Stable ID      | Title                                 | Seconds | Purpose                                                           | Source IDs                                             |
| ----- | -------------- | ------------------------------------- | ------- | ----------------------------------------------------------------- | ------------------------------------------------------ |
| 1     | `pv-title`     | Il tuo impianto è sporco di merda     | 12      | Hook and production question; illustrative contamination          | `pv-narrative`                                         |
| 2     | `pv-problem`   | Funziona. Ma rende quanto dovrebbe?   | 18      | Company's need for evidence the owner understands                 | `pv-narrative`, `pv-pitch`                             |
| 3     | `pv-pipeline`  | Lo scostamento indica dove verificare | 20      | Available peer comparison versus future theoretical reference     | `pv-narrative`, `pv-comparison`, `pv-data-plan`        |
| 4     | `pv-prototype` | Lo schema elettrico del prototipo     | 25      | Show canonical wiring, USB supply, and separate solar branch      | `pv-narrative`, `pv-wiring`, `pv-wiring-svg`           |
| 5     | `pv-evidence`  | Un inverter da verificare             | 25      | SOLARMA replay, inverter 1, matched period, units, and limits     | `pv-narrative`, `pv-comparison`, `pv-comparison-chart` |
| 6     | `pv-decision`  | Proporre, scegliere, verificare       | 20      | Technician proposal, owner choice, and later benefit verification | `pv-narrative`, `pv-maintenance`                       |

<!-- markdownlint-enable MD013 -->

Total: 120 seconds. Preserve these six anchors if adapting the storyboard to
`talk.qmd`. The future checker compares IDs, order, and durations with the
speaking plan and authored source. `pv-prototype` now identifies electrical
wiring, rather than an STL viewport.

## Appendix

<!-- markdownlint-disable MD013 -->

| Stable ID         | Subject                                               | Canonical sources                                         |
| ----------------- | ----------------------------------------------------- | --------------------------------------------------------- |
| `pv-a-deployment` | Full schematic, secured parts, unresolved integration | `pv-wiring`, `pv-deployment`, `pv-hardware`               |
| `pv-a-components` | Local modules and theoretical-reference inputs        | `pv-acquisition`, `pv-diagnostics`, `pv-maintenance`      |
| `pv-a-flows`      | Independent phone/replay paths and reassessment       | `pv-flow-soiling`, `pv-flow-plant`, `pv-flow-maintenance` |
| `pv-a-sources`    | Replay limits and commercial/model assumptions        | `pv-comparison`, `pv-data-plan`, `coesa-energy-context`   |

<!-- markdownlint-enable MD013 -->

Appendix material is outside the video and two-minute pitch. Coesa is a possible
counterpart, not an established partner. Free-device distribution and an STL
concept, if supplied, belong in supporting discussion. Update timings, visual
cues, and validation together if the budget changes.
