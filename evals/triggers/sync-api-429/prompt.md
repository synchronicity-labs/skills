---
description: "Debugging an integration: sync-api with correct retry advice."
tags: ["trigger", "sync-api"]
max_turns: 30
timeout_seconds: 420
allowed_tools: ["Skill", "Read", "Glob", "Grep"]
---

our python worker calls sync's generate endpoint and keeps getting 429 concurrency_limit_reached when we push a lot of jobs. whats the right way to handle this
