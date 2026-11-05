# lipsync

## What it does

`lipsync` takes a video of someone talking and makes their mouth match new speech. The speech can be a voiceover, a re-recorded take, a song, or a script that sync. voices for you. You get one MP4 back, with the original picture and the new audio.

Before anything is charged, the agent saves your files to sync., works out how long the speech is, quotes the cost, and waits for you to say go.

## When to reach for it

Use it when you already have footage of a real person and want them to say something else.

| What you have | Reach for |
| --- | --- |
| A video and new audio, or a video and a script | `lipsync` |
| A clip from Veo, Kling, Sora or another generator | [ai-video-to-talking](ai-video-to-talking.md) |
| A still photo or illustration | [talking-photo](talking-photo.md) |
| A video that should speak another language | [translate-and-dub](translate-and-dub.md) |
| One or two wrong words in an otherwise good take | [edit-dialogue](edit-dialogue.md) |
| Dozens of videos or audio files | [batch-lipsync](batch-lipsync.md) |

## Try

- "Lipsync ./interview.mp4 to ./new-take.wav"
- "Make the guy in https://example.com/talk.mp4 say what's in this mp3"
- "Sync my music video ./take3.mov to the final mix"

## What you need

- The sync. MCP server connected, or `SYNC_API_KEY` set. The [setup](setup.md) skill walks you through either.
- The video as a local file, a public URL, a sync. asset ID, or a YouTube, TikTok, Instagram or Facebook link.
- The speech as audio, or as a script plus a voice.

## Common questions

**Why did it stop and ask me before making the video?**
Every generation is billed, so the skill always shows the estimate first and waits for approval. Say "go ahead, anything under $5 is fine" up front and it won't stop twice.

**My audio is longer than my video. What happens?**
The agent asks which sync mode you want: play the video forward and back (`bounce`, the default), loop it, cut the speech when the video ends, keep the video going silently, or speed the video up or down to fit (`remap`).

**There are two people in the shot.**
The agent asks who should speak and points sync. at that face. Without that, sync. picks the active speaker itself.

**It refused to upload my file.**
It checks that the file really is media before spending anything. A file that isn't video or audio, or an upload address that isn't sync.'s own, stops the run with an explanation. Nothing is charged.

**Which model does it use?**
`sync-3`, the most capable model, unless you ask for another. The list comes from your account, not from the skill.

**Where's my video?**
The agent gives you the exact output link. In a coding agent it offers to download the file next to your source.

## It's working if

- You see a quote before any generation starts.
- Local files are uploaded once, and a retry reuses the same upload.
- The final message has a link that plays your video with the new speech.
