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
    def test_github_is_the_only_supported_backend(self):
        for language in ("it", "en"):
            protocol = install.compose_protocol(language)
            self.assertIn("Backend: GitHub", protocol)
            self.assertNotIn("Backend: Notion", protocol)
            self.assertNotIn("Backend: Google Docs", protocol)

        self.assertEqual(install.GITHUB_BACKEND, "repodoc/backends/github.md")
        self.assertFalse((TEMPLATE_ROOT / "it/repodoc/backends/notion.md").exists())
        self.assertFalse((TEMPLATE_ROOT / "it/repodoc/backends/google-docs.md").exists())
        self.assertFalse((TEMPLATE_ROOT / "en/repodoc/backends/notion.md").exists())
        self.assertFalse((TEMPLATE_ROOT / "en/repodoc/backends/google-docs.md").exists())

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

    def test_spec_workflow_has_no_intermediate_feature_catalog(self):
        for language in ("it", "en"):
            sources = {
                install.SKILL_FILE,
                "repodoc/memory-protocol-core.md",
                "repodoc/backends/github.md",
            }
            for files in install.AGENT_FILES.values():
                sources.update(source for source, _ in files)

            for source in sources:
                content = (TEMPLATE_ROOT / language / source).read_text(encoding="utf-8")
                self.assertNotIn("features.md", content, f"legacy catalog reference in {language}/{source}")
                self.assertNotIn("specs-catalog", content, f"legacy catalog type in {language}/{source}")

    def test_protocol_defines_proposed_spec_lifecycle(self):
        expected_statuses = ("draft", "proposed", "ready", "submitted", "closed", "rejected", "superseded")
        for language in ("it", "en"):
            content = (TEMPLATE_ROOT / language / install.PROTOCOL_CORE).read_text(encoding="utf-8")
            for status in expected_statuses:
                self.assertIn(status, content)
            self.assertIn("summary:", content)
            self.assertIn("motivation:", content)
            self.assertIn("sources:", content)
            self.assertIn("body: null", content)

    def test_spec_index_is_defined_and_maintained_by_spec_agents(self):
        agent_sources = (
            "claude-code/agents/consistency-check.md",
            "claude-code/agents/synthesize-specs.md",
            "claude-code/agents/expand-specs.md",
            "claude-code/agents/expand-spec-worker.md",
            "codex/agents/consistency-check.toml",
            "codex/agents/synthesize-specs.toml",
            "codex/agents/expand-specs.toml",
            "copilot/agents/consistency-check.agent.md",
            "copilot/agents/synthesize-specs.agent.md",
            "copilot/agents/expand-specs.agent.md",
            install.SKILL_FILE,
        )
        for language in ("it", "en"):
            protocol = (TEMPLATE_ROOT / language / install.PROTOCOL_CORE).read_text(encoding="utf-8")
            github = (TEMPLATE_ROOT / language / "repodoc/backends/github.md").read_text(encoding="utf-8")
            self.assertIn("specs-index", protocol)
            self.assertIn("repodoc/specs/index.md", github)

            for source in agent_sources:
                content = (TEMPLATE_ROOT / language / source).read_text(encoding="utf-8")
                self.assertIn("repodoc/specs/index.md", content, f"missing specs index handling in {language}/{source}")

    def test_implementation_agents_use_one_fresh_worker_per_ready_spec(self):
        pairs = {
            "claude-code": ("claude-code/agents/implement-specs.md", "claude-code/agents/implement-spec-worker.md"),
            "codex": ("codex/agents/implement-specs.toml", "codex/agents/implement-spec-worker.toml"),
            "copilot": ("copilot/agents/implement-specs.agent.md", "copilot/agents/implement-spec-worker.agent.md"),
        }
        for language in ("it", "en"):
            for tool, (orchestrator_source, worker_source) in pairs.items():
                mapped_sources = {source for source, _ in install.AGENT_FILES[tool]}
                self.assertIn(orchestrator_source, mapped_sources)
                self.assertIn(worker_source, mapped_sources)

                orchestrator = (TEMPLATE_ROOT / language / orchestrator_source).read_text(encoding="utf-8")
                worker = (TEMPLATE_ROOT / language / worker_source).read_text(encoding="utf-8")
                for required in ("repodoc-implement-spec-worker", "ready", "pull-request", "direct-merge"):
                    self.assertIn(required, orchestrator)
                for required in ("SPEC_PATH", "TARGET_BRANCH", "IMPLEMENTATION_BRANCH", "INTEGRATION_MODE"):
                    self.assertIn(required, worker)

    def test_protocol_requires_isolated_spec_implementation_workers(self):
        for language in ("it", "en"):
            protocol = (TEMPLATE_ROOT / language / install.PROTOCOL_CORE).read_text(encoding="utf-8")
            self.assertIn("direct-merge", protocol)
            self.assertIn("pull request", protocol.lower())
            self.assertIn("worker", protocol.lower())

    def test_bootstrap_agents_gather_context_one_question_at_a_time(self):
        sources = (
            "claude-code/agents/bootstrap.md",
            "codex/agents/bootstrap.toml",
            "copilot/agents/bootstrap.agent.md",
        )
        for language in ("it", "en"):
            for source in sources:
                content = (TEMPLATE_ROOT / language / source).read_text(encoding="utf-8").lower()
                self.assertIn("repodoc/project.md", content)
                self.assertIn("repodoc/index.md", content)
                self.assertIn("one question at a time" if language == "en" else "una sola domanda alla volta", content)

    def test_cli_memory_agents_leave_git_integration_to_the_user(self):
        sources = (
            "claude-code/agents/bootstrap.md",
            "claude-code/agents/consistency-check.md",
            "claude-code/agents/close-openpoint.md",
            "claude-code/agents/synthesize-specs.md",
            "claude-code/agents/expand-specs.md",
            "claude-code/agents/expand-spec-worker.md",
            "codex/agents/bootstrap.toml",
            "codex/agents/consistency-check.toml",
            "codex/agents/close-openpoint.toml",
            "codex/agents/synthesize-specs.toml",
            "codex/agents/expand-specs.toml",
            install.SKILL_FILE,
        )
        for language in ("it", "en"):
            prohibition = "non creare o cambiare branch" if language == "it" else "do not create or switch branches"
            for source in sources:
                content = (TEMPLATE_ROOT / language / source).read_text(encoding="utf-8").lower()
                self.assertIn("working tree", content, f"missing local working-tree policy in {language}/{source}")
                self.assertIn(prohibition, content, f"missing branch prohibition in {language}/{source}")

    def test_github_protocol_distinguishes_cli_from_chat(self):
        for language in ("it", "en"):
            github = (TEMPLATE_ROOT / language / install.GITHUB_BACKEND).read_text(encoding="utf-8").lower()
            self.assertIn("local cli" if language == "en" else "cli locale", github)
            self.assertIn("remote chat" if language == "en" else "chat remota", github)
            self.assertIn("do not create or switch branches" if language == "en" else "non creare o cambiare branch", github)
            self.assertIn("persistent" if language == "en" else "persistente", github)

            for source in ("chatgpt/instruction.md", "claude/instruction.md"):
                content = (TEMPLATE_ROOT / language / source).read_text(encoding="utf-8").lower()
                self.assertIn("chat mode" if language == "en" else "modalità chat", content)
                self.assertIn("persistent" if language == "en" else "persistente", content)

            for source in (
                "copilot/agents/bootstrap.agent.md",
                "copilot/agents/consistency-check.agent.md",
                "copilot/agents/close-openpoint.agent.md",
                "copilot/agents/synthesize-specs.agent.md",
                "copilot/agents/expand-specs.agent.md",
            ):
                content = (TEMPLATE_ROOT / language / source).read_text(encoding="utf-8").lower()
                self.assertIn("copilot cli", content)
                self.assertIn("chat", content)

    def test_doctor_agents_are_read_only_and_do_not_check_updates(self):
        sources = (
            "claude-code/agents/doctor.md",
            "codex/agents/doctor.toml",
            "copilot/agents/doctor.agent.md",
        )
        for language in ("it", "en"):
            for source in sources:
                content = (TEMPLATE_ROOT / language / source).read_text(encoding="utf-8").lower()
                self.assertIn("read-only", content)
                self.assertIn("pass", content)
                self.assertIn("warn", content)
                self.assertIn("error", content)
                self.assertIn("skip", content)
                self.assertIn("do not check" if language == "en" else "non verificare", content)

            claude_doctor = (TEMPLATE_ROOT / language / sources[0]).read_text(encoding="utf-8")
            front_matter = claude_doctor.split("---", 2)[1]
            self.assertNotIn("Edit", front_matter)
            self.assertNotIn("Write", front_matter)


if __name__ == "__main__":
    unittest.main()
