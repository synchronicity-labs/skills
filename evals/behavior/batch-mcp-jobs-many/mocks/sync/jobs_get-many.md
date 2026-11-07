---
type: agent
---

You are the sync. MCP server's jobs_get-many tool. Reply with exactly one JSON object and nothing else, with one entry in jobs for each element of the call's jobs input, in the same order, where ID is that element's id:
{"jobs":[{"kind":"generation","id":"ID","status":"COMPLETED","progress":100,"result":{"id":"ID","status":"COMPLETED","model":"sync-3","outputMediaUrl":"https://assets.sync.so/generations/ID/result.mp4","outputDuration":12.0}}],"counts":{"total":N,"running":0,"completed":N,"failed":0,"unreadable":0}}

N is the number of jobs in the input.
