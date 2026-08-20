# Protocollo di memoria persistente

Fonte unica di verità del protocollo. Non duplicare questo contenuto altrove: gli altri file del pacchetto linguistico devono limitarsi a referenziarlo.

Questo progetto usa un backend esterno come **memoria persistente e fonte di verità** delle informazioni consolidate. Le regole operative del backend configurato (dove si scrive, come si organizza, come si revisiona) sono descritte in [Backend di memoria](#backend-di-memoria).

La chat è memoria temporanea; il backend configurato è memoria persistente, strutturata e versionata.

## Cosa memorizzare

Usa liberamente la chat per brainstorming, ipotesi, confronti e ragionamenti temporanei.

Quando emerge un'informazione importante e sufficientemente consolidata, registrala nel backend configurato. In particolare:

* obiettivi, requisiti e vincoli;
* decisioni progettuali e architetturali;
* scelte tecnologiche e convenzioni;
* informazioni importanti sul dominio;
* configurazioni e procedure rilevanti;
* risultati di ricerche utili;
* punti aperti e decisioni da prendere;
* problemi e relative soluzioni;
* alternative scartate, se è utile conservarne il motivo;
* questioni aperte e attività future;
* qualsiasi informazione utile per riprendere correttamente il progetto in futuro.

Non archiviare automaticamente le conversazioni. **Estrai la conoscenza**, sintetizzala e integrala nella documentazione esistente.

Come criterio generale: se un'informazione potrebbe servire tra alcune settimane per capire il progetto o prendere una decisione, dovrebbe probabilmente essere registrata.

## Raccolta delle specifiche

Quando il documento `project` non esiste o è ancora uno stub, prima di registrare altro raccogli il contesto minimo del progetto ponendo le domande mancanti, una alla volta e non come questionario unico:

1. problema o motivazione: perché nasce il progetto;
2. obiettivo: cosa deve fare, a grandi linee;
3. utenti e casi d'uso principali;
4. cosa è esplicitamente fuori scope;
5. vincoli noti (tecnici, tempi, budget, compliance).

Registra le risposte nel documento `project` man mano che emergono. Solo dopo aver stabilito questa cornice ha senso scomporre singoli requisiti in REQ.

Quando durante la conversazione emerge un nuovo requisito senza criteri di accettazione, chiedi come si verifica che sia soddisfatto prima di creare il REQ. Non richiedere l'intero template: chiedi solo l'informazione mancante necessaria a rendere il requisito verificabile.

Questa raccolta attiva non sostituisce la regola generale di non interrompere continuamente la conversazione (vedi [Comportamento automatico](#comportamento-automatico)): si applica solo quando manca il contesto minimo di progetto o gli acceptance criteria di un requisito nuovo.

## Tipi di documento

Adatta i tipi di documento a quelli già esistenti. Non creare documenti o tipi equivalenti superflui.

* `README`: panoramica del progetto;
* `AGENTS`: solo istruzioni operative, senza duplicare la conoscenza di progetto;
* `index`: indice della memoria;
* `project`: contesto del progetto;
* `architecture`: architettura;
* `glossary`: termini;
* `REQ-xxx-<title>`: requisiti;
* `OPEN-xxx-<title>`: questioni aperte;
* `ADR-xxx-<title>`: decisioni;
* `specs`: specifiche;
* `research`: ricerche;
* `knowledge`: conoscenza stabile.

Crea questi documenti solo quando servono. La posizione concreta di ciascun tipo (percorso file, cartella o pagina) dipende dal backend configurato: vedi [Backend di memoria](#backend-di-memoria).

## Knowledge base collegata

Crea documenti focalizzati e indicizzati, collegati tra loro. Evita contenuti enormi, frammentazione e duplicazioni; mantieni una fonte principale per informazione. Il meccanismo di collegamento concreto dipende dal backend configurato.

## Metadati

Quando utile, i documenti `knowledge`, `decision`, `research` e `specs` possono avere metadati con:
- `title`
- `updated`
- `related`
- `status` (`draft`, `active`, `deprecated` o `superseded`).
- `tag`

I documenti `openpoint` usano gli stessi metadati, ma con `status` (`open` o `resolved`).

Non aggiungere metadati inutili. La sintassi concreta dei metadati dipende dal backend configurato.

## Aggiornamento della conoscenza

La documentazione deve descrivere principalmente **lo stato corrente**.

Quando una decisione cambia:

1. individua i documenti coinvolti;
2. aggiorna la documentazione corrente;
3. crea o aggiorna l'ADR, se necessario;
4. aggiorna collegamenti e indici.

Non conservare informazioni obsolete nei documenti correnti solo per mantenerne la storia: **il backend configurato conserva la storia; la documentazione descrive lo stato corrente.**

## ADR

Crea ADR solo per decisioni significative. Intestazione: `# ADR-XXX - Titolo`. 
Sezioni minime: 
* `Status`
* `Context`
* `Decision`
* `Rationale`
* `Alternatives`
* `Consequences`
* `Related`.

Se possibile, collega un ADR ad uno o più requisiti.

## Requisiti

Crea REQ per tutti i requisiti esposti. Intestazione: `# REQ-XXX - Titolo`. 
Sezioni minime: 
* `Status`
* `Priority`
* `Context`
* `Related`
* `Description`
* `Acceptance Criteria`: elenco puntato di condizioni verificabili; usa Given/When/Then solo per comportamenti complessi
* `Example` (se disponibile)

Se il requisito emerge senza criteri di accettazione, chiedili prima di creare il REQ (vedi [Raccolta delle specifiche](#raccolta-delle-specifiche)).

## Questioni aperte

Crea OPEN per le questioni non ancora risolte. Intestazione: `# OPEN-XXX - Titolo`.
Sezioni minime:
* `Status` (`open` o `resolved`)
* `Context`
* `Description`
* `Related`

Quando una questione si risolve, aggiorna lo `Status` a `resolved`. Se la risoluzione è una decisione significativa, crea o aggiorna l'ADR corrispondente invece di lasciare la conoscenza solo nell'OPEN.

## Consultazione

Per domande sullo stato del progetto, consulta prima il backend di memoria configurato. Ordine di affidabilità:

1. documentazione consolidata nel backend;
2. conversazione corrente;
3. memoria delle conversazioni precedenti.

Se la conversazione corrente contraddice la documentazione, verifica che rappresenti una nuova decisione prima di aggiornare il backend.

## Backend di memoria

Questo progetto usa **un solo backend** come memoria persistente. Le regole operative specifiche del backend configurato seguono da qui in avanti.

## Comportamento automatico

Non è necessario che l'utente chieda esplicitamente di aggiornare la memoria ogni volta.

Quando emerge chiaramente conoscenza consolidata e rilevante:

1. consulta la documentazione esistente;
2. determina dove registrarla;
3. aggiorna preferibilmente un documento esistente;
4. crea un nuovo documento solo quando necessario;
5. aggiorna eventuali indici e collegamenti;
6. salva l'aggiornamento seguendo le regole del backend configurato;
7. comunica sinteticamente cosa hai registrato.

Non interrompere continuamente la conversazione per chiedere se ogni informazione debba essere salvata. Distingui autonomamente brainstorming e conoscenza consolidata.

## Limiti

Puoi modificare automaticamente solo **documentazione e memoria del progetto**. Codice, infrastruttura, pipeline, dipendenze, database, configurazioni, script e altri artefatti eseguibili richiedono una richiesta esplicita.

Questa autonomia riguarda esclusivamente gli aggiornamenti automatici della memoria e documentazione gestiti da RepoDoc. Non si estende a ogni tipo di modifica del progetto e non autorizza modifiche autonome a codice, infrastruttura, pipeline, dipendenze, database, configurazioni, script o altri artefatti eseguibili, indipendentemente dal backend configurato.

## Obiettivo

Mantenere una memoria affidabile, sintetica, aggiornata, versionata e collegata. **La chat serve per pensare; il backend configurato per ricordare; la storia resta preservata; il flusso di revisione del backend mantiene la memoria in evoluzione.**
