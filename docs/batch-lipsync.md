---
title: "batch-lipsync skill"
subtitle: "Lip-sync every row of a CSV or folder, resumably, within your plan's limits or through the Batch API."
description: "The sync. labs batch-lipsync agent skill lip-syncs many videos in one go from a CSV, spreadsheet, folder or list: it quotes the whole run, offers a pilot, keeps to your plan's concurrency and resumes without paying twice."
og:subtitle: "Lip-sync every row of a CSV or folder, resumably."
og:description: "Lip-sync every row of a CSV or folder from your agent, resumably, within your plan's limits or through the Batch API."
---

# batch-lipsync

> [!TIP]
> Install this skill with `npx skills add synchronicity-labs/skills --skill batch-lipsync`, or get every skill with the Claude Code plugin. See [Agent skills](overview.md).

## What it does

`batch-lipsync` lip-syncs many videos in one go: one output per row of a CSV, a spreadsheet, a folder, or a list like "this presenter with each of these 40 audio files". It builds a manifest, quotes the whole run, offers a pilot, then runs every row within your plan's limits and collects the outputs into a results table.

With an API key it uses a bundled script, `sync_batch.py`, that uploads each file once, keeps to your plan's concurrency, resumes after an interruption, and downloads every result. On Scale plans and above, 20 or more rows can go through the [Batch API](https://sync.so/docs/api-reference/guides/batch-processing) instead, either with the script or straight through the MCP server's batch tools.

## When to reach for it

| What you have | Reach for |
| --- | --- |
| Many rows of video plus audio or script | `batch-lipsync` |
| Personalized video per lead or customer | `batch-lipsync` |
| One recording personalized with each recipient's name in the same voice | [edit-dialogue](edit-dialogue.md) previews, then `batch-lipsync` |
| Several videos into other languages | [localize-campaign](localize-campaign.md) |
| One video | [lipsync](lipsync.md) |

## Try

- "Lipsync each row of leads.csv onto presenter.mp4"
- "Make a version of this ad for each of these 12 voiceovers"
- "Run manifest.csv through sync, the total is approved"

## What you need

- The sync. MCP server connected, or `SYNC_API_KEY` and Python 3.9 or later for the script. The [setup](setup.md) skill walks you through either.
- A list where every row has a video or image, and audio or a script with a voice.

## Common questions

**Why does it want a pilot?**
If a shared input is wrong, like the voice or the presenter's framing, a pilot costs two generations instead of two hundred.

**What leaves my machine?**
The media, the scripts, file names and the row IDs (used as output names). Columns the run doesn't use stay local, so keep names and emails out of the row IDs.

**It stopped halfway.**
Run the same command again. Finished rows are skipped, submitted rows are polled instead of resubmitted, and nothing already paid for is paid for again.

**I changed a row after it ran.**
The script refuses to reuse that row's result. Give the changed row a new ID, which makes it a new generation.

**Should I use the Batch API?**
On Scale and above, for 20 to 500 short rows when a turnaround of up to 24 hours is fine. On other paid plans a batch can only hold as many rows as the plan runs at once, so the regular run is just as fast.

**Some rows failed.**
The results table lists each failure with its reason. Rows that failed on bad input need a fixed input. Retry the rest with `--retry-failed`.

## It's working if

- The quote covers every row, or tells you which rows it couldn't price.
- No more generations run at once than your plan allows.
- Rerunning a finished manifest creates nothing new.
