# Sessione session_01WeZD3EBshsBb5mxg9qdvnt - YouTube project setup e regole (The Senior Advantage: short 4 LIHEAP, copertine, video correlati, passaggio chat)

Esportazione dei soli messaggi dell'utente e del testo visibile dell'assistente, in ordine cronologico (orari UTC).

## human - 2026-10-01T21:26:03.823033Z

CONTESTO GENERALE
Lavoro con te sul mio progetto YouTube. Repo GitHub: kovacevstevo1993-gif/Tr, ramo claude/money-backstory-project-bqq9ic (cartella /home/user/Tr). Leggi per prima /home/user/Tr/CLAUDE.md: contiene le regole permanenti. Poi senior_advantage/README.md e senior_advantage/MEMORIA-CANALE.md.

HO DUE CANALI SEPARATI. NON MESCOLARE MAI TEMI, STILE O DATI.
1) The Senior Advantage (@TheSeniorAdvantage), cartella senior_advantage/. Vecchio canale di circa 1.700 iscritti americani, rilanciato. Tema: sconti, benefici e aiuti per over 60 USA. Slide verde bosco e avorio (oro e rosso come accenti). Short verticali 1080x1920, video lunghi 1920x1080.
2) The Money Backstory (@TheMoneyBackstoryUSA), cartella money_backstory/. Tema: pensione USA over 50 (Social Security, Medicare, tasse). Slide blu navy e oro con cornice 3D. Miniature in stile rosso/verde dei miei video 1 e 2, font Montserrat ExtraBold.

