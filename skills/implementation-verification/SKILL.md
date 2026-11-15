---
name: implementation-verification
description: Verify completed code, docs, or agent runs against acceptance criteria before closing work. Use for final review, pre-PR checks, tracker updates, or deciding whether an agent run is Passed, Partial, or Failed.
---

# Implementation Verification

## Overview

Check whether the work actually satisfies the contract before it becomes project memory.

## Workflow

1. Read the task, acceptance criteria, validation plan, and nearest `AGENTS.md`.
2. Inspect changed files and confirm the diff stays inside the requested boundary.
3. Run the required validation commands when tooling is available.
4. Compare evidence against each acceptance criterion.
5. Classify the result:
   - `Passed`: criteria satisfied and required checks passed.
   - `Partial`: useful progress, but checks, criteria, or evidence are incomplete.
   - `Failed`: required outcome is missing, broken, or unverified.
6. Report exact blockers for missing auth, tools, fixtures, credentials, services, or commands.
7. Recommend the next action: close, repair, re-dispatch, or convert the failure into an eval.

## Evidence Rules

- Do not infer tests passed from code inspection.
- Distinguish fresh validation from stale logs or prior artifacts.
- Record command, exit result, and meaningful failure text.
- Treat missing validation as `Partial` unless the task explicitly allows manual review.
- If unrelated local changes exist, identify them without reverting them.

## Output Contract

Use this shape:

```markdown
Verification: Passed | Partial | Failed

Criteria:
-

Commands:
-

Changed files:
-

Blockers:
-

Next action:
-
```

Use `implementation-comms-log` after verification to write durable tracker, PR, or handoff notes.
