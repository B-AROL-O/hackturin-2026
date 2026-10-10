# PoopVolt — il tuo impianto produce quanto dovrebbe?

> Copione di 3 minuti, adattato dalla bozza del team `pitch-narrative2.md`.
> Scenario illustrativo; materiali previsti: MVP software e modello STL. Il
> modello teorico è una proposta da definire e validare. Questa PR documenta la
> demo: non ne implementa il software o l'hardware.

## 0:00–0:25 — Un impianto che continua a funzionare

Anni fa un cliente ha installato un impianto fotovoltaico.

È ancora lì, sul tetto. Continua a produrre energia e, apparentemente, tutto
funziona. Ma oggi il proprietario non sa quanto produce ogni parte dell'impianto
e se le sue prestazioni siano quelle che potrebbe aspettarsi.

**Il suo impianto produce. Ma sa veramente quanto dovrebbe produrre?**

## 0:25–0:50 — Il problema nascosto

È la domanda da cui parte PoopVolt.

Il nostro protagonista è il proprietario di un impianto datato che non ha una
visione chiara della produzione delle singole stringhe, cioè i gruppi di
pannelli in serie che compongono l'impianto.

Polvere, usura e deiezioni di piccioni, da cui il nome PoopVolt, sono possibili
problemi da approfondire. Una contaminazione localizzata può influire sulle
prestazioni; il suo effetto elettrico va verificato nell'impianto specifico.

## 0:50–1:20 — Rendere visibile il divario

La nostra proposta è mettere a confronto due informazioni: **la produzione
osservata e quella attesa**.

Puntiamo a stimare la produzione attesa attraverso un modello teorico, da
definire in base alle caratteristiche dell'impianto e ai dati disponibili.

Il confronto, sullo stesso periodo e in condizioni confrontabili, vuole rendere
visibile lo scostamento e indicare dove approfondire. Il dettaglio per stringa
richiede misure e una mappatura adeguate.

Il dato diventa così un punto di partenza per capire come e dove intervenire.

## 1:20–1:35 — Dimostrazione hardware

Accanto al software presentiamo il modello STL che accompagna PoopVolt. È la
proposta fisica del progetto: il disegno digitale ne illustra il concetto,
mentre integrazione e verifica sul campo restano passaggi da completare.

_Mostrare il modello e spiegare in una frase che cosa rappresenta. Se si
mostrano componenti disponibili, distinguerli da un dispositivo collaudato._

## 1:35–2:15 — Dimostrazione software

L'MVP software serve a mostrare il percorso dal dato alla decisione.

Qui confrontiamo produzione attesa e osservata per lo stesso periodo.
Evidenziamo il divario e, dove i dati e la mappatura lo consentono, le
differenze fra le stringhe.

Il proprietario passa da «so che il mio impianto funziona» a «vedo dove sta
rendendo meno e voglio capire perché».

Ora dispone di elementi per chiedere a un tecnico, o a un'azienda come Coesa,
una verifica e una proposta di intervento.

_Mostrare soltanto funzioni presenti nell'MVP. Dichiarare dati misurati,
simulati o riprodotti da log storici, unità, periodo e metodo della stima. Se il
modello o il dettaglio per stringa non sono implementati, dichiararlo e mostrare
una simulazione esplicitamente etichettata._

## 2:15–3:00 — Dalla scoperta alla rigenerazione

Uno scostamento non identifica, da solo, la causa del problema. Ma offre al
proprietario e a Coesa un punto da cui partire.

Da qui si possono valutare pulizia, riparazione, sostituzione di componenti
guasti o una rigenerazione più ampia, secondo le evidenze raccolte. L'obiettivo
è recuperare produzione e migliorare le prestazioni dell'impianto.

Dopo l'intervento, un nuovo confronto in condizioni comparabili permette di
verificare e misurare il beneficio. Non tutto il divario è necessariamente
recuperabile.

**PoopVolt: conoscere il proprio impianto datato, per decidere come farlo
rendere meglio.**

## Note per il team prima della presentazione

- Confermare il modello teorico, gli input disponibili e le condizioni del
  confronto.
- Usare dettaglio per stringa solo con mappatura e misure verificate.
- Distinguere uno scostamento dalla stima da un calo dimostrato con dati
  storici.
- Tenere separati foto RGB con sporco simulato e replay storico SOLARMA: non
  sono misure dello stesso impianto o dello stesso evento.
- Non ricavare hotspot, perdita elettrica o kWh persi da una fotografia RGB.
- Presentare la rigenerazione come valutazione tecnica, senza garantire
  recuperi.
- Chiarire la funzione del modello STL; il file e la demo software vanno
  collegati quando disponibili, senza considerarli implementati da questa PR.
- Provare copione e demo entro 3 minuti e preparare una registrazione di
  riserva.

La [scaletta](../presentation/plan/agenda.md) e il
[piano del parlato](../presentation/plan/speech_plan.md) seguono questo copione.
Il [pitch di progetto](pitch-draft.md) conserva il contesto commerciale
proposto.
