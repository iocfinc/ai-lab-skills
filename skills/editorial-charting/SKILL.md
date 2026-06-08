---
name: editorial-charting
description: Use when creating, revising, or critiquing charts that need editorial clarity, story-led framing, disciplined color, readable annotations, source treatment, and implementation-ready chart guidance.
---

# Editorial Charting

## Overview

Turn chart requests into clear, programmatic, publication-grade chart briefs and examples. Use this skill when a chart needs a single claim, truthful visual encoding, restrained emphasis, and implementation details an agent can execute.

Keep this file lean. Load the supporting files only when the task needs them:

- `references/color-system.yaml` for palette tokens, shade ramps, and emphasis rules.
- `references/chart-patterns.yaml` for chart-type recipes and anti-patterns.
- `assets/contact-sheet.html` for a visual contact sheet of available chart capabilities.
- `assets/contact-sheet-preview.png` for repo and review surfaces that render images inline more reliably than HTML.
- `references/contact-sheet-setup.md` for opening, printing, rebuilding, and extending the contact sheet.
- `references/contact-sheet-capabilities.yaml` for mirrored contact sheet metadata and source notes.
- `references/contact-sheet-review-rubric.yaml` for proofreader and visual creative director review checks.
- `scripts/sample_basic_chart.py` for a minimal Python chart using the color tokens.
- `scripts/sample_emphasis_chart.py` for one-color shade emphasis, labels, annotations, and source treatment.
- `scripts/build_contact_sheet.py` for regenerating the contact sheet HTML.
- `scripts/build_contact_sheet_preview.py` for regenerating the PNG preview when Pillow is available.
- `references/skill-prd.md`, `references/skill-adr.md`, `references/skill-bdd.feature`, and `references/skill-wtf.md` when maintaining or extending this skill.

## Foundations

- Start with one reader-facing claim. If there are two claims, split the chart.
- Pick the simplest form that matches the analytical job: comparison, trend, distribution, composition, relationship, or annotated story.
- Use titles and annotations to reduce hunting, not to decorate the page.
- Prefer direct labels over legends when the chart has few series.
- Remove visual elements that do not help the claim, comparison frame, or provenance.
- Treat color as hierarchy: neutral context first, one purposeful accent second.
- Use saturated, Bloomberg-inspired colors for attention, but do not claim an official Bloomberg palette.

## Workflow

1. State the chart's single editorial claim.
2. Select a chart pattern from `references/chart-patterns.yaml`.
3. Select a color role from `references/color-system.yaml`.
4. Define what should be primary, secondary, muted, and annotated.
5. If the user is choosing among chart types, point them to `assets/contact-sheet.html`.
6. Specify implementation details: dimensions, axes, labels, responsive behavior, source line, and export target.
7. Run the chart against anti-chartjunk and accessibility checks before finalizing.

## Output Contract

Return these sections unless the user asks for code only:

1. `Chart claim`
2. `Recommended chart type`
3. `Encoding and comparison frame`
4. `Color and emphasis plan`
5. `Labeling and annotation plan`
6. `Implementation guidance`
7. `Quality checks`

## Maintenance Rule

When changing this skill, update the PRD, ADR, BDD, or WTF reference if the change affects intent, behavior, rationale, or known failure modes. Keep examples out of this `SKILL.md` unless they are essential to invocation.
