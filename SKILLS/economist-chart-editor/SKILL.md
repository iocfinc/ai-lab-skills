---
name: economist-chart-editor
description: Use when a chart needs Economist-style editorial discipline across chart choice, framing, typography, annotation, palette, source treatment, and implementation guidance.
---

# Economist Chart Editor

## Overview

Turn a chart request into an editorial chart brief with disciplined design and implementation guidance.

Aim for sharp communication, not decorative visualization.

## What Good Looks Like

- one clear point per chart
- chart type selected for comparison, trend, composition, or distribution on purpose
- typography and spacing that support scanning
- restrained color with one purposeful emphasis
- labels and annotations that reduce hunting
- source and note lines that feel editorial, not academic clutter

## Workflow

1. Identify the chart's single editorial claim.
2. Choose the simplest chart type that makes that claim legible.
3. Define the comparison frame:
   - what the reader should notice first
   - what can stay muted
   - what needs annotation
4. Set layout and style rules before implementation.
5. Produce implementation guidance that a JS, CSS, Tailwind, or SVG workflow can execute directly.

## Chart Rules

- Prefer bars for ranked comparison, lines for trends, scatter only when relationships matter, and avoid novelty forms.
- Remove anything that does not help the main claim.
- Use direct labeling where possible.
- Keep gridlines light and sparse.
- Make axis titles short and unit-aware.
- If the chart needs heavy explanation, fix the chart or split it.

## Typography And Layout

- Use a clear title that states the point, not just the topic.
- Use a short subtitle only when it adds necessary context.
- Keep the plot area generous enough for labels to breathe.
- Maintain consistent spacing between title, chart, notes, and source.
- Use annotation sparingly and place it near the data it explains.

## Color And Emphasis

- Default to a restrained neutral base.
- Use one primary accent to direct attention.
- Add a second accent only when a comparison truly needs it.
- Avoid rainbow palettes, heavy fills, gradients, shadows, or 3D effects.
- Emphasis should come from contrast and hierarchy, not ornament.

## Source And Notes

- Include a compact source line.
- Add notes only when methodology, estimate status, or time coverage matters.
- Keep footnotes visually subordinate to the chart.

## Output Contract

Return:

1. `Recommended chart type`
2. `Editorial framing`
3. `Layout and palette`
4. `Labeling and annotation plan`
5. `Implementation guidance`
6. `Anti-chartjunk checks`

## Implementation Guidance

When producing implementation notes, include:

- container width and aspect ratio guidance
- axis and grid treatment
- label placement strategy
- responsive behavior
- color tokens or CSS variable suggestions
- whether the chart is better rendered with SVG, canvas, or HTML overlays
