"""Generate the eval cases and mocks in evals/. Edit this file, then run: python3 scripts/build_evals.py"""
import json, textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "evals"
M = ROOT / "mocks" / "sync"
P = "mcp__plugin_sync_sync__"

def mock(name, body, expect=None):
    fm = ""
    if expect:
        fm = "---\nexpect:\n" + "".join(f"  {k}: {v}\n" for k, v in expect.items()) + "---\n\n"
    (M / f"{name}.md").write_text(fm + body.strip() + "\n")

# Dialogue + speech + timeline mocks
mock("dialogue_get-options", '{"available":true,"keyedPreview":true,"maxEdits":100,"maxSourceSeconds":600}')
mock("dialogue-transcriptions_create", '{"id":"9d1f0000-0000-4000-8000-00000000a001","status":"PROCESSING","videoAssetId":"{{input.videoAssetId}}"}', {"projectId": "string", "videoAssetId": "string"})
mock("dialogue-transcriptions_get", json.dumps({
    "id": "9d1f0000-0000-4000-8000-00000000a001", "status": "COMPLETED", "speakerCount": 1,
    "videoAssetId": "{{input.videoAssetId}}",
    "transcript": {"segments": [{"id": "s3", "speaker": "A", "startMs": 9200, "endMs": 12900, "words": [
        {"id": "w30", "text": "Our", "startMs": 9200, "endMs": 9400}, {"id": "w31", "text": "starter", "startMs": 9400, "endMs": 9800},
        {"id": "w32", "text": "plan", "startMs": 9800, "endMs": 10100}, {"id": "w33", "text": "is", "startMs": 10100, "endMs": 10250},
        {"id": "w34", "text": "just", "startMs": 10250, "endMs": 10500}, {"id": "w35", "text": "$39", "startMs": 10500, "endMs": 11400},
        {"id": "w36", "text": "a", "startMs": 11400, "endMs": 11500}, {"id": "w37", "text": "month,", "startMs": 11500, "endMs": 11900},
        {"id": "w38", "text": "um,", "startMs": 11900, "endMs": 12300}, {"id": "w39", "text": "billed", "startMs": 12300, "endMs": 12600},
        {"id": "w40", "text": "yearly.", "startMs": 12600, "endMs": 12900}]}]}}))
mock("dialogue-previews_create", '{"id":"5e5e0000-0000-4000-8000-00000000b001","status":"PROCESSING"}', {"projectId": "string", "videoAssetId": "string", "edits": "array"})
mock("dialogue-previews_get", '{"id":"{{input.id}}","status":"COMPLETED","previewAudioUrl":"https://assets.sync.so/previews/{{input.id}}.wav","failedEdits":[],"segmentLipsyncEnabled":true,"sectionExpansionEnabled":true}')
mock("dialogue-videos_estimate", '{"estimatedGenerationCost":0.85,"estimatedCredits":null,"model":"{{input.model}}"}', {"dialogueEditId": "string", "model": "string"})
mock("dialogue-videos_create", '{"id":"7c1e0000-0000-4000-8000-00000000d001","status":"PENDING"}', {"idempotencyKey": "string", "dialogueEditId": "string"})
mock("speech-previews_create", '{"id":"5bee0000-0000-4000-8000-0000000c0001","status":"PENDING","url":null,"duration":null,"error":null,"createdAt":"2026-11-05T00:00:00Z","startedAt":null,"finishedAt":null}', {"idempotencyKey": "string", "voiceId": "string", "script": "string"})
mock("speech-previews_get", '{"id":"{{input.id}}","status":"SUCCESS","url":"https://assets.sync.so/tts/{{input.id}}.mp3","duration":3.2,"error":null,"createdAt":"2026-11-05T00:00:00Z","startedAt":"2026-11-05T00:00:01Z","finishedAt":"2026-11-05T00:00:04Z"}')
mock("lipsync_create-timeline", '{"id":"7c1e0000-0000-4000-8000-00000000e001","status":"PENDING"}', {"videoAssetId": "string", "clips": "array"})

