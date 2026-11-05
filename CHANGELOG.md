# Changelog

## 1.0.0

First public release.

- Ten skills: `setup`, `lipsync`, `talking-photo`, `ai-video-to-talking`, `translate-and-dub`, `edit-dialogue`, `localize-campaign`, `batch-lipsync`, `sync-api` and `troubleshoot`. `troubleshoot` is adapted from Noah's work in mcp-server#143.
- One repo for skills.sh, the Claude Code plugin marketplace, Codex and Cursor, wired to the hosted sync. MCP server.
- `batch-lipsync` and `localize-campaign` can use the MCP server's batch tools on Scale plans and above.
- `batch-lipsync` ships `sync_batch.py`: one upload per file, stable idempotency keys, plan-aware concurrency, safe resume, and the Batch API on Scale plans and above.
- `catalog.json`, a generated list of the skills that Studio and the docs read from GitHub.
- A `claude plugin eval` suite with MCP mocks, plus tests for the bundled script and the `sync-api` code samples.
