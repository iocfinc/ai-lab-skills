---
name: prompt-hardening
description: Improve AGENTS.md files, task briefs, implementation plans, and acceptance criteria so Codex can execute with less ambiguity and fewer review cycles. Use when prompts are vague, tasks sprawl, instructions conflict, or a repo needs sharper operating constraints and clearer definitions of done.
---

# Prompt Hardening

## Overview

Rewrite loose instructions into concise, operational inputs that drive reliable execution.

## Workflow

1. Extract the current request, constraints, and success criteria.
2. Remove ambiguity:
   - define the exact outcome
   - identify in-scope and out-of-scope work
   - name protected files or systems
3. Add validation requirements.
4. Replace subjective language with observable acceptance criteria.
5. Keep the final prompt short enough to remain usable.

## Hardening Rules

- Prefer imperatives over narrative prose.
- Prefer file paths, commands, and measurable checks over adjectives.
- Keep one owner per instruction.
- Surface instruction conflicts explicitly and propose a default resolution.
