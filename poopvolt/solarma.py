"""Importer for SOLARMA / SOLPEV Danfoss Comlynx Weblogger exports.

Source: https://github.com/SOLARMA/pv-analysis-tools (MIT licence, notice in
``data/solarma/NOTICE.md``), pinned to :data:`SOURCE_REVISION`. See
``docs/data-plan.md`` for the limits of this dataset.

Parsing rules that matter for fault inference:

* Files are tab-separated, Latin-1 encoded, with whitespace around headers.
* An empty field is *missing* and becomes ``None``. It is never turned into
  zero: a measured ``0`` and an absent value mean different things.
* Device IDs are inverters, not panels or strings. A DC input reading ``0`` is
  not evidence of a failed string; the physical wiring is unverified.
"""

from __future__ import annotations

import csv
import hashlib
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

SOURCE_REPOSITORY = "https://github.com/SOLARMA/pv-analysis-tools"
SOURCE_REVISION = "fc96313e453978fc89211322a8afb966b85f7913"
EXPORT_FOLDER = "2019-10-05-solpev-danfoss-weblogger"

# SHA-256 of the pinned files, verified against the downloaded bytes.
PINNED_SHA256 = {
    "details.txt": "2635281bb709e9b7301bbb095268397fa219b771c3500eed2c3ef0f458e89dae",
    "summary.txt": "5c158cb2091d35e51a9fb18de4a6d5322e91a478923649fabe288b764b97b2e4",
}

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

# Italian header (units stripped) -> canonical field name.
_DETAILS_COLUMNS = {
    "Orario di rilevazione": "timestamp",
    "Numero dispositivo": "device",
    "Numero di serie": "serial",
    "Potenza": "power_w",
    "Energia di oggi": "energy_today_kwh",
    "Temperatura": "temperature_c",
    "Tensione griglia": "grid_voltage_v",
    "Corrente griglia": "grid_current_a",
    "Frequenza di rete": "grid_frequency_hz",
    "Tens. Fotov. 1": "dc1_voltage_v",
    "Corr. fotov. 1": "dc1_current_a",
    "Tens. Fotov. 2": "dc2_voltage_v",
    "Corr. fotov. 2": "dc2_current_a",
    "Tens. Fotov. 3": "dc3_voltage_v",
    "Corr. fotov. 3": "dc3_current_a",
    "Stato": "status",
    "Moduli C.C.": "dc_modules",
    "Errore": "error",
    "Pannello fotovoltaico": "pv_panel",
    "Limite di potenza": "power_limit_w",
    "Posizione di fase": "phase_position",
    "CosPhi": "cos_phi",
}
_SUMMARY_COLUMNS = {
    "Orario di rilevazione": "timestamp",
    "Numero registratore di dati": "logger",
    "Potenza": "power_w",
    "Energia di oggi": "energy_today_kwh",
    "Rendimento conteggiato": "yield_kwh",
    # The irradiance unit is mojibake ("m\xfd") in the source; match on the name.
    "Intensità di irradiamento": "irradiance_w_m2",
    "Energia di irradiamento odierna": "irradiance_energy_today_kwh",
}
_TEXT_FIELDS = {"serial"}
_INT_FIELDS = {"device", "logger"}


@dataclass(frozen=True)
class Record:
    """One logged row. ``values`` maps canonical names to ``float | None``."""

    timestamp: datetime
    device: int
    values: dict[str, float | None]
    serial: str | None = None


@dataclass(frozen=True)
class Coverage:
    """How many samples of a field are present, for coverage checks."""

    present: int
    missing: int

    @property
    def total(self) -> int:
        return self.present + self.missing


def _strip_unit(header: str) -> str:
    return header.split("[", 1)[0].strip()


def _parse_number(raw: str) -> float | None:
    raw = raw.strip()
    return float(raw) if raw else None


def _read_table(path: Path, columns: dict[str, str]) -> list[dict[str, str]]:
    with path.open(encoding="latin-1", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        header = next(reader)
        names = [columns.get(_strip_unit(h)) for h in header]
        unknown = [h for h, n in zip(header, names, strict=True) if n is None]
        if unknown:
            raise ValueError(f"{path.name}: unrecognised columns {unknown!r}")
        rows = []
        for line_no, row in enumerate(reader, start=2):
            if not any(cell.strip() for cell in row):
                continue
            if len(row) != len(names):
                raise ValueError(
                    f"{path.name}:{line_no}: expected {len(names)} fields, got {len(row)}"
                )
            rows.append(dict(zip(names, row, strict=True)))
    return rows


def _convert(rows: list[dict[str, str]], key: str) -> list[Record]:
    records = []
    for row in rows:
        values: dict[str, float | None] = {}
        for name, raw in row.items():
            if name in {"timestamp", key} | _TEXT_FIELDS:
                continue
            values[name] = _parse_number(raw)
        serial = row.get("serial", "").strip() or None
        records.append(
            Record(
                timestamp=datetime.strptime(row["timestamp"].strip(), TIMESTAMP_FORMAT),
                device=int(row[key]),
                values=values,
                serial=serial,
            )
        )
    return records


def load_details(path: str | Path) -> list[Record]:
    """Per-inverter records (``details.txt``); ``Record.device`` is the inverter."""
    return _convert(_read_table(Path(path), _DETAILS_COLUMNS), "device")


def load_summary(path: str | Path) -> list[Record]:
    """Whole-plant records (``summary.txt``); ``Record.device`` is the logger."""
    return _convert(_read_table(Path(path), _SUMMARY_COLUMNS), "logger")


def series(
    records: list[Record], device: int, field: str
) -> list[tuple[datetime, float | None]]:
    """Time-ordered ``(timestamp, value)`` for one device; missing stays ``None``."""
    points = [(r.timestamp, r.values[field]) for r in records if r.device == device]
    return sorted(points, key=lambda p: p[0])


def by_device(records: list[Record]) -> dict[int, list[Record]]:
    """Group records per device, each list time-ordered."""
    groups: dict[int, list[Record]] = defaultdict(list)
    for record in records:
        groups[record.device].append(record)
    return {d: sorted(rs, key=lambda r: r.timestamp) for d, rs in sorted(groups.items())}


def coverage(records: list[Record]) -> dict[str, Coverage]:
    """Present/missing counts per field. Zero counts as present."""
    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for record in records:
        for name, value in record.values.items():
            counts[name][0 if value is not None else 1] += 1
    return {n: Coverage(present=p, missing=m) for n, (p, m) in sorted(counts.items())}


def sha256_of(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify(directory: str | Path) -> None:
    """Raise ``ValueError`` if a pinned file is missing or its hash differs."""
    directory = Path(directory)
    for name, expected in PINNED_SHA256.items():
        path = directory / name
        if not path.is_file():
            raise ValueError(f"{path} is missing; run fetch()")
        actual = sha256_of(path)
        if actual != expected:
            raise ValueError(f"{path}: sha256 {actual} != pinned {expected}")


def fetch(directory: str | Path) -> Path:
    """Download the pinned export into ``directory`` and verify its hashes."""
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    base = (
        "https://raw.githubusercontent.com/SOLARMA/pv-analysis-tools/"
        f"{SOURCE_REVISION}/data/{EXPORT_FOLDER}"
    )
    for name in PINNED_SHA256:
        with urllib.request.urlopen(f"{base}/{name}", timeout=60) as response:  # noqa: S310
            (directory / name).write_bytes(response.read())
    verify(directory)
    return directory
