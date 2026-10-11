# PoopVolt — Brand guidelines

**Stato:** bozza per revisione del team, 11 ottobre 2026.

Questo documento propone l'identità comune di PoopVolt per repository,
documentazione, presentazioni, video e futura interfaccia. Le regole diventano
il riferimento condiviso dopo la revisione del team. Non attestano funzionalità
del prodotto né risultati sperimentali.

## 1. Identità e posizionamento

PoopVolt aiuta a rendere comprensibili gli scostamenti nella produzione
fotovoltaica, fornendo elementi per una verifica e una proposta di intervento.
L'azienda di manutenzione è l'utilizzatore principale; il proprietario
dell'impianto è il destinatario delle evidenze e della proposta.

**Messaggio principale proposto:**

> PoopVolt trasforma uno scostamento produttivo in una proposta di intervento
> comprensibile.

**Descrittore breve proposto:**

> Evidenze per la manutenzione fotovoltaica.

Il confronto fra produzione osservata e riferimento atteso è il centro del
racconto. Sporco, deiezioni e usura sono possibili problemi da approfondire:
uno scostamento, da solo, non ne identifica la causa.

L'Edge AI e la manutenzione predittiva descrivono la direzione del progetto.
Quando si presenta la demo, dichiarare quali parti funzionano e quali sono
ancora previste. Le linee guida di brand non sostituiscono lo stato del progetto.

### Nome

- Scrivere sempre **PoopVolt**, con P e V maiuscole.
- Usare **Team B-AROL-O** per l'attribuzione al team.
- Tenere separati nome del prodotto, nome del team e nome dell'evento.
- Conservare i nomi tecnici esistenti nei percorsi e nel codice.

## 2. Personalità e voce

Il brand è diretto, concreto e accessibile. L'ironia rende memorabile l'apertura;
la precisione rende credibile ciò che segue.

- Parlare prima del problema dell'utente, poi della tecnologia.
- Preferire frasi brevi, verbi concreti e termini comprensibili.
- Spiegare i termini tecnici quando servono al pubblico.
- Presentare numeri insieme a origine, periodo, unità e limiti essenziali.
- Distinguere capacità attuali, obiettivi e ipotesi commerciali.

L'apertura «Il tuo impianto è sporco di merda. Letteralmente.» appartiene al
pitch concordato. Non diventa automaticamente il tono di report, documentazione
o messaggi dell'interfaccia. Il piccione introduce il nome; le evidenze guidano
il resto della storia.

| Preferire | Evitare |
| --- | --- |
| «Questo inverter produce meno dei suoi pari: va verificato.» | «Abbiamo diagnosticato lo sporco» senza una diagnosi validata. |
| «Confronto su dati storici riprodotti.» | Presentare un replay come una misura del prototipo. |
| «Il tecnico valuta il prossimo intervento.» | Attribuire al software una proposta formulata manualmente. |
| «Il beneficio va verificato dopo l'intervento.» | Promettere recuperi energetici o risparmi garantiti. |

## 3. Logo

Il riferimento visivo della bozza è il file fornito dal team,
**Logo_PoopVolt.png**: composizione orizzontale con pannello, piccione e nome.
Il file originale è integrato nella repository:
[Logo_PoopVolt.png](assets/brand/Logo_PoopVolt.png). Provenienza e stato delle
varianti sono registrati in [assets/brand/README.md](assets/brand/README.md).

Conservare l'originale. Registrare autore, provenienza e autorizzazione d'uso
prima di pubblicare il kit. La licenza del codice non determina da sola la
licenza del marchio.

### Uso principale

- Usare la composizione completa su fondo bianco nella prima integrazione.
- Mantenere le proporzioni originali e tutti gli elementi del logo.
- Ridimensionare senza deformazioni e senza superare la risoluzione utile.
- Conservare il colore e la forma del pannello giallo.
- Valutare lo spazio intorno alla grafica visibile, non ai bordi del file.

