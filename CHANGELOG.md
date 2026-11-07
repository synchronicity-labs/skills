# Changelog

## Unreleased

- Skills, shared references and eval mocks use the sync. MCP server's `<noun>_<verb>` tool names (mcp-server#148): `lipsync_create`, `generations_get`, `generations_estimate-cost`, `account_get-context`, `dubbing_create`, `voices_list`, `models_list` and the rest. The old names stay callable on the server for a deprecation period, but clients list only the new ones.
- Several independent jobs start together with the MCP server's `jobs_create-many` and are followed with `jobs_get-many` (mcp-server#164), on any paid plan, after one quote and one approval for the whole set: `batch-lipsync` (one `lipsync_create` item per row), `translate-and-dub` (one `dubbing_create` item per language), `localize-campaign` (the versions after the pilot) and `edit-dialogue` (one preview, then one video, per variant). Where those tools aren't listed, as in the ChatGPT app, the skills keep starting one job at a time within the plan's concurrency, and `batch-lipsync` keeps its bundled script.
- The Batch API is described as Scale plans and above only, again: a queued pipeline for large runs (20 to 500 rows of up to 30 seconds each) that can wait hours, not a faster way to send a few generations. Below Scale, `POST /v2/batch` answers `402 plan_feature_unavailable`. The note about credits reserved for every row at submit is gone. Edit Dialogue renders no longer go through `batch-lipsync` by default.
- `sync_batch.py submit-batch` explains a `402` as a plan without batch access, points to `run`, and leaves the rows free for `run` instead of marking the submission as unconfirmed.
- Eval mocks list `jobs_create-many` and `jobs_get-many`. The new `batch-mcp-jobs-many` case checks that three rows start with one `jobs_create-many` call, and `batch-mcp-three-rows` still checks one `lipsync_create` per row when the tool isn't listed.
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
