---
name: agent-tdd-loop
description: Drive implementation through a test-first agent loop. Use when accepted criteria should become failing tests, the smallest code change, rerun validation, repair failures, and produce handoff evidence for a human or downstream agent.
---

# Agent TDD Loop

## Overview

Use this skill when the work is ready to move from accepted criteria into implementation and verification.

## Preconditions

- A task, issue, or spec has a clear boundary.
- Success criteria or acceptance criteria exist.
- The target repo and nearest `AGENTS.md` are known.
- Validation commands are known, or the missing command is an explicit blocker.

## Loop

1. Read the issue, spec, criteria, and local instructions.
2. Identify the smallest behavior that can be tested first.
3. Add or update a focused failing test before implementation when the repo has a relevant test harness.
4. Run the narrow test and record the failure.
5. Implement the smallest change that satisfies the criterion.
6. Rerun the narrow test, then broaden to the repo's normal validation commands.
7. Repair failures that are inside the task boundary.
8. Stop and report exact blockers for missing tools, auth, data, unclear scope, or unrelated failures.
9. Hand off changed files, commands run, results, and residual risk.

## Test Strategy

- Prefer existing test patterns and helpers.
- Add characterization tests when changing legacy behavior.
- Use manual verification only when automation is not practical, and say why.
- Do not claim a red-green loop unless the failing test was actually observed.
- Do not broaden scope to refactor unrelated modules just to make the test easier.

## Output Contract

Return:

- criteria implemented
- tests added or changed
- red command and result, when available
- green commands and results
- changed files
- blockers or skipped checks
- suggested eval or regression case if the task exposed a reusable failure

Use `implementation-verification` before closing or promoting the work.
