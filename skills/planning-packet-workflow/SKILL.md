---
name: planning-packet-workflow
description: Turn an idea, feature, article, or product initiative into a reusable planning packet with PRD, ADR, BDD, WTF, story/task map, Linear seed, agent launch brief, and optional HTML review notes. Use when a user wants planning artifacts before implementation or agent delegation; use codex-project-planner instead for repo scaffolding.
---

# Planning Packet Workflow

## Purpose

Convert fuzzy work into a packet that can be reviewed, promoted into a tracker, and handed to agents without losing the product intent.

## Minimum Packet

Create or update these artifacts:

- `opportunity-brief.md`: outcome, first user, scope, constraints, unknowns.
- `PRD.md`: audience, problem, requirements, acceptance criteria, non-goals, success signals.
- `ADR.md`: decision pressure, options, chosen approach, consequences, revisit trigger.
- `BDD.md`: Given/When/Then scenarios, edge cases, failure modes, validation commands.
- `WTF.md`: Why, Tradeoffs, Failures, kill criteria, what would change our mind.
- `story-task-map.md`: resolving Stories with agent-sized child Tasks.
- `linear-seed.md`: tracker-safe promotion payload.
- `agent-launch-brief.md`: context, boundaries, commands, done condition.
- `html-review.md`: optional local HTML review surface for plans, diagrams, comparisons, or article spines.

## Boundary With Project Planning

- Use this skill when the desired output is a reusable planning packet.
- Use `codex-project-planner` when the desired output is a repo starter, `AGENTS.md`, task templates, or implementation checklist.
- Use both only when a product idea needs both planning governance and a concrete repo scaffold.

## Workflow

1. Restate the idea in one paragraph.
2. Name the first user and the smallest useful outcome.
3. Separate in-scope work from non-goals.
4. Fill the PRD/ADR/BDD/WTF quartet before creating tracker items.
5. Turn accepted scope into resolving Stories and child Tasks.
6. Mark each Task with:
   - boundary
   - done condition
   - validation command
   - dependency note
7. Prepare `linear-seed.md`, but read the live tracker before creating or updating issues.
8. Write `agent-launch-brief.md` only after the packet has enough context to reduce clarification loops.

## Quality Bar

- Do not promote vague prerequisites as standalone Stories.
- Keep reusable workflow guidance separate from product-specific repo instructions.
- Use concrete validation commands, or write the exact missing-command blocker.
- Treat HTML review artifacts as evidence, not approval by themselves.
- For public/shared packets, remove private paths, secrets, internal IDs, and personal preferences.
- Use `agent-sprint-lead` when the packet is ready to become a manager-to-tech-lead sprint loop.
