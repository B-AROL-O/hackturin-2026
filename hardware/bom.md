# Bill of materials (BOM)

- Status: Prototype as built on 2026-10-10, following
  [hardware connections](../docs/hardware-connections.md). Wiring is reported by
  the bring-up author in [PR #49](https://github.com/B-AROL-O/hackturin-2026/pull/49).
- Prices: single-unit list prices found on 2026-10-10 (see
  [price sources](#price-sources)); approximate, for the pitch only.
- Source of parts: secured by the team (the inventory does not record which
  parts came from a shared kit and which are owned).

## Parts in the prototype

<!-- markdownlint-disable MD013 -->

| Item                                              | Qty | Role                                                               | Status                                         | Approx. price |
| ------------------------------------------------- | --- | ------------------------------------------------------------------ | ---------------------------------------------- | ------------- |
| Arduino UNO Q 4GB                                 | 1   | Edge computer: Linux side (Python) and MCU (sketches)              | Wired (USB-C power)                            | 79            |
| Seeed Grove Base Shield V2.0                      | 1   | Grove connectors on the UNO headers; VCC switch set to 3.3 V       | Wired                                          | 4.7           |
| Seeed Grove AHT20 temperature and humidity sensor | 1   | Ambient temperature and humidity (I2C 0x38)                        | Wired, verified                                | 6.1           |
| Seeed Grove Light Sensor (P) v1.1                 | 1   | Relative light level (not calibrated irradiance), A0               | Wired, verified                                | 3.1           |
| Seeed Grove 2.5A DC Current Sensor (ACS70331)     | 1   | Solar panel current, in series on the panel's positive wire, A1    | Wired; zero verified, current under light TBD  | 9.3           |
| Seeed Grove 16x2 LCD (White on Blue)              | 1   | Local status display (I2C 0x3E)                                    | Wired, verified                                | 5.6           |
| Seeed Grove NFC (PN532)                           | 1   | Shows the latest finding as NFC tag text; UART mode, no card reads | Wired, verified                                | 16.5          |
| Waveshare Solar Power Manager (5V/1A version)     | 1   | Charges the LiPo from the panel (6 V input); USB OUT not connected | Wired                                          | 8 (estimate)  |
| Mini Solar Panel R1123 (90x60)                    | 1   | Small-panel test fixture                                           | Wired; open-circuit 4.55 V at dusk, rating TBD | 6 (estimate)  |
| LiPo battery 3.7 V, 1000 mAh, JST PH2.0           | 1   | Battery for the solar charge path                                  | Wired                                          | 5 (estimate)  |
| Grove cables                                      | 5   | One per Grove module on the shield                                 | Wired                                          | not priced    |
| Android phone camera                              | 1   | Visible-light (RGB) photos of the panel, over Wi-Fi to the UNO Q   | Planned; model and transfer method not decided | own, no cost  |

<!-- markdownlint-enable MD013 -->

**Approximate cost per device: about 145** (euro and dollar prices treated as
equal, excluding VAT and shipping, one unit each). The UNO Q is more than half of
it. This is a prototype cost from single-unit list prices, not a volume or
production cost. Prices marked "estimate" come from a comparable product or a
low-confidence listing. Phone, cables and jumper wires are not in the total.

## Secured but not used, or unavailable

<!-- markdownlint-disable MD013 -->

| Item                                 | Status                 | Substitution or note                                                       |
| ------------------------------------ | ---------------------- | -------------------------------------------------------------------------- |
| Grove Thermal Imaging Camera         | Unavailable            | Replaced by the phone RGB camera; no thermal measurement in this prototype |
| Breadboards                          | Out of stock           | Not needed: modules connect through the Base Shield with Grove cables      |
| Arduino UNO Media Carrier            | Secured, not used      | The UNO Q runs on its own with the Base Shield stacked on it               |
| Arduino Modulino Movement            | Used in first bring-up | Unplugged now; not part of the PoopVolt sensing                            |
| Solar Charger HRS1358                | Secured, not used      | The Waveshare manager is used instead                                      |
| Step-down converter HAS4966 (LM2596) | Secured, not used      | Cannot make 5 V from a 3.7 V LiPo                                          |
| Jumper wires (M-M, F-F, M-F)         | Secured, not used      | Grove cables replace them                                                  |

<!-- markdownlint-enable MD013 -->

The earlier [hardware availability](../docs/hardware.md) note listed the
Waveshare manager as unavailable. The as-built records show it is in use, so
this BOM follows them.

## Price sources

Prices were read from search results on 2026-10-10 and may have changed. Figures
are per unit, excluding VAT where the listing shows it.

- UNO Q 4GB: US list price $79 from 2026-07-06, per
  [Arduino](https://blog.arduino.cc/2026/06/26/a-heads-up-on-the-arduino-uno-q-board-pricing-straight-from-marcello-majonchi/).
- Base Shield V2.0: [RS Italy](https://it.rs-online.com/web/p/arduino-shield/1743233?gb=s),
  4.73 euro.
- AHT20: [Farnell Ireland](https://cpcireland.farnell.com/seeed-studio/101990644/sensor-board-aht20-temp-humid/dp/SC19985),
  6.06 euro.
- Light Sensor (P) v1.1: [Kiwi Electronics](https://www.kiwi-electronics.com/nl/grove-light-sensor-p-v1-1-2658),
  3.09 euro.
- Current sensor 2.5A: [Farnell Germany](https://de.farnell.com/en-DE/seeed-studio/101020652/sensor-board-arduino-raspberry/dp/4007735),
  9.29 euro.
- 16x2 LCD: [Farnell Belgium](https://be.farnell.com/en-BE/seeed-studio/104020111/lcd-board-arduino-raspberry-pi/dp/4007789),
  5.61 euro.
- NFC (PN532): [RobotShop US](https://robotshop.com/products/grove-nfc-module),
  16.50 dollars.
- Waveshare solar manager: the closest listing is the
  [6-24 V module at The Pi Hut](https://thepihut.com/collections/all/products/solar-power-management-module-for-6v-24v-solar-panel),
  8.70 pounds including VAT. It may not be the exact variant; confirm the model.
- Mini solar panel R1123: no listing found. A
  [comparable 6 V, 110x60 mm panel at Jameco](https://www.jameco.com/z/ALI-MVPWR-Jameco-ValuePro-Mini-Solar-Panel-Module-for-Cell-Phone-Battery-Chargers-6V-160mA-110x60mm_2282559.html)
  is 5.95 dollars.
- LiPo 1000 mAh: [Grobotronics](https://grobotronics.com/polymer-lithium-ion-battery-3.7v-1000mah-jst-ph.html)
  lists it; currency unclear, so about 5 is a rough estimate.

<!-- EOF -->
