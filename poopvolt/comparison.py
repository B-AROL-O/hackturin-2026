"""Peer-relative expected-versus-observed daily energy on SOLARMA replay data.

This is a scoped channel comparison, not the weather-adjusted theoretical model
the pitch proposes: the SOLARMA export has no irradiance, so there is nothing
to normalise by weather. Instead every inverter is compared with its own peers
on the same days. Read the results with these limits in mind:

* The expectation is *relative*: "what this inverter normally produces compared
  with the others". A fault shared by every inverter, such as dirt on all
  panels, cancels out.
* Differences in capacity, orientation and shading are unknown, so slow drifts
  of a few percent between inverters are expected and are not faults.
* A deviation is a candidate for inspection. It is not a diagnosis and not
  recoverable energy.
* The data is replayed history. Injected losses (:func:`simulate_loss`) are
  synthetic and measure how the method behaves on that injection only.
* Missing days stay missing; a day is never filled with zero.

Method (all chronological, so fitting and evaluation never overlap):

1. Daily energy of an inverter is the maximum of its own ``energy_today_kwh``
   counter, valid only if the counter was still reported late in the evening.
2. Only productive days (fleet median above :data:`MIN_FLEET_KWH`) are used. The
   first ``fit_fraction`` of them fit each inverter's typical ratio to its
   peers; the remaining ones are the evaluation window.
3. An inverter's expected energy on a day is that ratio times the median of
   its peers' energy, each peer scaled by its own typical ratio.
4. The deviation is observed over expected energy in the evaluation window. Its
   band comes from the day-to-day spread of the ratio in the fit window.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, replace
from datetime import date, datetime

from poopvolt.solarma import Record, by_device

# A day's counter must still be reported at or after this hour to count.
COMPLETE_DAY_HOUR = 22
# Days with a fleet median below this many kWh carry no usable signal.
MIN_FLEET_KWH = 5.0
# Inverters producing less than this share of a typical peer have no baseline.
MIN_RELATIVE_OUTPUT = 0.3
MIN_PEERS = 3
# Smallest deviation, in percent, worth flagging even if statistically clear.
# Chosen after seeing that peers of this plant drift apart by about 3 %.
MIN_FLAG_PCT = 5.0
Z = 2.0  # roughly a 95 % band


@dataclass(frozen=True)
class DeviceResult:
    """Outcome for one inverter; ``deviation_pct`` is ``None`` without a baseline."""

    device: int
    relative_output: float
    observed_kwh: float
    expected_kwh: float | None
    deviation_pct: float | None
    band_pct: float | None
    days: int
    flagged: bool

    @property
    def has_baseline(self) -> bool:
        """Whether a comparison against peers was possible."""
        return self.deviation_pct is not None


@dataclass(frozen=True)
class Comparison:
    """Results for all inverters plus the windows they were computed over."""

    provenance: str
    fit_days: tuple[date, date]
    eval_days: tuple[date, date]
    results: dict[int, DeviceResult]


def daily_energy(records: list[Record], device: int) -> dict[date, float]:
    """Energy per day in kWh from the inverter's own daily counter.

    A day whose counter was not reported at or after :data:`COMPLETE_DAY_HOUR`
    is omitted (missing, not zero).
    """
    best: dict[date, float] = {}
    last: dict[date, datetime] = {}
    for record in by_device(records).get(device, []):
        value = record.values.get("energy_today_kwh")
        if value is None:
            continue
        day = record.timestamp.date()
        best[day] = max(best.get(day, value), value)
        if day not in last or record.timestamp > last[day]:
            last[day] = record.timestamp
    return {d: v for d, v in best.items() if last[d].hour >= COMPLETE_DAY_HOUR}


def simulate_loss(
    records: list[Record], device: int, start: date, loss: float
) -> list[Record]:
    """Copy of ``records`` with ``device`` producing ``loss`` less from ``start``.

    Scales the power and the daily energy counter. The result is synthetic and
    must be labelled as simulated wherever it is shown.
    """
    if not 0.0 <= loss < 1.0:
        raise ValueError(f"loss must be in [0, 1), got {loss}")
    scaled = {"power_w", "energy_today_kwh"}
    out = []
    for record in records:
        if record.device == device and record.timestamp.date() >= start:
            values = {
                name: (v * (1.0 - loss) if v is not None and name in scaled else v)
                for name, v in record.values.items()
            }
            record = replace(record, values=values)
        out.append(record)
    return out


def _mad_sd(values: list[float]) -> float:
    """Robust standard deviation estimate (1.4826 x median absolute deviation)."""
    centre = statistics.median(values)
    return 1.4826 * statistics.median(abs(v - centre) for v in values)


class _Model:
    """Fitted peer-relative model: windows, per-inverter ratios and peers."""

    def __init__(self, records: list[Record], fit_fraction: float) -> None:
        self.devices = sorted(by_device(records))
        self.energy = {d: daily_energy(records, d) for d in self.devices}
        days = sorted({day for e in self.energy.values() for day in e})
        fleet = {
            d: statistics.median(
                self.energy[j][d] for j in self.devices if d in self.energy[j]
            )
            for d in days
            if sum(d in self.energy[j] for j in self.devices) > MIN_PEERS
        }
        productive = [d for d in days if d in fleet and fleet[d] >= MIN_FLEET_KWH]
        cut = int(len(productive) * fit_fraction)
        self.fit, self.evaluation = productive[:cut], productive[cut:]
        if len(self.fit) < 5 or len(self.evaluation) < 3:
            raise ValueError("not enough productive days to fit and evaluate")
        self.relative = {
            j: statistics.median(
                [self.energy[j][d] / fleet[d] for d in self.fit if d in self.energy[j]]
                or [0.0]
            )
            for j in self.devices
        }
        self.reference_set = [
            j for j in self.devices if self.relative[j] >= MIN_RELATIVE_OUTPUT
        ]

    def peer_reference(self, device: int, day: date) -> float | None:
        """Median of the scaled peers' energy on ``day``, or ``None``."""
        peers = [
            self.energy[j][day] / self.relative[j]
            for j in self.reference_set
            if j != device and day in self.energy[j]
        ]
        if len(peers) < MIN_PEERS:
            return None
        ref = statistics.median(peers)
        return ref if ref >= MIN_FLEET_KWH else None

    def scale_and_spread(self, device: int) -> tuple[float, float, int]:
        """Typical ratio to the peer reference, its spread and the days used."""
        ratios = []
        for d in self.fit:
            ref = self.peer_reference(device, d)
            if ref is not None and d in self.energy[device]:
                ratios.append(self.energy[device][d] / ref)
        return statistics.median(ratios), _mad_sd(ratios), len(ratios)


