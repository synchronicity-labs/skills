#!/usr/bin/env python3
"""Validate the skills repo: frontmatter, links, shared copies, manifests and MCP tool names.

  python3 scripts/validate.py

Checks:
- Each skills/<dir>/SKILL.md has frontmatter that meets the Agent Skills spec: `name` equals the
  directory name (lowercase letters, digits and single hyphens, at most 64 chars), a
  `description` of at most 1024 chars, and a `compatibility` of at most 500 chars.
- Every relative Markdown link in a skill resolves inside that skill's folder, so a skill
  installed on its own has no broken references.
- Every backticked tool name a skill mentions exists in the hosted server's tool list
  (evals/mocks/sync/_tools.json), apart from the chat-app-only tools listed below.
- Shared copies are current (scripts/sync_shared.py --check).
- The plugin manifests parse, use only known top-level keys, and list only skills that exist.
- No em dashes or en dashes anywhere in the repo's text files.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Tools the hosted server shows only to chat apps with file uploads (ChatGPT, Codex app).
APP_ONLY_TOOLS = {"upload-media"}
TOOL_LIKE = re.compile(r"`((?:[a-z]+_)?[a-z]+(?:-[a-z]+)+|[a-z]+_[a-z]+(?:-[a-z]+)*)`")
NOT_TOOLS = {
    # Backticked values that look like tool names but are field values, workflows or skill names.
    "cut_off", "sync_mode", "translate-and-dub", "edit-dialogue", "talking-photo", "lipsync-video",
    "batch-lipsync", "localize-campaign", "ai-video-to-talking", "sync-api", "lipsync-2", "lipsync-2-pro",
    "sync-3", "react-1", "plan_feature_unavailable", "concurrency_limit_reached", "import_in_progress",
    "import_failed", "import_not_enabled", "import_unavailable", "import_daily_limit_reached",
    "generation_plan_duration_exceeded", "insufficient_credits", "free_tier_generations_exhausted",
    "translate_and_dub", "edit_dialogue", "active_speaker_detection", "auto_detect", "frame_number",
    "dry_run", "webhook_url", "request_id", "output_url", "total_generations", "success_count",
    "failed_count", "pending_count", "max_retries", "additional_headers", "voice_id", "asset_id",
    "lead-042", "es-ad1", "lead-001", "row-name", "x-api-key", "idempotency-key", "sync-signature",
    "sync-delivery-id", "spring24_hero-30s_de",
}


def frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def main() -> int:
    errors = []
    tools = {t["name"] for t in json.loads((ROOT / "evals/mocks/sync/_tools.json").read_text())["tools"]}
    skills = sorted(p.parent for p in (ROOT / "skills").glob("*/SKILL.md"))
    names = {p.name for p in skills}

    for skill in skills:
        rel = skill.relative_to(ROOT)
        text = (skill / "SKILL.md").read_text()
        fm = frontmatter(text)
        name, desc, compat = fm.get("name", ""), fm.get("description", ""), fm.get("compatibility", "")
        if name != skill.name:
            errors.append(f"{rel}: name {name!r} must equal the directory name")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{rel}: name must be lowercase letters, digits and single hyphens, at most 64 chars")
        for key, value in fm.items():
            # Strict YAML parsers (the skills.sh CLI) read an unquoted ": " or " #" as structure, not text.
            if value and value[0] not in "\"'|>" and (": " in value or " #" in value):
                errors.append(f"{rel}: frontmatter `{key}` has an unquoted ': ' or ' #'; reword it or quote the value")
        if not desc or len(desc) > 1024:
            errors.append(f"{rel}: description must be 1-1024 chars (is {len(desc)})")
        if len(compat) > 500:
            errors.append(f"{rel}: compatibility must be at most 500 chars")
        body_lines = text.count("\n")
        if body_lines > 500:
            errors.append(f"{rel}: SKILL.md has {body_lines} lines; keep it under 500 and move detail to references/")

        for md in skill.rglob("*.md"):
            md_text = md.read_text()
            for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", md_text):
                if re.match(r"^[a-z]+://|^mailto:", target):
                    continue
                resolved = (md.parent / target).resolve()
                if not resolved.exists():
                    errors.append(f"{md.relative_to(ROOT)}: broken link {target}")
                elif skill.resolve() not in resolved.parents and resolved != skill.resolve():
                    errors.append(f"{md.relative_to(ROOT)}: link {target} leaves the skill folder")
            for token in TOOL_LIKE.findall(md_text):
                if token in tools or token in APP_ONLY_TOOLS or token in NOT_TOOLS or token in names:
                    continue
                if re.search(r"(assets_|generate_|projects_|voices_|models_)", token) or token.startswith(
                        ("create-", "get-", "estimate-", "upload-", "trim-", "rename-")):
                    errors.append(f"{md.relative_to(ROOT)}: `{token}` is not a tool on the hosted sync. MCP server")

    catalog = subprocess.run([sys.executable, str(ROOT / "scripts/build_catalog.py"), "--check"], capture_output=True, text=True)
    if catalog.returncode:
        errors.append(catalog.stdout.strip() or catalog.stderr.strip())

    shared = subprocess.run([sys.executable, str(ROOT / "scripts/sync_shared.py"), "--check"], capture_output=True, text=True)
    if shared.returncode:
        errors.append(shared.stdout.strip())

    for manifest in [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", ".codex-plugin/plugin.json",
                     ".cursor-plugin/plugin.json", ".mcp.json"]:
        path = ROOT / manifest
        try:
            data = json.loads(path.read_text())
        except (OSError, ValueError) as err:
            errors.append(f"{manifest}: {err}")
            continue
        listed = data.get("skills") if isinstance(data.get("skills"), list) else []
        for plugin in data.get("plugins", []):
            listed += plugin.get("skills", []) if isinstance(plugin.get("skills"), list) else []
        for entry in listed:
            entry_path = entry if isinstance(entry, str) else entry.get("path", "")
            if not (ROOT / entry_path).exists():
                errors.append(f"{manifest}: lists missing skill path {entry_path}")

    # Top-level keys each client accepts (Cursor's schema rejects unknown keys outright).
    known_keys = {
        ".cursor-plugin/plugin.json": {"name", "displayName", "version", "description", "author", "publisher", "homepage",
                                       "repository", "license", "logo", "keywords", "category", "tags", "skills",
                                       "rules", "agents", "commands", "hooks", "mcpServers", "minClientVersions", "variables"},
    }
    for manifest, keys in known_keys.items():
        extra = set(json.loads((ROOT / manifest).read_text())) - keys
        if extra:
            errors.append(f"{manifest}: unknown top-level keys {sorted(extra)}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "results" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".py", ".json", ".yaml", ".yml", ".sh", ".txt", ".csv"}:
            continue
        for n, line in enumerate(path.read_text(errors="ignore").splitlines(), start=1):
            if "\u2014" in line or "\u2013" in line:
                errors.append(f"{path.relative_to(ROOT)}:{n}: em or en dash; use a comma, colon, period or plain hyphen")

    for skill in skills:
        if not (ROOT / "docs" / f"{skill.name}.md").exists():
            errors.append(f"docs/{skill.name}.md: missing guide for skill {skill.name}")
        yaml = skill / "agents" / "openai.yaml"
        if not yaml.exists() or f"${skill.name} " not in yaml.read_text():
            errors.append(f"{yaml.relative_to(ROOT)}: missing, or its default_prompt doesn't name ${skill.name}")
    for page in (ROOT / "docs").glob("*.md"):
        for target in re.findall(r"\]\(([^)#\s]+)\)", page.read_text()):
            if not re.match(r"^[a-z]+://", target) and not (page.parent / target).exists():
                errors.append(f"{page.relative_to(ROOT)}: broken link {target}")

    readme = (ROOT / "README.md").read_text()
    for name in names:
        if f"skills/{name}" not in readme:
            errors.append(f"README.md: skill {name} isn't listed")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"ok: {len(skills)} skills, {len(tools)} hosted tools")
    return 0


if __name__ == "__main__":
    sys.exit(main())
