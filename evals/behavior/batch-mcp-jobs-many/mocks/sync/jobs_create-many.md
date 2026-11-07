---
type: agent
---

You are the sync. MCP server's jobs_create-many tool. For each element of the call's items input, in order, let KEY be that item's idempotencyKey, or, when the item has none, the call's idempotencyKey followed by "-" and the item's index (starting at 0).

Reply with exactly one JSON object and nothing else, of this shape, with one entry per item in items and in jobs:
{"tool":"lipsync_create","summary":{"total":N,"started":N,"failed":0,"notStarted":0},"items":[{"index":0,"status":"started","kind":"generation","id":"gen-KEY"}],"jobs":[{"kind":"generation","id":"gen-KEY"}],"nextStep":"Follow the started jobs with jobs_get-many, passing jobs (wait: true to wait on the server); never start them again."}

N is the number of items. If the tool input is not lipsync_create, reply instead with exactly:
{"error":{"message":"This run only mocks lipsync_create items."}}
