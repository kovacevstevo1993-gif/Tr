# BAMBINI CIAO CIAO — PASSAGGIO DI CONSEGNE v4 (3 ottobre 2026, sera)

Documento per la **nuova chat**. Sostituisce e completa `PASSAGGIO_Bambini_Ciao_Ciao_v3.md` (che resta come storia). Contiene tutto il progetto: regole dell'utente, storia di TUTTE le chat, stato, file, API, trappole, prossimi passi.
Repo: `kovacevstevo1993-gif/Tr` — **branch da usare: `claude/nifty-brown-0jnc8w`** (contiene tutto: `parco/` con pose, ambienti, oggetti, voci, Shorts, SEO, documenti). Cartella di lavoro: `parco/`.
Documenti di background già nel repo (leggerli prima di fare qualunque cosa):
1. `parco/docs/Bambini_Ciao_Ciao_progetto_completo_originale.md` — identità canale, personaggi, regole Higgsfield, pubblicazioni.
2. `parco/docs/PROGETTO_COMPLETO_Bambini_Ciao_Ciao.md` — chat dei motori A/B e dei video v5/v6.
3. `parco/docs/PASSAGGIO_Bambini_Ciao_Ciao_v3.md` — chat delle pose Pollinations e dello Short v1-v3.
4. questo file.

---

