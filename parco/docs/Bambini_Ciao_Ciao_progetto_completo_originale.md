# BAMBINI CIAO CIAO — Documento completo del progetto

Canale YouTube **Bambini Ciao Ciao** (@BambiniCiaoCiao), video per bambini 2-6 anni, in italiano, animazione 3D con il topolino come personaggio fisso.

Fonti: la chat principale (Higgsfield, video, pubblicazioni), le due chat del 21 agosto (Remotion) e la memoria salvata. Dove una data o un dato non è stato confermato da te lo segno con *(da confermare)*.
Non incluso: i progetti Lea & Leo, The Real Backstory, The Money Backstory, che sono separati.

---

## 1. Identità del canale

| | |
|---|---|
| Nome / handle | Bambini Ciao Ciao / @BambiniCiaoCiao |
| Target | Bambini 2-6 anni, genitori italiani |
| Lingua | Italiano |
| Obiettivo | Monetizzazione |
| Etichetta | Sempre "Realizzato per bambini" (obbligo COPPA) |
| Categoria | **Istruzione per tutti i video** (decisione presa, non alternare) |
| Orario | Italia. Pubblicazione martedì e venerdì verso le 16:00 |
| Strumenti | Higgsfield (piano Ultra, Seedance 2.0), CapCut per il montaggio, YouTube Studio |
| Voce ufficiale | **Gracie** (ElevenLabs su Higgsfield) |

---

## 2. Cronologia delle chat del progetto

**21 agosto, chat 1 — "Creare video YouTube per bambini piccoli"**
- Nascita del progetto: canale creato il giorno prima.
- Panoramica della nicchia: filastrocche, video educativi, storie animate, personaggi ricorrenti.
- Regole "Made for Kids" (niente commenti, niente notifiche, pubblicità non personalizzata).
- Avviato `npx create-video@latest` (Remotion).
- Progetto Remotion completo su "Nella vecchia fattoria" (dominio pubblico): `Root.tsx`, `Farm.tsx`, `AnimalScene.tsx`, formato 1080x1920, otto animali.
- File di istruzioni e presentazione PowerPoint di 8 slide su come usarlo.
- Link YouTube di altri creatori non apribili; chiarito che non si ricreano video altrui.

**21 agosto, chat 2 — "Remotion video creation"**
- Clip HTML "La Canzone dei Numeri" (numeri 1-5 con animali e palloncini, ~25 s, 9:16).
- Clip HTML "La Canzone dei Colori" (sei palline 3D con volti, mascotte che rimbalza).

**21 agosto → 29 settembre, chat principale (Higgsfield)**
- Passaggio dai file Remotion alla generazione video con Higgsfield.
- Tutto quello che segue nelle sezioni 3-9.

---

## 3. Personaggi e riferimenti visivi

**Topolino (protagonista):** topolino da bambino, pelo grigio chiaro, grandi orecchie rotonde rosa dentro, occhi scuri grandi e lucidi, naso rosa piccolo, salopette di jeans gialla con taschino rosso sopra maglietta a righe turchesi, scalzo, coda sottile.

**Altri personaggi:**
- Mamma Topo: pelo beige, occhiali rotondi rossi, grembiule a fiori sopra vestito lilla
- Papà Topo: pelo grigio caldo, gilet di maglia blu
- Orsetto farmacista: marrone miele, camice bianco, occhialini, papillon verde
- Chip lo scoiattolo: arancio-marrone, coda folta, sciarpa verde lime
- Spike il riccio: aculei marroni morbidi, cappellino blu inclinato
- Coniglietto bianco, granchietto arancione (storia della spiaggia)

**Riferimenti salvati (da agganciare come immagini nei prompt):**

| Cosa | ID |
|---|---|
| Foglio personaggi 1 (topolino, mamma topo, orsetto farmacista) | `b598fa5d-960a-4ebf-9dca-8785fee546db` |
| Foglio personaggi 2 (topolino, scoiattolo, riccio, bottiglia e razzo) | `f7d1c48b-ac46-4b3e-a64f-093a01347740` |
| Topolino col microfono dorato | `6514cc8a-c496-4e59-a561-7ad3d71ff77f` |
| Cucina (topolino, tavolo, tovaglia a quadretti, cesto di frutta, finestra tonda) | `b35c0875-a0ac-4ec2-bcdb-c45e59e914f2` |
| Voce Gracie | `09878754-f20b-5330-9790-58a8027ab5b2` (modello text2speech_v2, variante elevenlabs) |

