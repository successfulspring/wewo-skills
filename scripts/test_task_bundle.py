"""Exercise the shipped read-only task checker on real isolated file bundles.

These are deterministic artifact tests, not a simulation of an agent workflow.
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "skills/wewo-task/scripts/validate_task_bundle.py"
SPEC = importlib.util.spec_from_file_location("task_bundle", SCRIPT)
bundle = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bundle)


class TaskBundleTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="wewo-task-bundle-")
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)
        self.root = self.project / "docs/wewo/web-002/f-005"
        self.make_bundle(self.root, 2)

    def make_bundle(self, root, count):
        root.mkdir(parents=True)
        for name in ("prd.md", "technical-design.md"):
            (root / name).write_text("# Confirmed fixture\n", encoding="utf-8")
        links = []
        for number in range(1, count + 1):
            task_id = f"TASK-{number:03d}"
            task = root / "tasks" / task_id
            task.mkdir(parents=True)
            (task / "task.md").write_text(f"# {task_id} — Fixture work\n", encoding="utf-8")
            links.append(f"[{task_id}](tasks/{task_id}/task.md)")
        (root / "task-breakdown.md").write_text("\n".join(links), encoding="utf-8")

    def test_exact_count_and_read_only_check(self):
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual([], bundle.validate_bundle(self.root, 2))
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})
        self.assertTrue(bundle.validate_bundle(self.root, 1))
        self.assertTrue(bundle.validate_bundle(self.root, 3))

    def test_missing_and_invalid_counts_fail_cli(self):
        for value in (None, "0", "-1", "2.5", "two", "1-3", ""):
            with self.subTest(value=value):
                args = [sys.executable, "-B", str(SCRIPT), "--requirement-dir", str(self.root)]
                if value is not None:
                    args += ["--count", value]
                result = subprocess.run(args, capture_output=True, text=True)
                self.assertNotEqual(0, result.returncode)
        for value in (0, -1, True, 2.5, "2"):
            self.assertTrue(bundle.validate_bundle(self.root, value))
        with self.assertRaises(argparse.ArgumentTypeError):
            bundle.positive_count("02")

    def test_cli_valid_bundle(self):
        result = subprocess.run([sys.executable, "-B", str(SCRIPT), "--requirement-dir",
                                 str(self.root), "--count", "2"], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr + result.stdout)

    def test_missing_required_document_and_empty_task(self):
        (self.root / "prd.md").unlink()
        self.assertTrue(bundle.validate_bundle(self.root, 2))
        (self.root / "prd.md").write_text("# Confirmed fixture", encoding="utf-8")
        (self.root / "tasks/TASK-002/task.md").write_text("", encoding="utf-8")
        self.assertTrue(bundle.validate_bundle(self.root, 2))

    def test_stale_extra_directory_or_wrong_heading_fails(self):
        (self.root / "tasks/TASK-003").mkdir()
        self.assertTrue(bundle.validate_bundle(self.root, 2))
        (self.root / "tasks/TASK-003").rmdir()
        (self.root / "tasks/TASK-002/task.md").write_text("# TASK-001 — Wrong ID", encoding="utf-8")
        self.assertTrue(bundle.validate_bundle(self.root, 2))

    def test_ids_and_paths_cannot_disagree(self):
        original = self.root / "tasks/TASK-002"
        for name in ("TASK-2", "TASK-000", "TASK-003", "other"):
            with self.subTest(name=name):
                moved = original.with_name(name)
                original.rename(moved)
                self.assertTrue(bundle.validate_bundle(self.root, 2))
                moved.rename(original)

    def test_retained_stable_ids_need_not_be_renumbered(self):
        # Model an explicitly authorized revision; the helper does not grant it.
        (self.root / "tasks/TASK-001/task.md").unlink()
        (self.root / "tasks/TASK-001").rmdir()
        (self.root / "task-breakdown.md").write_text(
            "[TASK-002](tasks/TASK-002/task.md)", encoding="utf-8")
        self.assertEqual([], bundle.validate_bundle(self.root, 1))

    def test_external_citation_is_neither_read_nor_counted(self):
        with (self.root / "task-breakdown.md").open("a", encoding="utf-8") as stream:
            stream.write("\n[Authorized prerequisite](https://example.invalid/task.md)\n")
        self.assertEqual([], bundle.validate_bundle(self.root, 2))

    def test_links_must_match_this_bundle(self):
        path = self.root / "task-breakdown.md"
        for link in ("tasks/TASK-003/task.md", "../other/tasks/TASK-002/task.md",
                     "https://example.invalid/task.md", "tasks/TASK-002/../../task.md"):
            with self.subTest(link=link):
                path.write_text(f"[one](tasks/TASK-001/task.md)\n[two]({link})", encoding="utf-8")
                self.assertTrue(bundle.validate_bundle(self.root, 2))

    def test_other_branches_and_requirements_do_not_count(self):
        other = self.project / "docs/wewo/feature/cart/f-005"
        self.make_bundle(other, 3)
        sibling = self.project / "docs/wewo/web-002/f-006"
        self.make_bundle(sibling, 1)
        self.assertEqual([], bundle.validate_bundle(self.root, 2))
        self.assertEqual([], bundle.validate_bundle(other, 3))
        self.assertEqual([], bundle.validate_bundle(sibling, 1))

    def test_symlink_or_windows_junction_is_rejected(self):
        outside = self.project / "outside"
        outside.mkdir()
        link = self.root / "tasks/TASK-003"
        try:
            link.symlink_to(outside, target_is_directory=True)
        except OSError:
            if os.name != "nt":
                self.skipTest("symlink creation unavailable")
            # Creating a junction through native PowerShell does not require admin.
            result = subprocess.run(["powershell", "-NoProfile", "-Command",
                "New-Item -ItemType Junction -Path $env:WEWO_TEST_LINK -Target $env:WEWO_TEST_TARGET | Out-Null"],
                env={**os.environ, "WEWO_TEST_LINK": str(link), "WEWO_TEST_TARGET": str(outside)},
                capture_output=True, text=True)
            if result.returncode:
                self.skipTest("symlink/junction creation unavailable")
        try:
            self.assertTrue(bundle.validate_bundle(self.root, 3))
        finally:
            if link.is_symlink():
                link.unlink()
            else:
                link.rmdir()


if __name__ == "__main__":
    unittest.main()
