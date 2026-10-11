# PoopVolt — Il tuo impianto è sporco di merda

> Copione italiano per un video motion graphics di **2 minuti**: sei scene, voce
> fuori campo e schema elettrico in primo piano. Leggere soltanto i blocchi
> **Voce**. Il gancio è illustrativo; il confronto software usa un replay
> storico; l'hardware è un prototipo di bring-up. Il modello teorico e i
> benefici sul campo restano da validare. Questo documento pianifica il video,
> non ne produce il montaggio.

## 0:00–0:12 — Il gancio

**Voce:**

Il tuo impianto è sporco di merda. Letteralmente.

Ma quanto sta influendo sulla produzione? È da questa domanda che nasce
PoopVolt.

**A schermo:** «Quanto sta producendo davvero?» · «Scena illustrativa».

**Movimento:** un piccione entra nell'inquadratura di un pannello stilizzato;
compare una deiezione. Pausa breve su «Letteralmente». Il pannello si riduce
accanto alla domanda. Nessun numero di perdita associato allo sporco.

## 0:12–0:30 — Il problema dell'azienda

**Voce:**

Un impianto installato da anni produce ancora. Il proprietario non sa se rende
quanto dovrebbe. L'azienda che lo segue deve spiegare perché vale la pena
verificarlo. Per proporre un intervento servono evidenze comprensibili.

**A schermo:** «Funziona. Ma rende quanto dovrebbe?».

**Movimento:** lo stesso pannello diventa un impianto; ai lati entrano
proprietario e tecnico. Una linea collega la domanda del proprietario alla
verifica del tecnico. Mantenere i due ruoli nelle scene successive.

## 0:30–0:50 — Rendere visibile il divario

**Voce:**

PoopVolt confronta produzione osservata e riferimento atteso, nello stesso
periodo. Oggi abbiamo un confronto con gli altri inverter; il modello teorico,
corretto per le condizioni ambientali, è il prossimo passo. Lo scostamento
indica dove approfondire, non identifica la causa.

**A schermo:** «Osservata / Attesa» · «Confronto fra inverter: disponibile» ·
«Modello teorico: da sviluppare».

**Movimento:** entrano due etichette, poi la cornice del confronto. Evidenziare
il passaggio «Scostamento → Verifica». Il risultato numerico arriva nella scena
del replay; qui non disegnare una curva teorica inventata.

## 0:50–1:15 — Mostrare lo schema elettrico

**Voce:**

Il prototipo usa Arduino UNO Q: temperatura, umidità, luce, display e NFC. Lo
schema mostra anche il sensore di corrente sul percorso pannello, caricatore e
batteria. La corrente sotto luce resta da verificare. La scheda è alimentata via
USB; il ramo solare è separato.

**A schermo:** «Schema elettrico del prototipo» · «UNO Q: alimentazione USB» ·
«Corrente: zero verificato, misura sotto luce da validare».

