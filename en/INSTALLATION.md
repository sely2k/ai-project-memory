# Instruction file mapping

This language package contains the English templates to deploy into a target repository. Preserve filename casing exactly.

## Memory backend

The shared protocol is no longer a single file: `repodoc/memory-protocol.md` is **composed** by combining a backend-agnostic core with the operating rules of **one** backend chosen among:

| Backend | Source fragment | Placeholder |
|---|---|---|
| GitHub | `en/repodoc/backends/github.md` | `GITHUB_REPOSITORY: <owner>/<repo>` |
| Google Docs (preview: parameters only, no live writes yet) | `en/repodoc/backends/google-docs.md` | `GOOGLE_DRIVE_FOLDER: <folder>` |
| Notion (preview: parameters only, no live writes yet) | `en/repodoc/backends/notion.md` | `NOTION_PARENT_PAGE: <page>` |

`install.py` asks which backend to use, then composes `en/repodoc/memory-protocol-core.md` + the chosen backend fragment, substitutes the placeholder, and writes the result to `repodoc/memory-protocol.md`.

ChatGPT Project and Claude Project still assume a GitHub flow and are only offered when the chosen backend is GitHub.

| Tool | Source file | Target path | Installation |
|---|---|---|---|
| Shared protocol | `en/repodoc/memory-protocol-core.md` + `en/repodoc/backends/<backend>.md` | `repodoc/memory-protocol.md` | The installer composes both files and substitutes the chosen backend's placeholder. Every CLI wrapper references the resulting file. |
| Claude Code | `en/claude-code/CLAUDE.md` | `.claude/CLAUDE.md` | Create `.claude/` if needed. |
| OpenAI Codex CLI | `en/codex/AGENTS.md` | `AGENTS.md` | Copy to the repository root. |
| GitHub Copilot | `en/copilot/copilot-instructions.md` | `.github/copilot-instructions.md` | Create `.github/` if needed. |
| ChatGPT Project (GitHub backend only) | `en/chatgpt/instruction.md` | `repodoc/project-instructions/chatgpt.md` | The installer replaces `<owner>/<repo>`; then paste the content into Project instructions. |
| Claude Project (GitHub backend only) | `en/claude/instruction.md` | `repodoc/project-instructions/claude.md` | The installer replaces `<owner>/<repo>`; then paste the content into Project Instructions. |

## Resulting repository layout

```text
<target-repository>/
├── .claude/
│   └── CLAUDE.md
├── .github/
│   └── copilot-instructions.md
├── repodoc/
│   ├── memory-protocol.md
│   └── project-instructions/
│       ├── chatgpt.md
│       └── claude.md
└── AGENTS.md
```

## Notes

- The installer does not overwrite instructions already present in `AGENTS.md`, `.claude/CLAUDE.md`, or `.github/copilot-instructions.md`: it adds a block delimited by `<!-- repodoc:start -->` and `<!-- repodoc:end -->`, then updates only that block on later runs.
- Claude Code supports both root `CLAUDE.md` and `.claude/CLAUDE.md`; this project uses `.claude/CLAUDE.md`. Its import is therefore `@../repodoc/memory-protocol.md`.
- Codex reads root `AGENTS.md` and may layer additional files from nested directories.
- Copilot uses `.github/copilot-instructions.md` for repository-wide guidance. Path-specific rules can live under `.github/instructions/*.instructions.md`.
- The generated ChatGPT and Claude Project files are ready-to-paste copies for their respective interfaces; the applications do not read them directly from the repository.
