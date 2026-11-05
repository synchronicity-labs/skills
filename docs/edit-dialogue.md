---
title: "edit-dialogue skill"
subtitle: "Change or remove a few spoken words in the speaker's own voice."
description: "The sync. labs edit-dialogue agent skill fixes a few spoken words in a single-speaker video without a reshoot: it transcribes, previews the new words in the speaker's own voice, then re-syncs the lips on just that part."
og:description: "Fix a wrong price, name, date or word in a video, in the speaker's own voice, without a reshoot."
---

# edit-dialogue

> [!TIP]
> Install this skill with `npx skills add synchronicity-labs/skills --skill edit-dialogue`, or get every skill with the Claude Code plugin. See [Agent skills](overview.md).

## What it does

`edit-dialogue` fixes a few spoken words in a video without a reshoot. It transcribes the video, maps your fix to the exact words, synthesizes the new words in the speaker's own voice, lets you hear a preview, then re-syncs the lips on just that part. Everything else keeps the original picture and sound.

## When to reach for it

| What you have | Reach for |
| --- | --- |
| A wrong price, name, date or word, or a filler to cut | `edit-dialogue` |
| A whole new script | [lipsync](lipsync.md) with a chosen voice |
| The same video in another language | [translate-and-dub](translate-and-dub.md) |
| One recording personalized per recipient | `edit-dialogue` for the previews, then [batch-lipsync](batch-lipsync.md) |

## Try

- "In ./promo.mp4 I say $39 a month. It's $49 now, fix just that."
- "Cut the 'um' after 'billed yearly' in this video"
- "The name should be Siobhan, not Shannon"

## What you need

- The sync. MCP server connected. The [setup](setup.md) skill walks you through it. The REST version of this workflow is in early access; see [Transcription and Dialogue Editing](https://sync.so/docs/developer-guides/dialogue-editing).
- A video with one speaker, up to 10 minutes.

## Common questions

**Why does it show me the transcript?**
So you can both point at the same words. Every change and removal is tied to a word in the transcript, which keeps the edit exact.

**Does the preview cost money?**
It can. The preview clones the speaker's voice and synthesizes the new words, so the agent mentions it when confirming the edits. The final video is quoted separately before it's created.

**A name came out wrong.**
Ask for a pronunciation. The agent adds a respelling like "shivawn", written as a plain word, and makes a new preview.

**Some edits failed.**
Usually the new wording is too long for the gap it fills. The agent says which edits failed and suggests shorter wording.

**Can I replace a whole paragraph?**
This workflow is for targeted words. For a new script, lipsync with a voice is the better tool, and the agent will say so.

## It's working if

- The preview audio has only your words changed.
- You approve the preview and the cost before the video is made.
- The output plays the original video with just those words different.
