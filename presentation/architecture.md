# HTML presentation architecture

- Architecture ID: `pv-presentation`
- Status: Proposed draft, with no runtime implementation yet.
- System source: [PoopVolt architecture index](../docs/architecture/README.md).
- Build sequence: [Implementation plan](plan/implementation.md).

## Purpose and boundaries

Explain the proposed device sale to a service company, free distribution to
owners, and the path from mapped observations to maintenance and revamping review.
Show phone-based single-string localization separately from historical
multi-channel telemetry analysis. Give judges and the potential buyer a readable
pitch and engineers a technical appendix from the same canonical sources.

The presentation is a static site. It shows architectural proposals and an
optional illustrative decision scenario. It does not acquire telemetry, execute
inference, trigger maintenance, or establish the Operator interface technology.
The site runs on an audience browser independently of the intended UNO Q system.

## Existing architecture translated into presentation work

<!-- markdownlint-disable MD013 -->

| Canonical area  | Audience explanation                                                     | Presentation work                                     | Product work still unresolved                               |
| --------------- | ------------------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------------- |
| Context         | The company buys, the owner benefits, and the technician reviews work    | Buyer/owner/service relationship                      | Device ownership, pricing, and service workflow             |
| Acquisition     | Phone capture and telemetry have separate provenance and mapped scope    | Phone scene, channel coverage, missing-input scenario | Transfer, adapters, topology, units, timestamp rules        |
| Diagnostics     | Visible localization and multi-channel trends answer different questions | Independent RGB and telemetry paths                   | Labels, models, calibration, prediction horizon, evaluation |
| Maintenance     | Evidence supports maintenance or revamping review                        | Service options and economic inputs                   | Policy, production baseline, quotes, uncertainty            |
| `Local storage` | History supports reassessment after an intervention                      | History loop and evidence links                       | Retention, storage medium, record contracts                 |
| Deployment      | Edge analysis targets UNO Q; remote views require synchronization        | Edge/platform boundary and stale remote state         | Power, compatibility, transfer, access and synchronization  |

<!-- markdownlint-enable MD013 -->

Source pages remain authoritative. Presentation excerpts must carry the parent
diagram ID and proposed status. Keep wiring details and unsupported hardware
specifications out of the main deck.

The proposed company platform is part of the product architecture, not this
static presentation. Illustrative company/customer screens are fixtures only;
they provide no live monitoring, login, or economic calculation service.

Hardware availability comes from [the team inventory](../docs/hardware.md), source
ID `pv-hardware`. Show the UNO Q 4GB with Media Carrier and selected Base Shield
as secured parts with integration pending. The current demo uses phone RGB
instead of the unavailable thermal camera; thermal diagnosis is deferred.

## Stack decision

Propose Quarto with Reveal.js, following the reference's authoring workflow.
Markdown keeps slides and speaker notes reviewable. Reveal.js supplies navigation,
overview, deep links, and presentation controls. SCSS defines an original theme.
Small JavaScript enhancements handle motion preferences and the optional scenario.

Use build-time rendering for canonical Mermaid diagrams so the audience bundle
contains static, accessible figures. Pin tool versions after validating the first
render. The initial build needs no Node application framework or backend.

