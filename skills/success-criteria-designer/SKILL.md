---
name: success-criteria-designer
description: Turn vague goals, specs, backlog items, or planning packets into observable success criteria, acceptance tests, non-goals, validation commands, and done conditions. Use before implementation, agent delegation, tracker promotion, or review when outcomes are ambiguous.
---

# Success Criteria Designer

## Overview

Convert intent into criteria a human reviewer or agent can actually verify.

## Workflow

1. Read the source request, planning packet, issue, or spec.
2. Name the beneficiary and the smallest useful outcome.
3. Separate:
   - in-scope behavior
   - non-goals
   - constraints
   - failure modes
   - unknowns
4. Rewrite subjective claims into observable checks.
5. Attach a validation path for each important criterion:
   - automated command
   - manual review step
   - artifact inspection
   - explicit blocker when validation is impossible
6. End with a short `Done when` section that a fresh agent can use.

## Criteria Rules

- Prefer behavior, artifacts, and commands over adjectives.
- Include negative criteria when avoiding behavior matters.
- Keep criteria small enough to test or inspect independently.
- Do not invent product scope to make criteria feel complete.
- If a validation command is unknown, write the exact missing-command blocker.
- Keep reusable workflow guidance out of product repos.

## Output Contract

Use this shape:

```markdown
## Success Criteria

Outcome:

Non-goals:
-

Acceptance criteria:
-

Validation:
-

Done when:
-
```

## Handoff

Use `agent-tdd-loop` after criteria are accepted and implementation should begin. Use `linear-backlog-grooming` before mutating a tracker.
