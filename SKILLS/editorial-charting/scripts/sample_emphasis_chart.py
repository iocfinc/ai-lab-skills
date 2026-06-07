"""One-hue emphasis chart using the bundled shade ramp.

Run from this directory or pass an output path:
    python sample_emphasis_chart.py /tmp/editorial-emphasis.png
"""

from __future__ import annotations

from pathlib import Path
import sys


def _parse_nested_yaml_map(path: Path, section: str, child: str) -> dict[str, str]:
    values: dict[str, str] = {}
    in_section = False
    in_child = False
    section_indent = None
    child_indent = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip())
        stripped = raw_line.strip()

        if raw_line.startswith(f"{section}:"):
            in_section = True
            in_child = False
            section_indent = 0
            continue
        if in_section and indent == section_indent and not raw_line.startswith(f"{section}:"):
            break
        if in_section and stripped == f"{child}:":
            in_child = True
            child_indent = indent
            continue
        if in_child:
            if indent <= (child_indent or 0):
                break
            if ":" in stripped:
                key, value = stripped.split(":", 1)
                values[key.strip().strip('"')] = value.strip().strip('"')
    return values


def load_blue_ramp() -> dict[str, str]:
    color_yaml = Path(__file__).resolve().parents[1] / "references" / "color-system.yaml"
    return _parse_nested_yaml_map(color_yaml, "shade_ramps", "blue")


def main(output_path: str = "editorial-emphasis.png") -> None:
    import matplotlib.pyplot as plt

    ramp = load_blue_ramp()
    labels = ["Baseline", "Automation", "Review", "Publish", "Reuse"]
    values = [18, 27, 42, 55, 71]
    colors = [ramp["0.2"], ramp["0.2"], ramp["0.55"], ramp["0.85"], ramp["1.0"]]

    fig, ax = plt.subplots(figsize=(7.8, 4.4), dpi=160)
    bars = ax.barh(labels, values, color=colors, height=0.62)
    ax.invert_yaxis()
    ax.set_title("Reuse is where the workflow starts to compound", loc="left", fontsize=14, weight="bold")
    ax.set_xlabel("Share of work preserved for future runs")
    ax.set_xlim(0, 80)
    ax.grid(axis="x", color="#E5E7EB", linewidth=0.8)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.tick_params(axis="x", length=0, colors="#6B7280")

    for bar, value in zip(bars, values):
        ax.text(value + 1.5, bar.get_y() + bar.get_height() / 2, f"{value}%", va="center", fontsize=9)

    ax.annotate(
        "Main claim",
        xy=(values[-1], len(values) - 1),
        xytext=(61, len(values) - 1.75),
        arrowprops={"arrowstyle": "-", "color": "#334155", "linewidth": 1},
        fontsize=9,
        color="#334155",
    )
    fig.text(0.01, 0.01, "Source: Example operating metrics; values are illustrative.", fontsize=8, color="#6B7280")
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    fig.savefig(output_path, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "editorial-emphasis.png")
