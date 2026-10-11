"""Tests for the peer-relative comparison, using small synthetic fixtures."""

from datetime import date, datetime, timedelta

import pytest

from poopvolt import comparison
from poopvolt.solarma import Record

FIRST_DAY = date(2019, 7, 1)
DAYS = 24  # 14 fit days, 10 evaluation days at fit_fraction 0.6


def _daily_base(index: int) -> float:
    """A varying fleet energy per day (kWh), always above the usable minimum."""
    return 12.0 + (index * 7) % 9


def _records(
    factors: dict[int, float],
    missing: dict[int, set[int]] | None = None,
    late_hour: int = 23,
) -> list[Record]:
    """Two samples a day per inverter; energy is ``factors[device] * base``.

    ``missing`` maps a device to day indexes with no samples at all.
    """
    missing = missing or {}
    records = []
    for index in range(DAYS):
        day = datetime.combine(FIRST_DAY + timedelta(days=index), datetime.min.time())
        for device, factor in factors.items():
            if index in missing.get(device, set()):
                continue
            energy = factor * _daily_base(index)
            for hour, share in ((12, 0.5), (late_hour, 1.0)):
                values: dict[str, float | None] = {
                    "power_w": 1000.0,
                    "energy_today_kwh": energy * share,
                }
                records.append(
                    Record(day.replace(hour=hour), device, values, serial=None)
                )
    return records


FACTORS = {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 0.5}


def test_daily_energy_uses_the_counter_maximum() -> None:
    energy = comparison.daily_energy(_records(FACTORS), 2)
    assert len(energy) == DAYS
    assert energy[FIRST_DAY] == pytest.approx(_daily_base(0))


def test_incomplete_day_is_missing_not_zero() -> None:
    # The counter stops at 18:00, before COMPLETE_DAY_HOUR: no day is valid.
    assert comparison.daily_energy(_records(FACTORS, late_hour=18), 2) == {}


def test_missing_day_stays_missing() -> None:
    records = _records(FACTORS, missing={3: {5, 6}})
    energy = comparison.daily_energy(records, 3)
    assert len(energy) == DAYS - 2
    assert FIRST_DAY + timedelta(days=5) not in energy


def test_unmodified_peers_show_no_deviation() -> None:
    result = comparison.compare(_records(FACTORS))
    for device, outcome in result.results.items():
        assert outcome.has_baseline
        assert outcome.deviation_pct == pytest.approx(0.0, abs=1e-6)
        assert not outcome.flagged, device
    assert result.provenance == "replayed"


def test_windows_are_chronological_and_disjoint() -> None:
    result = comparison.compare(_records(FACTORS))
    assert result.fit_days[0] < result.fit_days[1] < result.eval_days[0]
    assert result.eval_days[0] < result.eval_days[1]


def test_injected_loss_is_flagged_and_negative() -> None:
    records = _records(FACTORS)
    start = comparison.compare(records).eval_days[0]
    changed = comparison.simulate_loss(records, 2, start, 0.20)
    result = comparison.compare(changed, provenance="simulated")
    outcome = result.results[2]
    assert outcome.deviation_pct == pytest.approx(-20.0, abs=0.5)
    assert outcome.flagged
    assert result.provenance == "simulated"
    # Peers are not blamed for one inverter's loss.
    assert not any(r.flagged for d, r in result.results.items() if d != 2)


def test_simulate_loss_does_not_change_the_input() -> None:
    records = _records(FACTORS)
    before = [dict(r.values) for r in records]
    comparison.simulate_loss(records, 1, FIRST_DAY, 0.5)
    assert [dict(r.values) for r in records] == before


def test_simulate_loss_scales_only_from_the_start_day() -> None:
    records = _records(FACTORS)
    start = FIRST_DAY + timedelta(days=10)
    changed = comparison.simulate_loss(records, 1, start, 0.5)
    energy = comparison.daily_energy(changed, 1)
    assert energy[FIRST_DAY] == pytest.approx(_daily_base(0))
    assert energy[start] == pytest.approx(_daily_base(10) * 0.5)


def test_simulate_loss_rejects_nonsense() -> None:
    with pytest.raises(ValueError, match="loss must be"):
        comparison.simulate_loss([], 1, FIRST_DAY, 1.0)


def test_inverter_without_output_has_no_baseline() -> None:
    factors = {**FACTORS, 7: 0.0}
    result = comparison.compare(_records(factors))
    assert not result.results[7].has_baseline
    assert result.results[7].relative_output == 0.0
    assert not result.results[7].flagged
    # It does not disturb the others.
    assert result.results[2].deviation_pct == pytest.approx(0.0, abs=1e-6)


def test_too_few_days_raises() -> None:
    with pytest.raises(ValueError, match="not enough productive days"):
        comparison.compare(_records(FACTORS)[:20])


def test_daily_series_marks_days_without_reference() -> None:
    series = comparison.daily_series(_records(FACTORS), 2)
    assert len(series) == DAYS
    day, observed, expected = series[0]
    assert day == FIRST_DAY
    assert expected == pytest.approx(observed)
    # A device with no baseline has no expected values at all.
    none = comparison.daily_series(_records({**FACTORS, 7: 0.0}), 7)
    assert all(expected is None for _, _, expected in none)


def test_detection_sweep_counts_larger_losses_first() -> None:
    sweep = comparison.detection_sweep(_records(FACTORS), [0.01, 0.30])
    assert sweep[0.01][0] == 0
    assert sweep[0.30] == (6, 6)
