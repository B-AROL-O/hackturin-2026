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
* Header units are checked against :data:`UNITS`; a different unit is an error.
* Timestamps are naive logger times, assumed to be Europe/Rome local time
  (:data:`LOCAL_TIMEZONE`). The source does not state the timezone; the
  assumption fits the data (power is positive from about 06:00 to 21:00 in
  summer) but is not verified. Duplicate timestamps per device are rejected.
* Sampling is nominally every :data:`NOMINAL_INTERVAL`; longer holes are
  communication outages and are reported by :func:`gaps`, never filled.
"""

from __future__ import annotations

import csv
import hashlib
import urllib.request
from collections import defaultdict
from collections.abc import Iterator
from dataclasses import dataclass
from datetime import datetime, timedelta
from itertools import pairwise
from pathlib import Path
from zoneinfo import ZoneInfo

SOURCE_REPOSITORY = "https://github.com/SOLARMA/pv-analysis-tools"
SOURCE_REVISION = "fc96313e453978fc89211322a8afb966b85f7913"
EXPORT_FOLDER = "2019-10-05-solpev-danfoss-weblogger"

# SHA-256 of the pinned files, verified against the downloaded bytes.
PINNED_SHA256 = {
    "details.txt": "2635281bb709e9b7301bbb095268397fa219b771c3500eed2c3ef0f458e89dae",
    "summary.txt": "5c158cb2091d35e51a9fb18de4a6d5322e91a478923649fabe288b764b97b2e4",
}

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
LOCAL_TIMEZONE = ZoneInfo("Europe/Rome")  # assumed, see module docstring
NOMINAL_INTERVAL = timedelta(minutes=10)

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
# Unit expected in the source header of each numeric field. Fields not listed
# carry no unit in the source (codes, flags, identifiers).
UNITS = {
    "power_w": "W",
    "power_limit_w": "W",
    "energy_today_kwh": "kWh",
    "yield_kwh": "kWh",
    "irradiance_energy_today_kwh": "kWh",
    "irradiance_w_m2": "W/m²",
    "temperature_c": "°C",
    "grid_voltage_v": "V",
    "grid_current_a": "A",
    "grid_frequency_hz": "Hz",
    "dc1_voltage_v": "V",
    "dc1_current_a": "A",
    "dc2_voltage_v": "V",
    "dc2_current_a": "A",
    "dc3_voltage_v": "V",
    "dc3_current_a": "A",
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


def _unit(header: str) -> str | None:
    """Unit in square brackets, or ``None``. Repairs the ``ý`` mojibake of ``²``."""
    if "[" not in header:
        return None
    return header.split("[", 1)[1].split("]", 1)[0].strip().replace("\xfd", "²")


def _parse_number(raw: str) -> float | None:
    raw = raw.strip()
    return float(raw) if raw else None


def _read_table(path: Path, columns: dict[str, str]) -> list[dict[str, str]]:
    with path.open(encoding="latin-1", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t")
        header = next(reader)
        mapped = [columns.get(_strip_unit(h)) for h in header]
        unknown = [h for h, n in zip(header, mapped, strict=True) if n is None]
        if unknown:
            raise ValueError(f"{path.name}: unrecognised columns {unknown!r}")
        names = [n for n in mapped if n is not None]
        for h, n in zip(header, names, strict=True):
            if _unit(h) != UNITS.get(n):
                raise ValueError(
                    f"{path.name}: column {h.strip()!r} has unit {_unit(h)!r}, "
                    f"expected {UNITS.get(n)!r}"
                )
        rows = []
        for line_no, row in enumerate(reader, start=2):
            if not any(cell.strip() for cell in row):
                continue
            if len(row) != len(names):
                raise ValueError(
                    f"{path.name}:{line_no}: expected {len(names)} fields, "
                    f"got {len(row)}"
                )
            rows.append(dict(zip(names, row, strict=True)))
    return rows


def _convert(rows: list[dict[str, str]], key: str) -> list[Record]:
    records: list[Record] = []
    seen: set[tuple[int, datetime]] = set()
    for row in rows:
        values: dict[str, float | None] = {}
        for name, raw in row.items():
            if name in {"timestamp", key} | _TEXT_FIELDS:
                continue
            values[name] = _parse_number(raw)
        serial = row.get("serial", "").strip() or None
        timestamp = datetime.strptime(row["timestamp"].strip(), TIMESTAMP_FORMAT)
        device = int(row[key])
        if (device, timestamp) in seen:
            raise ValueError(f"duplicate record for device {device} at {timestamp}")
        seen.add((device, timestamp))
        records.append(
            Record(timestamp=timestamp, device=device, values=values, serial=serial)
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
    return {
        d: sorted(rs, key=lambda r: r.timestamp) for d, rs in sorted(groups.items())
    }


def coverage(records: list[Record]) -> dict[str, Coverage]:
    """Present/missing counts per field. Zero counts as present."""
    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for record in records:
        for name, value in record.values.items():
            counts[name][0 if value is not None else 1] += 1
    return {n: Coverage(present=p, missing=m) for n, (p, m) in sorted(counts.items())}


def localize(timestamp: datetime) -> datetime:
    """Attach the assumed logger timezone to a naive timestamp."""
    return timestamp.replace(tzinfo=LOCAL_TIMEZONE)


@dataclass(frozen=True)
class Gap:
    """A hole in one device's samples, from its last sample to the next one."""

    device: int
    start: datetime
    end: datetime

    @property
    def duration(self) -> timedelta:
        return self.end - self.start


