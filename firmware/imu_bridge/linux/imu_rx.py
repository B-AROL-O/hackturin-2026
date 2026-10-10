"""Linux side of the IMU -> Linux bridge (runs on the UNO Q, not the laptop).

Registers the "imu" method on arduino-router and receives the samples the MCU
pushes with Bridge.notify(). The reader thread enqueues each sample and
releases a semaphore; the worker thread blocks on it and calls process(), so
the worker wakes once per MCU timer tick.

Run on the board: python3 imu_rx.py
"""

import collections
import os
import socket
import sys
import threading
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor"))
import msgpack  # noqa: E402, RUF100  # pylint: disable=wrong-import-position

ROUTER_SOCKET = "/var/run/arduino-router.sock"
METHOD = "imu"
QUEUE_MAX = 256  # oldest samples are dropped if the worker falls behind
RT_PRIORITY = 50  # SCHED_FIFO priority, applied only when permitted (root)

Sample = collections.namedtuple("Sample", "seq t_us ax ay az gx gy gz rx_ns")

queue: collections.deque = collections.deque(maxlen=QUEUE_MAX)
ready = threading.Semaphore(0)
stats = {"rx": 0, "dropped": 0, "seq_gaps": 0}


def try_realtime():
    """Switch the calling thread to SCHED_FIFO; return False if not permitted."""
    try:
        os.sched_setscheduler(0, os.SCHED_FIFO, os.sched_param(RT_PRIORITY))
        return True
    except PermissionError:
        return False


def register(sock, unpacker):
    """Register the "imu" method on arduino-router and wait for the reply."""
    sock.sendall(msgpack.packb([0, 1, "$/register", [METHOD]]))
    while True:
        unpacker.feed(sock.recv(4096))
        for msg in unpacker:
            if msg[0] == 1 and msg[1] == 1:
                if msg[2] is not None:
                    raise RuntimeError(f"register '{METHOD}' failed: {msg[2]}")
                return


def reader(sock, unpacker):
    """Receive samples from the router and enqueue them for the worker."""
    try_realtime()
    last_seq = None
    while True:
        data = sock.recv(4096)
        if not data:
            raise ConnectionError("arduino-router closed the socket")
        unpacker.feed(data)
        rx_ns = time.monotonic_ns()
        for msg in unpacker:
            if msg[0] != 2 or msg[1] != METHOD:
                continue
            sample = Sample(*msg[2], rx_ns)
            if last_seq is not None and sample.seq != last_seq + 1:
                stats["seq_gaps"] += 1
            last_seq = sample.seq
            if len(queue) == QUEUE_MAX:
                stats["dropped"] += 1
            queue.append(sample)
            stats["rx"] += 1
            ready.release()


def process(sample):
    """Placeholder: replace with the real per-sample processing."""
    del sample


def worker():
    """Wake once per sample, process it, and print one stats line per second."""
    rt = try_realtime()
    print(f"worker started (SCHED_FIFO={'yes' if rt else 'no, run as root to enable'})")
    prev = None
    window_start = time.monotonic()
    n = 0
    max_rx_jitter_ms = 0.0
    while True:
        ready.acquire()  # pylint: disable=consider-using-with
        try:
            sample = queue.popleft()
        except IndexError:  # dropped by deque overflow
            continue
        process(sample)

        n += 1
        if prev is not None:
            mcu_dt_ms = (sample.t_us - prev.t_us) / 1e3
            rx_dt_ms = (sample.rx_ns - prev.rx_ns) / 1e6
            max_rx_jitter_ms = max(max_rx_jitter_ms, abs(rx_dt_ms - mcu_dt_ms))
        prev = sample

        now = time.monotonic()
        if now - window_start >= 1.0:
            print(
                f"rate={n / (now - window_start):6.1f} Hz  "
                f"max_rx_jitter={max_rx_jitter_ms:5.2f} ms  "
                f"gaps={stats['seq_gaps']} dropped={stats['dropped']}  "
                f"a=({sample.ax:+.2f},{sample.ay:+.2f},{sample.az:+.2f}) g  "
                f"w=({sample.gx:+7.1f},{sample.gy:+7.1f},{sample.gz:+7.1f}) dps",
                flush=True,
            )
            window_start, n, max_rx_jitter_ms = now, 0, 0.0


def main():
    """Connect to arduino-router, register the method, and run the threads."""
    sock = socket.socket(  # pylint: disable=consider-using-with
        socket.AF_UNIX, socket.SOCK_STREAM
    )
    sock.connect(ROUTER_SOCKET)
    unpacker = msgpack.Unpacker(raw=False)
    register(sock, unpacker)
    print(f"registered '{METHOD}' on {ROUTER_SOCKET}")
    threading.Thread(target=worker, name="imu_worker", daemon=True).start()
    reader(sock, unpacker)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