def case(group, name, prompt, graders, tags, desc, max_turns=30, allowed=("Skill", "Read", "Glob", "Grep"), files=None):
    d = ROOT / group / name
    (d / "graders").mkdir(parents=True, exist_ok=True)
    fm = {"description": desc, "tags": tags, "max_turns": max_turns, "timeout_seconds": 420, "allowed_tools": list(allowed)}
    lines = ["---"] + [f"{k}: {json.dumps(v) if isinstance(v, (list, int)) else json.dumps(v)}" for k, v in fm.items()] + ["---", "", prompt.strip(), ""]
    (d / "prompt.md").write_text("\n".join(lines))
    for gname, g in graders.items():
        body = g.pop("_body", "")
        fmg = "---\n" + "".join(k + ": " + json.dumps(v) + "\n" for k, v in g.items()) + "---\n"
        (d / "graders" / f"{gname}.md").write_text(fmg + ("\n" + body.strip() + "\n" if body else ""))
    if files:
        import base64
        sc = ["#!/usr/bin/env bash", "set -euo pipefail"]
        for p, c in files.items():
            if isinstance(c, Path):
                b64 = base64.b64encode(c.read_bytes()).decode()
                sc.append(f"mkdir -p \"$(dirname '{p}')\" && base64 --decode > '{p}' <<'B64'\n{b64}\nB64")
            else:
                sc.append(f"mkdir -p \"$(dirname '{p}')\" && cat > '{p}' <<'TXT'\n{c.rstrip(chr(10))}\nTXT")
        (d / "scaffold.sh").write_text("\n".join(sc) + "\n")
        (d / "case.yaml").write_text(f'schema_version: "1.1"\nname: {name}\ncontext:\n  scaffold_script: scaffold.sh\n')

def fired(skill):
    alt = skill if isinstance(skill, str) else "(?:" + "|".join(skill) + ")"
    return {"type": "tool_used", "tool": "Skill", "input_match": f'"skill"\\s*:\\s*"(?:[\\w-]+:)?{alt}"'}

def used(tool, **kw):
    return {"type": "tool_used", "tool": P + tool, **kw}

def never(tool):
    return {"type": "tool_used", "tool": P + tool, "min": 0, "max": 0, "arm": "both"}

def neg(**extra):
    return {"no-sync-skill": no_sync_skill(), "no-lipsync": never("lipsync_create"),
            "no-dub": never("dubbing_create"), "no-dialogue-video": never("dialogue-videos_create"), **extra}

def no_sync_skill():
    return {"type": "tool_used", "tool": "Skill", "input_match": '"skill"\\s*:\\s*"(?:sync:)?(?:setup|lipsync|talking-photo|ai-video-to-talking|translate-and-dub|edit-dialogue|localize-campaign|batch-lipsync|sync-api)"', "min": 0, "max": 0, "arm": "both"}

def judge(text):
    return {"type": "llm", "_body": text}

T = "triggers"
# --- Routing: should trigger, no approval given -> quote and stop -------------------------------
case(T, "lipsync-urls", "can you make the guy in https://example.com/clips/talk.mp4 say whatever is in https://example.com/vo/new-take.mp3? use the best model you have",
     {"skill-fired": fired("lipsync"), "quoted": used("generations_estimate-cost"), "no-paid-create": never("lipsync_create"),
      "asks-approval": judge("PASS if the final reply shows an estimated cost (about $1.60) and asks the user to confirm before creating the video.\nFAIL if it says the video was already created or started, or gives no cost.")},
     ["trigger", "lipsync"], "Video + audio URLs, no approval yet: load lipsync, quote, stop before the paid create.")
case(T, "lipsync-song", "I recorded a music video of me miming, link is https://cdn.example.com/mv/take3.mov, and the final mix is https://cdn.example.com/mv/final-vocals.wav. get my mouth matching the song",
     {"skill-fired": fired("lipsync"), "no-paid-create": never("lipsync_create")},
     ["trigger", "lipsync"], "Song/music video phrasing without the word lipsync.")
case(T, "talking-photo-headshot", "make our CEO headshot https://example.com/team/ceo.jpg say \"Welcome to Acme, we're so glad you're here\" in a warm female voice",
     {"skill-fired": fired("talking-photo"), "picked-voice": used("voices_list"), "quoted": used("generations_estimate-cost"), "no-paid-create": never("lipsync_create")},
     ["trigger", "talking-photo"], "Still image + script: talking-photo, voice lookup, quote, no create.")
