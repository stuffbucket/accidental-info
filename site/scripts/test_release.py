"""Tests for release.py. Run from the repo root:

    .venv/bin/python -m unittest discover -s site/scripts
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import release  # noqa: E402

GUIDE = dict(id="mcp", status="draft", title="Model Context Protocol", subtitle="A subtitle.",
             version="0.1.0", blurb="A blurb.", pdf="mcp.pdf", docx="mcp.docx")


class Release(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.folder = Path(self.tmp.name)
        (self.folder / "guides").mkdir()
        for name in ("mcp.pdf", "mcp.docx"):
            (self.folder / "guides" / name).write_bytes(b"")

    def tearDown(self):
        self.tmp.cleanup()

    def test_draft_is_a_prerelease_with_both_files(self):
        args = release.command(GUIDE, self.folder, "abc123")
        self.assertEqual(args[:4], ["gh", "release", "create", "mcp-v0.1.0"])
        self.assertEqual([Path(a).name for a in args[4:6]], ["mcp.pdf", "mcp.docx"])
        self.assertIn("Model Context Protocol 0.1.0", args)
        self.assertEqual(args[args.index("--target") + 1], "abc123")
        self.assertIn("--prerelease", args)

    def test_finished_guide_is_not_a_prerelease(self):
        guide = dict(GUIDE, status="published")
        self.assertNotIn("--prerelease", release.command(guide, self.folder))
        self.assertIn("https://stuffbucket.github.io/accidentalguide/guides/mcp/", release.notes(guide))

    def test_notes(self):
        text = release.notes(GUIDE)
        self.assertIn("A subtitle.\n\nA blurb.\n\n", text)
        self.assertIn("Read it online: https://stuffbucket.github.io/accidentalguide/drafts/mcp/", text)

    def test_missing_file_fails(self):
        (self.folder / "guides" / "mcp.docx").unlink()
        with self.assertRaises(SystemExit):
            release.command(GUIDE, self.folder)


if __name__ == "__main__":
    unittest.main()
