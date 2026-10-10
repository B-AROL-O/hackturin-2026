# PoopVolt HTML presentation

Status: Architecture and planning draft. The HTML deck, theme, JavaScript,
assets, build scripts, and hosting integration have not been implemented.

This folder plans the team's three-minute PoopVolt presentation, including demo
time. Follow the [Italian narrative](../docs/pitch-narrative.md): an owner of an
older plant lacks performance visibility. The approved strong opening leads into
the company's use of an expected/observed comparison to propose interventions
the owner can understand and assess. Technical review and benefit verification
remain essential; no service conversion is guaranteed.

Show an STL concept and one software case with its actual provenance and limits.
The theoretical reference, verified string mapping, and implemented MVP scope
remain to confirm. This PR does not implement the demo software or supply an
STL.

Phone RGB simulation and separate SOLARMA history remain supporting evidence
paths, not paired proof of production loss. RGB cannot confirm hotspots or lost
kWh. The company-funded/free-device offer remains an appendix hypothesis.

The [hardware inventory](../docs/hardware.md) records secured prototype parts
and unavailable items. The UNO Q 4GB with Media Carrier is secured; the phone
RGB camera replaces the unavailable thermal camera. Integration and power
validation remain planned work.

## Read the draft

- [Presentation architecture](architecture.md): stack, module boundaries, target
  tree, and contracts.
- [Agenda](plan/agenda.md): six-slide, three-minute pitch and technical
  appendix.
- [Speaking plan](plan/speech_plan.md): timing, main claims, and transitions.
- [Visual plan](plan/plots_plan.md): intended visuals and their canonical
  sources.
- [Implementation plan](plan/implementation.md): ordered work and acceptance
  criteria.
- [Source registry](sources/README.md): evidence status and pinned source
  manifest.
- [Guideline corpus](../.agent/README.md): content, design, interaction,
  workflow, and validation.

## Reference and deliberate adaptations

The engineering organization follows the
[reference's presentation folder at revision a2e02da](https://github.com/giacolees/cognitive-radar-simulator/tree/a2e02da9a64a893cca8009c8bc040d6d8c80ef72/presentation).
It separates Quarto slide authoring, narrative planning, visual planning,
sources, local assets, and generated preview/release output.

PoopVolt uses its own narrative and proposed visual identity. The draft assumes
six main slides in three minutes, Italian audience copy, English contributor
documentation, and one canonical deck source. The three-minute budget is the
team's requested brief, not an independently verified event requirement. No
radar content, institutional theme, logos, fonts, deployment credentials, or
site configuration are copied.

## Current system baseline

The [canonical architecture](../docs/architecture/README.md) is a proposed
draft. It describes Acquisition, Diagnostics, Maintenance, `Local storage`, and
an Operator interface on an intended UNO Q edge platform, plus queued
synchronization and a proposed company service platform with company/customer
views. Hardware, models, mappings, access, integration, pricing, and free-device
economics remain open. Read the [data plan](../docs/data-plan.md) and
[company context](../docs/company/coesa-energy.md) for demo sources and buyer
fit.

The presentation should show these intended responsibilities clearly. An
illustrative scenario can demonstrate the decision logic, while measured claims
wait for reproducible prototype evidence. The presentation itself can be built
before sensor or model integration exists.
