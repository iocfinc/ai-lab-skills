# Contact Sheet Setup

## Purpose

Use the contact sheet when a human or agent needs a quick visual inventory of what `editorial-charting` can help specify, prototype, or brief. It is intentionally no-frills: chart pattern, question, sample data, when to use it, and the file to load next.

## Open The Demo

Open:

```text
SKILLS/editorial-charting/assets/contact-sheet.html
```

The HTML is standalone and includes print CSS. To make a PDF, open it in a browser and print to PDF.

For repository browsing or pull-request review, use:

```text
SKILLS/editorial-charting/assets/contact-sheet-preview.png
```

Code hosts usually render PNG files inline. The PNG is a preview companion, not the source of truth.

## Rebuild The Demo

From the skill directory:

```bash
python scripts/build_contact_sheet.py --output assets/contact-sheet.html
```

The generator uses only the Python standard library. It embeds tiny toy-dataset-style sample values so the contact sheet is portable and does not need network access.

To rebuild the PNG preview when Pillow is available:

```bash
python scripts/build_contact_sheet_preview.py --output assets/contact-sheet-preview.png
```

## Extend The Demo

1. Mirror contact sheet metadata in `references/contact-sheet-capabilities.yaml`.
2. Add the matching chart pattern in `references/chart-patterns.yaml` if it is a new pattern.
3. Update `scripts/build_contact_sheet.py` for rendered cards and any new mini-chart renderer.
4. Rebuild `assets/contact-sheet.html`.
5. Run the review checks in `references/contact-sheet-review-rubric.yaml`.
6. Update `references/skill-bdd.feature` when behavior changes.

## Design Rules

- Keep the contact sheet compact, and verify print pagination after adding cards.
- Prefer numbered steps, compact labels, and direct visual examples.
- Use the bundled color tokens; do not add a new visual language here.
- Make the HTML easy to inspect and print before making it clever.
- Keep the PNG preview clear enough for code-host file browsers and review threads.

## Review Loop

Use two review roles before finalizing major contact sheet changes:

- Proofreader: checks source wording, setup truthfulness, exact file references, and overclaims.
- Visual creative director: checks positioning, clipping, callouts, scale, print density, and taste.

Fold accepted findings back into the generator, contact sheet metadata, setup guide, and BDD scenarios before syncing the canonical copy.
