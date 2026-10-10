# Hardware and prototype availability

- Status: Inventory availability reported by the team; USB prototype wiring
  reported tested in PR #49. Remaining power and camera integration unverified.
- Updated: 2026-10-10.
- Sources: Team-provided inventory and the connection record in PR #49.
- Scope: Hackathon prototype parts, substitutions, and their proposed roles.

The [prototype electrical schematic](../docs/hardware-connections.md) records
USB power and the four connected Grove modules reported in PR #49. The
inventory below records available parts and proposed roles; the schematic's
connection record tracks which parts are currently connected. Internal board
schematics and 3D-printable parts (STL) remain outside this implementation.

## Editable schematic and exports

Open [`poopvolt.kicad_pro`](poopvolt.kicad_pro) in KiCad 9 or newer. Its
[`poopvolt.kicad_sch`](poopvolt.kicad_sch) is the canonical electrical source.
The project includes a [local symbol library](PoopVolt.kicad_sym) and
[library table](sym-lib-table). Symbols describe module interfaces and Grove
connectors, not internal circuits or PCB footprints.

From the repository root, with Python 3.12 or newer:

```sh
python3 hardware/export_schematic.py
```

The [export script](export_schematic.py) runs KiCad ERC and checks the electrical
netlist against the bring-up record before replacing the published
[SVG](../docs/architecture/diagrams/pv-wiring.svg) and
[PDF](../docs/architecture/diagrams/pv-wiring.pdf). Pass
`--kicad-cli /path/to/kicad-cli` if needed. Edit the schematic directly in KiCad;
update the library and refresh embedded symbols if pin definitions change.
Visually review exports after editing. Detailed scope and editing instructions
are in the [connection record](../docs/hardware-connections.md).

## Secured hardware

<!-- markdownlint-disable MD013 -->

| Item                                        | Availability                                     | Proposed prototype role                                                                                |
| ------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| Arduino UNO Q 4GB + Media Carrier           | Secured                                          | Local acquisition, RGB inference, telemetry replay, and storage; carrier use and interfaces to verify. |
| Seeed Studio Base Shield                    | Secured; selected instead of the Grove shield v2 | Sensor/display connection approach; board compatibility and pin mapping to verify.                     |
| Jumper wires: M-M, F-F, M-F                 | Secured                                          | Assembly connections where compatible; connector requirements remain to check.                         |
| Grove AHT20 temperature and humidity sensor | Secured                                          | Environmental context; does not provide a panel thermal image.                                         |
| Grove Light Sensor (P) v1.1                 | Secured                                          | Relative light context; not an established calibrated irradiance measurement.                          |
| Grove 2.5A DC Current Sensor (ACS70331)     | Secured                                          | Current observations on a compatible small test circuit; range and integration to verify.              |
| Grove 16x2 LCD (White on Blue)              | Secured                                          | Proposed local status/findings display; connection and software to verify.                             |
| 1000mAh LiPo battery with JST 2mm           | Secured                                          | Candidate prototype power component; runtime and connector compatibility unmeasured.                   |
| Solar Charger HRS1358                       | Secured                                          | Candidate charging component selected in place of the unavailable Waveshare solar charger.             |
| Mini Solar Panel R1123 (90x60)              | Secured                                          | Small-panel test fixture and candidate charging input; electrical specifications to verify.            |
| HAS4966 step-down converter                 | Secured                                          | Candidate power conversion component; supply design and settings to verify.                            |

<!-- markdownlint-enable MD013 -->

Names, versions, capacities, and dimensions above follow the team's inventory.
Availability does not establish a tested connection, model, or power budget.

## Missing or unavailable

| Item                         | Reported status         | Prototype decision                                                                     |
| ---------------------------- | ----------------------- | -------------------------------------------------------------------------------------- |
| Breadboards                  | Completely out of stock | Plan assembly around shield/connector connections; confirm needed cables and adapters. |
| Grove Thermal Imaging Camera | Unavailable             | Replace image acquisition with a phone RGB camera.                                     |
| Waveshare Solar Charger      | Unavailable             | Use the secured HRS1358 as the charging candidate; integration remains to verify.      |

## Camera substitution

**The phone camera replaces the unavailable thermal camera for the current
prototype.** Phone model, transfer method, and capture/inference integration
remain undecided. The phone supplies visible RGB images of simulated dust or
droppings for contamination classification and image-region localization on a
declared panel/string. It is not added to the secured-parts list as a specified
hardware model.

There is no thermal acquisition or measured hotspot confirmation in the current
prototype scope. Hotspot risk can remain narrative background; thermal diagnosis
is deferred until an appropriate camera and aligned measurements are available.
Neither the AHT20 nor the light sensor replaces thermal imaging.

## Integration work still required

- Use the recorded USB prototype connections for the active Grove modules.
  Verify interfaces and cables for additional devices, including the unused
  Media Carrier, before extending the assembly.
- Build a breadboard-free connection plan from the available parts.
- **Supply blocker (checked 2026-10-10):** the "HAS4966" step-down module uses an
  LM2596HV (buck, about 1.5–2 V dropout), so it cannot make 5 V from the 3.0–4.2 V
  LiPo behind the CN3065-based HRS1358. Do not wire HRS1358 → LM2596 → UNO Q 5V.
  Options: power the UNO Q from USB-C and keep solar → current sensor → charger →
  LiPo as a measured subsystem, or use a 3.7→5 V boost converter rated ≥2–3 A.
- Verify the panel, charger, battery, converter, and device supply requirements.
  The parts list does not establish that this assembly can power the UNO Q
  continuously or provide a measured battery runtime.
- Define a compatible current-measurement test. Current alone does not establish
  electrical power or energy; a voltage measurement is not identified here.
- Keep small-panel observations, phone simulation, and historical SOLARMA replay
  distinct. The kit does not establish full-scale plant instrumentation or
  complete string coverage.

See the [proposed deployment](../docs/architecture/deployment.md),
[architecture index](../docs/architecture/README.md),
[firmware](../firmware/README.md), and
[data placeholder](../data/README.md). Thermal paths in the proposed system design
remain future work; the current prototype uses the phone camera described above.
