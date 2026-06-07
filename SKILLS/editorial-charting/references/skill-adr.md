# ADR: Editorial Charting Skill Refresh

## Status

Accepted.

## Context

The previous public chart skill was named `economist-chart-editor` and embedded most guidance directly in `SKILL.md`. The refreshed skill needs a broader editorial identity, portable examples, a maintained color system, and decision artifacts that help agents avoid accidental regressions.

## Decisions

1. Rename the active skill to `editorial-charting`.
2. Keep `economist-chart-editor` as a legacy alias instead of deleting the old public path.
3. Keep `SKILL.md` concise and move chart tokens, patterns, examples, and maintainability docs into support files.
4. Use a Bloomberg-inspired expanded palette and shade ramps, clearly marked as internal and unofficial.
5. Make YAML plus Python the primary executable example stack.
6. Keep canonical authoring in `../CodexSkills/.agents/skills/` and export curated public copies into this repo.
7. Add a standalone HTML contact sheet under `assets/` and a standard-library Python generator for rebuilds.

## Consequences

- Existing users get a soft migration path.
- Future chart variants can be added as reference or script files without bloating the main skill.
- Maintainers must update PRD, ADR, BDD, or WTF files when behavior or rationale changes.
- Humans can open the contact sheet directly, while agents can use it as a capability index before selecting a chart pattern.
