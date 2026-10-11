"""Tests for the station's sun model and panel performance index.

The reference sun positions were computed once with pvlib (Turin, 45.07 N,
7.69 E) and are fixed here, so the tests do not need pvlib. The receiver script
imports ``msgpack`` at module level; it is replaced by an empty stand-in
because these tests never talk to the Bridge.
"""

import calendar
import io
import json
import math
import sys
import time
import types
from contextlib import redirect_stderr
from datetime import datetime
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "firmware/station/linux"))
sys.modules.setdefault("msgpack", types.ModuleType("msgpack"))

import solar_model
import station_rx

LAT, LON = 45.07, 7.69
# (unix seconds, elevation deg, azimuth deg) from pvlib.
REFERENCE = [
    (1791698400, 2.6832, 102.7522),  # 2026-10-11 06:00 UTC
    (1791714600, 36.8049, 165.6966),  # 2026-10-11 10:30 UTC
    (1791730800, 17.6475, 239.6897),  # 2026-10-11 15:00 UTC
    (1782036000, 61.5348, 131.8633),  # 2026-06-21 10:00 UTC
    (1797850800, 21.2088, 173.2875),  # 2026-12-21 11:00 UTC
    (1791756000, -48.7944, 330.6986),  # 2026-10-11 22:00 UTC (night)
]
NOON = calendar.timegm(datetime(2026, 10, 11, 10, 30).timetuple())  # sun about 37 deg


@pytest.mark.parametrize("unix_s, elevation, azimuth", REFERENCE)
def test_sun_position_matches_pvlib(unix_s: int, elevation: float, azimuth: float):
    got_elevation, got_azimuth = solar_model.sun_position(unix_s, LAT, LON)
    assert got_elevation == pytest.approx(elevation, abs=0.02)
    assert got_azimuth == pytest.approx(azimuth, abs=0.02)


def test_no_irradiance_at_night_and_more_with_a_higher_sun():
    assert solar_model.clear_sky_poa(-10.0, 0.0, 0.0, 180.0) == 0.0
    low = solar_model.clear_sky_poa(30.0, 180.0, 0.0, 180.0)
    high = solar_model.clear_sky_poa(60.0, 180.0, 0.0, 180.0)
    assert 0.0 < low < high < 1353.0


def _args(tmp_path: Path, **overrides):
    values = {
        "lat": LAT,
        "lon": LON,
        "tilt": 0.0,
        "azimuth": 180.0,
        "min_elevation": 25.0,
        "calibrate": None,
        "baseline": str(tmp_path / "baseline.json"),
    }
    values.update(overrides)
    return types.SimpleNamespace(**values)


def _calibrated(tmp_path: Path, current_ma: float = 100.0):
    """Run a short calibration and return the saved baseline path."""
    index = station_rx.PerformanceIndex(_args(tmp_path, calibrate=0.01))
    for second in range(6):
        index.update(NOON + second, current_ma)
    time.sleep(0.02)  # the calibration window ends
    with redirect_stderr(io.StringIO()):
        index.update(NOON + 7, current_ma)
    assert index.baseline is not None
    return Path(index.args.baseline)


def test_index_is_100_percent_for_the_calibrated_current(tmp_path: Path):
    _calibrated(tmp_path, 100.0)
    index = station_rx.PerformanceIndex(_args(tmp_path))
    # The baseline is a median over a few seconds, so allow a little tolerance.
    assert index.update(NOON, 100.0)[4] == pytest.approx(100.0, abs=0.1)
    assert index.update(NOON, 80.0)[4] == pytest.approx(80.0, abs=0.1)


def test_index_is_not_computed_without_signal(tmp_path: Path):
    _calibrated(tmp_path)
    index = station_rx.PerformanceIndex(_args(tmp_path))
    assert math.isnan(index.update(NOON, 3.0)[4])  # below the minimum current
    assert math.isnan(index.update(NOON + 5 * 3600, 100.0)[4])  # sun below 25 deg


def test_failed_calibration_saves_nothing(tmp_path: Path):
    index = station_rx.PerformanceIndex(_args(tmp_path, calibrate=0.01))
    index.update(NOON, 100.0)
    time.sleep(0.02)
    with redirect_stderr(io.StringIO()) as err:
        index.update(NOON + 1, 100.0)
    assert "calibration failed" in err.getvalue()
    assert index.baseline is None
    assert not (tmp_path / "baseline.json").exists()


def test_baseline_for_another_orientation_is_ignored(tmp_path: Path):
    path = _calibrated(tmp_path)
    assert json.loads(path.read_text(encoding="utf-8"))["tilt"] == 0.0
    with redirect_stderr(io.StringIO()) as err:
        index = station_rx.PerformanceIndex(_args(tmp_path, tilt=30.0))
    assert index.baseline is None
    assert "ignoring" in err.getvalue()
    # The same orientation still works.
    assert station_rx.PerformanceIndex(_args(tmp_path)).baseline is not None
