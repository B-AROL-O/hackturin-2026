"""Prepare brand-aligned art and faithful copies of required video media."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from pathlib import Path

ASSETS = Path(__file__).resolve().parent
ROOT = ASSETS.parents[2]
BLUE = "#0D2D44"
YELLOW = "#F5C329"
WHITE = "#FFFFFF"
LIGHT = "#F4F5F7"
GREY = "#52606D"
RULE = "#D8DEE4"


def document(width: int, height: int, title: str, body: str) -> str:
    """Wrap illustrative art; do not present it as a photograph or logo."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        'role="img" aria-labelledby="title desc">\n'
        f'<title id="title">{title}</title>\n'
        '<desc id="desc">Original illustrative PoopVolt pitch artwork, '
        "not a photograph, measurement, detection result, or official logo.</desc>\n"
        f"{body}\n</svg>\n"
    )


def panel() -> str:
    """Shared panel geometry with an independently revealable deposit layer."""
    parts = [
        (
            f'<g id="panel-frame"><rect x="172" y="127" width="856" '
            f'height="506" rx="12" fill="{RULE}"/>'
            f'<rect x="180" y="135" width="840" height="490" rx="7" '
            f'fill="{BLUE}"/></g>'
        ),
        '<g id="panel-cells">',
    ]
    for row in range(4):
        for col in range(6):
            x = 198 + col * 135
            y = 153 + row * 115
            parts.append(
                f'<rect x="{x}" y="{y}" width="129" height="109" rx="3" fill="{GREY}"/>'
            )
            for bar in range(1, 4):
                parts.append(
                    f'<path d="M{x + bar * 32} {y + 5}v99" '
                    f'stroke="{RULE}" stroke-width="1.2" opacity="0.4"/>'
                )
    parts.extend(
        [
            '</g><g id="deposit" transform="translate(743 292)">',
            (
                f'<path d="M-31 -7C-27 -28 -8 -25 1 -13C11 -27 29 -22 '
                "29 -9C49 -1 39 16 23 15C15 31 -9 28 -15 14"
                f'C-43 20 -50 1 -31 -7Z" fill="{WHITE}"/>'
            ),
            (
                f'<ellipse cx="0" cy="1" rx="16" ry="10" fill="{RULE}"/>'
                f'<circle cx="42" cy="27" r="5" fill="{WHITE}"/></g>'
            ),
        ]
    )
    return "\n".join(parts)


def pigeon() -> str:
    """Separate narrative illustration; never a replacement official mark."""
    return (
        f'<g id="pigeon" fill="{BLUE}">'
        '<path d="M97 205L52 242L123 230Z"/>'
        '<ellipse cx="157" cy="197" rx="75" ry="52"/>'
        '<path d="M190 174C194 152 190 126 207 112L240 123L228 164L216 190Z"/>'
        '<circle cx="226" cy="118" r="28"/>'
        f'<path d="M250 115L277 126L249 133Z" fill="{YELLOW}"/>'
        f'<circle cx="235" cy="111" r="4" fill="{WHITE}"/>'
        f'<path d="M150 241L148 267M192 240L194 267M138 269L164 269'
        f'M182 269L208 269" stroke="{BLUE}" stroke-width="5" fill="none"/>'
        f'<path d="M119 178Q177 215 207 169" fill="none" stroke="{WHITE}" '
        'stroke-width="4"/></g>'
    )


def installation() -> str:
    """Conceptual older plant setting; no measured output or power claim."""
    return (
        f'<rect width="1600" height="900" fill="{WHITE}"/>'
        f'<path d="M0 680Q400 590 780 677T1600 650V900H0Z" fill="{LIGHT}"/>'
        f'<circle cx="1260" cy="180" r="57" fill="{YELLOW}"/>'
        f'<path d="M990 430L1120 330L1280 430V681H990Z" fill="{LIGHT}"/>'
        f'<path d="M968 432L1120 315L1297 432" fill="none" stroke="{BLUE}" '
        'stroke-width="12" stroke-linejoin="round"/>'
        f'<rect x="1152" y="520" width="77" height="161" fill="{BLUE}"/>'
        f'<rect x="1024" y="483" width="79" height="71" fill="{RULE}"/>'
        f'<g id="installation-panel" transform="translate(157 339) scale(.65)">'
        f'{panel()}</g><g id="owner" transform="translate(1360 570)">'
        f'<circle cx="0" cy="-60" r="24" fill="{BLUE}"/>'
        f'<path d="M-23 -22Q0 -37 23 -22L33 64H-33Z" fill="{GREY}"/>'
        f'<path d="M-18 59L-24 137M18 59L24 137" stroke="{BLUE}" '
        'stroke-width="15" stroke-linecap="round"/>'
        f'<path d="M-21 -3L-44 50M22 -3L50 20" stroke="{GREY}" '
        'stroke-width="14" stroke-linecap="round"/></g>'
    )