case(T, "ai-video-veo-clip", "I made an 8 sec clip in Veo of a barista behind the counter, no dialogue: https://example.com/gen/barista-veo.mp4 . Can you make her say \"Morning! Oat latte again?\"",
     {"skill-fired": fired("ai-video-to-talking"), "no-paid-create": never("lipsync_create")},
     ["trigger", "ai-video-to-talking"], "Silent AI clip + line. ai-video-to-talking is best; lipsync is acceptable.")
case(T, "ai-video-from-idea", "I want a UGC style ad where a guy in his 20s holds our energy drink and says 'this actually tastes good'. I can generate the video in Kling but I need it to actually talk. how do I do this",
     {"skill-fired": fired("ai-video-to-talking"), "no-paid-create": never("lipsync_create"),
      "prompt-advice": judge("PASS if the reply gives a video-generation prompt or concrete guidance for the Kling clip that covers framing the face, the character speaking or talking, and a steady single shot, and explains that the clip then gets lip-synced to the line.\nFAIL if it claims sync. itself generates the video, or gives no guidance for the source clip.")},
     ["trigger", "ai-video-to-talking"], "No clip yet: should plan the source clip and explain the flow, without claiming sync. generates video.")
case(T, "dub-youtube", "dub this into spanish and brazilian portuguese please https://www.youtube.com/watch?v=Xk3pQ7mN2aB",
     {"skill-fired": fired("translate-and-dub"), "checked-languages": used("dubbing_get-options"), "project-first": {"type": "tool_order", "before": P + "projects_create", "after": P + "assets_create"},
      "no-paid-create": never("dubbing_create")},
     ["trigger", "translate-and-dub"], "Social link + two languages: project before import, check languages, quote, no paid create.")
case(T, "edit-dialogue-price", "In my promo video https://example.com/promo/pricing.mp4 I say our starter plan is $39 a month but we changed it to $49. Can you fix just that word without me reshooting?",
     {"skill-fired": fired("edit-dialogue"), "transcribed": used("dialogue-transcriptions_create"), "no-paid-create": never("dialogue-videos_create")},
     ["trigger", "edit-dialogue"], "Word fix: edit-dialogue, transcribe, and stop before paying.")
case(T, "localize-campaign-markets", "We're launching our spring campaign in DACH, Brazil and Japan next month. We have three ads: https://example.com/ads/hero-30s.mp4, https://example.com/ads/feature-15s.mp4 and https://example.com/ads/cta-6s.mp4. Need localized versions of all of them.",
     {"skill-fired": fired("localize-campaign"), "checked-languages": used("dubbing_get-options"), "no-paid-create": never("dubbing_create"),
      "plan": judge("PASS if the reply maps the markets to languages (German for DACH, Portuguese for Brazil, Japanese for Japan), lays out the 3 videos x 3 languages (9 versions), and asks for approval before creating anything, mentioning or offering a pilot first.\nFAIL if it starts creating versions, or maps a market to the wrong language.")},
     ["trigger", "localize-campaign"], "Markets not languages: map them, plan the matrix, pilot, approval.")
case(T, "batch-csv-leads", "leads.csv has 40 rows, each with a first_name and an audio file I recorded saying hi to them (audio/<first_name>.wav). Lipsync each one onto presenter.mp4 so I can send personalized videos.",
     {"skill-fired": fired("batch-lipsync"), "no-paid-create": never("lipsync_create")},
     ["trigger", "batch-lipsync"], "Personalized at scale: batch-lipsync, no paid work before the quote.")
case(T, "sync-api-express", "add an endpoint to my express app that takes a video url and an audio url and returns a lipsynced video using the sync.so api",
     {"skill-fired": fired("sync-api"), "no-paid-create": never("lipsync_create")},
     ["trigger", "sync-api"], "Developer integration: sync-api, not a one-off generation.")
