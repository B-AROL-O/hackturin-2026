# Visual design guidelines

For the user-selected Remotion film, use
[video design](../presentation/video/design.md) and
[the local asset inventory](../presentation/video/assets/README.md).
Its 1920 × 1080 layout follows `brand-guidelines.md`, the complete original logo
on white, natural prototype photographs, and faithful technical source inserts.

## Direction

Build a calm, editorial presentation about photovoltaic field maintenance. Use
generous whitespace, clear technical drawings, and close views of a panel when a
photograph supplies useful context. Let the sensing and decision flow provide
the recurring visual structure. The title slide can use a dark blue canvas with
one panel image and a large PoopVolt wordmark.

Use the older plant and its owner's question as the recurring visual context.
The pigeon cue explains the name and remains secondary. The central visual is
expected versus observed production over matching periods, with estimates,
observations, and simulations distinguished by labels and line patterns. Unknown
reference inputs must remain visibly unavailable.

Show the prototype electrical schematic as a dedicated scene and the replay
chart with provenance. The undelivered STL is outside the main sequence. Keep
SOLARMA channels distinct from verified strings and phone imagery separate from
replay. A company-to-owner offer belongs in supporting context or the appendix.
Thermal illustrations are risk context only, never current measured output.

## Brand palette

Use the palette in [brand-guidelines.md](../brand-guidelines.md): dark blue,
solar yellow, white and neutral greys. It replaces the earlier teal, rust, amber
and ivory proposal for new materials. Existing video cards and charts remain
legacy exports and require a separate coordinated migration.

Use blue text on yellow. Check final contrast and communicate status through
labels, symbols and line patterns as well as color. Do not introduce extra brand
accents or reinterpret measured evidence through decorative color.

## Type and geometry

Use a single locally bundled sans-serif family, proposed as Source Sans 3, with
a system sans-serif fallback and its license. Verify and acquire font files in
the implementation phase. Use regular and semibold weights. Reserve monospace
for code identifiers in technical appendix material.

Design on a 1600 by 900 canvas. Start with a 72 px safe margin, 64 px headings,
32 px body copy, and 22 px source captions in canvas coordinates. At a 1280 by
720 display, normal body copy should remain about 25 px. Revise layouts before
shrinking text. Use a consistent baseline grid and at most two content columns.

## Composition vocabulary

- Cover: large title, one-line purpose, panel visual, team attribution.
- Problem: one field image with a localized, labeled observation.
- Architecture: one generous horizontal flow with a clearly marked edge
  boundary.
- Diagnostics: aligned evidence views with readable labels and a common legend.
- Decision: observation, finding, and operator recommendation in a stable
  sequence.
- Roadmap: current design state and the next validation steps, with honest
  status.

Use flat compositions for explanations. Reserve UI panels for the illustrative
operator interface, where they demonstrate an actual interaction. Avoid turning
every slide into a dashboard. Keep a small slide counter and source caption;
introduce no permanent sponsor footer without a verified need and usable assets.

## Diagrams and images

Derive engineering diagrams from canonical Mermaid sources. Keep names and
boundaries intact. Generate a full canonical view for the appendix and a labeled
presentation excerpt where the main talk needs less detail. Record the parent
diagram ID and extraction rule. Adapt colors during generation, without changing
the original system semantics or hand-editing generated files.

For photographs, preserve provenance and avoid crops that remove the evidence.
Show RGB and thermal observations as separate modalities. Label synthetic
thermal overlays as illustrations. Do not imply a photograph came from PoopVolt
hardware. Use diagram rendering or native chart tools for technical figures, and
image search or image generation for photographic or decorative assets when
needed.
