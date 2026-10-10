# VIDEO 8 - fine voce dei blocchi (dagli screenshot dell'utente, 30 fps)
Lettura: etichette righello 12f (x~200) e 14f (x~334), passo 2 fotogrammi ~134 px; cursore x=360 -> 14f.
- Blocco 1: fine voce 00:18 + 14f = 554 fotogrammi (screenshot 10/10/2026 00:06). Durata blocco 1 = 554 fotogrammi (18,47 s).
- Blocco 1 FATTO (10/10): slide 1 = 285 fotogrammi ("born before 1962 ... stack of bills"), slide 2 = 269 fotogrammi ("still paying ... say stop"); tagli ai confini delle frasi dal calcolo parola per parola (`sync.json`). File: `slide/v8-b1-01.mp4`, `v8-b1-02.mp4`; codice `code/v8b1.py`.
- Screenshot 10/10 (lettura: fine = min*60+sec fotogrammi + etichetta + (360 - x_etichetta)/67, arrotondata):
  - Blocco 2: 00:36 + 10f (etichetta 10f x=356) = 1090 assoluti; durata 536.
  - Blocco 3: 00:51 + 20f (etichetta 20f x=352) = 1550; durata 460.
  - Blocco 4: 01:08 + 22f (etichetta 22f x=358) = 2062; durata 512.
  - Blocco 5: 01:22 + 25f (etichetta 24f x=268 -> 25,4) = 2485; durata 423.
