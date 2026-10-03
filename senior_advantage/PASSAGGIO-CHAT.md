# PASSAGGIO CHAT - The Senior Advantage (03/10/2026)

Incolla nella nuova chat: "Leggi senior_advantage/PASSAGGIO-CHAT.md e CLAUDE.md, poi aspetta quello che ti chiedo."

## REPO
kovacevstevo1993-gif/Tr, cartella /home/user/Tr. Ramo: claude/ecstatic-shannon-wl7kwf (fai git fetch). Commit e push sempre su quel ramo.
Leggere: CLAUDE.md, poi questo file. README.md e MEMORIA-CANALE.md non sono aggiornati: vale questo file. Chat vecchie in senior_advantage/chat/ (fino al 29/09).

## DUE CANALI SEPARATI, MAI MESCOLARE
1. The Senior Advantage (@TheSeniorAdvantage), cartella senior_advantage/. Sconti, benefici e aiuti per over 60 USA. Slide verde bosco e avorio (oro e rosso accenti). Short 1080x1920, lunghi 1920x1080. Circa 1.700 iscritti americani. Niente pensione, Medicare, tasse, Social Security come tema.
2. The Money Backstory (@TheMoneyBackstoryUSA), cartella money_backstory/. Pensione USA over 50, slide blu navy e oro. Ignorarlo in questa chat.

## REGOLE FERREE
- Rispondi SOLO a quello che chiedo, il minimo. Niente poemi, spiegazioni, riepiloghi, tabelle, note, offerte o domande non richieste. Niente scuse ne "hai ragione". Se serve un testo lungo, FAI UN FILE e mandalo con SendUserFile, non scriverlo in chat.
- Una cosa alla volta. Verifica prima di dare un'indicazione. Esegui SOLO quello che dico. Non rifare quello che ho gia montato. Non proporre di fermarmi.
- Non creare file o cartelle che non ho chiesto (tranne quando chiedo un file).
- Mai spendere crediti vidIQ senza chiedermi (saldo 145, si rinnovano il 25/10/2026).
- Dimmi PRIMA dove va ogni nuovo video (playlist, cosa creare o cancellare).
- Se chiedo il pacchetto: solo titolo, descrizione, tag, commento fissato gia completi da incollare (Subscribe e disclaimer compresi, niente segnaposto).
- Disclaimer solo nei video lunghi: slide finale in chiaro con la frase a voce nell'ultimo blocco, piu descrizione e commento fissato. Negli short solo nella descrizione.
- Fatti solo da fonti ufficiali. Niente promesse di guadagno. Contenuto originale.
- Testo per la voce CapCut: niente trattini (legge "dash"), niente cifre ne simboli, telefoni a parole con virgole, "snap" minuscolo.
- Poppins non ha i simboli check, freccia, stella. Non usare pkill -f. git checkout sui .pyc modificati prima di committare.
- Slide e grafica le fai tu col codice. Devono essere movimentate, dettagliate, con tanti oggetti disegnati.
- CONTROLLA le slide (fotogrammi in vari momenti) PRIMA di mandarle e correggi subito i difetti.
- Mandami i file in ordine e tutti insieme (MP4 con SendUserFile, mai nel repo).
- Sono molto nervoso quando aspetti o mi fai cercare le cose: veloce e preciso.

## COME LEGGERE LA TIMELINE CAPCUT
Durate dei blocchi dai miei screenshot, sempre dalla fine del blocco precedente. 30 fps. Numero in alto a sinistra = MM:SS / totale. Al massimo zoom circa 66,5 px per fotogramma: etichette sui fotogrammi pari, puntini sui dispari, etichetta centrata sul fotogramma. La riga bianca puo cadere tra due fotogrammi: arrotonda al piu vicino. L'etichetta "MM:SS" = fotogramma 0 di quel secondo. Se manca il numero di fotogrammi, chiedimelo.

