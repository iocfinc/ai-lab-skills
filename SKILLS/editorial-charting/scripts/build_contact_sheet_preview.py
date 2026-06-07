"""Build a PNG preview for the editorial-charting contact sheet.

The HTML contact sheet is the primary demo. This PNG exists for repository and
pull-request visibility because code hosts render images inline more reliably
than arbitrary HTML files.
"""

from __future__ import annotations

import argparse
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover - environment dependent
    raise SystemExit("Pillow is required: python -m pip install pillow") from exc

from build_contact_sheet import ROOT, build_cards, parse_flat_yaml_section, parse_ramp


DEFAULT_OUTPUT = ROOT / "assets" / "contact-sheet-preview.png"
WIDTH = 1400
HEIGHT = 1040


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


FONTS = {
    "h1": font(38, True),
    "h2": font(21, True),
    "claim": font(16, True),
    "body": font(15),
    "small": font(13),
    "tiny": font(12),
    "num": font(22, True),
}


COLORS = {
    "ink": "#111827",
    "muted": "#64748B",
    "line": "#CBD5E1",
    "panel": "#F8FAFC",
    "blue": "#0B5FFF",
    "blue_light": "#CEDFFF",
    "blue_mid": "#79A7FF",
    "cyan": "#00AEEF",
    "orange": "#FF6B00",
    "violet": "#7B61FF",
    "magenta": "#E20074",
    "gray": "#D1D5DB",
    "grid": "#E5E7EB",
    "white": "#FFFFFF",
}


def draw_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fill: str, style: str) -> None:
    draw.text(xy, text, fill=fill, font=FONTS[style])


def draw_card(draw: ImageDraw.ImageDraw, index: int, card, x: int, y: int, w: int, h: int) -> None:
    draw.rectangle((x, y, x + w, y + h), fill=COLORS["white"], outline=COLORS["line"], width=2)
    draw.rectangle((x, y, x + 58, y + 62), fill=COLORS["ink"])
    draw_text(draw, (x + 17, y + 18), card.number, COLORS["white"], "num")
    draw_text(draw, (x + 74, y + 12), card.title, COLORS["ink"], "h2")
    draw_text(draw, (x + 74, y + 39), card.question, COLORS["blue"], "small")

    chart_x, chart_y = x + 16, y + 78
    chart_w, chart_h = w - 32, 150
    draw.rectangle((chart_x, chart_y, chart_x + chart_w, chart_y + chart_h), fill=COLORS["panel"], outline=COLORS["line"], width=1)
    draw_text(draw, (chart_x + 12, chart_y + 10), card.claim, COLORS["ink"], "claim")
    draw_mini_chart(draw, index, chart_x + 12, chart_y + 36, chart_w - 24, chart_h - 46)

    meta_y = chart_y + chart_h + 16
    draw_text(draw, (x + 16, meta_y), "USE WHEN", COLORS["muted"], "tiny")
    draw_text(draw, (x + 16, meta_y + 18), shorten(card.use_when, 48), COLORS["ink"], "small")
    draw_text(draw, (x + 16, meta_y + 47), "NEXT FILE", COLORS["muted"], "tiny")
    draw_text(draw, (x + 16, meta_y + 65), shorten(card.reference.replace("references/", ""), 46), COLORS["ink"], "small")


def shorten(text: str, limit: int) -> str:
    return text if len(text) <= limit else text[: limit - 3].rstrip() + "..."


