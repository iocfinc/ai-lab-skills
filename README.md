# AI Lab Skills

Public distribution repo for a curated set of installable `SKILL.md` skills focused on AI work quality, product thinking, and practical developer workflows.

This repository is intentionally thin:

- published skills live under `SKILLS/`
- canonical authoring stays in `CodexSkills`
- reusable export logic stays out of this repo
- checked-in files stay limited to curated skill content and docs

The product posture is deliberate: this is not a dump of every internal skill. It is a public-facing shortlist that should be useful on its own and legible as a portfolio of how we design AI-native workflows.

## Install

Install a single skill with `skills.sh`:

```bash
skills install github.com/iocfinc/ai-lab-skills/SKILLS/anti-slop-editorial
skills install github.com/iocfinc/ai-lab-skills/SKILLS/repo-onboarding
skills install github.com/iocfinc/ai-lab-skills/SKILLS/prompt-hardening
skills install github.com/iocfinc/ai-lab-skills/SKILLS/evidence-synthesis
```

Install the repo through other `SKILL.md`-compatible marketplaces by targeting the same `SKILLS/<skill-name>` path.

## Skill Inventory

### Writing And Communication

- `anti-slop-editorial`  
  Rewrite technical, AI, or product writing so it sounds concrete, useful, and close to the real work.

- `instant-influence`  
  Facilitate one-question-at-a-time when someone is stuck in a conversation, draft, or decision.

### Research And Framing

- `economist-chart-editor`  
  Apply Economist-style editorial discipline to chart framing, typography, annotation, and implementation detail.

- `evidence-synthesis`  
  Build a source-backed evidence matrix and keep facts separate from inference.

### Engineering Workflow

- `repo-onboarding`  
  Rapidly map an unfamiliar repository before changing code.

- `prompt-hardening`  
  Rewrite vague task briefs and operating instructions into tighter execution inputs.

- `python-env-bootstrap`  
  Standardize Python repo setup with a `pyproject.toml`-first workflow and `.venv` fallback.

- `codex-project-planner`  
  Turn a fuzzy product or feature idea into a Codex-ready project skeleton and execution checklist.

## Curation Notes

The canonical inventory in `CodexSkills` is much larger than the public surface here. Skills were selected for:

- stand-alone usefulness
- low private-context dependency
- broad applicability outside one repo or workflow
- strength as portfolio-quality product artifacts

See [docs/2026-05-29-skill-audit.md](docs/2026-05-29-skill-audit.md) for the current shortlist and deferred candidates.

## Publishing Model

This repo is the public distro surface, not the authoring workspace. The expected workflow is:

1. draft or refine the skill in `CodexSkills`
2. export the curated public copy into `SKILLS/`
3. validate the public tree
4. publish from this repo

See [docs/public-packaging.md](docs/public-packaging.md) for the authoring and packaging contract.
