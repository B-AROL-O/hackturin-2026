"""Tests for the SOLARMA importer, using small synthetic fixtures."""

from datetime import datetime, timedelta
from pathlib import Path

import pytest

from poopvolt import solarma

DETAILS_HEADER = (
    "Orario di rilevazione\tNumero dispositivo \tNumero di serie\tPotenza [W]\t"
    "Energia di oggi [kWh]\tTemperatura [°C]\tTensione griglia [V]\t"
    "Corrente griglia [A]\tFrequenza di rete [Hz]\tTens. Fotov. 1 [V]\t"
    "Corr. fotov. 1 [A]\tTens. Fotov. 2 [V]\tCorr. fotov. 2 [A]\t"
    "Tens. Fotov. 3 [V]\tCorr. fotov. 3 [A]\tStato\tModuli C.C.\tErrore\t"
    "Pannello fotovoltaico\tLimite di potenza [W]\tPosizione di fase\tCosPhi\n"
)
ROW_1 = "2019-07-01 12:10:00\t1\t029501N182\t5553\t0.59\t53\t240\t23.058\t49.99\t405\t6.91\t406.6\t6.91\t0\t0\t60\t\t0\t0\t16000\t\t\n"
# Frequency missing, third DC input measured as zero, power measured as zero.
ROW_2 = "2019-07-01 12:00:00\t1\t029501N182\t0\t0.59\t53\t240\t23.058\t\t405\t6.91\t406.6\t6.91\t0\t0\t60\t\t0\t0\t16000\t\t\n"
ROW_3 = "2019-07-01 12:10:00\t2\t101802N182\t9747\t1.023\t57\t240\t40.503\t49.99\t527.1\t6.156\t533.9\t6.165\t543.5\t6.264\t60\t\t0\t0\t16000\t\t\n"


@pytest.fixture
def details(tmp_path: Path) -> Path:
    path = tmp_path / "details.txt"
    path.write_bytes((DETAILS_HEADER + ROW_1 + ROW_2 + ROW_3).encode("latin-1"))
    return path


def test_parses_latin1_and_trims_headers(details: Path) -> None:
    records = solarma.load_details(details)
    assert len(records) == 3
    first = records[0]
    assert first.timestamp == datetime(2019, 7, 1, 12, 10)
    assert first.device == 1
    assert first.serial == "029501N182"
    assert first.values["power_w"] == 5553.0
    assert first.values["temperature_c"] == 53.0


def test_missing_stays_none_and_zero_stays_zero(details: Path) -> None:
    records = solarma.load_details(details)
    assert records[1].values["grid_frequency_hz"] is None
    assert records[1].values["power_w"] == 0.0
    assert records[0].values["dc3_voltage_v"] == 0.0
    assert records[0].values["cos_phi"] is None


def test_series_is_time_ordered_per_device(details: Path) -> None:
    records = solarma.load_details(details)
    points = solarma.series(records, 1, "power_w")
    assert [t.minute for t, _ in points] == [0, 10]
    assert solarma.by_device(records).keys() == {1, 2}


def test_coverage_counts_missing_separately_from_zero(details: Path) -> None:
    cov = solarma.coverage(solarma.load_details(details))["grid_frequency_hz"]
    assert (cov.present, cov.missing, cov.total) == (2, 1, 3)
    assert solarma.coverage(solarma.load_details(details))["power_w"].missing == 0


def test_summary_without_irradiance(tmp_path: Path) -> None:
    path = tmp_path / "summary.txt"
    path.write_bytes(
        (
            "Orario di rilevazione\tNumero registratore di dati\tPotenza [W]\t"
            "Energia di oggi [kWh]\tRendimento conteggiato [kWh]\t"
            "Intensità di irradiamento [W/m\xfd]\tEnergia di irradiamento odierna [kWh]\n"
            "2019-07-01 12:10:00\t0\t121186\t11.542\t\t\t\n"
        ).encode("latin-1")
    )
    (record,) = solarma.load_summary(path)
    assert record.values["power_w"] == 121186.0
    assert record.values["irradiance_w_m2"] is None


def test_rejects_unknown_columns_and_ragged_rows(tmp_path: Path) -> None:
    bad_header = tmp_path / "a.txt"
    bad_header.write_text("Orario di rilevazione\tSorpresa\n", encoding="latin-1")
    with pytest.raises(ValueError, match="unrecognised columns"):
        solarma.load_summary(bad_header)

    ragged = tmp_path / "b.txt"
    ragged.write_bytes((DETAILS_HEADER + "2019-07-01 12:10:00\t1\n").encode("latin-1"))
    with pytest.raises(ValueError, match="expected 22 fields"):
        solarma.load_details(ragged)


def test_verify_detects_missing_and_modified_files(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="is missing"):
        solarma.verify(tmp_path)
    for name in solarma.PINNED_SHA256:
        (tmp_path / name).write_text("tampered")
    with pytest.raises(ValueError, match="pinned"):
        solarma.verify(tmp_path)


