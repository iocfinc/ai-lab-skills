---
name: codex-project-planner
description: Turn a vague product or feature idea into a Codex-ready project plan, repository starter, and execution checklist. Use when starting a new codebase, shaping an MVP, defining acceptance criteria, or preparing boilerplate files such as AGENTS.md, task templates, validation commands, and architecture notes.
---

# Codex Project Planner

## Overview

Convert fuzzy project ideas into implementation-ready repo structure and instructions that let Codex operate with less guessing and lower review overhead.

## Workflow

1. Restate the requested product or feature in one paragraph.
2. Define boundaries:
   - user outcome
   - in-scope work
   - out-of-scope work
   - technical constraints
3. Choose the thinnest useful repo skeleton.
4. Draft the operating files:
   - root `AGENTS.md`
   - `TASK_TEMPLATE.md`
   - `IMPLEMENTATION_PLAN_TEMPLATE.md`
   - `docs/architecture.md` if architecture is non-trivial
5. Define validation commands before implementation work begins.
6. Record assumptions and open questions explicitly.

## Planning Rules

- Prefer small, testable MVPs over broad roadmaps.
- Define "done" using observable behavior, not intent.
- Make command names and repo layout obvious.
- Avoid speculative abstractions unless the project already needs them.
- Keep reusable process guidance separate from product-specific rules.