---

## 4. Impostazioni tecniche Higgsfield che funzionano

- Modello video: `seedance_2_0`, modalità `fast` (la `std` costa di più), 9:16, 480p, audio nativo attivo.
- Aggiungere sempre `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`, altrimenti propone un preset (es. "IN THE DARK") invece di generare.
- Il riferimento visivo deve essere **un'immagine**, mai un MP4: con un video la generazione fallisce. Per usare un fotogramma di un video: screenshot, ritaglio delle bande nere, caricamento col widget.
- **Costi:** circa 1,5 crediti al secondo in fast/480p (5 s = 7,5; 10 s = 15; 15 s = 22,5). Seedance 2.0 std 720p, 9 s = 40,5. Seedance 2.5 richiede il piano Plus (non usato). Immagine Nano Banana Pro = 2 crediti. Voce ElevenLabs ≈ 0,15 crediti. Voce Seed Audio ≈ 1-3 crediti.
- Le generazioni fallite o respinte per limite di richieste (errore 429) non vengono addebitate: si rilancia dopo qualche minuto.
- I crediti dell'abbonamento non si accumulano: si azzerano al rinnovo. Saldo al 27 agosto: 1.684,05.
- Higgsfield **non genera musica né canto**, solo voce parlata. La melodia va presa da MakeSong, dalla Libreria audio di YouTube Studio, da Pixabay o registrata a voce.
- Le voci preimpostate di Qwen non sono disponibili sull'account.

**Regole di prompt per evitare errori:**
- Scrivere "EXACTLY ONE / TWO / THREE characters, no duplicates, no clones" in ogni prompt.
- Camera ferma ("locked static camera"). Camera in movimento più personaggi che corrono produce lo sdoppiamento.
- Ambiente descritto in un blocco identico in tutte le clip, con punti fissi (scogli a sinistra, tronco a destra, ecc.).
- Gesti delle zampe semplici; il pollice in su è rischioso (dita in più). Nei prompt: "correct number of fingers".
- Testi, scritte e numeri non si fanno generare: si aggiungono in montaggio.
- I versi rari degli animali (tacchino, gufo, grillo, ape, elefante, balena, koala…) vengono spesso sbagliati dal modello: meglio silenziare e mettere un effetto vero da Pixabay.
- Il modello non sa contare: i numeri a schermo si mettono in montaggio.

---

## 5. Video prodotti e pubblicati

### 5.1 Pubblicati

| # | Video | Durata | Data | Note |
|---|---|---|---|---|
| 1 | Colori e frutta per i più piccoli (rosso fragola, giallo banana, verde mela) | ~10-13 s | sabato 22 ago | 0 views per giorni |
| 2 | Topolino Topoletto (filastrocca) | 55 s | martedì 25 ago, 16:20 | audio fatto con MakeSong, una parola cambiata |
| 3 | Il regalo o la scatola? (topolino che preferisce lo scatolone, con mamma e papà) | 22 s | venerdì 28 ago | senza parole |
| 4 | Concertino degli animali (cane, gatto, mucca, gallina, leone, maialino, pecora, rana, elefante, topolino) | 54 s | lunedì 31 ago, programmato alle 16 | |
| 5 | Il topolino ricicla (bottiglia trasformata in razzo; topolino, Chip, Spike) | 25 s | mercoledì 2 set, previsto alle 16 *(da confermare)* | 84 views in 48 h |
| 6 | Altri versi degli animali (asinello, capretta, scoiattolo, lupetto, colomba, picchio, cicala, serpentello, delfino, pinguino) | 44 s | 3 settembre | |
| 7 | Giro giro tondo (versione lunga orizzontale) | 2:17 | programmato per il 9 set | claim Content ID, vedi sezione 7 |
| 8 | Puliamo la spiaggia! (storia, 5 clip) | 31 s | prima del 29 set *(data da confermare)* | **22.128 views in 48 h** |

