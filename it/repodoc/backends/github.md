## Backend: GitHub

```text
GITHUB_REPOSITORY: <owner>/<repo>
```

> Sostituire il placeholder con il repository del progetto target prima dell'uso.

### Percorsi

| Tipo | Percorso |
|---|---|
| `README` | `README.md` |
| `AGENTS` | `AGENTS.md` |
| `index` | `repodoc/index.md` |
| `project` | `repodoc/project.md` |
| `architecture` | `repodoc/architecture.md` |
| `glossary` | `repodoc/glossary.md` |
| `REQ-xxx-<title>` | `repodoc/requirement/REQ-xxx-<title>.md` |
| `OPEN-xxx-<title>` | `repodoc/openpoint/OPEN-xxx-<title>.md` |
| `ADR-xxx-<title>` | `repodoc/decisions/ADR-xxx-<title>.md` |
| `SPEC-xxx-<title>` | `repodoc/specs/SPEC-xxx-<title>.yaml` |
| `research` | `repodoc/research/` |
| `knowledge` | `repodoc/knowledge/` |

### Collegamenti

Collega i documenti tra loro con link relativi.

### Metadati

I metadati vanno in un front matter YAML all'inizio del file:

```yaml
---
title: ...
updated: ...
related: [...]
status: ...
tag: [...]
---
```

I file `SPEC-xxx-<title>` sono YAML puro, non Markdown con front matter: vedi [Specifiche](../memory-protocol-core.md#specifiche) nel protocollo di base per lo schema.

### Pull Request persistente

**Non modificare direttamente il branch principale.**

Titolo valido della PR (numero GitHub, senza zeri iniziali):

```regex
^repodoc/[1-9][0-9]*-ProjectMemory$
```

Prima di scrivere, segui questi passi in ordine:

1. **Cerca una PR aperta conforme al titolo sopra.**
   - Se esiste una sola PR conforme, usa il suo branch.
   - Se ne esistono più di una, elencale e chiedi all'utente quale usare.
   - Se l'unica PR conforme è chiusa o mergiata, trattala come inesistente e passa al punto 2.
2. **Se non esiste una PR aperta conforme, creala:**
   - dal branch predefinito aggiornato, crea `repodoc/project-memory-<YYYYMMDD-HHMMSS>`;
   - apri la PR con titolo provvisorio `repodoc/pending-ProjectMemory`;
   - rinomina subito il titolo in `repodoc/<PR_NUMBER>-ProjectMemory`.
3. **Verifica l'accesso in scrittura del connector GitHub in uso** (creazione/modifica di file e commit).
   - Se il connector può scrivere, procedi normalmente con modifica dei documenti, commit, push e aggiornamento della PR.
   - Se il connector non può scrivere, non fermarti alla preparazione di una patch e non chiedere all'utente di applicarla manualmente: avvia o usa un ambiente o agente alternativo collegato alla repository e dotato di accesso in scrittura (ad esempio un'attività Codex o equivalente), e completa autonomamente l'aggiornamento RepoDoc con quell'ambiente.
   - Se nessun ambiente con accesso in scrittura è disponibile, non creare branch o PR vuoti e non simulare la scrittura: indica con precisione quale permesso o strumento manca e chiedi di abilitarlo; una volta disponibile, riprendi autonomamente il flusso da dove interrotto.
4. **Verifica l'esito reale di ogni operazione** rileggendo lo stato effettivo (commit, push, PR) tramite il connector o l'API, invece di fidarti solo del ritorno "successo" della chiamata.

Mantieni e riutilizza la stessa PR per gli aggiornamenti successivi, finché resta aperta.

**Non effettuare autonomamente il merge della PR.**

### Commit

Crea commit piccoli e coerenti per concetto, per esempio:

```text
docs: record authentication decision
```

### Pubblicare le specifiche come issue

Solo su richiesta esplicita, per un file `SPEC-xxx-<title>` con `status: ready`:

1. Verifica l'accesso in scrittura del connector GitHub in uso per le issue (non solo per file/commit). Se non può scrivere, non simulare la pubblicazione: indica con precisione quale permesso manca e chiedi di abilitarlo.
2. Risolvi `relations.parent`, `relations.children` e `relations.related` leggendo il `github.issue` di ciascuna specifica referenziata.
3. Crea la issue (`gh issue create --title ... --body-file ... --label ... --assignee ... --milestone ...`), oppure aggiornala con `gh issue edit` se `github.issue` è già valorizzato.
4. Imposta la relazione parent/children tramite la funzionalità nativa dei sub-issue di GitHub; rendi `relations.related` come elenco `Related: #...` nel corpo della issue, dato che GitHub non ha un tipo di collegamento non gerarchico nativo.
5. Scrivi `github.issue` e `github.synced_at` nel file YAML e porta `status` a `submitted`.
6. Verifica l'esito reale rileggendo la issue tramite il connector o l'API, e riporta i link delle issue create o aggiornate.
