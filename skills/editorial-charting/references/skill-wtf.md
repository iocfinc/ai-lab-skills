# WTF: Editorial Charting Skill

## Why is the main skill so short?

Skill context is expensive. The main file should tell an agent when to load the skill and where to find details. Examples belong in `scripts/` and reference material belongs in `references/`.

## Why not call this an Economist skill?

The original skill was useful because it taught editorial discipline, not because it needed to copy one publication. The active skill now uses broader data visualization foundations and avoids direct style imitation.

## Why "Bloomberg-inspired" instead of "Bloomberg palette"?

The color system uses high-saturation, attention-forward defaults inspired by Bloomberg-like chart energy. It is not an official Bloomberg style guide and should not be represented as one.

## Why use one hue plus shades?

Many editorial charts need emphasis, not categorical decoration. One hue plus shade levels gives agents a simple hierarchy: context, comparison, secondary emphasis, and main claim.

## Why include BDD for a skill?

Agents forget context and future maintainers change behavior. Human-readable scenarios describe what the skill must keep doing even as files evolve.

## Why include an HTML contact sheet?

Some users need to see the menu of possible chart patterns before choosing one. The contact sheet works like a quick-start page: visual first, low prose, printable, and easy for agents to reference.

## Why does the contact sheet use embedded toy data?

It should open offline and not depend on package installs. The examples are tiny, public toy-dataset-style values inspired by scikit-learn bundled datasets and Matplotlib chart forms.
