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

## REGOLA N.3 (utente, 04/10/2026): OGNI VIDEO HA UN MODELLO DI SLIDE DIVERSO
- Cambiare lo stile/modello grafico delle slide (colori, forme, impostazione, tipo di oggetti, animazioni) per OGNI nuovo video lungo e per ogni short, così i video non sono tutti uguali.
- NON cambiare il video 2 adesso (resta com'è). Si applica a partire dal PROSSIMO video (video lungo 3 e short successivi).
- Il canale resta riconoscibile (nome, logo, verde acqua come colore base), ma cambiano layout, forme, sfondo, tipo di didascalia e di oggetti.

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
- Modello di slide DIVERSO per ogni video (dal video 3 in poi, il video 2 resta com'è).
- Kit completo per cambiare chat: KIT-1 (testi, chat, regole) + zip dei video; messaggio di ripartenza in 07-KIT-COMPLETO/00-LEGGIMI-PRIMA.md; leggere anche REGOLE-FISSE.md.
- Eseguire SOLO gli ordini, nessuna scelta propria, lavorare a fondo senza scuse.
