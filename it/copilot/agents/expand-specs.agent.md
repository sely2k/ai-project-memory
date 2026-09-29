---
name: RepoDoc - Espandi tutte le specifiche
description: Espande sul posto tutte o alcune SPEC repodoc/specs/SPEC-*.yaml draft/proposed con contenuto implementativo dettagliato e sostenuto dalle evidenze.
---

Leggi il `repodoc/memory-protocol.md` corrente. Enumera i file `repodoc/specs/SPEC-*.yaml` con stato `draft` o `proposed`, limitandoti al sottoinsieme indicato dall'utente quando presente. Risolvi una sola volta la modalità di scrittura: Copilot CLI sul working tree attivo oppure chat sulla PR persistente.

Processa ogni SPEC in sequenza come compito isolato. Rileggi project, architecture, ontology, REQ, ADR, OPEN, ricerche, knowledge e SPEC correlate. Aggiorna lo stesso file YAML con problema/contesto, proposta, scope e out of scope, piattaforma definita nell'ontologia, gruppo/ordine di consegna, boundary, attività ordinate, sottotask atomici, criteri di accettazione oggettivi, dipendenze e relazioni, documenti correlati e readiness note sostenuti dalle evidenze. Conserva id e percorso; non creare un catalogo o una rappresentazione sostitutiva e non inventare decisioni irrisolte. Aggiorna `repodoc/specs/index.md` nella stessa operazione affinché ogni SPEC compaia una sola volta per ambito, gruppo e ordine di implementazione e assicurati che `repodoc/index.md` lo colleghi. In CLI non creare branch, commit, push o PR; in chat segui la PR persistente.

Espandere non significa approvare: mantieni `draft` finché non è revisionabile; usa `proposed` quando è revisionabile o completa ma in attesa di approvazione; usa `ready` soltanto quando è completa e approvata esplicitamente dall'utente o dalla documentazione consolidata. Non pubblicare issue e mantieni null i campi GitHub.

Prosegui oltre le SPEC incomplete, verifica file finali e persistenza applicabile e riporta stati, informazioni o approvazione mancanti, elementi ignorati, file modificati e conferma che non è stata pubblicata alcuna issue.
