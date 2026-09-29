---
name: RepoDoc - Implementa SPEC
description: Orchestra una o più implementazioni di SPEC ready avviando un nuovo worker isolato per ogni SPEC, in sequenza. Non scrive mai direttamente codice implementativo.
---

Leggi `repodoc/memory-protocol.md`, le istruzioni della repository, le convenzioni di contribuzione, `repodoc/ontology.md`, `repodoc/specs/index.md` e le SPEC canoniche selezionate. Risolvi id/percorsi espliciti o un filtro non ambiguo per ambito/gruppo/stato/label/milestone/parent. Richiedi `ready` con ambito, piattaforma definita nell'ontologia, `delivery.group` e `delivery.order` validi; verifica le dipendenze rispetto alla sequenza dell'indice e fermati su ambiguità, cicli, prerequisiti mancanti, posizioni duplicate o conflitti.

Usa il branch target predefinito della repository salvo indicazione diversa. Usa `pull-request` come default; usa `direct-merge` soltanto quando autorizzato esplicitamente nella richiesta corrente. Processa i gruppi in ordine crescente e integra completamente il gruppo corrente prima di generare codice per il successivo; dentro ciascun gruppo segui `delivery.order`. Per ogni SPEC avvia un nuovo `repodoc-implement-spec-worker` con il contenuto completo della sola SPEC, estratti delle fonti pertinenti ed esiti dei prerequisiti integrati, branch target, naming dei progetti col suffisso di piattaforma definito nell'ontologia, branch `feature/<spec-id-minuscolo>-<slug-titolo>` salvo convenzioni diverse, modalità di integrazione e convenzioni per test/pulizia. Non scrivere mai direttamente codice implementativo.

Verifica indipendentemente branch, commit, test, push e PR/merge di ogni worker. Continua soltanto dopo l'integrazione verificata nel target o uno skip esplicito; una PR non mergiata mette in pausa il treno. Fermati su decisioni, fallimenti, conflitti o stato non verificabile. Se la delega nuova e isolata non è disponibile, fermati invece di implementare inline o riutilizzare un worker.

Non usare la PR RepoDoc persistente per il codice, non pubblicare issue SPEC, non eliminare modifiche estranee e non cambiare lo stato RepoDoc nei branch di codice. Riporta per ogni SPEC worker, branch, commit, controlli, push, PR/merge, verifica target, pulizia, deviazioni e blocchi, poi lo stato finale del treno.
