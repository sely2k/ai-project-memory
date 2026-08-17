import tempfile
import unittest
from pathlib import Path

import install


class ManagedInstructionTests(unittest.TestCase):
    def test_adds_block_without_replacing_existing_content(self):
        existing = "# Existing instructions\n\nKeep this rule.\n"
        merged, action = install.merge_managed_content(existing, "# RepoDoc\n\nRead the protocol.\n")

        self.assertTrue(merged.startswith(existing))
        self.assertIn("Keep this rule.", merged)
        self.assertEqual(merged.count(install.MANAGED_BLOCK_START), 1)
        self.assertEqual(action, "Added RepoDoc instructions to")

    def test_updates_only_the_managed_block(self):
        original, _ = install.merge_managed_content("User content\n", "Old RepoDoc content")
        updated, action = install.merge_managed_content(original, "New RepoDoc content")

        self.assertIn("User content", updated)
        self.assertNotIn("Old RepoDoc content", updated)
        self.assertIn("New RepoDoc content", updated)
        self.assertEqual(updated.count(install.MANAGED_BLOCK_START), 1)
        self.assertEqual(action, "Updated")

    def test_rejects_malformed_markers(self):
        with self.assertRaises(RuntimeError):
            install.merge_managed_content("<!-- repodoc:start -->\nbroken", "content")

    def test_installer_preserves_an_existing_agents_file(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            agents = target / "AGENTS.md"
            agents.write_text("# Team rules\n\nNever remove this.\n", encoding="utf-8")

            install.install_managed_file("codex/AGENTS.md", "AGENTS.md", "en", "owner/repo", target)

            result = agents.read_text(encoding="utf-8")
            self.assertIn("Never remove this.", result)
            self.assertIn("repodoc/memory-protocol.md", result)
            self.assertEqual(result.count(install.MANAGED_BLOCK_START), 1)


if __name__ == "__main__":
    unittest.main()
