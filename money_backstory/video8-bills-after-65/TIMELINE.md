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
