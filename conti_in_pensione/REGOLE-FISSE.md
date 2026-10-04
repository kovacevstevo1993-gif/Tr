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
