# Protocollo di memoria persistente

Fonte unica di verità del protocollo. Non duplicare questo contenuto altrove: gli altri file del pacchetto linguistico devono limitarsi a referenziarlo.

Questo progetto usa una repository GitHub come **memoria persistente e fonte di verità** delle informazioni consolidate.

```text
GITHUB_REPOSITORY: <owner>/<repo>
```

> Sostituire il placeholder con il repository del progetto target prima dell'uso.

La chat è memoria temporanea; GitHub è memoria persistente, strutturata e versionata.

## Cosa memorizzare

Usa liberamente la chat per brainstorming, ipotesi, confronti e ragionamenti temporanei.

Quando emerge un'informazione importante e sufficientemente consolidata, registrala nella repository. In particolare:

* obiettivi, requisiti e vincoli;
* decisioni progettuali e architetturali;
* scelte tecnologiche e convenzioni;
* informazioni importanti sul dominio;
* configurazioni e procedure rilevanti;
* risultati di ricerche utili;
* problemi e relative soluzioni;
* alternative scartate, se è utile conservarne il motivo;
* questioni aperte e attività future;
* qualsiasi informazione utile per riprendere correttamente il progetto in futuro.

Non archiviare automaticamente le conversazioni. **Estrai la conoscenza**, sintetizzala e integrala nella documentazione esistente.

Come criterio generale: se un'informazione potrebbe servire tra alcune settimane per capire il progetto o prendere una decisione, dovrebbe probabilmente essere registrata.

## Struttura

Adatta la struttura a quella esistente. Non creare file o directory inutili né documenti equivalenti.

* `README.md`: panoramica; `AGENTS.md`: sole istruzioni operative.
* `repo-docs/index.md`: indice; `project.md`: contesto e requisiti; `architecture.md`: architettura; `glossary.md`: termini; `backlog.md`: questioni aperte.
* `repo-docs/decisions/ADR-xxx-<title>.md`: ADR; `specs/`: specifiche; `research/`: ricerche; `knowledge/`: conoscenza stabile.

Crea questi file solo quando servono.

## Knowledge base collegata

In `repo-docs/`, crea documenti focalizzati, collegati da link relativi e indicizzati. Evita file enormi, frammentazione e duplicazioni; mantieni una fonte principale per informazione.

## Metadati

Quando utile, `knowledge`, `research` e `specs` possono usare un front matter con `title`, `updated`, `related` e `status` (`draft`, `active`, `deprecated` o `superseded`). Non aggiungere metadati inutili.

## Aggiornamento della conoscenza

La documentazione deve descrivere principalmente **lo stato corrente**.

Quando una decisione cambia:

1. individua i documenti coinvolti;
2. aggiorna la documentazione corrente;
3. crea o aggiorna l'ADR, se necessario;
4. aggiorna collegamenti e indici.

Non conservare informazioni obsolete nei documenti correnti solo per mantenerne la storia: **Git conserva la storia; la documentazione descrive lo stato corrente.**

## ADR

Crea ADR solo per decisioni significative. Intestazione: `# ADR-XXX - Titolo`. Sezioni minime: `Status`, `Context`, `Decision`, `Rationale`, `Alternatives`, `Consequences`, `Related`.

## Consultazione

Per domande sullo stato del progetto, consulta prima la repository. Ordine di affidabilità:

1. documentazione consolidata nella repository;
2. conversazione corrente;
3. memoria delle conversazioni precedenti.

Se la conversazione corrente contraddice la documentazione, verifica che rappresenti una nuova decisione prima di aggiornare la repository.

## Pull Request persistente

**Non modificare direttamente il branch principale.**

Usa il numero GitHub della PR, senza zeri iniziali. Titolo valido:

```regex
^repodoc/[1-9][0-9]*-ProjectMemory$
```

Prima di scrivere, cerca una PR aperta conforme e usa il suo branch.

Se non esiste, dal branch predefinito aggiornato crea `repodoc/project-memory-<YYYYMMDD-HHMMSS>`, apri la PR come `repodoc/pending-ProjectMemory` e rinominala subito `repodoc/<PR_NUMBER>-ProjectMemory`.

Mantieni e riutilizza la PR. Se ce ne sono più di una, elencale e chiedi quale usare. Se è chiusa o mergiata, creane una nuova.

**Non effettuare autonomamente il merge della PR.**

Se il connector GitHub in uso non può creare o modificare file e commit, non fermarti alla preparazione di una patch e non chiedere all'utente di applicarla manualmente. Avvia o usa un'attività Codex collegata alla repository e dotata di accesso in scrittura, quindi completa autonomamente l'aggiornamento RepoDoc: modifica dei documenti, controlli, commit, push e creazione o aggiornamento della PR persistente. Verifica l'esito reale di ogni operazione.

Se nessun ambiente Codex con accesso in scrittura è disponibile, non creare branch o PR vuoti e non simulare la scrittura. Indica con precisione quale permesso o strumento manca e chiedi di abilitarlo; una volta disponibile, riprendi autonomamente il flusso.

Questa autonomia riguarda esclusivamente gli aggiornamenti automatici della memoria e documentazione gestiti da RepoDoc. Non si estende a ogni tipo di modifica della repository e non autorizza modifiche autonome a codice, infrastruttura, pipeline, dipendenze, database, configurazioni, script o altri artefatti eseguibili.

## Commit

Crea commit piccoli e coerenti per concetto, per esempio:

```text
docs: record authentication decision
```

## Comportamento automatico

Non è necessario che l'utente chieda esplicitamente di aggiornare la memoria ogni volta.

Quando emerge chiaramente conoscenza consolidata e rilevante:

1. consulta la documentazione esistente;
2. determina dove registrarla;
3. aggiorna preferibilmente un documento esistente;
4. crea un nuovo documento solo quando necessario;
5. aggiorna eventuali indici e collegamenti;
6. effettua il commit sul branch associato alla PR `repodoc/<PR_NUMBER>-ProjectMemory`;
7. comunica sinteticamente cosa hai registrato.

Non interrompere continuamente la conversazione per chiedere se ogni informazione debba essere salvata. Distingui autonomamente brainstorming e conoscenza consolidata.

## Limiti

Puoi modificare automaticamente solo **documentazione e memoria del progetto**. Codice, infrastruttura, pipeline, dipendenze, database, configurazioni, script e altri artefatti eseguibili richiedono una richiesta esplicita.

## Obiettivo

Mantenere una memoria affidabile, sintetica, aggiornata, versionata e collegata. **La chat serve per pensare; la repository per ricordare; Git conserva la storia; la PR `repodoc/<PR_NUMBER>-ProjectMemory` mantiene la memoria in evoluzione.**
