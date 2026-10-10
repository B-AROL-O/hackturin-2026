# Hardware connections (as built, 2026-10-10)

- Diagram ID: `pv-wiring`
- Level: Electrical wiring / prototype deployment
- Status: Implemented prototype, as reported by the bring-up author in
  [PR #49](https://github.com/B-AROL-O/hackturin-2026/pull/49); not independently
  retested for this diagram.
- Parent: [Physical deployment](architecture/deployment.md)
- Scope: USB-powered UNO Q, Base Shield, five connected Grove modules, and the
  separate solar charging path (panel, current sensor, Waveshare manager, LiPo).

The connection record in PR #49 reports verification with
[`sensor_diag`](../firmware/sensor_diag/sensor_diag.ino) and
[`station`](../firmware/station/station.ino). The team photo supplied on
2026-10-10 shows the assembly and a loose current sensor. Pin assignments and
the shield voltage setting below come from the bring-up record, since they
cannot all be read from the photo.

## Electrical schematic

![PoopVolt prototype electrical schematic](architecture/diagrams/pv-wiring.svg)

[Open SVG](architecture/diagrams/pv-wiring.svg) ·
[Download PDF](architecture/diagrams/pv-wiring.pdf) ·
[Editable KiCad schematic](../hardware/poopvolt.kicad_sch)

The single-sheet schematic shows individual electrical nets and numbered Grove
connector pins. `U1` represents the UNO Q with its stacked Base Shield, `J1`–`J4`
represent the shield's occupied Grove ports, and `U2`–`U5` represent the modules
at the other ends of their cables. These are interconnect symbols, not internal
IC schematics or a PCB design. USB data and internal processor wiring are outside
this sheet's scope.

Each line between a shield port and a module represents one cable conductor.
Same-name net labels are electrically connected across the sheet. `SCL` and
`SDA` are shared by the AHT20 and LCD; `+3V3` and `GND` reach all four modules.
UART uses separate `D0_RX` and `D1_TX` nets, with PN532 TX connected to MCU RX.

The light sensor's white conductor terminates at its unused connector contact.
That conductor carries A1, so `PV_ISENSE_A1` joins it with the current sensor
`U6` on the A1 port (`J5`); the light sensor does not drive it. Pin 2 of `U5`
and `U6` is modeled as a passive `NC / unused` contact. The UNO Q's remaining
headers are omitted.

The solar section (`PV1`, `U6` current path, `U7`, `BT1`) shares no conductor
with the UNO Q supply or Grove GND: `U6` is in series on the panel's positive
wire (`PV_POS` → IN+ … IN− → `PV_TO_CHARGER` → SOLAR IN +), and the LiPo plugs
into the Waveshare's PH2.0 socket. The Waveshare USB OUT is not connected.

## Grove cable pinout

<!-- markdownlint-disable MD013 -->

| Cable conductor | I2C: AHT20 and LCD         | UART: PN532                   | Analog: light sensor              |
| --------------- | -------------------------- | ----------------------------- | --------------------------------- |
| Pin 1, yellow   | PB10 / SCL to module SCL   | PB7 / D0 / MCU RX to PN532 TX | Module OUT to PA4 / A0            |
| Pin 2, white    | PB11 / SDA to module SDA   | PB6 / D1 / MCU TX to PN532 RX | Shield A1; unused by light sensor |
| Pin 3, red      | Shield 3.3 V to module VCC | Shield 3.3 V to module VCC    | Shield 3.3 V to module VCC        |
| Pin 4, black    | Common GND                 | Common GND                    | Common GND                        |

<!-- markdownlint-enable MD013 -->

Pin numbers follow the [Seeed Grove connector convention](https://wiki.seeedstudio.com/Grove_System/#interface-of-grove-modules),
not a left-to-right view of a connector. The UART labels are from the host's
point of view: the standard cable connects MCU RX to module TX and MCU TX to
module RX; no extra crossed jumper wiring is required.
The MCU header mapping is documented in the
[official UNO Q pinout](https://docs.arduino.cc/resources/pinouts/ABX00162-full-pinout.pdf).

## Main board

- **Arduino UNO Q (4 GB)** has two processors:
  - Linux MPU (Qualcomm QRB2210, Debian)
  - MCU (STM32U585, Zephyr, runs the sketches)
- The MPU and MCU are linked internally by UART at 115200 baud (MCU `LPUART1` ↔ Linux `/dev/ttyHS1`). This is the "Bridge", on the board, with no external wiring.
- **USB-C** connects to the laptop and provides 5 V power, ADB, and USB serial (`/dev/ttyACM0`).

## Seeed Grove Base Shield

Stacked on the UNO Q's UNO-format headers. **VCC switch set to 3.3 V**, so every Grove port supplies 3.3 V and GND.

| Shield port | UNO Q signal (MCU pin)                                      | Device                                                       | Bus / address                   | Status                                     |
| ----------- | ----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------- | ------------------------------------------ |
| I2C         | SDA (PB11), SCL (PB10): MCU I2C2, `Wire`                    | Grove AHT20 temperature/humidity                             | I2C 0x38                        | verified                                   |
| I2C         | same bus                                                    | Grove 16x2 LCD (monochrome, no RGB backlight chip)           | I2C 0x3E                        | verified                                   |
| UART        | D0 = MCU RX (PB7), D1 = MCU TX (PB6): MCU USART1, `Serial1` | Grove NFC (PN532), HSU mode, 115200 baud                     | UART                            | verified                                   |
| A0          | A0 (PA4), ADC1 ch 9                                         | Grove light sensor (phototransistor)                         | analog, 0–3.3 V                 | verified                                   |
| A1          | A1 (PA5), ADC1 ch 10                                        | Grove 2.5A DC current sensor (ACS70331), solar panel current | analog, 800 mV/A, zero 266.5 mV | zero verified; current under light pending |

Notes:

- The shield's I2C ports are wired in parallel, so it doesn't matter which I2C port each device uses.
- On the UART link, the PN532's TX goes to D0 (MCU RX) and its RX to D1 (MCU TX), using a standard Grove cable.
- The PN532 doesn't respond on I2C. That's expected, because it is in UART (HSU) mode.

## Not currently connected

- Arduino Modulino Movement (LSM6DSOX, I2C 0x6A): connects to the UNO Q's Qwiic connector (MCU `Wire1`). It was used for the first bring-up and is unplugged now.
- Arduino Media Carrier: not used.
- Camera (planned): an Android phone streaming over Wi-Fi to the Linux side. Wireless, no wiring.
- Waveshare Solar Power Manager USB OUT (5 V / 1 A): not connected; whether it can run the UNO Q is untested.
- HRS1358 charger and LM2596 ("HAS4966") step-down: not used. The step-down cannot make 5 V from a 3.7 V LiPo.

## Edit, check, and render

Open [`hardware/poopvolt.kicad_pro`](../hardware/poopvolt.kicad_pro) in KiCad,
then open its schematic. The project includes a local
[symbol library](../hardware/PoopVolt.kicad_sym) and
[library table](../hardware/sym-lib-table); no third-party part downloads are
required. Embedded definitions also keep the schematic self-contained.

The editable `.kicad_sch` is the canonical source for `pv-wiring`. After editing,
run this command from the repository root with KiCad 9 or newer and Python 3.12:

```sh
python3 hardware/export_schematic.py
```

The [export script](../hardware/export_schematic.py) runs KiCad's electrical
rules check, checks the exported netlist against the bring-up connections, and
then regenerates the SVG and PDF. It stops on violations or unexpected wiring.
For a KiCad installation outside `PATH`, pass `--kicad-cli /path/to/kicad-cli`.
When hardware changes intentionally, update the connection record and expected
net endpoints in the script together with the schematic and symbol library.

Validation with KiCad 10.0.7: electrical rules check and 15-net connectivity
check pass. Review the regenerated page visually before committing it. These
checks validate the modeled interconnect; they do not retest the physical board
or validate the internals of the purchased modules.

Keep this as-built snapshot separate from the proposed full-system deployment,
which includes future power and camera paths. See the
[architecture index](architecture/README.md).
