"""Write the comparison results page and charts from the SOLARMA replay.

Run ``uv run python -m poopvolt.report`` after downloading the pinned data
(``poopvolt.solarma.fetch``), then ``npx prettier --write
docs/comparison-results.md``. It rewrites ``docs/comparison-results.md`` and two
SVG charts under ``docs/images/``. Every chart says in the picture itself
whether it shows replayed history or a simulated loss.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

from poopvolt import comparison, solarma
from poopvolt.comparison import Comparison

LOSSES = [0.02, 0.04, 0.06, 0.08, 0.10, 0.15]
SIMULATED_DEVICE = 10
SIMULATED_LOSS = 0.10
REPLAYED_DEVICE = 9

WIDTH, HEIGHT = 760, 340
LEFT, RIGHT, TOP, BOTTOM = 56, 16, 54, 44
BLUE, GREY, ORANGE, SHADE = "#1f6feb", "#6e7781", "#bc4c00", "#eaeef2"


def chart(
    series: list[tuple[date, float, float | None]],
    result: Comparison,
    title: str,
    label: str,
    observed_name: str,
    colour: str,
) -> str:
    """Daily observed versus expected energy as a standalone SVG string."""
    # Only days with an expectation are drawn: unproductive days (zero output
    # for the whole fleet) and days without a peer reference carry no signal.
    points = [(d, v, e) for d, v, e in series if e is not None]
    days = [d for d, _, _ in points]
    top = max(max(v for _, v, _ in points), max(e or 0.0 for _, _, e in points))
    top = max(top, 1.0) * 1.08
    plot_w, plot_h = WIDTH - LEFT - RIGHT, HEIGHT - TOP - BOTTOM
    first = days[0].toordinal()
    span = max(days[-1].toordinal() - first, 1)

    def x(day: date) -> float:
        return LEFT + plot_w * (day.toordinal() - first) / span

    def y(value: float) -> float:
        return TOP + plot_h * (1 - value / top)

    def path(points: list[tuple[date, float]]) -> str:
        return " ".join(f"{x(d):.1f},{y(v):.1f}" for d, v in points)

    def dots(points: list[tuple[date, float]], fill: str, hollow: bool) -> str:
        paint = f'fill="white" stroke="{fill}"' if hollow else f'fill="{fill}"'
        return "".join(
            f'<circle cx="{x(d):.1f}" cy="{y(v):.1f}" r="3" {paint}/>'
            for d, v in points
        )

    observed = [(d, v) for d, v, _ in points]
    expected = [(d, e or 0.0) for d, _, e in points]
    eval_x = x(result.eval_days[0])
    parts = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}"'
            ' role="img" font-family="sans-serif" font-size="12">'
        ),
        f"<title>{title}</title>",
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="white"/>',
        f'<text x="{LEFT}" y="22" font-size="15" font-weight="bold">{title}</text>',
        f'<text x="{LEFT}" y="40" fill="{colour}" font-weight="bold">{label}</text>',
        (
            f'<rect x="{eval_x:.1f}" y="{TOP}" width="{LEFT + plot_w - eval_x:.1f}"'
            f' height="{plot_h}" fill="{SHADE}"/>'
        ),
        (
            f'<text x="{eval_x + 6:.1f}" y="{TOP + 14}" fill="{GREY}">'
            "evaluation window</text>"
        ),
        f'<text x="{LEFT + 6}" y="{TOP + 14}" fill="{GREY}">fit window</text>',
    ]
    for tick in range(0, int(top) + 1, 20):
        parts.append(
            f'<line x1="{LEFT}" x2="{LEFT + plot_w}" y1="{y(tick):.1f}"'
            f' y2="{y(tick):.1f}" stroke="#d0d7de"/>'
            f'<text x="{LEFT - 8}" y="{y(tick) + 4:.1f}" text-anchor="end">'
            f"{tick}</text>"
        )
    parts.append(
        f'<text x="14" y="{TOP + plot_h / 2:.0f}" transform="rotate(-90 14'
        f' {TOP + plot_h / 2:.0f})" text-anchor="middle">kWh per day</text>'
    )
    for d in (days[0], result.eval_days[0], days[-1]):
        parts.append(
            f'<text x="{x(d):.1f}" y="{HEIGHT - 22}" text-anchor="middle">'
            f"{d.isoformat()}</text>"
        )
    parts.append(
        f'<polyline fill="none" stroke="{GREY}" stroke-width="1"'
        f' stroke-opacity="0.5" points="{path(expected)}"/>'
    )
    parts.append(
        f'<polyline fill="none" stroke="{colour}" stroke-width="1"'
        f' stroke-opacity="0.5" points="{path(observed)}"/>'
    )
    parts.append(dots(expected, GREY, True) + dots(observed, colour, False))
    legend_y = HEIGHT - 6
    parts.append(
        f'<circle cx="{LEFT + 6}" cy="{legend_y - 4}" r="3" fill="{colour}"/>'
        f'<text x="{LEFT + 16}" y="{legend_y}">{observed_name}</text>'
        f'<circle cx="{LEFT + 266}" cy="{legend_y - 4}" r="3" fill="white"'
        f' stroke="{GREY}"/>'
        f'<text x="{LEFT + 276}" y="{legend_y}">expected from peers (fitted)</text>'
        f'<text x="{LEFT + plot_w}" y="{legend_y}" text-anchor="end"'
        f' fill="{GREY}">productive days only</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def results_table(result: Comparison) -> str:
    """Markdown table of every inverter's outcome."""
    lines = [
        (
            "| Inverter | Output vs a typical peer (fit) | Observed kWh | Expected kWh"
            " | Deviation | Flag |"
        ),
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for device, r in result.results.items():
        rel = f"{r.relative_output * 100:.0f} %"
        if not r.has_baseline:
            lines.append(
                f"| {device} | {rel} | {r.observed_kwh:.0f} | no baseline | - |"
                " reports (almost) no output in the fit window |"
            )
            continue
        flag = "candidate for inspection" if r.flagged else "no"
        lines.append(
            f"| {device} | {rel} | {r.observed_kwh:.0f} | {r.expected_kwh:.0f} |"
            f" {r.deviation_pct:+.1f} % (+/- {r.band_pct:.1f}) | {flag} |"
        )
    return "\n".join(lines)


def flagged_notes(records: list[solarma.Record], result: Comparison) -> str:
    """Bullets of what the data shows about each flagged inverter."""
    notes = []
    start = result.eval_days[0]
    for device, r in result.results.items():
        if not r.flagged:
            continue
        series = comparison.daily_series(records, device)
        onset = next(
            (
                d
                for d, observed, expected in series
                if expected
                and expected > comparison.MIN_FLEET_KWH
                and observed < 0.7 * expected
            ),
            None,
        )
        codes: dict[float, int] = {}
        for record in solarma.by_device(records)[device]:
            code = record.values.get("error")
            if record.timestamp.date() >= start and code:
                codes[code] = codes.get(code, 0) + 1
        listed = ", ".join(
            f"{int(c)} ({n} records)"
            for c, n in sorted(codes.items(), key=lambda x: -x[1])
        )
        note = (
            f"- Inverter {device}: first day below 70 % of expected: "
            f"{onset or 'none'}. Logged error codes since {start}: "
            f"{listed or 'none'}; we have not looked up what they mean."
        )
        notes.append(note)
    return "\n".join(notes)


def page(
    records: list[solarma.Record],
    result: Comparison,
    sweep: dict[float, tuple[int, int]],
    simulated: Comparison,
) -> str:
    """The Markdown results page."""
    hashes = "\n".join(
        f"  - `{name}`: `{digest}`" for name, digest in solarma.PINNED_SHA256.items()
    )
    sweep_rows = "\n".join(
        f"| {loss * 100:.0f} % | {hit} of {total} |"
        for loss, (hit, total) in sweep.items()
    )
    simulated_outcome = simulated.results[SIMULATED_DEVICE]
    baseline_drift = result.results[SIMULATED_DEVICE].deviation_pct or 0.0
    flagged = [str(d) for d, r in result.results.items() if r.flagged]
    return f"""# Expected versus observed production: SOLARMA replay

Status: Generated by `uv run python -m poopvolt.report`; do not edit by hand.
This is a **scoped peer comparison on replayed history**, not the
weather-adjusted theoretical model of the [pitch](pitch-draft.md). It supports
the question "which inverters produce unusually little compared with their
peers", nothing more.

## What was measured, replayed and simulated

- **Replayed:** daily energy of 13 inverters of one plant, July to October
  2019, from SOLARMA's `pv-analysis-tools` (revision
  `{solarma.SOURCE_REVISION}`, MIT licence, notice in
  [`data/solarma/NOTICE.md`](../data/solarma/NOTICE.md)). Pinned files:
{hashes}
- **Simulated:** the loss injections below. They are synthetic and measure how
  the method behaves, not a real fault.
- **Measured by us:** nothing in this page.

## Method

Each inverter is compared with the median of its peers on the same days, after
scaling every peer by its own typical ratio. Fit window:
{result.fit_days[0]} to {result.fit_days[1]}. Evaluation window:
{result.eval_days[0]} to {result.eval_days[1]}. Only productive days are used
(fleet median above {comparison.MIN_FLEET_KWH:g} kWh), split in time order so
fitting and evaluation never overlap. Missing days stay missing. The band is
about 95 % and comes from the day-to-day spread in the fit window. An inverter
is flagged when its deviation exceeds both its band and
{comparison.MIN_FLAG_PCT:g} %. That threshold was chosen after seeing that the
peers of this plant drift apart by about 3 %, so the results below are not an
independent validation.

## Results on the replayed data (no injection)

{results_table(result)}

Flagged: inverter(s) {", ".join(flagged) or "none"}. A flag is a candidate for
inspection, not a diagnosis. What the data shows about them:

{flagged_notes(records, result)}

The data does not say why they produce less, and capacity, orientation and
shading are unknown.

![Inverter {REPLAYED_DEVICE}: observed versus expected daily energy,
replayed](images/comparison-inverter-{REPLAYED_DEVICE}-replayed.svg)

## Synthetic loss test (simulated)

A loss of the given size is injected, from the start of the evaluation window,
into each inverter that has a baseline and is not already flagged. The table
counts how many are then flagged as producing less.

| Injected loss (simulated) | Inverters flagged |
| --- | --- |
{sweep_rows}

Example: a simulated {SIMULATED_LOSS * 100:.0f} % loss on inverter
{SIMULATED_DEVICE} is recovered as
{simulated_outcome.deviation_pct:+.1f} % (+/- {simulated_outcome.band_pct:.1f}).
It is smaller than the injected loss because that inverter already runs about
{baseline_drift:+.0f} % against its peers in the evaluation window; the method
measures the loss relative to that baseline.

![Inverter {SIMULATED_DEVICE} with a simulated
{SIMULATED_LOSS * 100:.0f} % loss](images/comparison-simulated-loss.svg)

## Limits

- No irradiance in the data, so no weather adjustment; a shared fault cancels
  out because every inverter is compared with its peers.
- Orientation, capacity and shading are unknown. Differences of a few percent
  between inverters are expected and are not faults.
- A deviation is not a diagnosis, not a confirmed cause and not guaranteed
  recoverable energy.
- One plant, one season: this says nothing about other plants.
- Soiling is not identified. Phone-photo detection is a separate, not yet
  implemented evidence path.

<!-- EOF -->
"""


def main(data_dir: str = "data/solarma/raw", docs_dir: str = "docs") -> None:
    """Load the pinned data, run the comparison and write the page and charts."""
    solarma.verify(data_dir)
    records = solarma.load_details(Path(data_dir) / "details.txt")
    result = comparison.compare(records)
    sweep = comparison.detection_sweep(records, LOSSES)
    injected = comparison.simulate_loss(
        records, SIMULATED_DEVICE, result.eval_days[0], SIMULATED_LOSS
    )
    simulated = comparison.compare(injected, provenance="simulated")

    out = Path(docs_dir)
    (out / "images").mkdir(parents=True, exist_ok=True)
    (out / "images" / f"comparison-inverter-{REPLAYED_DEVICE}-replayed.svg").write_text(
        chart(
            comparison.daily_series(records, REPLAYED_DEVICE),
            result,
            f"Inverter {REPLAYED_DEVICE}: observed vs expected daily energy",
            "REPLAYED HISTORY (SOLARMA 2019), not a measurement of ours",
            "observed (replayed)",
            BLUE,
        ),
        encoding="utf-8",
    )
    (out / "images" / "comparison-simulated-loss.svg").write_text(
        chart(
            comparison.daily_series(injected, SIMULATED_DEVICE),
            simulated,
            f"Inverter {SIMULATED_DEVICE}: simulated {SIMULATED_LOSS * 100:.0f} % loss",
            "SIMULATED LOSS injected into replayed data, not a real fault",
            "observed (with simulated loss)",
            ORANGE,
        ),
        encoding="utf-8",
    )
    (out / "comparison-results.md").write_text(
        page(records, result, sweep, simulated), encoding="utf-8"
    )


if __name__ == "__main__":
    main(*sys.argv[1:3])
