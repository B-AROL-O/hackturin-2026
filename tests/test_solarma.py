"""Tests for the SOLARMA importer, using small synthetic fixtures."""

from datetime import datetime
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
