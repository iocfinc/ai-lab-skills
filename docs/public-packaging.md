# Public Skill Packaging

## Purpose

`codex-ai-lab-skills` is a thin public distribution repo.

Keep these boundaries strict:

- canonical skill authoring lives in `CodexSkills/.agents/skills/`
- reusable export logic lives in `CodexSkills`
- this repo receives curated public outputs only

## What Gets Published

Each public skill should live at:

```text
SKILLS/<skill-name>/SKILL.md
```

Optional supporting files are allowed only when the public skill needs them:

- `references/`
- `scripts/`
- `assets/`

Do not copy harness-only helpers, internal planning docs, repo-local caches, or runtime scratch output into this repo.

## Public Skill Rules

- skill folder names use lowercase letters, numbers, and hyphens only
- frontmatter stays minimal: `name`, `description`, optional `version`
- descriptions should explain when to load the skill, not summarize the workflow
- published content should be concise enough to install cleanly from `SKILL.md` marketplaces

## XDG Runtime Policy

Any packaging, validation, preview, or export helper should default to XDG paths rather than repo-local clutter:

```bash
export XDG_STATE_HOME="${XDG_STATE_HOME:-$HOME/.local/state}"
export XDG_CACHE_HOME="${XDG_CACHE_HOME:-$HOME/.cache}"
export XDG_DATA_HOME="${XDG_DATA_HOME:-$HOME/.local/share}"
```

Use Dioscuri-scoped subdirectories under those roots, for example:

```text
$XDG_STATE_HOME/dioscuri/ai-lab-skills
$XDG_CACHE_HOME/dioscuri/ai-lab-skills
$XDG_DATA_HOME/dioscuri/ai-lab-skills
```

## Packaging Flow

1. Author or refine the canonical skill in `CodexSkills`.
2. Strip internal-only references, harness notes, and reusable private tooling.
3. Export the public copy into this repo's `SKILLS/` tree.
4. Validate:
   - every published skill has a `SKILL.md`
   - frontmatter is present and trigger-focused
   - no runtime clutter was added
5. Publish from this repo.

## Current Public Inventory

- `anti-slop-editorial`
- `instant-influence`
- `economist-chart-editor`
- `repo-onboarding`
- `prompt-hardening`
- `evidence-synthesis`
- `python-env-bootstrap`
- `codex-project-planner`
