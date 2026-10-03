# BAMBINI CIAO CIAO — PASSAGGIO DI CONSEGNE COMPLETO (aggiornato al 3 ottobre 2026)

Documento per la **nuova chat**. Contiene tutto il progetto: regole dell'utente, storia di tutte le chat, stato del lavoro, file, API, errori da non ripetere e prossimi passi.
Repo: `kovacevstevo1993-gif/Tr` — **branch da usare: `claude/fervent-johnson-ob5dk7`** (contiene tutto: progetto `parco/` + il lavoro di questa chat). Cartella di lavoro: `parco/`.
Documenti di background già nel repo (leggerli): `parco/docs/Bambini_Ciao_Ciao_progetto_completo_originale.md` (identità canale, personaggi, regole Higgsfield, pubblicazioni) e `parco/docs/PROGETTO_COMPLETO_Bambini_Ciao_Ciao.md` (chat dei motori A/B e dei video v5/v6).

---

## 0. COME RIPRENDERE (cosa fare per prima cosa)
1. **Leggere questo file e i due documenti sopra PRIMA di generare qualunque cosa.**
2. **Controllare cosa esiste già** nel repo e sui suoi branch (`git branch -a`, `ls parco/assets/pose parco/assets/amb`). Nella chat precedente si è sprecato tempo e denaro ripartendo da zero (vedi §8).
3. Verificare la chiave Pollinations con **una sola** generazione di prova (costa ~0,005 pollen). Attenzione: `GET /account/key` mostra solo il *tetto* della chiave, **non il saldo reale** (il saldo reale vuoto dà HTTP 402 alla generazione).
4. Poi proseguire dal §9 (prossimi passi).

Messaggio da incollare nella nuova chat (stesso testo in fondo, §11):
> *Riprendi Bambini Ciao Ciao. Leggi `parco/docs/PASSAGGIO_Bambini_Ciao_Ciao_v3.md` nel repo `kovacevstevo1993-gif/Tr`, branch `claude/fervent-johnson-ob5dk7`. Rispetta le regole del §1. Ho collegato un nuovo account Pollinations: genera le pose mancanti (§9) e rifai lo Short migliorandolo.*

---

