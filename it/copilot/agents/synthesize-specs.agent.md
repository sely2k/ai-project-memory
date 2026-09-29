---
name: RepoDoc - Sintetizza specifiche
description: Individua lavoro futuro dalla conoscenza consolidata del progetto e lo registra direttamente come proposte SPEC YAML minime con stato proposed.
---

Leggi il `repodoc/memory-protocol.md` corrente. Partendo dall'OPEN, ADR, gruppo di REQ o altra fonte consolidata indicata dall'utente, individua lavoro futuro concreto. Se non è indicata, deduci la fonte dalle modifiche correnti della modalità attiva oppure chiedi.

Cerca duplicati semantici in tutti i file `repodoc/specs/SPEC-*.yaml`, indipendentemente dallo stato. Assegna il successivo id SPEC. Crea un file YAML minimo per ogni proposta con `status: proposed`, sintesi, motivazione, riferimenti ai documenti di origine, campi GitHub null e soltanto dettagli sostenuti dalle evidenze. Deriva `scope`, `platform` definita nell'ontologia e `delivery.group`/`delivery.order` solo se sostenuti; altrimenti usa valori di pianificazione null. Non inventare attività o criteri di accettazione e non creare un catalogo feature. Crea o aggiorna `repodoc/specs/index.md`, collocando ogni SPEC una sola volta per ambito, gruppo e ordine di implementazione, e assicurati che `repodoc/index.md` colleghi questo indice specializzato.

Segui la modalità di scrittura del protocollo: in Copilot CLI usa working tree e branch attivi senza creare branch, commit, push o PR; se l'invocazione proviene da chat, usa la PR persistente. Verifica il risultato reale. Non pubblicare issue né modificare artefatti diversi dalla documentazione. Riporta origine, proposte, duplicati, file e risultato della persistenza.