**Spazio di rispetto proposto:** almeno metà dell'altezza della P del marchio
tipografico su ciascun lato della composizione visibile. È una regola iniziale
da verificare sulle applicazioni reali.

La dimensione minima non è ancora fissata. Prima di definirla, verificare logo
nel README, su una slide proiettata e su uno schermo mobile: nome, piccione e
separazioni del pannello devono rimanere distinguibili.

### Varianti da preparare

| Variante | Uso previsto | Stato |
| --- | --- | --- |
| PNG originale completo | Archivio e prima integrazione su bianco | Integrato |
| Composizione con margini ridotti | Header e copertine | Da preparare |
| Versione trasparente | Fondi chiari compatibili | Da preparare e verificare |
| Versione monocromatica e inversa | Stampa e fondi scuri | Da progettare |
| Simbolo compatto | Avatar e icone | Da progettare e verificare in piccolo |
| Originale vettoriale | Stampa e ridimensionamento | Disponibilità da verificare |

Un SVG che incorpora il PNG non equivale a un originale vettoriale.
Non usare varianti finché non sono disponibili e revisionate.

### Usi scorretti

Non stirare, ruotare, ricolorare o ricomporre il logo. Non aggiungere ombre,
contorni o effetti. Non sovrapporlo a immagini che ne compromettono la lettura.
Non rimuovere il fondo bianco senza verificare i bordi. Non ricreare la scritta
con un font simile e presentarla come logo ufficiale.

Il significato della cella gialla frammentata va confermato con l'autore:
non attribuirle una spiegazione ufficiale prima di questa verifica.

## 4. Colori

La palette proposta si concentra su blu scuro e giallo, coerenti con il logo,
accompagnati da bianco e grigi neutri. I valori di blu e giallo sono proposte
operative, non un campionamento certificato del file originale.

| Nome | Valore proposto | Ruolo |
| --- | --- | --- |
| Blu PoopVolt | `#0D2D44` | Titoli, testo principale, copertine scure |
| Giallo solare | `#F5C329` | Accenti, richiamo al pannello, evidenze selezionate |
| Bianco | `#FFFFFF` | Fondo del logo originale e superfici di supporto |
| Grigio chiaro | `#F4F5F7` | Superfici secondarie e fasce di incertezza |
| Grigio testo | `#52606D` | Didascalie, fonti e serie di riferimento su bianco |
| Grigio separatore | `#D8DEE4` | Linee e divisori non essenziali |

Usare soprattutto fondi chiari e testo scuro; riservare il giallo a pochi
accenti. Sul giallo usare testo blu scuro. Non usare il giallo come testo
piccolo su bianco o grigio chiaro.

I precedenti verde petrolio, ruggine, ambra e neutri con dominante verde o
avorio sono esclusi dalla nuova palette. Per nuovi materiali usare solo i
colori della tabella. I colori presenti nelle fotografie restano naturali.
Eventuali colori funzionali aggiuntivi per errori o stati dell'interfaccia
richiedono una convenzione documentata; non diventano accenti decorativi.

Verificare le combinazioni finali: contrasto minimo 4,5:1 per testo normale
e 3:1 per testo grande. Stati, serie e anomalie devono essere riconoscibili
anche tramite parole, forme o tratteggi, senza dipendere dal colore.

La palette è una proposta di migrazione. Le card attuali non sono già state
aggiornate; evitare sostituzioni parziali che producano nuovi disallineamenti.

## 5. Tipografia

**Famiglia proposta:** Source Sans 3, per titoli, testo, didascalie e grafici.
Usare principalmente regular e semibold; monospace solo per codice e identificatori.
Il carattere del logo resta parte dell'asset e non va sostituito.

Source Sans 3 deve essere acquisita, inclusa con la sua licenza e resa disponibile
anche al processo di rendering. Finché questo passaggio non è completato, usare
un fallback dichiarato e uniforme. Le card video attuali sono renderizzate con
DejaVu: non presumere che usino già Source Sans 3.

