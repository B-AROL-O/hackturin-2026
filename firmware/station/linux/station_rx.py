"""Linux side of the station sketch (runs on the UNO Q, not the laptop).

Registers the "station" method on arduino-router and receives the readings the
MCU pushes once per second with Bridge.notify(). Each reading is passed to
process() and written as a CSV line to stdout or, with --csv PATH, appended to
a file.

Run on the board: python3 station_rx.py [--csv station.csv]
"""

import argparse
import collections
import csv
import os
import socket
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor"))
import msgpack  # pylint: disable=wrong-import-position

ROUTER_SOCKET = "/var/run/arduino-router.sock"
METHOD = "station"

Reading = collections.namedtuple(
    "Reading", "seq uptime_ms temp_c rh_pct light_raw pv_ma pv_mv"
)
FIELDS = ("rx_unix_s",) + Reading._fields


def register(sock, unpacker):
    """Register METHOD on arduino-router and wait for the acknowledgement."""
    sock.sendall(msgpack.packb([0, 1, "$/register", [METHOD]]))
    while True:
        unpacker.feed(sock.recv(4096))
        for msg in unpacker:
            if msg[0] == 1 and msg[1] == 1:
                if msg[2] is not None:
                    raise RuntimeError(f"register '{METHOD}' failed: {msg[2]}")
                return


def process(reading):  # pylint: disable=unused-argument
    """Placeholder: replace with the real processing.

    Examples: alerts, fusion with CV results.
    """


def main():
    """Parse arguments and write readings to a CSV file or stdout."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv", help="append readings to this CSV file instead of stdout"
    )
    args = parser.parse_args()

    if args.csv:
        with open(args.csv, "a", encoding="utf-8", newline="") as out:
            receive(out, write_header=out.tell() == 0)
    else:
        receive(sys.stdout, write_header=True)


def receive(out, write_header):
    """Register with arduino-router and write each reading as a CSV row."""
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
            process(reading)
            writer.writerow(
                [
                    f"{time.time():.3f}",
                    *(round(v, 2) if isinstance(v, float) else v for v in reading),
                ]
            )
            out.flush()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
