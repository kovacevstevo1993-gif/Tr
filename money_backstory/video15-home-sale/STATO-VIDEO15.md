# VIDEO 15 - VENDERE CASA DOPO I 65 ANNI (28/10/2026) - STATO
- Tema scelto da ricerca gratuita (curl YouTube 28/10) + vidIQ (15 crediti: saldo 22 -> 12; keyword 'social security payment schedule' <750/mese, scartato; title score 96). check_tema.py: zero HIT. Titolo: "Every Senior Must Know This Before Selling Their Home After 65 (Tax and Medicare Trap)" (96). Playlist: "Retirement After 50" (da creare, non esiste).
- Fonti: FONTI-VERIFICATE.md + fonti/ (IRS Pub 523 2025, Topic 701/409/559/423, Pub 915, Rev. Proc. 2025-32, CMS fact sheet 2026, SSA POMS HI 01101.010).
- Copione 22 blocchi: code/mkblk.py -> code/blk.json (NON mandare il copione all'utente, regola 26/10). Personaggi fittizi Ray e Donna (72, congiunta, base $200.000, vendita $900.000, guadagno $646.000, tassabile $146.000, IRMAA 2026 +$81,20 a testa = $1.948,80).
- Voce: gemini-2.5-flash-preview-tts Fenrir, gruppi 1-3,4-6,7-9,10-12,13-15,16-18 FATTI (code/gen2.sh + code/post.sh = atempo + ritaglia3). Gruppo 19-22 NON fatto: quota 10 richieste/giorno finita il 28/10 (2 errori 502 contano). Riprovare dopo le 07:00 UTC del 29/10: ./code/gen2.sh 19,20,21,22 poi ./code/post.sh 19,20,21,22, poi chk.py 19..22, make_sync.py, slide, qa, consegna.
- Slide: motore code/homeeng.py (+v13eng/v14eng copiati), slide code/v15.py (22 blocchi), anteprime: PV=1 OUT=../pv/ python3 v15.py preview N; code/sheets.py; code/chkcue.py (cue nella voce); timing con code/timing14.py/cue_first.py adattati.
- DA FARE: voce 19-22, make_sync, render (xargs -P4), qa15 su ogni fotogramma, pad.py + unisci.py (rinominare V15), miniature, pacchetto, SendUserFile.

## AGGIORNAMENTO 28/10 sera
- Voce blocchi 1-18 controllata (small/base/tiny/medium/large-v3): copione allineato alla voce ("claim", "is not remarried"). sync.json con numeri espansi (make_sync.py corretto: riprova senza prompt se copertura <0,85).
- Slide 1-18 RENDERIZZATE (56 slide, 16.472 fotogrammi) e qa15 su ogni fotogramma: tutte OK. pad.py + unisci.py: consegna/V15-blocco01..18.mp4 (fotogrammi = durata voce, tutti OK; non nel repo, rigenerabili).
- Miniature A/B fatte: miniature_video15/ (code/thumbs_video15.py). Pacchetto: PUBBLICAZIONE-VIDEO15.md (code/mkpack.py: capitoli dai fine_blocchi; riesegue dopo la voce 19-22; tag da aggiornare con 'capital gains').
- Manca SOLO: voce 19-22 (quota Gemini dopo le 07:00 UTC 29/10; send_later gia' programmato 07:10 UTC), poi: post.sh, chk.py 19..22, make_sync.py (cancellare sync.json prima), render 19-22, qa15, pad, unisci 19-22, mkpack.py, SendUserFile (MP4 1-22 + 2 miniature) + pacchetto in chat.

## 29/10 mattina: VIDEO 15 COMPLETO E CONSEGNATO
- Voce 19-22 generata alle 07:20 UTC (gruppo 19-22 dava 502 due volte: fatto 19-21 e 22 a parte; atempo 0,763 e 0,779). Controllata con small/base/tiny/medium/large-v3. make_sync (blocchi 1-18 in cache), slide 19-22 rifatte con tagli sulla voce (19: intro + 3 slide a icone), render, qa15 su ogni fotogramma: 11 slide / 4.048 fotogrammi OK (totale video: 67 slide OK). unisci: consegna/V15-blocco01..22.mp4, fotogrammi = durata voce per tutti, totale 20.520 fotogrammi = 11:24.
- Pacchetto aggiornato (capitoli reali, tag + 'capital gains' 437 caratteri) in PUBBLICAZIONE-VIDEO15.md; miniature in ../miniature_video15/.
- APERTO: schermata finale/WATCH NEXT -> video 1; playlist "Retirement After 50" da creare; prossimo video: check_tema.py prima di tutto.
