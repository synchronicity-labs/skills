---
description: "Webhook handler: Sync-Signature, HMAC-SHA256 over raw body, constant-time compare."
tags: ["behavior", "sync-api"]
max_turns: 25
timeout_seconds: 420
allowed_tools: ["Skill", "Read", "Glob", "Grep", "Write", "Edit"]
---

Add a Next.js App Router route at app/api/sync-webhook/route.ts that receives sync.so generation webhooks, verifies them, and logs the generation id and status.
