# Interaction and accessibility guidelines

## Presentation controls

Delegate slide navigation, overview, URL hashes, and speaker notes to Reveal.js.
Use one linear main sequence. Keep appendix slides outside the pitch count and
timing. Preserve stable slide IDs through content and layout revisions.

Support keyboard navigation, visible focus, and native links and buttons. An
interactive control must consume its own Space or Enter activation so that the
same key does not also advance the deck. Fullscreen is an explicit user action.
Touch controls must have at least a 44 by 44 CSS px hit area.

## Scenario interaction

The planned scenario follows the pigeon-droppings story and compares adequate
illustrative soiling/thermal evidence with missing or stale input. A deposit in
an RGB image alone must not establish a hotspot or automatically authorize work.
Use an explicit selector with a readable state label. Maintain the same layout
while changing the observation quality, finding, and recommendation together.
Announce the result in a polite live region. Keep the illustrative label visible.

Render the default case as complete static content. JavaScript enhances that
content from a local fixture and never calls a sensor, model, or remote service.
Failure to load a fixture must retain the static explanation and show a concise
unavailable-state message. Switching scenarios must never change slides.

## Motion

Use a short crossfade of roughly 200 to 300 ms. Permit at most two or three
presenter-controlled builds to explain a causal relationship. Keep axes, source
labels, uncertainty, and measured values visible throughout.

Respect `prefers-reduced-motion` and provide a visible pause-motion control if
custom motion is added. Persist that choice only as an optional local preference.
Run custom animations only on the active slide and stop them in overview,
background tabs, and print mode. Essential information must remain visible when
animation is disabled. Avoid loops, decorative sweeps, parallax, and count-up KPIs.

## Reading and print

Provide meaningful headings, image alternatives, and diagram descriptions.
Use real text for labels where possible. Target WCAG AA contrast: at least 4.5:1
for normal text and 3:1 for large text. Verify effective size after deck scaling.

At narrow widths, offer a readable stacked view or handout with the same claims
and sources. Do not rely solely on shrinking the desktop canvas to phone width.
Check the chosen Quarto reading mode before treating it as sufficient.

The print view must show complete builds, both scenario cases, source captions,
and explicit illustrative/proposed status. Preserve the selected scenario after
printing. Publish an audience bundle without private presenter notes and a local
presenter bundle when notes contain rehearsal or internal material.
