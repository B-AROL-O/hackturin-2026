# Presentation source registry

Status: Canonical documentation baseline, not measured experiment evidence.

[manifest.json](manifest.json) pins the existing source files to repository
revision `f6a89c971bd670386c02c6438710ab2a8ef920d2`, with the application architecture
and reference index refreshed to `6994d38531f267e81bf1081f16eeeee6e31ac457` after
reviewing their terminology-only changes. Paths are relative to the repository
root. Checksums describe the bytes inspected for this draft. There are no local
snapshot copies: the canonical documents remain under `docs/`.

## Source map

<!-- markdownlint-disable MD013 -->

| Source ID             | Canonical page                                                             | Presentation use                                       |
| --------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------ |
| `pv-pitch`            | [Project pitch](../../docs/pitch-draft.md)                                 | Problem and intended value                             |
| `pv-index`            | [Architecture index](../../docs/architecture/README.md)                    | View hierarchy, conventions, and open decisions        |
| `pv-overview`         | [System overview](../../docs/architecture/overview.md)                     | Intended processing stages and goals                   |
| `pv-context`          | [System context](../../docs/architecture/context.md)                       | Operator responsibility and system boundary            |
| `pv-architecture`     | [Application architecture](../../docs/architecture/architecture.md)        | Logical modules and `Local storage`                    |
| `pv-deployment`       | [Physical deployment](../../docs/architecture/deployment.md)               | Intended platform and unresolved interfaces            |
| `pv-acquisition`      | [Acquisition](../../docs/architecture/components/acquisition.md)           | Normalization, quality, and alignment                  |
| `pv-diagnostics`      | [Diagnostics](../../docs/architecture/components/diagnostics.md)           | Modality analysis, history, and uncertainty            |
| `pv-maintenance`      | [Maintenance](../../docs/architecture/components/maintenance.md)           | Evidence checks and operator recommendation            |
| `pv-flow-soiling`     | [Soiling flow](../../docs/architecture/flows/detect-soiling.md)            | Valid and unreliable input branches                    |
| `pv-flow-maintenance` | [Maintenance flow](../../docs/architecture/flows/recommend-maintenance.md) | Operator review, intervention, and reassessment        |
| `pv-references`       | [Reference index](../../docs/references.md)                                | Candidate datasets and links for hardware verification |

<!-- markdownlint-enable MD013 -->

Architecture entries have proposed status. The pitch describes intended behavior,
and the reference index is a retrieval aid. Neither supplies measured project
performance. Follow external links before quoting hardware or dataset details.

## Baseline maintenance

The manifest is an auditable baseline. If a canonical file changes, review which
claims and figures are affected, update the source registry entry to the revision
containing the reviewed bytes, and regenerate its checksum. Keep the previous
baseline in Git history. Do not silently bless a changed file during a build.

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
- Applied ideas: separate narrative and visual plans, canonical authoring,
  local assets, provenance records, generated previews, and portable release.
- Scope: organization and workflow only. Its research content and visual identity
  supply no PoopVolt claim or design assets.