### 5.2 Preparati, stato non confermato
- Il coniglietto triste al parco giochi (30 s): titolo e descrizione pronti. *(pubblicazione da confermare)*
- Versi degli animali che inizia dalla capra: titolo e descrizione pronti per il 29 settembre alle 16. *(da confermare)*

### 5.3 Generati in libreria e non ancora usciti (da montare)
- **Frutta episodio 1:** hook + mela, banana, fragola, uva, arancia, pera, anguria, ciliegie, ananas, limone + finale (12 clip, 58 s). Montato e controllato (audio picco −1,6 dB).
- **Frutta episodio 2:** kiwi, pesca, prugna, melone, lampone, cocco, mirtilli, fico, mandarino, avocado (10 clip) + voce Gracie. Hook e finale si riusano dall'episodio 1.
- **Frutta episodio 3:** mango, melagrana, mora, castagna, mela verde, papaya, frutto della passione, uva bianca, pompelmo, albicocca (10 clip) + voce Gracie. Hook e finale riusati.
- **Animali, gruppo 2:** anatra, gallo, cavallo, ape, gufo, scimmia, grillo, orsetto, uccellino, tacchino (il tacchino rifatto, verso ancora sbagliato → audio da sostituire).
- **Animali, gruppo 4:** pappagallo, tigre, coniglietto, foca, gabbiano, corvo, balena, cammello, koala, cerbiatto.
- **Conteggio fino a 10** (cestino e palline, 2 clip da 10 s): generato, giunzione tra le clip poco coerente.
- **Girotondo 5 clip** (topolino, orsetto, coniglietto) e voci.

Totale clip di animali in libreria: 42.

---

## 6. Dati e cosa hanno insegnato

- **27 agosto:** 11 impressioni totali (6 Topolino Topoletto, 5 Colori), CTR 27,3%. Il canale non era bloccato: la distribuzione esisteva, ma con volumi minimi.
- **9 settembre — Il topolino ricicla:** 84 views in 48 h, 39,2% "ha continuato a guardare", durata media 0:19 su 25 s.
- **29 settembre — Puliamo la spiaggia!:** 22.128 views in 48 h. Feed Shorts 21,6K, video consigliati 160, altre funzioni 137, ricerca YouTube 104, pagine canale 37. La curva di visione parte sopra il 100% (molti rivedono) e arriva a circa il 45% a fine video.
- **Conclusione:** le **storie** (un problema, gli amici che aiutano, una soluzione) funzionano molto meglio delle sequenze didattiche (colori, frutta, versi). Il formato da privilegiare è la storia di 25-35 secondi con i personaggi ricorrenti.
- Le visualizzazioni "WhatsApp" e "Creator Studio" nelle sorgenti sono tue o di chi hai raggiunto direttamente, non distribuzione algoritmica. La voce da guardare è **Feed di Shorts**.

---

## 7. Problemi incontrati e regole che ne derivano

**Diritti d'autore**
- Mai usare audio preso da un video YouTube: Content ID lo riconosce.
- La melodia e il testo tradizionali (Giro giro tondo, Topolino Topoletto) sono liberi, **ma ogni incisione è protetta**.
- *Giro giro tondo* con audio di HeyKids Canzoni Per Bambini: la versione **Short** è stata **bloccata a livello globale** (nessun avvertimento al canale); la versione lunga si pubblica ma i ricavi vanno al titolare. Da rifare con audio proprio e riesportare.
- MakeSong: piano Avviamento 14,90 $/mese, include "Uso commerciale" ma non la licenza scaricabile; i brani si conservano 30 giorni (scaricare subito i WAV, salvare screenshot dei termini). Da verificare nei termini se la licenza dei brani resta valida dopo la disdetta.
- Non si riproducono scene, copioni o testi di video altrui: eventuali ispirazioni si trasformano in idee originali (es. spiaggia pulita al posto di un video di un altro creatore).

**Audio dei montaggi**
- Obiettivo: picco vicino a −1 dB. Primo video Topolino Topoletto saturava a 0 dB; video spiaggia era troppo basso (−25,8 dB di media) e poi corretto a −19,8.
- Il video lungo di Giro giro tondo era a 0,0 dB (saturazione) e a 1280x720: abbassare di 3 dB e, se possibile, esportare 1920x1080.

