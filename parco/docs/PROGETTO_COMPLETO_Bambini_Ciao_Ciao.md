# BAMBINI CIAO CIAO — PROGETTO COMPLETO + CRONOLOGIA DELLA CHAT

Da incollare nella nuova chat. Contiene tutto: regole dell'utente, cosa è stato fatto, dove sono i file, come riprendere.
Repo GitHub con tutto il codice, gli asset e i video: `kovacevstevo1993-gif/Tr`, branch `claude/lucid-volta-myb2ye`, cartella `parco/`.
Il documento originale del canale (identità, personaggi, regole Higgsfield, pubblicazioni, dati) è in `docs/Bambini_Ciao_Ciao_progetto_completo_originale.md`.

---

## 1. REGOLE DELL'UTENTE (leggerle per prime)
- Risposte **corte**, una cosa alla volta. Niente poemi, niente ripetizioni: l'utente ha un limite di utilizzo e si arrabbia se si sprecano risposte.
- **Non scansare il lavoro**: se serve fare tutto, si fa tutto. Se qualcosa non va, si cerca un'alternativa e si continua.
- **Strumenti solo gratuiti** (l'utente non ha crediti: Higgsfield finito, Google AI Studio gratis, Qwen gratis, CapCut). Dire sempre il costo prima di spendere (anche i crediti VidIQ: 5 per ricerca).
- Video **sempre verticali 9:16** (1080x1920), per Shorts. Qwen gratis produce solo video orizzontali → inutile: si usano **foto verticali** da AI Studio.
- **Finale di OGNI video**: il topolino dice dentro la scena "Bambini Ciao Ciao! Iscrivetevi al canale!" (nessuna slide separata). Fatto con pulsante "ISCRIVITI" animato nella scena.
- Voce narrante: **donna dolce** (Isabella, quella già scelta, "va bene"). I **bambini parlano solo l'essenziale** (esclamazioni tipo "Wow!", "Evviva!") + il saluto finale del topolino. Voci dei bambini diverse tra loro e più espressive.
- Obiettivo: video **il più realistici possibile**, "da professionista Disney", che attirino i bambini e possano diventare virali. Poi monetizzazione, quindi nessun problema di copyright.
- **Importante (errore ripetuto):** i file mandati dall'utente MENTRE l'assistente sta lavorando arrivano solo come anteprima e NON vengono salvati. Dire all'utente di mandare gli allegati **in un messaggio nuovo quando l'assistente è fermo**. Controllare sempre su disco prima di dire che un file c'è.
- Mai riprodurre video altrui (scene, copioni, audio): si copia solo la formula/struttura.
- Etichetta "Realizzato per bambini", categoria Istruzione, italiano, pubblicazione martedì e venerdì verso le 16.
- Il limite di invio file verso l'utente è ~30 MB: comprimere se serve.

## 2. CRONOLOGIA DI QUESTA CHAT (riassunto)
1. L'utente manda il documento del progetto e vuole fare video con l'assistente (non più con Higgsfield, ormai non disponibile). Prima proposta: 6 idee di storie (la più forte: "Puliamo il parco").
2. Sandbox: Python, ffmpeg, PIL, numpy; voce con gTTS. Fatta una bozza 100% a codice con personaggi disegnati a mano → troppo "finta".
3. L'utente genera su **Google AI Studio** (gratis) le immagini: topolino (neutro, bocca aperta, braccia alzate, triste), Chip lo scoiattolo, Spike il riccio, sfondo parco, cestini, rifiuti, tutto su verde piatto. L'assistente li ritaglia (key verde, filigrana via, logo Pepsi cancellato dalla lattina, scritte cestini in italiano).
4. Video v3 (solo topolino), v4 (tutti i personaggi veri), v5/v6 (lungo, 52 s) con camera, lip-sync, luci, voci neurali, musica sintetica originale, foley.
5. Voci: tentati gTTS → edge-tts (voci neurali Microsoft Isabella/Elsa/Diego/Giuseppe) + trasformazione con Praat per voci da bambino (altezza + formanti). Poi aumentata l'espressività (intonazione) senza cambiare le durate.
6. Domande dell'utente su copyright/monetizzazione: musica originale generata da codice (rischio Content ID basso); le voci edge-tts sono una zona grigia per uso commerciale → soluzione pulita: ElevenLabs a pagamento o Azure Speech a pagamento, oppure voci CapCut (controllare la licenza "uso commerciale"). Consigliato caricare prima come privato su YouTube Studio per i controlli.
7. Ricerca **VidIQ** (10 crediti spesi, ne restavano 160): Shorts virali di canali piccoli. Formula: emozione/aiuto/magia/sorpresa, personaggi fissi, titoli con emoji e "Cute 3D Animation", durate 11–75 s. In italiano dominano canzoni animate interattive (es. Super Wow Kids, Leo e Nubi Kids).
8. L'utente manda 2 video di riferimento (Leo puzzles, Jungle Baby drum). Analizzati: cicli di ~5 s azione→magia→reazione, ~1 taglio ogni 2 s; il secondo è un'unica inquadratura molto tenera con sguardo in camera.
9. Costruito il **motore di regia** (`engine.py`) e due Shorts nuovi: **A "La magia dei cestini"** (27,8 s) e **B "Chip e il tamburo"** (14,8 s), entrambi con finale del topolino in scena.
10. Ultimo tema: portare il realismo più in alto. Piano: (a) ambientazioni come **foto verticali** da AI Studio, (b) **pose multiple** dei personaggi (cammino, raccolta, lancio…) da AI Studio, così si anima a passi; (c) eventualmente clip video AI per le scene principali (ma l'utente non ha crediti). L'utente sta per mandare le foto delle ambientazioni e delle pose.
11. L'utente, frustrato per i troppi messaggi lunghi e per i problemi di invio file, chiede il pacchetto completo per trasferire la chat.

## 3. VIDEO PRODOTTI (in `video_finali/` e nel repo)
| File | Durata | Note |
|---|---|---|
| `short_A_magia_cestini.mp4` | 27,8 s | 3 cicli: item → cestino → magia (arcobaleno, farfalle, fiori) → reazione; finale in scena |
| `short_B_chip_tamburo.mp4` | 14,8 s | Chip cammina verso la camera, trova il tamburo, suona; arriva il topolino a salutare |
| `puliamo_il_parco_v6.mp4` | 52,4 s | Storia lunga con narratrice, finale in scena (la v5 aveva una slide finale: scartata) |
Le versioni v2/v3/v4/bozza sono vecchie: non usarle.

## 4. COME È FATTO IL PROGETTO (cartella `progetto/`)
- `engine.py` — motore: camera a inquadrature con tagli netti, lip-sync dall'ampiezza della voce, anticipazione/rimbalzo/squash&stretch, ombre, vignetta/grading, effetti (scintille, arcobaleno, farfalle, fiori, note musicali, coriandoli), pulsante "Iscriviti". Si usa con una **scena**: `SCENE=sceneA python3 engine.py full out.mp4` (anche `test 1.0 5.5` per fotogrammi di prova `test_sceneA_*.png`).
- `sceneA.py`, `sceneB.py` — copione, tempi, voci, keyframe dei personaggi, inquadrature (SHOTS), effetti.
- `render4.py` (+ `render.py` per le funzioni lerp/ease) — motore del video lungo v6: `python3 render4.py full 0 1258 out.mp4`.
- `voicegen.py` — genera le voci: narratrice (Isabella, intonazione 1.65) e bambini con Praat (topolino=Diego mediana 265 Hz formanti 1.30; Chip=Elsa 300 Hz/1.14; Spike=Giuseppe 235 Hz/1.24, intonazione ~1.4). `gen(righe, cartella)`: riga = (chi, testo[, eccitazione]). Riusa i `*_raw.mp3` già scaricati se ci sono (stessa durata, stessa sincronia). Nota: nella sandbox serve `certifi.where = lambda: "/root/.ccr/ca-bundle.crt"`; altrove va tolto.
- `mixA.py`, `mixB.py`, `mix4.py`, `mixlib.py` — audio: voci + musica sintetica originale (corde pizzicate/marimba/shaker, accordi Do-Sol-La min-Fa) + effetti (passi, whoosh, colpo nel cestino, brillantini, tamburo) + cinguettii; ducking sotto le voci.
- `prep3.py`, `prep4.py` — preparazione asset dalle immagini AI Studio (percorsi `/tmp/...` da adattare): ritaglio verde, rimozione filigrana, scritte cestini, inpainting logo lattina, **bocca aperta (2 livelli) e occhi che sbattono** dipinti su Chip/Spike/topolino.
- `assets/topo` (pose topolino ritagliate), `assets/s` (sfondo originale, Chip, Spike, cestini, rifiuti), `assets/v` (varianti con bocca/occhi). `audioA/`, `audioB/`, `audio3/` (voci finali `.wav` + `durate.json`).
- `riferimenti_analizzati/` — fotogrammi dei 2 video di riferimento.

Per rifare un video: modificare la scena → `SCENE=sceneX python3 engine.py full video_muto.mp4` → `python3 mixX.py` → `ffmpeg -i video_muto.mp4 -i mixX.wav -c:v copy -c:a aac -b:a 192k -shortest out.mp4`.
Dipendenze: `pip install pillow numpy scipy edge-tts gtts praat-parselmouth opencv-python-headless certifi` + ffmpeg.

## 5. PROBLEMI NOTI / LIMITI ONESTI
- I personaggi sono **ritagli con una sola posa**: braccia e gambe non si muovono davvero. Per il realismo servono **più pose** (cammino, raccolta, lancio, esultanza…) o clip da video-AI. È il punto da migliorare per primo.
- Chip e Spike hanno bocca (2 livelli) ed occhi dipinti sopra l'immagine: a distanza va bene, in primissimo piano si nota la patch. Bacchette e "zampette" del tamburo sono finte.
- Lo sfondo piatto del parco è una foto: il movimento è solo parallasse/zoom + particelle.
- Le voci sono sintetiche (edge-tts + Praat). **L'assistente non può ascoltare l'audio**: la valutazione la fa l'utente. Uso commerciale delle voci edge-tts = zona grigia → per la versione monetizzata rifare con ElevenLabs/Azure a pagamento (o CapCut se licenza commerciale).
- La filigrana a stellina di AI Studio è tolta dal topolino/Chip/Spike/sfondo; verificare sempre le nuove immagini (compare in basso a destra).
- Il video lungo v6 usa ancora il vecchio motore (`render4.py`); A e B usano `engine.py`.

## 6. PROMPT GIÀ DATI ALL'UTENTE (AI Studio, gratis, foto verticali 9:16)
**Blocco stile:** `Pixar-style 3D animated children's cartoon environment, soft warm sunlight coming from the upper left, smooth rounded shapes, vibrant pastel colors, cute and friendly. A clean, empty, open ground area in the lower half of the image where cartoon characters can stand. Horizon line at 45% from the top. No characters, no people, no animals, no text, no logos, no watermark. Vertical 9:16 image.`
**Scene (una alla volta):** parco con fiori; spiaggia; cucina; bosco; cameretta di sera; aula dell'asilo; parco giochi; fattoria; orto; neve.
**Pose (con il personaggio come riferimento, sfondo verde #00FF00, stessa inquadratura e piedi alla stessa altezza):** cammina piede sinistro avanti / piede destro avanti; si china a raccogliere; tiene un oggetto all'altezza della pancia; lancia con il braccio indietro; saluta con la mano alzata; sorpreso con bocca a "O"; ride con braccia alzate. Poi lo stesso per Chip e Spike.
(Prompt negativo, se il programma ha il campo: `characters, people, animals, text, logos, watermark, camera movement, zoom, pan, shaking, blurry, distorted`. Se non c'è, non serve.)

## 7. PROSSIMI PASSI
1. Ricevere (come allegati, assistente fermo) le **foto di ambientazioni** e le **pose** dei personaggi; controllare filigrane e verde.
2. Ritagliare le pose (`prep3/prep4`) e fare un **ciclo di camminata** vero alternando le pose; collegare raccolta/lancio/saluto alle pose giuste nel motore.
3. Rifare Short A/B e il lungo con più ambientazioni (cucina, spiaggia, asilo, camera di sera…). Storie da fare: primo giorno all'asilo, paura del buio, condividere il giocattolo, il coniglietto triste, versi degli animali.
4. Micro-Short da 11–15 s (formato che ha fatto più visualizzazioni nei riferimenti) e serie con personaggi fissi.
5. Prima di pubblicare: carica **privato** su YouTube Studio per i controlli copyright; titoli con emoji e "Cute 3D Animation"; Realizzato per bambini; Istruzione.
6. Per le voci definitive: ElevenLabs (o CapCut con licenza commerciale) → mandare i file audio → l'assistente li monta (il lip-sync si ricalcola dalle voci).

## 8. COME RIPRENDERE NELLA NUOVA CHAT
Scrivere: "Riprendi il progetto Bambini Ciao Ciao: leggi `PROGETTO_COMPLETO_Bambini_Ciao_Ciao.md` e la cartella `parco/` del repo `kovacevstevo1993-gif/Tr`, branch `claude/lucid-volta-myb2ye`. Rispetta le regole della sezione 1." Poi allegare il file `.md` e lo zip `progetto_codice_asset_audio.zip`.
