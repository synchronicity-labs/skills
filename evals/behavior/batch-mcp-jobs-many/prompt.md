---
description: "MCP batch with jobs_create-many listed: one call starts all three rows, then jobs_get-many follows them."
tags: ["behavior", "batch-lipsync"]
max_turns: 60
timeout_seconds: 420
allowed_tools: ["Skill", "Read", "Glob", "Grep", "Bash", "Write", "Edit"]
---

Run every row of manifest.csv through sync lipsync. It's 3 rows, the total is approved. Use the tools you have, there's no API key here.
