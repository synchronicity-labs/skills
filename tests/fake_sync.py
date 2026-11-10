"""A small local fake of the sync. API, shared by the tests."""
from __future__ import annotations

import json
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

KEY = "sk-test-key"


class FakeSync:
    """Just enough of the sync. API to exercise the script's contract."""

    def __init__(self):
        self.lock = threading.Lock()
        self.reset()

    def reset(self):
        self.generations = {}  # id -> {"status", "polls", "body"}
        self.keys = {}  # idempotency key -> generation id
        self.creates = []  # every POST /v2/generate attempt: (key, body)
        self.uploads = 0
        self.assets = 0
        self.active = 0
        self.max_active = 0
        self.limit = 2
        self.fail_first_with_503 = set()  # row output names that get one 503 first
        self.fail_rows = set()  # output names whose generation ends FAILED
        self.signed_requests_with_key = 0
        self.batches = {}
        self.batch_error = None  # Optional (HTTP status, error code) for a refused submission
        self.asset_durations = {}  # asset id -> seconds, for GET /v2/assets/{id}

    def handler(self):
        fake = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def _json(self, status, body, headers=None):
                raw = json.dumps(body).encode()
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                for k, v in (headers or {}).items():
                    self.send_header(k, v)
                self.send_header("Content-Length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)

            def _body(self):
                length = int(self.headers.get("Content-Length") or 0)
                return self.rfile.read(length) if length else b""

            def _authed(self):
                if self.headers.get("x-api-key") != KEY:
                    self._json(401, {"message": "Unauthorized"})
                    return False
                return True

            def do_PUT(self):
                self._body()
                if self.path.startswith("/signed/upload"):
                    if self.headers.get("x-api-key"):
                        fake.signed_requests_with_key += 1
                    with fake.lock:
                        fake.uploads += 1
                    self.send_response(200)
                    self.end_headers()
                    return
                self._json(404, {})

            def do_POST(self):
                raw = self._body()
                if not self._authed():
                    return
                body = json.loads(raw or b"{}")
                port = self.server.server_address[1]
                if self.path == "/v2/assets/upload":
                    name = uuid.uuid4().hex
                    return self._json(201, {"uploadUrl": f"http://127.0.0.1:{port}/signed/upload/{name}",
                                            "url": f"https://storage.example/{name}", "expiresIn": 900})
                if self.path == "/v2/assets":
                    with fake.lock:
                        fake.assets += 1
                    return self._json(201, {"id": str(uuid.uuid4()), "durationSeconds": 4.0})
                if self.path == "/v2/generations/estimate":
                    return self._json(200, {"estimatedGenerationCost": round(body["duration"] * 0.12, 4),
                                            "estimatedCredits": None, "estimatedFrameCount": 100})
                if self.path == "/v2/generate":
                    key = self.headers.get("Idempotency-Key")
                    name = body.get("outputFileName")
                    with fake.lock:
                        fake.creates.append((key, body))
                        if name in fake.fail_first_with_503:
                            fake.fail_first_with_503.discard(name)
                            return self._json(503, {"errorCode": "generation_admission_unavailable", "message": "try later"},
                                              {"Retry-After": "0"})
                        if key in fake.keys:
                            gen_id = fake.keys[key]
                            if fake.generations[gen_id]["status"] not in ("FAILED", "REJECTED"):
                                return self._json(200, {"id": gen_id, "status": fake.generations[gen_id]["status"]},
                                                  {"Idempotency-Replayed": "true"})
                        if fake.active >= fake.limit:
                            return self._json(429, {"statusCode": 429, "errorCode": "concurrency_limit_reached",
                                                    "concurrencyLimit": fake.limit, "retryAfterSeconds": 0.05})
                        gen_id = str(uuid.uuid4())
                        fake.keys[key] = gen_id
                        fake.generations[gen_id] = {"status": "PROCESSING", "polls": 0, "name": name}
                        fake.active += 1
                        fake.max_active = max(fake.max_active, fake.active)
                    return self._json(201, {"id": gen_id, "status": "PENDING"})
                if self.path == "/v2/batch":
                    if fake.batch_error:
                        status, code = fake.batch_error
                        return self._json(status, {"statusCode": status, "errorCode": code,
                                                   "message": "Batch submission denied."})
                    if body.get("dry_run"):
                        return self._json(200, {"status": "VALIDATED"})
                    batch_id = "batch_" + uuid.uuid4().hex[:8]
                    fake.batches[batch_id] = {"rows": body["rows"], "polls": 0}
                    return self._json(201, {"id": batch_id, "status": "PENDING"})
                self._json(404, {"message": self.path})

            def do_GET(self):
                port = self.server.server_address[1]
                if self.path.startswith("/signed/"):
                    if self.headers.get("x-api-key"):
                        fake.signed_requests_with_key += 1
                    if self.path.startswith("/signed/result/"):
                        batch_id = self.path.rsplit("/", 1)[1]
                        lines = []
                        for i, row in enumerate(fake.batches[batch_id]["rows"]):
                            ok = i % 2 == 0
                            lines.append(json.dumps({
                                "request_id": row["request_id"], "status": "COMPLETED" if ok else "FAILED",
                                "error": None if ok else {"code": "INVALID_INPUT", "message": "no face"},
                                "response": {"id": str(uuid.uuid4()), "output_url": f"http://127.0.0.1:{port}/signed/out/{row['request_id']}"} if ok else None,
                            }))
                        raw = ("\n".join(lines) + "\n").encode()
                    else:
                        raw = b"fake-mp4-bytes"
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(raw)))
                    self.end_headers()
                    self.wfile.write(raw)
                    return
                if not self._authed():
                    return
                if self.path.startswith("/v2/generate/"):
                    gen_id = self.path.split("/")[3].split("?")[0]
                    with fake.lock:
                        gen = fake.generations[gen_id]
                        gen["polls"] += 1
                        if gen["status"] == "PROCESSING" and gen["polls"] >= 2:
                            gen["status"] = "FAILED" if gen["name"] in fake.fail_rows else "COMPLETED"
                            fake.active -= 1
                    out = {"id": gen_id, "status": gen["status"],
                           "outputUrl": f"http://127.0.0.1:{port}/signed/out/{gen_id}" if gen["status"] == "COMPLETED" else None,
                           "error": "face not found" if gen["status"] == "FAILED" else None}
                    return self._json(200, out)
                if self.path.startswith("/v2/assets/"):
                    asset_id = self.path.rsplit("/", 1)[1]
                    return self._json(200, {"id": asset_id, "durationSeconds": fake.asset_durations.get(asset_id)})
                if self.path.startswith("/v2/batch/"):
                    batch_id = self.path.rsplit("/", 1)[1]
                    batch = fake.batches[batch_id]
                    batch["polls"] += 1
                    done = batch["polls"] >= 2
                    return self._json(200, {"id": batch_id, "status": "COMPLETED" if done else "PROCESSING",
                                            "metrics": {"total_generations": len(batch["rows"])},
                                            "outputUrl": f"http://127.0.0.1:{port}/v2/batches/{batch_id}/result"})
                if self.path.startswith("/v2/batches/") and self.path.endswith("/result"):
                    batch_id = self.path.split("/")[3]
                    self.send_response(302)
                    self.send_header("Location", f"http://127.0.0.1:{port}/signed/result/{batch_id}")
                    self.end_headers()
                    return
                self._json(404, {"message": self.path})

        return Handler



def serve():
    """Start a FakeSync server on a free port; returns (fake, server, base_url)."""
    fake = FakeSync()
    server = ThreadingHTTPServer(("127.0.0.1", 0), fake.handler())
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return fake, server, f"http://127.0.0.1:{server.server_address[1]}"
