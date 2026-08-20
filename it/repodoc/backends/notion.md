## Backend: Notion

```text
NOTION_PARENT_PAGE: <NOTION_PARENT_PAGE>
```

> Sostituire il placeholder con la sottopagina Notion del progetto target prima dell'uso.

### Percorsi

Crea una pagina Notion per ciascun tipo di documento sotto `NOTION_PARENT_PAGE`, con titolo `<Tipo> - <Titolo>` (es. "ADR-003 - Titolo").

### Collegamenti

Collega i documenti tra loro con i link nativi di Notion.

### Metadati

Usa le proprietà della pagina (o di un eventuale database Notion) per `title`, `updated`, `related`, `status`, `tag`, invece del front matter YAML.

### Scrittura

Se il connector Notion in uso non può creare o modificare pagine, non simulare la scrittura: indica con precisione quale permesso manca e chiedi di abilitarlo.

Il flusso di revisione (equivalente della PR persistente di GitHub) non è ancora definito per questo backend.
