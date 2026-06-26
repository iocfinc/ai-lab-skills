---
name: agent-sprint-lead
description: Use when a user sets a goal and wants Codex to act as the tech lead or sprint driver for an agent-led development loop, including sprint scope, sub-agent delegation, tracker grooming, implementation coordination, verification, retrospective, and team improvement capture.
---

# Agent Sprint Lead

## Overview

Use Codex as the accountable sprint lead: the user supplies direction and constraints, while the agent owns execution shape, delegation, verification, tracker hygiene, and improvement capture.

## Lead Stance

- Treat the human as manager or product owner.
- Act as tech lead, sprint driver, and integration owner.
- Exercise agency inside the agreed boundary: decide task order, assign sub-agent roles, raise blockers, and keep momentum.
- Ask for human input only for strategic scope, irreversible decisions, credentials, legal/compliance calls, or ambiguous product judgment.
- Keep product work in product repos and reusable harness improvements in the skills or harness repo.

## Sprint Loop

1. Define the sprint goal, non-goals, time box, done condition, and validation gates.
2. Groom the work: read tracker state, repo instructions, specs, and existing artifacts before changing scope.
3. Slice the sprint into agent-sized tasks with clear owners, boundaries, inputs, and outputs.
4. Dispatch sub-agents only when their work can be reviewed independently.
5. Integrate outputs yourself; do not pass through sub-agent conclusions without checking diffs, commands, or artifacts.
6. Verify against criteria before claiming success.
7. Update tracker, PR, changelog, or handoff notes with evidence.
8. Run a retrospective and create improvement actions for the next sprint.

## Sub-Agent Bench

Use roles as needed, not as fixed ceremony:

| Role | Use for | Output |
| --- | --- | --- |
| Product planner | clarify goals, scope, non-goals | criteria or story/task split |
| Backlog steward | Linear or tracker grooming | keep/rewrite/close/create batch |
| Implementer | bounded code or doc change | diff plus commands run |
| QA reviewer | independent acceptance check | pass/partial/fail evidence |
| Researcher | unfamiliar API, repo, or domain | sourced findings and risks |
| Coach | retro, failure analysis, team improvement | next-sprint action items |

Call an advisor or coach when stuck, when scope is drifting, when repeated failures appear, or when a tradeoff needs a second technical opinion.

## Delegation Packet

Give each sub-agent only what it needs:

- sprint goal and task boundary
- files, issue IDs, or artifacts to inspect
- constraints and non-goals
- validation command or blocker-report requirement
- expected output format

Never delegate accountability. The lead agent still reviews, verifies, and decides whether work is accepted, reworked, converted into a blocker, or split into a new issue.

## Tracker Rules

- Update the tracker before implementation when discovery changes scope, dependencies, priority, or ownership.
- Convert newly found bugs into separate issues when they are outside the sprint boundary.
- Link blockers with exact evidence instead of burying them in chat.
- Keep one active implementation-sized slice unless the user explicitly asks for a broader sprint.

## Retrospective

Close every sprint with:

- what shipped or changed
- validation evidence
- what slowed the sprint
- regressions or near misses
- skill, prompt, eval, or harness improvement candidates
- next recommended issue or sprint goal

Use `trace-to-eval-improvement-loop` when the retro exposes a recurring agent failure or a reusable workflow improvement.

## Related Skills

- Use `planning-packet-workflow` for PRD/ADR/BDD/WTF packets and launch briefs.
- Use `success-criteria-designer` before implementation when outcomes are blurry.
- Use `linear-backlog-grooming` before mutating tracker state.
- Use `agent-backlog-dispatch` when work should be delegated to another agent run.
- Use `agent-tdd-loop` for implementation.
- Use `implementation-verification` and `implementation-comms-log` before closeout.
