---
name: repodoc-spec-expand
description: Espande sul posto un file repodoc/specs/SPEC-xxx-<title>.yaml draft o proposed esistente. Usa questa skill quando l'utente chiede di dettagliare, rifinire o formalizzare una SPEC specifica.
---

# RepoDoc — Espandi una SPEC

## Input richiesto

Individua una SPEC esistente dall'id, titolo o percorso indicato dall'utente. Cerca in `repodoc/specs/SPEC-*.yaml` per risolvere un riferimento parziale. Chiedi soltanto se resta ambiguo. Non creare una nuova SPEC tramite questa skill: la creazione delle proposte appartiene a `repodoc-synthesize-specs`.

## Istruzioni

Leggi il `repodoc/memory-protocol.md` corrente e la SPEC selezionata. Verifica che lo stato sia `draft` o `proposed`, poi consulta `project.md`, `architecture.md`, `ontology.md` e tutti i REQ, ADR, OPEN, ricerche, SPEC e documenti knowledge correlati.

Arricchisci lo stesso file YAML con problema/contesto, proposta, scope e out of scope, piattaforma definita nell'ontologia, gruppo/ordine di consegna, boundary, attività ordinate, sottotask atomici, criteri di accettazione oggettivi, dipendenze e relazioni, documentazione correlata e readiness note sostenuti dalle evidenze. Conserva id e percorso. Non creare un catalogo feature, un documento sostitutivo o una decisione tecnica non supportata.

Aggiorna `repodoc/specs/index.md` nella stessa modifica affinché la SPEC compaia una sola volta per ambito, gruppo e ordine di implementazione. Assicurati che `repodoc/index.md` colleghi questo indice specializzato.

Applica esattamente le regole di stato:

- mantieni `draft` finché la SPEC non è abbastanza coerente per una revisione;
- imposta `proposed` quando è revisionabile, anche se completamente dettagliata ma ancora in attesa di approvazione;
- imposta `ready` soltanto quando sono presenti tutti i dettagli richiesti, l'utente o la documentazione consolidata l'ha approvata esplicitamente e ambito, piattaforma, gruppo e ordine sono validi;
- non pubblicare issue; lascia null `github.issue` e `github.synced_at`.

Opera nel working tree e nel branch già attivi. Non creare o cambiare branch, non creare commit, non eseguire push e non aprire o aggiornare PR. Conserva modifiche estranee e verifica file, diff locale e assenza di una issue GitHub.

Riporta file modificato, stato risultante e motivazione, numero di attività/sottotask, informazioni o approvazione mancanti ed esito delle verifiche locali.