def gaps(
    records: list[Record],
    interval: timedelta = NOMINAL_INTERVAL,
    tolerance: float = 1.5,
) -> list[Gap]:
    """Communication outages: consecutive samples more than ``tolerance`` x
    ``interval`` apart, per device. Nothing is interpolated or filled."""
    found = []
    for device, group in by_device(records).items():
        for before, after in pairwise(group):
            if after.timestamp - before.timestamp > interval * tolerance:
                found.append(Gap(device, before.timestamp, after.timestamp))
    return found


def dc_input_series(
    records: list[Record], device: int, number: int
) -> list[tuple[datetime, float | None, float | None]]:
    """``(timestamp, voltage_v, current_a)`` of DC input 1-3 of one inverter.

    The input is an inverter terminal, not necessarily one string. A reading of
    ``0`` is a measurement; ``None`` is missing.
    """
    if number not in (1, 2, 3):
        raise ValueError(f"DC input must be 1, 2 or 3, got {number}")
    volts, amps = f"dc{number}_voltage_v", f"dc{number}_current_a"
    return [
        (r.timestamp, r.values[volts], r.values[amps])
        for r in by_device(records).get(device, [])
    ]


def observed_windows(
    records: list[Record], device: int
) -> dict[str, tuple[datetime, datetime]]:
    """Per day (``YYYY-MM-DD``), first and last sample with positive power.

    Zeros outside this window are overnight/idle readings. It is derived from
    the data itself, so no site location or sun position is assumed.
    """
    windows: dict[str, tuple[datetime, datetime]] = {}
    for record in by_device(records).get(device, []):
        if (record.values.get("power_w") or 0) > 0:
            day = record.timestamp.strftime("%Y-%m-%d")
            first, _ = windows.get(day, (record.timestamp, record.timestamp))
            windows[day] = (first, record.timestamp)
    return windows


@dataclass(frozen=True)
class Snapshot:
    """Readings sharing one logger timestamp; ``replay_time`` is historical."""

    replay_time: datetime
    records: dict[int, Record]


def replay(
    records: list[Record],
    start: datetime | None = None,
    end: datetime | None = None,
) -> Iterator[Snapshot]:
    """Step through ``[start, end]`` in time order, one snapshot per timestamp.

    The time is the historical logger time, not wall-clock time: label anything
    shown from this as replayed. Devices without a sample at a timestamp are
    absent from that snapshot (never zero-filled). Pacing is up to the caller.
    """
    grouped: dict[datetime, dict[int, Record]] = defaultdict(dict)
    for record in records:
        if (start is None or record.timestamp >= start) and (
            end is None or record.timestamp <= end
        ):
            grouped[record.timestamp][record.device] = record
    for timestamp in sorted(grouped):
        yield Snapshot(timestamp, dict(sorted(grouped[timestamp].items())))


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
        with urllib.request.urlopen(f"{base}/{name}", timeout=60) as response:
            (directory / name).write_bytes(response.read())
    verify(directory)
    return directory
