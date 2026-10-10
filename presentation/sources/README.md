# Presentation source registry

Status: Canonical documentation baseline, not measured experiment evidence.

[manifest.json](manifest.json) uses schema version 2. Each canonical document is
pinned to the immutable revision recorded in its entry. Entries can refer to
different commits when only some sources change. Each committed source records
its revision, source URL, and SHA-256 checksum of the reviewed bytes.

For later uncommitted edits, record `source_state: working_tree`, null
`revision` and `upstream_url`, the checkout's `base_revision`, and the edited
file's checksum. The base does not contain those new bytes. Replace provisional
records with the immutable revision containing the reviewed bytes once
available.

Paths are relative to the repository root. Canonical documents stay under
`docs/`; no snapshot copies are made. The future source checker must support
explicit working-tree state, verify hashes, and reject fabricated revision
links.

## Source map

<!-- markdownlint-disable MD013 -->

| Source ID              | Canonical page                                                             | Presentation use                                                         |
| ---------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `pv-narrative`         | [Three-minute narrative](../../docs/pitch-narrative.md)                    | Owner story, proposed theoretical comparison, MVP and STL scope          |
| `pv-pitch`             | [Project pitch](../../docs/pitch-draft.md)                                 | Problem and intended value                                               |
| `pv-index`             | [Architecture index](../../docs/architecture/README.md)                    | View hierarchy, conventions, and open decisions                          |
| `pv-overview`          | [System overview](../../docs/architecture/overview.md)                     | Intended processing stages and goals                                     |
| `pv-context`           | [System context](../../docs/architecture/context.md)                       | Operator responsibility and system boundary                              |
| `pv-architecture`      | [Application architecture](../../docs/architecture/architecture.md)        | Logical modules and `Local storage`                                      |
| `pv-deployment`        | [Physical deployment](../../docs/architecture/deployment.md)               | Intended platform and unresolved interfaces                              |
| `pv-acquisition`       | [Acquisition](../../docs/architecture/components/acquisition.md)           | Normalization, quality, and alignment                                    |
| `pv-diagnostics`       | [Diagnostics](../../docs/architecture/components/diagnostics.md)           | Modality analysis, history, and uncertainty                              |
| `pv-maintenance`       | [Maintenance](../../docs/architecture/components/maintenance.md)           | Evidence checks and operator recommendation                              |
| `pv-flow-soiling`      | [Soiling flow](../../docs/architecture/flows/detect-soiling.md)            | Valid and unreliable input branches                                      |
| `pv-flow-maintenance`  | [Maintenance flow](../../docs/architecture/flows/recommend-maintenance.md) | Operator review, intervention, and reassessment                          |
| `pv-data-plan`         | [Data plan](../../docs/data-plan.md)                                       | Independent phone/replay paths and source limits                         |
| `pv-flow-plant`        | [Whole-plant flow](../../docs/architecture/flows/monitor-plant.md)         | Multi-channel analysis, coverage, synchronization                        |
| `coesa-energy-context` | [Company context](../../docs/company/coesa-energy.md)                      | Existing services and proposed buyer/distribution fit                    |
| `pv-hardware`          | [Hardware inventory](../../docs/hardware.md)                               | Secured/unavailable parts, phone-camera substitution, integration limits |
| `pv-references`        | [Reference index](../../docs/references.md)                                | Candidate datasets and links for hardware verification                   |

<!-- markdownlint-enable MD013 -->

Architecture entries have proposed status. The pitch describes intended
behavior, and the reference index is a retrieval aid. Neither supplies measured
project performance. Follow external links before quoting hardware or dataset
details.

## Narrative source

`pv-narrative` adapts the team-supplied `pitch-narrative2.md` into a clean
three-minute copione. It is an authored scenario, not a customer interview or
proof of a working MVP. The source entry records the input filename/checksum.
Typos, Markdown, timing, and unsupported causal wording were clarified.

The theoretical production reference is proposed; its inputs and validation are
unresolved. MVP code, executed output, and the STL artifact must be linked
separately. Do not treat planned demonstrations as implemented evidence.

## Demonstration sources

- `pv-hardware`: [Team hardware inventory](../../docs/hardware.md), reported on
  2026-10-10. Availability is team-reported; compatibility and operation are
  unverified. Phone RGB replaces the unavailable thermal camera in the
  prototype.
- `solarma-pv-analysis-tools`:
  [Pinned SOLARMA repository](https://github.com/SOLARMA/pv-analysis-tools/tree/fc96313e453978fc89211322a8afb966b85f7913).
  Inspected on 2026-10-10 via API/raw files; candidate historical telemetry
  replay from one plant. The external record pins the inspected revision and
  larger-export file hashes. It supplies no evaluated project model.
- Phone RGB simulation: proposed data collection, not an existing external
  dataset. Record capture-session provenance, simulated deposit method, labels,
  image-to-asset mapping, and evaluation split when collected.
- The phone scene and historical telemetry must remain independent. The
  [data plan](../../docs/data-plan.md) is authoritative for their limits.

## Narrative background

The pigeon-droppings story is an illustrative device selected for this talk.
These external research abstracts support background mechanisms, not measured
PoopVolt behavior, cause frequency, asset rights, or an adopted detection model.
Their `external_sources` records in the manifest are retrieval records; they are
not checksum-pinned local snapshots. Inspected on 2026-10-10:

- `pv-soiling-background`:
  [Dust accumulation and bird-droppings detection](https://arxiv.org/abs/2501.08304v1),
  preprint revision v1. Dust and droppings can obstruct incident light.
- `pv-hotspot-background`:
  [Mitigation of hot-spots in photovoltaic systems](https://research-hub.nlr.gov/en/publications/mitigation-of-hot-spots-in-photovoltaic-systems-using-distributed-2/),
  publication DOI `10.3390/en11040726`. Partial shading and mismatch can cause
  localized heating; the story's hotspot remains an illustrative candidate.
- `pv-hail-background`:
  [Photovoltaic module imaging for hail damage assessment](https://research-hub.nlr.gov/en/publications/photovoltaic-module-imaging-for-hail-damage-assessment-with-multi-3/),
  publication `NREL/PO-5K00-80227`. Hail damage can include cell cracking and
  belongs to the damage-inspection path, separate from a cleaning review.

## Baseline maintenance

The manifest is an auditable baseline. If a canonical file changes, review which
claims and figures are affected, record the reviewed source state and regenerate
its checksum. Use the revision containing the bytes when available; otherwise
mark it working-tree with a null revision/URL and a base revision, as above.
Keep the previous baseline in Git history. Do not silently bless a changed file
during a build.

For future measured reports, add immutable snapshots with their original path,
revision, checksum, evaluation scope, and status. Keep synthetic fixture records
in `presentation/data/` and label them illustrative. Do not promote a fixture
validation into model-performance evidence.

## Structural reference

- Repository: `giacolees/cognitive-radar-simulator`
- Branch inspected: `presentation-html`
- Revision: `a2e02da9a64a893cca8009c8bc040d6d8c80ef72`
- Inspected on: 2026-10-10
- [Presentation folder](https://github.com/giacolees/cognitive-radar-simulator/tree/a2e02da9a64a893cca8009c8bc040d6d8c80ef72/presentation)
- Applied ideas: separate narrative and visual plans, canonical authoring, local
  assets, provenance records, generated previews, and portable release.
- Scope: organization and workflow only. Its research content and visual
  identity supply no PoopVolt claim or design assets.