case(T, "sync-api-429", "our python worker calls sync's generate endpoint and keeps getting 429 concurrency_limit_reached when we push a lot of jobs. whats the right way to handle this",
     {"skill-fired": fired("sync-api"),
      "advice": judge("PASS if the reply says to wait retryAfterSeconds (or Retry-After) and keep at most the plan's concurrency limit of jobs in flight with a queue, and to retry with the same Idempotency-Key.\nFAIL if it recommends retrying immediately in a tight loop, or a new idempotency key per retry, or doesn't mention the concurrency limit.")},
     ["trigger", "sync-api"], "Debugging an integration: sync-api with correct retry advice.")
case(T, "setup-first-run", "just installed the sync plugin, how do i get started?",
     {"skill-fired": fired("setup"), "account": used("account_get-context"), "no-paid-create": never("lipsync_create")},
     ["trigger", "setup"], "First run: setup, read account, show options, no paid work.")
case(T, "setup-credits", "how much sync credit do i have left this month?",
     {"usage": used("account_get-usage"), "no-paid-create": never("lipsync_create")},
     ["trigger", "setup"], "Account question: reads usage, either through setup or by calling the tool directly.")
# --- Near misses: should not trigger any sync skill ------------------------------------------
case(T, "neg-burn-subtitles", "burn english subtitles from subs.srt into ./talk.mp4 with ffmpeg",
     neg(), ["trigger", "negative"], "Subtitles only: not a sync job.")
case(T, "neg-translate-text", "translate this paragraph to spanish for our landing page: Lip sync any video in seconds. Upload, pick a voice, and you're done.",
     neg(), ["trigger", "negative"], "Text translation that mentions lip sync.")
case(T, "neg-veo-prompt-no-dialogue", "write me a veo prompt for a slow drone shot over misty mountains at sunrise, no people",
     neg(), ["trigger", "negative"], "Video-generation prompt with nobody speaking.")
case(T, "neg-compress-video", "compress ./talk.mp4 to under 10MB for email without losing too much quality",
     neg(), ["trigger", "negative"], "Video file chore.")
case(T, "neg-elevenlabs-tts", "write a node script that uses the elevenlabs sdk to turn script.txt into an mp3 voiceover",
     neg(), ["trigger", "negative"], "Pure TTS with another vendor, no video.")

B = "behavior"
case(B, "lipsync-local-files-approved", "Lipsync ./talk.mp4 to ./new-take.wav. Use sync-3 and just go ahead, I approve anything under $5.",
     {"skill-fired": fired("lipsync"),
      "presign-video": used("assets_create-upload-url", input_match='"contentType"\\s*:\\s*"video/mp4"[^}]*"size"\\s*:\\s*27858|"size"\\s*:\\s*27858[^}]*"contentType"\\s*:\\s*"video/mp4"'),
      "presign-audio": used("assets_create-upload-url", input_match='"contentType"\\s*:\\s*"audio/(x-)?wav"'),
      "put-with-type": {"type": "tool_used", "tool": "Bash", "input_match": "curl[^\\n]*-X PUT[^\\n]*Content-Type: video/mp4[^\\n]*--data-binary @[^\\n]*talk\\.mp4|curl[^\\n]*--data-binary @[^\\n]*talk\\.mp4[^\\n]*Content-Type: video/mp4|curl[^\\n]*-T[^\\n]*talk\\.mp4"},
      "no-create-after-failed-upload": never("lipsync_create"),
      "explains": judge("The upload URL is unreachable in this environment, so the upload fails.\nPASS if the final reply says the upload failed, that no video was created or charged, and what the user can do next.\nFAIL if it claims a video was created, or invents an output link.")},
     ["behavior", "lipsync"], "Local files: presign with the right type and size, PUT with the same type, and no paid create when the upload fails.",
     max_turns=40, allowed=("Skill", "Read", "Glob", "Grep", "Bash"),
     files={"talk.mp4": ROOT / "fixtures" / "talk.mp4", "new-take.wav": ROOT / "fixtures" / "new-take.wav"})
