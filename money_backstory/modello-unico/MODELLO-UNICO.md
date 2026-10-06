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
