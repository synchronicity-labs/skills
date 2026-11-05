# sync. Batch API

`POST /v2/batch` takes many `/v2/generate` requests in one submission. sync. tracks every row and gives you one results file, plus a webhook when the batch finishes. Full guide: https://sync.so/docs/api-reference/guides/batch-processing.

## When to use it

Every paid plan can send batches. The free tier can't. What a batch can hold depends on the plan:

| Plan | Rows per batch | How it runs |
| --- | --- | --- |
| Scale and above | 20 to 500 | Queued, outside the plan's generation concurrency. Results usually arrive within the 24-hour target turnaround. |
| Other paid plans | 1 up to the plan's free concurrency slots right now | The rows count toward the plan's concurrency, like single generations. |

So below Scale, a batch is a convenience, not extra capacity. For more rows than the plan runs at once, individual generations (`sync_batch.py run`) get the same throughput with less bookkeeping.

- Always send `dry_run: true` first. It validates the rows against the plan's limits, creates nothing, and returns `{"status": "VALIDATED"}`.
- `400` means too many rows for the plan. `429 concurrency_limit_reached` means not enough free slots, or too many batches running. Wait `retryAfterSeconds`, or split the rows. `402 plan_feature_unavailable` means the plan has no batch access. `402 insufficient_credits` means the balance doesn't cover the whole batch; credit-billed plans reserve credits for every row at submit.
- Batches only take `/v2/generate` rows, and rows with inputs over 30 seconds may be refused.

## Request

```bash
curl -sS https://api.sync.so/v2/batch -H "x-api-key: $SYNC_API_KEY" -H 'Content-Type: application/json' -d '{
  "rows": [
    {"request_id": "lead-001", "endpoint": "/v2/generate",
     "payload": {"model": "sync-3", "input": [{"type": "video", "assetId": "<videoAssetId>"}, {"type": "audio", "assetId": "<audioAssetId>"}]}}
  ],
  "dry_run": true,
  "webhook_url": "https://example.com/hooks/sync-batch"
}'
```

- `request_id` must be unique within the batch, and links each result line to its row.
- `payload` is the same body as `POST /v2/generate`. Upload local files first and reference them by `assetId`.
- A JSONL file in a multipart `input` field works too, up to 5 MB.
- Batch creation is not idempotent. If a create request times out, list your batches with `GET /v2/batch` before sending it again, so the same rows don't run twice.

## Status and results

- `GET /v2/batch/{id}` returns `status` (`PENDING`, `JOBS_CREATED`, `PROCESSING`, `COMPLETED` or `FAILED`), `metrics` (`total_generations`, `success_count`, `failed_count`, `pending_count`) and `outputUrl`. Check every minute or so. It's slow work, and tight polling doesn't speed it up.
- When it's `COMPLETED`, a `GET` to `outputUrl` with the API key redirects (302) to a signed JSONL file. Fetch that signed URL without the key. Each line holds `request_id`, `status`, `error` and `response`. The video is at `response.output_url`, in snake_case.
- With `webhook_url` set, sync. posts once the batch finishes, signed like generation webhooks (`Sync-Signature`). The notification can arrive more than once, so dedupe on the batch `id`.

## Dialogue edit rows (early access)

To render one recording personalized many ways, such as one version per recipient's name in the presenter's own voice, make one dialogue-edit preview per variant (see the edit-dialogue skill). Then submit one row per completed preview: the same source video as the only input, plus `"dialogueEdit": {"id": "<previewId>"}`. This is enabled per organization. The `dry_run` response says whether it's available. Preview requests are limited to 30 a minute, so pace them.
