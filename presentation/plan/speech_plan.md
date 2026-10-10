# Speaking storyboard

Status: Proposed speaker outline. Times match the [agenda](agenda.md).
These notes guide authoring and rehearsal; they are not implemented slide notes.

<!-- markdownlint-disable MD013 -->

| Slide | Seconds | Start | End   | Main spoken point                                                                                            | Bridge to next slide                              |
| ----- | ------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| 1     | 20      | 00:00 | 00:20 | Present PoopVolt as a proposed local support system for photovoltaic maintenance                             | Introduce the decision an operator faces          |
| 2     | 35      | 00:20 | 00:55 | A performance change can have several explanations, and interventions need different evidence                | Identify who acts on the diagnosis                |
| 3     | 30      | 00:55 | 01:25 | The system observes and advises, while the operator reviews and performs maintenance                         | Open the local processing boundary                |
| 4     | 45      | 01:25 | 02:10 | Acquisition produces usable observations, Diagnostics produces findings, Maintenance proposes action         | Explain what makes an observation usable          |
| 5     | 40      | 02:10 | 02:50 | Timestamp and quality checks prevent unreliable input from becoming a confident finding                      | Show what each modality can contribute            |
| 6     | 45      | 02:50 | 03:35 | RGB, thermal, and electrical evidence answer different questions, and degradation needs history              | Turn the evidence into an operator recommendation |
| 7     | 40      | 03:35 | 04:15 | Use two labeled illustrative cases to show a cleaning review and a request for inspection                    | Explain what needs to become real next            |
| 8     | 25      | 04:15 | 04:40 | State the current design status and the next acquisition, inference, and recommendation validation steps     | Return to the operator's goal                     |
| 9     | 20      | 04:40 | 05:00 | Close on proportionate maintenance and propose validating the evidence chain on an instrumented installation | Move to questions and technical appendix          |

<!-- markdownlint-enable MD013 -->

## Required notes when authoring

Each slide's notes should state its claim status, source IDs, essential limitation,
and transition. Keep details of sensor selection, model evaluation, and wiring in
appendix notes. On slide 6, explicitly say that a single image cannot establish
irreversible degradation. On slide 7, identify both cases as illustrative.
On slide 8, say that no end-to-end prototype or measured benefit is established
by the repository's current documentation.

Rehearse the full talk with static slides first. Interaction must fit the
40-second scenario budget and must remain optional if the presenter needs to
continue without it. Do not spend the pitch explaining deck controls or build tools.
