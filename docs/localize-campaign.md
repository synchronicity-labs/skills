# localize-campaign

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

- The sync. MCP server connected, or `SYNC_API_KEY` set.
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
On Scale plans and above, 20 or more versions can go in one batch through the MCP server's batch tools. Below that, versions run side by side up to your plan's limit.

**The run was interrupted.**
Each version has its own saved key and generation ID, so resuming picks up where it stopped without paying twice.

## It's working if

- You confirm the market to language mapping and the matrix before any cost.
- The pilot comes back before the rest is started.
- You end with one file per video and language, plus a review sheet.
