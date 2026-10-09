# BAMBINI CIAO CIAO — PASSAGGIO DI CONSEGNE v5 (3 ottobre 2026, notte)

Completa `PASSAGGIO_Bambini_Ciao_Ciao_v4.md` (che resta valido: leggerlo PRIMA, poi questo). Qui c'è solo ciò che è NUOVO e le regole che l'utente ha aggiunto in questa chat.
Repo: `kovacevstevo1993-gif/Tr` — **branch da usare: `claude/festive-brown-pk4m7q`** (contiene TUTTO: v4 + elefantino + Short "castello di sabbia"). Cartella: `parco/`.
Documenti da leggere in ordine: `docs/Bambini_Ciao_Ciao_progetto_completo_originale.md`, `docs/PROGETTO_COMPLETO_Bambini_Ciao_Ciao.md`, `docs/PASSAGGIO_Bambini_Ciao_Ciao_v3.md`, `docs/PASSAGGIO_Bambini_Ciao_Ciao_v4.md`, questo.

---

## 1. NUOVE REGOLE DELL'UTENTE (hanno la precedenza su v4)
1. **Miniatura: SOLO VERTICALE 1080x1920.** Niente orizzontale: non generarla, non mandarla (l'utente si è arrabbiato). Consegna = video + miniatura verticale + `.srt` + testi in chat.
2. **Controllo qualità: raccogliere TUTTI gli errori prima, poi UN SOLO rendering.** Mai rifare il video completo a ogni errore (ogni rendering ~7 min; in questa chat ne ho fatti 5 e l'utente ha sbottato: "ci stai mettendo più di un'ora"). Metodo: render → controllo completo (fogli ogni 0,5 s + finestre a 0,1 s sui punti critici) → elenco di TUTTI i difetti → correggerli tutti insieme → un solo render finale → controllare solo le zone corrette. Per anteprime usare `python3 short_castello.py test <secondi...>` (6 s) o il `strip.py` (vedi §4), non il render completo.
3. **Il controllo va fatto PRIMA di mandare** il video, non dopo. Mandare solo quando è perfetto.
4. **Personaggi: si possono aggiungere/alternare.** Ora c'è un quarto personaggio, **l'elefantino** (originale, stesso stile 3D). Si alternano da video a video (non tutti sempre). Un nuovo personaggio si crea una volta sola come "scheda" e poi si fanno le pose in image-to-image dalla scheda (vedi §3).
5. **Più fluido, più 3D, ogni video migliore del precedente**: più pose di passaggio, luce/ombre, ambienti animati, personaggi che fanno ESATTAMENTE ciò che dice la narrazione, oggetti al posto giusto.
6. **Pochi crediti Pollinations**: una prova, poi la serie; non rigenerare ciò che c'è già (`ls assets/*`). 402 = saldo finito → fermarsi e dirlo (l'utente a volte ricarica e dice "prova adesso").
7. Risposte **corte**; mai messaggi lunghi; un'azione alla volta; l'utente scrive diretto e a volte con parolacce quando si spreca tempo: rispondere con fatti, scusarsi in una riga e correggere.
8. Messaggi arrivati mentre si lavora: leggerli e adeguarsi subito (non ignorarli).
9. Sempre: VidIQ NO, Higgsfield non disponibile, video 9:16, finale con topolino "Bambini Ciao Ciao! Iscrivetevi al canale!" + pulsante ISCRIVITI in scena, hook nei primi 2 s, voce narrante Isabella, bambini battute di 1–3 parole, testi SEO scritti direttamente nella chat (blocchi da copiare).

---

## 2. COSA È STATO FATTO IN QUESTA CHAT
- Letti repo e documenti; prova Pollinations OK (ambiente spiaggia; HTTP 200). Il saldo è finito una volta a metà e poi è tornato.
- **Nuovo personaggio ELEFANTINO** (pelle grigio-azzurra, orecchie enormi rosa dentro, proboscide corta, maglietta corallo con stella bianca, pantaloncini viola, scalzo). Scheda: `assets/s/ele.png`. **17 pose** `assets/pose/ele_*.png`: neutro, cammina_dx, passa_dx, tiene, saluta, saluta2, indica, sorpreso, ride, salto, balla, batte_sabbia, riempie, spruzza, spruzza_giu, parla_a, parla_o. Il prompt per `ele` contiene una frase rinforzata sulla proboscide (senza di essa Pollinations la toglie e viene un topo con orecchie grandi) — è in `pose_pollinations.py` (`chiedi`).
- Pose nuove anche per topolino e Chip: `passa_dx` (passaggio camminata), `batte_sabbia`; topolino: `fuggi`, `triste` (già c'era l'originale).
- **Ambienti nuovi** (`assets/amb/`): `spiaggia`, `spiaggia_baia`, `spiaggia_tramonto` (le ultime due derivate dalla spiaggia per coerenza: si può passare un ambiente di riferimento come 3° elemento della tupla in `ambientazioni_pollinations.py`).
- **Oggetti nuovi** (`assets/obj/`): bucket, shovel, castle_small, castle_big, sand_heap, seagull.
- **Voci**: `voci_castello.py` (audioG/), tutte verificate con trascrizione (tutte ✓).
- **Short "Il castello di sabbia"** (45,9 s, 30 fps): `short_castello_di_sabbia.mp4`. Storia: il topolino costruisce un castello → onda gigante lo distrugge ("Splash!", fuga, triste) → arriva l'elefantino (corre, saluta) → riempie il secchiello con la proboscide e spruzza sull'impasto → cerchio magico → baia: costruiscono un castello altissimo a scatti, Chip lancia la bandiera, grande getto + arcobaleno → cerchio magico → tramonto: ballano e chiusura "Bambini Ciao Ciao! Iscrivetevi al canale!" + ISCRIVITI.
- Consegnati: video, miniatura verticale (`miniatura_castello_1080x1920.jpg`), `sottotitoli_castello.it.srt`, testi SEO (`docs/SEO_castello_di_sabbia.md`). (La miniatura orizzontale `miniatura_castello_1280x720.jpg` esiste ma NON va più mandata.)

---

## 3. COSA È CAMBIATO NEL MOTORE (usare `short_castello.py` come base per i prossimi Short — è il più avanzato)
- **30 fps** (prima 24).
- `morph.py`: K=8 intermedi, e **`SHARP(t)`**: niente doppia esposizione (A fino a metà, B dopo, sfumatura stretta) → addio "fantasmi" tra pose diverse. Cache in `/tmp/claude-0/morph_cache8s` (si rigenera con `prep`, ~25 s).
- `pair_dur()`: la durata della transizione dipende da quanto cambia la sagoma (IoU): 0,22 s se simili, 0,14, 0,09 s se molto diverse.
- **Camminata a 4 pose** (`cammina_dx, passa_dx, cammina_dx_m, passa_dx_m`) con passo alternato, rimbalzo e rotazione.
- **Luce e volume dei personaggi**: ombra proiettata (sagoma deformata, sfocata), macchia di contatto, tinta dell'ambiente, **luce di bordo (rim light)**, leggero ombreggio verso i piedi; vignettatura.
- **Camera**: sempre in basso (`cy=1900`, la camera si blocca al bordo) con zoom lento; piccoli shake sugli eventi.
- **Acqua**: `stream()` (getto balistico con scia e gocce), `splash()`, `fountain()`; `water_sheet()` (acqua sulla sabbia con rumore, schiuma al fronte, sabbia che si bagna), `crest()` (cresta dell'onda sul mare).
- Mare che ondeggia (`sway`), riflessi che scintillano, schiuma che respira sulla battigia, gabbiani, barca che dondola, palme nel vento, raggi di sole al tramonto.
- Bandiera che vola e si pianta; oggetti con scala/rimbalzo (`back()`); castello che cresce a scatti con polvere e scintille.
- Se una posa non esiste per un personaggio: `ALIAS` + `rp()` la sostituisce (utile quando i crediti finiscono).
- Mix audio: `mix_castello.py` (musica sintetica + effetti sincronizzati: onda, getti, trombetta dell'elefantino, passi, sabbia battuta, costruzione, bandiera, arcobaleno).
- Miniatura: `miniatura_castello.py` (solo la funzione `tall()` serve; `wide()` non va usata).

Rendering tipo (~7 min):
```
python3 voci_castello.py && python3 short_castello.py prep && python3 mix_castello.py
python3 short_castello.py render muto_c.mp4
ffmpeg -y -i muto_c.mp4 -i mix_castello.wav -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest out.mp4
```
Pulire i file temporanei prima del commit (muto_c.mp4, mix_castello.wav, test_c_*.png, versioni intermedie).

---

## 4. METODO DI CONTROLLO (usato e funzionante)
- `ffmpeg -i v.mp4 -vf "fps=2,scale=300:533" qa/f_%03d.png` → fogli da 12 fotogrammi con il tempo scritto sopra, **guardarli tutti in ordine**.
- `ffmpeg -i v.mp4 -vf "fps=10,scale=216:384" qb/f_%04d.png` → finestre da 16 fotogrammi (1,6 s) sui punti critici: cambi di posa, arrivo personaggi, onda, getti, cerchi magici, camminate, ballo, finale.
- Ingrandire con `-ss <t> -frames:v 1` + crop quando serve (es. transizione di posa dell'elefantino).
- Controlli numerici utili: IoU tra pose (`morph.aligned`) per prevedere i fantasmi.
- Cercare: personaggi tagliati, sovrapposizioni, oggetti non alle mani, testi coperti o fuori campo, fotogramma finale, effetti a righe, ordine di disegno.
Difetti trovati e corretti in questo Short (per non ripeterli): hook troppo largo e sovrapposto ai sottotitoli; onda come poligoni piatti; doppia esposizione tra pose; secchiello che copriva l'elefantino; paletta sotto i piedi di Chip; personaggi troppo grandi che sfioravano i bordi; testo "L'ONDA!" minuscolo a t=0 (ora compare dopo 0,4 s).

---

## 5. TRAPPOLE NUOVE
- Un'ambientazione generata come "spiaggia" a volte ha il pavimento di parquet: il prompt deve dire "smooth flat golden sand… no wood, no planks, no tiles".
- Per il nuovo personaggio-animale serve ripetere nel prompt le sue parti distintive (proboscide) a ogni posa.
- Il verde chiave per oggetti: usare `magenta=True` solo per cose verdi; il secchiello e la pala vanno col verde normale.
- Non usare `sleep` lunghi nel terminale (bloccati): usare `until <condizione>; do sleep 3; done` con `run_in_background` o `timeout` alto.
- Non usare `pkill -f`/`ps | grep` col proprio nome: usare `awk '/nome/ && !/awk/'`.
- Hook "stop": se compare "uncommitted changes", committare e pushare subito.

---

## 6. PROSSIMI PASSI
1. Verificare il saldo Pollinations con UNA generazione.
2. Nuovo Short (alternare i personaggi; non serve usarli tutti): idee già pronte — primo giorno all'asilo, paura del buio (camera_sera + lucciole), condividere il giocattolo, versi degli animali, aquilone sulla collina, tempesta e arcobaleno. Ambiente diverso ogni 10–12 s.
3. Ancora da migliorare (dichiarato onestamente): bocca a 2–3 stati e niente occhi che sbattono; ambienti senza vera parallasse a più livelli; il ballo ripete due pose; il getto d'acqua è disegnato (non 3D); mancano ancora pose di passaggio per salto/atterraggio e per Chip/Spike nella camminata a 4 pose.
4. Per ogni video: video, **miniatura verticale** (sola), `.srt`, testi SEO in chat (titolo, descrizione, hashtag, tag), file in repo, commit+push sul branch.
5. Prima di pubblicare: caricare PRIVATO su YouTube Studio; "Realizzato per bambini"; categoria Istruzione; martedì/venerdì ~16.

---

## 7. MESSAGGIO DA INCOLLARE NELLA NUOVA CHAT
```
Riprendi Bambini Ciao Ciao.
Leggi nel repo kovacevstevo1993-gif/Tr, branch claude/festive-brown-pk4m7q, questi file in ordine: parco/docs/PASSAGGIO_Bambini_Ciao_Ciao_v4.md, poi parco/docs/PASSAGGIO_Bambini_Ciao_Ciao_v5.md (le regole del v5 hanno la precedenza), e i documenti che citano.
Regole chiave: risposte corte; niente VidIQ; solo miniatura VERTICALE (mai orizzontale); raccogli TUTTI gli errori prima e fai UN solo rendering; controlla il video fotogramma per fotogramma PRIMA di mandarlo; pochi crediti Pollinations (controlla il repo prima di generare); personaggi esistenti: topolino, Chip, Spike, elefantino (si alternano, niente personaggi nuovi senza chiedere).
Fai prima UNA generazione di prova Pollinations, poi un nuovo Short con una storiella diversa, ambienti diversi e animati, personaggi che fanno quello che dice la narrazione, migliore del "Castello di sabbia" (usa short_castello.py come base). Poi miniatura verticale, titolo, descrizione, hashtag, tag e sottotitoli.
```