case(B, "talking-photo-approved", "Make https://example.com/team/ceo.jpg say \"Welcome to Acme, we're so glad you're here.\" Pick a warm female voice yourself. Approved, go ahead.",
     {"skill-fired": fired("talking-photo"), "voice": used("voices_list"),
      "quote-before-create": {"type": "tool_order", "before": P + "generations_estimate-cost", "after": P + "lipsync_create"},
      "image-script-voice": used("lipsync_create", min=1, max=1, input_match='"imageUrl".*"script".*|"script".*"imageUrl"'),
      "real-voice-id": used("lipsync_create", input_match='"voiceId"\\s*:\\s*"voice_(rachel|bella)"'),
      "sync-3": used("lipsync_create", input_match='"model"\\s*:\\s*"sync-3"'),
      "delivers-url": {"type": "regex", "pattern": "assets\\.sync\\.so/generations/gen-[A-Za-z0-9._~-]+/result\\.mp4", "target": "last_message"}},
     ["behavior", "talking-photo"], "Approved talking photo: picks a listed voice, sync-3, one create, exact URL.", max_turns=30)
case(B, "dub-two-languages-approved", "Dub https://www.youtube.com/watch?v=Xk3pQ7mN2aB into Spanish and Japanese. The cost is approved, go.",
     {"skill-fired": fired("translate-and-dub"),
      "project-before-import": {"type": "tool_order", "before": P + "projects_create", "after": P + "assets_create"},
      "explicit-intent": used("assets_create", input_match='"projectIntent"\\s*:\\s*"explicit"'),
      "quote": used("generations_estimate-cost", input_match="translate-and-dub"),
      "one-per-language": used("dubbing_create", min=2, max=2),
      "spanish": used("dubbing_create", input_match='"targetLang"\\s*:\\s*"es"'),
      "japanese": used("dubbing_create", input_match='"targetLang"\\s*:\\s*"ja"'),
      "labelled-results": judge("PASS if the final reply gives two output video URLs, each labelled with its language (Spanish and Japanese).\nFAIL otherwise.")},
     ["behavior", "translate-and-dub"], "Two languages: project first, explicit intent, one paid job per language.", max_turns=40)
case(B, "edit-dialogue-approved", "In https://example.com/promo/pricing.mp4 I say the starter plan is $39 a month; it's $49 now. Also cut the \"um\" right after it. Preview and cost are pre-approved, just do it.",
     {"skill-fired": fired("edit-dialogue"),
      "order": {"type": "tool_order", "before": P + "dialogue-transcriptions_create", "after": P + "dialogue-previews_create"},
      "change-edit": used("dialogue-previews_create", input_match='"w35"[^}]*(49|forty-nine)|(49|forty-nine)[^}]*"w35"'),
      "remove-um": used("dialogue-previews_create", input_match='"w38"'),
      "estimate-before-create": {"type": "tool_order", "before": P + "dialogue-videos_estimate", "after": P + "dialogue-videos_create"},
      "created-once": used("dialogue-videos_create", min=1, max=1)},
     ["behavior", "edit-dialogue"], "Word change + filler removal mapped to word IDs; estimate before create.", max_turns=45)
THREE_ROWS = "id,video,audio\nintro,https://example.com/v/presenter.mp4,https://example.com/a/intro.wav\npricing,https://example.com/v/presenter.mp4,https://example.com/a/pricing.wav\noutro,https://example.com/v/presenter.mp4,https://example.com/a/outro.wav\n"

def case_mock(group, name, tool, body):
    d = ROOT / group / name / "mocks" / "sync"
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{tool}.md").write_text(body.strip() + "\n")

case(B, "batch-mcp-three-rows", "Run every row of manifest.csv through sync lipsync. It's 3 rows, the total is approved. Use the tools you have, there's no API key here.",
     {"skill-fired": fired("batch-lipsync"), "read-limits": used("account_get-context"),
      "three-creates": used("lipsync_create", min=3, max=3),
      "results-table": judge("PASS if the final reply reports all three rows (intro, pricing, outro) as done with their output URLs.\nFAIL if a row is missing or a row was created twice.")},
     ["behavior", "batch-lipsync"], "MCP-only batch without jobs_create-many listed: reads concurrency, one create per row.",
     max_turns=60, allowed=("Skill", "Read", "Glob", "Grep", "Bash", "Write", "Edit"),
     files={"manifest.csv": THREE_ROWS})
