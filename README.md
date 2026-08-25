# AI Project Memory

AI Project Memory is a bilingual, repository-backed memory protocol for ChatGPT Projects, Claude Projects, Claude Code, OpenAI Codex, and GitHub Copilot.

It gives AI assistants one versioned source of truth for established project knowledge. Conversations remain temporary working memory, while decisions, requirements, research, architecture, open questions, and durable context are consolidated in GitHub through one persistent pull request.

## What this repository provides

- Italian and English versions of the memory protocol.
- Project instructions for ChatGPT and Claude.
- Repository instruction wrappers for Claude Code, Codex, and GitHub Copilot.
- RepoDoc agents (GitHub backend only) for Claude Code, Codex, and GitHub Copilot: a consistency-check agent, a close-open-point agent, a synthesize-specs agent, and an expand-all-specs agent (which on Claude Code delegates each spec to a dedicated sub-agent), plus a `repodoc-spec-expand` skill that turns one high-level spec into a full `SPEC-xxx-<title>.yaml` file. See [Installed layout](#installed-layout) and [Using the RepoDoc agents](#using-the-repodoc-agents) below.
- An interactive installer that places each file in the location expected by the selected tools.

The language packages are under [`it/`](it/INSTALLATION.md) and [`en/`](en/INSTALLATION.md). Each `INSTALLATION.md` contains the complete source-to-target file mapping.

## Quick install with uv

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), open a terminal in the repository you want to configure, and run:

```sh
uv run https://raw.githubusercontent.com/sely2k/ai-project-memory/main/install.py
```

The command downloads the installer directly from the repository through GitHub Raw.

The installer asks for:

1. Italian or English;
2. the memory backend — GitHub, Google Docs, or Notion (only one; Google Docs and Notion are currently preview: the installer collects the target folder/page but does not yet write to them);
3. the backend-specific target: the GitHub repository (detected from `origin` when available; a bare repository name is automatically prefixed with the default owner `sely2k`), the Google Drive folder, or the Notion parent page;
4. ChatGPT Project, Claude Project, Claude Code, Codex, GitHub Copilot, or any combination through an interactive checkbox menu. ChatGPT Project and Claude Project are only offered when the backend is GitHub.

Use the arrow keys to navigate, Space to select or deselect a tool, and Enter to confirm. All available tools are selected by default.

It always installs the shared protocol and then the files required by the selected tools. ChatGPT Project and Claude Project instructions are generated as ready-to-paste files with repository placeholders and related setup notes already updated. Existing `AGENTS.md`, `.claude/CLAUDE.md`, and `.github/copilot-instructions.md` files are preserved: the installer adds or updates only a delimited RepoDoc-managed block. For other existing files, choose whether to skip them, overwrite them, or overwrite them and all following files.

The source repository and branch are configured near the top of [`install.py`](install.py):

```python
SOURCE_REPOSITORY = "https://github.com/sely2k/ai-project-memory"
SOURCE_BRANCH = "main"
```

Change these values if you publish the templates under another repository or branch.

## Local installation

Clone this repository, change to the target repository, and run the installer by absolute or relative path:

```sh
git clone https://github.com/sely2k/ai-project-memory.git
cd /path/to/target-repository
uv run /path/to/ai-project-memory/install.py
```

When the templates are available beside `install.py`, the installer reads them locally. Otherwise, it downloads them from `SOURCE_REPOSITORY`.

## Installed layout

Selecting all tools with the GitHub backend produces:

```text
<target-repository>/
├── .claude/
│   ├── CLAUDE.md
│   ├── agents/                          # repodoc-consistency-check.md, repodoc-close-openpoint.md, repodoc-synthesize-specs.md, repodoc-expand-specs.md, repodoc-expand-spec-worker.md
│   └── skills/repodoc-spec-expand/SKILL.md
├── .codex/agents/                       # repodoc-consistency-check.toml, repodoc-close-openpoint.toml, repodoc-synthesize-specs.toml, repodoc-expand-specs.toml
├── .github/
│   ├── copilot-instructions.md
│   └── agents/                          # repodoc-consistency-check.agent.md, repodoc-close-openpoint.agent.md, repodoc-synthesize-specs.agent.md, repodoc-expand-specs.agent.md
├── .agents/skills/repodoc-spec-expand/SKILL.md   # shared discovery path for Codex and Copilot CLI
├── repodoc/
│   ├── memory-protocol.md
│   ├── chatgpt-instruction.md
│   └── claude-chat-instruction.md
└── AGENTS.md
```

