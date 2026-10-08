# REGOLE FISSE - canale "Conti in Pensione" (da rileggere a inizio di ogni sessione)

## Slide, clip, video e short: CONTROLLO OBBLIGATORIO su TUTTI i fotogrammi
(regola dell'utente, 03/10/2026: "devi controllare le lettere delle slide, ogni video e ogni short, non a spezzoni")
1. Dopo ogni render: `python3 conti_in_pensione/qa/qa_slide.py <file.html> <indice_blocco> <n_frame>` deve dire "QA OK".
   Controlla su ogni fotogramma: testo che esce dal fotogramma, testo tagliato o fuori dal riquadro/pillola, testi sovrapposti, animazioni non finite prima della dissolvenza.
2. In più: guardare a occhio fotogrammi ogni 0,5 secondi del FILE FINITO (`ffmpeg -vf fps=2,scale=480:-1,tile=4x3`) e leggere ogni scritta.
3. Ogni slide deve avere il tempo di FINIRE: tutti gli elementi completi almeno 0,5 s prima della dissolvenza di fine scena, poi fermi.
4. Controllare le durate dei file con ffprobe (fotogrammi = durata della timeline CapCut a 30 fps).
5. Non dire "controllato" se il controllo è stato a campione. Se il controllo non passa, correggere e rifare finché passa.

## Testi e dati
- Testi (copioni, titoli, descrizioni, tag) vanno scritti DIRETTAMENTE IN CHAT, interi, pronti da copiare. La cartella è solo copia di riserva.
- Copioni dei video lunghi: blocchi da circa 15 secondi (max ~250 caratteri), video lungo sopra i 10 minuti (velocità reale voce ~16 caratteri al secondo).
- Voce: frasi punteggiate come parlato, tutti i numeri in lettere, "Inps", "Mai Inps", "Ape", "inps punto it".
- Notizie e dati li cerca e li verifica Claude su fonti ufficiali. Le proposte vanno dette sempre come proposte.
- Risposte corte, una cosa alla volta.
- Slide: stile verde acqua, titoletto in alto, grafica al centro, didascalia nel riquadro in basso; fatte con il codice, dettagliate, con oggetti.
- Descrizione di ogni video: intera, con Iscriviti, disclaimer e hashtag (la descrizione predefinita di YouTube è vuota). Hashtag 5-12, mai oltre 15. Tag sotto i 500 caratteri.
- vidIQ: spendere crediti solo se l'utente lo chiede.
- Le altre regole sono in `07-KIT-COMPLETO/00-LEGGIMI-PRIMA.md` (nel KIT-1).

## Velocità (regola dell'utente 04/10/2026: "usa la testa, deve essere veloce")
- Il collo di bottiglia è il render (uno screenshot per fotogramma). Renderizzare SEMPRE tutti i blocchi in parallelo, 4 alla volta (la macchina ha 4 processori):
  `printf '%s\n' 1 2 3 ... | xargs -P 4 -I{} python3 render.py {} video`
- Fare il controllo QA e l'anteprima a fogli PRIMA del render, così non si rifà niente. Mai renderizzare un blocco alla volta.
- Costruire più blocchi per volta, non uno per messaggio. Rispondere all'utente appena i file sono pronti.

## REGOLA N.1 (utente, 04/10/2026): ESEGUIRE SOLO GLI ORDINI
- Fare SOLO quello che l'utente ordina. Mai prendere decisioni proprie su qualità, semplificazioni, scorciatoie o cambi di metodo.
- Mai abbassare la qualità per andare più veloce: la velocità si ottiene con render più rapido, non con slide più povere.
- Mai rifare da zero il lavoro già fatto: si riusa e si MIGLIORA quello che c'è (aggiungere dettaglio sopra).
- Se serve una scelta, chiedere PRIMA, non dopo. Stesso livello di dettaglio per TUTTI i blocchi di un video (nessun video mezzo semplice e mezzo dettagliato).

## REGOLA N.2 (utente, 04/10/2026): LAVORARE A FONDO, SENZA SCUSE
- Se un lavoro è venuto male, si RIFÀ per intero e bene. Non scaricare sui problemi tecnici, non fare le cose a metà, non dire "fatto" se non è all'altezza.
- Niente giustificazioni lunghe: lavorare, consegnare completo.

## REGOLA N.3 (utente, 04/10/2026): NOMI DEI FILE DIVERSI PER OGNI VIDEO
- I file delle slide/clip hanno sempre lo stesso nome (blocco1.mp4, blocco2.mp4...) e in CapCut si confondono tra un video e l'altro. Rinominarli per OGNI video e short con un prefisso che identifica il video.
- Formato: `V3-blocco01.mp4`, `V3-blocco02.mp4`... (V3 = video lungo 3; per gli short: `S4-blocco01.mp4`, ...). Numeri a due cifre, così restano in ordine.
- NON farlo adesso per il video 2 (restano blocco1.mp4...blocco57.mp4). Si applica dal PROSSIMO video lungo e dai prossimi short.
- (Errore di Claude: all'inizio aveva capito "cambiare il modello grafico delle slide": NON era questo. La grafica non cambia per questa regola.)

## REGOLA N.4 (utente, 04/10/2026): SALVARE SEMPRE TUTTO QUELLO CHE DICE L'UTENTE
- Ogni istruzione, preferenza o correzione dell'utente va scritta SUBITO in questo file (nel repo, committata e pushata), senza aspettare che lo chieda.
- A inizio di ogni nuova chat: leggere questo file per primo.

## ELENCO ISTRUZIONI DELL'UTENTE (sessione 02-04/10/2026)
- Notizie e dati: li cerca e verifica Claude su fonti ufficiali; le proposte si dicono sempre come proposte.
- Risposte corte, una cosa alla volta.
- Testi (copioni, titoli, descrizioni, tag) sempre scritti in chat, interi, pronti da copiare (non solo nella cartella).
- Copioni video lunghi: blocchi da ~15 secondi, video sopra i 10 minuti, hook che trattiene, intrattenimento fino all'ultimo secondo, cercare su vidIQ cosa è cercato e cosa va virale (spendere crediti vidIQ solo se serve alla richiesta).
- Voce: frasi punteggiate come parlato, numeri in lettere, "Inps", "Mai Inps", "inps punto it".
- L'utente registra la voce in CapCut e manda lo screenshot di fine blocco; le durate partono dalla fine del blocco precedente (fotogrammi a 30 fps).
- Slide: fatte col codice, dettagliate, con oggetti, verde acqua; devono avere il tempo di FINIRE prima della dissolvenza; controllo OBBLIGATORIO di tutte le lettere su TUTTI i fotogrammi, mai a campione.
- Qualità mai abbassata (neanche per velocità); non rifare da zero ma migliorare; render in parallelo.
- Descrizione di ogni video: intera con "Iscriviti", disclaimer e hashtag (descrizione predefinita di YouTube vuota); hashtag 5-12 (max 15); tag sotto 500 caratteri; commento da fissare (dopo la pubblicazione, mai su video programmato).
- Short: pubblicato a mano (circa 7:30) il giorno dopo il video lungo, rimanda al video lungo ("video correlato" + commento fissato SENZA link: negli short i link non funzionano); miniatura che attira il click.
- Miniature: frase che ha in mente l'utente; attira click.
- Nomi dei file DIVERSI per ogni video (es. V3-blocco01.mp4), dal prossimo video in poi; il video 2 resta com'è.
- Kit completo per cambiare chat: KIT-1 (testi, chat, regole) + zip dei video; messaggio di ripartenza in 07-KIT-COMPLETO/00-LEGGIMI-PRIMA.md; leggere anche REGOLE-FISSE.md.
- Eseguire SOLO gli ordini, nessuna scelta propria, lavorare a fondo senza scuse.

## REGOLA N.5 (utente, 04/10/2026): DAL PROSSIMO VIDEO, SLIDE PIÙ LENTE E CHIARE, TUTTO MIGLIORATO
- Feedback sul video 2: era TROPPO VELOCE, quasi tutto non si riusciva a capire bene; le slide in movimento NON erano brutte, erano VELOCI (il problema è la velocità, non l'aspetto).
- Dal PROSSIMO video lungo (e dai prossimi short): fare MEGLIO, in modo che si capisca bene. Migliorare TUTTO.
- Non cambiare da zero: MIGLIORARE quello che c'è (regola n.1). Salvare sempre (regola n.4).
- Da applicare: ritmo più lento (più tempo di lettura per ogni slide, meno cose per slide), animazioni meno veloci (la grafica in movimento RESTA: va lasciato il movimento, ma deve FINIRE BENE, cioè completarsi con calma e restare ferma il tempo di leggere), testi grandi e leggibili, ogni elemento fermo e completo con tempo per essere letto. Se serve una scelta di metodo, chiedere PRIMA.
- Il video 2 resta com'è (già montato).
- (utente, 04/10/2026) Per i prossimi video: MIGLIORARE e basta (il video, le slide e il modo di far capire meglio), più DETTAGLIATO. Niente altri cambiamenti: si migliora quello che c'è, senza stravolgere.
- (utente, 04/10/2026) Nel video 2 le slide NON FINIVANO BENE (animazioni non completate in tempo). Dal prossimo video va risolto: ogni slide deve completare tutto il movimento e restare ferma e leggibile per un tempo sufficiente PRIMA della dissolvenza, controllando TUTTI i fotogrammi (regole di controllo in cima a questo file).

## ISTRUZIONI UTENTE (05/10/2026)
- Gli short 1, 2 e 3 sono GIÀ PUBBLICATI. Lo short da fare adesso è lo SHORT 4 = teaser del video lungo 2 (nomi file S4-blocco01.mp4...). Hook super interessante che tiene attaccati fino alla fine e convince a guardare il video lungo completo; con didascalia (descrizione).
- Nei commenti e nelle descrizioni degli short i link NON funzionano: negli short non dire "il link è nel commento"; dire "tocca il video correlato" (funzione "Video correlato" di YouTube Studio).

## REGOLA N.6 (utente, 05/10/2026): DIDASCALIE (TESTO NEL VIDEO) SEPARATE, UNA PER BLOCCO, OGNUNA IN UN SUO RIQUADRO DA COPIARE
- "Didascalia" (o "didascalia/voce") = il TESTO CHE VA NEL VIDEO (letto dalla voce / scritto sul video), NON la descrizione YouTube.
- Come mandarla: ogni didascalia SEPARATA, una per blocco/clip, ciascuna nel suo riquadro (```), numerata, pronta da copiare una alla volta (come nel copione del video 2). NON in un unico testo continuo (provato il 05/10: l'utente ha risposto "Separate").
- Descrizione, titolo, tag e commento da fissare: ognuno in un RIQUADRO SUO, separato, da copiare uno alla volta (mai tutto in un unico riquadro). Il titolo non contiene hashtag.
- Da applicare in ogni chat, per ogni video e short, senza che l'utente lo ripeta.

## ISTRUZIONI UTENTE (05/10/2026, short 4)
- Short 4: l'utente ha registrato la voce e mandato 6 screenshot di fine blocco. Le clip vanno fatte "migliorate rispetto agli altri, meglio e più dettagliate" e "deve capirsi benissimo le slide" (regola n.5: più lente, movimento che finisce bene, ferme e leggibili prima della fine).

## REGOLA N.7 (utente, 05/10/2026): IL TESTO CHE L'UTENTE METTE IN CAPCUT E' SOLO UN SEGNAPOSTO, LO TOGLIE LUI; LA DIDASCALIA STA NELLA SLIDE
- Frase dell'utente: "Il mio testo su CapCut lo tolgo io. Dove hai mai visto che metto io le didascalie nel video?"
- Il testo bianco che l'utente scrive in CapCut mentre registra la voce serve solo per segnare i blocchi: lo cancella. NON è la didascalia del video e NON va evitato nelle clip.
- La didascalia visibile sta DENTRO la slide (titoletto in alto, grafica al centro, didascalia nel riquadro in basso), come nei video 1 e 2. Le clip dello short 4 con la didascalia in basso (commit cad4b42) sono quelle GIUSTE.
- (Errore di Claude del 05/10: aveva tolto la didascalia dalle clip e rifatto tutto: sbagliato, ripristinato.)

## ISTRUZIONI UTENTE (05/10/2026, tag e miniatura short 4)
- I TAG vanno riempiti fino a circa 500 caratteri (sotto il limite), non a metà: short 4 = 491 caratteri.
- Miniatura dello short 4: deve attirare il click "per forza": `11-short-4-teaser-video-lungo-2/miniatura/miniatura-short4.png` (1080x1920).

## ISTRUZIONI UTENTE (06/10/2026, video lungo 3)
- Video lungo 3 = RIVALUTAZIONE 2027 (scelto dall'utente). Prefisso file: V3-blocco01.mp4...
- Fare ricerche su vidIQ su TUTTO (utente le ha ordinate: crediti ok): come lavorano gli altri su argomenti simili, come sono strutturati, video virali della nicchia pensioni, per far diventare virale anche il nostro.
- Il video deve essere più PROFESSIONALE, più CURIOSO e spiegato BENISSIMO, sia con le slide sia con la voce.
- (utente, 06/10/2026) Dopo le ricerche sugli altri canali/vidIQ, deve dire CLAUDE se il copione va bene e correggerlo da solo in base alla ricerca: NON chiedere all'utente "va bene?". L'utente ha fatto fare le ricerche apposta. Il copione va confrontato con i video virali: numeri/risposta subito, poi spiegazione.
- (utente, 06/10/2026) Le chat non vanno riempite inutilmente: risposte corte; quando la chat è piena si passa a una nuova con kit e messaggio di ripartenza.

## REGOLA N.8 (utente, 06/10/2026): OGNI CHAT NUOVA DEVE SAPERE GIA' TUTTO DEL PROGETTO, DALLA A ALLA Z
- Se un file/kit/chat non e' tra gli allegati, trovarlo DA SOLI (rami del repo `git fetch` + `git ls-tree`, tool list_sessions/list_events) e leggerlo; mai dire "non l'ho ricevuto" e aspettare. L'utente non deve rimandare niente.
- Dal 06/10/2026 TUTTO il progetto sta in questo ramo (`claude/trusting-mendel-d1bg54`, cartella conti_in_pensione/): cartelle 00-12 (canale, short 1-4, video lungo 1-3, kit, sorgenti, qa), chat intere in `07-KIT-COMPLETO/chat/chat-completa.md` (chat 0), `10-KIT-COMPLETO-V2/chat/` (chat 1 e 2), `12-KIT-05-10/chat-sessione-3-completa.md`, `chat/chat-sessione-4-completa.md`; stato in `12-KIT-05-10/00-LEGGIMI-PRIMA.md` + `STATO-06-10-2026.md`. Il vecchio branch con tutto: youthful-einstein (00-07), wizardly-galileo (06,08,09,10), new-session-79n9mt (09,11,12-KIT), eager-davinci (video 3).
- Quando i blocchi del copione sono richiesti: rimandarli SEMPRE in chat, numerati, ognuno nel suo riquadro.

## REGOLA N.9 (utente, 07/10/2026, video 3): SLIDE SINCRONIZZATE ALLA VOCE, CAPIBILI, CONTROLLO TOTALE
- Blocchi 1-5 del video 3 (V3-blocco01..05.mp4): l'utente dice "le lasciamo cosi'", NON rifarli.
- Le altre clip (dal blocco 6) devono avere i tempi calcolati sulla VELOCITA' DELLA VOCE: ogni elemento compare quando la voce dice quella parola/frase (velocita' reale ~16-17 caratteri al secondo, ricavata dal testo del blocco e dalla durata dello screenshot, con pause alle virgole e ai punti). Mai slide troppo veloci: ogni cosa ferma e leggibile mentre la voce ne parla, e tutto FINITO prima che la voce passi alla frase dopo.
- Le slide devono SPIEGARE (calcoli passo passo, schemi, esempi che si capiscono), non solo oggetti che volano qua e la'. Migliorare, non semplificare.
- Gli screenshot arrivano 5 alla volta fino al blocco 30: si costruiscono TUTTI i blocchi insieme (render in parallelo), controllo COMPLETO su tutti i fotogrammi (QA automatico + guardare, non solo ogni mezzo secondo). Lavorare da professionista, niente a meta'.

## ISTRUZIONI UTENTE (07/10/2026, video 3 - tempi dei blocchi)
- Gli screenshot danno le durate: ogni blocco parte dalla fine del precedente. Se l'utente corregge lo screenshot di un blocco (es. blocco 40: fine 09:40+1f, 500 fotogrammi), cambia SOLO la durata di quel blocco; le durate degli altri restano quelle dei loro screenshot (l'utente sposta i blocchi sulla timeline). Il blocco 41 resta di 417 fotogrammi.
- Il segno sotto la riga bianca del cursore e' il fotogramma; se la riga e' tra due segni si arrotonda per eccesso.

## ISTRUZIONI UTENTE (07/10/2026, short 5)
- Video lungo 3 PUBBLICATO (07/10: 747 visualizzazioni in poche ore, e' "esploso" quella mattina; video 1: 314, video 2: 34). Tutto il resto e' pubblicato.
- Appena un video/short e' finito, l'utente lo PROGRAMMA subito: non dire "da pubblicare il giorno dopo", pacchetto pronto subito dopo le clip.
- SHORT 5 = teaser del video lungo 3 (nomi file S5-blocco01.mp4...). Obiettivo: curiosita' che porta nel video lungo, iscrizione e mi piace (chiusura: "tocca il video correlato, guardalo, iscriviti e metti mi piace"). "Video correlato" = video lungo 3. Gancio diverso dagli altri short. Informarsi prima (dati pubblici YouTube gratis con curl, niente crediti vidIQ).
- (07/10/2026) Short 5: 6 clip S5-blocco01..06.mp4 fatte e controllate (QA su tutti i fotogrammi OK, 1080x1920, 30 fps, 1774 fotogrammi = 59,1 s). Cartella 13-short-5-teaser-video-lungo-3 (clip, sorgenti, DURATE.txt, copione-blocchi.txt). Da fare: miniatura e pacchetto.
- (07/10/2026) Le clip si mandano come FILE MP4 SINGOLI (S5-blocco01.mp4...), MAI in uno zip. Errore di Claude sullo short 5: mandato uno zip; l'utente non l'ha accettato.

## REGOLA N.10 (utente, 07/10/2026): RILEGGERE REGOLE-FISSE.md SEMPRE, AD OGNI MESSAGGIO
- Non "dalla prossima consegna": ad OGNI messaggio dell'utente, PRIMA di fare o rispondere qualsiasi cosa, rileggere REGOLE-FISSE.md (e CLAUDE.md) e applicarlo. Sempre, senza eccezioni.

## OSSERVAZIONE UTENTE (07/10/2026, video 3 - visualizzazione media)
- Video 3: va forte ma la visualizzazione media e' 2:05 su 12:54. Ipotesi dell'utente: "diciamo subito tutto e se ne vanno". Controllo: 2:05 cade a fine capitolo "Il conto subito" (1:10-2:03); chi ha meno di ~2.450 euro ha la risposta li' e se ne va. Prima ci sono 70 s di promesse (blocchi 2-5) senza numeri.
- PROPOSTA (non ancora decisa dall'utente) per i prossimi video: intro breve (~20 s), niente elenco di promesse, risposta tenuta per dopo con "cerchi aperti" (caso sorprendente da 3.000/4.000 euro prima, casi semplici da 1.000/1.500 piu' avanti, cifra finale a fine video). Da verificare con il grafico di fidelizzazione di YouTube Studio (da chiedere all'utente).

## ISTRUZIONI UTENTE (07/10/2026, video lungo 4)
- Video lungo 4: l'utente ha ordinato di CONTROLLARE e scegliere Claude l'argomento migliore ("scegli tu il migliore"). Scelto da Claude sui dati vidIQ: AUMENTO PENSIONI INVALIDITA' 2027 (pensioni invalidita' 4.399/mese conc. 28; aumento pensioni invalidita' 5.415/mese conc. 33; precedente Mr LUL 440k). Reversibilita' scartata (3.411/mese, conc. 39).
- Non chiedere all'utente di scegliere tra due opzioni dopo una ricerca: scegliere e dirlo. Crediti vidIQ: ogni ricerca keyword costa 5 crediti; ora 0 (rinnovo 25/10).
- Struttura del video 4 (vedi 12-.../analisi-fidelizzazione-07-10.md): 6-8 minuti, gancio 20 s con chicca finale, cerchi aperti, tesi forte, teaser finale. L'utente: "proviamo a farne uno cosi', poi vediamo come va".

## REGOLA N.11 (utente, 07/10/2026): NIENTE SEMAFORI NELLE SLIDE
- Dal PROSSIMO video (video lungo 4 in poi) non usare piu' i semafori (luci verde/giallo/rosso) nelle slide: "non ha senso e sembra per bambini". Usare altri elementi grafici seri (schede, tabelle, importi, calcoli, timbri, frecce). Valido anche per gli short.

## REGOLA N.12 (utente, 07/10/2026): PIU' PROFESSIONALE MA SEMPRE COERENTE CON I VIDEO VECCHI (NON STRAVOLGERE)
- Lo stile resta quello dei video vecchi (verde acqua, titoletto in alto, grafica al centro, didascalia nel riquadro in basso, stessi colori e stessa impostazione). NON stravolgere niente: si migliora e basta (regola n.1 e n.5).
- Cambia SOLO questo: togliere gli elementi che sembrano da bambini (semafori e simili) e tenere un tono serio per adulti. Il resto della grafica resta coerente con short 1-5 e video lungo 1-3.
- I video gia' fatti (short 1-5, video lungo 1-3) "vanno bene cosi'": non rifarli.
- Vale dal video lungo 4 (V4-blocco01.mp4...) in poi.

## REGOLA N.13 (utente, 07/10/2026): UNA DOMANDA = SOLO UNA RISPOSTA, MAI MODIFICHE
- Se l'utente fa una DOMANDA (es. "45 centesimi incuriosisce?", "va bene cosi'?", "c'entra col canale?"), si risponde SOLO alla domanda. Non si riscrive, non si cambia, non si salva niente di nuovo nel lavoro. Si cambia solo se l'utente ORDINA di cambiare. (Errore del 07/10: dopo la domanda sul blocco 1 del video 4 ho riscritto il blocco senza ordine; ripristinato.)

## REGOLA N.14 (utente, 07/10/2026): OGNI ELEMENTO SULLA PAROLA ESATTA DELLA VOCE
- L'utente: "non riesci a calcolare parola per parola e fare le slide nel momento giusto? Perche' devo ripeterlo ogni video?". Le slide devono comparire esattamente sulla parola che la voce dice.
- Il motore stima i tempi dal numero di caratteri (approssimato): NON basta. Per i tempi esatti serve l'AUDIO della voce: trascrivere/allineare l'audio parola per parola (vosk con modello italiano, scaricabile; whisper) e usare i tempi veri al posto della stima. Chiedere all'utente l'audio della voce (una volta, per tutto il video) invece di stimare.
- Video 4: blocchi 1-5 consegnati con tempi stimati (da rifare con l'audio); blocchi 6-15 costruiti ma NON ancora renderizzati, in attesa dell'audio.
- (07/10/2026) Errore di Claude: ho ri-renderizzato anche i blocchi 1-5 del video 4 senza ordine. Regola: i blocchi gia' consegnati NON si rifanno e NON si rimandano se l'utente non lo ordina. Restano validi i V4-blocco01..05.mp4 gia' consegnati (cartella clip/); dei nuovi render si consegnano solo i blocchi dal 6 in poi.

## REGOLA N.15 (utente, 07/10/2026): SLIDE CAPIBILI: TUTTO FINITO ALL'80 % DELLA SLIDE, ANIMAZIONI NON VELOCI
- L'utente (detto piu' di 10 volte): "le slide sono troppo veloci, devono essere capibili, e non finiscono all'80 % prima di finire la slide, cosi' si leggono".
- REGOLA: in ogni slide (scena) tutti gli elementi devono essere COMPLETI e fermi entro l'80 % della durata della slide; il restante 20 % (almeno) resta tutto fermo per leggere. Se la voce arriva tardi su una parola, l'elemento compare un po' PRIMA ma sempre entro l'80 %.
- Animazioni di comparsa lente (0,9 s, non 0,5 s). Dal video 4 il motore (b-sync.js, mkBlk) comprime i tempi di comparsa per rispettare l'80 %.
- Vale dal PROSSIMO video (video 5 in poi). Il video 4 (blocchi 1-30) resta come e' (l'utente: "queste vanno bene"): NON rifare i blocchi 1-15, i blocchi 16-30 si fanno come i precedenti. Il motore con l'80 % e' salvato in 14-video-lungo-4-invalidita-2027/sorgenti/b-sync-80.js (da usare nel video 5 al posto di b-sync.js).

## STATO 07-08/10/2026 - VIDEO LUNGO 4 FINITO (per la chat nuova)
- Video 4 (invalidita' 2027, cartella 14-video-lungo-4-invalidita-2027): 30 clip V4-blocco01..30.mp4 fatte, controllate e consegnate; l'utente le ha montate. Pacchetto in 14-.../pacchetto.txt (titolo, descrizione con capitoli, tag 478 caratteri, commento da fissare, impostazioni): consegnato in chat, tutto in riquadri.
- Titolo: "Invalidita' 2027: quanto aumenta DAVVERO? Importi e 3 trappole". NIENTE "45 centesimi" in titolo, descrizione e miniature (l'utente: "a chi interessano 45 centesimi?"). Il 45 centesimi resta solo dentro il video (blocchi 1 e 20-25).
- Miniature video 4: 3 (A, B, C) in 14-.../miniatura/, nello STILE DEI VIDEO PUBBLICATI (video 1-3: sfondo verde acqua a raggi, numeri giganti con contorno scuro, palline rosso/verde con VS, striscia bianca con bordo giallo in basso, tag rosso ATTENZIONE, scheda/tabella verde). NON usare stile dei concorrenti (fasce blu, strisce gialle, testo stretto): l'utente le ha rifiutate come "non coerenti". Le versioni scartate sono in miniatura/vecchie-*.
- Schermata finale del video 4: video lungo 3 (Pensioni 2027: quanto aumenta DAVVERO?), Iscriviti in basso a destra.
- Prossimo: l'utente programma il video 4 subito. Poi (solo se ordinato) short 6 teaser del video 4 ("video correlato" = video 4), video 5 con motore b-sync-80.js e regola N.15. Video lungo 3: visualizzazione media 2:05 su 12:54; vedere proposte di fidelizzazione sopra.
- ERRORI DA NON RIPETERE: fare cose non ordinate; copiare lo stile dei concorrenti invece di quello dei nostri video; mandare zip; scegliere angoli (45 centesimi) che non interessano al pubblico.
- Chat intera di questa sessione (07-08/10/2026): conti_in_pensione/chat/chat-sessione-6-completa.md (testo intero, 160 messaggi; le chat 4 e 5 sono in chat/ e 12-KIT-05-10/). Messaggio per ripartire: leggere REGOLE-FISSE.md + CLAUDE.md + 14-.../pacchetto.txt, poi aspettare l'ordine.
