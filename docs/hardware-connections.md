# Hardware connections (as built, 2026-10-10)

Input for drawing a schematic. Everything listed as verified was confirmed on the hardware with `firmware/sensor_diag` and `firmware/station`.

## Main board

- **Arduino UNO Q (4 GB)** has two processors:
  - Linux MPU (Qualcomm QRB2210, Debian)
  - MCU (STM32U585, Zephyr, runs the sketches)
- The MPU and MCU are linked internally by UART at 115200 baud (MCU `LPUART1` ↔ Linux `/dev/ttyHS1`). This is the "Bridge", on the board, with no external wiring.
- **USB-C** connects to the laptop and provides 5 V power, ADB, and USB serial (`/dev/ttyACM0`).

## Seeed Grove Base Shield

Stacked on the UNO Q's UNO-format headers. **VCC switch set to 3.3 V**, so every Grove port supplies 3.3 V and GND.

| Shield port | UNO Q signal (MCU pin) | Device | Bus / address | Status |
|---|---|---|---|---|
| I2C | SDA (PB11), SCL (PB10): MCU I2C2, `Wire` | Grove AHT20 temperature/humidity | I2C 0x38 | verified |
| I2C | same bus | Grove 16x2 LCD (monochrome, no RGB backlight chip) | I2C 0x3E | verified |
| UART | D0 = MCU RX (PB7), D1 = MCU TX (PB6): MCU USART1, `Serial1` | Grove NFC (PN532), HSU mode, 115200 baud | UART | verified |
| A0 | A0 (PA4), ADC1 ch 9 | Grove light sensor (phototransistor) | analog, 0–3.3 V | verified |

Notes:
- The shield's I2C ports are wired in parallel, so it doesn't matter which I2C port each device uses.
- On the UART link, the PN532's TX goes to D0 (MCU RX) and its RX to D1 (MCU TX). The Grove cable does the crossover.
- The PN532 doesn't respond on I2C. That's expected, because it is in UART (HSU) mode.

## Not currently connected

- Arduino Modulino Movement (LSM6DSOX, I2C 0x6A): connects to the UNO Q's Qwiic connector (MCU `Wire1`). It was used for the first bring-up and is unplugged now.
- Arduino Media Carrier: not used.
- Camera (planned): an Android phone streaming over Wi-Fi to the Linux side. Wireless, no wiring.
