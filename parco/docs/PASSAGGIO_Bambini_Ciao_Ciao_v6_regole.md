# Regole aggiunte in chat (v6) — leggere PRIMA di tutto
- **I file vanno SEMPRE inviati nella chat** (SendUserFile): video, miniatura verticale, .srt/.txt. Mai solo scrivere il percorso nel repo. L'utente non apre il repo.
- Sottotitoli: dentro il video sì (grandi, da cartone). Il file .srt solo se richiesto; se richiesto, inviarlo come file.
- Un solo rendering completo; correzioni locali con `short_mongolfiera.py renderpart <da> <a> out.mp4` e concatenazione.
- Motore più avanzato ora: `short_mongolfiera.py` (pendolo, parallasse, nuvole 3D). Short fatto: `short_mongolfiera_4_amici.mp4`.

## Chat 14/10/2026 — Short "Il pupazzo di neve" (topolino, Spike, elefantino)
- Saldo Pollinations finito (0,0001 pollen): anche la trascrizione costa. Soluzioni GRATIS usate:
  - immagini: modello gratuito Pollinations `community/scriptsnsenses-sys/flux-2-dev-free` (esce 1024x1024; ambienti ritagliati a 768x1376) -> `neve_free_pollinations.py` (ambienti neve_collina, neve_discesa, neve_sera; oggetti snowball, carrot, sled, pine). Non segue l'immagine di riferimento: va bene per ambienti/oggetti, non provato per pose.
  - pronuncia: `trascrivi.py` passa da solo a Whisper "medium" in locale (faster-whisper, modello in /tmp/claude-0/whisper) se Pollinations risponde 402.
- Motore: `short_neve.py` (base mongolfiera) + `voci_neve.py` (audioI/, parole.json con i tempi delle parole) + `mix_neve.py` + `miniatura_neve.py`. Video: `short_pupazzo_di_neve.mp4`. SEO: `docs/SEO_pupazzo_di_neve.md`.
- "Etciù" la voce lo legge "Et tu": usare "Ecciù".
- L'utente si lamenta della lentezza del rendering (~25 min per 44 s): bloom calcolato a 1/4 di risoluzione; usare renderpart per le correzioni.

## REGOLE NUOVE (15/10/2026, parole dell'utente) — valgono per TUTTI i prossimi Short
- "Falli più realistici i movimenti e tutto, creati altre posizioni dei personaggi, movimenti più naturali" -> generare pose nuove (passaggi, intermedie) prima di animare.
- "Non mettere i sottotitoli che non hanno senso" -> NIENTE sottotitoli nel video (solo hook/scritte di scena se servono).
- "Più centrale tutto" / "Perché i personaggi sono solo nella parte bassa e il resto è vuoto" -> personaggi GRANDI e al CENTRO dell'inquadratura (camera più vicina), niente metà alta vuota.
- "Fanne anche altri 2, falli diversi dagli altri perché sembrano tutti uguali, e migliorali" -> dopo il razzo, altri 2 Short con struttura/regia/ambienti diversi.
- 15/10: i modelli gratuiti Pollinations NON usano l'immagine di riferimento (flux-2-dev-free dà errore 400 su edits; sdxl-lightning-free inventa un altro personaggio: una volpe). Gemini: quota 0 (429). Pose nuove vere = solo con saldo Pollinations (klein).
- 15/10, utente: "Va bene anche la volpe" -> la volpe (/tmp -> assets/s/volpe.png) è ammessa come nuovo personaggio. Attenzione: col modello gratuito ogni immagine è una volpe diversa, quindi si anima solo con la sua unica immagine (deformazioni del motore).
- 15/10, utente: "È sempre un cambiamento, fai anche le altre storie, ingegnati per tutto, come fare e cosa fare, fai tutto te" -> decidere da soli storie, regia, asset, e consegnare.

## Short fatti il 15/10/2026 (tutti consegnati in chat con miniatura e testi; SEO in docs/)
- short_razzo_luna.mp4 (short_razzo.py: motore nuovo "corpo vivo" senza sottotitoli, personaggi grandi e centrali; base per i successivi)
- short_nascondino.mp4 (short_nascondino.py, volpe = assets/pose/volpe_salto.png, unica posa; bosco_autunno = bosco ricolorato)
- short_festa_sorpresa.mp4 (short_festa.py: stanza, luci spente/accese, candeline disegnate, panna sullo schermo, palloncini)
- I nuovi motori importano short_razzo e sostituiscono EV/JUMPS/VOICES. Correzioni locali: renderpart + concat ffmpeg.
- Trappola: word() trovava "soffia" dentro "soffiare": ora confronto esatto della parola.
- 15/10, utente: "Ci sono, puoi crearne finché ne vuoi di immagini gratis, devi farne una alla volta" -> VERIFICATO: flux-2-dev-free (generations) con SEED FISSO (42) + descrizione del personaggio identica + solo la posa che cambia, UNA richiesta ogni ~15 s, dà lo STESSO personaggio in pose diverse. Script: pose_free.py. Sfondo magenta se il personaggio ha vestiti verdi.
- 18/10, utente (arrabbiato): "Perché me lo mandi se non è perfetto?" -> REGOLA: mai mandare un video/pacchetto con un difetto noto (es. volpe con una sola posa nel nascondino). Prima si corregge, poi si manda; se qualcosa non si può correggere, dirlo PRIMA e chiedere, non mandarlo.
