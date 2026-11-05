---
type: "llm"
focus: {"source": "file", "path": "lipsync.py"}
---

PASS if the code (not just comments) creates one idempotency key per job and reuses that same key on every retry of the create call, reads the API key from the environment, uploads the local files through the presigned asset upload, and stops polling on COMPLETED, FAILED and REJECTED.
FAIL if any of those is missing, if a new key is generated per retry attempt, or if the key appears only in a comment or unused code.
