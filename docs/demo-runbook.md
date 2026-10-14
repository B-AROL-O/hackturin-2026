# PoopVolt prototype: demo runbook

Status 2026-10-11 (Lorenzo). This is the shortest path to a working demo on the UNO Q. Details are in the linked pages.

```text
phone (browser) ──Wi-Fi──► UNO Q Linux side :8000  (Docker: inspection server + CV model)
                               ▲  /api/station (latest.json)
                               │
          station_rx.py ◄─Bridge─ UNO Q MCU (station sketch): AHT20, light, panel current, LCD, NFC tag
```

## Who does what on the UNO Q

The board has two halves, and the prototype uses each for what it is good at:

- **MCU (STM32, real time, low bandwidth):** samples sensors at exact rates with
  timer interrupts and semaphores, drives actuators and local I/O (LCD, NFC), and
  keeps running when Linux is busy. It sends the Linux side small, already
  meaningful messages (readings, events), not raw data streams.
- **Linux side (Qualcomm, heavy compute):** large data (images), the CV model,
  the solar model, storage, Wi-Fi and the dashboard API.
- **The Bridge between them** is a 115200-baud UART (about 11 KB/s): fine for
  readings and commands, too slow for images. That is why cameras belong on the
  Linux side.

## What works today (verified on the hardware)

- **Station (MCU):** temperature, humidity, light and solar panel current, shown on the LCD and readable by tapping an Android phone on the NFC reader.
- **Bridge → Linux:** readings once per second, a clear-sky performance index, and CSV logging.
- **Dashboard (Linux, Docker):** take or choose a photo on the phone → CV model on the board (about 0.8 s) → boxes and recommendation. Live station strip, team branding, and delete / clear-all buttons.
- **Tested** from a Samsung S23 Ultra over the venue Wi-Fi.

## Main steps

1. **Flash the MCU** (laptop, USB-C): `arduino-cli compile -b arduino:zephyr:unoq --upload -p /dev/ttyACM0 firmware/station`. Tools and wiring: [replication guide](replicate-uno-q-setup.md).
2. **Wi-Fi on the board** (once; the board remembers it, no sudo): `adb shell nmcli device wifi connect "<SSID>" password "<password>"`, then `adb shell hostname -I`. Never commit Wi-Fi passwords.
3. **Copy the software to the board** and **start the services**: station receiver with `--latest`, then the `poopvolt` Docker container. See [phone inspection: tested route](phone-inspection.md#tested-route-on-our-uno-q-arduinos-python-image-no-sudo). Both come back by themselves after a power cycle: the container through Docker's restart policy, and the station receiver through a user crontab `@reboot` entry running [`start_station_rx.sh`](../firmware/station/linux/start_station_rx.sh) (no sudo; the install line is at the top of the script).
4. **Model:** until the team model is ready, use the [off-the-shelf test model](../models/offtheshelf/README.md) (`export.sh`, then copy to the board's `models/` and run `docker restart poopvolt`).
5. **Demo on the phone:** join the same Wi-Fi (or use the phone's hotspot for the board), then open `http://<board-ip>:8000/`. Don't know the IP? Tap the phone on the NFC reader: the tag text ends with `dashboard: http://<board-ip>:8000`. On Android, take the photo with the Camera app and use **Choose photo**: the in-page **Camera** button can lose the photo when Android reloads the tab. Then tap **Run inspection**.
6. **Clean up:** **Delete inspection** or **Clear all photos on the board** in the page.

## Known issues

- **Test model only:** it proves the pipeline but does not detect our staged soiling (paper on the mini panel). Real detections need Giacomo's model, and the server's YOLOv8 contract needs aligning with his one-target `affected_panel` output.
- **The result image is slow to appear:** after the inspection, the page re-downloads the full photo (about 2.4 MB) from the board over Wi-Fi, instead of reusing the one already on the phone. Fix later in `poopvolt/static/app.js`.
- **No usable panel current yet:** the mini panel can't drive the Waveshare charger (it needs at least 6 V), so the performance index waits for a stronger panel. Field data: [`data/field-2026-10-11/`](../data/field-2026-10-11/README.md).
- **USB drops:** the board disconnected from USB several times, so check the USB-C cable.

## Proposed next step: a fixed camera (design note, not built)

Goal: a camera that watches the panel continuously, with the frame rate set by a timer and semaphore. The CV model runs on the board, and results go to the same API and dashboard.

- **Don't route images through the MCU.** The MCU ↔ Linux Bridge is a UART at 115200 baud (about 11 KB/s), so one 320×240 JPEG takes about 1 s and a raw grayscale frame about 7 s.
- **Connect the camera to the Linux side instead:** a USB webcam on a USB-C hub, or a MIPI camera through the Arduino Media Carrier. A Linux capture loop driven by a periodic timer (the same timer + semaphore pattern as the [IMU bridge](uno-q-setup.md)) takes frames, runs the existing `Detector`, and saves each result as an inspection, so it appears on the dashboard like a phone photo.
- **The MCU stays the real-time side** for sensors and actuators. If needed, it can trigger a capture over the Bridge, for example on a schedule or an event.
- **Open questions:** which camera (USB webcam or the Media Carrier's MIPI camera), the frame rate (one frame every few seconds is enough for panels; inference takes about 0.8 s), and whether to keep every frame or only frames with detections (storage prunes beyond 100 inspections or 250 MB).
