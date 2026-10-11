# HTML presentation guideline corpus

Status: Draft guidelines for the planned PoopVolt web presentation.

Use the repository's [brand guidelines](../brand-guidelines.md) for shared logo,
palette, typography and voice proposals. Presentation-specific guidance adds
layout and interaction rules; legacy exported cards have not yet been migrated.

This corpus gives contributors and coding agents a common brief. The
[presentation architecture](../presentation/architecture.md) defines the proposed
application. The [implementation plan](../presentation/plan/implementation.md)
defines the order of work and acceptance criteria.

## Read by task

<!-- markdownlint-disable MD013 -->

| Task                                  | Read                                                                                                                               |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Understand the presentation           | [Presentation overview](../presentation/README.md), then the architecture                                                          |
| Write or revise slides                | [Content and evidence](content.md), [agenda](../presentation/plan/agenda.md), [speaking plan](../presentation/plan/speech_plan.md) |
| Design layouts or assets              | [Visual design](visual-design.md), [visual plan](../presentation/plan/plots_plan.md)                                               |
| Add navigation, motion, or a scenario | [Interaction and accessibility](interaction.md), then the architecture contracts                                                   |
| Build, package, or review             | [Engineering workflow](workflow.md), [validation](validation.md)                                                                   |

<!-- markdownlint-enable MD013 -->

## Authority and scope

1. Follow the user's current instructions and applicable repository guidance.
2. Resolve system facts against the canonical architecture and source documents.
3. Use the presentation plans for narrative, timing, and implementation decisions.
4. Apply these guidelines to the presentation implementation and review.

Keep architectural proposals, illustrative examples, and measured results
distinct. An HTML mockup never establishes that the edge application works.
These guidelines are repository documentation, not an installed Codex skill.
The root `AGENTS.md` provides the entry point for agents that support that file.

## Reference adaptation

The [reference presentation folder](https://github.com/giacolees/cognitive-radar-simulator/tree/a2e02da9a64a893cca8009c8bc040d6d8c80ef72/presentation)
informed the separation of plans, sources, assets, authoring, preview, and release.
Its institutional branding, radar motifs, theme, animation choreography, talk
length, and deployment identifiers are outside this project's design brief.
The corpus lives in `.agent/` as requested, with links from `presentation/`.
