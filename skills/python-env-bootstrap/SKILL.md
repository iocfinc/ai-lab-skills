---
name: python-env-bootstrap
description: Set up and standardize Python project environments with a pyproject-first workflow, while keeping venv as a safe fallback. Use when bootstrapping a new Python repo, onboarding an existing Python codebase, or standardizing local setup commands.
---

# Python Env Bootstrap

## Overview

Create a usable Python environment quickly, favoring `pyproject.toml`-based workflows and only falling back to bare `venv` when the project is intentionally minimal.

## Workflow

1. Inspect the repo for `pyproject.toml`.
2. If it exists, prefer a modern sync path such as `uv`.
3. If it does not exist, decide whether to add one or keep a minimal `.venv` setup.
4. Standardize the local environment path as `.venv` unless the repo already uses something else.
5. Document the bootstrap and validation commands in the repo `AGENTS.md` or `README.md`.
