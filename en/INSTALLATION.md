# Instruction file mapping

This language package contains the English templates to deploy into a target repository. Preserve filename casing exactly.

## Memory backend

GitHub is the supported memory backend. `install.py` composes `en/repodoc/memory-protocol-core.md` with `en/repodoc/backends/github.md`, substitutes `GITHUB_REPOSITORY: <owner>/<repo>`, and writes the result to `repodoc/memory-protocol.md`.

| Tool | Source file | Target path | Installation |
|---|---|---|---|
| Shared protocol | `en/repodoc/memory-protocol-core.md` + `en/repodoc/backends/github.md` | `repodoc/memory-protocol.md` | The installer composes both files and substitutes the GitHub repository. Every CLI wrapper references the resulting file. |
| Claude Code | `en/claude-code/CLAUDE.md` | `.claude/CLAUDE.md` | Create `.claude/` if needed. |
| OpenAI Codex CLI | `en/codex/AGENTS.md` | `AGENTS.md` | Copy to the repository root. |
| GitHub Copilot | `en/copilot/copilot-instructions.md` | `.github/copilot-instructions.md` | Create `.github/` if needed. |
| ChatGPT Project | `en/chatgpt/instruction.md` | `repodoc/chatgpt-instruction.md` | The installer replaces `<owner>/<repo>`; then paste the content into Project instructions. |
| Claude Project | `en/claude/instruction.md` | `repodoc/claude-chat-instruction.md` | The installer replaces `<owner>/<repo>`; then paste the content into Project Instructions. |

### RepoDoc agents

Besides the base instructions file, for each selected tool the installer also copies the dedicated agents defined in `install.py` (`AGENT_FILES`) and the spec-expansion skill (`SKILL_FILE`/`SKILL_DESTINATIONS`). From a CLI, memory agents edit the active working tree without creating branches, commits, pushes, or PRs; from chat they use the persistent PR. `repodoc-doctor` is always read-only, while implementation agents retain their dedicated code-branch flow.

| Tool | Source file | Target path in the target repository |
|---|---|---|
| Claude Code | `en/claude-code/agents/bootstrap.md` | `.claude/agents/repodoc-bootstrap.md` |
| Claude Code | `en/claude-code/agents/doctor.md` | `.claude/agents/repodoc-doctor.md` |
| Claude Code | `en/claude-code/agents/consistency-check.md` | `.claude/agents/repodoc-consistency-check.md` |
| Claude Code | `en/claude-code/agents/close-openpoint.md` | `.claude/agents/repodoc-close-openpoint.md` |
| Claude Code | `en/claude-code/agents/synthesize-specs.md` | `.claude/agents/repodoc-synthesize-specs.md` |
| Claude Code | `en/claude-code/agents/expand-specs.md` | `.claude/agents/repodoc-expand-specs.md` |
| Claude Code | `en/claude-code/agents/expand-spec-worker.md` | `.claude/agents/repodoc-expand-spec-worker.md` |
| Claude Code | `en/claude-code/agents/implement-specs.md` | `.claude/agents/repodoc-implement-specs.md` |
| Claude Code | `en/claude-code/agents/implement-spec-worker.md` | `.claude/agents/repodoc-implement-spec-worker.md` |
| Claude Code | `en/skills/spec-expand/SKILL.md` | `.claude/skills/repodoc-spec-expand/SKILL.md` |
| OpenAI Codex CLI | `en/codex/agents/bootstrap.toml` | `.codex/agents/repodoc-bootstrap.toml` |
| OpenAI Codex CLI | `en/codex/agents/doctor.toml` | `.codex/agents/repodoc-doctor.toml` |
| OpenAI Codex CLI | `en/codex/agents/consistency-check.toml` | `.codex/agents/repodoc-consistency-check.toml` |
| OpenAI Codex CLI | `en/codex/agents/close-openpoint.toml` | `.codex/agents/repodoc-close-openpoint.toml` |
| OpenAI Codex CLI | `en/codex/agents/synthesize-specs.toml` | `.codex/agents/repodoc-synthesize-specs.toml` |
| OpenAI Codex CLI | `en/codex/agents/expand-specs.toml` | `.codex/agents/repodoc-expand-specs.toml` |
| OpenAI Codex CLI | `en/codex/agents/implement-specs.toml` | `.codex/agents/repodoc-implement-specs.toml` |
| OpenAI Codex CLI | `en/codex/agents/implement-spec-worker.toml` | `.codex/agents/repodoc-implement-spec-worker.toml` |
| OpenAI Codex CLI | `en/skills/spec-expand/SKILL.md` | `.agents/skills/repodoc-spec-expand/SKILL.md` |
| GitHub Copilot | `en/copilot/agents/bootstrap.agent.md` | `.github/agents/repodoc-bootstrap.agent.md` |
| GitHub Copilot | `en/copilot/agents/doctor.agent.md` | `.github/agents/repodoc-doctor.agent.md` |
| GitHub Copilot | `en/copilot/agents/consistency-check.agent.md` | `.github/agents/repodoc-consistency-check.agent.md` |
| GitHub Copilot | `en/copilot/agents/close-openpoint.agent.md` | `.github/agents/repodoc-close-openpoint.agent.md` |
| GitHub Copilot | `en/copilot/agents/synthesize-specs.agent.md` | `.github/agents/repodoc-synthesize-specs.agent.md` |
| GitHub Copilot | `en/copilot/agents/expand-specs.agent.md` | `.github/agents/repodoc-expand-specs.agent.md` |
| GitHub Copilot | `en/copilot/agents/implement-specs.agent.md` | `.github/agents/repodoc-implement-specs.agent.md` |
| GitHub Copilot | `en/copilot/agents/implement-spec-worker.agent.md` | `.github/agents/repodoc-implement-spec-worker.agent.md` |
| GitHub Copilot | `en/skills/spec-expand/SKILL.md` | `.agents/skills/repodoc-spec-expand/SKILL.md` (skipped if Codex already wrote it) |

