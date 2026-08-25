# Installazione delle istruzioni

Questa repository contiene file sorgente da distribuire nei progetti target. Copia ogni file nel percorso indicato, mantenendo esattamente maiuscole e minuscole.

## Backend di memoria

Il protocollo condiviso non è più un file singolo: `repodoc/memory-protocol.md` viene **composto** unendo un core indipendente dal backend con le regole operative di **un solo backend** scelto tra:

| Backend | Frammento sorgente | Placeholder |
|---|---|---|
| GitHub | `it/repodoc/backends/github.md` | `GITHUB_REPOSITORY: <owner>/<repo>` |
| Google Docs (anteprima: solo parametri, scrittura reale non ancora attiva) | `it/repodoc/backends/google-docs.md` | `GOOGLE_DRIVE_FOLDER: <cartella>` |
| Notion (anteprima: solo parametri, scrittura reale non ancora attiva) | `it/repodoc/backends/notion.md` | `NOTION_PARENT_PAGE: <pagina>` |

`install.py` chiede quale backend usare, poi compone `it/repodoc/memory-protocol-core.md` + il frammento del backend scelto, sostituisce il placeholder e scrive il risultato in `repodoc/memory-protocol.md`.

ChatGPT Project e Claude Project assumono ancora un flusso GitHub e sono disponibili solo quando il backend scelto è GitHub.

## Mappa dei file

| Strumento | File sorgente | Destinazione nel repository target | Installazione |
|---|---|---|---|
| Protocollo condiviso | `it/repodoc/memory-protocol-core.md` + `it/repodoc/backends/<backend>.md` | `repodoc/memory-protocol.md` | L'installer compone i due file e sostituisce il placeholder del backend scelto. Tutte le istruzioni CLI referenziano il file risultante. |
| Claude Code | `it/claude-code/CLAUDE.md` | `.claude/CLAUDE.md` | Copia il file creando `.claude/` se necessario. |
| OpenAI Codex CLI | `it/codex/AGENTS.md` | `AGENTS.md` | Copia nella root del repository. |
| GitHub Copilot | `it/copilot/copilot-instructions.md` | `.github/copilot-instructions.md` | Copia il file creando `.github/` se necessario. |
| ChatGPT Project (solo backend GitHub) | `it/chatgpt/instruction.md` | `repodoc/chatgpt-instruction.md` | L'installer sostituisce `<owner>/<repo>`; incolla poi il contenuto nelle istruzioni del Project. |
| Claude Project (solo backend GitHub) | `it/claude/instruction.md` | `repodoc/claude-chat-instruction.md` | L'installer sostituisce `<owner>/<repo>`; incolla poi il contenuto nelle Project Instructions. |

### Agenti RepoDoc (solo backend GitHub)

Oltre al file di istruzioni base, per ciascuno strumento selezionato l'installer copia anche gli agenti dedicati definiti in `install.py` (`AGENT_FILES`) e la skill di espansione specifiche (`SKILL_FILE`/`SKILL_DESTINATIONS`). Sono installati **solo quando il backend scelto è GitHub**, perché operano il flusso di PR persistente descritto in `it/repodoc/backends/github.md`.

| Strumento | File sorgente | Destinazione nel repository target |
|---|---|---|
| Claude Code | `it/claude-code/agents/consistency-check.md` | `.claude/agents/repodoc-consistency-check.md` |
| Claude Code | `it/claude-code/agents/close-openpoint.md` | `.claude/agents/repodoc-close-openpoint.md` |
| Claude Code | `it/claude-code/agents/synthesize-specs.md` | `.claude/agents/repodoc-synthesize-specs.md` |
| Claude Code | `it/claude-code/agents/expand-specs.md` | `.claude/agents/repodoc-expand-specs.md` |
| Claude Code | `it/claude-code/agents/expand-spec-worker.md` | `.claude/agents/repodoc-expand-spec-worker.md` |
| Claude Code | `it/skills/spec-expand/SKILL.md` | `.claude/skills/repodoc-spec-expand/SKILL.md` |
| OpenAI Codex CLI | `it/codex/agents/consistency-check.toml` | `.codex/agents/repodoc-consistency-check.toml` |
| OpenAI Codex CLI | `it/codex/agents/close-openpoint.toml` | `.codex/agents/repodoc-close-openpoint.toml` |
| OpenAI Codex CLI | `it/codex/agents/synthesize-specs.toml` | `.codex/agents/repodoc-synthesize-specs.toml` |
| OpenAI Codex CLI | `it/codex/agents/expand-specs.toml` | `.codex/agents/repodoc-expand-specs.toml` |
| OpenAI Codex CLI | `it/skills/spec-expand/SKILL.md` | `.agents/skills/repodoc-spec-expand/SKILL.md` |
| GitHub Copilot | `it/copilot/agents/consistency-check.agent.md` | `.github/agents/repodoc-consistency-check.agent.md` |
| GitHub Copilot | `it/copilot/agents/close-openpoint.agent.md` | `.github/agents/repodoc-close-openpoint.agent.md` |
| GitHub Copilot | `it/copilot/agents/synthesize-specs.agent.md` | `.github/agents/repodoc-synthesize-specs.agent.md` |
| GitHub Copilot | `it/copilot/agents/expand-specs.agent.md` | `.github/agents/repodoc-expand-specs.agent.md` |
| GitHub Copilot | `it/skills/spec-expand/SKILL.md` | `.agents/skills/repodoc-spec-expand/SKILL.md` (se non già scritto da Codex) |

