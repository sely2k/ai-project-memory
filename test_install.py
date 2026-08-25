import tempfile
import tomllib
import unittest
from pathlib import Path

import install

TEMPLATE_ROOT = Path(__file__).resolve().parent


class ManagedInstructionTests(unittest.TestCase):
    def test_remote_templates_use_cdn_with_github_fallback(self):
        urls = install.template_base_urls()

        self.assertEqual(urls[0], "https://cdn.jsdelivr.net/gh/sely2k/ai-project-memory@main")
        self.assertEqual(urls[1], "https://raw.githubusercontent.com/sely2k/ai-project-memory/main")

    def test_adds_block_without_replacing_existing_content(self):
        existing = "# Existing instructions\n\nKeep this rule.\n"
        content = "<!--\nTemplate comments.\n-->\n\n# RepoDoc\n\nRead the protocol.\n"
        merged, action = install.merge_managed_content(existing, content)

        self.assertTrue(merged.startswith(existing))
        self.assertIn("Keep this rule.", merged)
        self.assertEqual(merged.count(install.MANAGED_BLOCK_START), 1)
        self.assertIn(f"{install.MANAGED_BLOCK_START}\n{install.MANAGED_BLOCK_VERSION}\n# RepoDoc", merged)
        self.assertNotIn("Template comments.", merged)
        self.assertEqual(action, "Added RepoDoc instructions to")

    def test_updates_only_the_managed_block(self):
        original, _ = install.merge_managed_content("User content\n", "Old RepoDoc content")
        updated, action = install.merge_managed_content(original, "New RepoDoc content")

        self.assertIn("User content", updated)
        self.assertNotIn("Old RepoDoc content", updated)
        self.assertIn("New RepoDoc content", updated)
        self.assertEqual(updated.count(install.MANAGED_BLOCK_START), 1)
        self.assertEqual(updated.count(install.MANAGED_BLOCK_VERSION), 1)
        self.assertEqual(action, "Updated")

    def test_rejects_malformed_markers(self):
        with self.assertRaises(RuntimeError):
            install.merge_managed_content("<!-- repodoc:start -->\nbroken", "content")

    def test_installer_preserves_an_existing_agents_file(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            agents = target / "AGENTS.md"
            agents.write_text("# Team rules\n\nNever remove this.\n", encoding="utf-8")

            install.install_managed_file("codex/AGENTS.md", "AGENTS.md", "en", {"GITHUB_REPOSITORY": "owner/repo"}, target)

            result = agents.read_text(encoding="utf-8")
            self.assertIn("Never remove this.", result)
            self.assertIn("repodoc/memory-protocol.md", result)
            self.assertEqual(result.count(install.MANAGED_BLOCK_START), 1)


class InjectVersionTests(unittest.TestCase):
    def test_keeps_yaml_front_matter_at_the_very_start(self):
        content = "---\nname: repodoc-example\ndescription: x\n---\nBody text.\n"
        result = install.inject_version(content, ".claude/agents/repodoc-example.md")

        self.assertTrue(result.startswith("---\n"))
        self.assertIn(f"<!-- repodoc:version {install.REPODOC_VERSION} -->", result)
        self.assertIn("Body text.", result)

    def test_uses_a_toml_comment_for_toml_destinations(self):
        content = 'name = "repodoc-example"\n'
        result = install.inject_version(content, ".codex/agents/repodoc-example.toml")

        self.assertTrue(result.startswith(f"# repodoc:version {install.REPODOC_VERSION}"))
        tomllib.loads(result)

    def test_prepends_html_comment_for_plain_markdown(self):
        content = "# Title\n\nBody.\n"
        result = install.inject_version(content, "repodoc/claude-chat-instruction.md")

        self.assertTrue(result.startswith(f"<!-- repodoc:version {install.REPODOC_VERSION} -->"))


class AgentTemplateTests(unittest.TestCase):
    def test_every_agent_and_skill_source_exists_for_both_languages(self):
        for language in ("it", "en"):
            for files in install.AGENT_FILES.values():
                for source, _ in files:
                    path = TEMPLATE_ROOT / language / source
                    self.assertTrue(path.is_file(), f"missing template: {path}")
            skill_path = TEMPLATE_ROOT / language / install.SKILL_FILE
            self.assertTrue(skill_path.is_file(), f"missing skill template: {skill_path}")

    def test_codex_agent_templates_are_valid_toml_once_versioned(self):
        for language in ("it", "en"):
            for source, destination in install.AGENT_FILES["codex"]:
                content = (TEMPLATE_ROOT / language / source).read_text(encoding="utf-8")
                versioned = install.inject_version(content, destination)
                parsed = tomllib.loads(versioned)
                self.assertIn("name", parsed)
                self.assertIn("description", parsed)

    def test_claude_and_copilot_agent_templates_start_with_front_matter(self):
        for language in ("it", "en"):
            for tool in ("claude-code", "copilot"):
                for source, _ in install.AGENT_FILES[tool]:
                    content = (TEMPLATE_ROOT / language / source).read_text(encoding="utf-8")
                    self.assertTrue(content.startswith("---\n"), f"{language}/{source} is missing front matter")

    def test_skill_template_starts_with_front_matter(self):
        for language in ("it", "en"):
            content = (TEMPLATE_ROOT / language / install.SKILL_FILE).read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---\n"))


if __name__ == "__main__":
    unittest.main()
