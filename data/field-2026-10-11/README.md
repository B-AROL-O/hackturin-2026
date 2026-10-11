# Field test 2026-10-11 (UNO Q station, mini panel)

These are real measurements, not synthetic. They come from `station_rx.py --csv` on the UNO Q, with one row per second. The columns are described in [UNO Q setup](../../docs/uno-q-setup.md#station-sketch-firmwarestation). Times are UTC, corrected with `--now`. The site is Turin, with the panel flat.

| File                 | UTC         | Setup                                                                                                                    | Panel current                                                    |
| -------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| `field_nocharge.csv` | 09:45–09:48 | Outdoors, full sun, panel → current sensor → Waveshare (Solar Charge LED off)                                            | none (`pv_mv` 256–268)                                           |
| `field_outdoor.csv`  | 09:55–10:37 | Outdoors. Includes the short-circuit test (SOLAR IN+ and − jumpered) and the original wiring; board restarted in between | at noise level: max 18 mA, `pv_mv` 248–281, temperature 21–43 °C |
| `field_window.csv`   | 10:58–10:59 | Indoors by a window, original wiring                                                                                     | at noise level: max 13 mA                                        |

Before 10:17 UTC the firmware reported negative currents. After that, it reports currents below 10 mA as 0.

What the data shows: no usable panel current. The current sensor's output varies by about ±15 mV with temperature, so readings up to about 18 mA cannot be told apart from that drift. A calibration run by the window (`field_window.csv`) produced a baseline from these noise-level readings, and it was deleted. The data is useful as a record of the sensor's noise and drift, not of panel performance.
