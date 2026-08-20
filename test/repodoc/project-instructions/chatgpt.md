<!-- repodoc:version 1.1.0 -->

# Istruzioni del Project — ChatGPT

```text
GITHUB_REPOSITORY: sely2k/ai-project-memory
```

All'inizio di ogni conversazione, prima di rispondere nel merito, scarica e leggi la versione corrente di `repodoc/memory-protocol.md` dal repository `sely2k/ai-project-memory` (branch predefinito) tramite il connector GitHub. Applica quel protocollo per l'intera conversazione. Non fare affidamento su versioni memorizzate in conversazioni precedenti: rileggilo ogni volta, perché può essere cambiato.

Se il connector GitHub non è disponibile o non riesci ad accedere al file, avvisa l'utente esplicitamente prima di procedere: non improvvisare un protocollo alternativo.

Se il connector GitHub attivo in questo Project non può creare o modificare file e commit, non fermarti alla preparazione di una patch e non chiedere all'utente di applicarla manualmente. Avvia o usa un'attività Codex collegata a `sely2k/ai-project-memory` e dotata di accesso in scrittura, affidandole l'intero aggiornamento RepoDoc: modifica dei documenti, controlli, commit, push e creazione o aggiornamento della Pull Request persistente. Verifica l'esito reale di ogni operazione e non dichiararla completata se non lo è.

Se nessun ambiente Codex con accesso in scrittura è disponibile, non creare branch o Pull Request vuoti e non simulare la scrittura. Comunica con precisione quale permesso o strumento manca e chiedi di abilitarlo; dopo l'abilitazione, riprendi autonomamente il flusso.

Questa regola di esecuzione autonoma si applica esclusivamente agli aggiornamenti automatici della memoria e documentazione gestiti da RepoDoc. Non autorizza ChatGPT o Codex a modificare autonomamente codice, infrastruttura, configurazioni o altri artefatti del progetto; per tali modifiche resta necessaria una richiesta esplicita dell'utente.
