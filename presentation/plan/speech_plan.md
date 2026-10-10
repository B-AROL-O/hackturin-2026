# Speaking storyboard

Status: Proposed speaker outline. Times match the [agenda](agenda.md).
These notes guide authoring and rehearsal; they are not implemented slide notes.

<!-- markdownlint-disable MD013 -->

| Slide | Seconds | Start | End   | Main spoken point                                                                                            | Bridge to next slide                              |
| ----- | ------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| 1     | 20      | 00:00 | 00:20 | Introduce the pigeon story and PoopVolt as proposed local maintenance support                                | Introduce the decision an operator faces          |
| 2     | 35      | 00:20 | 00:55 | Follow the deposit to a suspected hotspot; widen the problem to dust and hail                                | Identify who acts on the diagnosis                |
| 3     | 30      | 00:55 | 01:25 | The system observes and advises, while the operator reviews and performs maintenance                         | Open the local processing boundary                |
| 4     | 45      | 01:25 | 02:10 | Acquisition produces usable observations, Diagnostics produces findings, Maintenance proposes action         | Explain what makes an observation usable          |
| 5     | 40      | 02:10 | 02:50 | Timestamp and quality checks prevent unreliable input from becoming a confident finding                      | Show what each modality can contribute            |
| 6     | 45      | 02:50 | 03:35 | Compare deposit imagery and an illustrative thermal hotspot; history supports reassessment                   | Turn the evidence into an operator recommendation |
| 7     | 40      | 03:35 | 04:15 | Return to the same panel: adequate evidence prompts cleaning review; missing input prompts inspection        | Explain what needs to become real next            |
| 8     | 25      | 04:15 | 04:40 | State the current design status and the next acquisition, inference, and recommendation validation steps     | Return to the operator's goal                     |
| 9     | 20      | 04:40 | 05:00 | Close on proportionate maintenance and propose validating the evidence chain on an instrumented installation | Move to questions and technical appendix          |

<!-- markdownlint-enable MD013 -->

## Required notes when authoring

Introduce the pigeon as a memorable story device on slide 1 and its deposit on
slide 2. Explain that dust is another soiling example, while hail can cause
physical damage requiring inspection. On slide 6, connect localized soiling and
partial shading to a possible hotspot using separate RGB and illustrative thermal
observations; a visible deposit does not establish thermal detection. On slide 7,
return to the same panel for cleaning review or a request for better observations.
Do not present the story as measured project evidence or claim that dust and hail
account for most interruptions without field data.

Each slide's notes should state its claim status, source IDs, essential limitation,
and transition. Keep details of sensor selection, model evaluation, and wiring in
appendix notes. On slide 6, explicitly say that a single image cannot establish
irreversible degradation. On slide 7, identify both cases as illustrative.
On slide 8, say that no end-to-end prototype or measured benefit is established
by the repository's current documentation.

Rehearse the full talk with static slides first. Interaction must fit the
40-second scenario budget and must remain optional if the presenter needs to
continue without it. Do not spend the pitch explaining deck controls or build tools.
