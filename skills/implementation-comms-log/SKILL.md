---
name: implementation-comms-log
description: Produce durable implementation communication after agent or human work: Linear comments, changelog notes, PR bodies, release notes, test summaries, blocker reports, and handoff logs. Use when work should be understandable later without rereading the whole thread.
---

# Implementation Comms Log

## Purpose

Turn implementation work into durable project memory: what changed, why, how it was validated, and what remains.

## Required Sections

For tracker comments, PR bodies, or changelog notes, include:

- outcome
- changed files or modules
- validation commands and results
- user-visible behavior change
- blockers or skipped checks
- follow-up tasks

## Linear Comment Shape

```markdown
Update:
- Changed:
- Validation:
- Evidence:
- Blockers:
- Follow-up:
```

## PR Body Shape

```markdown
## Summary
-

## Validation
-

## Notes
-
```

## Changelog Shape

```markdown
### Changed
-

### Fixed
-

### Validation
-
```

## Rules

- Do not claim tests passed unless the command actually ran and passed.
- Preserve exact blocker text for missing auth, tools, providers, MCPs, or external services.
- Distinguish stale artifacts from fresh validation.
- Keep research-only, advisory, or compliance-sensitive language intact when the domain requires it.
- Link tracker issues, PRs, artifacts, and local paths when available.
