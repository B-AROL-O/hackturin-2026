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
- `SCHED_FIFO` on Linux needs root (`sudo python3 imu_rx.py`).
- The board has no network until Wi-Fi is configured. The Edge Impulse runner image (`ei-models-runner`) is already on the board.

## Grove sensor diagnostic (`firmware/sensor_diag`)

This uses the Base Shield at 3.3 V on the header I2C bus (`Wire`): AHT20 at 0x38, 16x2 LCD at 0x3E, PN532 at 0x24 or on the shield UART port (D0/D1 = `Serial1`; the Bridge uses `Serial2`), and the light sensor on A0. Libraries: `arduino-cli lib install "Adafruit AHTX0" "Adafruit PN532" "Grove - LCD RGB Backlight"`. Create `Adafruit_PN532` at runtime with `new`. A global or function-local `static` instance hangs the MCU before `setup()`.
