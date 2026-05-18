#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        fail(f"cannot parse {path}: {exc}")


def validate_skill(skill_dir: Path) -> None:
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.exists():
        fail(f"missing {skill_path}")

    text = skill_path.read_text()
    if not text.startswith("---\n"):
        fail(f"{skill_path} missing YAML frontmatter")
    try:
        _, frontmatter, _ = text.split("---\n", 2)
    except ValueError:
        fail(f"{skill_path} has malformed frontmatter delimiters")

    if "\nname:" not in f"\n{frontmatter}":
        fail(f"{skill_path} frontmatter missing name")
    if "\ndescription:" not in f"\n{frontmatter}":
        fail(f"{skill_path} frontmatter missing description")


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    plugin_path = repo_root / ".codex-plugin" / "plugin.json"
    marketplace_path = repo_root / ".agents" / "plugins" / "marketplace.json"
    skills_root = repo_root / "skills"

    if not plugin_path.exists():
        fail(f"missing {plugin_path}")
    if not marketplace_path.exists():
        fail(f"missing {marketplace_path}")
    if not skills_root.exists():
        fail(f"missing {skills_root}")

    plugin = load_json(plugin_path)
    marketplace = load_json(marketplace_path)

    if plugin.get("name") != "codex-ai-lab-skills":
        fail("plugin.json name must be codex-ai-lab-skills")
    if plugin.get("skills") != "./skills/":
        fail("plugin.json skills path must be ./skills/")

    plugins = marketplace.get("plugins", [])
    if len(plugins) != 1:
        fail("marketplace.json must expose exactly one plugin")
    path = plugins[0].get("source", {}).get("path")
    if path != ".":
        fail("marketplace.json local source path must be .")

    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("skills/ must contain at least one skill directory")

    for skill_dir in skill_dirs:
        validate_skill(skill_dir)

    print(f"Validated {len(skill_dirs)} skills in {repo_root}")


if __name__ == "__main__":
    main()
