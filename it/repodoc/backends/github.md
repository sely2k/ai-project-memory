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
| `ontology` | `repodoc/ontology.md` |
| `REQ-xxx-<title>` | `repodoc/requirement/REQ-xxx-<title>.md` |
| `OPEN-xxx-<title>` | `repodoc/openpoint/OPEN-xxx-<title>.md` |
| `ADR-xxx-<title>` | `repodoc/decisions/ADR-xxx-<title>.md` |
| `SPEC-xxx-<title>` | `repodoc/specs/SPEC-xxx-<title>.yaml` |
| `specs-index` | `repodoc/specs/index.md` |
| `research` | `repodoc/research/` |
| `knowledge` | `repodoc/knowledge/` |

Le specifiche proposte e quelle completamente dettagliate usano gli stessi file `repodoc/specs/SPEC-xxx-<title>.yaml`. Non creare un catalogo feature separato: usa `status: proposed` per il lavoro in attesa di approvazione e arricchisci lo stesso file mentre matura.

`repodoc/specs/index.md` raggruppa i collegamenti a tutti i file SPEC prima per gruppo di implementazione globale, poi per ambito e ordine, secondo il protocollo di base. Contiene soltanto metadati di navigazione e sequenziamento e va aggiornato atomicamente quando cambia una SPEC. `repodoc/index.md` collega questo indice specializzato invece di elencare le singole SPEC.

Usa questa struttura, creando un'intestazione per ogni gruppo presente in ordine crescente e mantenendo sempre la sezione finale Non pianificate:

```markdown
# Specifiche

## Gruppo 1

### Ambito: catalog
| Ordine | SPEC | Titolo | Piattaforma | Tipo | Stato | Aggiornata |
|---|---|---|---|---|---|---|
| 1 | [SPEC-014](./SPEC-014-support-multi-backend-export.yaml) | Support multi-backend export | web | feature | ready | 2026-09-28 |

## Gruppo 2

## Non pianificate

### Ambito: catalog
```

`repodoc/ontology.md` contiene la tabella canonica per il naming multipiattaforma. Struttura minima:

```markdown
# Ontologia

## Piattaforme e suffissi
| Identificatore | Nome | Suffisso | Alias/prefissi legacy |
|---|---|---|---|
| web | Web | web | frontend |
| ios | iOS | ios | apple-mobile |
| shared | Condiviso | shared | common |
```

Un progetto specifico di piattaforma usa `<nome-base>-<suffisso>`, per esempio `shop-web` e `shop-ios`. Il valore `platform` di ogni SPEC deve risolvere una riga di questa tabella.

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

### Modalità di scrittura

Determina la modalità dall'ambiente che ha originato il lavoro, non dal nome dell'agente eventualmente delegato:

