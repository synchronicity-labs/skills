# ai-video-to-talking

## What it does

`ai-video-to-talking` gives dialogue to AI-generated video. Clips from Veo, Kling, Sora, Runway, Hailuo, Luma, Seedance or Wan usually come back silent, or with speech you don't want. This skill writes or takes the line, picks a voice that fits the character, and lip-syncs them so they actually speak.

sync. doesn't generate the video. If you only have an idea, the skill writes a prompt for your video generator that produces a clip that lip-syncs well, then takes over once you have it.

## When to reach for it

| What you have | Reach for |
| --- | --- |
| A generated clip, or an idea for one | `ai-video-to-talking` |
| Real footage and a voiceover | [lipsync](lipsync.md) |
| A still image | [talking-photo](talking-photo.md) |

## Try

- "My Veo clip of a barista has no dialogue. Make her say: morning, oat latte again?"
- "I need a UGC-style ad where a guy holds our energy drink and says it tastes good. I'll make the clip in Kling."
- "This Sora scene has two characters talking. Give them these lines."

## What you need

- The sync. MCP server connected, or `SYNC_API_KEY` set.
- The clip, or access to a video generator.
- The line, or a description of what the character should say.

## Common questions

**What makes a generated clip lip-sync well?**
One character facing the camera, the face filling a good part of the frame, the mouth unobstructed, a steady camera, one continuous shot, and the character already moving like they're talking. The skill's prompt guide covers this, with an example prompt.

**My line is longer than the clip.**
Generated clips are often 5 to 10 seconds, which holds about 12 to 25 words. The skill suggests trimming the line, generating a longer clip, or using a sync mode that extends the video.

**Can it handle two characters or several shots?**
Yes, with the timeline tool. Each line gets its own voice and is placed on the shot where that character speaks. The lines, voices and total cost are agreed before anything is created.

**Can I use my own voice?**
Yes, record it and pass the audio. The skill can also clone a voice, but only when you ask for it and own the sample.

## It's working if

- The character says your exact words, in a voice that suits them.
- Nothing is generated before you approve the line, the voice and the cost.
- For a multi-shot scene, each line lands on the right character.
