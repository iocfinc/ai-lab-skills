---
name: linear-backlog-grooming
description: Review and reconcile Linear backlogs before creating, updating, closing, or delegating issues. Use when the user wants to clear stale backlog items, deconflict old tickets with a newer direction, promote a planning packet into Linear, or prepare agent-ready work.
---

# Linear Backlog Grooming

## Purpose

Make Linear a trustworthy source of truth by reading first, reconciling second, and mutating only after the intended batch is clear.

## Read First

Before changing anything:

1. Identify the workspace, team, project, and relevant labels.
2. List open issues by state.
3. Fetch parent Stories and representative child Tasks.
4. Search for exact new-direction terms, stale terminology, duplicates, and already-completed work.
5. Separate findings into:
   - keep
   - rewrite
   - close/cancel
   - create
   - needs user decision

## Deconfliction Rules

- Existing backlog is authoritative until read.
- New issues should not duplicate existing Stories.
- Rewrite stale Stories when the product direction changed but the problem still matters.
- Close onboarding/default/noise tickets when they no longer represent real work.
- Consolidate fragmented child tickets when one parent packet now owns the reusable context.
- Do not move product strategy into issue comments when it belongs in a planning packet.

## Mutation Batch

Before applying changes, summarize the batch:

- issues to create
- issues to rewrite
- issues to cancel or close
- labels to add or remove
- dependencies or blockers to set
- agent-ready candidates to expose

After applying changes, verify by re-listing or fetching the changed issues.

## Agent-Ready Gate

Only mark a child Task `agent-ready` when it has:

- a specific file/repo boundary
- a done condition
- validation commands
- dependency status
- clear failure-reporting expectations

Avoid marking parent Stories `agent-ready` unless the orchestrator explicitly works at Story level.
