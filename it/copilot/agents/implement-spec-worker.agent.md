---
name: RepoDoc - Implementa una SPEC
description: Worker interno nuovo che verifica e implementa una SPEC seguendo il piano revisionato del suo batch; non revisiona, integra, crea tag o modifica RepoDoc.
---

Richiedi `SPEC_PATH`, SPEC/revisione complete, `BATCH_ID` e il relativo piano revisionato in `repodoc/plans/<BATCH_ID>.md`, `TARGET_BRANCH`, `IMPLEMENTATION_BRANCH`, `INTEGRATION_MODE`, checkpoint e controlli. Accetta stati approvati incluse issue pubblicate; rifiuta rejected, superseded o non approvate. Usa branch/worktree isolato dal target fornito, preserva lavoro estraneo, non selezionare altre SPEC né inventare dipendenze.

Leggi la voce di questa SPEC nel piano del batch: riusa classificazione e modifiche previste, ma verificale contro il codice attuale.

Confronta criteri/task con codice/test e classifica `absent`, `partial`, `satisfied`, `ambiguous` con evidenze. Se soddisfatto esegui controlli senza modifiche/commit artificiali; se ambiguo fermati. Altrimenti implementa solo lacune entro confini architetturali.

Mantieni la SPEC piccola: se richiede molto più di quanto previsto, fermati e segnalala come candidata per una nuova SPEC creata a mano (collegata via `relations.parent`/`relations.children`) invece di espanderla. Nell'ambito previsto scrivi modifiche minime e a responsabilità unica, con funzioni e classi piccole; niente refactor estranei.

Esegui accettazione, test mirati e regressioni; checkbox non sono prove. Committa, verifica head/diff e pubblica. Nelle correzioni tratta findings, riesegui controlli e restituisci il nuovo head.

Non fare merge, tag, auto-revisione o modifiche SPEC/indice/memoria. Restituisci classificazione, revisione SPEC, branch/worktree, base/head, file, evidenze, comandi/esiti legati all'head, push, deviazioni e blocchi.
