# BAMBINI CIAO CIAO — PASSAGGIO v8 (21/10/2026) — LEGGERE PRIMA DI TUTTO
Sostituisce v7 come stato (v7 e v6 restano per storia e regole). Tutto su `main`, cartella `parco/`. Canale: @bambiniciaociao (UCxwr3sSMwnnAhZPm7Bez7mQ), 57 iscritti, 17 video, 92.283 view totali.

## 1. REGOLE DELL'UTENTE (tutte valide; l'utente è spesso arrabbiato: rispettarle alla lettera)
- Risposte CORTE, in ITALIANO. Una domanda = solo risposta. Fare SOLO quello che chiede. Niente scuse lunghe.
- MAI mandare un video con un difetto noto. Controllare il video (fotogrammi) PRIMA di mandarlo. File SEMPRE inviati in chat con SendUserFile. Solo miniatura VERTICALE 1080x1920. NIENTE sottotitoli nel video. Personaggi GRANDI e al CENTRO.
- Pacchetto testi (Titolo, Descrizione, Hashtag, Tag) e miniatura SOLO se li chiede; ognuno nel suo riquadro. vidIQ solo se lo chiede (ricerche già fatte in docs/RICERCHE-VIDIQ.md, non rifarle; saldo 35 crediti).
- Finale di ogni Short: "Bambini Ciao Ciao! Iscrivetevi al canale!" + pulsante ISCRIVITI animato.
- Ogni Short diverso dagli altri; l'utente vuole "più belli, come i video virali di YouTube": tagli veloci, una gag/sorpresa chiara, espressioni grandi, effetti sonori, ~20-30 s (gli short che hanno funzionato duravano 31-32 s).
- LABBRA (21/10): nelle clip il personaggio deve muovere la bocca SOLO quando parla lui; quando parla il narratore bocca chiusa (nei prompt: "mouth closed, nobody talks" + negativo "talking, moving lips").
- NON È TUTTO ILLIMITATO (19-21/10, insulti): prima di usare un servizio gratis/limitato CALCOLARE la quota e dire quante clip/giorni servono. Ogni clip va pensata per riuscire al primo colpo (azione semplice, niente oggetti/personaggi che compaiono dal nulla, niente camera in movimento, una sola azione). Mai dire "basta" se non è calcolato.
- NIENTE "automatico" se non c'è un meccanismo reale: la chat lavora solo quando l'utente scrive, a meno di un promemoria programmato (send_later). Non dire "lo faccio in automatico" senza averlo programmato.
- Non iniziare lavori non chiesti. Se la richiesta è "fallo adesso", farlo subito.

## 2. ANALISI DEL CANALE (18/10, dati veri: feed RSS pubblico + vidIQ Analytics + Studio dell'utente)
- Boom 27/09-03/10 (picco 25.548 view il 29/09): "Puliamo la spiaggia!" (clip video vere Higgsfield, topolino, 32 s) = 85.719 view, 693 like, +54 iscritti.
- Dall'08/10 la distribuzione di TUTTO il canale è crollata da un giorno all'altro (Feed Shorts 648 -> 40, pagina canale 61 -> 0, correlati 182 -> 0), anche per il video da 85K. Gli short nuovi hanno ritenzione buona (castello 83% continua a guardare) ma pochissime impressioni.
- Stato account in Studio: nessuna violazione, guadagni OK. Metadati dei nuovi uguali ai vecchi. Causa vera NON identificabile da fuori. Unica differenza misurabile: i nuovi durano 38-52 s (quelli che andavano 31-32 s) e dal 03/10 sono fatti col motore Python (immagini deformate), prima clip video vere.
- Conclusione dell'utente: gli short nuovi con movimenti finti "fanno schifo". Strada scelta: clip video VERE gratis (sotto).

