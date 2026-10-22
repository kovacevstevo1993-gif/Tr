# BAMBINI CIAO CIAO — PASSAGGIO v7 (18/10/2026) — leggere PRIMA di tutto
Tutto il progetto è su `main`, cartella `parco/`. Prima leggere questo file, poi `docs/PASSAGGIO_Bambini_Ciao_Ciao_v6_regole.md` (regole aggiunte 14-18/10), poi v5 e v4 (storia e motori vecchi).

## 1. REGOLE DELL'UTENTE (tutte valide, le ultime hanno la precedenza)
- Risposte CORTE. Rispondere SOLO a quello che chiede: una DOMANDA = solo risposta, mai iniziare lavori non chiesti (18/10 si è arrabbiato: chiedeva del pacchetto testi e ho iniziato a rifare il video).
- MAI mandare un video/pacchetto con un difetto noto: prima si corregge, poi si manda. Mai dire "perfetto/pronto" se non è vero.
- File (video, miniatura) SEMPRE inviati in chat con SendUserFile. Solo miniatura VERTICALE 1080x1920. .srt solo se lo chiede.
- NIENTE sottotitoli nel video. Personaggi GRANDI e al CENTRO (niente metà alta vuota).
- Movimenti naturali e realistici "come nei video normali": servono TANTE pose vere (20-35 per personaggio), non 3-4. Una posa ferma con deformazioni = "foto di passaggio" (bocciato).
- Ogni Short diverso dagli altri (storia, ambienti, regia). "Fai tutto te": decidere storie e regia da soli e consegnare.
- Controllare il video fotogramma per fotogramma PRIMA di mandarlo; un solo rendering, correzioni con renderpart.
- Pacchetto testi in chat, ognuno nel suo riquadro: Titolo, Descrizione, Hashtag, Tag. vidIQ: solo se lo chiede (ricerche salvate in docs/RICERCHE-VIDIQ.md — non rifarle).
- Finale di ogni Short: "Bambini Ciao Ciao! Iscrivetevi al canale!" + pulsante ISCRIVITI animato.

## 2. IMMAGINI GRATIS (saldo Pollinations klein = 0, Gemini quota 0)
- `pose_free.py <chi> [pose]`: modello GRATIS `community/scriptsnsenses-sys/flux-2-dev-free`, SEED fisso 42, descrizione del personaggio identica, cambia solo la posa, UNA richiesta ogni ~15 s (dà errori 400 se troppo veloce: lo script riprova). 35 pose nel dizionario POSES. Personaggi nel dizionario CHARS: volpe (35 pose FATTE), rana (19 fatte, da finire), coniglio, orso (da fare). Lancio: `nohup bash -c 'for c in rana coniglio orso; do python3 pose_free.py $c; done' &` (salta quelle già fatte). Limite noto: la tonalità della maglietta può variare un po' tra le pose.
- `neve_free_pollinations.py <nome>`: ambienti e oggetti gratis (dizionario ITEMS).
- I modelli gratuiti NON usano un'immagine di riferimento: i personaggi vecchi (topolino, Chip, Spike, elefantino) NON si possono rigenerare in pose nuove gratis; hanno solo le pose già in assets/pose.
- Voci: edge-tts (gratis) + controllo pronuncia con Whisper LOCALE (`trascrivi.py` passa da solo a faster-whisper se Pollinations dà 402). Trappole: "Etciù"->"Ecciù", "Tocca a me"->"Adesso io", "Guardate me"->"Guarda che salto", "Zitti"->"Silenzio", "la ranocchia" letta "l'aranocchia" (n5 di voci_trenino.py ancora da sistemare).

