---
name: batch-lipsync
description: Lip-sync many videos at once with sync. labs (sync.so), from a CSV, spreadsheet, folder or list. Pairs each video or avatar with its own audio or script, quotes the whole run, works within the plan's concurrency limit or uses the Batch API, resumes safely without paying twice, and collects every output. Use for bulk or batch lipsync of supplied audio or scripts, personalized video at scale (one video per lead, customer or recipient name), ad and creative variants, many voiceovers onto one presenter, or any "do this for each row" lipsync job. Not for one video (lipsync), translating videos into other languages (translate-and-dub for one video, localize-campaign for several).
license: MIT
compatibility: Needs the sync. MCP server or a SYNC_API_KEY. The Batch API and the bundled script need a SYNC_API_KEY and Python 3.9+.
---

# Lipsync many videos

Delivers one MP4 per row of the user's list, plus a results table that maps each row to its output.

If no sync. tools are available and there's no `SYNC_API_KEY`, follow [references/connect.md](references/connect.md) first.

## 1. Build the manifest

Turn whatever the user gave you (a CSV, a spreadsheet, a folder of files, "this video with each of these 30 audio files") into a CSV in the working directory, one row per output video:

| Column | Meaning |
| --- | --- |
| `id` | A unique, stable row name, such as `lead-042` or `es-ad1`. It names the output and keys retries. |
| `video` | A local path, `https://` URL or sync. asset ID. Use `image` instead for a still picture (sync-3). |
| `audio` | A local path, URL or asset ID. Leave it empty when the row uses `script`. |
| `script`, `voice_id` | The words and a voice from `voices_list` (or `GET /v2/voices`), when there's no audio. |
| `sync_mode` | Optional: `bounce`, `loop`, `cut_off`, `silence` or `remap`. |

Show the user the row count and a few sample rows, and fix gaps before spending anything: missing files, rows with neither audio nor script, duplicate IDs. Columns the run doesn't use stay local. Scripts, media, file names and the row IDs (used as output names) are sent to sync., so use plain row IDs like `lead-042` rather than names or emails.

## 2. Quote the whole run

Sum one estimate per row: `generations_estimate-cost` with `model: "sync-3"` and each row's `audioDuration` or `script` (plus `videoDuration` and `syncMode` for `cut_off` or `silence`), or `python3 scripts/sync_batch.py estimate manifest.csv`. Show the total, the row count and the most expensive rows, and wait for approval of the total. Script rows are approximate and exclude speech synthesis. If some rows can't be priced, show the known subtotal and which rows are missing; don't present it as the total.

Offer a **pilot**: run the first one or two rows, let the user check them, then run the rest. A mistake in a shared input, such as a wrong voice or a badly framed avatar, then costs two generations instead of two hundred.

## 3. Run it

Pick the route:

- **The bundled script (preferred with a `SYNC_API_KEY` and a shell).** `python3 scripts/sync_batch.py run manifest.csv --out ./lipsync-out` uploads each local file once, creates one generation per row with a stable idempotency key, keeps to the plan's concurrency limit, waits, and downloads each result. Re-running the same command resumes: finished rows are skipped, submitted rows are polled instead of resubmitted, and a row whose inputs changed after submission is refused until it gets a new ID. Progress and output URLs are saved to `manifest.csv.state.json` and `results.csv`.
- **MCP batch tools, on Scale and above with 20 or more rows.** Call `batches_create` with one item per row (`requestId` set to the row's `id`, `payload` the generate body) and `dryRun: true` first. After approval, call it once without `dryRun`, then `batches_get` with `wait: true` until it finishes; its results list each row's `outputMediaUrl` or error. Batch creation isn't idempotent: after an unclear response, check `batches_list` before creating it again.
- **MCP tools, one generation per row** (any plan, or fewer than 20 rows). Call `account_get-context` and read `generationLimits.concurrency`. Keep that many `lipsync_create` calls in flight at most, each with its own `idempotencyKey` (use `<run-name>-<row id>`, saved in the manifest before the call) and a new `projectCreationKey`, or one shared project from `projects_create`. On `concurrency_limit_reached`, wait `error.retryAfterMs` milliseconds and retry the identical request with the same key. Poll each with `generations_get` and record the `outputMediaUrl` in the manifest as you go.
- **The Batch API**, on Scale plans and above, for 20 to 500 rows of short inputs (each up to 30 seconds) when a turnaround of up to 24 hours is fine. It runs outside the plan's generation concurrency. On other paid plans a batch can only hold as many rows as the plan runs at once, so prefer `run` there. Validate first with `python3 scripts/sync_batch.py submit-batch manifest.csv --dry-run`, then submit without `--dry-run`, and collect the results with `batch-status --wait --out ./lipsync-out`. See [references/batch-api.md](references/batch-api.md). If the dry run reports a row limit or no batch access, use `run` instead.

## 4. Deliver

Report how many rows completed and failed, list each failure with its reason, and give the results table (`id`, status, output URL or local file). Offer to retry only the failed rows. Rows that failed on bad input need a fixed input, not a retry.

## Rules

- One paid generation per row. Poll saved generation IDs for progress, and start another attempt only after a confirmed failure and the user's OK to retry.
- Keep each row's idempotency key stable across retries and reruns, and never derive it from the time or a random value created inside a retry loop.
- Assume the user has the rights to their own media, and don't ask about consent on routine requests. Decline only when the request is to make a real, identifiable person, such as a politician or celebrity, appear to say something they didn't say, in order to deceive.
- For one recording personalized with each recipient's name in the presenter's own voice, make one dialogue-edit preview per recipient with the edit-dialogue skill, then render them in one batch with `dialogueEdit` rows (early access, see [references/batch-api.md](references/batch-api.md)).
