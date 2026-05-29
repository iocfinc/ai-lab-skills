---
name: anti-slop-editorial
description: Use when technical, AI, or product writing sounds vague, inflated, repetitive, machine-polished, or detached from the real work and needs a concrete editorial rewrite.
---

# Anti-Slop Editorial

## Overview

Rewrite drafts so they sound like a competent practitioner explaining real systems, decisions, and tradeoffs.

The target is not louder prose. The target is clearer prose with concrete actors, mechanisms, and implications.

## When To Use

Use this skill when a draft:

- looks polished but says little
- hides weak thinking behind abstract nouns
- overuses prestige phrasing or AI boilerplate
- sounds unlike the team that actually did the work
- needs to be sharper for engineers, operators, PMs, founders, or informed customers

## Core Method

1. Identify the reader, the document type, and the decision or understanding the piece should support.
2. Extract the concrete facts:
   - what changed
   - how it works
   - what tradeoffs matter
   - what evidence or examples make the point real
3. Rewrite abstract claims into observable mechanisms, constraints, and outcomes.
4. Keep domain language only when it improves precision for the intended reader.
5. Remove filler transitions, repeated framing, and status-signaling vocabulary.
6. End with a quick reader check: would this help someone understand, decide, or act?

## Anti-Slop Rules

- Start concrete before abstract.
- Prefer named actors, systems, and decisions over noun piles.
- Replace generic benefits with the mechanism that produced them.
- Name tradeoffs directly.
- Use examples when a claim would otherwise sound generic.
- Keep the writer's actual voice if it still reads clearly.

## Common Fixes

- "AI-powered insights" -> say what the model does and where it helps
- "robust framework" -> name the checks, components, or boundaries
- "seamless experience" -> describe the flow that got easier
- "unlock value" -> explain what changed for whom
- "best-in-class" -> remove unless it is proven

## Output Contract

Default to:

1. `Audience`: one sentence
2. `Core message`: one sentence
3. `Rewrite`
4. `Editorial notes`: short bullets only when useful

If the user only wants the improved copy, return the rewrite and omit the notes.

## Reference

Use [references/editorial-principles.md](references/editorial-principles.md) only when the draft needs a deeper pass on lexical register, evidence, or practitioner tone.
