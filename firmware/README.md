# Firmware

Arduino UNO Q MCU sketches introduced in the Arduino bring-up, PR #49:

- [`sensor_diag`](sensor_diag/sensor_diag.ino): probes and reads the Grove devices.
- [`station`](station/station.ino): reads temperature, humidity, and light; shows
  readings on the LCD and exposes them as PN532 NFC tag text over `Serial1`.
- [`imu_bridge`](imu_bridge/imu_bridge.ino): earlier Modulino Movement bring-up,
  with a [Linux receiver](imu_bridge/linux/imu_rx.py). The IMU is unplugged from
  the current prototype.

See [UNO Q setup](../docs/uno-q-setup.md) for build/upload commands and the
[hardware connection record](../docs/hardware-connections.md) for the current
wiring and editable KiCad schematic. Edge inference and the full PoopVolt
application remain proposed in the [architecture index](../docs/architecture/README.md).
