"""Build the editorial-charting contact sheet HTML.

The generated file is deliberately standalone: no external CSS, JavaScript, or
runtime data fetches. It uses small toy-dataset-style values inspired by
scikit-learn examples and Matplotlib gallery chart forms.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "assets" / "contact-sheet.html"


@dataclass(frozen=True)
class Card:
    number: str
    title: str
    claim: str
    question: str
    use_when: str
    sample_data: str
    reference: str
    chart_svg: str


def parse_flat_yaml_section(path: Path, section: str) -> dict[str, str]:
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
            if indent == 0:
                break
            if base_indent is None and indent > 0:
                base_indent = indent
            if indent == base_indent and ":" in raw_line:
                key, value = raw_line.strip().split(":", 1)
                values[key.strip().strip('"')] = value.strip().strip('"')
    return values


def parse_ramp(path: Path, hue: str) -> dict[str, str]:
    values: dict[str, str] = {}
    in_ramps = False
    in_hue = False
    hue_indent = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        stripped = raw_line.strip()
        indent = len(raw_line) - len(raw_line.lstrip())
        if raw_line.startswith("shade_ramps:"):
            in_ramps = True
            continue
        if in_ramps and stripped == f"{hue}:":
            in_hue = True
            hue_indent = indent
            continue
        if in_hue:
            if indent <= (hue_indent or 0):
                break
            if ":" in stripped:
                key, value = stripped.split(":", 1)
                values[key.strip().strip('"')] = value.strip().strip('"')
    return values


def svg_bar(values: list[tuple[str, float]], colors: list[str]) -> str:
    max_value = max(value for _, value in values)
    rows = []
    for i, (label, value) in enumerate(values):
        y = 18 + i * 31
        width = 136 * value / max_value
        rows.append(f'<text x="8" y="{y + 12}" class="tiny">{escape(label)}</text>')
        rows.append(f'<rect x="70" y="{y}" width="{width:.1f}" height="16" fill="{colors[i]}"/>')
        rows.append(f'<text x="222" y="{y + 12}" text-anchor="end" class="tiny strong">{value:g}</text>')
    return f'<svg viewBox="0 0 240 128" role="img" aria-label="Horizontal bar chart">{"".join(rows)}</svg>'


def svg_line(values: list[float], color: str) -> str:
    max_value = max(values)
    min_value = min(values)
    points = []
    for i, value in enumerate(values):
        x = 14 + i * (210 / (len(values) - 1))
        y = 106 - ((value - min_value) / (max_value - min_value)) * 82
        points.append((x, y))
    grid = "".join(f'<line x1="12" x2="226" y1="{y}" y2="{y}" class="gridline"/>' for y in [28, 56, 84, 112])
    point_string = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    end_x, end_y = points[-1]
    return f'<svg viewBox="0 0 240 128" role="img" aria-label="Line chart">{grid}<polyline points="{point_string}" fill="none" stroke="{color}" stroke-width="4"/><circle cx="{end_x:.1f}" cy="{end_y:.1f}" r="4" fill="{color}"/><text x="{end_x - 4:.1f}" y="{end_y - 8:.1f}" text-anchor="end" class="tiny strong">64</text></svg>'


def svg_histogram(values: list[float], muted: str, accent: str) -> str:
    max_value = max(values)
    bars = []
    for i, value in enumerate(values):
        height = 84 * value / max_value
        x = 18 + i * 29
        y = 106 - height
        color = accent if i == 5 else muted
        bars.append(f'<rect x="{x}" y="{y:.1f}" width="22" height="{height:.1f}" fill="{color}"/>')
    labels = '<text x="18" y="120" class="tiny">short</text><text x="104" y="120" text-anchor="middle" class="tiny">median</text><text x="214" y="120" text-anchor="end" class="tiny">long</text>'
    marker = '<line x1="116" x2="116" y1="25" y2="106" class="callout"/><text x="122" y="34" class="tiny strong">typical</text>'
    return f'<svg viewBox="0 0 240 128" role="img" aria-label="Histogram"><line x1="12" x2="226" y1="106" y2="106" class="axis"/>{"".join(bars)}{marker}{labels}</svg>'


def svg_stacked(parts: list[tuple[str, float, str]]) -> str:
    x = 18
    bars = []
    labels = []
    total = sum(value for _, value, _ in parts)
    for label, value, color in parts:
        width = 196 * value / total
        bars.append(f'<rect x="{x:.1f}" y="44" width="{width:.1f}" height="32" fill="{color}"/>')
        percent = round(value / total * 100)
        labels.append(f'<text x="{x + width / 2:.1f}" y="64" text-anchor="middle" class="tiny invert">{escape(label)} {percent}%</text>')
        x += width
    endpoints = '<text x="18" y="96" class="tiny">0%</text><text x="214" y="96" text-anchor="end" class="tiny">100%</text>'
    return f'<svg viewBox="0 0 240 128" role="img" aria-label="Stacked bar chart">{"".join(bars + labels)}{endpoints}</svg>'


def svg_scatter(points: list[tuple[float, float]], color: str, muted: str) -> str:
    circles = []
    min_x = min(x for x, _ in points)
    max_x = max(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_y = max(y for _, y in points)
    x0, x1 = 26, 214
    y0, y1 = 104, 20
    for i, (x_value, y_value) in enumerate(points):
        x = x0 + ((x_value - min_x) / (max_x - min_x)) * (x1 - x0)
        y = y0 - ((y_value - min_y) / (max_y - min_y)) * (y0 - y1)
        fill = color if i in {3, 8} else muted
        radius = 4.5 if i in {3, 8} else 3
        circles.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{fill}"/>')
    trend = '<path d="M32 94 C78 78, 118 53, 208 26" class="trendline"/>'
    return f'<svg viewBox="0 0 240 128" role="img" aria-label="Scatterplot"><line x1="18" x2="222" y1="108" y2="108" class="axis"/><line x1="18" x2="18" y1="18" y2="108" class="axis"/>{trend}{"".join(circles)}</svg>'


def svg_annotated(values: list[float], ramp: dict[str, str]) -> str:
    colors = [ramp["0.2"], ramp["0.2"], ramp["0.55"], ramp["0.85"], ramp["1.0"]]
    max_value = max(values)
    bars = []
    for i, value in enumerate(values):
        height = 78 * value / max_value
        x = 20 + i * 39
        y = 104 - height
        bars.append(f'<rect x="{x}" y="{y:.1f}" width="24" height="{height:.1f}" fill="{colors[i]}"/>')
    callout = '<defs><marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="#334155"/></marker></defs><text x="126" y="22" class="tiny strong">Peak reuse</text><path d="M170 25 L188 30" class="callout arrow"/>'
    return f'<svg viewBox="0 0 240 128" role="img" aria-label="Annotated bar chart"><line x1="14" x2="222" y1="104" y2="104" class="axis"/>{"".join(bars)}{callout}</svg>'


def build_cards(ramp: dict[str, str], palette: dict[str, str]) -> list[Card]:
    return [
        Card(
            "01",
            "Ranked Comparison",
            "Virginica leads on length",
            "Which category leads?",
            "Use for peer benchmarks, sorted categories, and single-winner comparisons.",
            "Iris-like mean sepal length by species.",
            "references/chart-patterns.yaml#comparison_ranked",
            svg_bar([("setosa", 5.0), ("versicolor", 5.9), ("virginica", 6.6)], [ramp["0.2"], ramp["0.55"], ramp["1.0"]]),
        ),
        Card(
            "02",
            "Trend",
            "Momentum accelerates late",
            "What changed over time?",
            "Use for direction, pace, inflection points, or forecast context.",
            "Toy quarterly metric series.",
            "references/chart-patterns.yaml#trend",
            svg_line([31, 35, 34, 42, 48, 51, 59, 64], palette["blue"]),
        ),
        Card(
            "03",
            "Distribution",
            "Most values cluster long",
            "How spread out are values?",
            "Use for skew, outliers, ranges, and typical values.",
            "Iris-like petal length bins.",
            "references/chart-patterns.yaml#distribution",
            svg_histogram([8, 18, 22, 14, 27, 31, 20], ramp["0.2"], ramp["1.0"]),
        ),
        Card(
            "04",
            "Composition",
            "Low digits are the largest group",
            "What makes up the whole?",
            "Use for stable parts-of-whole with a small number of groups.",
            "Digits-like classes grouped into low, middle, and high digits.",
            "references/chart-patterns.yaml#composition",
            svg_stacked([("0-3", 720, palette["cyan"]), ("4-6", 544, palette["orange"]), ("7-9", 533, palette["violet"])]),
        ),
        Card(
            "05",
            "Relationship",
            "Bigger sepals track bigger petals",
            "Do two measures move together?",
            "Use for association, clusters, and outliers.",
            "Iris-like sepal and petal measurements.",
            "references/chart-patterns.yaml#relationship",
            svg_scatter([(1.0, 1.2), (1.4, 1.3), (1.7, 2.1), (2.5, 3.7), (3.1, 3.4), (3.4, 4.2), (4.2, 4.6), (4.8, 5.1), (5.3, 6.0), (5.8, 5.6)], palette["magenta"], "#D1D5DB"),
        ),
        Card(
            "06",
            "Annotation Story",
            "Reuse is where work compounds",
            "What is the one point to notice?",
            "Use for a callout attached to a threshold, moment, or selected value.",
            "Toy workflow metric with highlighted reuse step.",
            "references/chart-patterns.yaml#annotation_story",
            svg_annotated([18, 27, 42, 55, 71], ramp),
        ),
    ]


def render_html(cards: list[Card]) -> str:
    card_html = "\n".join(render_card(card) for card in cards)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Editorial Charting Contact Sheet</title>
  <style>
    :root {{
      --ink: #111827;
      --muted: #6B7280;
      --line: #CBD5E1;
      --grid: #E5E7EB;
      --panel: #F8FAFC;
      --blue: #0B5FFF;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: white;
      color: var(--ink);
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.25;
    }}
    main {{ max-width: 1120px; margin: 0 auto; padding: 24px; }}
    header {{
      border-top: 2px solid var(--ink);
      border-bottom: 1px solid var(--ink);
      display: grid;
      grid-template-columns: 96px 1fr;
      gap: 20px;
      align-items: stretch;
      margin-bottom: 18px;
    }}
    .mark {{
      background: var(--ink);
      color: white;
      display: grid;
      place-items: center;
      font-size: 34px;
      font-weight: 800;
    }}
    h1 {{ margin: 14px 0 6px; font-size: 30px; letter-spacing: 0; }}
    .subhead {{ margin: 0 18px 14px 0; color: var(--muted); max-width: 760px; }}
    .steps {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin: 0 0 18px;
    }}
    .step {{
      border: 1px solid var(--line);
      padding: 9px;
      min-height: 62px;
    }}
    .step b {{ display: block; font-size: 13px; margin-bottom: 5px; }}
    .step span {{ color: var(--muted); font-size: 12px; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
    }}
    article {{
      border: 1px solid var(--line);
      min-height: 312px;
      display: flex;
      flex-direction: column;
      break-inside: avoid;
    }}
    .card-head {{
      display: grid;
      grid-template-columns: 48px 1fr;
      border-bottom: 1px solid var(--line);
      min-height: 52px;
    }}
    .num {{
      background: var(--ink);
      color: white;
      display: grid;
      place-items: center;
      font-weight: 800;
    }}
    h2 {{ font-size: 16px; margin: 8px 10px 2px; }}
    .question {{ margin: 0 10px 8px; color: var(--blue); font-size: 12px; font-weight: 700; }}
    .chart {{ padding: 9px 10px 6px; border-bottom: 1px solid var(--line); background: var(--panel); }}
    .chart-claim {{ display: block; margin: 0 0 4px; font-size: 11px; font-weight: 700; color: var(--ink); }}
    svg {{ width: 100%; height: auto; display: block; }}
    .tiny {{ font-size: 9px; fill: var(--muted); font-family: Arial, Helvetica, sans-serif; }}
    .strong {{ fill: var(--ink); font-weight: 700; }}
    .invert {{ fill: white; font-weight: 700; }}
    .gridline {{ stroke: var(--grid); stroke-width: 1; }}
    .axis {{ stroke: #9CA3AF; stroke-width: 1; }}
    .callout {{ stroke: #334155; stroke-width: 1.5; fill: none; }}
    .arrow {{ marker-end: url(#arrow); }}
    .trendline {{ stroke: #94A3B8; stroke-width: 1.4; fill: none; stroke-dasharray: 3 3; }}
    dl {{ margin: 0; padding: 9px 11px 11px; display: grid; gap: 6px; }}
    dt {{ font-size: 10px; color: var(--muted); text-transform: uppercase; letter-spacing: .06em; }}
    dd {{ margin: 2px 0 0; font-size: 12px; }}
    footer {{
      margin-top: 16px;
      border-top: 1px solid var(--line);
      padding-top: 10px;
      color: var(--muted);
      font-size: 11px;
    }}
    @page {{ size: A4 landscape; margin: 12mm; }}
    @media print {{
      main {{ max-width: none; padding: 0; }}
      body {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
      header {{ margin-bottom: 10px; }}
      h1 {{ font-size: 24px; margin-top: 10px; }}
      .subhead {{ font-size: 12px; margin-bottom: 10px; }}
      .steps {{ gap: 6px; margin-bottom: 10px; }}
      .step {{ min-height: 48px; padding: 6px 8px; }}
      .step span {{ font-size: 10px; }}
      .grid {{ gap: 8px; }}
      article {{ min-height: 238px; }}
      .chart {{ padding: 6px 8px 4px; }}
      dl {{ gap: 4px; padding: 7px 9px 8px; }}
      dt {{ font-size: 8px; }}
      dd {{ font-size: 10px; }}
      footer {{ font-size: 9px; margin-top: 8px; padding-top: 6px; }}
    }}
    @media (max-width: 860px) {{
      main {{ padding: 18px; }}
      header {{ grid-template-columns: 72px 1fr; }}
      .steps, .grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
<main>
  <header>
    <div class="mark">EC</div>
    <div>
      <h1>Editorial Charting Contact Sheet</h1>
      <p class="subhead">A quick visual inventory for humans and agents. Pick the reader question, load the matching pattern, then build with the color tokens and sample scripts.</p>
    </div>
  </header>
  <section class="steps" aria-label="Quick start">
    <div class="step"><b>1. Pick the question</b><span>Comparison, trend, distribution, composition, relationship, or callout.</span></div>
    <div class="step"><b>2. Load the pattern</b><span>Use <code>references/chart-patterns.yaml</code>.</span></div>
    <div class="step"><b>3. Choose emphasis</b><span>Use one hue plus shades; categorical tokens only for stable groups.</span></div>
    <div class="step"><b>4. Build or brief</b><span>Use the Python samples or return the skill output contract.</span></div>
  </section>
  <section class="grid" aria-label="Chart capabilities">
{card_html}
  </section>
  <footer>
    Demo data: tiny toy-dataset-style values inspired by scikit-learn bundled datasets and Matplotlib gallery chart forms. This palette is Bloomberg-inspired, not an official Bloomberg style guide.
  </footer>
</main>
</body>
</html>
"""


def render_card(card: Card) -> str:
    return f"""    <article>
      <div class="card-head">
        <div class="num">{escape(card.number)}</div>
        <div>
          <h2>{escape(card.title)}</h2>
          <p class="question">{escape(card.question)}</p>
        </div>
      </div>
      <div class="chart"><span class="chart-claim">{escape(card.claim)}</span>{card.chart_svg}</div>
      <dl>
        <div><dt>Use when</dt><dd>{escape(card.use_when)}</dd></div>
        <div><dt>Sample data</dt><dd>{escape(card.sample_data)}</dd></div>
        <div><dt>Next file</dt><dd><code>{escape(card.reference)}</code></dd></div>
      </dl>
    </article>"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the editorial-charting contact sheet.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    color_yaml = ROOT / "references" / "color-system.yaml"
    palette = parse_flat_yaml_section(color_yaml, "base_palette")
    ramp = parse_ramp(color_yaml, "blue")
    html = render_html(build_cards(ramp, palette))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html, encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
