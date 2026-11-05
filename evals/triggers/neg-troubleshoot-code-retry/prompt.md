---
description: "Integration code for 429s goes to sync-api, not troubleshoot."
tags: ["trigger", "negative", "troubleshoot"]
max_turns: 30
timeout_seconds: 420
allowed_tools: ["Skill", "Read", "Glob", "Grep"]
---

write retry logic in our node worker for when sync's /v2/generate returns 429 concurrency_limit_reached