## 3. MOTORI
- `attori.py` (CLASSE Attore) + `short_balla2.py` = il più avanzato: tante pose vere fuse col morph + "corpo vivo" (testa, respiro, peso, squash nei salti, ombra, luce di bordo). USARE QUESTO come base.
- `short_razzo.py` (motore 15/10 senza sottotitoli), `short_nascondino.py`, `short_festa.py` (importano short_razzo), `short_neve.py`, `short_mongolfiera.py` (vecchi).
- `rig.py` (marionetta da un'immagine): provato, scartato (sembra finto).
- Mix audio: mix_*.py (mixlib). Miniature: miniatura_*.py (outline_text, sparkle). Render ~4-7 min per 45 s con 4 core.

## 4. SHORT FATTI (video in parco/, SEO in docs/SEO_*.md)
- 14/10 short_pupazzo_di_neve.mp4 — 15/10 short_razzo_luna.mp4, short_nascondino.mp4 (volpe vecchia a UNA posa: l'utente l'ha criticata; pacchetto SEO aggiornato con vidIQ il 18/10), short_festa_sorpresa.mp4 — 16-18/10 short_balla_volpe.mp4 (volpe nuova 35 pose; pacchetto testi NON ancora dato in chat).

## 5. PROSSIMI PASSI (ordinati dall'utente)
1. Finire le pose di rana, coniglio, orso (pose_free.py).
2. Short con gli animali nuovi, voci GIÀ pronte e controllate: `voci_salti.py` (audioN, "Chi salta più in alto?" allo stagno), `voci_trenino.py` (audioO, "Il trenino degli animali", contare; n5 da correggere), `voci_ombre.py` (audioP, "Indovina chi è", ombre). Ambienti da generare (stagno, binari/campagna, sfondo ombre).
3. Poi "altri 2 short migliori e totalmente diversi".
4. Pacchetto testi di "Balla con la volpe" quando lo chiede.

## 6. ANALISI CANALE 18/10 (dati pubblici, gratis: feed RSS + pagina Shorts; 57 iscritti)
- Fino al 29/09 (clip video vere, 25-35 s, topolino): 387-509 view, Versi animali 3.378, Puliamo la spiaggia 85.709.
- Dal 03/10 (motore Python: immagini ferme deformate, 40-52 s, personaggi nuovi ogni volta): barattolo 17, seme 28, castello 10, mongolfiera 5, neve 5, razzo 1, nascondino 0.
- Cause probabili: movimento "da foto" (chi scorre se ne va subito, YouTube smette di mostrarli), durata troppo lunga, personaggio ricorrente (topolino) sparito. Per confermare servono le statistiche di Studio dell'utente ("ha continuato a guardare / ha scorso via", fonti di traffico).
- 18/10 screenshot Studio: Stato account = nessuna violazione, guadagni OK. Castello di sabbia: "ha continuato a guardare" 83,3% (buono) ma pochissime impressioni -> non è che scorrono via: YouTube non lo propone proprio. Causa non visibile da fuori.
- 18/10 utente: "Falli più naturali i movimenti, così fanno schifo... guarda come si fa" + "Gratis". Gli short che funzionavano = clip video vere (Higgsfield Seedance, a pagamento: NO). Strada GRATIS trovata: Space HuggingFace `zerogpu-aoti/wan2-2-fp8da-aoti-faster` (Wan 2.2 immagine->video, gradio_client, api /generate_video, clip 4 s). Senza account: "exceeded ZeroGPU runs limit" -> serve token HF GRATUITO come variabile d'ambiente HF_TOKEN. Pollinations non ha più flux-2-dev-free (502). Gemini immagini/Veo quota 0.
- 18-19/10 SHORT "Il palloncino rosso" (topolino + Chip, ~35 s, clip Wan 2.2 gratis): voci audioQ OK (voci_palloncino.py), fotogrammi palloncino_frames.py, clip palloncino_clips.py (DUR=4.0 per stare nella quota), montaggio+mix short_palloncino.py (video|mix|finale), mix già fatto.
  Quota gratis HF ZeroGPU ~5 min/giorno = 4-5 clip/giorno (clip 5 s chiede 105 s, 4 s ~90 s). Fatte clip1 (OK), clip2 (palloncino NON vola via: da rifare), clip3 (OK ma espressione allegra), clip4 (camera si muove, compaiono altri palloncini e un altro personaggio: da rifare). Mancano 5, 6, 7. Quota si ricarica ~24 h dopo il 19/10 00:40.
- REGOLA 19/10 (utente arrabbiato: "non è tutto illimitato, fai tutto a cazzo"): PRIMA di usare un servizio gratis/limitato calcolare la quota (HF ZeroGPU gratis ~300 s GPU/giorno, una clip 4 s ~50 s) e dire PRIMA quante clip/giorni servono. Ogni clip va pensata per riuscire al primo colpo: azione semplice, una sola cosa per clip, niente oggetti/personaggi che devono comparire dal nulla, niente camera che si muove. Mai dire "basta" se non è calcolato.
- 21/10 CONSEGNATO short_palloncino_rosso.mp4 (27,5 s, 7 clip Wan 2.2 gratis: clip4 e clip7 rifatte con SEED=7; vecchie in assets/v/palloncino/*_v1.mp4). Controllo: 825 fotogrammi, nessun nero, tagli solo tra clip. Mancano: miniatura verticale + pacchetto testi (solo se li chiede). Dopo: altri short con gli animali nuovi (voci_salti/trenino/ombre) — le pose rana/coniglio/orso NON servono più col metodo Wan (parte da un fotogramma composto).
- 21/10 palloncino: utente "fa cagare, video semplicissimo, labbra a caso" (lo teniamo così). Prossimo = "CHI HA MANGIATO IL BISCOTTO?" (gag/indovina, tagli veloci, 20 s, topolino+volpe+rana+Spike, cucina). Pronti: voci audioR (voci_biscotto.py), fotogrammi biscotto_frames.py (assets/v/biscotto/start1-7), clip biscotto_clips.py (prompt con bocca chiusa dove non si parla), montaggio+mix short_biscotto.py (video|mix|finale). Fatta SOLO clip6 (Spike, OK). Mancano 1,2,3,4,5,7 = ~17 s di clip.
  Quota HF: ~19 s di GPU per ogni secondo di clip; quota giornaliera ~400-500 s => ~20-25 s di clip/giorno; si ricarica 24 h dopo l'uso (quota finita 21/10 ~01:35 CEST => riprova dopo le 00:45 del 22/10). Generatore immagini gratis Pollinations MORTO (saldo 0): coniglio/orso impossibili, solo personaggi già presenti.
