# talking-photo

## What it does

`talking-photo` turns a still image into a talking video. Give it a photo, a headshot or an illustrated character, plus either a script or a recording, and it returns an MP4 of that face speaking. The video is as long as the speech.

If you don't have a picture yet and your agent can generate images, it offers to make one that works well: one clear face, looking at the camera, head and shoulders.

## When to reach for it

| What you have | Reach for |
| --- | --- |
| A photo, portrait or illustrated character | `talking-photo` |
| A video of a real person | [lipsync](lipsync.md) |
| A generated video clip | [ai-video-to-talking](ai-video-to-talking.md) |

## Try

- "Make our CEO headshot say: welcome to Acme, we're glad you're here"
- "Create a friendly cartoon barista and make her say good morning"
- "Make ./portrait.png say what's in ./greeting.mp3"

## What you need

- The sync. MCP server connected, or `SYNC_API_KEY` set.
- An image with one clear human or human-like face. Animals and non-humanoid characters aren't supported.
- A script, or an audio file, URL or sync. asset.

## Common questions

**Can it pick the voice for me?**
Yes. It lists the voices on your account and suggests two or three that fit the character. Say "pick one yourself" and it chooses.

**Why is the quote "approximate"?**
For a script, the length of the speech is estimated from the word count until it's spoken. Speech synthesis is billed separately from the lipsync, and the agent says so.

**My picture was rejected.**
sync. needs one clear face at a reasonable size. Group photos, tiny faces and side profiles are the usual causes. The agent explains which, and suggests a tighter head-and-shoulders crop.

**Can I make a celebrity say something?**
No. The skill declines to put words in a real, identifiable person's mouth to deceive. Your own photos, your team (with their OK) and fictional characters are fine.

## It's working if

- The agent picks a voice from your account's list, not a made-up ID.
- You see the quote before the video is created.
- The output is one MP4 of the face speaking your exact words.
