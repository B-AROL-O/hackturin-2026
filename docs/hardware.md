# PoopVolt hardware availability

- Status: Availability reported by the team; assembly and integration
  unverified.
- Updated: 2026-10-10.
- Source: Team-provided inventory in the project conversation.
- Scope: Hackathon prototype parts, substitutions, and their proposed roles.

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
| Grove NFC Reader (PN532)                    | Secured                                          | Shows the latest finding as NFC tag text (UART mode); wired and verified in PR #49.                    |
| 1000mAh LiPo battery with JST 2mm           | Secured                                          | Candidate prototype power component; runtime and connector compatibility unmeasured.                   |
| Solar Charger HRS1358                       | Secured                                          | Secured but not used: the Waveshare solar power manager is the charger in the as-built path.           |
| Mini Solar Panel R1123 (90x60)              | Secured                                          | Small-panel test fixture and candidate charging input; electrical specifications to verify.            |
| HAS4966 step-down converter                 | Secured                                          | Candidate power conversion component; supply design and settings to verify.                            |

<!-- markdownlint-enable MD013 -->

Names, versions, capacities, and dimensions above follow the team's inventory.
Availability does not establish a tested connection, model, or power budget.
See the [bill of materials](../hardware/bom.md) for quantities, status and approximate cost.

## Missing or unavailable

| Item                         | Reported status                                           | Prototype decision                                                                     |
| ---------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Breadboards                  | Completely out of stock                                   | Plan assembly around shield/connector connections; confirm needed cables and adapters. |
| Grove Thermal Imaging Camera | Unavailable                                               | Replace image acquisition with a phone RGB camera.                                     |
| Waveshare Solar Charger      | Found 2026-10-10 (Solar Power Manager, 5 V / 1 A version) | Now the charger in the as-built solar path; HRS1358 and LM2596 are no longer used.     |

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

## STL presentation concept

The team plans an STL design view in the three-minute pitch. It illustrates the
physical proposal and is distinct from this secured-parts inventory. Link the
actual STL filename/revision and explain its function when supplied. This PR
includes no STL artifact, assembled-device proof, or fabrication result.

## Integration work still required

- Verify UNO Q, Media Carrier, Base Shield, sensor, and LCD interfaces before
  specifying connections. Grove cables/adapters are not confirmed by this list.
- Build a breadboard-free connection plan from the available parts.
- Verify the panel, charger, battery, converter, and device supply requirements.
  The parts list does not establish that this assembly can power the UNO Q
  continuously or provide a measured battery runtime.
- Define a compatible current-measurement test. Current alone does not establish
  electrical power or energy; a voltage measurement is not identified here.
- Keep small-panel observations, phone simulation, and historical SOLARMA replay
  distinct. The kit does not establish full-scale plant instrumentation or
  complete string coverage.

See [deployment](architecture/deployment.md), [data plan](data-plan.md),
[architecture index](architecture/README.md), and [pitch](pitch-draft.md).
