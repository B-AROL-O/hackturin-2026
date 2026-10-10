# Visual design guidelines

## Direction

Build a calm, editorial presentation about photovoltaic field maintenance.
Use generous whitespace, clear technical drawings, and close views of a panel
when a photograph supplies useful context. Let the sensing and decision flow
provide the recurring visual structure. The title slide can use a dark graphite
canvas with one panel image and a large PoopVolt wordmark.

Use the pigeon and its deposit as a restrained recurring cue on the same panel.
Carry that location into separately labeled RGB and illustrative thermal views.
Use dust and hail examples to show the wider maintenance scope. Keep the pigeon
cue subordinate to the evidence and operator decision.

These are proposed tokens to evaluate on a projector, not an inherited brand.

| Role      | Draft value | Use                                          |
| --------- | ----------- | -------------------------------------------- |
| Canvas    | `#F7F4EC`   | Warm background for content slides           |
| Ink       | `#172A2A`   | Headings, body copy, diagram labels          |
| Teal      | `#176B63`   | Processing stages and selected state         |
| Amber     | `#E9AD35`   | Solar context and highlighted evidence       |
| Rust      | `#A5432C`   | Anomaly emphasis with an explicit text label |
| Muted ink | `#4D605D`   | Secondary copy and source captions           |
| Rule      | `#CED5CE`   | Dividers and diagram connections             |

Use ink on amber. Check every final foreground/background pairing. Color is
supporting information: labels, shapes, and line patterns must communicate
stage, status, or anomaly without it.

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
- Architecture: one generous horizontal flow with a clearly marked edge boundary.
- Diagnostics: aligned evidence views with readable labels and a common legend.
- Decision: observation, finding, and operator recommendation in a stable sequence.
- Roadmap: current design state and the next validation steps, with honest status.

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
Show RGB and thermal observations as separate modalities. Label synthetic thermal
overlays as illustrations. Do not imply a photograph came from PoopVolt hardware.
Use diagram rendering or native chart tools for technical figures, and image
search or image generation for photographic or decorative assets when needed.
