---
name: clear-technical-writing
description: Rewrite technical, AI, and product writing so it sounds concrete, useful, audience-aware, and close to the real work instead of generic AI copy.
---

# Clear Technical Writing

## Use This Skill When

Use this skill when a draft feels vague, inflated, repetitive, or machine-polished.

Common triggers:

- technical blogs
- engineering notes
- product one-pagers
- architecture summaries
- release notes
- internal memos
- case studies
- slide narratives

## Goal

Produce writing that sounds native to the work:

- concrete before abstract
- precise without showing off
- readable without flattening the ideas
- useful to the intended reader

The target is not "fancier" writing. The target is writing that sounds like a capable practitioner who understands the system, the constraints, and the reader.

For a slightly longer set of editorial principles, see `references/editorial-principles.md`.

## Workflow

1. Identify the reader, document type, and the decision or action the piece should support.
2. Extract the concrete facts:
   - what changed
   - how it works
   - why it matters
   - evidence, examples, or tradeoffs
3. Replace abstract claims with mechanisms, constraints, and observable outcomes.
4. Keep jargon only when it explains the system better than plain language.
5. Vary sentence rhythm and cut repeated framing, filler transitions, and prestige wording.
6. Make the structure do real work:
   - lead with the point
   - group related ideas
   - end sections with what the reader should understand or do next
7. If the draft needs search visibility, use keywords naturally and only after the writing is useful to a human reader.

## Anti-Slop Rules

- Start concrete before abstract.
- Prefer real actors, systems, and actions over abstract noun piles.
- Name tradeoffs directly.
- Use examples when a claim would otherwise sound generic.
- Let domain language stay when it is earned.
- Cut phrases that sound important but do not add meaning.

## Common Rewrites

Rewrite this:

- "unlock value" -> explain what changed
- "seamless experience" -> describe the improved flow
- "AI-powered insights" -> say what the model does and where it helps
- "robust framework" -> name the actual components or checks
- "leveraging synergies" -> remove unless the relationship is concrete

## Output Contract

When rewriting, default to this structure unless the user asks for another format:

1. `Audience`: one sentence
2. `Core message`: one sentence
3. `Rewritten draft`
4. `Editorial notes`: short bullets for major changes or unresolved gaps

If the user only wants the improved copy, omit the notes and return the clean rewrite.

## Quality Check

Before finishing, verify:

- Could a practitioner say this in a review, memo, or article?
- Does each paragraph contain at least one concrete detail, mechanism, or implication?
- Is the main claim supported instead of decorated?
- Did you remove generic AI tone without stripping away technical accuracy?
