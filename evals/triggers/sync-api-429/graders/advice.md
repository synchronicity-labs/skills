---
type: "llm"
---

PASS if the reply says to wait retryAfterSeconds (or Retry-After) and keep at most the plan's concurrency limit of jobs in flight with a queue, and to retry with the same Idempotency-Key.
FAIL if it recommends retrying immediately in a tight loop, or a new idempotency key per retry, or doesn't mention the concurrency limit.