## 1. REGOLE DELL'UTENTE (leggerle per prime)
- Risposte **corte**, una cosa alla volta. L'utente ha un limite d'uso e si arrabbia per messaggi lunghi, attese lunghe senza spiegazioni, e generazioni sprecate. Se qualcosa si blocca per un dettaglio, **trovare un'alternativa e andare avanti**, non fermarsi.
- **Mai ripartire da zero**: guardare prima cosa esiste (repo, altre chat, branch). Mai inventare personaggi nuovi: i personaggi sono quelli in `assets/` (topolino, Chip, Spike).
- **Prima di spendere** crediti/denaro (Pollinations, VidIQ, ElevenLabs…) dire il costo. **VidIQ: l'utente ha detto di LASCIARLO STARE — non usarlo.** Higgsfield non è più disponibile. Strumenti gratuiti o a costo irrisorio.
- Video **sempre verticali 9:16** (1080x1920), per Shorts. Durata: va bene 15–30 s, anche **più di 30 s** se serve (l'ultimo Short è 46 s e va bene).
- Obiettivo qualità: l'utente vuole un risultato **"stra perfetto", bellissimo, movimentato, dettagliato, con movimenti naturali e scorrevoli**, per bambini piccoli; "da professionista Disney". Ha criticato: video "banalissimo", "non dice niente", voce inglese, voci bambini robotiche, "Shhh" letto lettera per lettera.
- **Finale di OGNI video**: il topolino dice nella scena "Bambini Ciao Ciao! Iscrivetevi al canale!" con pulsante ISCRIVITI animato nella scena (nessuna slide separata).
- **Hook** nei primi secondi che attiri l'attenzione dei bambini.
- Voce narrante: **ragazza dolce, affettuosa, realistica** (Isabella di edge-tts è "va bene"). I **bambini dicono solo l'indispensabile** (esclamazioni, battute di 1–3 parole) con **voci di ambiti/timbri diversi** (topolino, Chip, Spike), **naturali**, non modificate solo col tono.
- Lingua: **italiano con intonazione italiana** (le voci OpenAI tts-1 parlano italiano con accento inglese: NON usarle).
- Mai riprodurre video altrui. Etichetta "Realizzato per bambini", categoria Istruzione, pubblicazione martedì e venerdì ~16.
- Gli allegati mandati dall'utente MENTRE l'assistente lavora non vengono salvati: chiedere di mandarli in un messaggio nuovo quando l'assistente è fermo. Limite invio file ~30 MB (comprimere se serve).
- L'utente scrive in modo molto diretto e quando è frustrato usa parolacce: non è un problema, è un segnale che si sta sprecando tempo. Rispondere con fatti, non con scuse lunghe.

---

## 2. STORIA DI TUTTE LE CHAT DEL PROGETTO
**Agosto 2026 (21–29): chat sul canale** — nascita del canale "Bambini Ciao Ciao" (@BambiniCiaoCiao), progetti Remotion (Vecchia fattoria, Canzone dei Numeri/Colori), poi passaggio a Higgsfield (Seedance 2.0, voce Gracie), personaggi (topolino, mamma/papà topo, orsetto, Chip, Spike), cucina di riferimento, pubblicazioni. Tutto in `docs/Bambini_Ciao_Ciao_progetto_completo_originale.md`.

**Chat "Video per bambini" (branch `claude/lucid-volta-myb2ye`, 3 ott. mattina)** — Higgsfield finito → si passa a produrre i video con codice. Immagini gratuite da Google AI Studio (topolino, Chip, Spike, parco, cestini, rifiuti su verde), ritaglio, motore `engine.py`, Shorts A "La magia dei cestini" e B "Chip e il tamburo", video lungo v5/v6, voci edge-tts + Praat, musica sintetica originale. Documento: `docs/PROGETTO_COMPLETO_Bambini_Ciao_Ciao.md`. Termina col piano: ambientazioni e **pose multiple** per animare meglio.

**Chat "Progetto Bambini Ciao Ciao" + "Riprendi Bambini Ciao Ciao" (branch `claude/upbeat-einstein-f0m1jz`, 3 ott.)** — importato `parco/`; prova di camminata del topolino (`parco/walk.py`, busto/braccia/gambe separati, `test_camminata_topolino.mp4`); tentativo di generare pose con **Gemini** (`gemini_pose.py`: quota immagini gratuita = 0, inutilizzabile); l'utente crea chiave **Pollinations** (budget, host consentito `gen.pollinations.ai`) e la salva nell'ambiente; si decide di generare le pose **partendo dal topolino esistente** (image-to-image).

**Questa chat (branch `claude/fervent-johnson-ob5dk7`, 3 ott.)** — cronologia in dettaglio:
1. Primo errore: **ho inventato un topolino nuovo da zero** (era simile a Mickey Mouse) con Pollinations invece di partire dal repo. Scartato. Lezione: leggere il repo prima.
2. Rifatto correttamente: pose del **vero topolino** in image-to-image (`parco/pose_pollinations.py`, endpoint `/v1/images/edits`, modello `klein`), poi Chip e Spike. Camminata corretta (braccio opposto alla gamba; `cammina_sx` = specchio di `cammina_dx`).
3. Scena **cucina** (`assets/amb/cucina.png`, stile del parco, pavimento in parquet; la prima versione aveva una zona "a vetro" sbagliata).
4. **Short v1** "Il barattolo misterioso" (23 s): troppo banale, voce OpenAI con accento inglese.
5. **Short v2** (46 s): voci italiane edge-tts, storia più ricca, transizioni fluide tra pose (flusso ottico), camera, luce, conto 1-2-3, farfalla, biscotti, ballo, finale con ISCRIVITI. Feedback: "migliorato ma non ancora", "Shhh letto lettera per lettera", "voci bambini troppo robotiche (modificate solo col tono)".
6. **Short v3** (46 s, `parco/short_barattolo_v3.mp4`): "Zitti, zitti" al posto di "Shhh", voci bambini con intonazione nativa e ritocco minimo, polvere ai piedi, onde sul barattolo, topolino triste. **Mancano ancora le pose nuove perché il saldo Pollinations era a zero** (gli ultimi 16 file non sono stati generati; si usano sostituti, §7).
7. L'utente ha creato **un nuovo account Pollinations** e ha collegato la chiave: la nuova chat lo userà.

Altri progetti nello stesso repo, **separati da questo** (non toccarli): `conti_in_pensione/` (canale "Conti in pensione"), "The Money Backstory", "Lea & Leo". Esistono altre chat su quei temi: non fanno parte di Bambini Ciao Ciao.

---

## 3. MAPPA DEI BRANCH
| Branch | Contenuto |
|---|---|
| `claude/fervent-johnson-ob5dk7` | **QUELLO DA USARE.** Tutto `parco/` + pose Pollinations, scene, Short v1/v2/v3, documenti. |
| `claude/upbeat-einstein-f0m1jz` | `parco/` con prova camminata, `gemini_pose.py`. Già incluso in fervent. |
| `claude/lucid-volta-myb2ye` | origine di `parco/` (motori A/B, video v5/v6, documenti). Già incluso. |
| `claude/youthful-einstein-uctfje`, `claude/wizardly-galileo-uh8q18`, `claude/ecstatic-shannon-wl7kwf`, `claude/gifted-dirac-fu42fm`, `claude/money-backstory-project-bqq9ic` | altri progetti (Conti in pensione, Money Backstory…): non riguardano i bambini. |
Nota: la tecnica PR non serve; l'utente non ha chiesto Pull Request. Committare e pushare solo sul branch indicato.

---

## 4. FILE IN `parco/` (cosa serve davvero)
**Del progetto originale** (vedi `PROGETTO_COMPLETO…md`): `engine.py`, `sceneA.py`, `sceneB.py`, `render4.py`, `voicegen.py` (Praat), `mixlib.py` (musica/effetti), `prep3.py`/`prep4.py`, `assets/topo|s|v`, `audio*/`, video v5/v6 e Shorts A/B.

**Creati in questa chat (usare questi per il nuovo Short):**
| File | Cosa fa |
|---|---|
| `pose_pollinations.py` | Genera pose **da un'immagine di riferimento** (image-to-image) → `assets/pose/<chi>_<posa>.png` (RGBA 768x1376). `python3 pose_pollinations.py topo|chip|spike [pose…] [--rifai]`. Salta quelle già fatte. Dizionario `POSE` con i prompt; `SPECCHIO` = pose ottenute specchiando. Riferimenti: `assets/topo/neutro_full.png`, `assets/s/chip.png`, `assets/s/spike.png`. |
| `ambientazioni_pollinations.py` | Genera scene verticali nello stile del parco (riferimento `assets/s/sfondo_src.png`) → `assets/amb/<nome>.png`. Per ora esiste solo `cucina`; nel dizionario anche `spiaggia`, `asilo`, `camera_sera` (non generate). |
| `morph.py` | **Interpolazione fluida tra pose** (flusso ottico Farneback + dissolvenza, cache su disco in `/tmp/claude-0/morph_cache`). Allinea le pose su una tela comune (ancora = centro busto, piedi). Contiene `SUBST` (sostituti per le pose mancanti). |
| `short_cucina2.py` | **Renderer dello Short v2/v3**: copione con tempi dalle voci, eventi di posa per personaggio, camera cinematografica, luce, polvere, farfalla, biscotti, conto, finale. `python3 short_cucina2.py info|prep|test 1.0 5.5|render muto.mp4`. (`short_cucina.py` = vecchio v1, non usare.) |
| `voci_cucina2.py` | Voci **italiane** con edge-tts → `audioD/*.wav` + `durate.json`. Narratrice Isabella; bambini Diego/Elsa/Giuseppe. |
| `mix_cucina2.py` | Mix: voci + musica (`mixlib`) + effetti sincronizzati (passi, toc, salti, scoppio, morsi). → `mix_cucina2.wav` |
| `voci_cucina.py`, `mix_cucina.py` | vecchie voci (Gemini/OpenAI) del v1: **non usare**. |
| `short_barattolo_v3.mp4` | **Ultimo video** (46 s, 1080x1920, con audio). v1/v2 sono in git history. |
| `docs/PASSAGGIO_…v3.md` | questo documento. |

Rendering completo: 
```
python3 voci_cucina2.py            # voci (edge-tts, gratis)
python3 short_cucina2.py prep      # precalcola le transizioni tra pose (~1 min)
python3 short_cucina2.py render muto.mp4      # ~15 min per 46 s (4 processi)
python3 mix_cucina2.py             # audio
ffmpeg -y -i muto.mp4 -i mix_cucina2.wav -c:v copy -c:a aac -b:a 192k -shortest out.mp4
```
Dipendenze: `pip install pillow numpy scipy requests edge-tts opencv-python-headless` + `ffmpeg` (rubberband incluso).

---

## 5. SERVIZI, CHIAVI E TRAPPOLE (importante)
**Pollinations (immagini)** — la chiave è **iniettata dal proxy** della sessione (host `gen.pollinations.ai`): nel codice non serve scrivere nessuna chiave.
- Image-to-image: `POST https://gen.pollinations.ai/v1/images/edits` multipart: `model=klein` (flux.2-klein, ~0,005 pollen/immagine), `size=768x1376`, `prompt=…`, `image=@riferimento.png` (il riferimento va messo su **sfondo verde #00FF00**; la risposta è JSON con `data[0].b64_json`). Funziona molto bene per mantenere identico il personaggio. Altri modelli con input immagine: `kontext` (0,03), `gptimage`, `gpt-image-1.5`, `mai-image-2.6`.
- Text-to-image: `GET https://gen.pollinations.ai/image/<prompt>?model=flux&width=…&height=…` (0,002).
- **Errori**: `HTTP 502 upstream request failed` = transitorio (riprovare con pausa). **`HTTP 402 INSUFFICIENT_BALANCE` = saldo reale finito** (il tetto della chiave `pollenBudget` è un'altra cosa). Con 3 processi in parallelo i 502 aumentano: meglio 1–2.
- Nessun modello video disponibile su Pollinations.
- Sfondo verde → trasparente: `ritaglia()` in `pose_pollinations.py` (key morbida + despill, tiene il componente più grande). Se il modello dà un verde "sporco" l'importante è la dominanza del verde, non il valore esatto.

**Voci italiane — edge-tts** (gratis): voci `it-IT-IsabellaNeural` (narratrice), `ElsaNeural`, `DiegoNeural`, `GiuseppeMultilingualNeural`. **Prima di `import edge_tts` nella sandbox:** `import certifi; certifi.where = lambda: "/root/.ccr/ca-bundle.crt"` (altrimenti errore SSL; altrove togliere). Le voci neurali aggiungono **pause di ~0,9 s sulla punteggiatura**: si accorciano con `silenceremove` (già in `voci_cucina2.py`). **Non scrivere "Shhh"**: viene letto lettera per lettera → usare "Zitti, zitti" (a schermo si può scrivere SHHH).
- I bambini: rubberband con rialzo grande (+4/+5 semitoni) suona robotico; ora si usa il tono nativo di edge-tts (`pitch="+34Hz"`) + ritocco minimo. Se ancora robotico: provare l'approccio **Praat** di `voicegen.py` (altezza + formanti, `praat-parselmouth`), che nel progetto originale era stato giudicato "va bene", oppure voci a pagamento (ElevenLabs/Azure) **solo dopo aver detto il costo**.
- Le voci OpenAI (Pollinations `tts-1`) hanno accento inglese: scartate. **Gemini TTS** funziona solo con frasi lunghe (le brevi tornano `finishReason: OTHER`) e ha quota giornaliera bassa (429): scartato.
- Nota: l'assistente **non può ascoltare l'audio**; i giudizi sulla voce li dà l'utente.

**Gemini (immagini/voce)**: immagini = quota 0 (429) → inutilizzabile. **VidIQ**: non usare (decisione dell'utente). **Higgsfield MCP**: espone solo Ads Studio, inutile qui.

---

## 6. STATO DELLE RISORSE GRAFICHE
**Personaggi** (stile 3D Pixar, tutti su verde nel riferimento):
- **Topolino**: pelo grigio, grandi orecchie rosa, occhi scuri, salopette gialla con taschino rosso, maglietta a righe turchesi, scalzo.
- **Chip** (scoiattolo, sciarpa verde lime) e **Spike** (riccio, cappellino blu).

**Pose generate** (in `assets/pose/`, per ognuno dei tre = `topo_`, `chip_`, `spike_`):
`cammina_dx`, `cammina_sx` (specchio), `china`, `tiene`, `lancia`, `saluta`, `sorpreso`, `ride`, `neutro`, `corre`, `sbircia` — presenti per tutti e 3. `indica` — presente per topolino e Spike, **manca per Chip**. `topo_triste` — copiata dall'originale `assets/topo/triste_full.png`.
**Mancanti (da generare appena c'è saldo):** `mangia`, `balla`, `salto`, `afferra`, `guarda_su` (per tutti e 3) e `indica` (Chip). Nel frattempo `morph.SUBST` le sostituisce: salto/balla→`ride`, guarda_su→`sorpreso`, afferra→`corre`, indica→`saluta`, mangia→`tiene` (il biscotto che si mangia è disegnato a codice).
**Scene:** `assets/amb/cucina.png`; parco in `assets/s/sfondo*.png`. Da fare: spiaggia, asilo, cameretta di sera, bosco, parco giochi, fattoria, orto, neve.

---

## 7. LO SHORT "IL BARATTOLO MISTERIOSO" (v3)
Storia (46 s): il topolino sente bussare nel barattolo dei biscotti (hook: "SHHH! Cosa si muove?", barattolo che trema e brilla, TOC!) → chiama Chip e Spike che arrivano di corsa → conto "Uno, due, tre" con numeri giganti e saltelli → il coperchio salta, esce una farfalla magica → la inseguono → la farfalla esce dalla finestra (topolino triste) → "Ciao ciao, farfalla!" → arcobaleno e un biscotto per ognuno, lo mangiano (morsi, briciole) → ballano → "Bambini Ciao Ciao! Iscrivetevi al canale!" con pulsante ISCRIVITI.
Copione e tempi: in `short_cucina2.py` (`EV` = eventi di posa, `KF` = posizioni, `CAM` = camera, `KNOCKS`, `BF` = percorso farfalla) e `voci_cucina2.py` (`RIGHE`).

---

## 8. ERRORI DA NON RIPETERE (lezioni di questa chat)
1. **Non ripartire da zero / non inventare personaggi.** Prima leggere repo, branch e documenti (è costato un'intera iterazione e crediti).
2. **Non lanciare molte generazioni parallele** su servizi con 502/limiti: poche alla volta; prima 1 test.
3. **Non cercare processi con `pkill -f`/`ps | grep` dentro un comando che contiene lo stesso nome**: si uccide la propria shell (exit 144). Usare uno script a parte o `awk '/nome/ && !/awk/'`.
4. **Controllare lo stato reale** (file/processi) prima di dire "in corso" o "finito".
5. Il tetto di una chiave (`pollenBudget`) non è il saldo: la prova vera è una generazione.
6. Il morph tra pose molto diverse (es. `corre`↔`corre_m`) lascia un po' di "fantasma": sono già stati alzati alpha e allineamento; per migliorare servono più pose intermedie reali, non più codice.
7. Il numero più importante per la qualità percepita sono **pose vere** (azioni diverse) e **voci naturali**.
8. L'ordine di disegno conta: numeri/testi pop-up vanno **dopo** i personaggi; telecamera zoom ≥ 1.

---

## 9. PROSSIMI PASSI (in ordine)
1. **Verificare la chiave Pollinations nuova** con una generazione. Poi generare le pose mancanti (1–2 processi alla volta): `python3 pose_pollinations.py topo mangia balla salto afferra guarda_su` e uguale per `chip` (+`indica`) e `spike`. Controllare ogni gruppo con un foglio contatto (in `scratchpad`, non nel repo).
2. **Pose in più per movimenti più naturali** (l'utente le chiede esplicitamente: "crea altre immagini se ti servono"): camminata con **braccia opposte alle gambe** per Chip e Spike (ora hanno le braccia simmetriche), pose di "passaggio" della camminata, `corre` alternate (non specchiate), saluto con due mani, abbraccio, bocca aperta/chiusa (versioni "parla"), occhi chiusi/ammiccanti, rotazione di tre quarti, salti in 3 fasi (anticipo/aria/atterraggio).
3. **Parlato**: i personaggi ora non muovono la bocca (solo rimbalzo). Idea: generare per le pose principali una variante a bocca aperta e alternarla con l'ampiezza della voce (come `assets/v/*_m0b0…`).
4. **Voci bambini più naturali**: provare Praat (`voicegen.py`), poi eventualmente servizi a pagamento (dire il costo prima).
5. **Altre scene** (spiaggia, asilo, cameretta) e nuovi Shorts: idee dal vecchio documento (primo giorno all'asilo, paura del buio, condividere il giocattolo, coniglietto triste, versi degli animali). Micro-Short da 11–15 s sono il formato che ha reso di più nei riferimenti.
6. Prima di pubblicare: caricare **privato** su YouTube Studio per i controlli copyright; "Realizzato per bambini", categoria Istruzione, titoli con emoji e "Cute 3D Animation".
7. Ricordare all'utente il costo reale delle voci a pagamento per la versione monetizzata (le voci edge-tts sono una zona grigia commerciale).

---

## 10. CHECKLIST RAPIDA PER L'ASSISTENTE
- [ ] letto questo file + i due documenti
- [ ] `git branch -a`, `ls parco/assets/pose` per vedere cosa c'è
- [ ] 1 generazione di prova Pollinations (0,005)
- [ ] niente VidIQ, niente personaggi nuovi, niente messaggi lunghi
- [ ] ogni passo: far vedere il risultato (fotogrammi/foglio contatto) all'utente con `SendUserFile`

---

## 11. MESSAGGIO DA INCOLLARE NELLA NUOVA CHAT
```
Riprendi Bambini Ciao Ciao.
Leggi `parco/docs/PASSAGGIO_Bambini_Ciao_Ciao_v3.md` nel repo kovacevstevo1993-gif/Tr, branch claude/fervent-johnson-ob5dk7, e i due documenti che cita. Rispetta le regole del §1 (risposte corte, niente VidIQ, niente personaggi nuovi, controlla il repo prima di generare).
Ho collegato un nuovo account Pollinations: fai prima UNA generazione di prova, poi genera le pose mancanti (§9) e rifai lo Short "Il barattolo misterioso" più movimentato e con le voci dei bambini più naturali.
```


---
## 12. AGGIORNAMENTO (3 ott. 2026, sera) — Short v4 "Il barattolo misterioso" (`short_barattolo_v4.mp4`, 45 s)
**Fatto:** pose mancanti di tutti e 3 (`mangia, balla, salto, afferra, guarda_su`, `chip_indica`) + pose nuove con l'oggetto GIÀ nelle mani: `orecchio, riceve, tiene_biscotto, mangia2, saluta2, parla_a/parla_o` (Spike senza parla_*; `indica_giu` è venuta male: non usarla). Oggetti 3D in `assets/obj/` (`jar, jar_open, lid, cookie, bf_open`; `jar_open`/`lid` sono ritagli di `jar`). Generatore: `oggetti_pollinations.py`.
**Voci:** `voci_cucina3.py` → `audioE/`. Solo voci native it-IT (Isabella, Diego, Elsa): la `GiuseppeMultilingual` sbaglia le doppie ("Aspatami") ed è esclusa. Bambini = edge-tts a tono quasi naturale + Praat (Change gender). **Ogni battuta viene riascoltata con `trascrivi.py`** (Pollinations whisper, costo irrisorio) e rifatta se non coincide col testo. Questo è il modo di "ascoltare" la pronuncia.
**Regia:** `short_cucina3.py` (+ `mix_cucina3.py`): biscotto che atterra nelle mani (posa `riceve`) → già nella posa (`tiene_biscotto`/`mangia`/`mangia2` alternati = masticare); mouse con l'orecchio al barattolo (`orecchio_m`); saluto a due mani; barattolo/biscotto/farfalla 3D. Rendering: ~4 min (4 core).
**Saldo Pollinations del 2° account: di nuovo 0** (HTTP 402). Da generare quando c'è saldo: `spike_parla_a/o`, `bf_closed` (ali chiuse), un vero `indica_giu`, pose di camminata con braccia opposte per Chip/Spike.
