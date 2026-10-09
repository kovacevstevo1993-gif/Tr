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