**Movimento:** taglio sullo
[schema elettrico completo](#schema-elettrico-da-mostrare). Da 0:50 a 0:55
mostrare l'intera tavola. Da 0:55 a 1:05 avvicinare UNO Q e Grove: evidenziare
I2C per AHT20/LCD, A0 per la luce e UART per NFC. Da 1:05 a 1:12 spostare il
fuoco sul percorso pannello → sensore di corrente → Waveshare → LiPo e sulla
lettura A1. Chiudere tornando alla tavola completa fino a 1:15. Usare contorni
ed etichette sovrapposti, lasciando intatti simboli e reti. Non animare un
collegamento dal caricatore all'alimentazione UNO Q: USB OUT non è collegata.

## 1:15–1:40 — Una prova software concreta

**Voce:**

Nel replay dei dati SOLARMA confrontiamo tredici inverter. Nel periodo mostrato,
l'inverter uno registra zero energia, contro circa duecentonovantadue
kilowattora attesi dal confronto con i suoi pari. Il software lo segnala per
ispezione. È un dato storico riprodotto, non una misura del nostro pannello né
una diagnosi di sporco.

**A schermo:** «REPLAY STORICO · SOLARMA · 13 inverter» · «1 agosto–17 settembre
2019 · Inverter 1» · «Osservata: 0 kWh · Attesa dai pari: 292 kWh» · «Candidato
per ispezione».

**Movimento:** taglio netto dal circuito al
[grafico del replay](images/comparison-inverter-1-replayed.svg). Mostrare assi,
unità, legenda e periodo fin dall'inizio; rivelare insieme le serie originali,
poi evidenziare il divario e la segnalazione. Tenere il grafico fermo per almeno
otto secondi. Non trasformare il pannello illustrato nel grafico: sono fonti
indipendenti. Fonte e limiti: [risultati del confronto](comparison-results.md).

## 1:40–2:00 — Dalla verifica alla proposta

**Voce:**

Il tecnico approfondisce e propone pulizia, riparazione o sostituzione, quando
serve. Il proprietario valuta. Dopo l'intervento, misure comparabili verificano
il beneficio: non tutto il divario è recuperabile.

PoopVolt trasforma uno scostamento produttivo in una proposta di intervento
comprensibile.

**A schermo:** «Verificare → Proporre → Scegliere → Misurare» · «PoopVolt ·
Evidenze per la manutenzione fotovoltaica».

**Movimento:** ritorno a tecnico e proprietario. Le quattro fasi entrano una
alla volta; la scelta resta al proprietario. Chiudere sul logo e sul messaggio
finale, fermi per gli ultimi tre secondi. Nessuna curva di recupero o promessa
di risparmio.

## Schema elettrico da mostrare

![Schema elettrico PoopVolt: UNO Q alimentata via USB, moduli Grove e ramo solare separato](architecture/diagrams/pv-wiring.svg)

[Apri SVG](architecture/diagrams/pv-wiring.svg) ·
[Scarica PDF](architecture/diagrams/pv-wiring.pdf) ·
[Connessioni e stato delle verifiche](hardware-connections.md) ·
[Sorgente KiCad](../hardware/poopvolt.kicad_sch)

Il diagramma `pv-wiring` registra le connessioni del prototipo riportate dal
team. Conservare il ramo solare separato dall'alimentazione USB della scheda.
Ritagli e zoom sono scelte di montaggio, non nuovi schemi. Le modifiche
elettriche partono dal sorgente KiCad e dal suo workflow di esportazione; non
modificare SVG e PDF generati a mano.

## Indicazioni di montaggio

- Durata totale: **120 secondi**, pause e chiusura comprese. Registrare soltanto
  la voce, poi adattare i movimenti ai sei intervalli; provare il parlato prima
  del montaggio definitivo.
- Usare formato 16:9, 1920 × 1080, e la palette blu scuro, giallo solare, bianco
  e grigi delle [linee guida di brand](../brand-guidelines.md).
- Una composizione per scena; frasi brevi a schermo, sottotitoli del parlato,
  transizioni di 200–300 ms. Preferire ingressi, evidenziazioni e zoom motivati
  dalla spiegazione; mantenere fermi i contenuti durante la lettura.
- Tenere leggibili etichette di stato, fonti e unità anche durante il movimento.
  Niente contatori animati, dashboard fittizie o effetti di energia in transito
  che sembrino misurazioni dal vivo.
- Lo schema sostituisce l'STL nella sequenza principale: nessun modello STL è
  consegnato nel repository. Inserirlo solo in materiale aggiuntivo quando
  disponibile e identificarlo come concept.
- Modello teorico, rilevamento validato dello sporco e benefici sul campo
  restano lavoro futuro. La
  [pipeline di ispezione da telefono](phone-inspection.md) ha upload, adattatore
  ONNX e interfaccia implementati; modello addestrato e verifica su UNO Q sono
  ancora da completare. Le proposte qui attribuite al tecnico non sono un output
  automatico del replay.

La [scaletta](../presentation/plan/agenda.md), il
[piano del parlato](../presentation/plan/speech_plan.md) e il
[piano visuale](../presentation/plan/plots_plan.md) seguono questi tempi. Il
[pitch di progetto](pitch-draft.md) conserva il contesto commerciale. Il
[video Devpost in inglese](video/README.md) ha un copione e materiali distinti:
sottotitoli e card esistenti non sono il montaggio di questa versione.
