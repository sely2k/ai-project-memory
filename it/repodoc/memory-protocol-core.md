<!-- repodoc:version 1.11.0 -->

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
* `ontology`: ontologia del progetto, inclusa la mappa tra piattaforme e suffissi di naming;
* `REQ-xxx-<title>`: requisiti;
* `OPEN-xxx-<title>`: questioni aperte;
* `ADR-xxx-<title>`: decisioni;
* `SPEC-xxx-<title>`: specifiche, incluso il lavoro proposto (uno YAML per specifica, vedi [Specifiche](#specifiche));
* `specs-index`: indice di navigazione di tutte le SPEC, raggruppate per gruppo di implementazione ordinato e, al suo interno, per ambito, con lo stato visibile per ogni voce;
* `research`: ricerche;
* `knowledge`: conoscenza stabile consolidata — non lavoro proposto o pianificato, che appartiene ai file `SPEC-xxx-<title>`.

Crea questi documenti solo quando servono. La posizione concreta di ciascun tipo (percorso file, cartella o pagina) dipende dal backend configurato: vedi [Backend di memoria](#backend-di-memoria).

## Knowledge base collegata

Crea documenti focalizzati e indicizzati, collegati tra loro. Evita contenuti enormi, frammentazione e duplicazioni; mantieni una fonte principale per informazione. Il meccanismo di collegamento concreto dipende dal backend configurato.

## Ontologia e naming multipiattaforma

Quando il progetto comprende artefatti specifici per una o più piattaforme, mantieni nel documento `ontology` una mappa canonica tra ogni identificatore di piattaforma e il relativo suffisso di naming; per i progetti multipiattaforma è obbligatoria. Ogni progetto, modulo o artefatto specifico di piattaforma deve terminare con il suffisso registrato, secondo la forma `<nome-base>-<suffisso-piattaforma>` salvo una convenzione già consolidata dalla repository. Non inventare varianti locali del suffisso e non usare lo stesso suffisso per piattaforme diverse.

L'ontologia deve distinguere almeno identificatore canonico, nome leggibile, suffisso e alias o prefissi legacy eventualmente accettati. Se la repository chiama “prefisso” un codice che nel nome compare come suffisso, registra esplicitamente questa corrispondenza. Le SPEC indicano la piattaforma tramite l'identificatore canonico dell'ontologia; gli artefatti condivisi usano un identificatore esplicito come `shared`, anch'esso mappato.

## Metadati

Quando utile, i documenti `knowledge`, `decision` e `research` possono avere metadati con:
- `title`
- `updated`
- `related`
- `status` (`draft`, `active`, `deprecated` o `superseded`).
- `tag`

I documenti `openpoint` usano gli stessi metadati, ma con `status` (`open` o `resolved`). I documenti `SPEC-xxx-<title>` non usano questi metadati generici: seguono lo schema dedicato in [Specifiche](#specifiche).

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

## Specifiche

Crea un file YAML `SPEC-xxx-<title>` non appena vale la pena tracciare un lavoro proposto. Non mantenere specifiche preliminari in un elenco o catalogo separato: lo stesso file evolve da proposta a specifica pronta per l'implementazione, conservando un solo identificativo e una sola fonte di verità per tutto il ciclo di vita.

Un'idea appena individuata può nascere con la sola sintesi, la motivazione, i documenti di origine e `status: proposed`. Espandi lo stesso file sul posto quando diventano noti scope, attività e criteri di accettazione. Non creare mai un secondo documento soltanto perché la specifica diventa più dettagliata.

Quando aggiorni una repository che contiene ancora un catalogo feature legacy, migra ogni voce univoca in un file SPEC proposed, conserva i collegamenti alle fonti originali e rimuovi il catalogo dopo aver verificato che nessuna proposta sia andata persa.

A differenza degli altri tipi di documento, una specifica è YAML puro, non Markdown con front matter. Campi minimi:

```yaml
id: SPEC-014
title: Support multi-backend export
status: proposed        # draft | proposed | ready | submitted | closed | rejected | superseded
approval: pending       # pending | approved
publication: unpublished # unpublished | published
type: feature            # feature | bug | task | chore
scope: catalog            # ambito funzionale o tecnico canonico
platform: web             # identificatore definito nell'ontologia del progetto
delivery:
  group: 1                # completato interamente prima del gruppo successivo
  order: 2                # ordine della SPEC all'interno del gruppo
labels: [backend, export]
assignees: []
milestone: null
summary: |
  Descrizione sintetica del lavoro proposto.
motivation: |
  Perché vale la pena considerarlo e quali documenti lo hanno originato.
sources:
  - ../decisions/ADR-003-multi-backend.md
body: null               # può essere null per draft/proposed; obbligatorio e completo per ready+
depends_on: []           # id delle SPEC prerequisito obbligatorie; non link informativi
relations:
  parent: null            # SPEC-xxx, corrisponde al parent sub-issue di GitHub
  children: []             # elenco di SPEC-xxx, corrisponde ai sub-issue di GitHub
  related: []               # SPEC-xxx o #issue, collegamento non gerarchico
github:
  issue: null              # owner/repo#123, valorizzato quando la issue esiste
  synced_at: null
implementation:
  state: not_started     # not_started | partial | verified | completed | blocked
  branch: null
  checkpoint_commit: null
  spec_revision: null    # blob/hash immutabile o commit del contenuto SPEC revisionato
  checks: []             # comando, commit, esito e riferimento opzionale all'evidenza
  review: null           # revisore, head_commit, verdetto, ciclo, riferimento ai findings
  blocker: null
  integration:
    target: null
    pull_request: null
    merge_commit: null
    tag: null
closure:
  reason: null           # completed | cancelled | duplicate | obsolete | other
  note: null
updated: ...
```

Usa gli stati in modo coerente:

* `draft`: il file è in fase di stesura e non è ancora abbastanza coerente per una revisione;
* `proposed`: il lavoro è una proposta revisionabile, ma non è ancora stato approvato come pronto per l'implementazione;
* `ready`: la proposta è approvata e scope, attività, dipendenze e criteri di accettazione sono sufficientemente completi per implementarla;
* `submitted`: stato di compatibilità per una SPEC approvata e pubblicata come issue GitHub; resta eseguibile;
* `closed`: il lavoro non è più attivo; `closure.reason` distingue completamento, annullamento, duplicazione, obsolescenza o altro motivo;
* `rejected`: la proposta è stata valutata e rifiutata;
* `superseded`: un'altra SPEC ha sostituito questa; indica la sostituta in `relations.related`.

Il passaggio di una SPEC a `ready` richiede sia dettaglio sufficiente sia approvazione esplicita nella richiesta dell'utente o nella documentazione consolidata del progetto. Espandere una SPEC non implica di per sé approvarla: mantienila `proposed` quando è dettagliata ma ancora in attesa di decisione.

Approvazione, pubblicazione, esecuzione e chiusura sono dimensioni separate. I file nuovi o migrati registrano `approval` e `publication` esplicitamente, conservando `status` per compatibilità: `ready` significa approvata/non pubblicata e `submitted` approvata/pubblicata. Entrambe sono implementabili. La pubblicazione modifica soltanto `publication`, i metadati GitHub e la proiezione compatibile dello stato; non revoca mai l'approvazione. `implementation.state` traccia la consegna e `closed` richiede `closure.reason`; soltanto `closure.reason: completed` prova il completamento. Nella migrazione inferisci solo valori deterministici (`ready` -> approved/unpublished, `submitted` -> approved/published) e lascia le chiusure ambigue da revisionare.

`depends_on` contiene soltanto id di SPEC prerequisito obbligatorie. `relations.related` resta un riferimento informativo e non va mai promosso automaticamente. Le dipendenze devono risolversi, non contenere auto-riferimenti o cicli ed essere coerenti con `delivery.group` e `delivery.order`: un prerequisito non può essere pianificato dopo la SPEC dipendente. Una contraddizione blocca readiness o implementazione.

Mantieni un solo `specs-index` nel percorso definito dal backend configurato. È una proiezione di navigazione e sequenziamento, non un'altra fonte del contenuto delle specifiche. Organizza ogni SPEC una sola volta con questa gerarchia:

1. **gruppo di implementazione** (`delivery.group`), in ordine numerico crescente;
2. **ambito** (`scope`), usando un identificatore canonico e stabile;
3. **ordine nel gruppo** (`delivery.order`), in ordine numerico crescente anche tra ambiti diversi.

Il gruppo è una barriera di esecuzione globale: tutte le SPEC ready selezionate del gruppo 1, qualunque sia il loro ambito, devono essere implementate e integrate prima di generare codice per il gruppo 2, e così via. Le SPEC dello stesso gruppo restano sequenziali salvo richiesta esplicita di parallelismo e compatibilità delle dipendenze. `delivery.group` e `delivery.order` devono essere interi positivi e la coppia deve essere univoca nell'intero indice; dipendenze dichiarate e ordine di consegna non possono contraddirsi. Le SPEC non ancora pianificabili possono usare valori `null` e vanno nella sezione finale **Non pianificate**, raggruppate per ambito; non possono passare a `ready` finché ambito, piattaforma, gruppo e ordine non sono definiti.

Ogni voce contiene soltanto l'id collegato al documento canonico, titolo, piattaforma, tipo, stato compatibile, approvazione, pubblicazione, stato implementativo, gruppo, ordine e data. Questi campi restano visibili ma non determinano il raggruppamento principale. Non copiare sintesi, motivazione, body, attività, criteri o evidenze di checkpoint. Aggiorna l'indice quando cambia un campo proiettato. L'`index` generale collega `specs-index`; non elenca le singole SPEC.

Fai riferimento alle altre specifiche in `relations` tramite il loro `id`, così i collegamenti restano validi prima che esista una issue. Risolvili in numeri di issue reali solo al momento della pubblicazione, leggendo il `github.issue` di ciascuna specifica referenziata.

Pubblicare una specifica come issue GitHub (o aggiornarne una già pubblicata) **non è mai automatico**: fallo solo su richiesta esplicita, e solo per specifiche con `status: ready`. Quando pubblichi:

1. risolvi `relations.parent`, `relations.children` e `relations.related` rispetto al `github.issue` delle specifiche referenziate; segnala quelli ancora irrisolti invece di indovinare;
2. crea o aggiorna la issue con `title`, `body`, `labels`, `assignees`, `milestone`;
3. imposta la relazione parent/children tramite la funzionalità nativa dei sub-issue di GitHub; rendi `related` come elenco di riferimenti incrociati nel corpo della issue, dato che GitHub non ha un tipo di collegamento non gerarchico nativo;
4. scrivi `github.issue` e `github.synced_at`, imposta `publication: published`, conserva `approval: approved`, proietta `status: submitted` e aggiorna l'indice;
5. verifica l'esito reale rileggendo la issue tramite il connector o l'API, e riporta quali issue sono state create o aggiornate, con i relativi link.

Questo passo di pubblicazione è un'azione reale e visibile ad altri: non rientra negli aggiornamenti automatici della documentazione descritti in [Limiti](#limiti); trattalo come qualsiasi altra azione visibile ad altri.

## Implementazione delle specifiche

L'implementazione di codice da SPEC non è mai automatica. Iniziala solo su richiesta esplicita e con `approval: approved`; i file compatibili `ready` e `submitted` sono entrambi idonei. Mantieni ogni repository in una sessione indipendente.

Task e sottotask della SPEC sono il piano funzionale canonico: non duplicarli altrove. Il blocco `implementation` è soltanto un checkpoint di ripresa, di responsabilità dell'orchestratore e aggiornato nella modalità RepoDoc attiva dopo ogni passo significativo, non dal worker nel branch di codice. Registra almeno branch, commit di checkpoint, revisione SPEC, controlli ed esiti legati a un commit, revisione indipendente, blocco e riferimenti PR/merge/tag. Le checkbox non sono prove. `partial` indica lavoro incompleto, `verified` implementazione e revisione positive ma integrazione non verificata, `completed` richiede integrazione verificata.

Prima di cambiare codice confronta SPEC, implementazione e test e classifica il lavoro come assente, parziale, soddisfatto o ambiguo. Implementa solo le lacune. Per lavoro già soddisfatto raccogli evidenze ed esegui i controlli senza modifiche o commit artificiali. Alla ripresa riconcilia revisione SPEC, checkpoint, codice e stato Git/PR/tag locale e remoto; riusa evidenze coincidenti e ripeti i controlli invalidati. Così le interruzioni tra merge, tag e memoria sono idempotenti.

Per più SPEC, ordinale prima per `depends_on` obbligatorio, poi `delivery.group` e `delivery.order`; fermati per dipendenze mancanti, cicli, contraddizioni o ambiguità. Processa una SPEC alla volta dal target aggiornato e fermati al primo blocco. Usa branch dedicato e worker implementativo nuovo e isolato. Poi avvia un diverso `repodoc-review-spec-worker` nuovo per il commit esatto. Il revisore è in sola lettura e controlla criteri, correttezza/regressioni, architettura/dipendenze, test e modifiche estranee, restituendo problemi bloccanti, osservazioni e riferimenti verificabili.

I problemi bloccanti tornano all'implementatore; riesegui i controlli interessati e richiedi una nuova revisione per ogni commit cambiato. Il limite dei cicli è configurabile e vale 3 per default. Al limite conserva branch e checkpoint e segnala il blocco.

La policy predefinita è `pull-request` (pull request): apri/aggiorna una PR dedicata e non integrarla. `direct-merge` è consentito solo quando la richiesta lo autorizza; l'autorizzazione per una selezione vale per tutte le SPEC selezionate. Non cambiare globalmente il target predefinito: usa `develop` solo se richiesto o convenzionale. Prima di pubblicare su un target che attiva deployment, ottieni ogni autorizzazione aggiuntiva richiesta.

Dopo una revisione positiva conserva il confine della SPEC nella storia, preferendo merge commit salvo convenzioni diverse. Verifica i controlli sul target integrato, pubblica e verifica il merge remoto, poi crea e pubblica un tag annotato sul commit risultante. Usa il naming della repository, altrimenti `spec/<spec-id-minuscolo>/completed`. Non sovrascrivere, spostare, forzare o riusare tag; verificalo sul remoto. Il tag identifica il completamento della SPEC, non una release o un deployment. Solo allora imposta `implementation.state: completed`, registra merge/tag, `closure.reason: completed`, lo `status: closed` compatibile e aggiorna l'indice. Non scartare lavoro estraneo né dichiarare E2E sulla base di soli controlli statici.

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
6. verifica che il contenuto che stai per scrivere sia coerente con la documentazione esistente; se rilevi un'incoerenza (dati contrastanti, decisioni contraddittorie, terminologia diversa), segnalala esplicitamente e chiedi come risolverla prima di salvare;
7. salva l'aggiornamento seguendo le regole del backend configurato;
8. comunica sinteticamente cosa hai registrato.

Non interrompere continuamente la conversazione per chiedere se ogni informazione debba essere salvata. Distingui autonomamente brainstorming e conoscenza consolidata.

## Limiti

Puoi modificare automaticamente solo **documentazione e memoria del progetto**. Codice, infrastruttura, pipeline, dipendenze, database, configurazioni, script e altri artefatti eseguibili richiedono una richiesta esplicita.

Questa autonomia riguarda esclusivamente gli aggiornamenti automatici della memoria e documentazione gestiti da RepoDoc. Non si estende a ogni tipo di modifica del progetto e non autorizza modifiche autonome a codice, infrastruttura, pipeline, dipendenze, database, configurazioni, script o altri artefatti eseguibili, indipendentemente dal backend configurato.

## Obiettivo

Mantenere una memoria affidabile, sintetica, aggiornata, versionata e collegata. **La chat serve per pensare; il backend configurato per ricordare; la storia resta preservata; il flusso di revisione del backend mantiene la memoria in evoluzione.**
