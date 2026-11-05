# sync-api

## What it does

`sync-api` helps your coding agent build sync. into your own app, backend, script or pipeline. It writes server-side code that uploads media, creates generations with idempotency keys, verifies webhooks, polls as a fallback, and handles errors and concurrency limits, using the REST API or the official Python (`syncsdk`) and TypeScript (`@sync.so/sdk`) SDKs.

## When to reach for it

| What you're doing | Reach for |
| --- | --- |
| Writing or reviewing code that calls the sync. API | `sync-api` |
| Debugging a 429, a webhook or a duplicate charge | `sync-api` |
| Making one video in this chat | [lipsync](lipsync.md), [talking-photo](talking-photo.md), [translate-and-dub](translate-and-dub.md) |
| Running a CSV of jobs once | [batch-lipsync](batch-lipsync.md) |

## Try

- "Add an endpoint to my Express app that lipsyncs a video URL to an audio URL with sync."
- "Write a Python script that dubs every video in ./in into Spanish"
- "Add a Next.js route that verifies sync. webhooks"
- "Our worker keeps getting 429 concurrency_limit_reached. What's the right fix?"

## What you need

- A sync. API key from https://sync.so/settings/api-keys, set as `SYNC_API_KEY` on the server.
- Python 3.8 or later, or Node 18 or later, for the SDKs.

## Common questions

**Why does the code save a key before calling the API?**
`POST /v2/generate` accepts an `Idempotency-Key`. Created once per job and reused on every retry, it turns a retry after a timeout into a replay of the original generation instead of a second paid one.

**Webhooks or polling?**
Webhooks, verified with the `Sync-Signature` header, for production. A periodic poll catches deliveries your endpoint missed.

**The SDK doesn't have a field the docs mention.**
The SDKs can lag the API. The skill calls that endpoint over HTTP instead of forcing the types.

**What should I do with a 429?**
Wait the time the response gives you, retry with the same idempotency key, and keep at most your plan's concurrency limit of jobs in flight with a queue on your side.

## It's working if

- The API key lives on the server, never in browser or mobile code.
- Every create carries an idempotency key that was stored before the call.
- The webhook handler checks the signature against the raw body before parsing it.
