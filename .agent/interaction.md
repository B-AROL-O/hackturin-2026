# Interaction and accessibility guidelines

Video implementation status: the local Remotion project and English audio now
exist. The earlier draft-only statements below describe their original handoff;
use [video implementation](../presentation/video/implementation.md) and
[video review](../presentation/video/review.md) for current commands and checks.

For the prerecorded Remotion adaptation, follow
[video motion and caption rules](../presentation/video/design.md).
The keyboard controls, presenter builds, and browser preference handling below
govern the HTML deck. The film uses deterministic frame-driven choreography,
visible qualifications, and captions within its fixed 120-second duration.

## Presentation controls

Delegate slide navigation, overview, URL hashes, and speaker notes to Reveal.js.
Use one linear main sequence. Keep appendix slides outside the pitch count and
timing. Preserve stable slide IDs through content and layout revisions.

Support keyboard navigation, visible focus, and native links and buttons. An
interactive control must consume its own Space or Enter activation so that the
same key does not also advance the deck. Fullscreen is an explicit user action.
Touch controls must have at least a 44 by 44 CSS px hit area.

## Scenario interaction

The planned slide-5 scenario compares expected and observed production. One case
has explicit illustrative reference inputs, period, and mapped scope; the other
has missing inputs or unknown mapping and shows an unavailable estimate or
limited comparison. Never substitute invented expected values for missing data.
A deviation does not establish a cause, historical decline, or recoverable
energy.

Phone RGB inspection and historical telemetry remain separate supporting scenes.
RGB cannot establish a hotspot or lost kWh. Company/customer screens are
illustrative; show coverage, source type, freshness, and unavailable economic
inputs. Use an explicit selector with a readable state label. Maintain the same
layout while changing the observation quality, finding, and recommendation
together. Announce the result in a polite live region. Keep the illustrative
label visible.

Render the default case as complete static content. JavaScript enhances that
content from a local fixture and never calls a sensor, model, or remote service.
Failure to load a fixture must retain the static explanation and show a concise
unavailable-state message. Switching scenarios must never change slides.

## Motion

The two-minute video uses the timed cues in the
[Italian storyboard](../docs/pitch-narrative.md): brief entrances, explanatory
highlights, focused schematic zooms, and holds for reading. Keep wiring and
chart labels legible. Video scene timing includes transitions and the final
hold. Provide synchronized subtitles. The following controls apply to an HTML
adaptation; no video player or deck implementation exists yet.

Use a short crossfade of roughly 200 to 300 ms. Permit at most two or three
presenter-controlled builds to explain a causal relationship. Keep axes, source
labels, uncertainty, and measured values visible throughout.

Respect `prefers-reduced-motion` and provide a visible pause-motion control if
custom motion is added. Persist that choice only as an optional local
preference. Run custom animations only on the active slide and stop them in
overview, background tabs, and print mode. Essential information must remain
visible when animation is disabled. Avoid loops, decorative sweeps, parallax,
and count-up KPIs.

## Reading and print

Provide meaningful headings, image alternatives, and diagram descriptions. Use
real text for labels where possible. Target WCAG AA contrast: at least 4.5:1 for
normal text and 3:1 for large text. Verify effective size after deck scaling.

At narrow widths, offer a readable stacked view or handout with the same claims
and sources. Do not rely solely on shrinking the desktop canvas to phone width.
Check the chosen Quarto reading mode before treating it as sufficient.

The print view must show complete builds, both scenario cases, source captions,
and explicit illustrative/proposed status. Preserve the selected scenario after
printing. Publish an audience bundle without private presenter notes and a local
presenter bundle when notes contain rehearsal or internal material.
