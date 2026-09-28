# AI Project Memory

AI Project Memory is a bilingual, repository-backed memory protocol for ChatGPT Projects, Claude Projects, Claude Code, OpenAI Codex, and GitHub Copilot.

It gives AI assistants one versioned source of truth for established project knowledge. Conversations remain temporary working memory, while decisions, requirements, research, architecture, open questions, and durable context are consolidated in GitHub. Local CLI tools leave changes in the active working tree; remote chat tools use one persistent pull request.

## What this repository provides

- Italian and English versions of the memory protocol.
- Project instructions for ChatGPT and Claude.
- Repository instruction wrappers for Claude Code, Codex, and GitHub Copilot.
- RepoDoc agents for Claude Code, Codex, and GitHub Copilot: guided project bootstrap, read-only installation diagnostics, consistency, open-point resolution, SPEC synthesis and expansion, plus an implementation orchestrator and isolated implementation worker. Proposed work is created directly as `SPEC-xxx-<title>.yaml` with `status: proposed`; ready SPECs can be implemented sequentially with a fresh worker per SPEC. See [Installed layout](#installed-layout) and [Using the RepoDoc agents](#using-the-repodoc-agents) below.
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
2. the GitHub repository used as persistent memory (detected from `origin` when available; a bare repository name is automatically prefixed with the default owner `sely2k`);
3. ChatGPT Project, Claude Project, Claude Code, Codex, GitHub Copilot, or any combination through an interactive checkbox menu.

Use the arrow keys to navigate, Space to select or deselect a tool, and Enter to confirm. All available tools are selected by default.

It always installs the shared protocol and then the files required by the selected tools. ChatGPT Project and Claude Project instructions are generated as ready-to-paste files with repository placeholders and related setup notes already updated. Existing `AGENTS.md`, `.claude/CLAUDE.md`, and `.github/copilot-instructions.md` files are preserved: the installer adds or updates only a delimited RepoDoc-managed block. For other existing files, choose whether to skip them, overwrite them, or overwrite them and all following files.

After installation, ask the selected assistant to `Initialize RepoDoc for this project` to run the guided `repodoc-bootstrap` flow. Run `repodoc-doctor` whenever you want a read-only diagnosis of the local installation and document structure; it never changes files or checks for available updates.

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

Selecting all tools produces:

```text
<target-repository>/
├── .claude/
│   ├── CLAUDE.md
│   ├── agents/                          # memory agents plus repodoc-implement-specs.md and repodoc-implement-spec-worker.md
│   └── skills/repodoc-spec-expand/SKILL.md
├── .codex/agents/                       # memory agents plus repodoc-implement-specs.toml and repodoc-implement-spec-worker.toml
├── .github/
│   ├── copilot-instructions.md
│   └── agents/                          # memory agents plus repodoc-implement-specs.agent.md and repodoc-implement-spec-worker.agent.md
├── .agents/skills/repodoc-spec-expand/SKILL.md   # shared discovery path for Codex and Copilot CLI
├── repodoc/
│   ├── memory-protocol.md
│   ├── chatgpt-instruction.md
│   └── claude-chat-instruction.md
└── AGENTS.md
```

Paste `repodoc/chatgpt-instruction.md` and `repodoc/claude-chat-instruction.md` into the corresponding project settings. These files are installation artifacts for manual use; the applications do not read them directly from the repository. They live under `repodoc/` specifically so Codex CLI, GitHub Copilot, and Claude Code never pick them up as instructions: those tools only read `AGENTS.md`, `.github/copilot-instructions.md`, and `CLAUDE.md`/`.claude/CLAUDE.md` respectively.

The `.claude/agents/`, `.codex/agents/`, `.github/agents/`, and `.agents/skills/` files are installed for their selected tools. When invoked locally from a CLI, memory agents edit the active working tree without creating branches, commits, pushes, or PRs. Chat-originated memory work uses the persistent RepoDoc PR. Implementation agents keep their separate dedicated-code-branch policy. Each agent runs in the native format of its tool: Claude Code subagents (`.claude/agents/*.md`), Codex custom agents (`.codex/agents/*.toml`), and Copilot custom agents (`.github/agents/*.agent.md`).

## Using the RepoDoc agents

Once installed, each agent is just a normal custom agent (or skill) for its tool: describe what you want and the tool matches your request against the agent's `description`, or reference it by its `name` directly if your tool version supports explicit selection. None of them ever publishes a GitHub issue on its own — turning a `status: ready` spec into an actual issue is a separate, explicit step described in the backend's ["Publishing specs as issues"](en/repodoc/backends/github.md#publishing-specs-as-issues) section, only ever run on request.

| Agent | Run it when... | What it does |
|---|---|---|
| `repodoc-bootstrap` | immediately after installation, or when the project memory is still missing its basic context | Inspects existing repository evidence, asks only for missing context one question at a time, then creates the minimal initial memory using the active write mode. |
| `repodoc-doctor` | after installation or whenever the local RepoDoc structure may be incomplete or damaged | Checks versions, managed wrappers, agent formats, placeholders, links, indexes, and SPEC structure read-only; it reports remediation without changing anything or looking for updates. |
| `repodoc-consistency-check` | before integrating RepoDoc changes, or after a batch of doc edits | Audits the whole `repodoc/` memory backend for broken links, one-way cross-references, stale statuses, and duplicated sources of truth; fixes unambiguous issues and flags the rest for a decision. |
| `repodoc-close-openpoint` | you want to push one specific `OPEN-xxx-<title>` forward | Gathers evidence from linked documents (and, read-only, from the code) and either resolves it — creating or updating an ADR when it is a real decision — or updates it with what is still missing. |
| `repodoc-synthesize-specs` | right after closing a situation (a resolved OPEN, a new ADR, a completed batch of REQs) | Scans what that closure implies and records newly visible future work directly as minimal `SPEC-xxx-<title>.yaml` proposals with `status: proposed`. |
| `repodoc-spec-expand` (skill) | you want to detail **one** draft or proposed SPEC | Enriches the existing YAML in place with scope, ordered tasks, atomic subtasks, acceptance criteria, and relations. Expansion does not imply approval. |
| `repodoc-expand-specs` | you want to expand all or several draft/proposed SPECs in one pass | Processes the selected YAML files sequentially in the active write mode. On Claude Code it hands off each file to `repodoc-expand-spec-worker`; on Codex and Copilot it runs the same steps inline. |
| `repodoc-expand-spec-worker` (Claude Code only) | never directly | Internal sub-agent that `repodoc-expand-specs` spawns once per SPEC via the Task tool, so each expansion starts from a clean context and they never run in parallel on the same branch. |
| `repodoc-implement-specs` | you want to implement one or more ready SPECs | Validates and orders the selection, then launches a fresh isolated worker for each SPEC, one at a time. It coordinates and verifies but never writes implementation code. |
| `repodoc-implement-spec-worker` | never directly | Implements exactly one assigned ready SPEC on a dedicated code branch, runs its acceptance and regression checks, pushes it, and opens a PR or performs an explicitly authorized direct merge. |

The SPEC lifecycle is `draft → proposed → ready → submitted → closed`, with `rejected` and `superseded` as terminal alternatives. A SPEC becomes `ready` only when it is sufficiently detailed and explicitly approved; adding detail alone leaves it `proposed`.

`repodoc/specs/index.md` provides the overview that the old catalog used to provide without duplicating specification content. It lists every SPEC once, grouped into proposals, ready, published, closed, and archived sections; `repodoc/index.md` links to this specialized index.

Implementation defaults to a dedicated branch plus an unmerged pull request. Direct merge is used only when the current request says so explicitly. In either mode, the next SPEC starts only after the previous one is integrated or explicitly skipped.

### Implementing a SPEC train

Invoke `repodoc-implement-specs` with an explicit list or an unambiguous selector. Legacy groups previously expressed as headings in a feature catalog should become a shared SPEC `label` or `milestone`.

```text
Implement the ready SPECs with label rich-chat-capabilities, in dependency order.
Target branch: develop.
Integration mode: direct-merge.
Use a fresh isolated worker for every SPEC and stop on the first blocker.
```

Omitting the last two settings uses the repository default branch and `pull-request` mode. The agent reads the canonical SPEC files, so the prompt never needs to copy their titles, paths, tasks, or acceptance criteria.
