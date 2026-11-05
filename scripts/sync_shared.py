#!/usr/bin/env python3
"""Copy shared reference files into each skill that uses them.

Skills install one at a time (`npx skills add ... --skill lipsync` copies only that folder),
so every skill carries its own copy. Edit the file in shared/, then run this script.

  python3 scripts/sync_shared.py          # write the copies
  python3 scripts/sync_shared.py --check  # fail if any copy is stale (CI)
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# shared file -> skills that ship a copy in references/
USES = {
    "connect.md": ["setup", "lipsync", "talking-photo", "translate-and-dub", "edit-dialogue",
                   "ai-video-to-talking", "batch-lipsync", "localize-campaign"],
    "media-input.md": ["lipsync", "talking-photo", "translate-and-dub", "edit-dialogue",
                       "ai-video-to-talking", "batch-lipsync", "localize-campaign"],
    "api.md": ["lipsync", "talking-photo", "translate-and-dub", "ai-video-to-talking",
               "localize-campaign", "sync-api"],
    "batch-api.md": ["batch-lipsync", "sync-api"],
}
HEADER = "<!-- Generated from shared/{name} by scripts/sync_shared.py. Edit the shared file, not this copy. -->\n\n"


def main() -> int:
    check = "--check" in sys.argv
    stale = []
    for name, skills in USES.items():
        body = HEADER.format(name=name) + (ROOT / "shared" / name).read_text()
        for skill in skills:
            target = ROOT / "skills" / skill / "references" / name
            if target.exists() and target.read_text() == body:
                continue
            if check:
                stale.append(str(target.relative_to(ROOT)))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(body)
                print(f"wrote {target.relative_to(ROOT)}")
    if stale:
        print("Stale shared copies; run python3 scripts/sync_shared.py:\n  " + "\n  ".join(stale))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
