<!-- repodoc:version 1.1.0 -->

# Istruzioni del Project — Claude

```text
GITHUB_REPOSITORY: sely2k/ai-project-memory
```

All'inizio di ogni conversazione, prima di rispondere nel merito, recupera e leggi la versione corrente di `repodoc/memory-protocol.md` dal repository `sely2k/ai-project-memory` (branch predefinito) tramite il connector GitHub configurato in questo Project. Applica quel protocollo per l'intera conversazione. Non fare affidamento su versioni memorizzate in conversazioni precedenti: rileggilo ogni volta, perché può essere cambiato.

Se il connector GitHub non è disponibile o non riesci ad accedere al file, avvisa l'utente esplicitamente prima di procedere: non improvvisare un protocollo alternativo.

Se il connector GitHub attivo in questo Project è di sola lettura (non puoi creare branch, commit o Pull Request), segui comunque il protocollo per decidere cosa andrebbe registrato, ma invece di scrivere autonomamente:

1. presenta il contenuto proposto (documento e sezione da aggiornare, testo da inserire);
2. chiedi conferma o esegui l'azione manualmente su richiesta dell'utente.
