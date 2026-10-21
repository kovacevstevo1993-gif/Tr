CONTI IN PENSIONE - CHECKLIST REGOLE (promemoria automatico a OGNI messaggio dell'utente. Fonte completa: REGOLE-FISSE.md. Applicarle TUTTE prima di rispondere e prima di consegnare.)
COME LAVORARE
1. Eseguire SOLO gli ordini. Una DOMANDA = solo una risposta, mai modifiche (N.13). Se non e' chiaro: UNA domanda sola prima di fare qualsiasi cosa. Mai iniziare lavori non ordinati. Non ripetere all'utente cio' che ha fatto lui.
2. Risposte corte, una cosa alla volta, niente scuse ne' "hai ragione" lunghi. Dopo aver mandato file (clip, miniature): NIENTE descrizione di cosa c'e' dentro, l'utente li vede da solo (spreca crediti): una riga sola. Mai dire "fatto/pronto/mandato" prima che sia vero (render finito, controllato, consegnato).
3. VERIFICARE PRIMA di dire "posso/non posso" (N.25): provare, poi una risposta sola. Mai dire una cosa e poi smentirsi. Mai attribuire all'utente decisioni non documentate (N.24).
4. Ogni errore/correzione mostrata dall'utente: scriverla SUBITO in REGOLE-FISSE.md con la soluzione (commit+push) senza che lo ordini (N.4, N.23). Prima di consegnare: rileggere questa checklist e usare gli script di controllo.
5. Mai chiedere l'audio della voce: i tempi si calcolano da testo+durate (N.16). Mai zip: clip MP4 singoli. Mai crediti vidIQ senza chiedere (saldo gratis con vidiq_balance; 5 crediti a chiamata). Dati pubblici canale: curl su /videos e /shorts (le pagine /watch sono bloccate).
6. "Copiare dai virali" = copiare TUTTO cio' che funziona (parola PENSIONI grande, domanda con ?, promessa, cedolino con importo, freccia/spunta); solo colori e stile restano quelli dell'utente (N.19). Niente volti di persone reali ne' logo Inps.
COPIONI (blocchi di voce)
0. Prima di consegnare QUALSIASI copione: python3 conti_in_pensione/qa/qa_copione.py <copione-blocchi.txt> <parola-tema> short|lungo. Controlla: tema nominato nelle prime 8 parole del blocco 1 (N.27), numeri in lettere, Mai Inps a voce, chiusura short (video correlato, iscriviti, mi piace), gancio diverso dagli altri short, max 250 caratteri a blocco. Se non passa, non si consegna.
TESTI (titolo, descrizione, tag, commento, impostazioni) - ognuno in un RIQUADRO ``` separato, in chat
7. Lanciare SEMPRE: python3 conti_in_pensione/qa/qa_testi.py <file pacchetto>. Se un controllo non passa, non consegnare.
8. Titolo: contiene PENSIONI/PENSIONE, parola calda in maiuscolo, domanda con ?, promessa; senza hashtag; max 100 caratteri.
9. "Mai Inps" SOLO a voce. Nei testi scritti: "My Inps", hashtag #myinps, tag "my inps", modello "ObisM" (N.20).
10. Tag: niente virgole dentro un tag; conteggio YouTube = lunghezze + 2 per ogni tag con spazio + 1 per ogni separatore; restare 480-497 (N.21). Hashtag da 5 a 12. Tag senza "inps" ripetuti inutilmente.
11. Descrizione: gancio, elenco, CAPITOLI dalla timeline dell'utente (arrotondati per difetto), fonti, Iscriviti + link canale, "Disclaimer: ... Questo canale non e' affiliato all'Inps", hashtag. Nessun altro link. Negli SHORT: "tocca il Video correlato" (mai link), e il video correlato si imposta solo sullo short.
12. Mai "INVALIDI" da solo come etichetta; mai "45 centesimi" in titoli/miniature; mai semafori nelle slide (dal video 4).
SLIDE / CLIP (1920x1080 lunghi, 1080x1920 short, 30 fps; nomi CON PREFISSO DEL CANALE dal 21/10: CIP-V10-blocco01.mp4 / CIP-S12-blocco01.mp4, mai V7-blocco come gli altri canali)
13. Una scena per blocco (due solo se ognuna >= 5 s), comparsa elementi 0,9 s, nessun elemento sparisce nella scena, ultimo elemento completo all'80 % e poi tutto fermo, >= 0,45 s tra elementi (N.15, N.18).
14. Stile dei blocchi FINALI del video 4, coerente con i video vecchi (verde acqua), tono serio da adulti (N.12, N.17).
15. Prima di ogni invio: render.py + b-sync-80.js (blocco automatico), qa_tempi.py, qa_slide.py su TUTTI i fotogrammi, ffprobe durate = fotogrammi dell'utente. Il QA non misura il tempo di lettura: misurare con window.__SC / __IT e GUARDARE la sequenza.
16. Ultimo blocco: disclaimer nella parte ALTA e ultimi 20 s con zona libera in basso per riquadro video correlato + Iscriviti (N.22).
17. Non rifare/rimandare blocchi gia' consegnati se l'utente non lo ORDINA.
19. Testi e domande coerenti con la data di pubblicazione: mai chiedere al passato cose future (N.33).
20. Prima di consegnare: rileggere tutto come lo spettatore nel giorno di pubblicazione (date, tempi verbali, numeri coerenti ovunque). Dubbi detti PRIMA, mai dopo (N.34).
MINIATURE
18. Stile dei video pubblicati (sfondo verde acqua a raggi, numeri giganti con contorno scuro, palline rosso/verde, striscia bianca con bordo giallo), layout DIVERSO dalla precedente, con la parola PENSIONI grande e la frase dell'utente. Controllare ogni immagine (testi tagliati/sovrapposti) prima di mandarla.
21. Il video piu recente e il PRIMO della lista /videos o /shorts, anche se il titolo e diverso dal pacchetto: mai dire "non pubblicato" senza verificarlo (N.39).
22. Sistemare solo il pezzo sbagliato, mai rifare tutto; misurare i testi PRIMA del primo render, un solo render finale (N.40).
23. Video e short MAI uguali ai precedenti: chiusura, struttura/numero blocchi, apertura, frasi fisse e grafica sempre diversi (short e lunghi).
24. Prima di consegnare: revisione critica del CONTENUTO ("e perfetto?": modello della ricerca, ripetizioni, promesse non decise dall utente, tono, dati che invecchiano). Correggere PRIMA; mai mandare cose con difetti noti (N.42).