def draw_mini_chart(draw: ImageDraw.ImageDraw, index: int, x: int, y: int, w: int, h: int) -> None:
    if index == 0:
        labels = ["setosa", "versicolor", "virginica"]
        values = [5.0, 5.9, 6.6]
        colors = [COLORS["blue_light"], COLORS["blue_mid"], COLORS["blue"]]
        for row, (label, value, color) in enumerate(zip(labels, values, colors)):
            yy = y + row * 30 + 10
            bar_w = int((w - 112) * value / max(values))
            draw_text(draw, (x, yy), label, COLORS["muted"], "tiny")
            draw.rectangle((x + 82, yy, x + 82 + bar_w, yy + 15), fill=color)
            draw_text(draw, (x + w - 28, yy - 1), f"{value:g}", COLORS["ink"], "tiny")
    elif index == 1:
        values = [31, 35, 34, 42, 48, 51, 59, 64]
        pts = []
        for i, value in enumerate(values):
            px = x + int(i * (w - 16) / (len(values) - 1))
            py = y + h - 8 - int((value - min(values)) * (h - 24) / (max(values) - min(values)))
            pts.append((px, py))
        for gy in [y + 16, y + 42, y + 68]:
            draw.line((x, gy, x + w, gy), fill=COLORS["grid"], width=1)
        draw.line(pts, fill=COLORS["blue"], width=5, joint="curve")
        draw.ellipse((pts[-1][0] - 5, pts[-1][1] - 5, pts[-1][0] + 5, pts[-1][1] + 5), fill=COLORS["blue"])
        draw_text(draw, (pts[-1][0] - 24, pts[-1][1] - 26), "64", COLORS["ink"], "tiny")
    elif index == 2:
        values = [8, 18, 22, 14, 27, 31, 20]
        for i, value in enumerate(values):
            bar_h = int((h - 22) * value / max(values))
            bx = x + 6 + i * 34
            color = COLORS["blue"] if i == 5 else COLORS["blue_light"]
            draw.rectangle((bx, y + h - bar_h - 16, bx + 22, y + h - 16), fill=color)
        draw.line((x, y + h - 16, x + w, y + h - 16), fill=COLORS["muted"], width=1)
        draw.line((x + 128, y + 20, x + 128, y + h - 16), fill=COLORS["ink"], width=2)
        draw_text(draw, (x + 136, y + 22), "typical", COLORS["ink"], "tiny")
    elif index == 3:
        parts = [(40, COLORS["cyan"], "0-3 40%"), (30, COLORS["orange"], "4-6 30%"), (30, COLORS["violet"], "7-9 30%")]
        bx = x + 4
        for pct, color, label in parts:
            bw = int((w - 8) * pct / 100)
            draw.rectangle((bx, y + 36, bx + bw, y + 70), fill=color)
            draw_text(draw, (bx + 8, y + 47), label, COLORS["white"], "tiny")
            bx += bw
        draw_text(draw, (x + 4, y + 86), "0%", COLORS["muted"], "tiny")
        draw_text(draw, (x + w - 36, y + 86), "100%", COLORS["muted"], "tiny")
    elif index == 4:
        points = [(26, 96), (48, 93), (68, 82), (100, 58), (124, 64), (144, 50), (168, 43), (190, 35), (210, 22), (226, 29)]
        draw.line((x, y + h - 10, x + w, y + h - 10), fill=COLORS["muted"], width=1)
        draw.line((x, y + 8, x, y + h - 10), fill=COLORS["muted"], width=1)
        draw.line([(x + 8, y + 86), (x + 76, y + 64), (x + 144, y + 42), (x + w - 10, y + 22)], fill="#94A3B8", width=2)
        for i, (px, py) in enumerate(points):
            color = COLORS["magenta"] if i in {3, 8} else COLORS["gray"]
            r = 5 if i in {3, 8} else 3
            draw.ellipse((x + px - r, y + py - r, x + px + r, y + py + r), fill=color)
    else:
        values = [18, 27, 42, 55, 71]
        colors = [COLORS["blue_light"], COLORS["blue_light"], COLORS["blue_mid"], "#3077FF", COLORS["blue"]]
        for i, (value, color) in enumerate(zip(values, colors)):
            bar_h = int((h - 18) * value / max(values))
            bx = x + 12 + i * 42
            draw.rectangle((bx, y + h - bar_h - 10, bx + 26, y + h - 10), fill=color)
        draw_text(draw, (x + 130, y + 2), "Peak reuse", COLORS["ink"], "tiny")
        draw.line((x + 178, y + 18, x + 202, y + 30), fill=COLORS["ink"], width=2)


def build_preview(output: Path) -> None:
    color_yaml = ROOT / "references" / "color-system.yaml"
    cards = build_cards(parse_ramp(color_yaml, "blue"), parse_flat_yaml_section(color_yaml, "base_palette"))
    image = Image.new("RGB", (WIDTH, HEIGHT), COLORS["white"])
    draw = ImageDraw.Draw(image)

    draw.rectangle((48, 42, 132, 124), fill=COLORS["ink"])
    draw_text(draw, (70, 68), "EC", COLORS["white"], "h1")
    draw_text(draw, (156, 46), "Editorial Charting Contact Sheet", COLORS["ink"], "h1")
    draw_text(draw, (158, 96), "Six chart patterns with claims, sample data, and implementation references.", COLORS["muted"], "body")
    draw.line((48, 144, WIDTH - 48, 144), fill=COLORS["ink"], width=2)

    steps = [
        ("1. Pick the question", "Comparison, trend, distribution, composition, relationship, or callout."),
        ("2. Load the pattern", "Use references/chart-patterns.yaml."),
        ("3. Choose emphasis", "Use shades for emphasis; categorical tokens for stable groups."),
        ("4. Build or brief", "Use samples, contact sheet, or the output contract."),
    ]
    step_w = (WIDTH - 96 - 36) // 4
    for i, (label, body) in enumerate(steps):
        sx = 48 + i * (step_w + 12)
        draw.rectangle((sx, 166, sx + step_w, 238), outline=COLORS["line"], width=2)
        draw_text(draw, (sx + 14, 180), label, COLORS["ink"], "small")
        draw_text(draw, (sx + 14, 204), shorten(body, 44), COLORS["muted"], "tiny")

    card_w = 410
    card_h = 315
    x_positions = [48, 460, 872]
    y_positions = [266, 610]
    for i, card in enumerate(cards):
        draw_card(draw, i, card, x_positions[i % 3], y_positions[i // 3], card_w, card_h)

    draw_text(draw, (48, 982), "Preview companion for assets/contact-sheet.html. Demo values are toy-dataset-style examples; palette is Bloomberg-inspired, not official.", COLORS["muted"], "tiny")
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)
    print(output)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a PNG preview for the editorial-charting contact sheet.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    build_preview(args.output)


if __name__ == "__main__":
    main()
