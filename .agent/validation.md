# Validation guidelines

## Checks for this architecture draft

Check Markdown with the CI versions and rules for Markdownlint, Prettier, and
textlint. Check relative links, six-scene timing, and source manifest paths,
states, revisions/base revisions, and checksums. The main duration is 120
seconds including demonstrations. Match agenda, speaking notes, and visual-plan
anchors.

Confirm that the theoretical reference, current under illumination, STL, and
field benefit are never claimed without evidence. Check the visible schematic,
separate USB/solar supply paths, and replay period/units. Verify that all six
voice-over blocks fit their intervals, including pauses and the closing hold. No
deck or new video implementation exists in this edit; browser review is pending,
not a passed check.

## Checks required for the future implementation

<!-- markdownlint-disable MD013 -->

| Area          | Acceptance criterion                                                                       |
| ------------- | ------------------------------------------------------------------------------------------ |
| Narrative     | One claim per main slide, six planned anchors, 120 seconds including holds and transitions |
| Fidelity      | Company use, informed owner decision, reference assumptions, mapped scope, proposed status |
| Sources       | Valid IDs, matching canonical hashes, local references, rights and artifact provenance     |
| Rendering     | No clipped text, overlaps, missing figures, or unreadable labels                           |
| Navigation    | Keyboard, touch, overview, direct links, history, and notes work                           |
| Scenario      | Usable and missing-reference states, visible provenance, independent phone/replay paths    |
| Motion        | Reduced motion and pause reveal all content; inactive slides stop custom motion            |
| Accessibility | Visible focus, readable scaled text, meaningful alternatives, verified contrast            |
| Offline       | Local HTTP bundle works without external runtime requests                                  |
| Print         | Complete builds and scenario states, readable sources, no clipped content                  |
| Packaging     | Audience notes removed, local assets/references present, nested host path works            |

<!-- markdownlint-enable MD013 -->

Inspect at 1600 by 900 and 1280 by 720, plus a 390 CSS px mobile reading view.
Review main and appendix slides and any exported PDF. Exercise rapid navigation
and scenario toggles to detect stale state.

Automate source, timing, link, asset, and bundle checks when build helpers
exist. A source check verifies provenance, not model performance. Rehearsal and
visual review remain required.

## Definition of ready to share

A clean checkout produces the complete bundle with pinned tools. The portable
preview passes checks and a two-minute rehearsal; a video export stays at or
below 120 seconds. Identify limitations and artifact status explicitly.
Publishing follows the user's authorized task and the selected host's workflow.
