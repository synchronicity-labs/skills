"""End-to-end tests for skills/batch-lipsync/scripts/sync_batch.py against a local fake of the sync. API.

Run: python3 -m unittest discover -s tests
"""
from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from fake_sync import KEY, serve

SCRIPT = Path(__file__).resolve().parents[1] / "skills" / "batch-lipsync" / "scripts" / "sync_batch.py"


class SyncBatchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fake, cls.server, cls.base = serve()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def setUp(self):
        self.fake.reset()
        self.dir = Path(tempfile.mkdtemp())
        (self.dir / "presenter.mp4").write_bytes(b"video")
        for i in range(6):
            (self.dir / f"vo{i}.wav").write_bytes(b"audio" * (i + 1))

    def manifest(self, rows):
        path = self.dir / "manifest.csv"
        with open(path, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["id", "video", "audio", "script", "voice_id", "sync_mode"])
            w.writeheader()
            w.writerows(rows)
        return path

    def run_script(self, *args, check=True):
        env = {**os.environ, "SYNC_API_KEY": KEY, "SYNC_API_BASE": self.base}
        proc = subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, env=env, timeout=120)
        if check and proc.returncode != 0:
            self.fail(f"exit {proc.returncode}\nstdout:\n{proc.stdout}\nstderr:\n{proc.stderr}")
        return proc

    def six_rows(self):
        rows = [{"id": f"lead-{i:03d}", "video": "presenter.mp4", "audio": f"vo{i}.wav"} for i in range(5)]
        rows.append({"id": "lead-005", "video": "presenter.mp4", "script": "Hi Sam, thanks for joining.", "voice_id": "v1"})
        return self.manifest(rows)

    def test_run_respects_concurrency_uploads_once_and_resumes_without_new_charges(self):
        path = self.six_rows()
        self.fake.fail_first_with_503.add("lead-002")
        out = self.dir / "out"
        self.run_script("run", str(path), "--concurrency", "4", "--out", str(out))

        self.assertLessEqual(self.fake.max_active, self.fake.limit, "never more generations in flight than the plan allows")
        self.assertEqual(self.fake.uploads, 6, "presenter.mp4 is uploaded once although six rows share it")
        self.assertEqual(len(self.fake.generations), 6, "one generation per row, including the row that got a 503")
        keys_per_row = {}
        for key, body in self.fake.creates:
            keys_per_row.setdefault(body["outputFileName"], set()).add(key)
        self.assertTrue(all(len(k) == 1 for k in keys_per_row.values()), "every retry of a row reuses its idempotency key")
        self.assertEqual(sorted(p.name for p in out.iterdir()), [f"lead-{i:03d}.mp4" for i in range(6)])
        self.assertEqual(self.fake.signed_requests_with_key, 0, "the API key is never sent to signed URLs")
        with open(self.dir / "results.csv") as fh:
            self.assertEqual({r["status"] for r in csv.DictReader(fh)}, {"COMPLETED"})

        creates_before = len(self.fake.creates)
        again = self.run_script("run", str(path), "--concurrency", "4", "--out", str(out))
        self.assertEqual(len(self.fake.creates), creates_before, "a rerun of a finished manifest creates nothing")
        self.assertIn("already completed", again.stdout)

    def test_interrupted_run_resumes_by_polling_not_resubmitting(self):
        path = self.six_rows()
        state_path = path.with_name(path.name + ".state.json")
        self.run_script("run", str(path), "--only", "lead-000")
        state = json.loads(state_path.read_text())
        # Simulate a crash after the create call: the generation exists, the run never saw it finish.
        row = state["rows"]["lead-000"]
        gen_id = row["generationId"]
        self.fake.generations[gen_id].update(status="PROCESSING", polls=0)
        self.fake.active += 1
        row.update(status="PENDING", outputUrl=None)
        state_path.write_text(json.dumps(state))
        creates_before = len(self.fake.creates)
        self.run_script("run", str(path), "--only", "lead-000")
        self.assertEqual(len(self.fake.creates), creates_before, "resume polls the saved generation instead of creating one")
        self.assertEqual(json.loads(state_path.read_text())["rows"]["lead-000"]["status"], "COMPLETED")

    def test_failed_rows_are_reported_and_only_retried_on_request(self):
        path = self.six_rows()
        self.fake.fail_rows.add("lead-001")
        self.run_script("run", str(path), "--concurrency", "2")
        with open(self.dir / "results.csv") as fh:
            statuses = {r["id"]: r["status"] for r in csv.DictReader(fh)}
        self.assertEqual(statuses["lead-001"], "FAILED")
        creates_before = len(self.fake.creates)
        self.run_script("run", str(path))
        self.assertEqual(len(self.fake.creates), creates_before, "failed rows aren't retried unless asked")
        self.fake.fail_rows.clear()
        self.run_script("run", str(path), "--retry-failed")
        self.assertEqual(len(self.fake.creates), creates_before + 1, "--retry-failed retries just the failed row")

    def test_bad_manifest_is_rejected_before_any_request(self):
        path = self.manifest([
            {"id": "a", "video": "presenter.mp4", "audio": "missing.wav"},
            {"id": "a", "video": "presenter.mp4", "script": "hi"},
        ])
        proc = self.run_script("run", str(path), check=False)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("is not a file", proc.stderr)
        self.assertIn("duplicate id a", proc.stderr)
        self.assertIn("script needs voice_id", proc.stderr)
        self.assertEqual(self.fake.creates, [])

    def test_estimate_sums_rows(self):
        path = self.manifest([{"id": "s1", "video": "presenter.mp4", "script": " ".join(["word"] * 25), "voice_id": "v"}])
        proc = self.run_script("estimate", str(path))
        self.assertIn("estimated total $1.20", proc.stdout)  # 25 words / 2.5 wps = 10 s * 0.12
        self.assertIn("approximate", proc.stdout)

    def test_estimate_respects_sync_mode_and_flags_unpriced_rows(self):
        video, voice, short = "11111111-1111-4111-8111-111111111111", "22222222-2222-4222-8222-222222222222", "33333333-3333-4333-8333-333333333333"
        self.fake.asset_durations.update({video: 60.0, voice: 5.0})
        path = self.manifest([{"id": "quiet-tail", "video": video, "audio": voice, "sync_mode": "silence"},
                              {"id": "trimmed", "video": video, "audio": voice, "sync_mode": "cut_off"}])
        proc = self.run_script("estimate", str(path))
        self.assertIn("estimated total $7.80", proc.stdout)  # silence bills 60 s, cut_off 5 s: 65 s * $0.12
        path = self.manifest([{"id": "known", "video": video, "audio": voice},
                              {"id": "unknown", "video": video, "audio": short}])
        proc = self.run_script("estimate", str(path), check=False)
        self.assertEqual(proc.returncode, 2, "an incomplete estimate must not look like a total")
        self.assertIn("Known subtotal $0.60 for 1 of 2 rows", proc.stdout)
        self.assertNotIn("estimated total", proc.stdout)

    def test_changed_row_is_refused_after_submission(self):
        path = self.six_rows()
        self.run_script("run", str(path), "--only", "lead-000")
        (self.dir / "vo0.wav").write_bytes(b"a different take")
        proc = self.run_script("run", str(path), "--only", "lead-000", check=False)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("changed after they were submitted: lead-000", proc.stderr)

    def test_missing_download_is_restored_without_a_new_generation(self):
        path = self.six_rows()
        self.run_script("run", str(path), "--only", "lead-000", "--out", str(self.dir / "a"))
        creates = len(self.fake.creates)
        self.run_script("run", str(path), "--only", "lead-000", "--out", str(self.dir / "b"))
        self.assertTrue((self.dir / "b" / "lead-000.mp4").exists())
        self.assertEqual(len(self.fake.creates), creates)

    def test_second_command_on_the_same_manifest_is_refused(self):
        import fcntl
        path = self.six_rows()
        with open(path.with_name(path.name + ".lock"), "a+") as held:
            fcntl.flock(held, fcntl.LOCK_EX)
            proc = self.run_script("run", str(path), check=False)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("already running", proc.stderr)
        self.assertEqual(self.fake.creates, [])

    def test_legacy_submission_state_blocks_duplicate_work(self):
        path = self.six_rows()
        state_path = path.with_name(path.name + ".state.json")
        for legacy, saved in (
            ({"submitting": True}, {}),
            ({"id": "previous-submission", "status": "PROCESSING"}, {}),
            ({"id": "previous-submission", "status": "COMPLETED"}, {}),
            ({"id": "previous-submission", "status": "FAILED"}, {}),
            ({"id": "previous-submission", "status": "COMPLETED"}, {"status": "COMPLETED"}),
            ({"id": "previous-submission", "status": "COMPLETED"}, {"status": "PROCESSING"}),
        ):
            with self.subTest(legacy=legacy, saved=saved):
                self.fake.reset()
                state_path.write_text(json.dumps({"batch": legacy, "rows": {"lead-000": {"mode": "batch", **saved}}}))
                proc = self.run_script("run", str(path), "--only", "lead-000", check=False)
                self.assertEqual(self.fake.creates, [], "old submission state must not create duplicate paid work")
                self.assertNotEqual(proc.returncode, 0)
                self.assertIn("unfinished work from an older script version", proc.stderr)

        gen_id = "confirmed-generation"
        self.fake.generations[gen_id] = {"status": "COMPLETED", "polls": 0, "name": "lead-000"}
        out = self.dir / "out"
        for saved, message in (
            ({"status": "COMPLETED", "outputUrl": f"{self.base}/signed/out/{gen_id}"}, "already completed"),
            ({"generationId": gen_id}, "lead-000: COMPLETED"),
            ({"status": "FAILED"}, "FAILED earlier"),
            ({"status": "REJECTED"}, "REJECTED earlier"),
        ):
            with self.subTest(saved=saved):
                state_path.write_text(json.dumps({
                    "batch": {"id": "previous-submission", "status": "COMPLETED"},
                    "rows": {"lead-000": {"mode": "batch", **saved}, "lead-001": {"mode": "batch"}},
                }))
                proc = self.run_script("run", str(path), "--only", "lead-000", "--out", str(out))
                self.assertEqual(self.fake.creates, [], "reconciled rows must reuse or report their saved outcome")
                self.assertIn(message, proc.stdout)
        self.assertTrue((out / "lead-000.mp4").exists())
        state_path.write_text(json.dumps({
            "batch": {"id": "previous-submission", "status": "COMPLETED"},
            "rows": {"lead-000": {"mode": "batch", "status": "FAILED"}},
        }))
        self.run_script("run", str(path), "--only", "lead-000", "--retry-failed")
        self.assertEqual(len(self.fake.creates), 1, "a confirmed failed row can be retried explicitly")
        self.assertEqual(json.loads(state_path.read_text())["rows"]["lead-000"]["status"], "COMPLETED")


if __name__ == "__main__":
    unittest.main()
