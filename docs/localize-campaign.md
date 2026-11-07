---
title: "localize-campaign skill"
subtitle: "Localize a set of videos across markets: plan, pilot, run, review sheet."
description: "The sync. labs localize-campaign agent skill produces every video in a campaign, course or product set in every target language: it maps markets to languages, quotes the matrix, pilots one version, then runs the rest with a review sheet."
og:description: "Localize several videos into several languages from your agent, with a pilot first and a review sheet at the end."
---

# localize-campaign

> [!TIP]
> Install this skill with `npx skills add synchronicity-labs/skills --skill localize-campaign`, or get every skill with the Claude Code plugin. See [Agent skills](overview.md).

## What it does

`localize-campaign` takes a set of videos, such as a campaign's ads, a course or product videos, and produces every one of them in every target language. It maps your markets to languages, lays out the video by language matrix, quotes the whole thing, pilots one version so names and terms get checked early, then runs the rest. You get consistently named files and a `review.csv` that regional teams can sign off from.

## When to reach for it

| What you have | Reach for |
| --- | --- |
| Several videos, several markets or languages | `localize-campaign` |
| One video into a few languages | [translate-and-dub](translate-and-dub.md) |
| Many videos with new speech in the same language | [batch-lipsync](batch-lipsync.md) |

## Try

- "We launch in DACH, Brazil and Japan next month. Localize these three ads."
- "Make our five onboarding videos in Spanish, French and Italian"

## What you need

- The sync. MCP server connected, or `SYNC_API_KEY` set. The [setup](setup.md) skill walks you through either.
- The source videos, each with its original speech.

## Common questions

**I gave it markets, not languages.**
That's expected. The agent maps them (DACH to German, Brazil to Portuguese, Japan to Japanese) and asks you to confirm before quoting.

**Why a pilot first?**
A mistranslated product name or slogan would otherwise repeat across every version. One version, checked by you or a native speaker, catches it for the price of one dub.

**What doesn't change?**
On-screen text, burned-in captions, logos and end cards stay in the source language. The agent tells you up front so nobody is surprised in review.

**What are the files called?**
`<campaign>_<video>_<lang>.mp4` by default, for example `spring24_hero-30s_de.mp4`. Agree another pattern before the run if you need one.

**Can it run as one batch?**
It doesn't need to. After the pilot, the rest of the versions start together, up to your plan's limit, with one `jobs_create-many` call through the MCP server on any paid plan. On Scale plans and above, a large run of 20 or more short versions that can wait hours can also go through the Batch API, a queued pipeline whose results can take up to a day.

**The run was interrupted.**
Each version has its own saved key and generation ID, so resuming picks up where it stopped without paying twice.

## It's working if

- You confirm the market to language mapping and the matrix before any cost.
- The pilot comes back before the rest is started.
- You end with one file per video and language, plus a review sheet.