La skill `repodoc-spec-expand` è un unico contenuto sorgente, copiato nel percorso di scoperta nativo di ciascuno strumento selezionato: `.claude/skills/` per Claude Code, `.agents/skills/` per Codex e Copilot CLI (che lo condividono). Se sia Codex sia Copilot sono selezionati, il file viene scritto una sola volta.

## Struttura risultante

```text
<repository-target>/
├── .claude/
│   ├── CLAUDE.md
│   ├── agents/
│   │   ├── repodoc-consistency-check.md
│   │   ├── repodoc-close-openpoint.md
│   │   ├── repodoc-synthesize-specs.md
│   │   ├── repodoc-expand-specs.md
│   │   └── repodoc-expand-spec-worker.md
│   └── skills/
│       └── repodoc-spec-expand/SKILL.md
├── .codex/
│   └── agents/
│       ├── repodoc-consistency-check.toml
│       ├── repodoc-close-openpoint.toml
│       ├── repodoc-synthesize-specs.toml
│       └── repodoc-expand-specs.toml
├── .github/
│   ├── copilot-instructions.md
│   └── agents/
│       ├── repodoc-consistency-check.agent.md
│       ├── repodoc-close-openpoint.agent.md
│       ├── repodoc-synthesize-specs.agent.md
│       └── repodoc-expand-specs.agent.md
├── .agents/
│   └── skills/
│       └── repodoc-spec-expand/SKILL.md
├── repodoc/
│   ├── memory-protocol.md
│   ├── chatgpt-instruction.md
│   └── claude-chat-instruction.md
└── AGENTS.md
```

(gli agenti, `.codex/agents/`, `.github/agents/` e `.agents/skills/` sono presenti solo quando il backend è GitHub.)

## Copia manuale

Esegui dalla root di questa repository, sostituendo `<repository-target>` con il percorso del progetto da configurare e `<backend>` con `github`, `google-docs` o `notion`:

```sh
mkdir -p <repository-target>/.claude \
         <repository-target>/.github \
         <repository-target>/repodoc

cp it/claude-code/CLAUDE.md <repository-target>/.claude/CLAUDE.md
cp it/codex/AGENTS.md <repository-target>/AGENTS.md
cp it/copilot/copilot-instructions.md <repository-target>/.github/copilot-instructions.md

cat it/repodoc/memory-protocol-core.md it/repodoc/backends/<backend>.md > <repository-target>/repodoc/memory-protocol.md
# poi sostituisci a mano il placeholder del backend scelto nel file appena creato

# solo se il backend è github:
cp it/chatgpt/instruction.md <repository-target>/repodoc/chatgpt-instruction.md
cp it/claude/instruction.md <repository-target>/repodoc/claude-chat-instruction.md
```

## Note

- L'installer non sovrascrive eventuali istruzioni già presenti in `AGENTS.md`, `.claude/CLAUDE.md` o `.github/copilot-instructions.md`: aggiunge un blocco delimitato da `<!-- repodoc:start -->` e `<!-- repodoc:end -->`, aggiornando solo quel blocco nelle esecuzioni successive.
- Claude Code riconosce sia `CLAUDE.md` nella root sia `.claude/CLAUDE.md`; questa repository adotta `.claude/CLAUDE.md`. Poiché gli import `@path` sono relativi al file che li contiene, il wrapper usa `@../repodoc/memory-protocol.md`.
- Codex carica `AGENTS.md` dalla root e può applicare file aggiuntivi nelle sottodirectory.
- Copilot usa `.github/copilot-instructions.md` per le istruzioni valide in tutto il repository. Le regole mirate possono essere aggiunte in `.github/instructions/*.instructions.md`.
- I file generati per ChatGPT Project e Claude Project sono copie pronte da incollare nelle rispettive interfacce; le applicazioni non li leggono direttamente dal repository. Risiedono sotto `repodoc/` apposta, così Codex CLI, GitHub Copilot e Claude Code non rischiano di leggerli e interpretarli come istruzioni: questi strumenti leggono solo, rispettivamente, `AGENTS.md`, `.github/copilot-instructions.md` e `CLAUDE.md`/`.claude/CLAUDE.md`.
