CHECKLIST THE SENIOR ADVANTAGE (stampata a ogni messaggio dall'hook .claude/hooks/regole-senior.py). Regole complete: CLAUDE.md + senior_advantage/PASSAGGIO-CHAT.md.
1. MAI LA STRADA PIU VELOCE (ordine assoluto). Mentre lavori cerchi TUTTO e applichi TUTTE le regole, sempre, non solo all'inizio della chat.
2. Ogni fatto e numero: letto sulla fonte ORIGINALE e COMPLETA (pagina ufficiale, PDF intero, note comprese), non su riassunti. Cercare eccezioni (Stati esclusi, fasce di prezzo, condizioni). Se non si puo verificare, NON si mette.
3. Controllo completo PRIMA di mandare, senza che l'utente lo chieda, TUTTI i controlli insieme (non a pezzi). Copione: lanciare python3 senior_advantage/qa/qa_copione.py <file> (se stampa ERRORI non si manda) + fonti originali e date a mano. Lo script controlla (max 500 caratteri, niente cifre/simboli, sigle a lettere, snap minuscolo, numero annunciato = voci = riepilogo, nessuna frase o sequenza di 5 parole ripetuta). Slide: OGNI fotogramma controllato, fotogrammi = durate dell'utente.
4. Mai dire fatto/pronto/mandato se non e vero e confermato.
5. Rispondere SEMPRE in italiano, SOLO a cio che chiede, il minimo. Niente scuse, niente offerte non richieste.
6. Copioni in chat: **Blocco N** + riquadro ```, tutti in un colpo, mai in file. Pacchetto: formato fisso (MODELLO-DESCRIZIONE-VIDEO-1.md / MODELLO-PACCHETTO-SHORT.md).
7. Slide: solo cio che dice la voce; layout diverso dai video precedenti in ogni blocco; ultimo elemento all'80%; tutto finito dentro il blocco; screenshot delle durate = fare SUBITO le slide.
8. Non anticipare i passi. vidIQ: controllare il saldo con vidiq_balance (gratis); crediti solo se l'utente lo chiede/autorizza.
9. Salvare tutto subito (file di stato), commit, push sul branch, merge su main. Ogni nuova regola dell'utente: scriverla SUBITO parola per parola in CLAUDE.md e qui (una riga).
10. VERIFICA TUTTO IN OGNI MODO POSSIBILE (ordine utente 22/10): se una fonte originale non si apre, cercarne un'altra originale; se nessuna lo conferma, il fatto non si mette.
11. Per ogni fatto controllare anche la DATA della fonte: se la fonte e vecchia o non si puo confermare che valga oggi, la frase lo dice ('Walmart has said'), mai al presente come se fosse sicuro oggi (errore 22/10, blocchi 10, 14, 18, 20 Walmart).
12. Niente frasi generiche non verificabili presentate come fatti ('most people never...', 'every day somebody...', 'nobody...'): o c'e la fonte o la frase si riscrive senza affermarlo (errore 22/10 copione Walmart).
13. Controllo di LOGICA prima di mandare: ogni esempio deve essere vero anche facendo i conti (es. regalo comprato a novembre: i 90 giorni vanno gia oltre il 31 gennaio, quindi l'esempio giusto era ottobre; errore 22/10 Walmart blocco 7). Ogni rimando ('number five', 'the sentence from number ten') deve puntare al blocco giusto.
14. Controllo dell'INGLESE prima di mandare: rilettura frase per frase (grammatica, articoli, tempi, frasi naturali per un americano), insieme a tutti gli altri controlli (errore 22/10: fatto solo dopo la domanda dell'utente).
15. Alla consegna di un copione, una riga sopra i blocchi: 'Controlli 1-24 fatti (tutta la lista): fonti originali, date, logica, inglese, script OK'. Si scrive SOLO se e vero. L'utente non deve mai chiedere 'e perfetto?' (ordine utente 22/10).
CONTROLLI AGGIUNTI IN ANTICIPO (22/10, ordine utente: aggiungere subito tutti i tipi di errore possibili, non aspettare di farli):
16. Data di PUBBLICAZIONE: ogni mese, stagione, 'right now', 'this week' deve essere vero quando il video esce, non quando si scrive (es. 'buy a gift in October' tolto: il video esce dopo).
17. Ortografia inglese: lo script la controlla (pyspellchecker; se manca: pip install pyspellchecker).
18. Gancio mai uguale ai copioni precedenti (lo script confronta) e con formula diversa.
19. Promesse = contenuto: ogni anticipazione dei blocchi iniziali va mantenuta; numero nel titolo = voci; il titolo non deve far credere cose che il video non dice (es. 'Over 60' quando nessuna voce dipende dall'eta).
20. Tema del canale: niente Medicare, Social Security, tasse, pensione come argomento (sono di Money Backstory).
21. Coerenza dei numeri: la stessa cifra detta in piu blocchi deve essere identica ovunque (script: elenco NUMERO da guardare uno per uno).
22. Pronuncia per CapCut: nomi, siti e sigle scritti come vanno letti (Sheer I D, walmart dot com, E B T); niente parole che la voce legge male.
23. Niente consigli medici o legali e niente promesse di guadagno: rimandare sempre a farmacista, medico, piano, ente ufficiale.
24. Stessi controlli (fonti, date, logica, inglese) anche per titolo, descrizione, tag, commento, testi delle slide e miniature.
25. Dopo QUALSIASI correzione si rimanda SEMPRE il copione INTERO, mai solo i blocchi cambiati (ordine utente 22/10: 'mandami tutto il copione... mandi solo il sette per confondere').
26. Slide di ogni video nuovo: stile grafico proprio (sfondo, testata, schede) diverso dai video precedenti, piu professionali e con piu elementi (ordine utente 23/10).
27. Nomi file delle slide UNICI, mai uguali a quelli di altri progetti (ordine utente 23/10: V8-blocco era gia usato da Conti in Pensione). Formato SA-<tema>-bloccoNN.mp4; controllare con find su tutto il repo prima di mandare. Vale dal PROSSIMO video (Walmart resta V8-blocco).
28. Slide finale: riquadro WATCH NEXT sempre nella STESSA posizione dei video precedenti (a destra, x 1150-1830, y 250-710), mai spostarlo: l'utente dovrebbe rifare la schermata finale (ordine utente 23/10; Walmart resta col riquadro a sinistra).
