# Team response to hackTurin 2026

PoopVolt starts with the owner of an older photovoltaic plant who does not know
whether it produces as expected. A proposed expected/observed comparison makes
performance gaps visible. A photovoltaic service company uses the proposed
evidence to explain interventions the owner can understand and assess. The
three-minute story includes the approved strong opening, an MVP software case,
an STL concept, and technician-reviewed regeneration. The theoretical model,
implemented demo scope, and field benefits remain to verify. The
company-funded/free-device offer remains a secondary commercial hypothesis.

## Challenge

We are tackling the **Beyond Solar** challenge with **PoopVolt**, an Edge AI
predictive maintenance system for off-grid photovoltaic installations. See the
[project pitch](docs/pitch-draft.md) for the idea description.

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

## Quick links

- [Three-minute Italian narrative](docs/pitch-narrative.md) — owner, production
  comparison, software demo, STL concept, and regeneration.
- [Project pitch](docs/pitch-draft.md) — proposed product and commercial
  context.
- [Data and demonstration plan](docs/data-plan.md) — phone-camera simulation and
  separate historical SOLARMA replay.
- [Hardware availability](docs/hardware.md) — secured prototype parts and phone
  RGB camera replacement for the unavailable thermal camera.
- [Project status and reuse disclosure](docs/project-status.md) — what works,
  what is incomplete, what we built and what we reuse.
- [HTML presentation draft](presentation/README.md) — architecture, narrative,
  and implementation plan.
- [Presentation guidelines](.agent/README.md) — contributor and agent guidance.
- [Architecture index](docs/architecture/README.md) — diagram hierarchy and
  system design.
- [Coesa Energy evaluator context](docs/company/coesa-energy.md) — researched
  company background, sources, and PoopVolt fit hypotheses for contributors and
  AI models.

- [Documentation reference index](docs/references.md) — official sources and
  retrieval keywords for contributors and AI agents.
- [hackTurin Manuale dei partecipanti](https://docs.google.com/document/u/0/d/1Amd6yVSujHK4o_KcjB97IKTJN76TH6P6QJ-XG2Q1pEk/mobilebasic)
- Dropbox share:
  [hackturin-2026](https://www.dropbox.com/scl/fo/5eclqx2zvtit1mjfkiske/AGWotLCqgu1aaEHfJxRGDaE?rlkey=ni635441clcv6t9ir6xaxde1j&st=n5uyvz8e&dl=0)
- <https://kiro.dev/>

## The Team

- [Giacomo Lisita](https://www.linkedin.com/in/giacomolisita) | GitHub:
  <https://github.com/giacolees> | Telegram: @younglees
- [Gianpaolo Macario](https://www.linkedin.com/in/gmacario/) | GitHub:
  <https://github.com/gmacario> | Telegram: @gmacario
- [Lorenzo Palloni](https://www.linkedin.com/in/lorenzopalloni/) | GitHub:
  <https://github.com/lorenzopalloni> | Telegram: @lorenzopalloni
- [Federico Nebuloni](https://www.linkedin.com/in/federico-nebuloni-770641246) |
  GitHub: <https://github.com/fedenebu> | Telegram: @Foxtrot230

## hackTurin 2026 at a glance

### Events on Luma

- [hackTurin - kickoff](https://luma.com/q34azfxn?tk=ttfAQz)
- [hackTurin](https://luma.com/t2odor1k?tk=Sw9Jz9)
- [hackTurin - premiazione](https://luma.com/gwgj3w45?tk=Np7Euc)

### Presenters during Kickoff

- [Marco Gay](https://www.linkedin.com/in/marcogay) - CEO, Zest. Ex Presidente
  Giovani Imprenditori di Confindustria
- [Federico Sandrone](https://www.linkedin.com/in/federico-sandrone) - CEO,
  Coesa Energy. Presidente Gruppo Giovani Imprenditori di Torino
- ...

### Confirmed Mentors

- [Davide Gomba](https://www.linkedin.com/in/davidegomba) - Seeed Studio
- [Luciano Lavagno](https://www.linkedin.com/in/luciano-lavagno-487495) -
  Politecnico di Torino
- [Andrea Richetta](https://www.linkedin.com/in/andrearichetta) - Arduino
- [Matteo Stoppa](https://www.linkedin.com/in/matteo-stoppa) - Coesa Energy

## Partners and Sponsors

- [Amazon Web Services (AWS)](https://aws.amazon.com)
- [Apeira](https://www.apeira.it/)
- [Arduino](https://www.arduino.cc/)
- [Club TOsto](https://www.clubtosto.com/)
- [COESA Energy](https://landing.coesaenergy.it)
- [GOMA Elettronica](https://www.goma.it)
- [Seeed Studio](https://www.seeedstudio.com)
- Unione Industriali Torino - Gruppo Giovani Imprenditori

### Useful links

- <https://fuorielettrico.vercel.app/>
- <https://www.solarma.it/impianto.html>
- <https://www.solarma.it/servizi.html#progettazione>

<!-- EOF -->
