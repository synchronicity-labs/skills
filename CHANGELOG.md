# Changelog

## 1.0.0

First public release.

- Nine skills: `setup`, `lipsync`, `talking-photo`, `ai-video-to-talking`, `translate-and-dub`, `edit-dialogue`, `localize-campaign`, `batch-lipsync` and `sync-api`.
- One repo for skills.sh, the Claude Code plugin marketplace, Codex and Cursor, wired to the hosted sync. MCP server.
- `batch-lipsync` ships `sync_batch.py`: one upload per file, stable idempotency keys, plan-aware concurrency, safe resume, and the Batch API on Scale plans and above.
- A `claude plugin eval` suite with MCP mocks, plus tests for the bundled script and the `sync-api` code samples.