The `repodoc-spec-expand` skill is authored once and copied to whichever native discovery path each selected tool uses: `.claude/skills/` for Claude Code, `.agents/skills/` for Codex and Copilot CLI (which share it). If both Codex and Copilot are selected, the file is written only once.

## Resulting repository layout

```text
<target-repository>/
├── .claude/
│   ├── CLAUDE.md
│   ├── agents/
│   │   ├── repodoc-bootstrap.md
│   │   ├── repodoc-doctor.md
│   │   ├── repodoc-consistency-check.md
│   │   ├── repodoc-close-openpoint.md
│   │   ├── repodoc-synthesize-specs.md
│   │   ├── repodoc-expand-specs.md
│   │   ├── repodoc-expand-spec-worker.md
│   │   ├── repodoc-implement-specs.md
│   │   └── repodoc-implement-spec-worker.md
│   └── skills/
│       └── repodoc-spec-expand/SKILL.md
├── .codex/
│   └── agents/
│       ├── repodoc-bootstrap.toml
│       ├── repodoc-doctor.toml
│       ├── repodoc-consistency-check.toml
│       ├── repodoc-close-openpoint.toml
│       ├── repodoc-synthesize-specs.toml
│       ├── repodoc-expand-specs.toml
│       ├── repodoc-implement-specs.toml
│       └── repodoc-implement-spec-worker.toml
├── .github/
│   ├── copilot-instructions.md
│   └── agents/
│       ├── repodoc-bootstrap.agent.md
│       ├── repodoc-doctor.agent.md
│       ├── repodoc-consistency-check.agent.md
│       ├── repodoc-close-openpoint.agent.md
│       ├── repodoc-synthesize-specs.agent.md
│       ├── repodoc-expand-specs.agent.md
│       ├── repodoc-implement-specs.agent.md
│       └── repodoc-implement-spec-worker.agent.md
├── .agents/
│   └── skills/
│       └── repodoc-spec-expand/SKILL.md
├── repodoc/
│   ├── memory-protocol.md
│   ├── chatgpt-instruction.md
│   └── claude-chat-instruction.md
└── AGENTS.md
```

## Notes

- The installer does not overwrite instructions already present in `AGENTS.md`, `.claude/CLAUDE.md`, or `.github/copilot-instructions.md`: it adds a block delimited by `<!-- repodoc:start -->` and `<!-- repodoc:end -->`, then updates only that block on later runs.
- Claude Code supports both root `CLAUDE.md` and `.claude/CLAUDE.md`; this project uses `.claude/CLAUDE.md`. Its import is therefore `@../repodoc/memory-protocol.md`.
- Codex reads root `AGENTS.md` and may layer additional files from nested directories.
- Copilot uses `.github/copilot-instructions.md` for repository-wide guidance. Path-specific rules can live under `.github/instructions/*.instructions.md`.
- The generated ChatGPT and Claude Project files are ready-to-paste copies for their respective interfaces; the applications do not read them directly from the repository. They live under `repodoc/` on purpose, so Codex CLI, GitHub Copilot, and Claude Code never risk reading and interpreting them as instructions: those tools only read `AGENTS.md`, `.github/copilot-instructions.md`, and `CLAUDE.md`/`.claude/CLAUDE.md` respectively.