COME LAVORO / REGOLE (valgono sempre)
- Risposte corte. Niente scuse e niente "hai ragione". Una cosa alla volta. Verificare prima di dare un'indicazione.
- Eseguire SOLO quello che dico. Non fare di testa tua, non rifare quello che ho già montato o sistemato (il blocco 1 lo avevo sistemato io), non proporre di fermarmi.
- Non mettere file o cartelle che non ho chiesto. Se chiedo un testo, lo scrivi QUI in chat (mi sono arrabbiato quando ho trovato il copione tradotto nella cartella: l'ho fatto togliere).
- Mai spendere crediti vidIQ senza dirlo e chiedere prima, tranne quando lo autorizzo nel messaggio.
- Titolo, descrizione e tag devono essere già completi da incollare, con Subscribe e disclaimer. Niente segnaposto, niente [T_...].
- Dirmi PRIMA dove va ogni nuovo video (playlist, cosa creare o cancellare su YouTube).
- Gli orari dei capitoli si prendono dalla mia timeline, non si stimano dal testo.
- Slide e grafica le fai tu con il codice (gratis).
- Disclaimer: per TUTTI i video lunghi di ENTRAMBI i canali, NON per gli short. Va alla FINE, in una slide finale in chiaro con testo grande, e la frase detta a voce nell'ultimo blocco. In più sempre nella descrizione e nel commento fissato. Non all'inizio.
- Il disclaimer non protegge da YouTube. Contano: contenuto originale, dati verificati su fonti ufficiali, niente promesse di guadagno, niente persone/avatar AI che si presentano come esperti.
- Fatti solo da fonti ufficiali (siti governativi/ufficiali delle aziende).
- Le miniature devono avere la frase che ho in mente io, se te la dico.
- Dai prossimi video: slide più movimentate, più dettagliate, più oggetti disegnati in ogni didascalia (il primo video lungo "è sciatto e basico", ma per il primo va bene).
- Dove ci sono screenshot/timeline: le durate dei blocchi partono SEMPRE dalla fine del blocco precedente letta nello screenshot, MAI dalla somma dei miei clip. (L'errore sul blocco 21 è nato da questo.)

STATO DEL LAVORO: THE SENIOR ADVANTAGE, VIDEO LUNGO 1
Titolo del video (punteggio vidIQ 94/100): "Senior Discounts Start at 55, Not 65: 12 Hidden Places (Most Never Ask)". Alternativa (90/100): "Senior Discounts at 55, Not 65: 12 Places That Never Tell You".
Durata totale del video: 11:01. Montato da me in CapCut, con la voce in inglese generata da CapCut blocco per blocco (36 blocchi).

Cosa è stato fatto (tutto già in repo e già mandato a me):
- Copione di 36 blocchi in inglese: senior_advantage/COPIONE-VIDEO-LUNGO-1.md e copione_video_lungo_1.py (lista B). Fonti ufficiali: FONTI-VIDEO-LUNGO-1.md.
- Clip slide 1920x1080 a 30 fps per tutti i 36 blocchi in senior_advantage/video_lungo_1/blocoNN-slideKK.mp4. Il totale dei fotogrammi di ogni blocco coincide con la durata letta dai miei screenshot di CapCut.
- Codice dei clip: senior_advantage/code/. Il motore è engine.py. long1_b01.py è il blocco 1. long1_blocks.py copre i blocchi 2-6, long1_blocks2.py i 7-11, long1_blocks3.py i 12-20, long1_blocks4.py i 21-36 (compresa la slide finale del blocco 36 con il disclaimer e il riquadro tratteggiato "WATCH NEXT"). Uso: python3 long1_blocksN.py <blocco> [clip]. Per rendere servono ffmpeg e SA_TMP per frame separati se si renderizza in parallelo. ffprobe non esiste: per le durate si usa ffmpeg -i. Il blocco 21 è stato rifatto a 862 fotogrammi (era 882, sbagliato).
- Durate dei blocchi 21-36 in fotogrammi: 21: 862, 22: 507, 23: 505, 24: 505, 25: 543, 26: 455, 27: 709, 28: 459, 29: 433, 30: 416, 31: 553, 32: 782, 33: 534, 34: 353, 35: 319, 36: 594.
- Ho controllato il video con una mia registrazione dello schermo (3:08, scorre la timeline). Ho confrontato slide e didascalia in 63 punti e non ho trovato nessuna slide fuori posto. Un taglio fuori di pochi fotogrammi non si vede in quei campioni.
- Il copione tradotto in italiano è stato dato in chat (non salvato in cartella).

Pacchetto SEO pronto (da incollare su YouTube):
- Playlist: la playlist esistente "Senior Discounts" (ci sono gli short 1 e 2). Mettere il video lungo come primo video della playlist. Gli aiuti (pasti a domicilio ecc.) vanno in un'altra playlist.
- Descrizione: prima riga con "Senior discounts start at 55..." (parola chiave nei primi 125 caratteri), capitoli, fonti, riga Subscribe (https://www.youtube.com/@TheSeniorAdvantage?sub_confirmation=1), disclaimer, hashtag #seniordiscounts #seniorsavings #over55. Capitoli: 0:00, 0:22, 0:40, 0:59, 1:15, 1:40 (#1 Denny's e IHOP), 2:20 (#2 Walgreens), 3:11 (#3 Ross), 3:23 (#4 Kohl's), 3:43 (#5 Savers e Goodwill), 4:01 (#6 Michaels), 4:25, 4:51 (#7 telefono), 5:20 (#8 AMC), 5:42 (#9 Amtrak), 6:17 (#10 bus e metro), 6:45 (#11 Senior Pass parchi, $80 a vita), 7:54 (#12 AARP), 8:33 (trucco hotel), 8:48 (3 errori), 9:35 (riepilogo), 10:01 (piano), 10:41 (disclaimer). Gli orari dei blocchi 1-20 sono calcolati dalle durate dei clip, quelli dal 21 dalle mie fine blocco: possono sbagliare di circa 1 secondo. Da controllare sulla mia timeline se voglio esattezza.
- Tag (448 caratteri): senior discounts, senior discounts at 55, senior citizen discounts, hidden senior discounts, senior discount list, stores with senior discounts, senior discounts restaurants, discounts for seniors over 55, senior savings, senior benefits, senior discount age, walgreens senior discount, kohl's senior discount, amtrak senior discount, national parks senior pass, aarp discounts, senior phone plans, senior discounts 2026, senior discounts usa, ask for senior discount.
- Commento da fissare: "Which of the 12 places did you NOT know about? Tell me below 👇 And save this video: prices and ages change, and I'll keep it updated."
- Impostazioni: IA No, promozione No, schermata finale negli ultimi 20 secondi (Iscriviti + miglior video della playlist; il riquadro tratteggiato nella slide finale indica dove).
- Dati vidIQ (US): "senior discounts" 12.828 ricerche/mese, concorrenza 26,3. "senior discount" 9.826, conc. 20,7. "senior citizen discounts" 4.821, conc. 30,8. "hidden senior discounts" 4.045, conc. 23,6. "senior savings" 3.786, conc. 26,2.
- Crediti vidIQ: ne restano 5 (ogni ricerca keyword e ogni punteggio titolo costa 5). Si rinnovano il 29/10/2026. Non spenderli senza chiedermi.

MINIATURE (cartella senior_advantage/miniature/, 1280x720, codice in senior_advantage/code/thumb_long1*.py)
- A: video-lungo-1-55-not-65.png. Verde e oro: "STARTS AT 55 / NOT 65 (barrato) / NOBODY TELLS YOU", cartellino 55+, carta d'identità, coupon -10%.
- B: video-lungo-1-stop-paying-full-price.png. Giallo a raggi, personaggio sorpreso semplice, scontrino $50 barrato -> $40, bollino 55+ OFF.
- C: video-lungo-1-nonno-stop-paying-full-price.png. La più dettagliata: nonno disegnato con capelli, rughe, occhiali dorati, baffi, papillon e cardigan; titolo "STOP PAYING FULL PRICE"; cartellino "55+ SENIOR PRICE"; cartellini -30% Savers, $80 Parks for life, -20% Walgreens, -15% Kohl's, -10% Ross/Michaels. Questa è l'ultima richiesta, già fatta.
- Consiglio dato: caricare due miniature (per esempio A e C) con "Test e confronta" di YouTube Studio e tenere quella con più clic. Le scritte piccole dei cartellini non si leggono sul telefono, si leggono i numeri grandi e il titolo.

THE MONEY BACKSTORY (altro canale, non mescolare)
- Il progetto è stato recuperato dalla mia chat claude.ai (cartelle money_backstory/chat, code, miniature_video3, documenti_caricati; file README.md, MEMORIA-CANALE.md, VIDEO3-SEO.md).
- Video 3 ("59 1/2 Rule Retirement: 5 Changes That Cost Thousands (#4 Is a Trap)"): pacchetto SEO completo in money_backstory/VIDEO3-SEO.md. Tre miniature nello stile rosso/verde, una per titolo, in money_backstory/miniature_video3/. Video 4 e 5: stato non noto, non c'è una richiesta in sospeso.
- Ho visto le statistiche di un suo video, "5 Retirement Mistakes That Leave You Broke at 65", dopo 3 giorni: 610 impressioni, percentuale di clic 2,8%, 52 visualizzazioni, 56% da navigazione e 42% da video consigliati. L'intervallo normale della percentuale di clic è 2-10% secondo YouTube. 2,8% con così pochi dati dice poco, e le 52 visualizzazioni non tornano con 2,8% di 610: la percentuale vera è probabilmente più alta. Va ricontrollato dopo 1.500-2.000 impressioni e confrontato con i video 1 e 2.

COSE DA SAPERE / ERRORI GIÀ FATTI (da non ripetere)
- Il blocco 21 era sbagliato di circa 20 fotogrammi perché ho usato la somma dei miei clip invece della fine del blocco 20 nel mio screenshot. Gli altri blocchi (22-36) dipendono da differenze tra screenshot consecutivi e non sono toccati.
- Leggere il righello CapCut: il numero in alto a sinistra è il tempo (MM:SS / totale). Il righello ha etichette di fotogrammi ("Nf") e i puntini sono i fotogrammi dispari. La riga bianca è la posizione. A seconda dello zoom i fotogrammi sono larghi 66,5 px (zoom stretto) oppure 12,6 px a fotogramma (zoom largo). Con zoom largo le etichette sono ogni 10 fotogrammi.
- In Poppins il simbolo "✓" e la freccia "➜" non esistono (vengono quadratini): usare "OK" o disegnare la forma. Se sostituisci un testo nel codice, controlla con grep che sia cambiato (la sostituzione può fallire in silenzio con caratteri speciali).
- Non usare pkill -f con testo presente nel proprio comando: ha già ucciso la shell due volte.
- Non spendere crediti vidIQ senza chiedermi. Non cambiare formati già approvati (video 2 del Money Backstory). Niente segnaposto nei testi.
- Per risparmiare crediti: usare una chat nuova (questa è molto lunga) e rileggere sempre CLAUDE.md all'inizio.

COSA PUÒ SUCCEDERE ADESSO
- Caricamento del video lungo 1 (titolo, descrizione, tag, commento, playlist, schermata finale, miniatura).
- Prossimo video del Senior Advantage: serve prima l'argomento, il copione in blocchi, le fonti ufficiali, poi le slide più dettagliate e movimentate.
- Eventuale controllo dei capitoli sulla mia timeline, o una seconda miniatura per "Test e confronta".

## assistant - 2026-10-01T21:26:20.821444Z

Letti CLAUDE.md, README e MEMORIA-CANALE. Contesto chiaro.

Nota tecnica: la sessione parte sul ramo `claude/ecstatic-shannon-wl7kwf` (vuoto, solo i vecchi file). Il tuo lavoro è sul ramo `claude/money-backstory-project-bqq9ic`, che ho letto da remoto.

Cosa faccio adesso? Scegli:
1. Caricamento video lungo 1 (ti guido passo per passo)
2. Controllo capitoli sulla tua timeline
3. Seconda miniatura per "Test e confronta"
4. Prossimo video Senior Advantage (argomento + copione)

## human - 2026-10-01T21:29:25.790394Z

Cosa ti manda per avere tutto sul progetto di the senior advantage?

## assistant - 2026-10-01T21:29:34.107449Z

Niente. Tutto il progetto è già nel repo, sul ramo `claude/money-backstory-project-bqq9ic`.

Contiene:
- Copione, fonti, README e memoria del canale.
- Codice delle slide (`senior_advantage/code/`).
- Gli MP4 dei blocchi del video lungo 1 (95 file).
- Le 3 miniature, le anteprime e i riferimenti.

Cosa non è nel repo e puoi mandarmi, solo se serve:
- Gli screenshot della timeline, per controllare i capitoli.
- Le statistiche di YouTube Studio, per analizzare le prestazioni.

Per il prossimo video mi basta l'argomento.

## human - 2026-10-01T22:47:14.056890Z

Creiamo il quarto short per il canale the senior advantage che attiri attenzione e utile hook e tutto quello che serve informati se serve così la facciamo la. Migliore

## assistant - 2026-10-01T22:48:00.826134Z

Sto verificando i dati ufficiali per lo short 4 (bollette, LIHEAP). Ho finito. Costo: 0 crediti vidIQ.

**Dove va:** nella playlist degli aiuti, con lo short 3. Non va in "Senior Discounts". Non devi creare né cancellare niente.

**Fonti ufficiali verificate:**
- LIHEAP: gli aiuti coprono riscaldamento, raffrescamento ed emergenze. Il limite di reddito è il maggiore tra il 150% della soglia di povertà federale e il 60% del reddito mediano dello Stato. Gli Stati fissano il limite, quindi varia. Hanno priorità le famiglie con anziani, disabili o bambini piccoli. [LIHEAP Fact Sheet](https://acf.gov/ocs/fact-sheet/liheap-fact-sheet), [Eligibility](https://liheapch.acf.gov/delivery/eligibility-houseincome.htm)
- Numero NEAR: 1-866-674-6327, giorni feriali 9:00-19:00 (ora della costa Est). Sito: energyhelp.us. [NEAR](https://liheapch.acf.gov/referral.htm)
- Gancio: nell'anno fiscale 2021 circa il 12% delle famiglie con i requisiti ha ricevuto aiuto per il riscaldamento. È il dato più recente che ho trovato, quindi lo dico come "about one in eight". [Performance data](https://acf.gov/archive/ocs/grant-funding/liheap-data-performance-measurements)
- Non ho potuto aprire direttamente le pagine acf.gov (errori 403 e 503). I dati vengono dai risultati di ricerca sui siti ufficiali.

**Copione (una frase per clip, circa 36 s):**
1. About one in eight households that qualify gets help paying energy bills.
2. It's a federal program called LIHEAP.
3. It can help with heating, cooling, and emergency help in a crisis.
4. Homes with older adults are a priority group.
5. Income limits depend on your state.
6. Call 1-866-674-6327, weekdays, or go to energyhelp dot US.
7. Funding is limited, so apply early.
8. Follow for more help most seniors never claim.

**Titolo:** Help Paying Electric & Heating Bills for Seniors (LIHEAP)

**Descrizione:**
Most households that qualify never get help paying their energy bills. LIHEAP is a federal program that can help with heating, cooling and crisis costs, and homes with older adults are a priority group. Income limits depend on your state. Call 1-866-674-6327 (weekdays, 9am-7pm ET) or visit energyhelp.us.

Sources: acf.gov/ocs/programs/liheap · liheapch.acf.gov/referral.htm

Subscribe for more help most seniors never claim: https://www.youtube.com/@TheSeniorAdvantage?sub_confirmation=1

Rules, amounts and ages change and differ by location and plan. Always confirm with the official source before you rely on them. General information, not financial advice.

#seniorassistance #energyassistance #LIHEAP

**Tag:** LIHEAP, energy assistance for seniors, help paying electric bills, help paying heating bills, senior assistance programs, low income energy assistance, utility bill help seniors, LIHEAP application, home energy assistance, senior benefits, help with energy bills, energy assistance program

**Commento da fissare:** "Did you know LIHEAP existed? Tell me below 👇 Rules and limits vary by state, so call the number in the video to confirm."

**Impostazioni:** IA No, promozione No. Il disclaimer a voce non serve negli short.

Posso confermare il copione e passare alla voce CapCut? Poi mandami gli screenshot della timeline a fine di ogni frase e faccio le slide sulle tue durate.

## human - 2026-10-01T22:51:14.241216Z

Falle con le punteggiati realtà come se parlasse una persona vera con pause quando servono esclamazioni ecc

## assistant - 2026-10-01T22:51:22.665751Z

**Copione short 4, con pause e tono parlato** (incolla in CapCut così com'è):

1. Wait… only about one in eight households that qualify actually gets help with energy bills!
2. It's a federal program called LIHEAP.
3. It can help with heating… cooling… and even emergency help in a crisis!
4. And if there's an older adult at home? That household is a priority!
5. Income limits depend on your state, so check yours.
6. Call: one, eight-six-six, six-seven-four, six-three-two-seven. Weekdays. Or go to energyhelp dot U-S.
7. Funding is limited, so don't wait… apply early!
8. Follow for more help most seniors never claim.

**Note:**
- Nella frase 6 ho scritto il numero a cifre, così CapCut non legge "eight hundred sixty-six".
- Durata stimata: circa 40 secondi (circa 480 caratteri, più le pause dei "…").
- I fatti non sono cambiati: titolo, descrizione, tag e commento di prima restano validi.

Quando hai la voce, mandami gli screenshot della timeline a fine di ogni frase e faccio le slide sulle tue durate.

## human - 2026-10-01T23:03:19.893639Z

[5 immagini allegate]

## human - 2026-10-01T23:03:31.690543Z

[3 immagini allegate]

## assistant - 2026-10-01T23:03:40.617508Z

Letti i 5 screenshot. Ogni durata parte dalla fine del clip precedente.

| Frase | Fine (timeline) | Fotogrammi |
|---|---|---|
| 1 | 6 s 6 f | 186 |
| 2 | 8 s 24 f | 78 |
| 3 | 13 s 20 f | 146 |
| 4 | 18 s 9 f | 139 |
| 5 | 21 s 20 f | 101 |

In questi screenshot la riga bianca cade tra due fotogrammi, perché la fine della voce non coincide con un fotogramma intero. Ho arrotondato al più vicino, quindi può esserci 1 fotogramma di scarto.

La frase 5 ("Income limits depend on your state, so check yours.") corrisponde al testo che si vede nell'anteprima.

Mandami gli screenshot delle frasi 6, 7 e 8. Poi faccio le slide.

## assistant - 2026-10-01T23:06:58.842612Z

Sto controllando le slide dello short 4 con alcuni fotogrammi di prova, prima di renderizzare i clip.

## human - 2026-10-01T23:07:11.034453Z

[Image: original 2025x1440, displayed at 2000x1422. Multiply coordinates by 1.01 to map to original image.]

## assistant - 2026-10-01T23:07:13.074139Z

Le anteprime vanno bene. Renderizzo gli 8 clip.

## assistant - 2026-10-01T23:09:20.223434Z

Ho fatto gli 8 clip dello short 4 (1080x1920, uno per frase) e te li ho mandati. Costo: 0 crediti vidIQ.

Le durate dei clip coincidono con le tue, controllate con ffmpeg:

| Clip | Fotogrammi | Cosa si vede |
|---|---|---|
| 1 | 186 | 8 case, una si accende, "1 IN 8" |
| 2 | 78 | edificio federale, "LIHEAP" |
| 3 | 146 | fiamma, fiocco di neve e triangolo di emergenza |
| 4 | 139 | nonna alla finestra, tag "PRIORITY" |
| 5 | 101 | mappa con pin "$ / $$ / $$$", lente |
| 6 | 292 | cornetta, numero scritto a gruppi, giorni L-V, finestra energyhelp.us |
| 7 | 109 | misuratore del fondo che si svuota, sveglia, calendario "EARLY" |
| 8 | 94 | campanella, "FOLLOW", barra Subscribe |

- **Tempi dentro i clip lunghi:** nel clip 6 (e in parte nel 3) i momenti in cui compaiono le cifre, i giorni e il sito sono stimati dal testo. Il clip 6 dura 9,7 secondi e non ho una timeline interna. Se uno scatta fuori tempo rispetto alla voce, dimmi quale e lo sposto.
- **Dato sul numero:** nel clip 1 lo scrivo come "1 IN 8" (circa il 12% nell'anno fiscale 2021).
- **Ramo:** il codice (`senior_advantage/code/scenes4.py`) è sul ramo `claude/ecstatic-shannon-wl7kwf`, non su `claude/money-backstory-project-bqq9ic`. La sessione è configurata su quel ramo e non ho spinto su quello dei tuoi file. Se vuoi tutto sul ramo del progetto, dimmelo.

Prossimo passo: la miniatura dello short 4?

## assistant - 2026-10-01T23:09:25.870313Z

Il repo è pulito e tutto è già spinto. L'unica modifica rimasta era un file `.pyc` generato dall'esecuzione, e l'ho ripristinato.

## human - 2026-10-01T23:27:26.906960Z

Si fai ka. Mignatura attira curiosità

## assistant - 2026-10-01T23:28:06.591300Z

Sto salvando la miniatura e il codice, poi te la mando.

## assistant - 2026-10-01T23:28:15.377568Z

La copertina dello short 4 è qui sopra (1080x1920), costo 0 crediti.

Cosa mostra:
- **Curiosità:** 8 case, una sola accesa, e "1 IN 8 GETS THIS HELP".
- **Sticker:** "DO YOU QUALIFY?".
- **Riquadro in basso:** "HELP WITH ENERGY BILLS".
- **Fiamma e fiocco di neve:** riscaldamento e raffrescamento.

Non mi hai dato una frase tua, quindi ho scelto io questa. Se ne hai una in mente, dimmela e la cambio.

Caricala in Anteprima → Modifica dello Short. Il video va nella playlist degli aiuti, non in quella degli sconti.

## human - 2026-10-02T15:12:20.080811Z

Mandami titolo è tutto con seo parole chiavie tutto

## assistant - 2026-10-02T15:12:32.442263Z

Pacchetto completo dello short 4, da incollare così com'è.

**Dove va:** playlist "aiuti", con lo short 3. Non va nella playlist "Senior Discounts". Non devi creare né cancellare niente. Costo: 0 crediti vidIQ.

**Titolo (57 caratteri):**
Help Paying Electric & Heating Bills for Seniors (LIHEAP)

**Descrizione:**
```
Help paying electric and heating bills for seniors: LIHEAP is a federal program that can help with heating, cooling and crisis costs, and homes with older adults are a priority group. Only about 1 in 8 eligible households gets help.

Income limits depend on your state. Call 1-866-674-6327 (weekdays, 9am-7pm ET) or visit energyhelp.us to find your local office. Funding is limited, so apply early.

Sources:
https://acf.gov/ocs/programs/liheap
https://liheapch.acf.gov/referral.htm
https://acf.gov/ocs/fact-sheet/liheap-fact-sheet

Subscribe for more help most seniors never claim: https://www.youtube.com/@TheSeniorAdvantage?sub_confirmation=1

Rules, amounts and ages change and differ by location and plan. Always confirm with the official source before you rely on them. General information, not financial advice.

#Shorts #LIHEAP #seniorassistance #energyassistance
```

**Tag (451 caratteri):**
```
LIHEAP, energy assistance for seniors, help paying electric bills, help paying heating bills, senior assistance programs, low income energy assistance, utility bill help seniors, LIHEAP application, home energy assistance, senior benefits, help with energy bills, energy assistance program, senior utility assistance, how to apply for LIHEAP, heating assistance for seniors, electric bill assistance
```

**Commento da fissare:**
Did you know LIHEAP existed? Tell me below 👇 Rules and limits vary by state, so call the number in the video to confirm.

**Impostazioni:**
- Utilizzo dell'IA: No.
- Promozione a pagamento: No.
- Miniatura: la copertina che ti ho mandato.
- Il disclaimer a voce non serve negli short.

**Dati vidIQ già salvati:**
- "senior assistance programs": 4.229 ricerche al mese, concorrenza 21.
- "low income relief": 24.886 ricerche al mese.
- Non ho speso crediti.

Dopo la pubblicazione: lo short 5 è da decidere. Dimmi l'argomento oppure scelgo io dalla lista dei temi del canale.

## human - 2026-10-02T15:19:08.162791Z

Video correlati cosa ci metto?

## assistant - 2026-10-02T15:19:16.676140Z

Metti il video lungo 1: "Senior Discounts Start at 55, Not 65: 12 Hidden Places (Most Never Ask)".

Motivo: ti servono le ore di visualizzazione, e un video lungo le fa. Lo spettatore dello short sugli aiuti ha lo stesso interesse (risparmiare da senior).

Se il video lungo non è ancora pubblicato, metti lo short 3 (pasti a domicilio, Meals on Wheels). Poi aggiungi il lungo appena è online.

Il campo si trova in YouTube Studio, nei dettagli dello short, alla voce "Video correlato".

## human - 2026-10-02T15:22:30.928338Z

Quindi tutti gli short gli indirizzo al video lungo?

## assistant - 2026-10-02T15:22:36.663356Z

No. Ogni short va collegato al video più vicino al suo tema.

- **Short 1 e 2 (sconti):** al video lungo 1, che ha lo stesso tema.
- **Short 3 e 4 (aiuti):** per ora al video lungo 1, perché non hai ancora un video lungo sugli aiuti. Il collegamento è meno preciso. Se preferisci, collega lo short 4 allo short 3 e viceversa.
- **Quando avrai un video lungo sugli aiuti:** sposta i collegamenti di short 3 e 4 su quello.

Il video correlato si può cambiare quando vuoi, quindi non è una scelta definitiva.

## human - 2026-10-03T18:10:07.416322Z

Dimmi cosa scrivere e cosa mandare alla chat nuova per sapere tutto del progetto sia tutte le robe scritte qua in questa chiat che nelle altre di questo progetto the senior advantage

## assistant - 2026-10-03T18:10:38.700509Z

**Cosa mandare:** solo il testo qui sotto, nella chat nuova. Non servono file: il lavoro è nel repo e la chat nuova non vede le altre chat. Il testo dice dove leggere tutto.

**Testo da incollare:**

```
CONTESTO
Lavoro con te sul mio progetto YouTube. Repo GitHub: kovacevstevo1993-gif/Tr, cartella /home/user/Tr.
RAMO DA USARE: claude/ecstatic-shannon-wl7kwf. Contiene tutto il lavoro del ramo claude/money-backstory-project-bqq9ic più il codice dello short 4. Fai git fetch e usa quello.
Leggi per prima CLAUDE.md (regole permanenti), poi senior_advantage/README.md e senior_advantage/MEMORIA-CANALE.md. Le chat vecchie esportate sono in senior_advantage/chat/ (arrivano al 29/09).

DUE CANALI SEPARATI, MAI MESCOLARE
1) The Senior Advantage (@TheSeniorAdvantage), cartella senior_advantage/. Sconti, benefici e aiuti per over 60 USA. Slide verde bosco e avorio (oro e rosso accenti). Short 1080x1920, lunghi 1920x1080. Circa 1.700 iscritti americani.
2) The Money Backstory (@TheMoneyBackstoryUSA), cartella money_backstory/. Pensione USA over 50. Slide blu navy e oro. Lo ignori in questa chat.

COME LAVORO
- Risposte corte. Niente scuse né "hai ragione". Una cosa alla volta. Verifica prima di dare un'indicazione.
- Eseguire SOLO quello che dico. Non rifare quello che ho già montato. Non proporre di fermarmi.
- Non mettere file o cartelle che non ho chiesto. I testi li scrivi qui in chat.
- Mai spendere crediti vidIQ senza chiedermi (ne restano 5, si rinnovano il 29/10/2026).
- Titolo, descrizione e tag già completi da incollare, con Subscribe e disclaimer. Niente segnaposto.
- Dirmi PRIMA dove va ogni nuovo video (playlist, cosa creare o cancellare).
- Durate dei clip: dai miei screenshot della timeline CapCut, sempre dalla fine del clip precedente. La riga bianca può cadere tra due fotogrammi: si arrotonda al più vicino. Il numero in alto a sinistra è il tempo (MM:SS / totale).
- Slide e grafica le fai tu col codice (gratis). Dai prossimi video: più movimentate, più dettagliate, più oggetti disegnati.
- Disclaimer solo nei video lunghi, alla fine (slide finale + frase a voce), più descrizione e commento fissato. Non negli short.
- Fatti solo da fonti ufficiali (siti governativi/aziende). Niente promesse di guadagno.
- Poppins non ha "✓" e "➜". Non usare pkill -f. Fai git checkout sui .pyc modificati prima di committare.
- Il repo va committato e spinto sul ramo ecstatic-shannon.

CODICE (senior_advantage/code/)
Motore engine.py + eng2.py. Short: scenes2.py (short 2), scenes3.py (short 3), scenes4.py (short 4, uso: S4_OUT=cartella python3 scenes4.py <clip>). Copertine: cover*.py, cover4.py. Video lungo: long1_*.py.

STATO
VIDEO LUNGO 1 (36 blocchi, 11:01), montato da me: "Senior Discounts Start at 55, Not 65: 12 Hidden Places (Most Never Ask)" (vidIQ 94/100). Copione, fonti, clip, pacchetto SEO e 3 miniature (A, B, C) sono pronti (README, COPIONE-VIDEO-LUNGO-1.md, FONTI-VIDEO-LUNGO-1.md, video_lungo_1/, miniature/). Playlist: "Senior Discounts", come primo video. Da controllare: orari dei capitoli sulla mia timeline.

SHORT PUBBLICATI
1 (sconto da 55 anni), 2 (4 posti con sconto) in playlist "Senior Discounts". 3 (Meals on Wheels, Eldercare Locator 1-800-677-1116) in playlist "aiuti".

SHORT 4 (bollette, LIHEAP), fatto il 03/10/2026
- Playlist: "aiuti" (con lo short 3).
- Fonti: acf.gov/ocs/programs/liheap, liheapch.acf.gov/referral.htm, acf.gov/ocs/fact-sheet/liheap-fact-sheet. Numero NEAR 1-866-674-6327, giorni feriali 9:00-19:00 ET, energyhelp.us. Limite: il maggiore tra 150% soglia di povertà federale e 60% reddito mediano dello Stato (varia per Stato). Priorità: famiglie con anziani. Dato "1 su 8": circa 12% delle famiglie idonee nell'anno fiscale 2021.
- Titolo: Help Paying Electric & Heating Bills for Seniors (LIHEAP)
- Copione (8 frasi): 1 Wait… only about one in eight households that qualify actually gets help with energy bills! 2 It's a federal program called LIHEAP. 3 It can help with heating… cooling… and even emergency help in a crisis! 4 And if there's an older adult at home? That household is a priority! 5 Income limits depend on your state, so check yours. 6 Call: one, eight-six-six, six-seven-four, six-three-two-seven. Weekdays. Or go to energyhelp dot U-S. 7 Funding is limited, so don't wait… apply early! 8 Follow for more help most seniors never claim.
- Durate in fotogrammi (dai miei screenshot): 186, 78, 146, 139, 101, 292, 109, 94 (totale 1145 = 38,2 s).
- 8 clip slide e copertina già fatti e mandati a me. Voce già fatta da me.
- Tag: LIHEAP, energy assistance for seniors, help paying electric bills, help paying heating bills, senior assistance programs, low income energy assistance, utility bill help seniors, LIHEAP application, home energy assistance, senior benefits, help with energy bills, energy assistance program, senior utility assistance, how to apply for LIHEAP, heating assistance for seniors, electric bill assistance
- Descrizione: prima riga "Help paying electric and heating bills for seniors: LIHEAP is a federal program…", numero e sito, fonti, riga Subscribe (https://www.youtube.com/@TheSeniorAdvantage?sub_confirmation=1), disclaimer, #Shorts #LIHEAP #seniorassistance #energyassistance.
- Commento fisso: "Did you know LIHEAP existed? Tell me below 👇 Rules and limits vary by state, so call the number in the video to confirm."
- Video correlato: il video lungo 1 (finché non esiste un lungo sugli aiuti).
- Impostazioni: IA No, promozione No.

DATI vidIQ (US)
"senior discounts" 12.828/mese (conc. 26,3). "senior discount" 9.826. "senior citizen discounts" 4.821. "hidden senior discounts" 4.045. "senior savings" 3.786. "senior assistance programs" 4.229 (conc. 21). "low income relief" 24.886. "senior meals" 7.069.

COSA PUÒ SUCCEDERE ADESSO
- Caricare il video lungo 1 e/o lo short 4.
- Controllo capitoli sulla mia timeline, seconda miniatura per "Test e confronta".
- Short 5 (argomento da decidere) o un video lungo sugli aiuti.
- Monetizzazione: dal 1/2/2027 servono 8.000 ore o 20 milioni di view Short (oggi 1.000 iscritti + 4.000 ore): servono i video lunghi.
```

Prima di incollare: se hai già pubblicato qualcosa (video lungo 1 o short 4), aggiungi in fondo una riga con cosa è online, così la chat nuova parte aggiornata.

