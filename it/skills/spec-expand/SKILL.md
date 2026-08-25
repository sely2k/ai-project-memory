---
name: repodoc-spec-expand
description: Trasforma una singola voce di alto livello del catalogo repodoc/specs/features.md in un file YAML SPEC-xxx-<title>.yaml completo e conforme al protocollo RepoDoc. Usa questa skill quando l'utente chiede di dettagliare, espandere o formalizzare una specifica a partire dal catalogo.
---

# RepoDoc — Espandi una specifica di alto livello

## Quando usarla

Quando l'utente chiede di trasformare una voce del catalogo `repodoc/specs/features.md` (tipicamente prodotta dall'agente `repodoc-synthesize-specs`) in una specifica YAML completa, pronta a diventare in futuro una issue GitHub.

## Parametri richiesti

- `SPEC_NUMBER`: identificativo della specifica così come appare nel catalogo (es. `SPEC-003`).
- `SPEC_TITLE`: titolo sintetico della specifica così come appare nel catalogo.

Se l'utente non fornisce entrambi i valori, chiedili prima di procedere. Se fornisce solo uno dei due (o un riferimento ambiguo), leggi `repodoc/specs/features.md` per dedurre l'altro; se la voce non è univoca, chiedi conferma invece di indovinare.

## Istruzioni operative

Esegui, sostituendo `SPEC_NUMBER` e `SPEC_TITLE` con i valori raccolti, il compito seguente:

---

Nel repository `GITHUB_REPOSITORY`, applica la versione corrente di `repodoc/memory-protocol.md`.

Trasforma `SPEC_NUMBER` (`SPEC_TITLE`), attualmente sintetizzata in `repodoc/specs/features.md`, in una specifica YAML precisa e completa conforme al protocollo.

Prima di scrivere:

- consulta `repodoc/project.md`, `repodoc/architecture.md` e tutti i requisiti, ADR, open point, ricerche e documenti correlati alla SPEC;
- verifica lo stato corrente del repository e della PR RepoDoc persistente;
- rispetta naming, responsabilità e dependency boundaries già consolidati;
- conserva eventuali naming o refusi intenzionalmente consolidati nei documenti autorevoli;
- non introdurre arbitrariamente decisioni tecniche che risultano ancora aperte.

La specifica YAML deve includere almeno:

- problema e contesto;
- proposta;
- scope e out of scope;
- regole, responsabilità e dependency boundaries pertinenti;
- attività di implementazione dettagliate e ordinate;
- sottotask specifici, atomici e verificabili;
- criteri di accettazione oggettivi, possibilmente associati a comandi, exit code, test o controlli osservabili;
- dipendenze e relazioni con le altre SPEC;
- documentazione correlata;
- readiness notes che indichino precisamente eventuali decisioni ancora mancanti.

Gestisci lo stato della SPEC in base alle evidenze documentali:

- mantienila `draft` se restano decisioni, prerequisiti o dettagli essenziali non consolidati;
- impostala `ready` soltanto se tutti i criteri previsti dal protocollo risultano chiaramente soddisfatti;
- non pubblicarla come GitHub issue;
- lascia `github.issue: null` e `github.synced_at: null`.

Aggiorna `repodoc/specs/features.md` affinché la vecchia sintesi sia sostituita da un collegamento al nuovo file YAML canonico, eliminando la duplicazione senza alterare le altre SPEC.

Gestisci l'aggiornamento mediante la PR RepoDoc persistente prevista dal protocollo:

1. cerca tutte le PR aperte il cui titolo rispetta esattamente il formato previsto;
2. se ne esiste una sola, riusa il relativo branch;
3. se non ne esiste nessuna, crea branch e PR seguendo il protocollo;
4. se ne esistono più di una, fermati e chiedi all'utente quale utilizzare;
5. crea commit piccoli e coerenti;
6. aggiorna la descrizione della PR per includere la nuova SPEC;
7. non effettuare il merge.

Verifica realmente, rileggendo GitHub dopo le modifiche:

- contenuto e SHA del nuovo file YAML;
- stato `draft` o `ready`;
- presenza di attività, sottotask e acceptance criteria;
- assenza della vecchia duplicazione in `features.md`;
- presenza del nuovo collegamento nel catalogo;
- commit presenti sul branch;
- stato, titolo, branch e contenuto della PR persistente;
- assenza di una GitHub issue per la SPEC.

Alla fine riporta sinteticamente:

- file creati o modificati;
- stato assegnato alla SPEC e motivazione;
- numero di attività e sottotask;
- commit creati;
- link alla PR persistente;
- risultato delle verifiche;
- conferma che non è stata creata alcuna issue.

---

## Note

- Questa skill non pubblica mai issue GitHub: quello resta un passo esplicito e separato, previsto dalla sezione "Specifiche" del protocollo, solo per SPEC con `status: ready` e solo su richiesta esplicita.
- Se il backend configurato non è GitHub, il flusso di PR persistente descritto sopra non si applica: segui invece il flusso di scrittura del backend configurato descritto in `repodoc/memory-protocol.md`.