Paste `repodoc/chatgpt-instruction.md` and `repodoc/claude-chat-instruction.md` into the corresponding project settings. These files are installation artifacts for manual use; the applications do not read them directly from the repository. They live under `repodoc/` specifically so Codex CLI, GitHub Copilot, and Claude Code never pick them up as instructions: those tools only read `AGENTS.md`, `.github/copilot-instructions.md`, and `CLAUDE.md`/`.claude/CLAUDE.md` respectively.

The `.claude/agents/`, `.codex/agents/`, `.github/agents/`, and `.agents/skills/` files are installed only for the GitHub backend, since they operate the persistent-PR flow described in [`en/repodoc/backends/github.md`](en/repodoc/backends/github.md#repodoc-agents). Each agent runs in the native format of its tool: Claude Code subagents (`.claude/agents/*.md`), Codex custom agents (`.codex/agents/*.toml`), and Copilot CLI custom agents (`.github/agents/*.agent.md`). The `repodoc-spec-expand` skill is one source file, copied to `.claude/skills/` for Claude Code and to the shared `.agents/skills/` path that both Codex and Copilot CLI discover.

## Using the RepoDoc agents

Once installed, each agent is just a normal custom agent (or skill) for its tool: describe what you want and the tool matches your request against the agent's `description`, or reference it by its `name` directly if your tool version supports explicit selection. None of them ever publishes a GitHub issue on its own — turning a `status: ready` spec into an actual issue is a separate, explicit step described in the backend's ["Publishing specs as issues"](en/repodoc/backends/github.md#publishing-specs-as-issues) section, only ever run on request.

| Agent | Run it when... | What it does |
|---|---|---|
| `repodoc-consistency-check` | before merging the persistent RepoDoc PR, or after a batch of doc edits | Audits the whole `repodoc/` memory backend for broken links, one-way cross-references, stale statuses, and duplicated sources of truth; fixes unambiguous issues and flags the rest for a decision. |
| `repodoc-close-openpoint` | you want to push one specific `OPEN-xxx-<title>` forward | Gathers evidence from linked documents (and, read-only, from the code) and either resolves it — creating or updating an ADR when it is a real decision — or updates it with what is still missing. |
| `repodoc-synthesize-specs` | right after closing a situation (a resolved OPEN, a new ADR, a completed batch of REQs) | Scans what that closure implies and records any newly visible future work as short entries in the `repodoc/specs/features.md` catalog — no detail yet, just a pointer to expand later. |
| `repodoc-spec-expand` (skill) | you want to detail **one** specific catalog entry right now | Give it the `SPEC_NUMBER`/`SPEC_TITLE`; it turns that single entry into a complete `SPEC-xxx-<title>.yaml` (problem, proposal, scope, ordered tasks, atomic subtasks, acceptance criteria, relations to other specs), replacing the catalog line with a link to the new file. |
| `repodoc-expand-specs` | you want to clear out the **whole catalog** (or several entries) in one pass | Resolves the persistent PR branch once, then processes every not-yet-formalized catalog entry, one at a time, producing the same detailed YAML as `repodoc-spec-expand` for each. On Claude Code it hands off each entry to `repodoc-expand-spec-worker`; on Codex and Copilot, which have no sub-agent mechanism to delegate to here, it runs the same steps inline instead, one entry at a time. |
| `repodoc-expand-spec-worker` (Claude Code only) | never directly | Internal sub-agent that `repodoc-expand-specs` spawns once per catalog entry via the Task tool, so each expansion starts from a clean context and they never run in parallel on the same branch. To expand a single spec by hand, use the `repodoc-spec-expand` skill instead. |
