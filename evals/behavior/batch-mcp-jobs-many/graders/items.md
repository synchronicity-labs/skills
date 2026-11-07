---
type: "llm"
focus: "mock_calls"
---

PASS if jobs_create-many was called exactly once, with tool lipsync_create, a UUID idempotencyKey, and exactly three items: one per manifest row (the intro, pricing and outro audio URLs, each with the presenter video), every item with its own different idempotencyKey.
FAIL if lipsync_create was called directly, jobs_create-many was called more than once, or an item is missing, repeated or shares another item's idempotencyKey.
