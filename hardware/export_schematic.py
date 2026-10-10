"""Check the PoopVolt interconnect and export its canonical KiCad schematic."""

import argparse
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMATIC = ROOT / "hardware" / "poopvolt.kicad_sch"
EXPORTS = ROOT / "docs" / "architecture" / "diagrams"

# These endpoints encode the bring-up connection record, not drawing coordinates.
EXPECTED_NETS = {
    "+5V_USB": {("P1", "VBUS"), ("U1", "USB_VBUS")},
    "+3V3": {("U1", "3V3")}
    | {(f"J{i}", "3") for i in range(1, 5)}
    | {(f"U{i}", "3") for i in range(2, 6)},
    "GND": {("P1", "GND"), ("U1", "USB_GND")}
    | {(f"J{i}", "4") for i in range(1, 5)}
    | {(f"U{i}", "4") for i in range(2, 6)},
    "SCL": {("U1", "SCL"), ("J1", "1"), ("J2", "1"), ("U2", "1"), ("U3", "1")},
    "SDA": {("U1", "SDA"), ("J1", "2"), ("J2", "2"), ("U2", "2"), ("U3", "2")},
    "D0_RX": {("U1", "D0"), ("J3", "1"), ("U4", "1")},
    "D1_TX": {("U1", "D1"), ("J3", "2"), ("U4", "2")},
    "LIGHT_A0": {("U1", "A0"), ("J4", "1"), ("U5", "1")},
    "SPARE_A1": {("U1", "A1"), ("J4", "2"), ("U5", "2")},
}


def check_connections(netlist):
    """Detect missing connections, crossed pins, and accidental power shorts."""
    nets = ET.parse(netlist).getroot().findall("./nets/net")
    actual = {
        net.attrib["name"].lstrip("/"): {
            (node.attrib["ref"], node.attrib["pin"]) for node in net.findall("node")
        }
        for net in nets
    }
    if actual != EXPECTED_NETS:
        differences = []
        for name in sorted(actual.keys() | EXPECTED_NETS.keys()):
            expected = EXPECTED_NETS.get(name, set())
            got = actual.get(name, set())
            if expected != got:
                differences.append(
                    f"{name}: missing={sorted(expected - got)}, "
                    f"extra={sorted(got - expected)}"
                )
        raise ValueError(
            "Schematic differs from bring-up wiring:\n" + "\n".join(differences)
        )
    pin_count = sum(len(pins) for pins in actual.values())
    print(f"Connectivity verified: {len(actual)} nets, {pin_count} pins.", flush=True)


def main():
    """Run electrical checks before publishing the schematic exports."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kicad-cli", help="Path to kicad-cli (KiCad 9 or newer)")
    args = parser.parse_args()
    cli = args.kicad_cli or shutil.which("kicad-cli")
    mac_cli = Path("/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli")
    if not cli and mac_cli.is_file():
        cli = str(mac_cli)
    if not cli:
        parser.error("Install KiCad or pass --kicad-cli /path/to/kicad-cli")

    def run(*arguments):
        subprocess.run(
            [cli, *map(str, arguments), str(SCHEMATIC)], check=True, cwd=ROOT
        )

    with tempfile.TemporaryDirectory(prefix="poopvolt-schematic-") as temporary:
        work = Path(temporary)
        run("sch", "erc", "--exit-code-violations", "--output", work / "erc.rpt")
        run(
            "sch",
            "export",
            "netlist",
            "--format",
            "kicadxml",
            "--output",
            work / "nets.xml",
        )
        check_connections(work / "nets.xml")
        run("sch", "export", "svg", "--output", str(work / "svg") + "/")
        run(
            "sch",
            "export",
            "pdf",
            "--exclude-pdf-property-popups",
            "--output",
            work / "pv-wiring.pdf",
        )
        svgs = list((work / "svg").glob("*.svg"))
        if len(svgs) != 1:
            raise ValueError(f"Expected one schematic sheet, found {len(svgs)} SVGs")
        EXPORTS.mkdir(parents=True, exist_ok=True)
        # KiCad emits trailing spaces in SVG attributes; normalize whitespace.
        svg = "\n".join(line.rstrip() for line in svgs[0].read_text().splitlines())
        (EXPORTS / "pv-wiring.svg").write_text(svg + "\n")
        shutil.copyfile(work / "pv-wiring.pdf", EXPORTS / "pv-wiring.pdf")
    print("Exported docs/architecture/diagrams/pv-wiring.{svg,pdf}")


if __name__ == "__main__":
    main()
