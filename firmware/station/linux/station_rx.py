"""Linux side of the station sketch (runs on the UNO Q, not the laptop).

Registers the "station" method on arduino-router and receives the readings the
MCU pushes once per second with Bridge.notify(). For each reading it computes a
relative performance index of the solar panel:

    ratio = panel current (mA) / clear-sky irradiance expected on the panel (W/m2)
    perf  = ratio / ratio measured once with the panel clean   (100 % = as clean)

The expected irradiance comes from solar_model.py (sun position for the given
place and time, clear-sky model). The index is only computed while the sun is
above --min-elevation, where the model is most accurate. Clouds lower the index
just like soiling does, so compare readings taken under a clear sky.

The index goes back to the MCU (LCD and NFC text) and every reading is written
as CSV to stdout or, with --csv PATH, appended to a file.

Run on the board, passing the laptop's UTC time because the board clock may be
wrong:
    python3 station_rx.py --now "$(date +%s)" [--calibrate 30] [--csv station.csv]
"""

import argparse
import collections
import csv
import datetime
import json
import math
import os
import socket
import statistics
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "vendor"))
import msgpack
import solar_model

ROUTER_SOCKET = "/var/run/arduino-router.sock"
METHOD = "station"
MCU_PERF_METHOD = "set_perf"  # provided by the sketch: perf in tenths of %, -1 = none
MIN_PANEL_MA = 5.0  # below this the current is ADC noise (about 4 mA per step)
# A baseline only applies to the place and panel orientation it was made for.
GEOMETRY = ("lat", "lon", "tilt", "azimuth")

Reading = collections.namedtuple(
    "Reading", "seq uptime_ms temp_c rh_pct light_raw pv_ma pv_mv"
)
FIELDS = (
    ("utc",)
    + Reading._fields
    + ("sun_elev_deg", "sun_az_deg", "poa_clear_wm2", "ratio", "perf_pct")
)


class PerformanceIndex:
    """Clear-sky-normalized panel current, relative to a clean-panel baseline."""

    def __init__(self, args):
        self.args = args
        self.baseline = None
        self.calibration = []
        self.calibrate_until = None
        if args.calibrate:
            self.calibrate_until = time.monotonic() + args.calibrate
        elif os.path.exists(args.baseline):
            with open(args.baseline, encoding="utf-8") as f:
                record = json.load(f)
            self.baseline = record["ratio"]
            if not self._geometry_matches(record):
                self.baseline = None

    def _geometry_matches(self, record):
        """False, with a message, if the baseline was made for another setup."""
        made_for = {k: record[k] for k in GEOMETRY if k in record}
        now = {k: getattr(self.args, k) for k in GEOMETRY}
        if all(math.isclose(v, now[k], abs_tol=1e-9) for k, v in made_for.items()):
            return True
        print(
            f"ignoring {self.args.baseline}: it was made for {made_for} but this "
            f"run uses {now}; run once with --calibrate to make a new baseline",
            file=sys.stderr,
        )
        return False

    def update(self, unix_s, pv_ma):
        """Return (elevation, azimuth, poa, ratio, perf_pct); NaN where not valid."""
        a = self.args
        elev, az = solar_model.sun_position(unix_s, a.lat, a.lon)
        poa = solar_model.clear_sky_poa(elev, az, a.tilt, a.azimuth)
        ratio = perf = math.nan
        if elev >= a.min_elevation and pv_ma >= MIN_PANEL_MA:
            ratio = pv_ma / poa
            if self.calibrate_until is not None:
                self.calibration.append(ratio)
            elif self.baseline:
                perf = 100.0 * ratio / self.baseline
        if (
            self.calibrate_until is not None
            and time.monotonic() >= self.calibrate_until
        ):
            self._finish_calibration(unix_s)
        return elev, az, poa, ratio, perf

    def _finish_calibration(self, unix_s):
        self.calibrate_until = None
        if len(self.calibration) < 5:
            print(
                f"calibration failed: only {len(self.calibration)} valid samples "
                f"(need sun above {self.args.min_elevation} deg and panel current "
                f">= {MIN_PANEL_MA} mA)",
                file=sys.stderr,
            )
            return
        self.baseline = statistics.median(self.calibration)
        record = {
            "ratio": self.baseline,
            "samples": len(self.calibration),
            "utc": iso_utc(unix_s),
            "lat": self.args.lat,
            "lon": self.args.lon,
            "tilt": self.args.tilt,
            "azimuth": self.args.azimuth,
        }
        with open(self.args.baseline, "w") as f:
            json.dump(record, f, indent=2)
        print(
            f"calibrated: clean ratio {self.baseline:.4f} mA per W/m2 from "
            f"{len(self.calibration)} samples, saved to {self.args.baseline}",
            file=sys.stderr,
        )