**Formato e risoluzione**
- Verticale dentro una cornice sfocata non è un vero orizzontale: su TV e computer si vede un francobollo.
- Esportazioni da CapCut risultano 1080x1880 invece di 1920: accettato da YouTube.

**Errori miei da non ripetere**
- Passare un MP4 come riferimento visivo (fallisce).
- Dare per certe le date: i giorni vanno controllati e le pubblicazioni segnate solo se le hai dette tu.
- Descrivere un video senza guardarlo (è successo con Giro giro tondo): guardare sempre più fotogrammi prima di scrivere.

---

## 8. Metodo di produzione (collaudato)

1. Foglio personaggi come immagine (2 crediti) e riferimenti fissi per ambiente e oggetti.
2. Blocco di consistenza identico in tutti i prompt.
3. Se serve la prova: una clip sola prima del resto.
4. Clip in batch; le fallite si rilanciano.
5. Voce con Gracie, una frase per scena, con pause.
6. Montaggio in CapCut: tagli secchi, audio nativo delle clip al 20-30%, voce sopra, musica libera al 15%, sottotitoli a schermo.
7. Controllo tecnico: durata, risoluzione, picco audio, fotogrammi.
8. Titolo, descrizione, tag e miniatura (per i video lunghi), "Realizzato per bambini", Istruzione, italiano.

**Costi indicativi per video (crediti):** Topolino Topoletto ≈ 245; Colori 45; Scatolone 30; Conteggio 30; Riciclo ≈ 40; Concertino ≈ 89; ogni gruppo di 10 animali o frutti 75; Spiaggia ≈ 50 (clip 46,5 + voce).

---

## 9. Miniature realizzate (Python/PIL, zero crediti)

- `miniatura_giro_giro_tondo.jpg`: 1280x720, testo ad arco rosso-arancio-verde, personaggi grandi, arcobaleno, raggi, nuvolette, stelle sul bordo, fascia rosa "Filastrocca per bambini".
- `miniatura_versi_animali.jpg`: stesso stile, "VERSI DEGLI ANIMALI", fascia "Impariamo insieme!", topolino col microfono e lupetto.
- Sugli Short la miniatura conta poco; sui video lunghi conta molto.

---

## 10. Titoli, descrizioni e tag preparati

Struttura comune di tutte le descrizioni: frase di apertura con domanda o situazione, riga sul contenuto, elenco con emoji (se serve), riga "per bambini 2-6 anni", riga "Iscriviti a Bambini Ciao Ciao…", 5-7 hashtag.

**Topolino Topoletto** — *Topolino Topoletto 🐭 Filastrocca per bambini piccoli*
Tag: filastrocche per bambini, topolino topoletto, canzoni per bambini piccoli, filastrocche italiane, cartoni animati bambini 2 anni, video per bambini
Hashtag: #filastrocche #perbambini #canzoniperbambini #cartonianimati #topolino

**Il regalo o la scatola?** — *Il regalo o la scatola? 🎁 Cartone per bambini*
Hashtag: #cartonianimati #perbambini #videoperbambini #storieperbambini #famiglia

**Il topolino ricicla** — *RICICLIAMO insieme! ♻️ Da bottiglia a razzo 🚀*
Tag: riciclo per bambini, educazione ambientale bambini, video educativi bambini, cartoni animati bambini 2 anni, storie per bambini, bambini ciao ciao
Hashtag: #riciclo #perbambini #videoeducativi #ambiente #cartonianimati #impariamogiocando

**Puliamo la spiaggia!** — *Puliamo la spiaggia! ♻️ Storia per bambini 🐭*
Tag: riciclo per bambini, storie per bambini, educazione ambientale bambini, pulire la spiaggia, cartoni animati bambini 2 anni, video educativi bambini, amicizia bambini, bambini ciao ciao
Hashtag: #riciclo #storieperbambini #perbambini #ambiente #cartonianimati #videoeducativi

**Concertino degli animali (primo)** — *I VERSI degli ANIMALI 🐄🐶 Impariamo con il topolino!*
Descrizione con l'elenco dei dieci animali e dei loro versi (bau bau, miao miao, muuu, co co dè, roaar, oink oink, beee, cra cra, peeep, squit squit).
Tag: versi degli animali, animali per bambini, video educativi bambini, imparare gli animali, suoni degli animali, cartoni animati bambini 2 anni, bambini ciao ciao

