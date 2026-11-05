# translate-and-dub

## What it does

`translate-and-dub` translates the speech in one video into other languages and re-syncs the speaker's lips to the dubbed audio. You get one MP4 per language, labelled with its language. It works from a local file, a public URL, or a YouTube, TikTok, Instagram or Facebook link.

## When to reach for it

| What you have | Reach for |
| --- | --- |
| One video, one or more languages | `translate-and-dub` |
| Several videos for several markets | [localize-campaign](localize-campaign.md) |
| A video and your own translated audio | [lipsync](lipsync.md) |
| Subtitles only | Not a sync. job |

## Try

- "Dub this YouTube video into Spanish and Brazilian Portuguese"
- "Translate ./keynote.mp4 into Japanese"
- "Make a German version of https://example.com/demo.mp4"

## What you need

- The sync. MCP server connected, or `SYNC_API_KEY` set.
- A video with its original speech on the audio track.

## Common questions

**Which languages are supported?**
The agent checks the live list before quoting. If a language isn't there, it names the closest one that is.

**How is it priced?**
By the length of the source video, once per language. The quote shows the breakdown per language and the total. If external voice-provider charges are excluded, the agent says so.

**Is on-screen text translated?**
No. Titles, captions and logos stay as they are. Only the speech changes.

**One language failed.**
Each language is its own job, so the others still finish. The agent reports which one failed and why.

**Dubbing failed with a voice-provider error.**
If you connected your own ElevenLabs key to sync., that key's credits or validity are the usual cause.

**It wouldn't dub a music video.**
Copyrighted songs and music videos need the rights holder's permission. Use a video you own or are licensed to localize.

## It's working if

- The languages are checked before the quote.
- There's one paid job per language, never a resubmit to check progress.
- Each output link is labelled with its language.
