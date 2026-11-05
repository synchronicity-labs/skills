# Changelog

## Unreleased

- Skills, shared references and eval mocks use the sync. MCP server's `<noun>_<verb>` tool names (mcp-server#148): `lipsync_create`, `generations_get`, `generations_estimate-cost`, `account_get-context`, `dubbing_create`, `voices_list`, `models_list` and the rest. The old names stay callable on the server for a deprecation period, but clients list only the new ones.
- `scripts/validate.py` recognizes tool names whose noun is hyphenated, such as `translation-previews_get` and `audio-trims_create`, so those are checked against the hosted tool list too.

## 1.0.0

First public release.

- Ten skills: `setup`, `lipsync`, `talking-photo`, `ai-video-to-talking`, `translate-and-dub`, `edit-dialogue`, `localize-campaign`, `batch-lipsync`, `sync-api` and `troubleshoot`. `troubleshoot` is adapted from Noah's work in mcp-server#143.
- One repo for skills.sh, the Claude Code plugin marketplace, Codex and Cursor, wired to the hosted sync. MCP server.
- `batch-lipsync` and `localize-campaign` can use the MCP server's batch tools on Scale plans and above.
- `batch-lipsync` ships `sync_batch.py`: one upload per file, stable idempotency keys, plan-aware concurrency, safe resume, and the Batch API on Scale plans and above.
- `catalog.json`, a generated list of the skills that Studio and the docs read from GitHub.
- `docs/` is the source of the Agent Skills pages on sync.so/docs, with an overview page and Spanish, French, Brazilian Portuguese and German translations that the validator keeps in step with the English pages.
- A `claude plugin eval` suite with MCP mocks, plus tests for the bundled script and the `sync-api` code samples.
