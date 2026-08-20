## Backend: Google Docs

```text
GOOGLE_DRIVE_FOLDER: <GOOGLE_DRIVE_FOLDER>
```

> Sostituire il placeholder con la cartella Google Drive del progetto target prima dell'uso.

### Percorsi

Crea un Google Doc per ciascun tipo di documento dentro `GOOGLE_DRIVE_FOLDER`, con titolo `<Tipo> - <Titolo>` (es. "ADR-003 - Titolo").

### Collegamenti

Collega i documenti tra loro con i link nativi di Google Docs.

### Metadati

Non essendo disponibile un front matter nativo, riporta i metadati (`title`, `updated`, `related`, `status`, `tag`) come prime righe del documento.

### Scrittura

Se il connector Google Drive/Docs in uso non può creare o modificare documenti, non simulare la scrittura: indica con precisione quale permesso manca e chiedi di abilitarlo.

Il flusso di revisione (equivalente della PR persistente di GitHub) non è ancora definito per questo backend.