Per slide 1600 × 900, partire da margini di 72 px, titoli di 64 px,
testo di 32 px e fonti di 22 px. Sono riferimenti iniziali: adattare la
composizione alla leggibilità effettiva. Su altri formati scalare le proporzioni
e verificare l'esportazione. Ridurre il contenuto prima di ridurre il testo.

## 6. Composizione e immagini

- Una domanda o un messaggio principale per schermata.
- Allineamenti semplici, spazio vuoto generoso e massimo due colonne principali.
- Titoli che spiegano il punto della slide, oltre all'argomento.
- Fotografie reali del prototipo e del suo utilizzo quando disponibili.
- Piccione come richiamo secondario, senza trasformare ogni schermata in una battuta.
- Logo completo in apertura e chiusura; nelle altre schermate solo se utile.

Conservare provenienza e permessi delle immagini. Segnalare scene preparate,
illustrazioni e concept. Non rappresentare un mockup come interfaccia funzionante
o una foto RGB come misura termica. Non tagliare dettagli necessari a comprendere
l'evidenza.

## 7. Grafici, diagrammi ed evidenze

Grafici e card devono usare la stessa tipografia e palette. Adattare il
generatore dei grafici, evitando modifiche manuali ai soli file esportati.

| Informazione | Convenzione proposta |
| --- | --- |
| Produzione osservata | Blu, linea continua e punti pieni |
| Riferimento atteso | Grigio testo, linea tratteggiata e indicazione della stima |
| Intervallo di incertezza | Fascia grigio chiaro con legenda esplicita |
| Scostamento da verificare | Richiamo giallo con testo blu, simbolo e annotazione esplicita |
| Dato simulato | Etichetta visibile «SIMULATO» e trattamento distinguibile |

Ogni figura quantitativa deve indicare unità, periodo, fonte e origine dei dati:
**misurati**, **replay storico**, **simulati** oppure **stimati**. Una serie può
richiedere più qualificazioni, ad esempio osservazioni riprodotte e riferimento
stimato. Distinguere sempre un dato assente da uno zero.

Conservare nomi, confini e significato dei diagrammi di architettura. Le versioni
semplificate per le slide devono rimandare alla fonte canonica e mantenere
visibile lo stato proposto quando applicabile.

Non usare un'immagine di sporco per spiegare causalmente una perdita registrata
su un altro impianto. Non presentare energia mancante come energia recuperata.

## 8. Applicazioni e fonti di riferimento

- **README:** logo, descrizione breve e accesso evidente a stato del progetto e demo.
- **Presentazione:** identità comune, una storia centrata sull'utente e fonti leggibili.
- **Video:** card coerenti, qualificazioni visibili e testo verificato su mobile.
- **Documentazione:** priorità a lettura, navigazione e precisione tecnica.
- **Interfaccia futura:** brand nei dettagli; priorità a chiarezza di dati e azioni.

Questo documento propone le regole comuni del brand. Le linee guida specifiche
della presentazione devono richiamarlo e aggiungere solo indicazioni relative
a slide, movimento e formato. In caso di divergenza, allineare i documenti
durante la revisione, senza considerare questa bozza un'approvazione implicita.

Le affermazioni sul prodotto restano subordinate alla documentazione tecnica,
allo stato di implementazione e alle evidenze disponibili.

## 9. Decisioni aperte per la revisione

- [ ] Confermare messaggio principale e descrittore breve.
- [ ] Confermare autore, provenienza e condizioni d'uso del logo.
- [ ] Confermare il significato del pannello giallo frammentato.
- [ ] Verificare originale vettoriale, trasparenza e varianti necessarie.
- [ ] Confermare colori definitivi e contrasto delle applicazioni.
- [ ] Confermare Source Sans 3 e includere file e licenza.
- [ ] Verificare spazio di rispetto e dimensione minima su esempi reali.
- [ ] Allineare le linee guida della presentazione.
- [ ] Pianificare l'aggiornamento coerente di card e grafici.

La prima PR può introdurre asset originale, provenienza, questo documento e
logo nel README. L'adozione della palette e della tipografia negli altri
materiali va verificata con confronti visivi prima/dopo.
