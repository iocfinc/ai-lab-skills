# AI Lab Skills

`codex-ai-lab-skills` is a public skills repository for reusable agent workflows that are concise, auditable, and easy to install from GitHub-based skill loaders.

The first release focuses on:

- `clear-technical-writing`: rewrite technical and product writing so it sounds concrete, useful, and close to the work
- `design-thinking-simulation`: run a customer-centric design-thinking exercise from opportunity framing through value propositions and story

## Repository Layout

- `skills/`: public skill folders
- `.codex-plugin/plugin.json`: Codex plugin manifest for local marketplace-style install
- `.agents/plugins/marketplace.json`: local marketplace entrypoint
- `scripts/validate.sh`: structural validation

## Install In Codex

From a Codex session after cloning this repo locally:

```bash
codex plugin marketplace add ./codex-ai-lab-skills
```

Then install **AI Lab Skills** from the local marketplace.

## GitHub Skill Loaders

This repo is also structured for GitHub-based skill installers that expect standalone skill folders under `skills/<skill-name>/SKILL.md`.

Current public skill slugs:

- `clear-technical-writing`
- `design-thinking-simulation`

## Skill Notes

### `clear-technical-writing`

Derived from an internal anti-slop editorial draft and refined into a public-safe writing skill. It is aimed at technical blogs, product notes, engineering updates, internal docs, and similar writing that should sound like it came from a practitioner rather than generic AI copy.

### `design-thinking-simulation`

Derived from a design-thinking simulation brief and packaged as a reusable facilitation skill. It produces structured customer scenarios, empathy maps, insight clusters, HMW prompts, value propositions, and a customer story.

## Publishing Notes

- Keep public skill names neutral and discoverable.
- Add repository topics such as `codex`, `skills`, `agent-skills`, `writing`, and `design-thinking` after pushing to GitHub.
- If you later register this repo with an external skills marketplace, keep the skill slugs stable.

## License

MIT