## CODICE (senior_advantage/code/)
- Motore engine.py + eng2.py (pip install pillow numpy, serve ffmpeg).
- Short: scenes2.py..scenes5.py. Copertine: cover*.py. Video lungo 1: long1_*.py.
- Video lungo 2 (SNAP): long2_b01.py, long2_b02_05.py, long2_b06_10.py, long2_b11_15.py, long2_b16_20.py, long2_b21_37.py. Il testo di voce di ogni blocco e nei dizionari BLOCKS di quei file (blocco 1 in long2_b01.py).
- Uso: OUT=cartella SA_TMP=/tmp/x python3 long2_b21_37.py <blocco> [clip]. Blocchi 1-10: long2_b06_10.py <blocco>. 11-15: long2_b11_15.py. 16-20: long2_b16_20.py.
- Ogni processo ha il suo SA_TMP. 4 core, circa 5 fotogrammi/s in totale: lancia 4 processi in parallelo. Il container puo riavviarsi e uccidere i render: controlla i file finiti e rilancia solo i mancanti.
- person() non ha parametro colore (usa person2 in long2_b21_37.py).

## SHORT PUBBLICATI
1 e 2: playlist "Senior Discounts". 3 (Meals on Wheels, Eldercare Locator 1-800-677-1116) e 4 (bollette LIHEAP, 1-866-674-6327, energyhelp.us): playlist "aiuti".
Short 5 (SNAP, 3 regole, gancio solo 55 su 100 senior idonei prendono SNAP): da pubblicare, playlist "aiuti". Titolo: SNAP for Seniors 60+: 3 Income Rules Most Never Hear About. Video correlato = il video lungo SNAP (impostazioni: IA No, promozione No).

## VIDEO LUNGO 1 (pubblicato)
"Senior Discounts Start at 55, Not 65: 12 Hidden Places (Most Never Ask)", 11:01, vidIQ 94/100, playlist "Senior Discounts". Da fare: controllare gli orari dei capitoli, seconda miniatura per "Test e confronta".

## VIDEO LUNGO 2 (SNAP over 60) - STATO
Playlist "aiuti". 37 blocchi, circa 10.400 caratteri, 11-12 minuti, fonti USDA. Voce registrata in CapCut. Slide dei blocchi 1-37 fatte, controllate e mandate.
Fine di ogni blocco in fotogrammi (dalla mia timeline):
1022 1631 2306 2886 3524 4202 4868 5346 5915 6586
7098 7722 8220 8642 9106 9632 10124 10702 11373 12037
12572 13049 13723 14190 14960 15507 15913 16739 17351 17947
18488 19054 19655 20207 20925 21469 21955
La fine del blocco 21 (12572) e stimata da screenshot ridotto: se sulla mia timeline e diversa, rifare blocchi 21 e 22.
Blocco 37 = slide finale col disclaimer (modello anteprima/3-finale-disclaimer.png).

Struttura: 1-3 gancio (solo il 55% prende SNAP); 4-7 regola 1 (a 60 anni si salta il test sul reddito lordo); 8-20 detrazione standard, spese mediche sopra 35 dollari, spesa abitativa senza tetto, calcolo completo della donna di 68 anni, esempio ufficiale USDA da 434 dollari; 21-24 regola 3 (risparmi 4.750, casa non conta, auto, stati piu generosi); 25-27 nucleo familiare e nessun obbligo di lavoro; 28-33 come fare domanda in 3 passi, procedura urgente, rappresentante autorizzato, errori; 34-37 nuova legge 2025, riepilogo, invito a like e iscrizione, disclaimer.