- **CLI locale** (Claude Code, Codex CLI, Copilot CLI o equivalente avviato dall'utente nella repository): modifica i file nel working tree e nel branch già attivi. Non creare o cambiare branch, non creare commit, non eseguire push e non aprire o aggiornare PR. Conserva tutte le modifiche estranee e verifica il risultato rileggendo file e diff locale. Lascia all'utente staging, commit e integrazione.
- **Chat remota** (ChatGPT Project, Claude Project o un'attività delegata da quella chat): usa la Pull Request RepoDoc persistente descritta di seguito. Una delega da chat a Codex resta in modalità chat e non diventa modalità CLI.

### Pull Request persistente per la chat

In modalità chat, **non modificare direttamente il branch principale.**

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

### Commit della chat

In modalità chat, crea commit piccoli e coerenti per concetto, per esempio:

```text
docs: record authentication decision
```

### Pubblicare le specifiche come issue

Solo su richiesta esplicita, per un file `SPEC-xxx-<title>` con `status: ready`:

1. Verifica l'accesso in scrittura del connector GitHub in uso per le issue (non solo per file/commit). Se non può scrivere, non simulare la pubblicazione: indica con precisione quale permesso manca e chiedi di abilitarlo.
2. Risolvi `relations.parent`, `relations.children` e `relations.related` leggendo il `github.issue` di ciascuna specifica referenziata.
3. Crea la issue (`gh issue create --title ... --body-file ... --label ... --assignee ... --milestone ...`), oppure aggiornala con `gh issue edit` se `github.issue` è già valorizzato.
4. Imposta la relazione parent/children tramite la funzionalità nativa dei sub-issue di GitHub; rendi `relations.related` come elenco `Related: #...` nel corpo della issue, dato che GitHub non ha un tipo di collegamento non gerarchico nativo.
5. Scrivi `github.issue` e `github.synced_at` nel file YAML, porta `status` a `submitted` e aggiorna la voce della SPEC nel relativo gruppo/ambito dentro `repodoc/specs/index.md` nella stessa operazione. In modalità chat includi tutto nello stesso commit della PR persistente; in modalità CLI lascia gli aggiornamenti nel working tree senza creare commit.
6. Verifica l'esito reale rileggendo la issue tramite il connector o l'API, e riporta i link delle issue create o aggiornate.

### Implementare le SPEC come codice

Usa le convenzioni di contribuzione documentate dalla repository quando esistono. Altrimenti:

- risolvi il branch target dalla richiesta dell'utente; se non è indicato, usa il branch predefinito della repository;
- crea `feature/<spec-id-minuscolo>-<slug-titolo>` per ogni SPEC, per esempio `feature/spec-005-titolo-breve`;
- preferisci un git worktree isolato per non interferire con il checkout corrente dell'utente e con modifiche estranee;
- in modalità `pull-request`, esegui il push del branch e apri una PR verso il branch target, senza eseguire il merge;
- in modalità `direct-merge`, procedi soltanto quando la richiesta corrente autorizza esplicitamente il merge diretto, quindi integra e pubblica il branch target secondo le convenzioni della repository;
- elimina branch locali o remoti soltanto quando le convenzioni della repository o l'utente richiedono esplicitamente la pulizia, e soltanto dopo aver verificato l'integrazione riuscita.

La PR RepoDoc persistente non è la PR di implementazione e non va mai usata come branch di codice.

### Agenti RepoDoc

Per questo backend, l'installer può copiare agenti dedicati che eseguono parti di questo protocollo in autonomia, ciascuno nel formato nativo dello strumento selezionato (Claude Code, Codex, GitHub Copilot):

- **Bootstrap** (`repodoc-bootstrap`): legge la repository, raccoglie una alla volta soltanto le informazioni essenziali mancanti e crea la memoria iniziale minima nella modalità di scrittura attiva.
- **Doctor** (`repodoc-doctor`): diagnostica in sola lettura installazione, wrapper, agenti, placeholder, link, indici e struttura delle SPEC, senza modifiche né controllo di aggiornamenti.
- **Verifica coerenza** (`repodoc-consistency-check`): audita l'intero backend di memoria alla ricerca di contraddizioni, link rotti, duplicazioni e stati non aggiornati.
- **Chiudi open point** (`repodoc-close-openpoint`): legge un `OPEN-xxx-<title>` e prova a risolverlo raccogliendo evidenze.
- **Sintetizza specifiche** (`repodoc-synthesize-specs`): a situazione chiusa, registra il lavoro futuro direttamente come file `SPEC-xxx-<title>.yaml` minimi con `status: proposed`.
- **Espandi specifica** (skill `repodoc-spec-expand`): arricchisce sul posto una SPEC draft o proposed esistente, su richiesta puntuale dell'utente.
- **Espandi tutte le specifiche** (`repodoc-expand-specs`): scorre i file `SPEC-xxx-<title>.yaml` draft e proposed e arricchisce ciascuno sul posto. Il template Claude Code delega ogni espansione a `repodoc-expand-spec-worker`; i template Codex e Copilot applicano attualmente la stessa procedura in linea, un file alla volta.
- **Implementa SPEC** (`repodoc-implement-specs`): orchestra un treno sequenziale di implementazione e avvia un nuovo `repodoc-implement-spec-worker` per ogni SPEC ready. Non scrive mai direttamente codice implementativo.
- **Worker implementazione SPEC** (`repodoc-implement-spec-worker`): implementa esattamente una SPEC assegnata sul relativo branch di codice, esegue le verifiche e la integra soltanto secondo la policy richiesta. È un worker interno e non va riutilizzato tra SPEC diverse.

Gli agenti che modificano la memoria e la skill di espansione seguono la modalità CLI o chat definita sopra; `repodoc-doctor` resta sempre read-only. Gli agenti di implementazione seguono il flusso separato su branch di codice dedicati.
