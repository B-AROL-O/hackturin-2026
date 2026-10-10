# PoopVolt — Il tuo impianto è sporco di merda

> Copione di 3 minuti, adattato dalla bozza del team `pitch-narrative2.md` e
> dalle successive revisioni concordate. Scenario illustrativo; materiali
> previsti: MVP software e modello STL. L'azienda usa i dati per proporre
> interventi che il cliente possa comprendere e valutare. Il modello teorico è
> una proposta da definire e validare. Questa PR documenta la demo: non ne
> implementa il software o l'hardware.

## 0:00–0:25 — L'apertura

**Il tuo impianto è sporco di merda.**

_Pausa._

**Letteralmente. Ma il problema è capire quanto sta influendo sulla
produzione.**

Un cliente ha un impianto fotovoltaico installato da anni. Produce ancora, ma
lui non sa se sta rendendo quanto dovrebbe.

È da questa domanda che nasce PoopVolt.

## 0:25–0:50 — Il problema dell'azienda

Ora pensate all'azienda che installa o segue questi impianti.

Come spiega al cliente perché vale la pena verificare un impianto che,
apparentemente, funziona?

Polvere, usura e deiezioni di piccioni sono possibili problemi da approfondire.
Ma per motivare un intervento servono dati comprensibili: che cosa osserviamo,
dove approfondire e che cosa possiamo proporre.

## 0:50–1:20 — Rendere visibile il divario

PoopVolt vuole aiutare l'azienda a proporre interventi motivati dai dati che il
cliente possa comprendere e valutare.

La nostra proposta confronta **produzione osservata e produzione attesa**.
Puntiamo a stimare quella attesa con un modello teorico, da definire in base
all'impianto e ai dati disponibili.

Il confronto rende visibile lo scostamento e indica dove approfondire. Così
l'azienda ha una base per spiegare al cliente il prossimo passo.

## 1:20–1:35 — Dimostrazione hardware

Accanto al software presentiamo il modello STL che accompagna PoopVolt. Il
disegno digitale illustra la proposta fisica del progetto. Integrazione e
verifica sul campo restano passaggi da completare.

_Mostrare il modello e spiegarne la funzione. Distinguere il concept e i
componenti disponibili da hardware collaudato._

## 1:35–2:15 — Dimostrazione software

Nel software mostriamo il percorso dal dato alla proposta di intervento.

Confrontiamo produzione attesa e osservata per lo stesso periodo. Evidenziamo lo
scostamento e, dove i dati lo consentono, le differenze fra stringhe con
mappatura verificata.

L'azienda può mostrare al cliente dove approfondire, spiegare quali verifiche
servono e proporre il prossimo passo. Il cliente ha elementi per comprendere e
valutare la proposta.

_Mostrare soltanto funzioni presenti nell'MVP. Dichiarare origine dei dati,
unità, periodo, riferimento della stima e copertura. Se il modello o il
dettaglio per stringa non sono implementati, usare una simulazione
esplicitamente etichettata. Non descrivere una proposta manuale del tecnico come
un output automatico del software._

## 2:15–3:00 — Dalla proposta alla verifica del beneficio

Uno scostamento non identifica, da solo, la causa. Offre all'azienda e al
proprietario un punto da cui partire.

Un'azienda come Coesa può valutare pulizia, riparazione, sostituzione di
componenti guasti o una rigenerazione più ampia, e spiegare al cliente perché
propone quell'intervento.

L'obiettivo è recuperare produzione e migliorare le prestazioni. Dopo
l'intervento, un confronto in condizioni comparabili permette di verificare il
beneficio: non tutto il divario è recuperabile.

**PoopVolt trasforma uno scostamento produttivo in una proposta di intervento
comprensibile.**

## Note per il team prima della presentazione

- L'apertura è una scena illustrativa; non attribuisce una perdita misurata allo
  sporco.
- Presentare l'azienda come utilizzatore del prodotto e il proprietario come
  destinatario delle evidenze e della proposta.
- La distribuzione gratuita resta un'ipotesi commerciale secondaria, non un
  accordo.
- Confermare modello teorico, input, unità, periodo e condizioni del confronto.
- Usare dettaglio per stringa solo con mappatura e misure verificate.
- Distinguere lo scostamento dalla stima da un calo storico e da una diagnosi.
- Tenere separati foto RGB con sporco simulato e replay storico SOLARMA.
- Non ricavare hotspot o kWh persi da una fotografia RGB.
- Non promettere richieste di intervento, benefici commerciali o recuperi
  garantiti.
- Chiarire quali raccomandazioni produce il software e quali formula il tecnico.
- Collegare il modello STL e la demo software quando disponibili.
- Provare copione e demo entro 3 minuti e preparare una registrazione di
  riserva.

La [scaletta](../presentation/plan/agenda.md) e il
[piano del parlato](../presentation/plan/speech_plan.md) seguono questo copione.
Il [pitch di progetto](pitch-draft.md) conserva il contesto commerciale
proposto.
