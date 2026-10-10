# PoopVolt HTML presentation

Status: Architecture and planning draft. The HTML deck, theme, JavaScript,
assets, build scripts, and hosting integration have not been implemented.

This folder defines a proposed web presentation for hackTurin. It translates the
renewed PoopVolt architecture into a short, visual explanation of the company
buyer, free customer device, local analysis, and maintenance/revamping services.

The narrative follows pigeon droppings to visible contamination on one mapped
string. A phone-camera simulation supplies that demonstration; separate SOLARMA
history supplies the whole-plant telemetry path. RGB does not confirm hotspots or
lost energy. Predictive maintenance and profitability gains remain validation
goals, with company and owner roles explained in the service review.

The [hardware inventory](../docs/hardware.md) records secured prototype parts and
unavailable items. The UNO Q 4GB with Media Carrier is secured; the phone RGB camera
replaces the unavailable thermal camera. Integration and power validation remain
planned work.

## Read the draft

- [Presentation architecture](architecture.md): stack, module boundaries,
  target tree, and contracts.
- [Agenda](plan/agenda.md): nine-slide pitch and technical appendix.
- [Speaking plan](plan/speech_plan.md): timing, main claims, and transitions.
- [Visual plan](plan/plots_plan.md): intended visuals and their canonical sources.
- [Implementation plan](plan/implementation.md): ordered work and acceptance criteria.
- [Source registry](sources/README.md): evidence status and pinned source manifest.
- [Guideline corpus](../.agent/README.md): content, design, interaction,
  workflow, and validation.

## Reference and deliberate adaptations

The engineering organization follows the
[reference's presentation folder at revision a2e02da](https://github.com/giacolees/cognitive-radar-simulator/tree/a2e02da9a64a893cca8009c8bc040d6d8c80ef72/presentation).
It separates Quarto slide authoring, narrative planning, visual planning,
sources, local assets, and generated preview/release output.

PoopVolt uses its own narrative and proposed visual identity. The draft assumes
nine main slides in five minutes, Italian audience copy, English contributor
documentation, and one canonical deck source. These are planning defaults,
not event requirements. No radar content, institutional theme, logos, fonts,
deployment credentials, or site configuration are copied.

## Current system baseline

The [canonical architecture](../docs/architecture/README.md) is a proposed draft.
It describes Acquisition, Diagnostics, Maintenance, `Local storage`, and an
Operator interface on an intended UNO Q edge platform, plus queued synchronization
and a proposed company service platform with company/customer views. Hardware,
models, mappings, access, integration, pricing, and free-device economics remain
open. Read the [data plan](../docs/data-plan.md) and
[company context](../docs/company/coesa-energy.md) for demo sources and buyer fit.

The presentation should show these intended responsibilities clearly. An
illustrative scenario can demonstrate the decision logic, while measured claims
wait for reproducible prototype evidence. The presentation itself can be built
before sensor or model integration exists.
