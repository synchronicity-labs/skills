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
- docs/ has a page per skill plus overview.md, each with title, subtitle, description and
  og:description front matter, links only to other pages (name.md) or absolute URLs, and no
  <, { or } outside code. Every page has a translation in docs/i18n/<locale>/ for each of LOCALES
  whose `source-sha256` is the sha256 of the English page it was translated from, with the same
  headings, questions and table rows.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Languages sync.so/docs serves (synchronicity-labs/sync-fern fern/docs.yml `translations`).
LOCALES = ["es", "fr", "pt-BR", "de"]
DOC_FIELDS = ("title", "subtitle", "description", "og:description")
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


def doc_frontmatter(path: Path, errors: list) -> dict:
    """Front matter of a docs page. Keys may contain ':' (og:description), so split on the first ': '."""
    rel = path.relative_to(ROOT)
    match = re.match(r"^---\n(.*?)\n---\n", path.read_text(), re.S)
    if not match:
        errors.append(f"{rel}: missing front matter")
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^([a-z][a-z0-9:-]*?): (.*)$", line)
        if not field:
            errors.append(f"{rel}: front matter line {line!r} isn't `key: value`")
            continue
        key, value = field.group(1), field.group(2).strip()
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except ValueError:
                errors.append(f"{rel}: front matter `{key}` isn't a valid double-quoted string")
        elif value.startswith("'"):
            value = value[1:-1].replace("''", "'")
        elif ": " in value or " #" in value:
            errors.append(f"{rel}: front matter `{key}` has an unquoted ': ' or ' #'; quote the value")
        fields[key] = value
    return fields


def doc_body_checks(path: Path, pages: set, errors: list) -> None:
    """Keep pages convertible to Fern MDX by synchronicity-labs/sync-fern's scripts/sync-agent-skills.mjs."""
    rel = path.relative_to(ROOT)
    text = re.sub(r"^---\n.*?\n---\n", "", path.read_text(), flags=re.S)
    text = re.sub(r"^\s*(```|~~~).*?^\s*\1\s*$", "", text, flags=re.S | re.M)
    for line in text.splitlines():
        if line.startswith("<!--"):
            continue
        prose = re.sub(r"`+[^`]*`+", "", line)
        if re.search(r"[<{}]", prose):
            errors.append(f"{rel}: {line.strip()[:60]!r} has <, {{ or }} outside code, which the docs site reads as JSX")
        for target in re.findall(r"\]\(([^)\s]+)\)", prose):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            page = re.match(r"^([a-z0-9-]+)\.md(#.*)?$", target)
            if not page or page.group(1) not in pages:
                errors.append(f"{rel}: link {target} must be another docs page (name.md) or an absolute URL")


def section_shape(path: Path) -> tuple:
    text = path.read_text()
    return (len(re.findall(r"^## ", text, re.M)), len(re.findall(r"^\*\*.+\*\*$", text, re.M)),
            len(re.findall(r"^\|", text, re.M)))


def validate_docs(names: set) -> list:
    errors = []
    docs = ROOT / "docs"
    pages = {p.stem for p in docs.glob("*.md")}
    expected = names | {"overview"}
    for extra in sorted(pages - expected):
        errors.append(f"docs/{extra}.md: not a skill or the overview; the docs site publishes every page in docs/")
    for page in sorted(pages):
        fields = doc_frontmatter(docs / f"{page}.md", errors)
        for key in DOC_FIELDS:
            if not fields.get(key):
                errors.append(f"docs/{page}.md: front matter needs `{key}`")
        doc_body_checks(docs / f"{page}.md", pages, errors)
    overview = (docs / "overview.md").read_text() if "overview" in pages else ""
    for name in sorted(names):
        if f"]({name}.md)" not in overview:
            errors.append(f"docs/overview.md: skill {name} isn't in the skills table")
    labels = json.loads((docs / "meta.json").read_text()) if (docs / "meta.json").exists() else {}
    if set(labels) != {"section", "overview"}:
        errors.append("docs/meta.json: needs exactly `section` and `overview` navigation labels")

    for locale_dir in sorted(p for p in (docs / "i18n").glob("*") if p.is_dir()):
        if locale_dir.name not in LOCALES:
            errors.append(f"{locale_dir.relative_to(ROOT)}: unknown locale; the docs site serves {', '.join(LOCALES)}")
    for locale in LOCALES:
        loc = docs / "i18n" / locale
        meta = loc / "meta.json"
        if not meta.exists() or set(json.loads(meta.read_text())) != set(labels):
            errors.append(f"{meta.relative_to(ROOT)}: needs the same keys as docs/meta.json")
        for stray in sorted({p.stem for p in loc.glob("*.md")} - pages):
            errors.append(f"docs/i18n/{locale}/{stray}.md: translates a page that docs/{stray}.md doesn't have")
        for page in sorted(pages):
            path = loc / f"{page}.md"
            rel = f"docs/i18n/{locale}/{page}.md"
            if not path.exists():
                errors.append(f"{rel}: missing translation of docs/{page}.md")
                continue
            fields = doc_frontmatter(path, errors)
            for key in DOC_FIELDS:
                if not fields.get(key):
                    errors.append(f"{rel}: front matter needs `{key}`")
            source = hashlib.sha256((docs / f"{page}.md").read_bytes()).hexdigest()
            if fields.get("source-sha256") != source:
                errors.append(f"{rel}: stale; docs/{page}.md changed since it was translated. Update the translation, "
                              f"then set `source-sha256: {source}`")
            if section_shape(path) != section_shape(docs / f"{page}.md"):
                errors.append(f"{rel}: headings, questions or table rows don't match docs/{page}.md")
            doc_body_checks(path, pages, errors)
    return errors


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
    errors += validate_docs(names)

    # skills.sh groups the repo page by skills.sh.json; every skill should appear exactly once.
    groups = json.loads((ROOT / "skills.sh.json").read_text()).get("groupings", [])
    grouped = [s for g in groups for s in g.get("skills", [])]
    for name in sorted(names):
        if grouped.count(name) != 1:
            errors.append(f"skills.sh.json: skill {name} must appear in exactly one grouping (found {grouped.count(name)})")
    for name in set(grouped) - names:
        errors.append(f"skills.sh.json: unknown skill {name}")

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
