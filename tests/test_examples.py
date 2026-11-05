"""Run the sync-api skill's code samples against the fake sync. API, so the docs can't silently rot.

Needs the published SDKs. Point the tests at them with:
  SYNC_TEST_PYTHON=/path/to/venv/bin/python   (a Python with `pip install syncsdk`)
  SYNC_TEST_NODE_MODULES=/path/to/node_modules (with @sync.so/sdk, typescript and @types/node)
Each test is skipped when its runtime isn't configured.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
import unittest
from pathlib import Path

from fake_sync import KEY, serve

REFS = Path(__file__).resolve().parents[1] / "skills" / "sync-api" / "references"


def code_block(md: Path, lang: str, index: int = 0) -> str:
    return re.findall(rf"```{lang}\n(.*?)```", md.read_text(), re.S)[index]


def sign(payload: dict, secret: str, t: int | None = None) -> tuple[str, str]:
    """Sign a webhook body exactly the way the sync. API does."""
    t = int(time.time()) if t is None else t
    body = json.dumps(payload, separators=(",", ":"))
    digest = hmac.new(secret.encode(), f"{t}.{body}".encode(), hashlib.sha256).hexdigest()
    return body, f"t={t},v1={digest}"


class ExamplesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake, cls.server, cls.base = serve()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def setUp(self):
        self.fake.reset()
        self.dir = Path(tempfile.mkdtemp())
        (self.dir / "talk.mp4").write_bytes(b"video")
        (self.dir / "new-take.wav").write_bytes(b"audio")

    def require_or_skip(self, why: str):
        if os.environ.get("SYNC_TEST_REQUIRE_SDKS"):
            self.fail(f"SYNC_TEST_REQUIRE_SDKS is set: {why}")
        self.skipTest(why)

    def run_in_dir(self, cmd, **env):
        proc = subprocess.run(cmd, cwd=self.dir, capture_output=True, text=True, timeout=180,
                              env={**os.environ, "SYNC_API_KEY": KEY, **env})
        if proc.returncode != 0:
            self.fail(f"{cmd} exited {proc.returncode}\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}")
        return proc

    def assert_full_flow(self, stdout: str):
        self.assertIn("Estimated cost: $1.44", stdout)  # 12 s * the fake's $0.12/s
        self.assertRegex(stdout, r"Output: http://127\.0\.0\.1:\d+/signed/out/")
        self.assertEqual(self.fake.uploads, 2)
        self.assertEqual(len(self.fake.creates), 1)
        key, body = self.fake.creates[0]
        self.assertRegex(key or "", r"^[0-9a-f-]{36}$", "the create carries an Idempotency-Key")
        self.assertEqual(body["model"], "sync-3")
        self.assertEqual([i["type"] for i in body["input"]], ["video", "audio"])
        self.assertTrue(all("assetId" in i for i in body["input"]), "inputs reference the uploaded assets")
        self.assertEqual(self.fake.signed_requests_with_key, 0, "the presigned upload never gets the API key")

    def test_python_sample_runs_end_to_end(self):
        python = os.environ.get("SYNC_TEST_PYTHON")
        if not python:
            self.require_or_skip("set SYNC_TEST_PYTHON to a Python with syncsdk installed")
        code = code_block(REFS / "python.md", "python")
        code = code.replace('API = "https://api.sync.so/v2"', f'API = "{self.base}/v2"')
        code = code.replace("client = Sync()", f'client = Sync(base_url="{self.base}")')
        (self.dir / "example.py").write_text(code)
        self.assert_full_flow(self.run_in_dir([python, "example.py"]).stdout)
        again = self.run_in_dir([python, "example.py"]).stdout
        self.assertIn("Output:", again)
        self.assertEqual(len(self.fake.creates), 1, "a restart polls the saved generation instead of creating another")
        self.assertEqual(self.fake.uploads, 2, "a restart doesn't upload again")

    def test_python_tts_variation_imports(self):
        python = os.environ.get("SYNC_TEST_PYTHON")
        if not python:
            self.require_or_skip("set SYNC_TEST_PYTHON to a Python with syncsdk installed")
        line = re.search(r"`(from sync\.common import [^`]+)`, then `([^`]+)`", (REFS / "python.md").read_text())
        self.assertIsNotNone(line, "python.md documents the script variation")
        self.run_in_dir([python, "-c", f"{line.group(1)}\nprint({line.group(2)}.provider.script)"])

    def test_python_sample_backs_off_on_concurrency_limit(self):
        python = os.environ.get("SYNC_TEST_PYTHON")
        if not python:
            self.require_or_skip("set SYNC_TEST_PYTHON to a Python with syncsdk installed")
        self.fake.limit = 0  # every create is refused until we raise the limit
        code = code_block(REFS / "python.md", "python")
        code = code.replace('API = "https://api.sync.so/v2"', f'API = "{self.base}/v2"')
        code = code.replace("client = Sync()", f'client = Sync(base_url="{self.base}")')
        (self.dir / "example.py").write_text(code)
        import threading
        threading.Timer(1.0, lambda: setattr(self.fake, "limit", 1)).start()
        self.run_in_dir([python, "example.py"])
        keys = {k for k, _ in self.fake.creates}
        self.assertGreater(len(self.fake.creates), 1, "the sample retried after 429")
        self.assertEqual(len(keys), 1, "every retry reused the same idempotency key")
        self.assertEqual(len(self.fake.generations), 1)

    def node_dir(self):
        modules = os.environ.get("SYNC_TEST_NODE_MODULES")
        if not modules or not shutil.which("node"):
            if os.environ.get("SYNC_TEST_REQUIRE_SDKS"):
                self.fail("SYNC_TEST_REQUIRE_SDKS is set but SYNC_TEST_NODE_MODULES or node is missing")
            self.skipTest("set SYNC_TEST_NODE_MODULES to node_modules with @sync.so/sdk, typescript and @types/node")
        (self.dir / "node_modules").symlink_to(modules)
        (self.dir / "package.json").write_text('{"type": "module"}')
        return Path(modules)

    def test_typescript_sample_typechecks_and_runs(self):
        modules = self.node_dir()
        code = code_block(REFS / "typescript.md", "typescript")
        code = code.replace('const API = "https://api.sync.so/v2";', f'const API = "{self.base}/v2";')
        code = code.replace("new SyncClient({ apiKey })", f'new SyncClient({{ apiKey, baseUrl: "{self.base}" }})')
        (self.dir / "example.ts").write_text(code)
        self.run_in_dir([str(modules / ".bin" / "tsc"), "--strict", "--module", "nodenext", "--target", "es2022",
                         "--types", "node", "--skipLibCheck", "--outDir", "dist", "example.ts"])
        self.assert_full_flow(self.run_in_dir(["node", "dist/example.js"]).stdout)
        self.run_in_dir(["node", "dist/example.js"])
        self.assertEqual(len(self.fake.creates), 1, "a restart polls the saved generation instead of creating another")

    def test_typescript_webhook_route_verifies_signatures(self):
        modules = self.node_dir()
        route = code_block(REFS / "webhooks.md", "typescript")
        (self.dir / "route.ts").write_text(route)
        secret = "whsec_test"
        good_body, good_sig = sign({"id": "g1", "status": "COMPLETED"}, secret)
        _, old_sig = sign({"id": "g1", "status": "COMPLETED"}, secret, t=int(time.time()) - 3600)
        harness = f"""
