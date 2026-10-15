# VIDEO 9 - LAVORO DA FARE NELLA CHAT NUOVA (15/10/2026). Leggere SOLO questo + money_backstory/REGOLE-UTENTE-05-10.md
Branch: claude/wonderful-volta-0848iy (git fetch origin claude/wonderful-volta-0848iy; git checkout origin/claude/wonderful-volta-0848iy).

## Cosa fare: SOLO la voce dei blocchi 13-30. LE SLIDE NON SI RIFANNO (ordine utente).
- Errore da correggere: b1-b12 voce gemini-2.5-flash-preview-tts, b13-b30 gemini-3.1-flash-tts-preview (modello diverso). Tutto deve essere gemini-2.5-flash-preview-tts, voce Fenrir, testo SENZA istruzioni davanti.
- Testi dei blocchi: copione-video9.md (BLOCCO 13 ... BLOCCO 30). Script: code/tts.py - gruppi da 3 blocchi = 6 richieste: python3 code/gen_voce.py code code/blk_13_30.json voce (gia pronto); poi code/ritaglia.py code/blk_13_30.json voce/gNN.wav NN,NN+1,NN+2 per tagliare ai confini; controllo testo con code/verifica_voce.py. Prima di generare: cancellare voce/g13..g28.wav vecchi (altrimenti li riusa).
- Se la quota finisce: FERMARSI e aspettare, MAI cambiare modello.
- Controllo voce uguale: Gemini (gemini-3.8-flash o altro disponibile) ascolta b12.wav e b13.wav nuovi e conferma stessa voce; piu' confronto numerico di altezza e velocita'.

## Come adattare SENZA rifare le slide
- Le slide di ogni blocco (slide/v9-bNN-*.mp4) restano identiche. La durata di ogni blocco e' fissa: fotogrammi = fine_blocchi.txt[n] - fine_blocchi.txt[n-1].
- Per ogni blocco 13-30: durata obiettivo voce = fotogrammi/30 - 0,25 s. Se la voce nuova e' piu' corta: aggiungere silenzio alla fine. Se e' piu' lunga: accelerare leggermente con ffmpeg atempo (rapporto = nuova/obiettivo, ammesso fino a 1,08; oltre, dirlo all'utente). Poi apad fino ai fotogrammi esatti -> voce/bNN_pad.wav.
- Unire: python3 code/unisci.py 13-30 (slide gia' fatte + voce nuova). Controllare che i fotogrammi di ogni file = attesi (lo script stampa OK).

## Consegna (ordine utente)
- Mandare TUTTI i 30 file in ordine, V9-blocco01 ... V9-blocco30 (1-12 gia' fatti in consegna/ se presenti; se la cartella consegna/ non c'e' perche' e' in .gitignore, rigenerarli con code/unisci.py 1-30 dopo aver rifatto i *_pad.wav di 1-12 dai voce/bN.wav con lo stesso calcolo dei fotogrammi).
- Risposte cortissime, niente spiegazioni. Salvare lo stato in money_backstory/START-QUI-NUOVA-CHAT.md, commit e push.
