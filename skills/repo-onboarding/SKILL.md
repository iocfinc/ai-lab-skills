---
name: repo-onboarding
description: Rapidly map an unfamiliar repository so Codex can work safely and efficiently. Use when starting in an existing codebase, preparing for a bugfix or feature, reviewing architecture, identifying validation commands, or drafting concise repo notes such as AGENTS.md and execution plans.
---

# Repo Onboarding

## Overview

Build a fast mental model of a repository before making changes. Focus on structure, commands, risks, and the smallest set of files needed to proceed.

## Workflow

1. Read the nearest `AGENTS.md` files in scope.
2. Capture the top-level layout and identify the primary app, libraries, tests, and scripts.
3. Locate package manifests, build files, and CI entry points.
4. Identify validation commands:
   - lint
   - tests
   - typecheck
   - build
5. Find the files most likely to control the requested behavior.
6. Summarize:
   - architecture
   - active constraints
   - likely change surface
   - validation plan

## Heuristics

- Prefer `rg` and focused file reads over broad dumps.
- Read only enough code to explain the current behavior.
- Distinguish between facts, likely inferences, and open questions.
- Escalate only when sandbox or missing tooling blocks progress.
