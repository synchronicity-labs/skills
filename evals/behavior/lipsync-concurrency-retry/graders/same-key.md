---
type: "llm"
focus: "mock_calls"
---

PASS if create-lipsync was called at least twice, the first call got a concurrency_limit_reached error, and every create-lipsync call used the same idempotencyKey and the same video, audio and model.
FAIL if any retry used a different idempotencyKey or different inputs.
