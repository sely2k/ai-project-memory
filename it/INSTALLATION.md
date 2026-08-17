# Installazione delle istruzioni

Questa repository contiene file sorgente da distribuire nei progetti target. Copia ogni file nel percorso indicato, mantenendo esattamente maiuscole e minuscole.

## Mappa dei file

| Strumento | File sorgente | Destinazione nel repository target | Installazione |
|---|---|---|---|
| Protocollo condiviso | `it/repodoc/memory-protocol.md` | `repodoc/memory-protocol.md` | Copia il file. Tutte le istruzioni CLI lo referenziano. |
| Claude Code | `it/claude-code/CLAUDE.md` | `.claude/CLAUDE.md` | Copia il file creando `.claude/` se necessario. |
| OpenAI Codex CLI | `it/codex/AGENTS.md` | `AGENTS.md` | Copia nella root del repository. |
| GitHub Copilot | `it/copilot/copilot-instructions.md` | `.github/copilot-instructions.md` | Copia il file creando `.github/` se necessario. |
| ChatGPT Project | `it/chatgpt/instruction.md` | `repodoc/project-instructions/chatgpt.md` | L'installer sostituisce `<owner>/<repo>`; incolla poi il contenuto nelle istruzioni del Project. |
| Claude Project | `it/claude/instruction.md` | `repodoc/project-instructions/claude.md` | L'installer sostituisce `<owner>/<repo>`; incolla poi il contenuto nelle Project Instructions. |

## Struttura risultante

```text
<repository-target>/
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

## Copia manuale

Esegui dalla root di questa repository, sostituendo `<repository-target>` con il percorso del progetto da configurare:

```sh
mkdir -p <repository-target>/.claude \
         <repository-target>/.github \
         <repository-target>/repodoc/project-instructions

cp it/chatgpt/instruction.md <repository-target>/repodoc/project-instructions/chatgpt.md
cp it/claude/instruction.md <repository-target>/repodoc/project-instructions/claude.md
cp it/claude-code/CLAUDE.md <repository-target>/.claude/CLAUDE.md
cp it/codex/AGENTS.md <repository-target>/AGENTS.md
cp it/copilot/copilot-instructions.md <repository-target>/.github/copilot-instructions.md
cp it/repodoc/memory-protocol.md <repository-target>/repodoc/memory-protocol.md
```

## Note

- L'installer non sovrascrive eventuali istruzioni già presenti in `AGENTS.md`, `.claude/CLAUDE.md` o `.github/copilot-instructions.md`: aggiunge un blocco delimitato da `<!-- repodoc:start -->` e `<!-- repodoc:end -->`, aggiornando solo quel blocco nelle esecuzioni successive.
- Claude Code riconosce sia `CLAUDE.md` nella root sia `.claude/CLAUDE.md`; questa repository adotta `.claude/CLAUDE.md`. Poiché gli import `@path` sono relativi al file che li contiene, il wrapper usa `@../repodoc/memory-protocol.md`.
- Codex carica `AGENTS.md` dalla root e può applicare file aggiuntivi nelle sottodirectory.
- Copilot usa `.github/copilot-instructions.md` per le istruzioni valide in tutto il repository. Le regole mirate possono essere aggiunte in `.github/instructions/*.instructions.md`.
- I file generati per ChatGPT Project e Claude Project sono copie pronte da incollare nelle rispettive interfacce; le applicazioni non li leggono direttamente dal repository.
