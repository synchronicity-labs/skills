---
type: "regex"
pattern: "x-api-key\"?\\s*[:=]\\s*\"sk"
match: "not_contains"
target: {"source": "file", "path": "lipsync.py"}
---
