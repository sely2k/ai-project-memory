# Installazione delle istruzioni

Questa repository contiene file sorgente da distribuire nei progetti target. Copia ogni file nel percorso indicato, mantenendo esattamente maiuscole e minuscole.

## Backend di memoria

GitHub è il backend di memoria supportato. `install.py` compone `it/repodoc/memory-protocol-core.md` con `it/repodoc/backends/github.md`, sostituisce `GITHUB_REPOSITORY: <owner>/<repo>` e scrive il risultato in `repodoc/memory-protocol.md`.

## Mappa dei file

| Strumento | File sorgente | Destinazione nel repository target | Installazione |
|---|---|---|---|
| Protocollo condiviso | `it/repodoc/memory-protocol-core.md` + `it/repodoc/backends/github.md` | `repodoc/memory-protocol.md` | L'installer compone i due file e sostituisce il repository GitHub. Tutte le istruzioni CLI referenziano il file risultante. |
| Claude Code | `it/claude-code/CLAUDE.md` | `.claude/CLAUDE.md` | Copia il file creando `.claude/` se necessario. |
| OpenAI Codex CLI | `it/codex/AGENTS.md` | `AGENTS.md` | Copia nella root del repository. |
| GitHub Copilot | `it/copilot/copilot-instructions.md` | `.github/copilot-instructions.md` | Copia il file creando `.github/` se necessario. |
| ChatGPT Project | `it/chatgpt/instruction.md` | `repodoc/chatgpt-instruction.md` | L'installer sostituisce `<owner>/<repo>`; incolla poi il contenuto nelle istruzioni del Project. |
| Claude Project | `it/claude/instruction.md` | `repodoc/claude-chat-instruction.md` | L'installer sostituisce `<owner>/<repo>`; incolla poi il contenuto nelle Project Instructions. |

### Agenti RepoDoc

Oltre al file di istruzioni base, per ciascuno strumento selezionato l'installer copia anche gli agenti dedicati definiti in `install.py` (`AGENT_FILES`) e la skill di espansione specifiche (`SKILL_FILE`/`SKILL_DESTINATIONS`). Da CLI gli agenti di memoria modificano il working tree attivo senza creare branch, commit, push o PR; dalla chat usano la PR persistente. `repodoc-doctor` è sempre read-only e gli agenti implementativi conservano il proprio flusso su branch di codice dedicati.

| Strumento | File sorgente | Destinazione nel repository target |
|---|---|---|
| Claude Code | `it/claude-code/agents/bootstrap.md` | `.claude/agents/repodoc-bootstrap.md` |
| Claude Code | `it/claude-code/agents/doctor.md` | `.claude/agents/repodoc-doctor.md` |
| Claude Code | `it/claude-code/agents/consistency-check.md` | `.claude/agents/repodoc-consistency-check.md` |
| Claude Code | `it/claude-code/agents/close-openpoint.md` | `.claude/agents/repodoc-close-openpoint.md` |
| Claude Code | `it/claude-code/agents/synthesize-specs.md` | `.claude/agents/repodoc-synthesize-specs.md` |
| Claude Code | `it/claude-code/agents/expand-specs.md` | `.claude/agents/repodoc-expand-specs.md` |
| Claude Code | `it/claude-code/agents/expand-spec-worker.md` | `.claude/agents/repodoc-expand-spec-worker.md` |
| Claude Code | `it/claude-code/agents/implement-specs.md` | `.claude/agents/repodoc-implement-specs.md` |
| Claude Code | `it/claude-code/agents/implement-spec-worker.md` | `.claude/agents/repodoc-implement-spec-worker.md` |
| Claude Code | `it/skills/spec-expand/SKILL.md` | `.claude/skills/repodoc-spec-expand/SKILL.md` |
| OpenAI Codex CLI | `it/codex/agents/bootstrap.toml` | `.codex/agents/repodoc-bootstrap.toml` |
| OpenAI Codex CLI | `it/codex/agents/doctor.toml` | `.codex/agents/repodoc-doctor.toml` |
| OpenAI Codex CLI | `it/codex/agents/consistency-check.toml` | `.codex/agents/repodoc-consistency-check.toml` |
| OpenAI Codex CLI | `it/codex/agents/close-openpoint.toml` | `.codex/agents/repodoc-close-openpoint.toml` |
| OpenAI Codex CLI | `it/codex/agents/synthesize-specs.toml` | `.codex/agents/repodoc-synthesize-specs.toml` |
| OpenAI Codex CLI | `it/codex/agents/expand-specs.toml` | `.codex/agents/repodoc-expand-specs.toml` |
| OpenAI Codex CLI | `it/codex/agents/implement-specs.toml` | `.codex/agents/repodoc-implement-specs.toml` |
| OpenAI Codex CLI | `it/codex/agents/implement-spec-worker.toml` | `.codex/agents/repodoc-implement-spec-worker.toml` |
| OpenAI Codex CLI | `it/skills/spec-expand/SKILL.md` | `.agents/skills/repodoc-spec-expand/SKILL.md` |
| GitHub Copilot | `it/copilot/agents/bootstrap.agent.md` | `.github/agents/repodoc-bootstrap.agent.md` |
| GitHub Copilot | `it/copilot/agents/doctor.agent.md` | `.github/agents/repodoc-doctor.agent.md` |
| GitHub Copilot | `it/copilot/agents/consistency-check.agent.md` | `.github/agents/repodoc-consistency-check.agent.md` |
| GitHub Copilot | `it/copilot/agents/close-openpoint.agent.md` | `.github/agents/repodoc-close-openpoint.agent.md` |
| GitHub Copilot | `it/copilot/agents/synthesize-specs.agent.md` | `.github/agents/repodoc-synthesize-specs.agent.md` |
| GitHub Copilot | `it/copilot/agents/expand-specs.agent.md` | `.github/agents/repodoc-expand-specs.agent.md` |
| GitHub Copilot | `it/copilot/agents/implement-specs.agent.md` | `.github/agents/repodoc-implement-specs.agent.md` |
| GitHub Copilot | `it/copilot/agents/implement-spec-worker.agent.md` | `.github/agents/repodoc-implement-spec-worker.agent.md` |
| GitHub Copilot | `it/skills/spec-expand/SKILL.md` | `.agents/skills/repodoc-spec-expand/SKILL.md` (se non già scritto da Codex) |