# jobs_create-many and jobs_get-many are mocked only in this case, so every other case runs
# as a client that doesn't list them (the ChatGPT app, or a server before they shipped).
case(B, "batch-mcp-jobs-many", "Run every row of manifest.csv through sync lipsync. It's 3 rows, the total is approved. Use the tools you have, there's no API key here.",
     {"skill-fired": fired("batch-lipsync"),
      "one-set-call": used("jobs_create-many", min=1, max=1, input_match='"tool"\\s*:\\s*"lipsync_create"'),
      "no-single-creates": never("lipsync_create"),
      "followed": used("jobs_get-many"),
      "items": {"type": "llm", "focus": "mock_calls", "_body": "PASS if jobs_create-many was called exactly once, with tool lipsync_create, a UUID idempotencyKey, and exactly three items: one per manifest row (the intro, pricing and outro audio URLs, each with the presenter video), every item with its own different idempotencyKey.\nFAIL if lipsync_create was called directly, jobs_create-many was called more than once, or an item is missing, repeated or shares another item's idempotencyKey."},
      "results-table": judge("PASS if the final reply reports all three rows (intro, pricing, outro) as done with their output URLs.\nFAIL if a row is missing or a row was created twice.")},
     ["behavior", "batch-lipsync"], "MCP batch with jobs_create-many listed: one call starts all three rows, then jobs_get-many follows them.",
     max_turns=60, allowed=("Skill", "Read", "Glob", "Grep", "Bash", "Write", "Edit"),
     files={"manifest.csv": THREE_ROWS})
case_mock(B, "batch-mcp-jobs-many", "jobs_create-many", """---
type: agent
---

You are the sync. MCP server's jobs_create-many tool. For each element of the call's items input, in order, let KEY be that item's idempotencyKey, or, when the item has none, the call's idempotencyKey followed by "-" and the item's index (starting at 0).

Reply with exactly one JSON object and nothing else, of this shape, with one entry per item in items and in jobs:
{"tool":"lipsync_create","summary":{"total":N,"started":N,"failed":0,"notStarted":0},"items":[{"index":0,"status":"started","kind":"generation","id":"gen-KEY"}],"jobs":[{"kind":"generation","id":"gen-KEY"}],"nextStep":"Follow the started jobs with jobs_get-many, passing jobs (wait: true to wait on the server); never start them again."}

N is the number of items. If the tool input is not lipsync_create, reply instead with exactly:
{"error":{"message":"This run only mocks lipsync_create items."}}
""")
case_mock(B, "batch-mcp-jobs-many", "jobs_get-many", """---
type: agent
---

You are the sync. MCP server's jobs_get-many tool. Reply with exactly one JSON object and nothing else, with one entry in jobs for each element of the call's jobs input, in the same order, where ID is that element's id:
{"jobs":[{"kind":"generation","id":"ID","status":"COMPLETED","progress":100,"result":{"id":"ID","status":"COMPLETED","model":"sync-3","outputMediaUrl":"https://assets.sync.so/generations/ID/result.mp4","outputDuration":12.0}}],"counts":{"total":N,"running":0,"completed":N,"failed":0,"unreadable":0}}

N is the number of jobs in the input.
""")
case(B, "ai-video-script-approved", "https://example.com/gen/barista-kling.mp4 is a 12 second Kling clip of a barista. Make her say \"Morning! Oat latte again?\" Pick whatever voice fits a friendly barista. Cost approved.",
     {"skill-fired": fired("ai-video-to-talking"), "voice": used("voices_list"),
      "script-create": used("lipsync_create", min=1, max=1, input_match='"script"\\s*:\\s*"Morning! Oat latte again\\?"'),
      "video-input": used("lipsync_create", input_match='"videoUrl"\\s*:\\s*"https://example\\.com/gen/barista-kling\\.mp4"|"videoAssetId"')},
     ["behavior", "ai-video-to-talking"], "AI clip with the user's exact line and a chosen voice.", max_turns=30)
