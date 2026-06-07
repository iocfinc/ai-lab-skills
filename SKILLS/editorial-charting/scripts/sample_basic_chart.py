"""Basic editorial chart using the bundled color-system YAML.

Run from this directory or pass an output path:
    python sample_basic_chart.py /tmp/editorial-basic.png
"""

from __future__ import annotations

from pathlib import Path
import sys


def _parse_simple_yaml_map(path: Path, section: str) -> dict[str, str]:
    """Parse flat key: "#HEX" pairs from a known section of the skill YAML."""
    values: dict[str, str] = {}
    in_section = False
    base_indent = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith(f"{section}:"):
            in_section = True
            base_indent = None
            continue
        if in_section:
            indent = len(raw_line) - len(raw_line.lstrip())
            if base_indent is None and indent > 0:
                base_indent = indent
            if indent == 0:
                break
            if base_indent is not None and indent == base_indent and ":" in raw_line:
                key, value = raw_line.strip().split(":", 1)
                values[key.strip().strip('"')] = value.strip().strip('"')
    return values


def load_palette() -> dict[str, str]:
    color_yaml = Path(__file__).resolve().parents[1] / "references" / "color-system.yaml"
    return _parse_simple_yaml_map(color_yaml, "base_palette")


def main(output_path: str = "editorial-basic.png") -> None:
    import matplotlib.pyplot as plt

    palette = load_palette()
    labels = ["Research", "Prototype", "Pilot", "Launch"]
    values = [34, 51, 63, 78]

    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=160)
    ax.bar(labels, values, color=palette["blue"], width=0.58)
    ax.set_title("Launch readiness rises after the pilot", loc="left", fontsize=14, weight="bold")
    ax.set_ylabel("Readiness score")
    ax.set_ylim(0, 90)
    ax.grid(axis="y", color="#E5E7EB", linewidth=0.8)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0, colors="#6B7280")
    ax.tick_params(axis="x", length=0)

    for index, value in enumerate(values):
        ax.text(index, value + 2, f"{value}", ha="center", va="bottom", fontsize=9, color="#1F2937")

    fig.text(0.01, 0.01, "Source: Example project tracker", fontsize=8, color="#6B7280")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(output_path, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "editorial-basic.png")
