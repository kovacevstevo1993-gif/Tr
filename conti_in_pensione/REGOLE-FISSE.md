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

## ISTRUZIONI UTENTE (08/10/2026, short 6)
- SHORT 6 = teaser del video lungo 4 (invalidita' 2027), "video correlato" = video 4. Didascalie che attirano curiosita' verso il video lungo; "migliora tutto, professionale, facile da capire". Cartella 15-short-6-teaser-video-lungo-4 (copione-blocchi.txt). Gancio diverso dagli short precedenti; niente 45 centesimi come angolo.
- Risposte ai commenti YouTube: scritte con i NUMERI in cifre (non in lettere: non sono voce), in un riquadro.
- (08/10/2026) Short 6: 6 clip S6-blocco01..06.mp4 fatte (QA OK su tutti i fotogrammi, 1080x1920, 30 fps, 1924 fotogrammi = 64,1 s; tempi sulla voce stimati a caratteri, tutto completo entro l'80% del blocco). Cartella 15-short-6-teaser-video-lungo-4 (clip, sorgenti, DURATE.txt, copione-blocchi.txt). Da fare: miniatura e pacchetto (solo se ordinati).
- Risposte ai commenti offensivi (es. "SOMARI"): chiedere con gentilezza di moderare i termini, spiegando che il canale e' solo informativo: non decide e non paga le pensioni.
- (09/10/2026) Miniature degli short: ogni short ha un LAYOUT DIVERSO dal precedente (stesso stile del canale), non lo stesso schema con altri numeri. L'utente ha rifiutato la miniatura dello short 6 uguale allo short 5 ("cambia solo 2 numeri"): rifatta con tag ATTENZIONE, INVALIDI 2027 gigante, scheda accompagnamento, timbro NON E' 3%.
- (09/10/2026) MAI usare "INVALIDI" da solo come etichetta per le persone (es. "INVALIDI 2027" in miniatura): offensivo. Usare "INVALIDITÀ". Va bene dentro una frase descrittiva (es. "INVALIDI AL 100%").

## STATO 08-11/10/2026 - SHORT 6 FATTO + (per la chat nuova)
- Short 6 (teaser video 4, cartella 15-short-6-teaser-video-lungo-4): 6 clip S6-blocco01..06.mp4 consegnate (QA OK), pacchetto.txt (titolo, descrizione, tag, commento, impostazioni) consegnato in chat, miniatura miniatura-short6.png (layout nuovo: tag ATTENZIONE, "INVALIDITA' 2027" gigante, scheda accompagnamento, timbro "NON E' 3%"). Miniature vecchie scartate: vecchia-uguale-short5.*.
- Risposte ai commenti del video 3 date in chat (numeri in cifre, riquadro; ai commenti offensivi si chiede di moderare i termini: canale solo informativo).
- Dati canale 09-11/10: video lunghi ~19.000 visualizzazioni (video 3: 16 mila), short ~3.500, circa 40 iscritti; notifiche portano visualizzazioni anche ai non iscritti (notifiche di video consigliati).
- NICCHIA (11/10): il canale e' partito ed e' creato. La nicchia RESTA pensioni/Inps over 55: NON si cambia e NON si propongono spostamenti o canali nuovi. La domanda dell'utente sulle nicchie piu' pagate era solo una domanda (regola N.13), non un ordine.
- Regole nuove 09/10: mai "INVALIDI" da solo come etichetta per persone (ok "invalidi al 100%" in frase); miniature con layout DIVERSO dalla precedente.

## REGOLA N.16 (utente, 11/10/2026): MAI CHIEDERE L'AUDIO DELLA VOCE, I TEMPI LI CALCOLA CLAUDE
- L'utente: "quando mai te li ho mandati? Ogni chat lo chiedi... devi calcolarlo te". L'audio NON arriva mai e NON va mai chiesto (la regola n.14 che dice "chiedere l'audio" e' ANNULLATA).
- I tempi di ogni elemento si calcolano da soli: testo del blocco + durata del blocco (screenshot) -> tempo di ogni parola in proporzione ai caratteri, con pause alle virgole e ai punti, ricalibrato sulla durata esatta del blocco. Ogni elemento compare sulla sua parola, tutto completo entro l'80% (regola n.15). Nessuna domanda all'utente su questo.
- Se la chat e' nuova: leggere DURATE.txt e copione-blocchi.txt della cartella del video e procedere.

## STATO 11/10/2026 - VIDEO LUNGO 5 (tredicesima 2026), cartella 16-video-lungo-5
- Copione v2 a 37 blocchi (copione-blocchi.txt), durate dagli screenshot per TUTTI i 37 blocchi in DURATE.txt (totale 14137 fotogrammi = 07:51+7f). Ricerca in ricerca-11-10-2026.md (vidIQ: V3 perde 53 punti nel primo minuto; formula "tabella netti + TUTTA LA VERITA'" + trucco pratico).
- Correzione voce blocco 34: "Mai Inps" e "Obis emme" (nel file del copione c'e' ancora "My Inps"/"O bis em": nelle slide usare Mai Inps / ObisM).
- Prossimo: clip V5-blocco01..37.mp4 (1920x1080, 30 fps, motore b-sync-80.js, niente semafori, stile video vecchi), QA su tutti i fotogrammi, consegna come MP4 singoli.

## REGOLA N.17 (utente, 11/10/2026): VIDEO 5 = REGOLE E STILE DEI BLOCCHI FINALI DEL VIDEO 4
- L'utente: "segui tutte le regole dell'ultimo video, non quelle dei blocchi iniziali perche' li hai sbagliati, ma segui quelli finali che sono perfetti". Per il video 5: stesso stile, stessa densita' e stesso ritmo dei blocchi FINALI del video 4 (V4-blocco16..30, motore con tempi calibrati sulla voce), NON dei blocchi 1-5 del video 4. In piu' regola N.15 (tutto completo entro l'80 %), N.11 (niente semafori), N.12 (stile coerente con i video vecchi).

## REGOLA N.18 (utente, 11/10/2026, dopo il primo render del video 5): SLIDE TROPPO VELOCI = ERRORE GRAVE, MAI PIU'
- L'utente: "le slide sono velocissime, non si capisce niente; ogni parola fai sparire la slide in mezzo secondo; gli elementi che durano mezzo secondo non si vedono neanche; 80 % inteso anche per TUTTI gli elementi che devono finire". Errore di Claude: scene da 1,6-2,5 secondi (media 4 s, V4 finali 5,5 s), comparse accorciate a 0,4 s, 3 scene per blocco.
- REGOLE (valgono sempre, per ogni video e short): (1) UNA scena per blocco; DUE solo se il blocco e' lungo e ognuna dura almeno 5 secondi; mai scene sotto i 5 s. (2) Dentro una scena gli elementi COMPAIONO e RESTANO fino a fine scena: nessun elemento sparisce a meta' scena. (3) Animazione di comparsa 0,9 s, mai accorciata. (4) Ogni elemento resta completo e fermo almeno 2,5 s prima della fine. (5) Tutti gli elementi finiti entro l'80 % della scena, il resto fermo. (6) Tra un elemento e il successivo almeno 0,45 s. (7) Controllare la durata delle scene (window.__SC) PRIMA di renderizzare: se una e' sotto i 5 s, unire.

## ERRORI DEL VIDEO 5 (11/10/2026) - DA NON RIPETERE MAI (l'utente: "salvale ste robe")
1. SLIDE TROPPO VELOCI: ogni blocco spezzato in 2-4 mini-slide (111 in tutto), media 4 s, alcune da 1,6-2,5 s; a ogni cambio spariscono tutti gli elementi. Nei blocchi FINALI del video 4 (quelli "perfetti") le scene durano in media 5,5 s e sono poche (circa 2,5 per blocco).
2. COMPARSE ACCORCIATE: nelle scene brevi ho ridotto la comparsa degli elementi da 0,9 s a circa 0,4-0,5 s (elementi che non si vedono). Comparsa SEMPRE 0,9 s.
3. 80 % APPLICATO MALE: l'80 % l'ho applicato a ogni mini-slide. Il senso: gli elementi COMPAIONO e RESTANO sullo schermo, l'ultimo compare all'80 % della slide, poi tutto fermo e leggibile. Una scena per blocco (due solo se ciascuna dura almeno 5 s). Nessun elemento sparisce dentro la scena.
4. CONTROLLO SBAGLIATO E "CONTROLLATO" DETTO SENZA AVERLO FATTO: il QA automatico controlla solo testi tagliati/sovrapposti/fermi, NON il tempo di lettura. Prima di dire "controllato" e prima di mandare: (a) misurare con window.__SC e window.__IT la durata di ogni scena (>= 5 s) e il tempo di comparsa di ogni elemento (ultimo completo all'80 %, fermo il resto, distanza >= 0,45 s tra elementi); (b) guardare la sequenza del video, non solo le slide a fine scena.
5. LA REGOLA N.15 L'AVEVO LETTA E NON L'HO SEGUITA: leggere le regole non basta, vanno applicate con i NUMERI (scena >= 5 s, comparsa 0,9 s, ecc.) e verificate.
6. ALTRI ERRORI DI QUESTA CHAT: chiesto l'audio nonostante la regola N.16; ricominciato a rifare le slide senza un ordine dell'utente (violata la regola N.13: una domanda = una risposta, si cambia solo se l'utente ORDINA); letto "restituisci" (crediti/soldi) come "rifai"; fatto domande inutili all'utente gia' arrabbiato; croci rosse che coprivano le scritte (corretto nel render 1).
7. COSA VUOLE L'UTENTE PER LE SLIDE: lente, un elemento alla volta, elementi che restano sullo schermo, tutto finito all'80 % e fermo, stile dei blocchi finali del video 4. Se non e' chiaro un ordine: UNA domanda breve, mai ricominciare da soli.
8. STATO: i 37 clip V5-blocco01..37.mp4 consegnati l'11/10 sono la versione 1 (slide troppo veloci, NON accettata dall'utente). La versione 2 (una scena per blocco) e' salvata nelle sorgenti (specs-v5.js) ma NON renderizzata e NON consegnata: si rifa' solo se l'utente lo ORDINA.
- Script del controllo dei tempi: conti_in_pensione/qa/qa_tempi.py (da lanciare PRIMA di ogni render, insieme a qa_slide.py).
- BLOCCO AUTOMATICO PROVATO (11/10/2026): in 16-video-lungo-5/sorgenti il motore (b-sync-80.js) RIFIUTA le scene sotto i 5 s (errore "REGOLA N.18") e render.py NON fa partire il render se i controlli dei tempi o dei fotogrammi non passano. Per provarlo senza creare video: python3 render.py <blocco> check. DAL VIDEO 6 e per ogni short: copiare b-sync-80.js e render.py da 16-video-lungo-5/sorgenti, non usare le versioni vecchie.

## REGOLA N.19 (utente, 11/10/2026): MINIATURE E TITOLI = COPIARE TUTTO DAI VIRALI, SENZA CHE LO DICA L'UTENTE
- L'utente: "non devo dirlo io, per quello ti dico di copiare tutto dagli altri". Quando l'ordine e' "come i video virali", si copia da quelli che vanno TUTTO cio' che funziona: parola chiave di tema ("PENSIONI" / "PENSIONE") GRANDE e subito leggibile, cosi' si capisce che e' la tredicesima della PENSIONE e non quella di tutti; domanda con "?"; promessa ("ECCO IL TUO IMPORTO", "TABELLA IMPORTI"); cedolino/documento con l'importo; freccia/spunta. Solo i colori e lo stile grafico restano quelli dei video dell'utente.
- Titolo: parola calda in maiuscolo con "PENSIONI/PENSIONE" dentro il titolo (come i titoli virali), non solo "TREDICESIMA".
- Errore del 11/10 (miniature video 5): tolta/omessa la parola PENSIONE dalle 3 miniature e dal titolo; non si capiva che era la tredicesima dei pensionati.

## REGOLA N.20 (utente, 11/10/2026): "MAI INPS" SOLO A VOCE; NEI TESTI SCRITTI SI SCRIVE "MY INPS"
- Titoli, descrizioni, tag, hashtag, commenti e slide: il portale si scrive "My Inps" (nome vero, come lo cercano le persone), tag "my inps", hashtag #myinps. "Mai Inps" e' SOLO la pronuncia nei blocchi di voce. Errore del 11/10: scritto "mai inps" nei tag, #maiinps e "Mai Inps" nella descrizione del video 5. Il modello si scrive "ObisM" (tag "obism"), non "obis m".

## REGOLA N.21 (utente, 11/10/2026): TAG - NIENTE VIRGOLE DENTRO UN TAG E CONTEGGIO COME YOUTUBE
- Errore del 11/10 (video 5): ho scritto il tag "importo aggiuntivo 154,94": YouTube lo ha spezzato in due tag ("154" e "94") e ho detto "499 caratteri" mentre YouTube ne contava 516/500 (rosso). Regole: (1) mai virgole o punti-virgola dentro un tag (usare "154 euro"); (2) il conteggio di YouTube = somma delle lunghezze dei tag, +2 per ogni tag che contiene uno spazio (virgolette), + 1 per ogni virgola di separazione (n-1). Controllare con questo calcolo (verificato: ha dato 516 come YouTube) e restare sotto 500 (meglio 490-496). Mai dire "sotto i 500" senza averlo calcolato cosi'.

## REGOLA N.22 (utente, 11/10/2026): SLIDE FINALE CON SPAZIO LIBERO PER LA SCHERMATA FINALE DI YOUTUBE
- Errore scoperto dall'utente dopo 5 video: la slide finale (disclaimer) riempie tutto lo schermo, quindi il riquadro del video correlato e il pulsante Iscriviti della schermata finale di YouTube (20 s) si sovrappongono al testo. Non c'e' spazio per niente.
- REGOLA per ogni video lungo, dal prossimo: l'ultimo blocco (disclaimer / chiusura) deve avere gli ultimi 20 secondi con una zona LIBERA e vuota dove YouTube mette gli elementi (riquadro video correlato al centro-basso, Iscriviti in basso a destra), e il testo del disclaimer deve stare nella parte alta, mai sotto o dietro i riquadri. Le slide degli ultimi 20 s devono restare leggibili con gli elementi sopra.
- Controllare nei fotogrammi finali, sovrapponendo le zone dei riquadri, che nessun testo sia coperto. La schermata finale dura 20 s: il video deve durare almeno 20 s di slide finale (i tempi partono da fine video meno 20 s).
- Video 5: la slide finale (blocco 37) e' fatta col disclaimer a tutto schermo e NON ha spazio. Si rifa' solo se l'utente lo ORDINA.

## REGOLA N.23 (utente, 11/10/2026): OGNI ERRORE MOSTRATO = SOLUZIONE SALVATA DA SOLO, SENZA CHE LO DICA L'UTENTE
- L'utente: "quando ti faccio vedere gli errori devi salvare le soluzioni da solo, non devo dirtelo io". Appena l'utente mostra o segnala un errore (screenshot, frase, domanda), PRIMA di rispondere: scrivere in REGOLE-FISSE.md l'errore, la causa e la regola/soluzione, con commit e push (regola N.4). Poi rispondere in breve. Vale anche per gli errori scoperti da me. Non va aspettato l'ordine "salvalo".
- Salvare solo la regola (non cambiare il lavoro: regola N.13).

## REGOLA N.24 (utente, 12/10/2026): MAI DIRE "L'HAI APPROVATO TU" SE NON C'E' PROVA; TITOLO SENZA "PENSIONI" = DIFETTO
- Errore del 12/10: ho scritto all'utente che il titolo del video 4 "l'aveva approvato lui". Nel repo non c'e' nessuna approvazione del titolo (e' scritto da Claude; l'utente ha ordinato solo di togliere "45 centesimi"). Mai attribuire all'utente decisioni non documentate.
- Titolo video 4 ("Invalidita' 2027: quanto aumenta DAVVERO? Importi e 3 trappole"): non contiene la parola "PENSIONI/PENSIONE" ne' una parola calda in maiuscolo come i titoli virali; la ricerca (vidIQ) dava le keyword "pensioni invalidita'" e "aumento pensioni invalidita'". Stesso difetto del primo titolo del video 5 (regola N.19). Non e' provato che sia questa la causa dei 149 view.

## REGOLA N.25 (utente, 12/10/2026): VERIFICARE PRIMA DI DIRE "POSSO" O "NON POSSO"; MAI CORREGGERSI DOPO
- Errore del 12/10: ho detto "le visualizzazioni le guardo gratis", dopo aver detto che da curl non potevo leggere i video; poi ho controllato e ho corretto me stesso. Regola: PRIMA di dire se una cosa si puo' o non si puo' fare (curl, vidIQ, crediti), provarla; poi dare una risposta sola. Non dire mai prima una cosa e poi smentirsi.
- Dati verificati: dal curl funzionano le pagine elenco del canale (/videos e /shorts, danno titoli e visualizzazioni totali) e oembed (solo titolo); le pagine /watch sono bloccate (anti-robot): descrizioni e tag solo con vidIQ (5 crediti per chiamata, chiedere prima).

## REGOLA N.26 (utente, 12/10/2026): RISPOSTE AI COMMENTI CON UN IMPORTO = FARE IL CONTO COME NEL VIDEO
- Errore del 12/10: a un commento con un importo (2.618 euro lordi, moglie e 2 figli maggiorenni) ho risposto in modo generico (assegno unico), senza fare il conto del video. L'utente aveva mandato lo stesso commento per sbaglio in un'altra chat, dove la risposta era giusta: conto come nel video (lordo x 13 = reddito annuo, scaglione Irpef, Irpef sulla tredicesima senza detrazioni, netto), numeri in cifre, "il conto non include le addizionali", "il canale e' solo informativo". Causa: non ho letto il copione del video (16-video-lungo-5/copione-blocchi.txt) e ho trattato l'altra chat come estranea.
- Regola: davanti a un commento con un importo, PRIMA leggere il copione del video e rifare lo stesso conto con quell'importo; non inventare consigli fuori dal video. Se l'utente dice "ho sbagliato chat", la risposta deve comunque essere quella giusta per il suo canale.

## REGOLA N.27 (utente, 12/10/2026): IL GANCIO DI UNO SHORT DEVE NOMINARE SUBITO IL TEMA DEL VIDEO
- Errore del 12/10 (short 7, teaser video 5): il blocco 1 parlava di "mille euro di pensione... ne arrivano settecentosettanta" senza dire "tredicesima" ne' "dicembre"; chi guarda non capisce che e' la tredicesima. Causa: ho cercato un gancio diverso dagli altri short (regola del gancio) e ho tolto la parola del tema.
- Regola: nel blocco 1 di ogni short, nelle prime parole, deve comparire la parola del tema del video lungo (es. "tredicesima", "dicembre"). Il gancio e' diverso dagli altri, ma il tema si capisce subito.
- SOLUZIONE N.27 (12/10/2026): creato `conti_in_pensione/qa/qa_copione.py` (tema nelle prime 8 parole del blocco 1, numeri in lettere, Mai Inps a voce, chiusura short, gancio diverso, max 250 caratteri) e aggiunto alla CHECKLIST-REGOLE.md (riga 0, stampata a ogni messaggio dall'hook). Da lanciare PRIMA di consegnare ogni copione. Errore di fondo: le regole stavano nei file ma nessun controllo le verificava sul copione; ora c'e' lo script.

## STATO 12-13/10/2026 - SHORT 7 (teaser video lungo 5, tredicesima), cartella 17-short-7-teaser-video-lungo-5
- Copione 6 blocchi (qa_copione.py OK), DURATE.txt dagli screenshot (329, 286, 365, 352, 321, 305 = 1958 fotogrammi = 65,3 s), 6 clip S7-blocco01..06.mp4 in clip/ (1080x1920, 30 fps, fotogrammi verificati con ffprobe). Sorgenti in sorgenti/ (scenes7.js, checktempi.py: tempi OK, qa7.sh: QA su TUTTI i fotogrammi OK, anteprima a 0,5 s guardata). Da fare solo se ordinato: miniatura e pacchetto (video correlato = video lungo 5).
- (13/10/2026) Short 7: pacchetto.txt (qa_testi OK: titolo 64 caratteri, 25 tag = 494/500, 8 hashtag) e miniatura-short7.png (layout nuovo: barre 1.000 € lordo contro 770 € in banca con il pezzo mancante -230 €, PENSIONI TREDICESIMA, timbro NON È UN ERRORE, striscia "Dove sono finiti i 230 euro?") in 17-short-7-teaser-video-lungo-5. Video correlato = video lungo 5.

## REGOLA N.28 (utente, 13/10/2026): LA VOCE E' LA VOCE DI CAPCUT (SINTETICA); MAI DIRE "LA REGISTRI TU"; CONTROLLO DEL CANALE CONTRO LE REGOLE YOUTUBE
- Errore del 13/10: ho scritto che "la voce la registri tu" (nel repo "l'utente registra la voce in CapCut" significa che la genera con la voce CapCut). Su quella frase falsa avevo basato una risposta sul rischio monetizzazione. Mai attribuire all'utente cio' che non e' documentato (N.24).
- Errore 2: avevo detto di non aver mai controllato il canale contro le regole YouTube e ho risposto due volte con cose generiche. L'utente aveva detto fin dall'inizio di seguire le regole. Il controllo va fatto sulle pagine ufficiali (support.google.com/youtube), non a memoria.
- Verificato 13/10 sulle pagine ufficiali: (1) Programma Partner: 1.000 iscritti + 4.000 ore pubbliche (12 mesi) oppure 1.000 iscritti + 10 milioni di visualizzazioni Short (90 gg); domanda in Studio, revisione automatica + umana sul canale intero; rifiuto: ricorso entro 21 giorni o nuova domanda dopo 30 giorni. Canale: 137 iscritti il 13/10. (2) Contenuti non autentici (ex "ripetitivi", luglio 2025): vietati i contenuti in serie, generici, ripetitivi, "sulla base di un modello"; presentazioni di immagini/storie a modello con poco valore didattico non idonee; l'IA e' ammessa se c'e' visione creativa/valore originale. (3) Dichiarazione contenuti alterati/sintetici: serve per contenuti realistici che fanno dire/fare a una persona reale cio' che non ha fatto, scene realistiche mai avvenute, musica IA; una voce narrante sintetica che non imita una persona reale non e' tra gli esempi da dichiarare (l'elenco non e' esaustivo).
- Rischio vero del canale: slide dello stesso schema + voce sintetica = YouTube puo' giudicarle "a modello". Difesa: ogni video con analisi/conti originali e valore didattico, fonti ufficiali, titoli veritieri.

## STATO 13/10/2026 - VIDEO LUNGO 6 (cedolino di novembre), cartella 18-video-lungo-6
- Ordine utente (13/10): "procedi, controlla"; QUESTO video solo, per prova: blocchi di voce fino a 500 caratteri (invece di 250) per farlo piu' veloce. qa_copione.py ha ora il 4o argomento opzionale (limite caratteri): `python3 qa/qa_copione.py <file> novembre lungo 500`. Dal prossimo video vale di nuovo 250 se l'utente non dice altro.
- Copione 13 blocchi, 4815 caratteri, qa_copione OK (copione-blocchi.txt). Angolo: due voci fiscali di novembre: "arriva" (secondo acconto Irpef, 60%, esempio 800 euro -> 320 + 480) e "finisce" (addizionali, ultima rata); date: pagamento lunedi 2 novembre.
- Fatti verificati: UFFICIALE Inps: pensioni pagate il primo giorno bancabile (festivo -> giorno dopo) => 2 novembre; trattenute rateali del 730 devono concludersi entro novembre. DA FONTI SECONDARIE (money.it 28/09/2026, informazionefiscale, centrofiscale, che citano l'avviso Inps): acconto 100% dell'imposta, 40% + 60% se >= 257,52 euro, unica rata a novembre se sotto, nessun acconto se imposta <= 51,65, riduzione entro 10 ottobre; ultima rata addizionali a novembre; Enpam = aumenti/arretrati solo medici (trascrizioni Mr LUL e Pensioni e Aggiornamenti). Non trovato il messaggio Inps originale 2026: nel pacchetto citare "pagine ufficiali Inps" solo per cio' che e' ufficiale.
- Da fare solo se ordinato: durate (screenshot), slide, miniatura, pacchetto.

## REGOLA N.29 (13/10/2026): COME SI LEGGE LO SCREENSHOT DI CAPCUT (errore di lettura del blocco 1 del video 6)
- Errore: sul blocco 1 avevo letto il numero scritto sul righello ("22f") invece del segno sotto la riga bianca: 712 fotogrammi, quelli giusti erano 714. Causa: nello screenshot la riga bianca sta sempre OLTRE l'ultimo segno disegnato (il righello finisce con il video), di 0,4-0,9 fotogrammi.
- Regola di lettura (misurata sugli screenshot del 13/10): i segni del righello sono 1 fotogramma ciascuno, circa 67 px l'uno (etichetta, punto, etichetta...: etichette ogni 2 fotogrammi, il punto in mezzo vale +1). Fotogramma di fine blocco = ULTIMO SEGNO DISEGNATO prima della riga + 1 (arrotondamento per eccesso). Se l'ultimo segno e' un punto: etichetta precedente + 1, piu' 1.
- Video 6: 13 screenshot (blocchi 1-13), totale 8768 fotogrammi = 04:52+8f (DURATE.txt in 18-video-lungo-6).
- Motore: 18-video-lungo-6/sorgenti (copia di quello del video 5 + patch: cap vuota nell'ultimo blocco, nuovi elementi calS/stepRow/recap). Ogni blocco ha una o due scene (>= 5 s); il primo elemento compare entro ~1-2 s (nessuna slide vuota all'inizio); ultimo blocco: contenuti solo nella parte alta (y < 760), zona bassa libera per la schermata finale (N.22).

## REGOLA N.30 (utente, 14/10/2026): OGNI RICERCA vidIQ DEVE ESSERE IN ITALIANO E SU VIDEO ITALIANI
- Errore del 14/10 (pacchetto video 6): ho speso 5 crediti in `vidiq_similar_thumbnails` con una descrizione senza filtro paese: sono usciti video in inglese/indiano/spagnolo che non c'entrano (Costco, ASMR, Italia turismo, ecc.). Il canale e' italiano: la ricerca va fatta solo su video italiani.
- Regola: ogni chiamata vidIQ per questo canale usa SEMPRE parole chiave in italiano e i filtri di lingua/paese: outliers `language: "it"`; similar_thumbnails/similar_videos `channelCountry: "IT"` (e description in italiano); keyword_research con `country: "IT"` o `language: "it"`; generate_titles `language: "it"`, `regionCode: "IT"`. Dopo ogni risposta: controllare che i risultati siano italiani e pertinenti; se non lo sono, NON usarli e dirlo. Per le miniature dei concorrenti italiani i file si scaricano gratis (i.ytimg.com/vi/<id>/maxresdefault.jpg) dagli ID trovati con la ricerca pubblica di YouTube: preferire questo ai crediti.

## REGOLA N.31 (utente, 14/10/2026): VERIFICARE I FATTI SU FONTI UFFICIALI PRIMA DI CREARE TUTTO; MAI DIRE "NON VERIFICATO" DOPO LA CONSEGNA
- Errore: sul video 6 ho cercato i fatti, ho trovato per l'acconto Irpef solo siti di informazione fiscale, ho scritto copione e slide lo stesso e solo a lavoro finito ho detto "non verificato". La verifica sulle pagine ufficiali (Agenzia delle Entrate, Inps) si poteva fare subito: 14/10 fatta, tutte le soglie e percentuali dell'acconto sono confermate.
- Regola: PRIMA del copione, ogni cifra/data/regola va trovata su una fonte ufficiale (inps.it, agenziaentrate.gov.it, mef, gazzetta ufficiale). Se dopo la ricerca un dato resta solo su fonti non ufficiali: dirlo SUBITO, prima di scrivere il copione, e chiedere all'utente se tenerlo, toglierlo o dirlo come "secondo fonti di informazione". Mai consegnare tutto e poi elencare i dubbi.

## STATO 14/10/2026 - VIDEO LUNGO 6 (pensioni novembre / cedolino), cartella 18-video-lungo-6 (per la chat nuova)
- FATTO e consegnato: copione 13 blocchi (copione-blocchi.txt), durate dagli screenshot (DURATE.txt, 8768 fotogrammi = 04:52+8f), clip V6-blocco01..13.mp4 (cartella clip/, QA su tutti i fotogrammi OK, fotogrammi = durate), pacchetto.txt (titolo vidIQ 78, tag 496/500, qa_testi OK), 3 miniature A/B/C (miniatura/), ricerca-13-10-2026.md (ricerche e verifiche ufficiali). Fatti verificati su fonti ufficiali Inps e Agenzia delle Entrate; solo "aumenti e arretrati solo medici Enpam" resta senza fonte ufficiale.
- DA FARE solo se ordinato: l'utente carica il video; short 8 teaser del video 6 ("video correlato" = video 6); risposte ai commenti con importo (regola N.26); fidelizzazione del video 6 dopo qualche giorno. Crediti vidIQ: 40 (rinnovo 11/11).
- Regole nuove di questa sessione: N.28 (voce CapCut sintetica, verifica regole YouTube), N.29 (lettura righello CapCut: ultimo segno + 1), N.30 (vidIQ solo in italiano), N.31 (fatti su fonti ufficiali PRIMA di creare). Motore slide video 6: 18-video-lungo-6/sorgenti (specs-v6.js; per un nuovo video copiare b-sync-80.js, render.py e gli helper da li').
- ATTENZIONE: tutto e' sul branch della sessione claude/brave-ptolemy-b0jg0p; vedere la sezione AVVIO in CLAUDE.md (unione su main solo su ordine dell'utente).

## REGOLA N.32 (utente, 14/10/2026): CREDITI vidIQ = DIRE PRIMA QUANTI E PER COSA; NIENTE CHIAMATE A VUOTO
- Errore del 14/10 (pacchetto video 6): su 35 crediti spesi, 10 sprecati (similar_thumbnails senza filtro paese = risultati non italiani; keyword matching_terms su una frase troppo specifica = zero risultati). Due punteggi del titolo erano in piu'.
- Regola: anche quando l'utente autorizza vidIQ ("usa vidiq"), PRIMA di chiamare scrivere in una riga il piano (quali chiamate, quanti crediti in tutto, perche'). Fare per prime le chiamate piu' sicure (generate_titles, score_title con max 3 titoli, keyword_research con parole gia' cercate dagli italiani); le ricerche che possono uscire a vuoto o fuori lingua (matching_terms su frasi lunghe, similar_thumbnails) solo con filtri italiani e dopo aver provato l'alternativa gratuita (ricerca pubblica YouTube, miniature scaricate con curl). Dopo ogni chiamata controllare il risultato prima di farne un'altra. A fine lavoro dire quanti crediti sono andati sprecati.

## STATO 14/10/2026 - SHORT 8 (teaser video lungo 6, novembre), cartella 19-short-8-teaser-video-lungo-6
- Ultimo video pubblicato (verificato con curl /videos): video 6 "PENSIONI NOVEMBRE: pagamento lunedi 2 novembre...". Video correlato dello short 8 = video lungo 6.
- Copione 6 blocchi (copione-blocchi.txt, qa_copione.py novembre short OK, 953 caratteri), consegnato in chat.
- Ordine utente 14/10: "slide un po piu differenti, non stravolgere, cambia pochissimo, piu professionale". Fatte: schede con filetto verde a sinistra, barra di avanzamento a 6 trattini sotto il titoletto, calendari (1 e 2 novembre), frecce giu/su per le due voci, righe numerate. Durate in DURATE.txt (311,317,274,322,282,274 = 1780 fotogrammi). Clip S8-blocco01..06.mp4 in clip/ (checktempi OK, qa_slide OK su tutti i fotogrammi, ffprobe = durate, sequenza a 0,5 s guardata), consegnate. Da fare solo se ordinato: miniatura e pacchetto.
- (14/10) Short 8: pacchetto.txt (qa_testi OK: titolo 58 caratteri, 26 tag = 486/500, 8 hashtag) e miniatura/miniatura-short8.png (layout nuovo: cedolino di novembre inclinato con la riga "VOCE ? -480 €" cerchiata in rosso, freccia gialla, timbro NON E' UNA MULTA, tag CONTROLLA IL CEDOLINO, striscia "PERCHE' 480 EURO IN MENO?"). vidIQ: 1 sola chiamata score_title (titolo 73), 5 crediti, nessuno sprecato; saldo 35 (rinnovo 11/11). Keyword del tema gia' in 18-video-lungo-6/ricerca-13-10-2026.md, non rifatte.

## REGOLA N.33 (utente, 15/10/2026): TESTI COERENTI CON LA DATA DI PUBBLICAZIONE
- Errore del 14/10 (commento fissato short 8): "A novembre ti hanno trattenuto qualcosa nel cedolino?" mentre lo short esce a meta' ottobre: novembre non e' ancora arrivato. L'utente: "che domanda e' che siamo a ottobre?".
- Regola: prima di consegnare titolo, descrizione, commento e copione, controllare la data di oggi/pubblicazione: mai parlare al passato di cose future (cedolino, pagamento, trattenute). Domande al pubblico solo su cose che la gente puo' gia' sapere (quanto prende, se ha fatto il 730), o al futuro ("cosa aspettarti a novembre").
