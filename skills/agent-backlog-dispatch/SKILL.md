---
name: agent-backlog-dispatch
description: Prepare tracker issues for safe agent execution through codex exec, Symphony, or another local orchestration runner. Use when converting backlog Tasks into agent candidates, filtering executable work, running agents, collecting validation evidence, and updating tracker status.
---

# Agent Backlog Dispatch

## Purpose

Dispatch only the work that is ready for an agent, and keep the orchestration loop auditable.

Symphony is a local runner pattern for pulling labeled tracker issues into prepared workspaces. If a repo does not use Symphony, apply the same gates to `codex exec`, worktrees, or another runner.

Use `agent-sprint-lead` first when the user wants one lead agent to own scope, assign sub-agent roles, coordinate tickets, and run the sprint closeout.

## Candidate Gate

An issue is a candidate only when it is a child Task or similarly bounded work item with:

- `agent-ready` or equivalent execution label
- runner label if the local runner filters on labels
- clear boundary
- done condition
- validation commands
- dependency notes
- exact blocker reporting requirements

Do not dispatch blocked implementation work before its prep task is complete.

## Dispatch Workflow

1. Read the tracker issue and any parent Story.
2. Read the planning packet or implementation brief.
3. Confirm the target repo and nearest `AGENTS.md`.
4. Prepare a workspace or worktree according to the runner's convention.
5. Run the agent with the smallest complete prompt:
   - issue identifier and title
   - source packet path or artifact
   - repo boundary
   - required commands
   - expected comms output
6. Poll or inspect logs until the run finishes or blocks.
7. Verify changed files and command output yourself before calling the work complete.

## `codex exec` Use

Use `codex exec` for bounded subtasks when a separate agent run is useful. Keep prompts short and concrete. Ask the agent to return:

- changed files
- commands run
- exact failures
- summary for tracker comment
- changelog or PR-body draft when relevant

Do not use `codex exec` to bypass local review. The primary agent still owns final verification.

## Completion Rule

After a successful run:

- update the tracker with evidence
- remove or advance execution labels if appropriate
- attach or quote validation commands
- write changelog or PR notes if requested

If blocked, leave the issue open and report the exact blocker.
