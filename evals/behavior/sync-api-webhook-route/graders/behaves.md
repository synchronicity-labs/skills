---
type: "llm"
focus: {"source": "file", "path": "app/api/sync-webhook/route.ts"}
---

PASS if the handler parses the Sync-Signature header as t=<timestamp>,v1=<hex>, computes HMAC-SHA256 over the timestamp, a dot and the raw request body with the webhook secret from the environment, compares in constant time, rejects a missing or mismatched signature with a 4xx before parsing JSON, and returns 2xx for a valid one.
FAIL if the HMAC is computed over re-serialized JSON instead of the raw body, the comparison isn't constant time, or invalid signatures are accepted.