case(B, "sync-api-python-script", "Write lipsync.py: a Python script that lipsyncs ./talk.mp4 with ./voice.wav using the sync.so API and prints the output URL. Don't run it.",
     {"skill-fired": fired("sync-api"),
      "file": {"type": "file_exists", "path": "lipsync.py"},
      "env-key": {"type": "regex", "pattern": "SYNC_API_KEY|Sync\\(\\)", "target": {"source": "file", "path": "lipsync.py"}},
      "idempotency": {"type": "regex", "pattern": "Idempotency-Key", "flags": "i", "target": {"source": "file", "path": "lipsync.py"}},
      "upload-flow": {"type": "regex", "pattern": "/assets/upload", "target": {"source": "file", "path": "lipsync.py"}},
      "terminal-statuses": {"type": "regex", "pattern": "REJECTED", "target": {"source": "file", "path": "lipsync.py"}},
      "no-hardcoded-key": {"type": "regex", "pattern": "x-api-key\"?\\s*[:=]\\s*\"sk", "match": "not_contains", "target": {"source": "file", "path": "lipsync.py"}},
      "behaves": {"type": "llm", "focus": {"source": "file", "path": "lipsync.py"}, "_body": "PASS if the code (not just comments) creates one idempotency key per job and reuses that same key on every retry of the create call, reads the API key from the environment, uploads the local files through the presigned asset upload, and stops polling on COMPLETED, FAILED and REJECTED.\nFAIL if any of those is missing, if a new key is generated per retry attempt, or if the key appears only in a comment or unused code."}},
     ["behavior", "sync-api"], "Generated integration code: env key, upload flow, idempotency, terminal statuses.",
     max_turns=25, allowed=("Skill", "Read", "Glob", "Grep", "Write", "Edit"))
case(B, "sync-api-webhook-route", "Add a Next.js App Router route at app/api/sync-webhook/route.ts that receives sync.so generation webhooks, verifies them, and logs the generation id and status.",
     {"skill-fired": fired("sync-api"),
      "file": {"type": "file_exists", "path": "app/api/sync-webhook/route.ts"},
      "header": {"type": "regex", "pattern": "sync-signature", "flags": "i", "target": {"source": "file", "path": "app/api/sync-webhook/route.ts"}},
      "hmac": {"type": "regex", "pattern": "createHmac\\(\\s*[\"']sha256", "target": {"source": "file", "path": "app/api/sync-webhook/route.ts"}},
      "constant-time": {"type": "regex", "pattern": "timingSafeEqual", "target": {"source": "file", "path": "app/api/sync-webhook/route.ts"}},
      "raw-body": {"type": "regex", "pattern": "\\.text\\(\\)|arrayBuffer\\(\\)", "target": {"source": "file", "path": "app/api/sync-webhook/route.ts"}},
      "behaves": {"type": "llm", "focus": {"source": "file", "path": "app/api/sync-webhook/route.ts"}, "_body": "PASS if the handler parses the Sync-Signature header as t=<timestamp>,v1=<hex>, computes HMAC-SHA256 over the timestamp, a dot and the raw request body with the webhook secret from the environment, compares in constant time, rejects a missing or mismatched signature with a 4xx before parsing JSON, and returns 2xx for a valid one.\nFAIL if the HMAC is computed over re-serialized JSON instead of the raw body, the comparison isn't constant time, or invalid signatures are accepted."}},
     ["behavior", "sync-api"], "Webhook handler: Sync-Signature, HMAC-SHA256 over raw body, constant-time compare.",
     max_turns=25, allowed=("Skill", "Read", "Glob", "Grep", "Write", "Edit"))
mock("lipsync_create", '{"id":"gen-{{input.idempotencyKey}}","status":"PENDING","model":"{{input.model}}","projectId":"3f9a6b2e-1c4d-4e8f-a1b2-c3d4e5f60789"}', {"idempotencyKey": "string"})
rec = ROOT / "behavior" / "lipsync-concurrency-retry"
case(B, "lipsync-concurrency-retry", "Lipsync https://example.com/clips/talk.mp4 to https://example.com/vo/new-take.mp3 with sync-3. Cost is approved, go ahead.",
     {"skill-fired": fired("lipsync"), "retried": used("lipsync_create", min=2),
      "same-key": {"type": "llm", "focus": "mock_calls", "_body": "PASS if lipsync_create was called at least twice, the first call got a concurrency_limit_reached error, and every lipsync_create call used the same idempotencyKey and the same video, audio and model.\nFAIL if any retry used a different idempotencyKey or different inputs."},
      "delivers-url": {"type": "regex", "pattern": "assets\\.sync\\.so/generations/gen-[A-Za-z0-9._~-]+/result\\.mp4", "target": "last_message"}},
     ["behavior", "lipsync"], "First create hits the plan's concurrency limit: wait, then retry with the same key and inputs.", max_turns=30)
