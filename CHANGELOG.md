# Changelog

## 1.1.0

- New `troubleshoot` skill: diagnoses failed, stalled or rejected work, resumes it without a second paid job, and can send a redacted report with `send-feedback`. Adapted from Noah's work in mcp-server#143.
- `batch-lipsync` and `localize-campaign` can use the MCP server's `batches_create`, `batches_get` and `batches_list` on Scale plans and above.
- `ai-video-to-talking` now treats voice cloning as a one-time, non-idempotent action and checks the voice list before any retry.

## 1.0.0

First public release.

- Nine skills: `setup`, `lipsync`, `talking-photo`, `ai-video-to-talking`, `translate-and-dub`, `edit-dialogue`, `localize-campaign`, `batch-lipsync` and `sync-api`.
- One repo for skills.sh, the Claude Code plugin marketplace, Codex and Cursor, wired to the hosted sync. MCP server.
- `batch-lipsync` ships `sync_batch.py`: one upload per file, stable idempotency keys, plan-aware concurrency, safe resume, and the Batch API on Scale plans and above.
- A `claude plugin eval` suite with MCP mocks, plus tests for the bundled script and the `sync-api` code samples.
