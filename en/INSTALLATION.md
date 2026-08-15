# Instruction file mapping

This language package contains the English templates to deploy into a target repository. Preserve filename casing exactly.

| Tool | Source file | Target path | Installation |
|---|---|---|---|
| Shared protocol | `en/repodoc/memory-protocol.md` | `repodoc/memory-protocol.md` | Copy it; every CLI wrapper references it. |
| Claude Code | `en/claude-code/CLAUDE.md` | `.claude/CLAUDE.md` | Create `.claude/` if needed. |
| OpenAI Codex CLI | `en/codex/AGENTS.md` | `AGENTS.md` | Copy to the repository root. |
| GitHub Copilot | `en/copilot/copilot-instructions.md` | `.github/copilot-instructions.md` | Create `.github/` if needed. |
| ChatGPT Project | `en/chatgpt/instruction.md` | `repodoc/project-instructions/chatgpt.md` | The installer replaces `<owner>/<repo>`; then paste the content into Project instructions. |
| Claude Project | `en/claude/instruction.md` | `repodoc/project-instructions/claude.md` | The installer replaces `<owner>/<repo>`; then paste the content into Project Instructions. |

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

- Claude Code supports both root `CLAUDE.md` and `.claude/CLAUDE.md`; this project uses `.claude/CLAUDE.md`. Its import is therefore `@../repodoc/memory-protocol.md`.
- Codex reads root `AGENTS.md` and may layer additional files from nested directories.
- Copilot uses `.github/copilot-instructions.md` for repository-wide guidance. Path-specific rules can live under `.github/instructions/*.instructions.md`.
- The generated ChatGPT and Claude Project files are ready-to-paste copies for their respective interfaces; the applications do not read them directly from the repository.