Dati USDA verificati (dal 1/10/2026 al 30/9/2027, 48 stati e D.C.):
- Limite lordo 1 persona 1.729, netto 1.330. 2 persone: lordo 2.345, netto 1.804.
- Detrazione standard 217 (1-3 persone). Spese mediche: si detrae la parte sopra 35 al mese. Spesa abitativa: nessun tetto per over 60 (tetto 769 per gli altri).
- Risparmi 4.750 (3.000 per gli altri), casa non conta. Beneficio massimo 306 (1 persona), 562 (2 persone). Beneficio = massimo meno 30% del reddito netto (arrotondato in su).
- Over 60: solo test sul reddito netto. Nessun obbligo di lavoro per nuclei di soli anziani o disabili.
- Domanda presso l'ufficio SNAP dello Stato (fns.usda.gov/snap/state-directory), info 1-800-221-5689. Benefici dalla data della domanda, decisione entro 30 giorni, urgente entro 7 giorni.
- Partecipazione: 55% degli over 60 idonei, 32% se vivono con altri (anno fiscale 2022).
- Fonti: fns.usda.gov/snap/recipient/eligibility, /snap/eligibility/elderly-disabled-special-rules, /research/snap/national-participation-rates/fy20and22, /contact-us.

### Titolo
SNAP for Seniors 60+: The Income Rules Most People Never Hear About (Full Guide + Math)

### Descrizione
Only 55 out of 100 eligible seniors over 60 get SNAP. In this full guide you'll see the three rules that change everything after 60: you skip the gross income test, medical costs over $35 a month come off your income, and you can keep $4,750 in savings while your home doesn't count. We also run the math step by step, with USDA's own example, and show how to apply in three steps.

Official sources (USDA Food and Nutrition Service):
https://www.fns.usda.gov/snap/recipient/eligibility
https://www.fns.usda.gov/snap/eligibility/elderly-disabled-special-rules
https://www.fns.usda.gov/research/snap/national-participation-rates/fy20and22
SNAP information line: 1-800-221-5689
Find your state office: https://www.fns.usda.gov/snap/state-directory

Subscribe to The Senior Advantage: https://www.youtube.com/@TheSeniorAdvantage?sub_confirmation=1

Disclaimer: This video is general information, not financial or legal advice. Rules, amounts and ages change and differ by state. Always confirm with your official state SNAP office before you rely on them.

#SNAP #seniorbenefits #foodassistance #seniors #governmentbenefits

### Tag
SNAP for seniors, SNAP benefits for seniors, food stamps for seniors, SNAP eligibility seniors over 60, SNAP income limits seniors, SNAP medical deduction, how to apply for SNAP, senior food assistance, food assistance for seniors, EBT for seniors, government benefits for seniors, senior benefits, senior assistance programs, help with food costs seniors, SNAP rules 2026

### Commento fisso
Did you know about the $35 medical rule? Tell me below 👇 Rules and limits vary by state, so confirm with your state SNAP office. This is general information, not financial advice. If this helped you, please like and subscribe. It helps us a lot.

## DA FARE
1. Miniatura del video lungo SNAP (la frase la decido io).
2. Capitoli dalle mie fine-blocco (orari presi dalla timeline).
3. Pubblicare il video lungo e impostarlo come correlato dello short 5.
4. Poi: video CSFP (scatola mensile gratuita di cibo per over 60, USDA; verificare sui siti ufficiali prima del copione) o short 6.

## DATI vidIQ (US)
"senior discounts" 12.828/mese (conc. 26,3). "senior discount" 9.826. "senior citizen discounts" 4.821. "hidden senior discounts" 4.045. "senior savings" 3.786. "senior assistance programs" 4.229 (conc. 21). "low income relief" 24.886. "senior meals" 7.069. "snap benefits" 11.295 (+164%). "snap for seniors" 5.338 (conc. 28). "food stamps" 6.331 (+84%). "government benefits for seniors" 4.323 (conc. 19,6, la migliore).
Concorrenti: un video sulle regole SNAP per over 60 ha fatto 509.000 view da un canale da 22.000 iscritti; altri lo copiano e fanno 230.000. Canali di riferimento: Benefits Insider, Low Income Relief. Formula che funziona: gancio con numero o "rule nobody tells you", regole concrete, durata lunga per i video del cibo (8-20 min).

## MONETIZZAZIONE
Dal 1/2/2027 servono 8.000 ore o 20 milioni di view Short (oggi 1.000 iscritti + 4.000 ore): servono i video lunghi.