La skill `repodoc-spec-expand` è un unico contenuto sorgente, copiato nel percorso di scoperta nativo di ciascuno strumento selezionato: `.claude/skills/` per Claude Code, `.agents/skills/` per Codex e Copilot CLI (che lo condividono). Se sia Codex sia Copilot sono selezionati, il file viene scritto una sola volta.

## Struttura risultante

```text
<repository-target>/
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

## Copia manuale

Esegui dalla root di questa repository, sostituendo `<repository-target>` con il percorso del progetto da configurare:

```sh
mkdir -p <repository-target>/.claude \
         <repository-target>/.github \
         <repository-target>/repodoc

cp it/claude-code/CLAUDE.md <repository-target>/.claude/CLAUDE.md
cp it/codex/AGENTS.md <repository-target>/AGENTS.md
cp it/copilot/copilot-instructions.md <repository-target>/.github/copilot-instructions.md

cat it/repodoc/memory-protocol-core.md it/repodoc/backends/github.md > <repository-target>/repodoc/memory-protocol.md
# poi sostituisci a mano <owner>/<repo> nel file appena creato

cp it/chatgpt/instruction.md <repository-target>/repodoc/chatgpt-instruction.md
cp it/claude/instruction.md <repository-target>/repodoc/claude-chat-instruction.md
```

## Note

- L'installer non sovrascrive eventuali istruzioni già presenti in `AGENTS.md`, `.claude/CLAUDE.md` o `.github/copilot-instructions.md`: aggiunge un blocco delimitato da `<!-- repodoc:start -->` e `<!-- repodoc:end -->`, aggiornando solo quel blocco nelle esecuzioni successive.
- Claude Code riconosce sia `CLAUDE.md` nella root sia `.claude/CLAUDE.md`; questa repository adotta `.claude/CLAUDE.md`. Poiché gli import `@path` sono relativi al file che li contiene, il wrapper usa `@../repodoc/memory-protocol.md`.
- Codex carica `AGENTS.md` dalla root e può applicare file aggiuntivi nelle sottodirectory.
- Copilot usa `.github/copilot-instructions.md` per le istruzioni valide in tutto il repository. Le regole mirate possono essere aggiunte in `.github/instructions/*.instructions.md`.
- I file generati per ChatGPT Project e Claude Project sono copie pronte da incollare nelle rispettive interfacce; le applicazioni non li leggono direttamente dal repository. Risiedono sotto `repodoc/` apposta, così Codex CLI, GitHub Copilot e Claude Code non rischiano di leggerli e interpretarli come istruzioni: questi strumenti leggono solo, rispettivamente, `AGENTS.md`, `.github/copilot-instructions.md` e `CLAUDE.md`/`.claude/CLAUDE.md`.
