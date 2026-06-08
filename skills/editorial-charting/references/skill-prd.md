# PRD: Editorial Charting Skill

## Problem

Agents need a reusable charting skill that keeps the invokable instructions concise while still providing executable chart examples, color tokens, and maintainable design decisions.

## Audience

- Agents creating chart briefs, chart code, analytical reports, dashboards, and scrollytelling visuals.
- Maintainers extending chart patterns, palettes, examples, or regression checks.

## Goals

- Produce charts with one clear claim, legible hierarchy, truthful encodings, and compact source treatment.
- Move implementation examples out of `SKILL.md` and into reference or script files.
- Replace the old direct Economist framing with broader editorial charting principles.
- Provide a documented color system based on high-saturation, Bloomberg-inspired defaults plus single-hue shade ramps.
- Provide a no-frills contact sheet that lets humans and agents scan available chart capabilities before choosing an implementation path.
- Make future changes traceable through PRD, ADR, BDD, and WTF artifacts.

## Non-Goals

- Recreating any publication's proprietary style guide.
- Building a chart-rendering framework.
- Supporting every visualization library in v1.

## Success Criteria

- `SKILL.md` stays short and clearly invokable.
- Agents can find color and chart examples without loading every detail by default.
- Python examples compile and demonstrate token loading.
- The contact sheet opens as standalone HTML and can be printed to PDF.
- Legacy users of `economist-chart-editor` receive a clear pointer to `editorial-charting`.
