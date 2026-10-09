# MODELLO UNICO slide — The Money Backstory (06/10/2026)
Regola dell'utente: i video devono essere fatti tutti allo stesso modo. Da qui in poi (video 8 in poi) si usa SOLO questo modello. Video 1-7 restano come sono (consegnati/pubblicati).

## Codice
- `modello_unico.py` = libreria unica (percorsi relativi al repo, nessun percorso della vecchia chat). Si importa con `from modello_unico import *`.
- Ogni nuovo video: un file `v8b1_5.py` ecc. con `SPEC` (fotogrammi per slide, la SOMMA = durata del blocco letta dallo screenshot dell'utente), `SLIDES`, e `run(SPEC, SLIDES, 'v8', OUT)`.
- Comandi: `python3 v8b1_5.py preview 3` (4 fotogrammi: 25%, 50%, 80%, 97%), `check 3` (conta i pixel che cambiano dopo l'84%: deve essere ~0), `render 3`.
- Esempio funzionante: `test_modello.py`.

## Standard fissi (uguali in ogni video)
- Sfondo, cornice oro 3D, particelle: `stage()` (stesso per tutti).
- Titolo: Gloock oro, centrato in alto (y=90), size 56-64, maiuscolo, breve.
- Corpo: card/equazioni/barre/anelli con le funzioni `card_`, `eq`, `bars3`, `ring_`, `tracker`, `numcard`; testi >= 44 px (card piccole: >= 34), oggetti disegnati in ogni slide.
- Tempi: `sp(n)` distribuisce n elementi da 0,07D fino all'80% di D; l'ULTIMO elemento e' sempre la pillola-didascalia `pill_last()` (y=800, size 50-54) che compare all'80% e resta ferma fino alla fine.
- Fonte ufficiale: `chip_src()` in basso (y=920).
- Slide finale disclaimer: `final_slide()`, identica in ogni video lungo (IMPORTANT + 3 gruppi di testo + WATCH NEXT + SUBSCRIBE).
- Loghi/font: solo file veri del repo (`kit-02-10/06-immagini/logo/logo-the-money-backstory-pro2.png`, `kit-02-10/08-font`).
- Controllo prima di consegnare: `check`, poi fotogrammi a inizio, meta', 80%, fine di OGNI mp4 guardati a vista; conteggio fotogrammi = SPEC.
- Durate: SOLO dagli screenshot della timeline dell'utente (fine voce di ogni blocco).

## SINCRONIA CON LA VOCE (obbligatoria dal video 8)
- Serve l'AUDIO della voce (tutto il video, mp3/wav/mp4 esportato da CapCut). Senza audio non si fanno le slide.
- `python3 sync_voce.py voce.mp3 copione.md sync.json fine_blocchi.txt` misura quando la voce dice ogni parola (faster-whisper in locale, gratis, nessun credito). `fine_blocchi.txt` = fine voce in fotogrammi dagli screenshot dell'utente (una riga per blocco).
- `Voice(sync.json).plan(blocco, n)` propone SPEC: tagli delle slide ai confini delle frasi, somma = durata del blocco.
- Nelle slide: `cue('parola chiave del copione')` = istante in cui la voce la dice (mai oltre l'80%); ogni elemento compare con il suo cue, la didascalia finale con l'ultimo.
- `test_sync.py` = esempio funzionante, provato con una voce di prova (copione video 7, blocchi 1-3: 84% parole agganciate, le altre sono i numeri scritti in lettere e vengono interpolate).
- Dopo il render: a vista i fotogrammi dei punti in cui la voce dice le parole chiave (la slide deve gia' mostrare l'oggetto).

## SENZA AUDIO (10/10/2026, ordine dell'utente): sincronia CALCOLATA
- `python3 calcola_sync.py copione.md fine_blocchi.txt sync.json` (fine_blocchi.txt = fine voce in fotogrammi dagli screenshot, una riga per blocco). Calcola il tempo di ogni parola (sillabe + pause) scalato sulla durata del blocco.
- Nel codice del blocco: `V = Voice('sync.json')`, `tm('parola')` = istante in cui la voce dice la parola (clampato prima dell'ultimo elemento), `V.plan(blocco, n)` = tagli delle slide ai confini delle frasi, `frozen(fn)` = elementi e testi fermi dall'80%, MA sfondo e particelle dietro continuano a muoversi (`stage_live`). Esempio: `video8-bills-after-65/code/v8b1.py`.
- Verifica fatta (10/10): 80% = ultimo elemento completo; dopo l'81% gli elementi restano identici (posizioni uguali al fotogramma finale) e solo lo sfondo (banconote, monete, punti) continua a muoversi. Errore corretto: la prima versione congelava anche lo sfondo, e l'utente ha detto che non si muoveva niente dietro.
