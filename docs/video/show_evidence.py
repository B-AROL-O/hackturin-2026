"""Print the peer comparison of the SOLARMA replay for the demo video (#37).

Read-only: unlike ``poopvolt.report`` it writes nothing. Run from the
repository root with ``uv run python docs/video/show_evidence.py`` after
downloading the pinned data with ``poopvolt.solarma.fetch``.
"""

from pathlib import Path

from poopvolt import comparison, solarma

DATA = Path("data/solarma/raw")


def main() -> None:
    """Print one line per inverter, flagged inverters marked."""
    solarma.verify(DATA)
    records = solarma.load_details(DATA / "details.txt")
    result = comparison.compare(records)
    print("REPLAYED: SOLARMA open data, one plant, 2019")
    first, last = result.eval_days
    print(f"{len(records)} records, {len(result.results)} inverters")
    print(f"energy from {first} to {last}, each inverter against its peers\n")
    for device, r in result.results.items():
        if r.expected_kwh is None or r.deviation_pct is None:
            print(f"inverter {device:2}  no baseline")
            continue
        flag = "  <- inspect" if r.flagged else ""
        print(
            f"inverter {device:2}  observed {r.observed_kwh:4.0f} kWh"
            f"  expected {r.expected_kwh:4.0f} kWh"
            f"  {r.deviation_pct:+6.1f} %{flag}"
        )


if __name__ == "__main__":
    main()
