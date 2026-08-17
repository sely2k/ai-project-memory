# AI Project Memory

AI Project Memory is a bilingual, repository-backed memory protocol for ChatGPT Projects, Claude Projects, Claude Code, OpenAI Codex, and GitHub Copilot.

It gives AI assistants one versioned source of truth for established project knowledge. Conversations remain temporary working memory, while decisions, requirements, research, architecture, open questions, and durable context are consolidated in GitHub through one persistent pull request.

## What this repository provides

- Italian and English versions of the memory protocol.
- Project instructions for ChatGPT and Claude.
- Repository instruction wrappers for Claude Code, Codex, and GitHub Copilot.
- An interactive installer that places each file in the location expected by the selected tools.

The language packages are under [`it/`](it/INSTALLATION.md) and [`en/`](en/INSTALLATION.md). Each `INSTALLATION.md` contains the complete source-to-target file mapping.

## Quick install with uv

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), open a terminal in the repository you want to configure, and run:

```sh
uv run https://raw.githubusercontent.com/sely2k/ai-project-memory/main/install.py
```

The installer asks for:

1. Italian or English;
2. the GitHub repository, detected from `origin` when available; a bare repository name is automatically prefixed with the default owner `sely2k`;
3. ChatGPT Project, Claude Project, Claude Code, Codex, GitHub Copilot, or any combination through an interactive checkbox menu.

Use the arrow keys to navigate, Space to select or deselect a tool, and Enter to confirm. All five tools are selected by default.

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

Selecting all tools produces:

```text
<target-repository>/
├── .claude/CLAUDE.md
├── .github/copilot-instructions.md
├── repodoc/
│   ├── memory-protocol.md
│   └── project-instructions/
│       ├── chatgpt.md
│       └── claude.md
└── AGENTS.md
```

Paste `repodoc/project-instructions/chatgpt.md` and `repodoc/project-instructions/claude.md` into the corresponding project settings. These files are installation artifacts for manual use; the applications do not read them directly from the repository.
