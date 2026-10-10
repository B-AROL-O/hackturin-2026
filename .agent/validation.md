# Validation guidelines

## Checks for this architecture draft

Check Markdown formatting, relative links, the nine-slide timing total, and the
source manifest's paths, revisions, and checksums. Confirm that implemented,
measured, and generated outputs are never claimed without evidence.
No HTML deck or visual result exists yet, so browser review is pending.

## Checks required for the future implementation

<!-- markdownlint-disable MD013 -->

| Area | Acceptance criterion |
| --- | --- |
| Narrative | One claim per main slide, all nine planned anchors, 300 seconds total |
| Fidelity | Canonical module names, operator responsibility, quality handling, proposed status |
| Sources | Valid registry IDs, matching hashes, local reference files, rights for every asset |
| Rendering | No clipped text, overlaps, missing diagrams, or unreadable labels |
| Navigation | Keyboard, touch, overview, direct hash links, browser history, and notes work |
| Scenario | Complete static default, both branches, accessible selector, and load-failure fallback |
| Motion | Reduced motion and pause reveal all content; inactive slides stop custom motion |
| Accessibility | Visible focus, readable scaled text, meaningful alternatives, verified contrast |
| Offline | Local HTTP bundle works with the network disabled and has no external runtime requests |
| Print | Complete builds and both scenario states, readable sources, no clipped content |
| Packaging | Audience notes removed, assets and references present, nested host path works |

<!-- markdownlint-enable MD013 -->

Inspect at 1600 by 900 and 1280 by 720, plus a 390 CSS px mobile reading view.
Review all main and appendix slides, not just the cover. Inspect the exported PDF
if one is produced. Exercise rapid navigation and scenario toggles to detect
stale state or controls that accidentally advance the deck.

Automate manifest, timing, link, asset, and bundle checks. Add browser checks for
the scenario's coupled state and keyboard behavior. Visual review and rehearsal
remain required because lint and screenshots alone do not establish readability
or a coherent explanation. Record the tool version and reviewed build revision.

## Definition of ready to share

A clean checkout produces the same complete bundle with the pinned tools. The
portable preview passes the checks above and a five-minute rehearsal. The review
identifies any remaining limitations by scope. Publishing follows the user's
authorized task and the selected host's workflow.
