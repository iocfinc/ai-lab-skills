# Repository Instructions

## Purpose

This repository publishes reusable public-facing agent skills under the AI Lab brand.

## Working Rules

- Keep this repo public-safe. Do not add private planning notes, internal memory, secrets, or user-specific operating context.
- Prefer small, auditable Markdown skills over hidden behavior or heavy automation.
- Keep each `SKILL.md` concise. Move long examples or source notes into sibling `references/` files only when needed.
- Optimize for discoverability: clear names, clear descriptions, concrete trigger language.
- Treat the root `skills/` directory as the public distribution surface.

## Validation

- Run `bash scripts/validate.sh` before claiming the repo is ready.
- Ensure every skill has valid frontmatter with `name` and `description`.
