---
description: "MCP-only batch without jobs_create-many listed: reads concurrency, one create per row."
tags: ["behavior", "batch-lipsync"]
max_turns: 60
timeout_seconds: 420
allowed_tools: ["Skill", "Read", "Glob", "Grep", "Bash", "Write", "Edit"]
---

Run every row of manifest.csv through sync lipsync. It's 3 rows, the total is approved. Use the tools you have, there's no API key here.
