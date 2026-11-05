---
name: edit-dialogue
description: Change or remove a few spoken words in a single-speaker video with sync. labs (sync.so), keeping the speaker's own voice and re-syncing the lips, with no reshoot. Use for fixing a misspoken word, a wrong name, number, price or date, a mispronunciation, a typo in a spoken line, or cutting a filler word or phrase. Not for replacing a whole script (lipsync with a new script), translation (translate-and-dub), or switching to a different voice.
license: MIT
compatibility: Needs the sync. MCP server. See references/connect.md.
---

# Fix spoken words

Delivers one MP4 where only the agreed words change. Everything else keeps the original picture and voice.

If no sync. tools are available, follow [references/connect.md](references/connect.md) first. The REST version of this workflow is in early access and needs features enabled per organization; see https://sync.so/docs/developer-guides/dialogue-editing.

## Inputs

- **Video:** one person speaking, up to 10 minutes, as a local file, public URL or sync. video asset ID.
- **The fix:** which words to change or remove, and what to say instead. Never guess the replacement words.

## Tools

| Step | Tool |
| --- | --- |
| Check support | `get-dialogue-options` |
| Create the project | `projects_create` |
| Save the video | `upload-media`, `assets_create-upload-url` + `assets_create` (local files), or `assets_create` (URLs) |
| Transcribe | `create-dialogue-transcription`, `get-dialogue-transcription` |
| Preview the new audio | `create-dialogue-preview`, `get-dialogue-preview` |
| Quote | `estimate-dialogue-video` |
| Create | `create-dialogue-video` |
| Wait | `generate_get-generation` |

## Steps

1. **Support.** Call `get-dialogue-options`. If Edit Dialogue isn't available for this account, say so and stop. Note whether it reports `keyedPreview`.
2. **Project.** Call `projects_create` with a new random UUID as `id`, a short `name` and `defaultWorkflow: "edit_dialogue"`. Save the returned `id` as `projectId`. Pass it wherever a tool asks for `projectId`, and add `projectIntent: "explicit"` only on tools that take that field.
3. **Save the video** into that project. Follow [references/media-input.md](references/media-input.md).
4. **Transcribe.** Call `create-dialogue-transcription` with the `projectId` and `videoAssetId`, then `get-dialogue-transcription` with the returned `id` until it completes. If the result includes a new `videoAssetId`, the video was copied into sync. storage: use that ID from here on. If more than one speaker is detected, explain that this workflow handles one speaker, and stop.
5. **Agree the edits.** Show the transcript lines around the fix. Turn the request into edits that use the transcript's word IDs:
   - `{"kind": "change", "wordId": "w35", "replacement": "Mia"}`, adding `"pronunciation": "meeah"` only for a name the voice might say wrong. Write respellings as plain words, without hyphens or capitals, which the voice may spell out.
   - `{"kind": "remove", "wordIds": ["w12", "w13"]}` for consecutive words.

   Confirm the edits with the user.
6. **Preview.** The preview clones the speaker's voice and can incur synthesis charges, so mention that when you confirm the edits. Call `create-dialogue-preview` with the edits and the `transcriptionJobId`, plus a new `idempotencyKey` saved before the call when `keyedPreview` is reported. If that call's outcome is unclear, retry only the identical request with the same key. Poll `get-dialogue-preview` until it completes, and share the preview audio. If some edits failed (a partial completion), for example because a replacement is too long for the gap it fills, say which, suggest shorter wording, confirm the revised edits, and make a new preview with `previousPreviewId`.
7. **Quote.** Call `estimate-dialogue-video` with the completed preview's ID as `dialogueEditId` and `model: "sync-3"`. Show the estimate and wait for approval of both the preview and the cost.
8. **Create.** Call `create-dialogue-video` once with the same `dialogueEditId`, the model, the project and a new `idempotencyKey`. If the response is lost, retry once with the same key and inputs.
9. **Wait and deliver.** Poll `generate_get-generation` with the returned `id` and `wait: true` until it's final. Give the exact `outputMediaUrl` unchanged.

## Limits

- One speaker per video, up to 10 minutes, and at most 100 edits per preview.
- Targeted words only. For a whole new script, explain that this workflow keeps the original recording, and offer the lipsync skill with a script and a chosen voice instead. Never split a new script into many word edits to get around this.
- The speaker's voice is cloned for the new words. Assume the user has the rights to their own media, and don't ask about consent on routine requests. Decline only when the request is to make a real, identifiable person, such as a politician or celebrity, appear to say something they didn't say, in order to deceive.
- To make many variants of one recording, such as one per recipient's name, use one preview per variant, then render them together with the batch-lipsync skill.