def iso_utc(unix_s):
    return datetime.datetime.fromtimestamp(unix_s, datetime.UTC).isoformat(
        timespec="seconds"
    )


def register(sock, unpacker):
    sock.sendall(msgpack.packb([0, 1, "$/register", [METHOD]]))
    while True:
        unpacker.feed(sock.recv(4096))
        for msg in unpacker:
            if msg[0] == 1 and msg[1] == 1:
                if msg[2] is not None:
                    raise RuntimeError(f"register '{METHOD}' failed: {msg[2]}")
                return


def parse_args():
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("--csv", help="append readings to this CSV file instead of stdout")
    p.add_argument(
        "--now",
        type=float,
        help=(
            "current UTC time as Unix seconds (from the laptop: $(date +%%s)); "
            "corrects the board clock"
        ),
    )
    p.add_argument("--lat", type=float, default=45.07, help="latitude (default Turin)")
    p.add_argument("--lon", type=float, default=7.69, help="longitude (default Turin)")
    p.add_argument("--tilt", type=float, default=0.0, help="panel tilt, 0 = flat")
    p.add_argument(
        "--azimuth",
        type=float,
        default=180.0,
        help="panel facing direction, degrees clockwise from north (180 = south)",
    )
    p.add_argument(
        "--min-elevation",
        type=float,
        default=25.0,
        help="compute the index only with the sun above this (deg)",
    )
    p.add_argument(
        "--calibrate",
        type=float,
        metavar="SECONDS",
        help="panel is clean and in clear sun: record the baseline for this long",
    )
    p.add_argument(
        "--baseline",
        default=os.path.join(HERE, "baseline.json"),
        help="clean-panel baseline file",
    )
    p.add_argument(
        "--latest",
        metavar="PATH",
        help="also keep the latest reading in this JSON file (read by the dashboard)",
    )
    return p.parse_args()


def main():
    args = parse_args()
    clock_offset = args.now - time.time() if args.now else 0.0
    if not args.now and time.gmtime().tm_year < 2026:
        print(
            "warning: board clock looks wrong; pass --now $(date +%s)", file=sys.stderr
        )

    index = PerformanceIndex(args)
    if index.baseline is None and not args.calibrate:
        print(
            "no baseline yet: run once with --calibrate 30 while the panel is "
            "clean in clear sun",
            file=sys.stderr,
        )

    if args.csv:
        with open(args.csv, "a", newline="") as out:
            receive(out, out.tell() == 0, index, clock_offset, args.latest)
    else:
        receive(sys.stdout, True, index, clock_offset, args.latest)


def write_latest(path, record):
    """Atomically replace PATH with RECORD as JSON (NaN becomes null)."""
    clean = {
        k: None if isinstance(v, float) and math.isnan(v) else v
        for k, v in record.items()
    }
    tmp = f"{path}.tmp"
    with open(tmp, "w") as f:
        json.dump(clean, f)
    os.replace(tmp, path)


def receive(out, write_header, index, clock_offset, latest=None):
    writer = csv.writer(out)
    if write_header:
        writer.writerow(FIELDS)

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(ROUTER_SOCKET)
    unpacker = msgpack.Unpacker(raw=False)
    register(sock, unpacker)
    print(f"registered '{METHOD}' on {ROUTER_SOCKET}", file=sys.stderr)

    while True:
        data = sock.recv(4096)
        if not data:
            raise ConnectionError("arduino-router closed the socket")
        unpacker.feed(data)
        for msg in unpacker:
            if msg[0] != 2 or msg[1] != METHOD:
                continue
            reading = Reading(*msg[2])
            now = time.time() + clock_offset
            elev, az, poa, ratio, perf = index.update(now, reading.pv_ma)

            perf_x10 = -1 if math.isnan(perf) else max(0, round(perf * 10))
            sock.sendall(msgpack.packb([2, MCU_PERF_METHOD, [perf_x10]]))

            values = (*reading, elev, az, poa, ratio, perf)
            writer.writerow(
                [iso_utc(now)]
                + [round(v, 4) if isinstance(v, float) else v for v in values]
            )
            out.flush()

            if latest:
                write_latest(
                    latest,
                    {
                        "utc": iso_utc(now),
                        **reading._asdict(),
                        "sun_elev_deg": elev,
                        "poa_clear_wm2": poa,
                        "perf_pct": perf,
                        "calibrated": index.baseline is not None,
                    },
                )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
