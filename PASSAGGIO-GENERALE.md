# PASSAGGIO GENERALE - TUTTO IL PROGETTO DALLA A ALLA Z (aggiornato 07/10/2026)
Repo: kovacevstevo1993-gif/Tr, cartella /home/user/Tr. L'utente ha 4 progetti/canali SEPARATI (non mescolare mai). "Tutto" = tutto il progetto, non solo la chat corrente. Regole generali: CLAUDE.md (root). Un hook SessionStart carica senior_advantage/PASSAGGIO-CHAT.md.

## 1. The Senior Advantage (@TheSeniorAdvantage), cartella senior_advantage/
Sconti, benefici e aiuti per over 60 USA. Stato completo: senior_advantage/PASSAGGIO-CHAT.md. Chat intere salvate: senior_advantage/chat/ (10 file, ultima: 2026-10-07_sessione-01JMto9 = slide Costco). Ramo di lavoro piu recente: claude/affectionate-bell-7a1gzs (contiene TUTTO il lavoro Senior Advantage fino al 07/10/2026: video Costco con 63 slide in senior_advantage/video_costco/, 3 miniature in senior_advantage/miniature/, pacchetto in senior_advantage/PACCHETTO-VIDEO-COSTCO.md, codice in senior_advantage/code/). Per usarlo: git fetch origin; git checkout claude/affectionate-bell-7a1gzs.
Video Costco pronto da pubblicare (playlist "Senior Discounts"); dopo: lungo CSFP con scatola vera.

## 2. The Money Backstory (@TheMoneyBackstoryUSA), cartella money_backstory/
Pensione USA over 50. Per iniziare: money_backstory/START-QUI-NUOVA-CHAT.md. Lavoro piu recente (video 6 "2027 COLA", video 7 "500k", miniature video 7, "modello-unico"): ramo claude/lucid-cerf-4jmcl8 (65 commit non su main, ultimo 06/10 10:50 "Video 7: testi di pubblicazione + 3 miniature"). Chat in money_backstory/chat/. Altri rami: claude/money-backstory-project-bqq9ic (miniature, 01/10).

## 3. Conti in Pensione (@ContiInPensione), cartella conti_in_pensione/
Canale italiano sulla pensione. Regole: conti_in_pensione/REGOLE-FISSE.md (leggerlo SEMPRE per intero prima di rispondere). Lavoro piu recente (06/10, video lungo 3 rivalutazione 2027, regola n.8, stato, chat 4): rami claude/trusting-mendel-d1bg54 (ultimo 06/10 21:23, contiene anche i kit 06-09, 11, 12 piu vecchi) e claude/eager-davinci-vlhrsq (kit aggiornamento 06/10, STATO-06-10-2026.md). Kit precedenti: claude/new-session-79n9mt (05/10), claude/wizardly-galileo-uh8q18 (kit v2 04/10), claude/youthful-einstein-uctfje (kit completo 02/10). Nel repo main c'e solo REGOLE-FISSE.md.

## 4. Bambini Ciao Ciao (video per bambini, cartella parco/)
Animazioni per bambini (motore "Puliamo il parco!", short "Il seme magico", "La mongolfiera dei 4 amici"). Non e su main. Rami: claude/lucid-volta-myb2ye (07/10 base, documento di trasferimento), claude/fervent-johnson-ob5dk7 (documento di passaggio completo 03/10), claude/festive-brown-pk4m7q (passaggio v5: regole nuove, elefantino, motore castello; ULTIMO sul progetto bambini), claude/nifty-brown-0jnc8w (seme magico corretto), claude/zealous-mendel-8m8aas (mongolfiera, sottotitoli), claude/upbeat-einstein-f0m1jz (prova camminata topolino).

## Come ritrovare tutto
- Elenco rami: git fetch origin; git branch -r. Contenuto di un ramo: git log origin/<ramo> e git ls-tree.
- Tutte le chat di Claude Code dell'utente: tool list_sessions / list_events (titoli: "Canale YouTube Conti in Pensione", "The Money Backstory ...", "Bambini Ciao Ciao ...", "Senior ...").
- Per ogni canale: leggere il suo file di stato (sopra) PRIMA di fare qualsiasi cosa. Non chiedere all'utente cose che stanno nei file.
- main NON ha tutto: il lavoro recente di ogni canale e sui rami elencati. Non unire/cancellare rami senza ordine dell'utente.