(rec / "mocks" / "sync").mkdir(parents=True, exist_ok=True)
(rec / "mocks" / "sync" / "lipsync_create.md").write_text("""---
type: agent
---

You are the sync. MCP server's lipsync_create tool. Look at the earlier calls in this run.

- If this is the first lipsync_create call in the run, reply with exactly this text and nothing else:
  {"error":{"message":"API request failed: 429 Too Many Requests - You have 3 active generations, which is your current concurrency limit of 3. Wait for an in-flight generation to finish.","status":429,"code":"concurrency_limit_reached","retryAfterMs":1500,"nextStep":"Wait retryAfterMs, then retry the identical request with the same idempotencyKey."}}
- Otherwise reply with exactly this JSON, replacing KEY with the call's idempotencyKey input:
  {"id":"gen-KEY","status":"PENDING","model":"sync-3"}
""")
mock("generations_estimate-cost", '{"estimatedGenerationCost":1.6,"estimatedCredits":null,"estimatedFrameCount":300,"durationEstimate":{"durationSeconds":12,"audioDurationSeconds":12,"source":"audio","approximate":false,"excludesSpeechSynthesis":true}}', {"model": "string"})

case(T, "troubleshoot-failed", "my lipsync 7c1e2a90-4b1d-4f6e-9a55-0d2f1c3b9e01 failed, what happened? was I charged?",
     {"skill-fired": fired("troubleshoot"), "read-job": used("generations_get"), "no-paid-create": never("lipsync_create"),
      "explains": judge("PASS if the reply says the video's resolution (8192x4320) is above the 4096x2160 maximum, suggests re-exporting at 4K or 1080p, and says failed generations aren't charged.\nFAIL if it starts a new generation, guesses a different cause, or says the user was charged.")},
     ["trigger", "troubleshoot"], "Failed generation: read it, explain the real cause, say it isn't charged, no new paid job.")
case_mock(T, "troubleshoot-failed", "generations_get", '{"id":"{{input.id}}","status":"FAILED","errorCode":"generation_input_resolution_unsupported","error":"Input video resolution 8192x4320 exceeds the maximum supported resolution of 4096x2160.","model":"sync-3","outputMediaUrl":null}')
case(T, "troubleshoot-stuck", "this dub d0b1a2c3-0000-4000-8000-es0000000001 has been processing for like 25 minutes. should i just start it again?",
     {"skill-fired": fired(["troubleshoot", "translate-and-dub"]), "read-job": used("generations_get"),
      "no-new-dub": never("dubbing_create"), "no-new-lipsync": never("lipsync_create"),
      "advice": judge("PASS if the reply says the job is still processing, advises not to start it again because that would be a second paid job and wouldn't be faster, and offers to keep checking the same job.\nFAIL if it recommends or starts a new dub.")},
     ["trigger", "troubleshoot"], "Slow job: keep polling the same ID, never resubmit.")
case_mock(T, "troubleshoot-stuck", "generations_get", '{"id":"{{input.id}}","status":"PROCESSING","progress_percent":62,"model":"sync-3","outputMediaUrl":null}')
case(T, "neg-troubleshoot-code-retry", "write retry logic in our node worker for when sync's /v2/generate returns 429 concurrency_limit_reached",
     {"skill-fired": fired("sync-api"), "not-troubleshoot": {"type": "tool_used", "tool": "Skill", "input_match": '"skill"\\s*:\\s*"(?:sync:)?troubleshoot"', "min": 0, "max": 0, "arm": "both"}},
     ["trigger", "negative", "troubleshoot"], "Integration code for 429s goes to sync-api, not troubleshoot.")
print("ok")