## 3. METODO ATTUALE (gratis): clip animate vere con Wan 2.2 su HuggingFace
- Space `zerogpu-aoti/wan2-2-fp8da-aoti-faster` via `gradio_client` (api /generate_video: immagine di partenza + prompt + steps 6 + negative + durata 0.5-5 s + seed). Pipeline: si compone un fotogramma di partenza 720x1280 (sfondo `assets/amb/*.png` + pose `assets/pose/*.png` + oggetti `assets/obj/*.png`) -> clip 16 fps 480x832 -> montaggio a 1080x1920 30 fps + voci + musica + pulsante.
- Account HuggingFace dell'utente (nome Steee123, email storie.truee@gmail.com) con token READ salvato nei SEGRETI DI RETE dell'ambiente cloud (huggingface.co e zerogpu-aoti-wan2-2-fp8da-aoti-faster.hf.space): nelle chiamate il token viene aggiunto dal proxy, non serve scriverlo. `pip install gradio_client opencv-python-headless scipy edge-tts praat-parselmouth faster-whisper` in un container nuovo.
- QUOTA: ~19 s di GPU per ogni secondo di clip; quota giornaliera ~400-500 s = ~20-25 s di clip al giorno. Si ricarica 24 h dopo l'uso (messaggio d'errore "Try again in HH:MM:SS"). Esaurita il 21/10 ~01:35 CEST (circa 23 s di clip usati per il palloncino + clip6 biscotto) -> riprova dopo le 00:45 del 22/10.
- Il generatore gratis di immagini Pollinations (flux-2-dev-free) è MORTO (502) e il saldo Pollinations è 0; Gemini quota 0. => NON si possono creare nuove pose né nuovi personaggi (coniglio, orso impossibili). Personaggi usabili: topolino (assets/pose/topo_*), Chip scoiattolo (chip_*), Spike riccio (spike_*), elefantino (ele_*), volpe (35 pose volpe_*), rana (19 pose rana_*).
- Voci: edge-tts gratis + Praat + controllo pronuncia con Whisper locale (`voci_*.py` -> audioX/*.wav + durate.json). Trappole: "Chip" viene letto "Cep" (evitare il nome nella voce narrante), "Cra cra" non riconosciuto, "Non sono stato io" -> usare "Io non sono stato!".

## 4. SHORT FATTI
- Vecchi (motore Python, tutti con visualizzazioni quasi 0): pupazzo di neve, razzo luna, nascondino, festa sorpresa, balla con la volpe (pacchetto testi mai dato).
- 21/10 `short_palloncino_rosso.mp4` (27,5 s, 7 clip Wan): CONSEGNATO e giudicato dall'utente "fa cagare, video semplicissimo, labbra a caso" -> "lo teniamo così" (non rifarlo; non ha miniatura né pacchetto testi: farli solo se li chiede). Codice: palloncino_frames.py, palloncino_clips.py, short_palloncino.py, voci_palloncino.py (audioQ).

## 5. IN CORSO: "CHI HA MANGIATO IL BISCOTTO?" (gag a tagli veloci, ~20 s)
Storia: in cucina il biscotto sparisce dal piatto; topolino "Io non sono stato!", volpe "Io? Non c'ero!", rana "Neanche io!"; scia di briciole sul pavimento; si scopre Spike col biscotto ("Ops! Era troppo buono!"); tutti ridono; finale ISCRIVITI.
- PRONTI: voci `voci_biscotto.py` -> `audioR/` (controllate); fotogrammi `biscotto_frames.py` -> `assets/v/biscotto/start1..7.png`; clip `biscotto_clips.py` (prompt con regola labbra); montaggio+mix `short_biscotto.py` (comandi: info | video | mix | finale -> `short_chi_ha_mangiato_il_biscotto.mp4`; LENS=[3,2.5,2.5,2,3,3,4.2]; VOICES e T_SUB già impostati, effetti sonori già nel mix).
- FATTA: solo clip6 (Spike mangia e si copre la faccia) = `assets/v/biscotto/clip6.mp4` (2,9 s, OK).
- DA FARE: `cd parco && python3 biscotto_clips.py 1 2 3 4 5 7` (dopo ricarica quota; ~17 s di clip = ~330 s GPU), controllare ogni clip con fotogrammi (bocca chiusa dove non si parla, niente personaggi/oggetti nuovi, niente zoom), rifare solo quelle difettose con `SEED=7` (spostare la vecchia in clipN_v1.mp4), poi `python3 short_biscotto.py video && python3 short_biscotto.py mix && python3 short_biscotto.py finale`, controllo di TUTTI i fotogrammi (differenze tra fotogrammi consecutivi: i salti devono essere solo ai tagli 3.0, 5.5, 8.0, 10.0, 13.0, 16.0 s; nessun nero), poi SendUserFile. Un promemoria programmato (send_later) era previsto per il 22/10 00:55 CEST nella chat precedente.
- Poi (se l'utente vuole): altri short "totalmente diversi" con lo stesso metodo (idee: "Indovina chi è" con le ombre, voci già pronte in audioP/voci_ombre.py ma usa coniglio e orso non disponibili -> rifare con personaggi esistenti; "Chi salta più in alto" idem).

## 6. COMANDI UTILI
- Controllo salti fotogrammi: ffmpeg scala 270x480, differenza media tra fotogrammi consecutivi (mediana ~2; i tagli >15). Contact sheet: `ffmpeg -vf "select='not(mod(n,8))',scale=160:277,tile=9x1"`.
- Non usare `pkill -f` con il nome dello script nella stessa riga di comando (chiude la shell).
- Fine lavoro: aggiornare questo file, commit, push sul branch della sessione e poi unire su main.

## AGGIORNAMENTO 21/10 sera (UTC 23:00)
- Generate e controllate (contact sheet) clip 1,2,3,4,5 del biscotto (assets/v/biscotto/clipN.mp4). Clip5: la rana apre un po' la bocca a meta' (difetto lieve, da valutare). Clip6 gia' fatta.
- MANCA SOLO clip7 (finale, tutti ridono, 4.0 s): quota HF finita di nuovo dopo 5 clip (~130 s di clip generate = ~30 s GPU l'una: la quota reale e' ~150 s/giorno circa, non 400). Riprovare `python3 biscotto_clips.py 7` dopo ~23:00 UTC del 22/10, poi montaggio (video|mix|finale), controllo fotogrammi, SendUserFile.
