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