def _details_file(tmp_path: Path, *rows: str, header: str = DETAILS_HEADER) -> Path:
    path = tmp_path / "details.txt"
    path.write_bytes((header + "".join(rows)).encode("latin-1"))
    return path


def _row(minute: int, device: int = 1, power: str = "100") -> str:
    """A details row at 12:<minute> with only power and DC input 1 populated."""
    return (
        f"2019-07-01 12:{minute:02d}:00\t{device}\tSN{device}\t{power}\t1\t50\t"
        "240\t1\t50\t400\t5\t\t\t\t\t60\t\t0\t0\t16000\t\t\n"
    )


def test_rejects_unexpected_header_unit(tmp_path: Path) -> None:
    header = DETAILS_HEADER.replace("Potenza [W]", "Potenza [kW]")
    path = _details_file(tmp_path, ROW_1, header=header)
    with pytest.raises(ValueError, match="unit 'kW', expected 'W'"):
        solarma.load_details(path)


def test_irradiance_unit_mojibake_is_repaired(tmp_path: Path) -> None:
    # The real header spells the unit "W/m\xfd"; it must still be accepted.
    path = tmp_path / "summary.txt"
    path.write_bytes(
        (
            "Orario di rilevazione\tNumero registratore di dati\tPotenza [W]\t"
            "Energia di oggi [kWh]\tRendimento conteggiato [kWh]\t"
            "Intensità di irradiamento [W/m\xfd]\t"
            "Energia di irradiamento odierna [kWh]\n"
        ).encode("latin-1")
    )
    assert solarma.load_summary(path) == []


def test_rejects_duplicate_timestamp_for_a_device(tmp_path: Path) -> None:
    path = _details_file(tmp_path, ROW_1, ROW_1)
    with pytest.raises(ValueError, match="duplicate record for device 1"):
        solarma.load_details(path)


def test_same_timestamp_on_different_devices_is_fine(tmp_path: Path) -> None:
    assert len(solarma.load_details(_details_file(tmp_path, ROW_1, ROW_3))) == 2


def test_localize_marks_the_assumed_timezone() -> None:
    summer = solarma.localize(datetime(2019, 7, 1, 12, 10))
    assert summer.utcoffset() == timedelta(hours=2)  # CEST
    assert summer.tzinfo is solarma.LOCAL_TIMEZONE


def test_gaps_report_outages_without_filling(tmp_path: Path) -> None:
    rows = [_row(0), _row(10), _row(20), _row(55), _row(5, device=2)]
    records = solarma.load_details(_details_file(tmp_path, *rows))
    (gap,) = solarma.gaps(records)
    assert gap.device == 1
    assert (gap.start.minute, gap.end.minute) == (20, 55)
    assert gap.duration == timedelta(minutes=35)
    assert len(records) == 5  # nothing was interpolated


def test_dc_input_series_keeps_zero_and_missing_apart(details: Path) -> None:
    records = solarma.load_details(details)
    third = solarma.dc_input_series(records, 1, 3)
    assert [(v, c) for _, v, c in third] == [(0.0, 0.0), (0.0, 0.0)]
    assert solarma.dc_input_series(records, 99, 1) == []
    with pytest.raises(ValueError, match="1, 2 or 3"):
        solarma.dc_input_series(records, 1, 4)


def test_dc_input_missing_stays_none(tmp_path: Path) -> None:
    records = solarma.load_details(_details_file(tmp_path, _row(0)))
    ((_, voltage, current),) = solarma.dc_input_series(records, 1, 2)
    assert (voltage, current) == (None, None)


def test_observed_windows_use_positive_power_only(tmp_path: Path) -> None:
    rows = [_row(0, power="0"), _row(10), _row(20), _row(30, power="0")]
    records = solarma.load_details(_details_file(tmp_path, *rows))
    first, last = solarma.observed_windows(records, 1)["2019-07-01"]
    assert (first.minute, last.minute) == (10, 20)
    assert solarma.observed_windows(records, 2) == {}


def test_replay_steps_in_time_order_without_zero_filling(tmp_path: Path) -> None:
    rows = [_row(20), _row(0), _row(0, device=2), _row(10, device=2)]
    records = solarma.load_details(_details_file(tmp_path, *rows))
    snapshots = list(solarma.replay(records))
    assert [s.replay_time.minute for s in snapshots] == [0, 10, 20]
    assert list(snapshots[0].records) == [1, 2]
    assert list(snapshots[1].records) == [2]  # device 1 has no sample: absent
    assert list(snapshots[2].records) == [1]


def test_replay_window_is_inclusive(tmp_path: Path) -> None:
    rows = [_row(0), _row(10), _row(20), _row(30)]
    records = solarma.load_details(_details_file(tmp_path, *rows))
    window = solarma.replay(
        records, start=datetime(2019, 7, 1, 12, 10), end=datetime(2019, 7, 1, 12, 20)
    )
    assert [s.replay_time.minute for s in window] == [10, 20]