- Blocchi 2-5 FATTI (10/10): B2 = 252+284 (536), B3 = 266+194 (460), B4 = 202+310 (512), B5 = 189+234 (423) fotogrammi; tagli ai confini delle frasi dal calcolo parola per parola (sync.json); file `slide/v8-b2-01.mp4` ... `v8-b5-02.mp4`; codice `code/v8b2_5.py` (usa v8b1.py). Controllati: conteggio fotogrammi con ffprobe, fotogrammi a 5%, 50%, 82%, fine di ogni file guardati a vista.
- Screenshot 10/10 (blocchi 6-10, stessa lettura: min*60+sec in fotogrammi + etichetta + (360 - x_etichetta)/67, arrotondato):
  - Blocco 6: 01:37 + 23f (etichetta 22f x=280 -> 23,2) = 2933; durata 448.
  - Blocco 7: 01:50 + 14f (etichetta 14f x=353 -> 14,1) = 3314; durata 381.
  - Blocco 8: 02:06 + 11f (etichetta 10f x=311 -> 10,7) = 3791; durata 477.
  - Blocco 9: 02:22 + 15f (etichetta 14f x=322 -> 14,6) = 4275; durata 484. (lettura 14,57: arrotondata a 15)
  - Blocco 10: 02:35 + 30f (etichetta 28f x=235 -> 29,9) = 4680; durata 405. (lettura 29,87: arrotondata a 30, cioe' 02:36+0f)
- Blocchi 6-10 (10/10): slide RENDERIZZATE (12 MP4, 2195 fotogrammi, conteggio e formato verificati), NON ANCORA CONSEGNATE. Slide 6-1: 258, 6-2: 190, 7-1: 195, 7-2: 186, 8-1: 180, 8-2: 155, 8-3: 142, 9-1: 224, 9-2: 153, 9-3: 107, 10-1: 147, 10-2: 258. Codice `code/v8b6_10.py` (comando `evt` = controllo automatico dei tempi degli elementi). Controllo a vista fotogramma per fotogramma: incompleto.
- Blocchi 6-10 CONSEGNATI (10/10): 12 MP4 (2195 fotogrammi). Controllo: `code/qa8.py` ha analizzato OGNI fotogramma (2195 su 2195, rendering dei soli elementi su nero: nulla fuori dall'area sicura, elementi completi a 80%, identici dall'81% alla fine, primo elemento entro 0,37 s, nessun buco oltre 1,9 s) = 12 slide su 12 OK; fotogramma finale di ogni slide guardato a vista; conteggio fotogrammi con ffprobe. Risultati in `code/qa_b6.json` ... `qa_b10.json`.
- Screenshot 10/10 (blocco 11): 02:54 + 3f (etichetta 2f x=310 -> 2 + (360-310)/67 = 2,75, arrotondato 3) = 5223; durata 543 (18,1 s).
- Blocco 11 CONSEGNATO (10/10): 3 MP4, 172 + 143 + 228 = 543 fotogrammi (= durata dallo screenshot). Controllo di ogni fotogramma con code/qa8.py (3 su 3 OK) + fotogrammi finali guardati a vista (corretti: freccia sul titolo, barra sul titolo, testo sugli edifici, etichette che si toccavano). Codice code/v8b11.py.
- Screenshot 10/10 (blocchi 12-15, stessa lettura: min*60+sec in fotogrammi + etichetta + (360 - x_etichetta)/67):
  - Blocco 12: 03:07 + 13f (punto fotogramma 13 a x=355) = 5623; durata 400.
  - Blocco 13: 03:23 + 28f (etichetta 26f x=249 -> 27,7) = 6118; durata 495.
  - Blocco 14: 03:39 + 12f (etichetta 12f x=355) = 6582; durata 464.
  - Blocco 15: 03:52 + 22f (etichetta 22f x=336 -> 22,4) = 6982; durata 400.
- Screenshot 10/10 (blocchi 16-40, 25 screenshot; lettura: min*60+sec in fotogrammi + etichetta + (360 - x_etichetta)/67, arrotondato .5 in su):
  16: 04:09+24f = 7494 (dur 512) | 17: 04:25+27f = 7977 (483) | 18: 04:41+19f = 8449 (472) | 19: 04:58+16f = 8956 (507) | 20: 05:15+29f = 9479 (523)
  21: 05:33+19f = 10009 (530) | 22: 05:49+15f = 10485 (476) | 23: 06:04+12f = 10932 (447) | 24: 06:22+27f = 11487 (555) | 25: 06:36+24f = 11904 (417)
  26: 06:53+15f = 12405 (501) | 27: 07:06+18f = 12798 (393) | 28: 07:17+22f = 13132 (334) | 29: 07:32+19f = 13579 (447) | 30: 07:46+22f = 14002 (423)
  31: 08:05+0f = 14550 (548) | 32: 08:20+22f = 15022 (472) | 33: 08:36+5f = 15485 (463) | 34: 08:56+8f = 16088 (603) | 35: 09:13+17f = 16607 (519)
  36: 09:31+25f = 17155 (548) | 37: 09:49+8f = 17678 (523) | 38: 10:00+0f = 18000 (322) | 39: 10:18+3f = 18543 (543) | 40: 10:28+20f = 18860 (317)
  Controllo: ogni durata e' coerente col testo del blocco (circa 16 caratteri al secondo).
- Screenshot 10/10 (blocchi 41-48, 8 screenshot): 41: 10:43+23f = 19313 (dur 453) | 42: 10:57+14f = 19724 (411) | 43: 11:19+3f = 20373 (649) | 44: 11:36+23f = 20903 (530) | 45: 11:49+9f = 21279 (376) | 46: 12:00+19f = 21619 (340) | 47: 12:12+11f = 21971 (352) | 48: 12:25+10f = 22360 (389). FINE VIDEO = 22360 fotogrammi = 12:25,3 (coerente coi ~12,3 min del copione).
- Blocchi 12-15 CONSEGNATI (10/10): 9 MP4 (12: 269+131; 13: 184+186+125; 14: 198+266; 15: 246+154 = 1759 fotogrammi, = durate dagli screenshot). Controllo di ogni fotogramma con code/qa8.py (9 su 9 OK: nulla fuori area, completo a 80%, identico dall'81%, primo elemento <= 0,43 s, nessuna pausa oltre 1,8 s) + fotogrammi finali guardati a vista. Codice code/v8b12_15.py. DA FARE: blocchi 16-48 (le fine voce sono gia' tutte in fine_blocchi.txt/sync.json).
- Blocchi 16-48 CONSEGNATI (10/10): 71 MP4 (15378 fotogrammi = durate dagli screenshot, da fine blocco 15 = 6982 a fine video = 22360). Controllo: code/qa8.py su ogni fotogramma (14989 fotogrammi dei blocchi 16-47: tutte le slide OK) + fotogrammi finali di tutte le slide guardati a vista; trovati e corretti: numeri che salgono non arrivavano al valore finale, icone sovrapposte al testo, etichette sovrapposte, numero barrato nel blocco 47. Blocco 48 = final_slide del modello (disclaimer). Codice code/v8b16_48.py. VIDEO 8: SLIDE COMPLETE (blocchi 1-48).