def compare(
    records: list[Record],
    fit_fraction: float = 0.6,
    provenance: str = "replayed",
) -> Comparison:
    """Compare every inverter with its peers; see the module docstring."""
    model = _Model(records, fit_fraction)
    results: dict[int, DeviceResult] = {}
    for device in model.devices:
        energy = model.energy[device]
        observed = sum(energy[d] for d in model.evaluation if d in energy)
        relative = model.relative[device]
        if device not in model.reference_set:
            results[device] = DeviceResult(
                device, relative, observed, None, None, None, 0, False
            )
            continue
        scale, spread, n_fit = model.scale_and_spread(device)
        obs_sum = exp_sum = 0.0
        used = 0
        for d in model.evaluation:
            ref = model.peer_reference(device, d)
            if ref is not None and d in energy:
                obs_sum += energy[d]
                exp_sum += scale * ref
                used += 1
        if used == 0:
            results[device] = DeviceResult(
                device, relative, observed, None, None, None, 0, False
            )
            continue
        deviation = (obs_sum / exp_sum - 1.0) * 100.0
        # Uncertainty of the evaluation mean plus that of the fitted scale.
        band = Z * spread / scale * (1 / used + 1 / n_fit) ** 0.5 * 100.0
        flagged = abs(deviation) > max(band, MIN_FLAG_PCT)
        results[device] = DeviceResult(
            device, relative, obs_sum, exp_sum, deviation, band, used, flagged
        )
    return Comparison(
        provenance,
        (model.fit[0], model.fit[-1]),
        (model.evaluation[0], model.evaluation[-1]),
        results,
    )


def daily_series(
    records: list[Record], device: int, fit_fraction: float = 0.6
) -> list[tuple[date, float, float | None]]:
    """``(day, observed_kwh, expected_kwh)`` for every complete day of a device.

    Expected is ``None`` for devices without a baseline and on days without a
    peer reference. Uses the same fit as :func:`compare`.
    """
    model = _Model(records, fit_fraction)
    energy = model.energy[device]
    if device not in model.reference_set:
        return [(d, v, None) for d, v in sorted(energy.items())]
    scale, _, _ = model.scale_and_spread(device)
    series = []
    for d, value in sorted(energy.items()):
        ref = model.peer_reference(device, d)
        series.append((d, value, None if ref is None else scale * ref))
    return series


def detection_sweep(
    records: list[Record], losses: list[float], fit_fraction: float = 0.6
) -> dict[float, tuple[int, int]]:
    """How often an injected loss is flagged, per loss level.

    A synthetic ``loss`` is injected, over the evaluation window, into each
    inverter that has a baseline and is not already flagged. ``(detected,
    tested)`` counts the inverters whose deviation is then flagged and
    negative. The records are replayed history; the losses are synthetic, so
    this measures the method, not a real fault.
    """
    base = compare(records, fit_fraction)
    start = base.eval_days[0]
    testable = [d for d, r in base.results.items() if r.has_baseline and not r.flagged]
    sweep: dict[float, tuple[int, int]] = {}
    for loss in losses:
        detected = 0
        for device in testable:
            changed = compare(
                simulate_loss(records, device, start, loss),
                fit_fraction,
                "simulated",
            )
            result = changed.results[device]
            if result.flagged and (result.deviation_pct or 0.0) < 0.0:
                detected += 1
        sweep[loss] = (detected, len(testable))
    return sweep
