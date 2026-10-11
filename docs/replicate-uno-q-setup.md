# Replicate the UNO Q prototype

How to rebuild Lorenzo's working bench setup from scratch: UNO Q, Grove sensors, LCD, NFC tag, and the solar charging path with the current sensor. Wiring diagram: [hardware connections](hardware-connections.md) ([PDF](architecture/diagrams/pv-wiring.pdf)). Background and gotchas: [UNO Q setup](uno-q-setup.md).

## Status (2026-10-11)

What works, verified on the hardware:

- `station` sketch: AHT20 temperature and humidity, light sensor (A0), LCD, and the solar current sensor (A1).
- NFC: tapping an Android phone reads the live readings as tag text.
- Current sensor zero offset calibrated in the dark: 266.5 mV, meaning 0 ± 3 mA.
- Readings stream once per second to the board's Linux side over the Bridge, received by `station_rx.py` as CSV.
- Panel performance index (relative, clear-sky model + clean baseline) computed on the board's Linux side and shown on the LCD and NFC text. The model is checked against pvlib and the return path to the MCU works.
- Solar path wired: panel → current sensor → Waveshare Solar Power Manager → 1000 mAh LiPo. The Waveshare's ON LED and all four battery LEDs are lit.

Still pending:

- Calibrating the performance index in clear sun, then the demo (partly cover or soil the panel, and watch `P…%` drop). Waiting for Gianpaolo's solar panel; the mini panel may be too weak for the Waveshare's 6 V input.
- Current reading and Solar Charge LED under real sunlight. The panel showed only 4.55 V open-circuit at dusk, below the Waveshare's 6 V input, and its rating isn't known.
- Whether the Waveshare's USB OUT (5 V / 1 A) can run the UNO Q. Arduino recommends a 5 V / 3 A supply.
- The phone camera and CV model: owned by Giacomo (see [model budget](uno-q-model-budget.md)).
- Panel voltage (resistor divider into A2) for absolute power and efficiency: optional, later.
- Wi-Fi and network time on the board. Until then, pass the laptop time with `--now`.

Decisions taken:

- The UNO Q is powered from USB-C. The solar side is a separate, measured subsystem with no shared wire.
- The HRS1358 charger and the LM2596 step-down sold as "HAS4966" are not used. A step-down can't make 5 V from a 3.7 V LiPo.
- The PN532 runs in UART mode on the shield's UART port, and the sketch makes it act as an NFC tag. In that mode it doesn't read cards.

## Parts

- Arduino UNO Q, plus a USB-C cable to the laptop
- Seeed Grove Base Shield, with its VCC switch on **3.3 V**
- Grove AHT20, Grove 16x2 LCD, Grove NFC (PN532), Grove Light Sensor (P), Grove 2.5A DC Current Sensor (ACS70331), and 5 Grove cables
- Waveshare Solar Power Manager (5 V / 1 A version), mini solar panel R1123, 3.7 V LiPo with a PH2.0 JST plug
- Multimeter. Soldering only if the panel's wires need extending.

## 1. Laptop tools (Ubuntu 24.04, same base as the devcontainer)

Flashing needs the board's USB connection. The devcontainer doesn't pass USB through by default, so run these steps on the host. Running them inside the container is untested.

```sh
# arduino-cli
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=$HOME/.local/bin sh
export PATH=$HOME/.local/bin:$PATH

# USB permissions for Arduino devices (serial port + adb used for uploading)
echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="2341", MODE="0666", TAG+="uaccess"' | sudo tee /etc/udev/rules.d/60-arduino.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
sudo usermod -aG dialout "$USER"   # then log out and back in

# UNO Q core and libraries
arduino-cli core update-index
arduino-cli core install arduino:zephyr
arduino-cli lib install Arduino_RouterBridge "Adafruit AHTX0" "Adafruit PN532" "Grove - LCD RGB Backlight"
```

Plug in the UNO Q and wait about a minute for Linux to boot. `arduino-cli board list` should then show `/dev/ttyACM0` as **Arduino UNO Q**. Other teams' boards also appear as network ports, so always flash with `-p /dev/ttyACM0`.

## 2. Wiring

Do it with the UNO Q unplugged.

1. Set the Base Shield's VCC switch to **3.3 V** and stack the shield on the UNO Q.
2. Plug in the Grove cables:

   | Shield port | Module                                            |
   | ----------- | ------------------------------------------------- |
   | I2C (any)   | AHT20                                             |
   | I2C (any)   | LCD 16x2                                          |
   | UART        | NFC PN532. Must be in UART/HSU mode, its default. |
   | A0          | Light sensor                                      |
   | A1          | 2.5A current sensor                               |

3. Battery: switch the Waveshare's battery switch **ON**, then plug the LiPo into the PH2.0 socket.
   - **ON** LED lit means polarity is correct.
   - **Battery Warning** LED lit means it's reversed. Unplug it at once, and don't connect any USB charger to the Waveshare while that LED is on.
   - LEDs VD1–VD4 show the charge level.
4. Check the Waveshare's MPPT SET DIP switch, on the bottom: only **6 V** should be ON.
5. Solar, with the panel face down while wiring because it's live in light:
   - panel **+** → current sensor **IN+**
   - current sensor **IN−** → Waveshare **SOLAR IN +** (green screw terminal)
   - panel **−** → Waveshare **SOLAR IN −**

   Check the panel's polarity with the multimeter first: it should read positive from + to −.

6. Plug the UNO Q's USB-C into the laptop. Leave the Waveshare's USB OUT unconnected.

## 3. Flash and check

From the repository root:

```sh
arduino-cli compile -b arduino:zephyr:unoq --upload -p /dev/ttyACM0 firmware/station
arduino-cli monitor -p /dev/ttyACM0 --config baudrate=9600
```

Expected Monitor output, about once per second:

```text
PoopVolt: T=24.4C RH=48% light=633 Ipv=0mA up=30s pv_mv=266.5 nfc_reads=0
```

- **LCD:** line 1 shows temperature, humidity and light. Line 2 shows `Ipv …mA NFC`.
- **Phone:** turn NFC on, unlock the phone, and hold its back on the PN532 antenna. The tag text appears; NFC Tools → Read always shows it. `nfc_reads` goes up after each tap.
- **Current zero:** with the panel covered, `pv_mv` should sit near 266 mV. If yours differs, set `PV_ZERO_MV` in [`station.ino`](../firmware/station/station.ino) to your dark reading and flash again.

Optional, to check the readings reach the board's Linux side: deploy `firmware/station/linux/station_rx.py` as described in [UNO Q setup](uno-q-setup.md#station-sketch-firmwarestation). It should print one CSV line per second. The same page explains the performance index: calibrate once with the panel clean in clear sun, then the LCD shows `P…%`.

If something is missing, flash [`sensor_diag`](../firmware/sensor_diag/sensor_diag.ino) instead. It scans the I2C bus and reports each device.

## Troubleshooting

- **Monitor prints nothing:** `arduino-cli monitor` exits at once when its input is closed, which happens in scripts and AI agents. Run it as `sleep 30 | arduino-cli monitor …`. Only one program can hold `/dev/ttyACM0` at a time.
- **Upload fails with `adb: device … not found`:** the board isn't on USB, or it's still booting. Wait for `/dev/ttyACM0` to appear.
- **PN532 not found:** check that it's on the UART port. In I2C mode it would have to be on an I2C port, and the sketch expects UART.
- **No current reading in daylight:** check that the Solar Charge LED is lit. Below about 6 V the panel doesn't charge. Readings under about 200 mA are coarse, 4 mA per ADC step.