import {{ POST }} from "./route.ts";
const call = (body: string, sig: string | null) =>
  POST(new Request("http://x/api", {{ method: "POST", body, headers: sig ? {{ "sync-signature": sig }} : {{}} }})).then(r => r.status);
const results = [
  await call({json.dumps(good_body)}, {json.dumps(good_sig)}),
  await call({json.dumps(good_body)}, {json.dumps(good_sig.replace("v1=", "v1=0"))}),
  await call({json.dumps(good_body.replace("COMPLETED", "FAILED"))}, {json.dumps(good_sig)}),
  await call({json.dumps(good_body)}, {json.dumps(old_sig)}),
  await call({json.dumps(good_body)}, null),
];
console.log(JSON.stringify(results));
"""
        (self.dir / "harness.ts").write_text(harness.replace('"./route.ts"', '"./route.js"'))
        self.run_in_dir([str(modules / ".bin" / "tsc"), "--strict", "--module", "nodenext", "--target", "es2022",
                         "--types", "node", "--skipLibCheck", "--outDir", "dist", "route.ts", "harness.ts"])
        out = self.run_in_dir(["node", "dist/harness.js"], SYNC_WEBHOOK_SECRET=secret).stdout.strip().splitlines()[-1]
        self.assertEqual(json.loads(out), [200, 400, 400, 400, 400])

    def test_python_webhook_verify_matches_server_signing(self):
        block = code_block(REFS / "webhooks.md", "python")
        verify_src = block[block.index("def verify"):block.index("@app.post")]
        namespace = {}
        exec("import hashlib, hmac, re, time\nSECRET = b'whsec_test'\n" + verify_src, namespace)
        verify = namespace["verify"]
        body, sig = sign({"id": "g1", "status": "COMPLETED"}, "whsec_test")
        self.assertTrue(verify(body.encode(), sig))
        self.assertFalse(verify(body.replace("COMPLETED", "FAILED").encode(), sig))
        self.assertFalse(verify(body.encode(), None))
        _, old = sign({"id": "g1"}, "whsec_test", t=int(time.time()) - 3600)
        self.assertFalse(verify(json.dumps({"id": "g1"}, separators=(",", ":")).encode(), old))


if __name__ == "__main__":
    unittest.main()
