---
name: trace-to-eval-improvement-loop
description: Turn Codex traces, failed agent runs, reviewer feedback, or recurring workflow mistakes into eval cases and harness improvement tasks. Use when an ADLC loop needs regression coverage, skill updates, prompt hardening, or reusable agent-harness follow-up.
---

# Trace To Eval Improvement Loop

## Overview

Close the agentic development lifecycle by turning observed failures into better criteria, evals, skills, or harness tasks.

This is the coach and retrospective lane for `agent-sprint-lead`: use it when the sprint exposes repeated mistakes, delegation gaps, validation misses, or reusable team-improvement opportunities.

## Inputs

- Codex run trace, terminal log, PR review, Linear comment, or user correction.
- Original task, acceptance criteria, and validation evidence.
- Changed files or generated artifacts, when available.
- The repo or skill family that should own the fix.

## Workflow

1. Identify the expected behavior and the observed behavior.
2. Classify the failure:
   - trigger or routing
   - context gathering
   - success criteria
   - task decomposition
   - implementation
   - verification
   - communication
   - tooling or permission
3. Decide the owner:
   - product repo for product-specific fixes
   - public skill for reusable, public-safe guidance
   - `CodexSkills` harness for reusable private agents, hooks, templates, evals, or automations
4. Write the smallest regression case that would catch the failure next time.
5. Propose or apply the skill, prompt, eval, or harness change.
6. Run available validators and report any unverified layer.

## Eval Case Shape

Use this shape when creating eval candidates:

```yaml
- id: regression-short-name
  type: regression
  prompt: "<realistic future prompt>"
  expected_behavior: "<what the agent should do>"
  assertions:
    - "<observable check>"
  deterministic_checks:
    - kind: file_contains
      path: "<path>"
      contains:
        - "<required term>"
```

Use deterministic checks for files, commands, terms, or artifact contracts. Use rubric checks only for judgment-heavy behavior.

## Routing Rules

- Do not copy private paths, secrets, workspace IDs, or personal operating context into public skills.
- Keep reusable harness logic in `CodexSkills`.
- Keep product-specific fixes in the product repo.
- Do not treat a one-off failure as a harness rule until there is a clear recurring risk.
- If live services or credentials are involved, prefer dry-run or fixture evals before live mutation evals.

## Output Contract

Return the failure summary, owner, proposed regression case, proposed change, validation performed, and remaining risk.