def main() -> None:
    """Generate art, copy supplied media without alteration, and record hashes."""
    converter = shutil.which("rsvg-convert")
    if not converter:
        raise SystemExit("Install librsvg (rsvg-convert) before rebuilding assets.")
    art = {
        "panel-rgb": (1200, 760, "Illustrative panel and deposit", panel()),
        "pigeon": (320, 320, "Separate illustrative pigeon", pigeon()),
        "plant-owner": (
            1600,
            900,
            "Illustrative plant and owner; not a prototype photograph",
            installation(),
        ),
    }
    records = []
    for name, (width, height, title, body) in art.items():
        if name == "panel-rgb":
            body = f'<rect width="1200" height="760" fill="{WHITE}"/>' + body
        svg_path = ASSETS / f"{name}.svg"
        svg_path.write_text(document(width, height, title, body), encoding="utf-8")
        subprocess.run(
            [converter, "--output", str(ASSETS / f"{name}.png"), str(svg_path)],
            check=True,
        )
        for ext in ["svg", "png"]:
            records.append(
                {
                    "path": f"{name}.{ext}",
                    "source": "presentation/video/assets/build_illustrations.py",
                    "status": "illustrative",
                    "creator": "Original artwork authored for PoopVolt with Codex",
                    "rights": "Repository MIT license; not official brand artwork",
                    "modifications": "Original SVG" if ext == "svg" else "PNG export",
                }
            )
    copies = [
        ("assets/brand/Logo_PoopVolt.png", "Logo_PoopVolt.png", "brand_original"),
        (
            "docs/video/assets/prototype-bench-01.jpg",
            "prototype-bench-01.jpg",
            "prototype_photo",
        ),
        (
            "docs/video/assets/prototype-bench-02.jpg",
            "prototype-bench-02.jpg",
            "prototype_photo",
        ),
        (
            "docs/video/assets/prototype-outdoor.jpg",
            "prototype-outdoor.jpg",
            "prototype_photo",
        ),
        (
            "docs/architecture/diagrams/pv-wiring.svg",
            "pv-wiring.svg",
            "reported_prototype_wiring",
        ),
        (
            "docs/images/comparison-inverter-1-replayed.svg",
            "comparison-inverter-1-replayed.svg",
            "historical_replay",
        ),
    ]
    for source, name, status in copies:
        shutil.copyfile(ROOT / source, ASSETS / name)
        revision = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", source], cwd=ROOT, text=True
        ).strip()
        rights = "Repository material; retain its source and license notices"
        creator = "Repository source; see canonical document"
        if status == "brand_original":
            rights = "Team-supplied brand asset; creator and brand permissions pending in assets/brand/README.md"
            creator = "Supplied by GitHub user fedenebu; creator unconfirmed"
        elif status == "prototype_photo":
            rights = "Existing repository prototype photo; author and explicit usage permission not recorded"
            creator = "Repository-supplied prototype photograph; author unrecorded"
        record = {
            "path": name,
            "source": source,
            "revision": revision,
            "upstream_url": f"https://github.com/B-AROL-O/hackturin-2026/blob/{revision}/{source}",
            "status": status,
            "creator": creator,
            "rights": rights,
            "modifications": "None; byte-identical local copy",
        }
        records.append(record)
        if name.endswith(".svg"):
            png = ASSETS / name.replace(".svg", ".png")
            subprocess.run(
                [
                    converter,
                    "--width",
                    "2400",
                    "--output",
                    str(png),
                    str(ASSETS / name),
                ],
                check=True,
            )
            records.append(
                {**record, "path": png.name, "modifications": "Faithful PNG export"}
            )
    for record in records:
        record["sha256"] = hashlib.sha256(
            (ASSETS / record["path"]).read_bytes()
        ).hexdigest()
    manifest = {
        "schemaVersion": 1,
        "preparedOn": "2026-10-11",
        "generator": "build_illustrations.py",
        "rasterizer": subprocess.check_output(
            [converter, "--version"], text=True
        ).splitlines()[0],
        "brandGuidelines": "brand-guidelines.md",
        "panelGeometry": {
            "viewBox": "0 0 1200 760",
            "evidenceAnchor": {"x": 743, "y": 292},
        },
        "assets": records,
    }
    (ASSETS / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Prepared {len(records)} brand-aligned and source-faithful video assets.")


if __name__ == "__main__":
    main()
