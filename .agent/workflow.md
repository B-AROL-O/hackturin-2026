# Engineering workflow guidelines

The user-selected Remotion film has an independent
[implementation contract](../presentation/video/implementation.md).
Keep its code, local images/fonts/audio, dependencies, and exports inside
`presentation/video/`. Preserve shared source provenance and the brand rules.
The Quarto workflow below applies to the HTML deck.

## Boundaries

Keep slide sources, presentation assets, and build helpers inside `presentation/`.
Keep guidelines in `.agent/`. Read the system architecture before changing
technical content. The presentation is a static communication artifact and has
no runtime dependency on the planned PoopVolt edge application.

Use Quarto with Reveal.js as the proposed authoring stack. Pin the exact Quarto
version after a successful baseline render. Use the bundled Reveal.js runtime.
Start with Markdown, SCSS, and a small JavaScript enhancement. Add dependencies
only when an accepted requirement needs them. A backend, framework application,
authentication layer, or model-serving integration is outside the initial build.

## Change sequence

1. Read the relevant corpus pages and the presentation architecture.
2. Locate the canonical source and record the claim's status.
3. Update agenda, notes, visual plan, and slide source together when affected.
4. Generate figures from their sources and record asset provenance.
5. Render and check the complete deck and the packaged preview.
6. Inspect the changed slides and adjacent transitions in a browser.

Keep a single canonical `talk.qmd` once implementation starts. A separate blank
starter is unnecessary for the initial pitch. Use stable IDs to coordinate work.
Do not hand-edit generated HTML, diagram exports, or release directories.

## Build and packaging

The future build must run from the repository root, verify source records, render
diagrams and slides, validate local dependencies, and package an audience bundle.
Use deterministic source inputs. Verify explicit working-tree hashes without
pretending the edited bytes exist at their base revision; resolve provisional
source records to an immutable revision when available.
Exclude speaker notes from the audience bundle
through a tested build profile, rather than hiding them visually.

Put generated previews and release bundles in separate ignored directories.
Copy the canonical documents referenced by slides to a `references/` folder
inside each bundle and rewrite links during packaging. Check those links after
copying. Relative links inside copied Markdown also need resolution, either by
including the full documentation tree or by producing a linked HTML handout.

Bundle fonts, runtime code, styles, figures, and fixture data locally. The talk
must work over a local HTTP server without network access. Do not promise
`file://` support while the scenario uses `fetch`. Viewing external source URLs
can require connectivity, but navigating the talk must not.

## Hosting

Select GitHub Pages, Netlify, or another static host only after the portable
bundle works. Keep hosting configuration explicit about base paths and output
directories. Account IDs and URLs from the reference are unrelated to this repository.
Avoid changing the existing Docsify documentation deployment while adding the
presentation. Record the chosen path and link the two surfaces deliberately.

This draft adds no hosting integration. Future scripts and commands in the
implementation plan become executable instructions only when those files exist.
