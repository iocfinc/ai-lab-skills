---
name: design-thinking-simulation
description: Run a customer-centric design-thinking simulation from opportunity statement through empathy mapping, insight clustering, HMW questions, value propositions, and a customer story.
---

# Design Thinking Simulation

## Use This Skill When

Use this skill when the user needs a structured design-thinking exercise for a product, service, or workflow idea.

Common triggers:

- "simulate design thinking for this product"
- "give me customer scenarios"
- "build empathy maps and HMW prompts"
- "turn this concept into value propositions"

## Default Scope

Unless the user specifies otherwise, produce:

- 3 customer scenarios
- 10 insights per scenario
- 3 higher-level insight clusters per scenario
- 10 "How Might We" questions per scenario
- 5 value propositions per scenario
- 1 customer story per scenario

If the request is narrower, scale down cleanly instead of forcing the full packet.

## Workflow

### 1. Frame the Opportunity

Start with an opportunity statement that includes:

- business context
- improvement opportunity
- opportunity size: large, mid-sized, or small

If the source material is thin, state the assumptions clearly.

### 2. Observe Before Solving

Build an empathy map for the target customer before brainstorming solutions.

Cover:

- what they see
- what they hear
- pains
- what they think and feel
- what they say and do
- gains

Do not jump to product ideas until the customer situation is concrete.

### 3. Generate Insights

Write at least 10 point-of-view insights per scenario.

Strong insights should connect:

- a concrete behavior or friction
- the hidden reason behind it
- the implication for product or service design

Then cluster them into 3 higher-level insights.

### 4. Create HMW Prompts

Generate 10 "How Might We" questions that vary in angle.

Use a mix of:

- amplify what already works
- remove the bad
- challenge an assumption
- explore the opposite
- identify overlooked resources
- borrow from another domain

### 5. Create Value Propositions

Produce 5 candidate value propositions that respond to the insight clusters.

Each should be concrete enough to imagine as a product or feature direction, not just a slogan.

### 6. Write the Customer Story

Use the most relevant value proposition and the empathy-map context to write a short customer story.

Include:

- the target customer as the central character
- their starting situation
- what they want
- how they encounter the solution
- what improves
- how their social or professional position is strengthened

Also name 3 aspects of why the outcome matters socially for that customer group.

## Output Structure

Default to this structure:

1. `Opportunity Statement`
2. `Scenario 1`
3. `Scenario 2`
4. `Scenario 3`

Within each scenario, use:

- `Persona`
- `Empathy Map`
- `Insights`
- `Higher-Level Insight Clusters`
- `How Might We Questions`
- `Value Propositions`
- `Customer Story`

## Guardrails

- Label assumptions instead of pretending they are research facts.
- Keep personas specific enough to feel real.
- Avoid generic innovation language.
- Do not confuse "customer pain" with "feature request."
- Make the value propositions respond to the insights, not float above them.
