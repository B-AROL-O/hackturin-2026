# PoopVolt (hackTurin 2026)

<img src="assets/brand/Logo_PoopVolt.png" alt="PoopVolt logo: pigeon on a photovoltaic panel beside the product name" width="640" />

Brand resources: [brand guidelines](brand-guidelines.md) and
[logo provenance and available variants](assets/brand/README.md).

PoopVolt starts with the owner of an older photovoltaic plant who does not know
whether it produces as expected. A proposed expected/observed comparison makes
performance gaps visible. A photovoltaic service company uses the proposed
evidence to explain interventions the owner can understand and assess. The
three-minute story includes the approved strong opening, an MVP software case,
an STL concept, and technician-reviewed regeneration. The theoretical model,
implemented demo scope, and field benefits remain to verify. The
company-funded/free-device offer remains a secondary commercial hypothesis.

## The Challenge

> This project was initially developed during the [hackTurin 2026](https://luma.com/t2odor1k) hackathon which took place in Turin over the 2026-10-11 weekend.
> See the [full writeup on Devpost](https://devpost.com/software/poopvolt).
> Quick links, event details, partners and sponsors are in
> [hackTurin 2026 resources](docs/hackturin-2026.md).

Our team tackled the **Beyond Solar** challenge with **PoopVolt**, an Edge AI
predictive maintenance system for off-grid photovoltaic installations. See the
[project pitch](docs/pitch-draft.md) for the idea description.

## The problem and who it is for

The owner of an older photovoltaic plant usually cannot tell whether it still
produces as much as it should. Dust, bird droppings and ageing lower the output
slowly, and a plant that "apparently works" is rarely inspected. A service
company that maintains the plant has the same problem in reverse: it needs
evidence the owner can understand before proposing a cleaning, a repair or a
replacement.

## Our solution: PoopVolt

PoopVolt is a proposed Edge AI maintenance aid built around an Arduino UNO Q.
It combines three things, each kept separate and labelled by where its data
comes from (measured, replayed or simulated):

- **Expected versus observed production:** compare what a plant produced with a
  theoretical reference, and show the gap with its uncertainty. A gap is a
  candidate for inspection, not a diagnosis.
- **Visible soiling from a phone photo:** classify clean, dust or droppings on a
  panel and mark the affected region. RGB images cannot show hotspots or lost
  energy, and we make no such claim.
- **A technician-reviewed proposal:** a short evidence summary the service
  company can use to explain an intervention to the owner.

The UNO Q also reads local sensors (temperature, humidity, light, panel
current) and shows the latest findings on its LCD and as NFC tag text that a
technician's phone can read. See the [project pitch](docs/pitch-draft.md) and
the [Italian three-minute narrative](docs/pitch-narrative.md).

## How it works

Electrical, environmental and image data feed local diagnostics on the UNO Q;
maintenance and lifecycle recommendations come from those diagnostics. The
diagram shows the proposed design. Only the parts marked "working" in
[project status](docs/project-status.md) exist today.

```mermaid
flowchart TB
    A["Off-grid photovoltaic system"]
    B["Data collection<br/>Electrical, environmental, phone RGB"]
    C["Arduino UNO Q 4GB<br/>Edge AI"]
    D["Diagnostics<br/>Soiling, expected vs observed"]
    E["Maintenance proposal<br/>technician-reviewed"]

    A --> B --> C --> D --> E
```

The prototype wiring (UNO Q with Base Shield, five Grove modules and a separate
solar charging path) is recorded in [hardware connections](docs/hardware-connections.md):

![PoopVolt prototype electrical schematic](docs/architecture/diagrams/pv-wiring.svg)

More views are in the [architecture index](docs/architecture/README.md).

## What works today

| Area                                                | State                                   |
| --------------------------------------------------- | --------------------------------------- |
| Grove sensors, LCD and NFC on the UNO Q             | Working (bring-up)                      |
| Readings streamed to the Linux side over the Bridge | Working (bring-up)                      |
| SOLARMA inverter log importer and replay            | Working                                 |
| Expected-versus-observed comparison (peers, replay) | Working (scoped)                        |
| Phone RGB inspection upload / CPU adapter           | Implemented; trained model pending      |
| Inspection UI; broader maintenance output           | Implemented UI; broader design proposed |
| STL enclosure concept                               | Not delivered                           |

[Project status and reuse disclosure](docs/project-status.md) has the evidence
and limits for every row, and separates what the team built from what it reuses.

## Build and run

Python (importer, replay and tests), with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
uv run pytest
# Downloads the pinned SOLARMA export (needs network) and loads it
uv run python -c "from poopvolt import solarma as s; d = s.fetch('data/solarma/raw'); r = s.load_details(d / 'details.txt'); print(len(r), 'rows,', len(s.by_device(r)), 'inverters')"
```

Firmware and the bench setup: follow
[Replicate the UNO Q prototype](docs/replicate-uno-q-setup.md) (laptop tools,
wiring, flashing and checks) and [UNO Q setup](docs/uno-q-setup.md). The parts,
quantities and approximate cost are in the [bill of materials](hardware/bom.md).

## Validation

Numbers we have, with their origin:

- **Measured on the UNO Q:** CPU-only inference of reference models, for
  example NanoDet-Plus at 416x416 in 258 ms and YOLOX-S at 640x640 in 2.27 s
  ([model budget](docs/uno-q-model-budget.md)). No PoopVolt model has been run
  yet.
- **Replayed:** the SOLARMA export loads as 58,687 detail rows from 13
  inverters, with 1,157 communication outages and no irradiance values
  ([data plan](docs/data-plan.md)). One plant does not show how a model
  generalises.
- **Approximate device cost:** about 145 for the prototype, from single-unit
  list prices ([bill of materials](hardware/bom.md)). It is not a production
  cost.

- **Replayed and simulated (peer comparison):** on the SOLARMA replay, each of
  the 12 inverters with a baseline is compared with its peers; 2 are flagged as
  producing unusually little (one stopped producing in late July, one fell
  about 25 % below its peers). A **simulated** loss injected into the other
  inverters is flagged in all 10 tested cases from 8 % upwards, in 4 of 10 at
  4 to 6 %, and mostly not at 2 %. The flag threshold was chosen after seeing
  the data, so this is not an independent validation. Details, method and
  charts: [comparison results](docs/comparison-results.md).
- **Replayed, the improvement over today:** inverter 1 kept logging but
  produced nothing from 21 July to the end of the record on 3 October 2019,
  except on one day. Nothing in the data shows the output being restored in
  those 75 days. On the 30 days with a peer reference, it fell about 550 kWh
  short of its peers (a lower bound, because days without a reference are not
  counted). A daily peer check puts it below 70 % of its expected output on 21
  July, its first day without production.

Not yet available: soiling classifier accuracy, a weather-adjusted expected
production (the replay has no irradiance), and inference time of a PoopVolt
model on the board. They will be added here, each labelled as measured,
replayed or simulated.

## Licence and reuse

The repository is MIT licensed ([LICENSE](LICENSE)). SOLARMA data is MIT
licensed and its notice is kept in [`data/solarma/NOTICE.md`](data/solarma/NOTICE.md).
[Project status](docs/project-status.md) lists what is pre-existing.

## Repository layout

- `docs/`: architecture, pitch and reference documentation.
- `presentation/`: HTML presentation draft.
- `poopvolt/`: Python package, managed with [uv](https://docs.astral.sh/uv/).
- [firmware/](firmware/README.md): Arduino UNO Q sketches (sensor bring-up, NFC station).
- [hardware/](hardware/README.md): available parts and substitutions, KiCad
  schematic; 3D-printable parts are planned.
- `data/`: measurements and fixtures; SOLARMA replay notice in `data/solarma/`.
- `tests/`: Python tests, run with `uv run pytest`.

Set up the Python environment with `uv sync`.

## Phone-to-edge inspection

The UNO Q Linux service accepts mobile phone photographs and serves the inspection
dashboard at the same URL. Start locally with:

```sh
uv sync --extra desktop
uv run --extra desktop poopvolt-inspect
```

Open `http://localhost:8000/`. The trained ONNX artifact and export/class
configuration remain placeholders; the API reports model-not-ready until supplied
and never substitutes demo predictions in the API. The home page opens a labeled
visual demo for layout review. See [phone inspection setup](docs/phone-inspection.md)
for exact UNO Q commands, API details, model contract, and phone/laptop workflow.
The board reuses its existing OpenCV 4.12/numpy; the desktop extra is for laptops.
See [project status](docs/project-status.md) for implementation and testing limits.

## The Team

| Name                                                                         | GitHub                              | Telegram        |
| ---------------------------------------------------------------------------- | ----------------------------------- | --------------- |
| [Giacomo Lisita](https://www.linkedin.com/in/giacomolisita)                  | <https://github.com/giacolees>      | @younglees      |
| [Gianpaolo Macario](https://www.linkedin.com/in/gmacario/)                   | <https://github.com/gmacario>       | @gmacario       |
| [Lorenzo Palloni](https://www.linkedin.com/in/lorenzopalloni/)               | <https://github.com/lorenzopalloni> | @lorenzopalloni |
| [Federico Nebuloni](https://www.linkedin.com/in/federico-nebuloni-770641246) | <https://github.com/fedenebu>       | @Foxtrot230     |

<!-- EOF -->
