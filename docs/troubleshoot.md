---
title: "troubleshoot skill"
subtitle: "Find why a job failed, stalled or was rejected, and resume it without paying twice."
description: "The sync. labs troubleshoot agent skill works out why a sync. job failed, stalled or was rejected, explains the real cause in plain words, picks the work back up without starting a second paid job, and can report the problem to sync."
og:description: "Find out from your agent why a sync. job failed, stalled or was rejected, and resume it without paying twice."
---

# troubleshoot

> [!TIP]
> Install this skill with `npx skills add synchronicity-labs/skills --skill troubleshoot`, or get every skill with the Claude Code plugin. See [Agent skills](overview.md).

## What it does

`troubleshoot` works out why a sync. job failed, stalled or was rejected, tells you the real cause in plain words, and picks the work back up without starting a second paid job. When the problem was a confusing error or a missing feature, it can also send a short report to the sync. team, with no secrets or media attached.

## When to reach for it

| What happened | Reach for |
| --- | --- |
| A job failed, was rejected, or seems stuck | `troubleshoot` |
| A 402, 429 or other sync. error | `troubleshoot` |
| The sync. tools vanished or say you're signed out | `troubleshoot`, which reconnects you the same way as [setup](setup.md) |
| You haven't connected sync. yet | [setup](setup.md) |
| Your own code gets errors from the API | [sync-api](sync-api.md) |

## Try

- "My lipsync failed, why?"
- "This dub has been processing for 20 minutes"
- "I keep getting concurrency_limit_reached"
- "The video came out but the mouth looks off"

## What you need

- The sync. MCP server connected, for reading job status and your account. Without it, the skill can still explain an error message you paste.
- The error text, or the generation or batch ID if you have it.

## Common questions

**Was I charged for the failed job?**
No. Failed generations aren't charged.

**It's still processing. Should I start it again?**
No. Pending isn't failed, and a second job won't finish sooner. The skill keeps checking the same job.

**My request timed out. Did it go through?**
Maybe. The skill looks for the job, or retries the identical request with the same key, which returns the original instead of starting another one.

**The result looks wrong.**
The usual causes are in the source: a turned or covered face, several people in frame, music under the voice, or low resolution. The skill checks those, and suggests `sync-3` if an older model was used. Trying again is a new paid generation, so it quotes first.

**What does the report to sync. include?**
The kind of problem, the exact error, the tool and the job ID. Never your key, signed links, personal data or media.

## It's working if

- You get the actual cause, with the error code when there is one.
- No second paid job starts unless you approve a new attempt.
- The original work resumes from where it stopped.