**Altri versi degli animali** — *ALTRI VERSI degli ANIMALI 🐴🐦 Impariamo con il topolino!*
Elenco: asinello, capretta, scoiattolo, lupetto, colomba, picchio, cicala, serpentello, delfino, pinguino.

**Versi degli animali, apertura con la capra** — *I VERSI degli ANIMALI per bambini 🐐🐴 Impariamo insieme!*
Tag: versi degli animali, suoni degli animali per bambini, che verso fa, animali per bambini, imparare gli animali, versi degli animali della fattoria, video educativi bambini, cartoni animati bambini 2 anni, video per bambini piccoli, bambini ciao ciao
Hashtag: #versideglianimali #suonideglianimali #perbambini #videoeducativi #animaliperbambini #cartonianimati #impariamogiocando

**Giro giro tondo** — *GIRO GIRO TONDO 🌼 Filastrocca per bambini piccoli*
Tag: giro giro tondo, filastrocche per bambini, filastrocche italiane, canzoni per bambini piccoli, girotondo, cartoni animati bambini 2 anni, bambini ciao ciao
Hashtag: #girogirotondo #filastrocche #perbambini #canzoniperbambini #cartonianimati

**Il coniglietto triste** — *Il topolino consola l'amico 🐰💙 Storia per bambini*
Hashtag: #storieperbambini #perbambini #amicizia #cartonianimati #videoeducativi #emozioni

**Descrizione del canale** (da incollare nelle informazioni):
> Benvenuti su Bambini Ciao Ciao! 🐭 Qui trovate filastrocche, canzoncine e video educativi per bambini dai 2 ai 6 anni, animati in 3D con colori vivaci e un ritmo lento e chiaro, pensato per i più piccoli. Con il nostro topolino e i suoi amici impariamo i colori, i numeri, i versi degli animali e le filastrocche della tradizione italiana. Storie semplici e allegre, senza niente che possa spaventare, perfette da guardare e cantare insieme a mamma e papà. Nuovi video ogni settimana. Ciao ciao bambini! 👋

---

## 11. Realtà della monetizzazione (stime emerse in chat)

- RPM nella nicchia bambini: circa 1-3 $ ogni 1.000 visualizzazioni; sugli Short spesso 0,03-0,10 $ ogni 1.000.
- Soglie del Programma Partner citate: 1.000 iscritti più 10 milioni di visualizzazioni Shorts in 90 giorni, oppure 4.000 ore di visione. Una soglia più alta per i nuovi richiedenti era indicata dal 1° febbraio 2027 *(da verificare su YouTube)*.
- Con "Realizzato per bambini": niente commenti, notifiche, schede e schermate finali, fan funding.
- I soldi veri della nicchia: partnership con marchi di giocattoli ed edtech, licenze, compilation lunghe (20-30 minuti in autoplay, che rendono molto più degli Short).
- Rischio da evitare: pubblicare molti video quasi identici (politica sui contenuti inautentici). Meglio storie diverse con personaggi ricorrenti.

---

## 12. Prossimi passi

1. Rifare l'audio di **Giro giro tondo** con voce/base propria e sostituire il video.
2. Montare e pubblicare le storie: priorità alle **storie** (il formato che rende).
3. Idee di storie con i personaggi già pronti: condividere un giocattolo, aiutare un amico in difficoltà, paura del buio, il primo giorno all'asilo.
4. Serie didattiche in cucina (stesso riferimento): verdure, numeri, forme, opposti.
5. Sostituire i versi sbagliati (tacchino e altri rari) con effetti reali.
6. Compilation lunghe da 20-30 minuti con le clip già in libreria (miniatura obbligatoria).
7. Tenere il ritmo martedì e venerdì verso le 16, categoria Istruzione, "Realizzato per bambini".

---

## 13. Regole di lavoro con Claude (le tue)

- Prima di ogni generazione: costo in crediti e, se esiste, un modo per spendere meno.
- Risposte corte, una cosa alla volta.
- Se qualcosa non va, si cerca un'alternativa e si continua.
- Le correzioni vanno salvate subito in memoria.
