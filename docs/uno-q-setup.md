# UNO Q setup (Arch Linux laptop)

Toolchain: `arduino-cli` (pacman `arduino-cli`); `adb` ships with the core.

```sh
arduino-cli core update-index
arduino-cli core install arduino:zephyr
arduino-cli lib install Arduino_Modulino Arduino_RouterBridge
ADB=$(ls -d ~/.arduino15/packages/arduino/tools/adb/*/ | tail -1)adb
```

Your user must be in `uucp` for `/dev/ttyACM0`. Always pass `-p /dev/ttyACM0`: `arduino-cli board list` also shows other teams' UNO Qs on the venue Wi-Fi.

## IMU bridge placeholder (`firmware/imu_bridge`)

The Modulino Movement module is on Qwiic (Wire1). On the MCU, a `k_timer` ISR runs at 100 Hz and gives a semaphore. A sampler thread then sends `Bridge.notify("imu", seq, t_us, ax, ay, az, gx, gy, gz)` to `arduino-router`. On Linux, `linux/imu_rx.py` reads from the router socket and posts a semaphore for each sample, which wakes the `process()` worker.

```sh
# MCU
arduino-cli compile -b arduino:zephyr:unoq --upload -p /dev/ttyACM0 firmware/imu_bridge
arduino-cli monitor -p /dev/ttyACM0 --config baudrate=9600   # Monitor heartbeat

# Linux side (board has no pip: vendor an aarch64 cp313 msgpack wheel)
uvx pip download msgpack --only-binary=:all: --platform manylinux2014_aarch64 --python-version 3.13 -d /tmp/wh
$ADB shell mkdir -p imu_bridge
$ADB push firmware/imu_bridge/linux/imu_rx.py /tmp/wh/msgpack-*.whl imu_bridge/
$ADB shell 'cd imu_bridge && python3 -m zipfile -e msgpack-*.whl vendor && python3 -u imu_rx.py'
```

Measured: 100 Hz, no gaps or drops. Arrival jitter is about 0.6 ms, with peaks up to about 3 ms (not using `SCHED_FIFO`).

## Gotchas

- The MCU↔Linux UART runs at 115200 baud, about 11 KB/s. One sample is about 50 B, so 100 Hz uses about 45% of the link. For higher rates, batch samples.
- Sketch threads get their stacks from a pool of 2 × 1024 B, and the Bridge already uses one. A larger `k_thread_stack_alloc` fails silently and the sketch hangs.
- `arduino-cli monitor` exits immediately when stdin is closed (scripts, agents): use `sleep 30 | arduino-cli monitor …`. Only one reader can hold `/dev/ttyACM0`.
- `SCHED_FIFO` on Linux needs root (`sudo python3 imu_rx.py`).
- The board has no network until Wi-Fi is configured. The Edge Impulse runner image (`ei-models-runner`) is already on the board.

## Grove sensor diagnostic (`firmware/sensor_diag`)

This uses the Base Shield at 3.3 V on the header I2C bus (`Wire`): AHT20 at 0x38, 16x2 LCD at 0x3E, PN532 at 0x24 or on the shield UART port (D0/D1 = `Serial1`; the Bridge uses `Serial2`), and the light sensor on A0. Libraries: `arduino-cli lib install "Adafruit AHTX0" "Adafruit PN532" "Grove - LCD RGB Backlight"`. Verified: AHT20, LCD and light sensor all OK, PN532 OK over UART (firmware 1.6).

## Station sketch (`firmware/station`)

Reads the sensors (including the solar panel current on A1, zero offset 266.5 mV) and shows them on the LCD. The PN532 (on the UART port) emulates a read-only NFC Forum Type 4 tag. Its NDEF Text record holds the current readings and is refreshed every second, so a phone tap (Android, for example with NFC Tools) shows the data when the LCD can't be read. In this mode the PN532 does not read cards. Verified: a full NDEF read from a phone (Monitor shows `nfc_reads` increasing).

It also streams the readings to the Linux side once per second with `Bridge.notify("station", seq, uptime_ms, temp_c, rh_pct, light_raw, pv_ma, pv_mv)`. On the board, `linux/station_rx.py` receives them, computes the panel **performance index**, sends it back to the MCU (`set_perf`, shown as `P…%` on the LCD and `perf=` in the NFC text), and writes CSV. It uses the same vendored msgpack as the IMU receiver:

```sh
$ADB shell mkdir -p station
$ADB push firmware/station/linux/station_rx.py firmware/station/linux/solar_model.py /tmp/wh/msgpack-*.whl station/
$ADB shell 'cd station && python3 -m zipfile -e msgpack-*.whl vendor'

# once, with the panel clean and in clear sun (sun above 25 deg): record the baseline
$ADB shell "cd station && python3 station_rx.py --now $(date +%s) --calibrate 30"
# then
$ADB shell "cd station && python3 station_rx.py --now $(date +%s) --csv station.csv"
```

How the index works:

- `ratio = panel current (mA) / expected clear-sky irradiance on the panel (W/m²)`, and `perf = ratio / clean ratio` (100 % means as good as when calibrated). The clean ratio is saved in `baseline.json` next to the script.
- The expected irradiance comes from `solar_model.py`. It uses the sun position (NOAA equations), Kasten–Young air mass, the Meinel direct-beam model, and 10 % diffuse, for the given place and time. Defaults: Turin, panel flat (`--lat`, `--lon`, `--tilt`, `--azimuth` to change).
- `--now $(date +%s)` passes the laptop's UTC time, because the board clock is wrong without network time.
- Checked against `pvlib`: sun position within 0.02°. Irradiance is about 9 % above the Ineichen clear-sky model on average, but calibration cancels a constant offset. What remains is drift with sun height: about 8 % with the sun above 25° (`--min-elevation`, default), which in October-November means roughly 10:00–17:00. So the index flags losses of roughly 10–15 % or more.
- Limits: clouds lower the index just like soiling; a full battery stops the charger drawing current (keep a load such as a phone on the Waveshare USB OUT); the light sensor saturates (about 640) and is not used; no panel voltage yet, so this is a relative index, not efficiency in %.

CSV columns: `utc` (corrected), the reading fields, `sun_elev_deg`, `sun_az_deg`, `poa_clear_wm2`, `ratio`, `perf_pct` (`nan` when not computed: sun too low, or panel current under 5 mA).