Technical references:
[Quarto Reveal.js](https://quarto.org/docs/presentations/revealjs/),
[presenting and exporting](https://quarto.org/docs/presentations/revealjs/presenting.html),
and [diagram authoring](https://quarto.org/docs/authoring/diagrams.html).
Offline behavior, print completeness, and responsive reading are acceptance
requirements to verify, not guarantees from choosing the stack.

## Build and runtime boundaries

```mermaid
flowchart TB
    docs["Canonical system documents"]
    registry["Source registry and checksums"]
    plans["Agenda, speaking plan, and visual plan"]
    corpus["Guideline corpus in .agent"]
    figures["Build-time diagram exports and local assets"]
    talk["talk.qmd: slides and notes"]
    render["Quarto render with local Reveal.js and theme"]
    package["Validation and audience packaging"]
    preview["Portable preview bundle"]
    release["Portable release bundle"]
    browser["Audience browser"]
    docs -->|Canonical content| talk
    docs -->|Diagram sources| figures
    registry -->|Verified provenance| package
    plans -->|Claims, anchors, timing| talk
    corpus -->|Authoring rules| talk
    figures -->|Static visuals| render
    talk -->|Slide source| render
    render -->|HTML and dependencies| package
    package -->|Review output| preview
    package -->|Release output| release
    release -->|Static files| browser
```

This diagram describes the proposed presentation build, not the PoopVolt edge
application. Preview and release use the same inputs, with separate output paths.
The audience browser loads local assets and optional illustrative fixture data.

## Target file layout

Only documentation and the source manifest exist in this draft. All runtime and
build files below are planned. Generated directories must be ignored when added.

```text
.agent/
  README.md                  guideline entry point
  content.md                 narrative and evidence rules
  visual-design.md           original design direction
  interaction.md             navigation, scenario, motion, accessibility
  workflow.md                build and contributor workflow
  validation.md              review and acceptance criteria
presentation/
  README.md
  architecture.md
  plan/
    agenda.md
    speech_plan.md
    plots_plan.md
    implementation.md
  sources/
    README.md
    manifest.json            canonical source revision and checksum registry
  talk.qmd                   PLANNED: single canonical slide source
  _quarto.yml                PLANNED: rendering and presenter/audience profiles
  theme.scss                 PLANNED: tokens, layouts, print, reading mode
  fonts.css                  PLANNED: local font declarations
  assets/                    PLANNED: images, fonts, licenses, provenance
  figures/                   PLANNED: generated canonical diagram exports
  data/scenarios.json        PLANNED: explicitly illustrative scenario fixture
  js/presentation.js         PLANNED: motion preference and lifecycle handling
  js/scenario.js             PLANNED: optional local scenario enhancement
  scripts/render_diagrams.py PLANNED: extract canonical Mermaid and render it
  scripts/check_presentation.py PLANNED: source, timing, links, bundle checks
  scripts/build_share.py     PLANNED: portable bundle and local references
  preview/                   PLANNED: ignored review output
  deployment/                PLANNED: ignored release output
```

## Responsibility contracts

<!-- markdownlint-disable MD013 -->

| Module               | Inputs                                            | Outputs and limits                                    |
| -------------------- | ------------------------------------------------- | ----------------------------------------------------- |
| Narrative source     | Plan, canonical docs, source IDs                  | Slides, notes, stable anchors, timing metadata        |
| Diagram generation   | Canonical page, Mermaid block, diagram ID         | Static figure, description, parent ID, source hash    |
| Theme                | Design tokens and layout classes                  | Screen, print, and narrow-width styles                |
| Motion enhancement   | Active slide, preference, visibility, print state | Optional motion with a complete static fallback       |
| Scenario enhancement | Local fixture and explicit selection              | Coupled observation/finding/recommendation view       |
| Source checker       | Manifest, slide source, plans, assets             | Errors for mismatched claims, inputs, or dependencies |
| Packaging            | Validated render, local assets, source documents  | Audience bundle with working relative references      |

<!-- markdownlint-enable MD013 -->

Keep all required static slide content in `talk.qmd`. JavaScript must not be the
only place where the main claim, uncertainty, or source attribution exists.
An interactive scenario enriches a complete static default, rather than gating it.

## Proposed presentation metadata

Each future main slide has a stable ID from the agenda, an integer duration in
seconds, source IDs, and claim status. Store these as Quarto heading attributes
and validate the rendered metadata as well as the authored source.
The nine-slide total is 300 seconds. Appendix IDs start with `pv-a-` and are
excluded from the main timing and counter.

The source manifest records repository-relative paths, source state, revision
when committed, SHA-256, scope, and upstream URL when available. A reviewed
uncommitted source has a null revision/URL and a recorded base revision; its
checksum pins working-tree bytes without claiming that they exist at the base.
It is a registry of canonical files, not a second copy of the system architecture.
At build time, fail on a checksum mismatch
until the source change has been reviewed and the baseline deliberately refreshed.

Canonical file entries live in `sources`; external background and dataset records
live in `external_sources`, with stable IDs and available revision or publication
identifiers. The future source checker must resolve IDs from both collections,
while requiring file checksums only for the canonical file entries.

## Illustrative scenario contract

The proposed fixture schema is presentation-only. It is not an edge API contract.

<!-- markdownlint-disable MD013 -->

| Field            | Meaning                                                                    |
| ---------------- | -------------------------------------------------------------------------- |
| `id`             | Stable scenario ID                                                         |
| `status`         | Always `illustrative` for the initial fixture                              |
| `sourceIds`      | Canonical design sources that justify the depicted behavior                |
| `observations`   | Modality, provenance, plant/asset mapping, readable summary, time, quality |
| `finding`        | Kind, image region, localization scope, evidence references, uncertainty   |
| `recommendation` | Suggested action, reason, and `operatorReviewRequired: true`               |
| `limitations`    | Missing inputs and unverified assumptions                                  |

<!-- markdownlint-enable MD013 -->

Both cases follow the phone-camera simulation on one declared panel/string.
Case one has usable illustrative RGB evidence, a deposit region, and known demo
mapping; it proposes cleaning review. Case two has stale/missing imagery or unknown
mapping and requests a new observation or asset inspection. Neither establishes
a hotspot, electrical interruption, production loss, or irreversible degradation.

Telemetry replay is a separate historical scene with its own provenance,
channel coverage, and unknown string mapping. Never fuse it with the phone scene.
An illustrative service view can compare maintenance and revamping inputs but
must show an unavailable economic estimate where production/cost inputs are absent.
No invented probabilities, electrical thresholds, ROI, or forecast performance.

External background sources in the registry support the narrative's mechanisms;
they are separate from the checksum-pinned system documents and supply no
measured PoopVolt results.

## Delivery model and open decisions

Package local scripts, fonts, figures, fixture data, and readable source references
with the generated `index.html`. Serve the portable folder over HTTP. Strip private
notes in the audience profile and verify their absence from the bundle. A presenter
profile retains notes for local rehearsal. Print includes complete static content.

The draft leaves the host, public path, official pitch duration, final slide
language, actual image assets, exact tool versions, and font acquisition open.
The defaults above allow drafting without making those choices into product facts.
Review them before implementation or publication. A host connection is unnecessary
to build and evaluate the local presentation.
