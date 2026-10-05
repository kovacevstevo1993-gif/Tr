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
- Short: pubblicato a mano (circa 7:30) il giorno dopo il video lungo, rimanda al video lungo ("video correlato" + commento fissato con link); miniatura che attira il click.
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
- Descrizione, titolo, tag e commento da fissare: a parte, come sempre (descrizione completa, tutto insieme in un riquadro).
- Da applicare in ogni chat, per ogni video e short, senza che l'utente lo ripeta.

## ISTRUZIONI UTENTE (05/10/2026, short 4)
- Short 4: l'utente ha registrato la voce e mandato 6 screenshot di fine blocco. Le clip vanno fatte "migliorate rispetto agli altri, meglio e più dettagliate" e "deve capirsi benissimo le slide" (regola n.5: più lente, movimento che finisce bene, ferme e leggibili prima della fine).
- L'utente scrive le didascalie in CapCut sopra le clip (testo bianco circa al 33% dell'altezza): lasciare libera la fascia centrale-alta (circa y 330-680 su 1920) e tenere le grafiche principali sotto.

## REGOLA N.7 (utente, 05/10/2026): IL TESTO CHE L'UTENTE METTE IN CAPCUT E' SOLO UN SEGNAPOSTO, LO TOGLIE LUI; LA DIDASCALIA STA NELLA SLIDE
- Frase dell'utente: "Il mio testo su CapCut lo tolgo io. Dove hai mai visto che metto io le didascalie nel video?"
- Il testo bianco che l'utente scrive in CapCut mentre registra la voce serve solo per segnare i blocchi: lo cancella. NON è la didascalia del video e NON va evitato nelle clip.
- La didascalia visibile sta DENTRO la slide (titoletto in alto, grafica al centro, didascalia nel riquadro in basso), come nei video 1 e 2. Le clip dello short 4 con la didascalia in basso (commit cad4b42) sono quelle GIUSTE.
- (Errore di Claude del 05/10: aveva tolto la didascalia dalle clip e rifatto tutto: sbagliato, ripristinato.)