## 0. COME RIPRENDERE (cosa fare per prima cosa)
1. Leggere questo file e i tre documenti sopra. 
2. Controllare cosa esiste (`git branch -a`, `ls parco/assets/pose parco/assets/amb parco/assets/obj`). **Mai ripartire da zero, mai inventare personaggi.**
3. `pip install pillow numpy scipy requests edge-tts opencv-python-headless praat-parselmouth certifi` (ffmpeg c'è già).
4. Verificare i crediti Pollinations con **una sola** generazione (~0,005 pollen): HTTP 200 = ok, **402 = saldo finito** (la chiave non permette di leggere il saldo).
5. Procedere dai "Prossimi passi" (§9).

Messaggio da incollare nella nuova chat (anche in fondo, §11).

---

## 1. REGOLE DELL'UTENTE (leggerle per prime)
- Risposte **corte**, una cosa alla volta. L'utente ha limiti d'uso e si arrabbia per messaggi lunghi, attese senza spiegazioni, generazioni sprecate, e quando gli si manda un file e lui "non vede niente" (vedi §8). Se qualcosa si blocca, trovare un'alternativa e andare avanti.
- **Mai inventare personaggi**: topolino, Chip (scoiattolo, sciarpa lime), Spike (riccio, cappellino blu), in `assets/`.
- **Crediti**: "tenta di sprecare meno crediti". Dire il costo prima di spendere; una prova prima delle serie; niente generazioni parallele inutili (§5). **VidIQ: l'utente ha detto di LASCIARLO STARE.** Higgsfield non disponibile.
- Video **sempre verticali 9:16** (1080x1920). Durata 15–60 s va bene.
- Qualità: "stra perfetto", "il più realistico possibile", "movimenti, gesti, oggetti fatti bene, **i personaggi fanno quello che dice la narrazione**, gli oggetti al posto giusto davanti a loro", "ambiente diverso a seconda della storia, **ambientazione che si muove**, tutto movimentato che attira i bambini", "da progettista Disney", "stile cartoon realistico come i video virali su YouTube".
- **Controllare il video da cima a fondo prima di consegnarlo** ("devi controllarlo fotogramma per fotogramma, non a cazzo, deve essere perfetto"): vedi §6 per il metodo.
- **Finale di OGNI video**: il topolino dice nella scena "Bambini Ciao Ciao! Iscrivetevi al canale!" con pulsante ISCRIVITI animato nella scena (nessuna slide).
- **Hook** nei primi 2 secondi (nell'ultimo: testo gigante "COSA C'È NEL BOSCO?" + seme che brilla).
- Voce narrante: ragazza dolce (Isabella). **Bambini: solo battute di 1–3 parole**, voci diverse, **italiane native** e con pronuncia corretta ("c'è qualche parola che la sbagliano": vedi §5 trascrizione).
- Con ogni video l'utente vuole anche: **titolo, descrizione con parole chiave SEO, hashtag, tag, miniatura che attira l'attenzione** (e **anche la miniatura VERTICALE 1080x1920 — la vuole, mandarla da sola**), sottotitoli `.srt`, descrizione playlist.
- **NIENTE miniatura orizzontale: l'utente vuole SOLO la verticale 1080x1920** (non generarla né mandarla). Consegna = video + miniatura verticale + `.srt` + testi in chat.
- Se trova errori: **raccogliere TUTTI gli errori prima, poi UN solo rendering** (ogni rendering costa ~7 min; l'utente si arrabbia se si rifà più volte).
- Dare i testi **direttamente nella chat** (in blocchi da copiare), non solo come file.
- Etichetta "Realizzato per bambini", categoria Istruzione, pubblicazione martedì e venerdì ~16. Mai riprodurre video altrui.
- Gli allegati mandati dall'utente MENTRE l'assistente lavora non vengono salvati: chiedere di rimandarli a assistente fermo.
- L'utente scrive diretto e usa parolacce quando è frustrato: è un segnale che si sta sprecando tempo. Rispondere con fatti.

---

## 2. STORIA DI TUTTE LE CHAT DEL PROGETTO
- **Agosto 2026**: nascita del canale, Remotion, Higgsfield (Seedance, voce Gracie), personaggi. → doc "originale".
- **Chat "Video per bambini" (`lucid-volta-myb2ye`, 3 ott. mattina)**: Higgsfield finito → video con codice; immagini gratuite AI Studio; `engine.py`; Shorts A "La magia dei cestini" e B "Chip e il tamburo"; video lungo v5/v6; voci edge-tts + Praat. → doc "PROGETTO_COMPLETO".
- **Chat `upbeat-einstein-f0m1jz` (3 ott.)**: import di `parco/`, prova camminata, tentativo Gemini (quota immagini = 0), chiave Pollinations.
- **Chat `fervent-johnson-ob5dk7` (3 ott.)**: pose del vero topolino/Chip/Spike in image-to-image; cucina; Short "Il barattolo misterioso" v1→v3 (46 s). → doc v3. Il saldo Pollinations finì.
- **Questa chat (`nifty-brown-0jnc8w`, 3 ott., pomeriggio-sera)**:
  1. Letto repo; nuovo account Pollinations → generate tutte le pose mancanti (mangia, balla, salto, afferra, guarda_su, indica Chip) + pose nuove con l'oggetto in mano (orecchio, riceve, tiene_biscotto, mangia2, saluta2, parla_a/parla_o).
  2. **Voci**: scartata `GiuseppeMultilingual` (sbaglia le doppie: "Aspatami"); ora Isabella/Diego/Elsa + Praat; **ogni battuta riascoltata via trascrizione Pollinations** e rifatta se non coincide (`voci_cucina3.py`, `trascrivi.py`).
  3. **Short v4 "Il barattolo misterioso"** (45 s): oggetti 3D, biscotto che atterra nelle mani, orecchio al barattolo, ecc. L'utente: "Va bene". Miniature, SEO, sottotitoli, playlist.
  4. Nuovo account Pollinations di nuovo con saldo → **Short "Il seme magico"** (51 s): 3 ambienti nuovi animati, oggetti 3D (albero, seme, germoglio, mela, nuvola, uccellino), pose con la mela, pioggia, arcobaleno, albero che cresce, mele che cadono, cerchio magico. L'utente: "Va bene, ma il prossimo lo facciamo meglio".
  5. Controllo fotogramma per fotogramma del seme magico (103 fotogrammi + punti critici): trovati e corretti difetti (§6), rifatto il rendering.
- Altri progetti nello stesso repo, **separati** (non toccare): `conti_in_pensione/`, Money Backstory, Lea & Leo.

---

## 3. MAPPA DEI BRANCH
| Branch | Contenuto |
|---|---|
| `claude/nifty-brown-0jnc8w` | **QUELLO DA USARE** (include tutto il lavoro di fervent-johnson + questa chat). |
| `claude/fervent-johnson-ob5dk7`, `upbeat-einstein-f0m1jz`, `lucid-volta-myb2ye` | storia, già inclusi. |
| altri (`youthful-einstein`, `wizardly-galileo`, `ecstatic-shannon`, `gifted-dirac`, `money-backstory`) | altri progetti, non bambini. |
Committare e pushare solo sul branch indicato. L'utente non ha chiesto Pull Request.

---

## 4. FILE IN `parco/` (cosa serve davvero)
**Asset**
| Cartella | Contenuto |
|---|---|
| `assets/pose/` | Pose RGBA 768x1376 per `topo_`, `chip_`, `spike_`: neutro, cammina_dx/sx, china, tiene, lancia, saluta, saluta2, sorpreso, ride, corre, sbircia, indica, mangia, mangia2, balla, salto, afferra, guarda_su, orecchio, riceve, tiene_biscotto, **tiene_mela, mangia_mela, mangia_mela2**, parla_a, parla_o (spike senza parla_*; `indica_giu` venuta male: non usarla). `topo_triste` è l'originale. Le pose terminate in `_m` si ottengono specchiando (non sono file). |
| `assets/amb/` | cucina, **giardino, bosco, tramonto** (verticali 768x1376 nello stile del parco). Da generare: spiaggia, asilo, camera_sera (già nel dizionario). |
| `assets/obj/` | jar, jar_open, lid, cookie, bf_open (farfalla), **tree, seed, sprout, apple, cloud, bird**. (`bf_closed` mai generato: ali "chiuse" simulate schiacciando.) |

**Script di generazione**
- `pose_pollinations.py` — pose in image-to-image (`python3 pose_pollinations.py topo|chip|spike [pose…] [--rifai]`), dizionario `POSE`.
- `ambientazioni_pollinations.py` — scene verticali (dizionario `AMB`; voce = testo o `(scena, suolo)`).
- `oggetti_pollinations.py` — oggetti 3D; chiave **verde** per oggetti con vetro/trasparenze, **magenta** per quelli verdi (albero, germoglio): `ritaglia(..., magenta=True)`.
- `trascrivi.py` — "ascolta" un wav con Pollinations whisper (per controllare la pronuncia).

**Regia/rendering (usare questi come base per i nuovi Short)**
- `morph.py` — transizioni fluide tra pose (flusso ottico), cache in `/tmp/claude-0/morph_cache`.
- `short_seme.py` — **renderer più avanzato** (3 ambienti, vento/nuvole/luci/lucciole/foglie/uccellini/farfalle, albero che cresce, pioggia, arcobaleno, mele con fisica, cerchio magico, camera cinematografica, bocca che parla, sottotitoli, ISCRIVITI). `python3 short_seme.py info|prep|test 1.0 5.5|render muto.mp4`.
- `voci_seme.py` + `mix_seme.py` — voci (audioF/) e mix (musica sintetica + effetti sincronizzati).
- `short_cucina3.py`, `voci_cucina3.py`, `mix_cucina3.py` — Short "barattolo" v4 (audioE/).
- Vecchi (non usare): `short_cucina.py`, `short_cucina2.py`, `voci_cucina*.py` v1/v2, `mixlib.py` è la libreria audio **da usare**.
- Miniature: `miniatura_barattolo.py`, `miniatura_seme.py` (funzioni riusabili: `pose`, `rays`, `add_glow`, `outline_text`, `sparkle`, `finish`).

**Video e testi consegnati**
- `short_barattolo_v4.mp4` (45 s), `short_seme_magico.mp4` (51 s, versione corretta dopo il controllo).
- `miniatura_barattolo_1280x720.jpg`, `..._1080x1920.jpg`, `miniatura_seme_1280x720.jpg`, `..._1080x1920.jpg`.
- `docs/SEO_barattolo_misterioso.md`, `docs/SEO_seme_magico.md`, `sottotitoli_barattolo_v4.it.srt/.txt`.

Rendering tipo (~5 min per 50 s con 4 core):
```
python3 voci_seme.py && python3 short_seme.py prep && python3 mix_seme.py
python3 short_seme.py render muto.mp4
ffmpeg -y -i muto.mp4 -i mix_seme.wav -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest out.mp4
```
(`-crf 23` per restare sotto i 30 MB di invio.)

---

## 5. SERVIZI, CHIAVI E TRAPPOLE
**Pollinations** — chiave **iniettata dal proxy** (host `gen.pollinations.ai`): nel codice non va scritta.
- Image-to-image: `POST /v1/images/edits` multipart `model=klein`, `size`, `prompt`, `image` (riferimento su sfondo verde #00FF00); risposta JSON `data[0].b64_json`. ~0,005 pollen/immagine.
- Text-to-image: `POST /v1/images/generations` (json `model=klein, prompt, size, n`).
- Trascrizione: `POST /v1/audio/transcriptions` (`model=openai/whisper-large-v3`, `language=it`). TTS Pollinations = solo voci OpenAI con **accento inglese: non usarle**.
- Errori: `502 upstream` = transitorio (gli script riprovano); **`402 INSUFFICIENT_BALANCE` = saldo finito** → fermarsi e dirlo all'utente (non insistere). Poche richieste in parallelo (2–3).
- Il vecchio `image.pollinations.ai` gratuito funziona ma aggiunge scritta e stile diverso: inadatto.
- Prompt che funzionano: "Use the attached character exactly as it is… Only change the pose: …"; per **mani con oggetto** descrivere l'oggetto già in mano ("holding one big shiny red apple with both hands in front of the chest…"). Per `riceve` dire "both arms stretched far out forward… palms up" (con "cupped hands" veniva uguale a `tiene`).
- Se la prima versione di una posa non va: `rm` il file e rilanciare con prompt rinforzato (costa solo quella).

**Voci — edge-tts** (gratis). Voci native it-IT: `IsabellaNeural` (narratrice), `DiegoNeural` (topolino e Spike con timbro diverso), `ElsaNeural` (Chip). **NON usare `GiuseppeMultilingualNeural`** (doppie sbagliate). Nella sandbox, prima di `import edge_tts`: `certifi.where = lambda: "/root/.ccr/ca-bundle.crt"` (altrove togliere). I bambini passano da Praat `Change gender` (formanti/mediana/intonazione, vedi `VOCE` in `voci_seme.py`). Pause lunghe della punteggiatura tagliate con `silenceremove`. **Non scrivere "Shhh"** nel parlato. Numeri: scrivere "Uno/Due/Tre" (la trascrizione dà "1/2/3": `NUM` li normalizza).
- **Controllo pronuncia**: dopo ogni battuta `trascrivi.py` confronta; se diverso, riprova con rate/pitch alternativi (`ALT`). Così ho corretto "bossa→bussa", "Una→Uno". L'assistente **non può ascoltare**: il giudizio sul timbro/naturalezza resta dell'utente.

**Trappole di programmazione**
- Non usare `pkill -f`/`ps | grep` con il proprio nome nel comando (si uccide la shell): usare `awk '/nome/ && !/awk/'`.
- Disegnare ellissi con raggio negativo → crash nel rendering (`x1 must be >= x0`): controllare `rr > 2`.
- Render parallelo (`Pool`): nessuno stato globale che cambia tra fotogrammi (la bocca usa isteresi senza stato).
- Un'immagine passata a `Read` è visibile all'assistente; per l'utente va inviata con `SendUserFile` (**un file/argomento per volta, con didascalia**).
- Il tetto della chiave (`pollenBudget`) non è il saldo.
- Hook "stop": se compare "uncommitted changes", committare e pushare subito (e togliere i file temporanei: muto, wav, log, test_*.png).

---

## 6. METODO DI CONTROLLO QUALITÀ (obbligatorio prima di consegnare)
1. Estrarre un fotogramma ogni 0,5 s: `ffmpeg -i video.mp4 -vf "fps=2,scale=400:711" qa/f_%03d.png`, comporre fogli da 5 e guardarli **tutti in ordine**.
2. Per ogni sezione chiave guardare a 24 fps o a passi di 0,2 s (es. mele nelle mani).
3. Cercare: personaggi tagliati/fuori campo, **doppioni (fantasmi)** nelle transizioni di posa, oggetti non allineati con le mani, testo coperto, sottotitoli non sincronizzati, effetti a righe/gradini, scritte fuori dai bordi, fotogramma finale nero.
4. Correggere, rifare `prep`/`mix`/`render`, ricontrollare **le sole zone corrette**.
Difetti trovati e corretti nel "seme magico": topolino che entrava tagliato a sinistra; seme non nelle mani nella raccolta (china specchiata); doppioni nelle transizioni (durate max 0,17 s); lucciole additive sui personaggi (ora normali, dietro); scintille della crescita sull'albero (ora sulla chioma); tramonto troppo scuro; camera che tagliava i personaggi; arcobaleno a gradini (ora liscio).
**Difetti noti ancora da migliorare (il prossimo Short deve essere migliore):**
- Le pose cambiano a scatto con pochi frame intermedi: servono più pose di passaggio vere (anticipo/aria/atterraggio dei salti, camminata completa con braccia opposte per Chip e Spike).
- Il ballo e l'esultanza si ripetono (balla/balla_m): servono più varianti.
- Le mele a terra restano ferme in fila; il "fantasma" residuo nella transizione corre↔corre_m.
- Occhi che sbattono e ammiccano non ci sono; bocca solo 3 stati (neutro/o/a).
- Ambienti statici: il vento deforma i fondali ma non c'è vera parallasse a più livelli (si potrebbe separare cielo/colline/primo piano).
- Il pulsante ISCRIVITI è visibile ma piccolo nei primi fotogrammi mentre entra.

---

## 7. LO SHORT "IL SEME MAGICO" (copione)
Bosco: il topolino passeggia (hook "COSA C'È NEL BOSCO?") → vede il seme che brilla → si china e lo raccoglie ("Che bello!") → cerchio magico → giardino: lo porta e lo pianta → nuvoletta (faccina) con pioggia, il topolino ride ("Evviva!") → "Pop!" germoglio + arcobaleno → chiama Chip e Spike (arrivano di corsa) → l'albero cresce in 3 scatti, tutti guardano su ("Che alto!", "Che meraviglia!") → cadono le mele, le prendono ("Prendiamole!") → cerchio magico → tramonto: mangiano le mele ("Che buona!", "Buonissima!") → ballo → "Bambini Ciao Ciao! Iscrivetevi al canale!" + ISCRIVITI.
Tempi/eventi: `short_seme.py` (`EV` pose per personaggio, `KF` posizioni, `CAM` camera, `SCENES`, `LAND`/`ET` mele, `G0/G1` crescita). Testi/voci: `voci_seme.py` (`RIGHE`).

---

## 8. ERRORI DA NON RIPETERE
1. Non ripartire da zero / non inventare personaggi.
2. Non lanciare molte generazioni parallele, **non sprecare crediti**: una prova, poi la serie; non rigenerare ciò che c'è già.
3. Non dire "consegnato" prima di aver controllato il video **fotogramma per fotogramma** (§6).
4. **Consegne all'utente**: mandare i testi (titolo, descrizione, tag…) **scritti nella chat**; mandare **la miniatura verticale da sola** (l'ha richiesta due volte); un messaggio = una cosa.
5. Non dichiarare cose non verificate ("ho controllato" solo se è vero). Non posso ascoltare l'audio.
6. Il morph tra pose molto diverse lascia "fantasmi": servono pose intermedie reali, non più codice.
7. L'ordine di disegno conta: pop-up/testi dopo i personaggi; camera con zoom ≥ 1.
8. Hashtag/tag: attenzione a caratteri strani (una volta è comparso un carattere cirillico nell'hashtag): ricontrollare con grep non-ASCII.

---

## 9. PROSSIMI PASSI
1. Verificare il saldo Pollinations (1 prova).
2. **Nuovo Short migliore** (l'utente: "il prossimo lo facciamo meglio"): storia nuova (idee: primo giorno all'asilo, paura del buio, condividere il giocattolo, coniglietto triste, versi degli animali, spiaggia/castello di sabbia). Per alzare il livello:
   - più **pose di passaggio** reali (salto in 3 fasi, camminata con braccia opposte per Chip/Spike, abbraccio, saluto con due mani, occhi chiusi/ammiccanti);
   - **parallasse a livelli** negli ambienti (cielo, colline, alberi, primo piano che si muovono a velocità diverse);
   - più **eventi/effetti** coerenti con la narrazione (ogni frase = un'azione chiara, con l'oggetto nel posto giusto davanti ai personaggi);
   - 1 ambiente diverso ogni 10–12 s; hook ancora più forte nei primi 2 secondi;
   - più musica/effetti (già buoni) e voci controllate con `trascrivi.py`.
3. Per ogni video: miniatura orizzontale **e verticale**, titolo, descrizione, hashtag, tag, sottotitoli `.srt`, scritti in chat + file.
4. Prima di pubblicare: caricare **privato** su YouTube Studio per i controlli; "Realizzato per bambini"; categoria Istruzione; playlist "Cartoni Animati per Bambini 🐭🍪 Storie Brevi in Italiano | Bambini Ciao Ciao".
5. Ricordare il costo reale delle voci a pagamento per la versione monetizzata (le voci edge-tts sono una zona grigia commerciale).

---

## 10. CHECKLIST RAPIDA
- [ ] letto questo file + i 3 documenti
- [ ] `git branch -a`, `ls parco/assets/*`
- [ ] 1 generazione di prova (0,005); 402 = fermarsi
- [ ] niente VidIQ, niente personaggi nuovi, messaggi corti
- [ ] voci controllate con `trascrivi.py`
- [ ] video controllato fotogramma per fotogramma prima di inviarlo
- [ ] inviati: video, miniatura orizzontale, **miniatura verticale (da sola)**, `.srt`; testi scritti in chat
- [ ] commit + push sul branch; file temporanei puliti

---

## 11. MESSAGGIO DA INCOLLARE NELLA NUOVA CHAT
```
Riprendi Bambini Ciao Ciao.
Leggi `parco/docs/PASSAGGIO_Bambini_Ciao_Ciao_v4.md` nel repo kovacevstevo1993-gif/Tr, branch claude/nifty-brown-0jnc8w, e i tre documenti che cita. Rispetta le regole del §1 (risposte corte, niente VidIQ, niente personaggi nuovi, pochi crediti, controlla il repo prima di generare, controlla il video fotogramma per fotogramma prima di consegnarlo).
Fai prima UNA generazione di prova Pollinations, poi facciamo un nuovo Short con una storiella diversa, ambienti diversi e animati, personaggi che fanno quello che dice la narrazione, migliore dei due precedenti (Il barattolo misterioso, Il seme magico). Poi miniatura orizzontale e verticale, titolo, descrizione, hashtag, tag e sottotitoli.
```
