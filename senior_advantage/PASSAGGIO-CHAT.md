# PASSAGGIO CHAT - The Senior Advantage (aggiornato 04/10/2026)

Incolla nella nuova chat: "Leggi senior_advantage/PASSAGGIO-CHAT.md e CLAUDE.md, poi aspetta quello che ti chiedo."

## REPO
kovacevstevo1993-gif/Tr, cartella /home/user/Tr. Ramo: claude/ecstatic-shannon-wl7kwf (git fetch, checkout di quel ramo). Commit e push sempre su quel ramo.
Leggere SEMPRE prima: CLAUDE.md (regole), questo file (stato), RICERCHE-VIDIQ.md (tutte le ricerche vidIQ e analytics gia fatti: non rifarle, crediti limitati), MODELLO-DESCRIZIONE-VIDEO-1.md (pacchetto video lungo), MODELLO-PACCHETTO-SHORT.md (pacchetto short). README.md e MEMORIA-CANALE.md sono vecchi: vale questo file.
CHAT INTERE (testo completo, in senior_advantage/chat/): 2026-09-27_31 rilancio canale; 2026-10-01 sessione 01VdcN6 (video lungo 1, pacchetto, short 1-2, regole); 2026-10-01 sessione 01WeZD3 (short 4, copertine, video correlati); 2026-10-03 sessione 01LADT (short 5); 2026-10-03 sessione 01JUxym (slide video lungo 2); 2026-10-04 sessione 016BFAJ (short 6, pacchetti, miniature, regole). Per i dettagli di qualsiasi cosa: grep in quella cartella prima di chiedere all'utente.
Altre chat: leggibili anche con i tool list_sessions / list_events (sessioni utili: 01WeZD3EBshsBb5mxg9qdvnt = setup, short 4, pacchetto video 1; 01VdcN6aGh1CnYp1K1Fxe615 = pacchetto originale video 1; 01LADTs8xMTy5ijgQHHcdpHE = short 5; 01JUxymSGwEfoRbmuDNuBFFx = slide video lungo 2). Se manca qualcosa, cercarlo li e salvarlo nel repo, non chiederlo all'utente.

## DUE CANALI SEPARATI, MAI MESCOLARE
1. The Senior Advantage (@TheSeniorAdvantage), cartella senior_advantage/. Sconti, benefici e aiuti per over 60 USA. Slide verde bosco e avorio (oro e rosso accenti). Short 1080x1920, lunghi 1920x1080. Circa 1.700 iscritti americani. Niente pensione, Medicare, tasse, Social Security come tema.
2. The Money Backstory (@TheMoneyBackstoryUSA), cartella money_backstory/. Ignorarlo in questa chat.

## REGOLE FERREE (l'utente le ha ripetute centinaia di volte: non fargliele ripetere)
- SALVARE TUTTO subito nel repo (commit + push), senza che lo chieda. CONTROLLARE PRIMA come sono fatti i precedenti dello stesso tipo e rifarli IDENTICI; mai inventare formati nuovi.
- Rispondi SOLO a quello che chiedo, il minimo. Niente poemi, spiegazioni, riepiloghi, note, offerte, domande non richieste. Niente scuse ne "hai ragione". Una cosa alla volta. Non rifare quello che ho gia montato. Non proporre di fermarmi.
- COPIONI / BLOCCHI DI VOCE: sempre in chat, numerati, pronti da copiare in CapCut (mai in file). PACCHETTO (titolo, descrizione, tag, commento fisso): in chat, ogni campo in un blocco di codice, ordine: Dove va, Titolo, Descrizione, Tag, Commento da fissare, Impostazioni. Solo gli MP4 (e immagini) si mandano come file; passaggio chat = file.
- Descrizione: sul modello dei file MODELLO-*. NIENTE URL interi (https://...) tranne il link Subscribe; fonti = nomi pagine + dominio. DISCLAIMER sempre presente con etichetta "Disclaimer:" e frase "This channel is not affiliated with ..." (lunghi e short). Lunghi: anche slide finale + frase a voce nell'ultimo blocco + capitoli (orari dalla mia timeline). Tag lunghi: virgole senza spazi; tag short: virgola + spazio.
- Video correlato: si imposta SOLO sullo short (campo "Video correlato" nei dettagli), mai nel video lungo.
- Dimmi PRIMA dove va ogni nuovo video (playlist, cosa creare o cancellare).
- Mai spendere crediti vidIQ senza chiedermi (saldo 5, si rinnovano il 29/10/2026).
- Fatti solo da fonti ufficiali. Niente promesse di guadagno. Contenuto originale. Non scrivere "free" se non verificato.
- Voce CapCut: niente trattini, niente cifre ne simboli, telefoni a parole con virgole. "snap" parola minuscola; altre sigle a lettere separate: "C S F P", "U S D A", "L I H E A P"; siti "f n s dot u s d a dot gov". Vale per tutti i video e short.
- Gancio DIVERSO per ogni video ("Wait" gia usato negli short 5 e 6).
- Slide e grafica col codice (gratis): movimentate, dettagliate, tanti oggetti. Dal prossimo video: montaggio PIU DETTAGLIATO e slide che si capiscono meglio; ogni slide finisce DENTRO la sua frase (tutto completo e visibile prima del blocco dopo). CONTROLLA i fotogrammi prima di mandare. Mandami i file in ordine e tutti insieme.
- Miniature: 3 versioni diverse per test A/B, una coerente con la prima del video (verde, numero gigante). Frase scelta da me se l'utente non la da. Font Montserrat ExtraBold.
- Poppins non ha check, freccia, stella. Non usare pkill -f. git checkout sui .pyc modificati prima di committare.
- Sono molto nervoso quando aspetti o mi fai cercare le cose: veloce e preciso.

## COME LEGGERE LA TIMELINE CAPCUT
Durate dei blocchi dai miei screenshot, sempre dalla fine del blocco precedente. 30 fps. Numero in alto a sinistra = MM:SS / totale. Al massimo zoom circa 66,5 px per fotogramma: etichette sui fotogrammi pari, puntini sui dispari, etichetta centrata sul fotogramma. La riga bianca puo cadere tra due fotogrammi: arrotonda al piu vicino. L'etichetta "MM:SS" = fotogramma 0 di quel secondo. Se manca il numero di fotogrammi, chiedimelo.

## CODICE (senior_advantage/code/)
- Motore engine.py + eng2.py (pip install pillow numpy, serve ffmpeg).
- Short: scenes2.py..scenes6.py (uso S6_OUT=cartella python3 scenes6.py <clip>). Copertine: cover*.py (cover6.py = short 6). Miniature video lungo: thumb_long1*.py, thumb_long2.py (3 versioni video 2). Video lungo 1: long1_*.py.
- Video lungo 2 (SNAP): long2_b01.py, long2_b02_05.py, long2_b06_10.py, long2_b11_15.py, long2_b16_20.py, long2_b21_37.py. Il testo di voce di ogni blocco e nei dizionari BLOCKS di quei file (blocco 1 in long2_b01.py).
- Uso: OUT=cartella SA_TMP=/tmp/x python3 long2_b21_37.py <blocco> [clip]. Blocchi 1-10: long2_b06_10.py <blocco>. 11-15: long2_b11_15.py. 16-20: long2_b16_20.py.
- Ogni processo ha il suo SA_TMP. 4 core, circa 5 fotogrammi/s in totale: lancia 4 processi in parallelo. Il container puo riavviarsi e uccidere i render: controlla i file finiti e rilancia solo i mancanti.
- person() non ha parametro colore (usa person2 in long2_b21_37.py).

## SHORT PUBBLICATI
1 e 2: playlist "Senior Discounts". 3 (Meals on Wheels, Eldercare Locator 1-800-677-1116) e 4 (bollette LIHEAP, 1-866-674-6327, energyhelp.us): playlist "aiuti".
Short 5 (SNAP, 3 regole): da pubblicare, playlist "aiuti"; pacchetto completo in MODELLO-PACCHETTO-SHORT.md. Dopo la pubblicazione del video lungo SNAP: sullo short 5 impostare Video correlato = video lungo SNAP.

## SHORT 6 (CSFP, scatola di cibo mensile over 60) - FATTO IL 04/10
Slide fatte e mandate (8 clip, senior_advantage/code/scenes6.py, uso: S6_OUT=cartella python3 scenes6.py <clip>). Durate in fotogrammi: 375 170 160 324 246 345 279 112. Playlist "aiuti". Blocco 7 voce: "snap" minuscolo. Fonti: fns.usda.gov/csfp/commodity-supplemental-food-program, /csfp/factsheet, /csfp/applicant-recipient, /csfp/program-contacts. Il sito USDA da' 130% o 150% del livello di poverta: non citare percentuali. "Free" non verificato: non usarlo.

Voce blocchi 1-8 (testo nel codice scenes6.py e qui):
1 Wait. Once a month, the government can send you a box of food. And almost no one over sixty knows it exists. Stay to the end, because I'll show you where to check if you can get it.
2 It's called C S F P, the Commodity Supplemental Food Program, run by the U S D A.
3 The rule is simple. You must be at least sixty years old, and have a low income.
4 Inside the box, you can find milk, cheese, juice, cereal, rice, pasta, peanut butter, and dry beans. Plus canned meat, fruit and vegetables.
5 But here is the catch. Every state sets its own income limit. And the program is not available in every area.
6 So contact your state agency. The list is on the U S D A website, f n s dot u s d a dot gov, slash c s f p, slash program contacts.
7 This is one of many benefits most seniors never claim. Want another one? Watch my short about the three snap rules. Click below.
8 Follow The Senior Advantage, so you don't miss the next one.

Pacchetto short 6 (formato short 4, fatto il 04/10): playlist "aiuti"; video correlato = video lungo SNAP (dopo la pubblicazione); IA No; promozione No. Copertina: senior_advantage/code/cover6.py ("MONTHLY FOOD BOX", scatola CSFP, "WHO GETS IT?", "NOBODY TELLS YOU").
Titolo: CSFP: Monthly Food Box for Seniors 60+ Most Never Hear About
Descrizione (testo esatto, struttura = short 5):
Monthly food box for seniors 60+: CSFP, the Commodity Supplemental Food Program, is a USDA program for adults age 60 and older with low income. It supplements their diet with a monthly package of USDA foods. Each state sets its own income limit, and the program is not available in every area.

To apply, contact your state CSFP agency (fns.usda.gov/csfp/program-contacts)

Sources: USDA CSFP program page, USDA CSFP fact sheet, USDA CSFP applicant information (fns.usda.gov)

Subscribe for more help most seniors never claim: https://www.youtube.com/@TheSeniorAdvantage?sub_confirmation=1

Disclaimer: Rules, amounts and ages change and differ by location and plan. Always confirm with the official source before you rely on them. General information, not financial advice. This channel is not affiliated with the USDA or any government agency.

#Shorts #CSFP #seniorbenefits #foodassistance
Tag: CSFP, commodity supplemental food program, monthly food box for seniors, food box for seniors, senior food assistance, food assistance for seniors over 60, USDA food program for seniors, CSFP food package, how to get CSFP, help with groceries for seniors, low income seniors food help, government benefits for seniors, senior benefits, senior assistance programs
Commento fisso: Did you know CSFP existed? Tell me below 👇 Rules and limits vary by state, so contact your state agency to confirm. The full video about SNAP is right below this short.
Stato: slide, copertina e pacchetto FATTI; da pubblicare (playlist "aiuti"). Video correlato = video lungo SNAP (impostarlo sullo short dopo la pubblicazione del lungo).

## VIDEO LUNGO 1 (pubblicato)
"Senior Discounts Start at 55, Not 65: 12 Hidden Places (Most Never Ask)", 11:01, vidIQ 94/100, playlist "Senior Discounts". Pacchetto completo (titolo, descrizione con capitoli, tag, commento): MODELLO-DESCRIZIONE-VIDEO-1.md. Da fare: controllare gli orari dei capitoli, seconda miniatura per "Test e confronta".

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

### Titolo (pacchetto video lungo 2, da incollare)
SNAP for Seniors 60+: The Income Rules Most People Never Hear About (Full Guide + Math)

### Descrizione (formato = senior_advantage/MODELLO-DESCRIZIONE-VIDEO-1.md; capitoli dalle fine-blocco dell'utente)
Only 55 out of 100 eligible seniors over 60 get SNAP, and most never hear why. In this video you'll see the three rules that change everything after 60: you skip the gross income test, medical costs over $35 a month come off your income, and you can keep $4,750 in savings while your home doesn't count. We run the math step by step with USDA's own example, and show how to apply in three steps.

The one rule to remember: never decide by yourself that you earn too much. Apply and let your state SNAP office decide.

CHAPTERS
0:00 Only 55 out of 100 seniors get SNAP
0:34 What is SNAP?
0:54 Why most seniors never apply
1:16 Rule 1: you're elderly at 60
1:36 The two income tests
1:57 The income limits
2:20 Example: $1,800 Social Security
2:42 Deductions: gross to net income
2:58 Rule 2: medical costs
3:17 What counts
3:39 What doesn't count
3:56 Shelter costs
4:17 Rent, mortgage, taxes and utilities
4:34 The full math: step 1
4:48 Step 2: medical
5:03 Step 3: shelter
5:21 The net income test
5:37 How much she gets
6:19 USDA's own example
6:41 Rule 3: savings
6:59 Your home doesn't count
7:14 What about your car?
7:53 Who's in your household
8:18 Why seniors who live with others miss out
8:36 No work requirement
8:50 How to apply: 3 steps
9:58 Need food fast? Urgent help
10:16 Can't leave the house?
10:35 Mistakes that cost you SNAP
10:55 The new 2025 law
11:13 Quick recap
11:37 Before you go

Sources: official pages of the USDA Food and Nutrition Service (fns.usda.gov).

Subscribe to The Senior Advantage: https://www.youtube.com/@TheSeniorAdvantage?sub_confirmation=1

Disclaimer: Rules, amounts and ages change and differ by state. Always confirm with your official state SNAP office before you rely on them. General information, not financial or legal advice. This channel is not affiliated with the USDA or any government agency.

#snapbenefits #seniorbenefits #over60

### Tag
SNAP for seniors,SNAP benefits for seniors,food stamps for seniors,SNAP eligibility seniors over 60,SNAP income limits seniors,SNAP medical deduction,how to apply for SNAP,senior food assistance,food assistance for seniors,EBT for seniors,government benefits for seniors,senior benefits,senior assistance programs,help with food costs seniors,SNAP rules 2026

### Commento fisso
Did you know about the $35 medical rule? Tell me below 👇 Rules and limits vary by state, so confirm with your state SNAP office. This is general information, not financial advice. If this helped you, please like and subscribe. It helps us a lot.

## DA FARE (in ordine)
1. Pubblicare video lungo SNAP (pacchetto sopra; playlist "aiuti"; IA No; promozione No; schermata finale 20 s) con 1 delle 3 miniature (A verde "ONLY 55 OUT OF 100", B nonno "THE $35 RULE", C chiara "SKIP THE INCOME TEST"): test A/B.
2. Pubblicare short 5 e short 6 (playlist "aiuti"); poi impostare su entrambi Video correlato = video lungo SNAP.
3. Controllare gli orari capitoli del video 1 e fare la seconda miniatura per "Test e confronta".
4. Prossimo video lungo: CSFP (scatola mensile di cibo over 60, USDA; verificare sui siti ufficiali prima del copione: soglia reddito 130% o 150%? "free"? numero di Stati?) o altro short. Gancio nuovo, montaggio piu dettagliato.

## DATI vidIQ (US)
"senior discounts" 12.828/mese (conc. 26,3). "senior discount" 9.826. "senior citizen discounts" 4.821. "hidden senior discounts" 4.045. "senior savings" 3.786. "senior assistance programs" 4.229 (conc. 21). "low income relief" 24.886. "senior meals" 7.069. "snap benefits" 11.295 (+164%). "snap for seniors" 5.338 (conc. 28). "food stamps" 6.331 (+84%). "government benefits for seniors" 4.323 (conc. 19,6, la migliore).
Concorrenti: un video sulle regole SNAP per over 60 ha fatto 509.000 view da un canale da 22.000 iscritti; altri lo copiano e fanno 230.000. Canali di riferimento: Benefits Insider, Low Income Relief. Formula che funziona: gancio con numero o "rule nobody tells you", regole concrete, durata lunga per i video del cibo (8-20 min).

## MONETIZZAZIONE
Dal 1/2/2027 servono 8.000 ore o 20 milioni di view Short (oggi 1.000 iscritti + 4.000 ore): servono i video lunghi.

## ID VIDEO PUBBLICATI E CAPITOLI (verificato il 06/10/2026 leggendo YouTube)
- Video lungo 1: id Tqw_9LMUJYE. Titolo pubblicato SENZA due punti e parentesi: "Senior Discounts Start at 55, Not 65 12 Hidden Places Most Never Ask". Descrizione corretta con 23 capitoli (tutti link), ma YouTube NON ha creato i segmenti nella barra (nessun chapterRenderer).
- Video lungo 2 (SNAP): id KDYxb4tKm1Q. Pubblicato, 33 capitoli, i segmenti nella barra funzionano.
- Differenza trovata: nel video 1 i titoli dei capitoli hanno "#" ("#1 Denny's and IHOP") e parentesi; nel video 2 no. Causa non certa. Fix da provare: ri-salvare la descrizione del video 1 con i capitoli senza "#".
- Filigrana canale: senior_advantage/filigrana-senior-advantage.png (codice code/watermark.py), da caricare in Studio > Personalizzazione > Branding.

## AUDIT CANALE (06/10/2026, dati pubblici YouTube, 0 crediti vidIQ)
- Canale: 1,71K iscritti, 8 video (2 lunghi, 6 short). Lungo 1 (Tqw_9LMUJYE): 1 view dopo 4 giorni. Lungo SNAP (KDYxb4tKm1Q): 5 view dopo 1 giorno. Short: CSFP 15, SNAP 58, LIHEAP 35, Meals on Wheels 30, sconti 77 e 84 view.
- Problemi trovati: (1) descrizione canale dice "over 50" e keyword con Social Security, Medicare, Medicaid, VA, scams: fuori tema; (2) titolo video 1 pubblicato senza ":" e "()"; (3) capitoli video 1 non creati (vedi sopra); (4) miniatura video 1 "STOP PAYING FULL PRICE" non coerente col titolo "55 not 65", 6 cartellini illeggibili; stesso nonno su entrambi i video; (5) nessuno short ha il Video correlato verso un lungo; descrizioni degli short 1-5 pubblicati senza "Disclaimer:", short 3/4/5 con link https interi; (6) iscritti vecchi non attivi (audience di prima).
- Concorrenti che vanno: "New Food Assistance Rules for Seniors Start October 1 (One Erases Your Old Denial)" 530K e 231K; "15 Places Seniors DON'T know give BIG Discounts" 462K; "15 HIDDEN Costco Senior Discounts" 335K; "15 Hidden Senior Discounts Aldi Never Advertises" 66K; serie "What's inside a senior commodity food box?" (CSFP, scatola vera mostrata) 45K-58K a video. Formula: urgenza con data, marchio famoso (Costco, Aldi, Walmart), numero, contenuto reale mostrato. Tanti copiano e fanno 2-500 view.
- Da fare: titolo video 1 con ":" e "()"; descrizione canale su over 60 aiuti e sconti, via keyword fuori tema; miniatura A sul video 1; Video correlato su tutti gli short; descrizioni short aggiornate; prossimi lunghi con marchio famoso (Costco, Walmart, Aldi) e CSFP scatola; titoli con urgenza/data. Servono da Studio: impressioni e CTR del video 1 e del SNAP.

## DATI vidIQ/ANALYTICS (06/10/2026, autorizzati dall'utente; spesi 35 crediti, saldo 30, rinnovo 25/10/2026)
- Ultimi 30 giorni: circa 225 view totali. Fonti: ricerca YouTube 156 (69%), feed Shorts 62, iscritti 2, browse e suggeriti 0. YouTube non consiglia i video: arrivano solo da ricerca.
- Short: ritenzione buona (durata media 21-40 s, 55-120% guardato). Top: XCRw0E4eTaE 76 view, sj4vzbjii_k 62, bkZ8pOaoX3g 30, 96JkWmUbRF4 30, EGDTj4NTlQw 26. Iscritti guadagnati in 30 giorni: 1. Video lungo 1: 1 view, 0 minuti.
- Punteggio miniatura vidIQ: video 1 (nonno STOP PAYING FULL PRICE) 60/100 (poca energia, composizione sbilanciata, faccia troppo grande); SNAP (nonno THE $35 RULE) 77/100.
- Piccoli canali che esplodono: Robin MBA (6,3K iscritti) "New Food Assistance Rules for Seniors Starting This October 1 (One Erases Your Old Denial)" 231K. The Smart Steward (8,4K iscritti) "Aldi Is Hiding 15 Discounts From Seniors Over 60 (Here's Every One)" 21K e "Costco Is Hiding 17 Discounts From Seniors Over 60 (Here's Every One)" 11K, 10 minuti. Scatola senior mensile (CrazyForJesus) "Senior box for September 2026" 7,6K.
- Parole chiave US: "costco for seniors" 5.235 ricerche/mese, concorrenza 12,3 (ottima); "costco senior discount" 3.269, conc. 19; "senior discounts" 8.964 ora contro 20.150 di base (-55%, in calo); "costco membership" 18.372 (+85%); "costco deals" 40.773 (+183%).

## SISTEMAZIONE CANALE, PASSI FATTI E VERIFICATI SU YOUTUBE (06/10/2026)
1 titolo video 1 rimesso con ":" e "()"; 2 capitoli video 1 funzionanti (24 segmenti); 3 miniatura video 1 = miniature/video-lungo-1-55-not-65.png; 4 descrizione canale riscritta (over 60, sconti e aiuti); 5 parole chiave canale senza Social Security/Medicare/VA.
Passo 6 in corso: Video correlato sugli short, uno alla volta. Sconti (XCRw0E4eTaE "Senior Discounts Start at 55 - Not 65", sj4vzbjii_k "Senior Discounts Nobody Tells You About") -> video 1 (Tqw_9LMUJYE). Aiuti (96JkWmUbRF4 SNAP, bkZ8pOaoX3g Meals on Wheels, EGDTj4NTlQw LIHEAP, Mk6ZIS9JMBQ CSFP) -> video SNAP (KDYxb4tKm1Q). Poi: descrizioni short 1-5 con "Disclaimer:" e senza https.
Regola: verificare SEMPRE su YouTube (curl innertube /next, /oembed, browse) ogni passo fatto dall'utente prima di dare il successivo.
Passo 6 FATTO (06/10/2026): Video correlato impostato su tutti i 6 short (sconti -> video 1; SNAP, CSFP, LIHEAP, Meals on Wheels -> video SNAP).
Passo 7 in corso: descrizioni degli short 1-5 pubblicati da rifare con "Disclaimer:" e senza https (modello MODELLO-PACCHETTO-SHORT.md), uno alla volta: SNAP, LIHEAP, Meals on Wheels, sconti (2).
Passo 7 FATTO e verificato su YouTube (06/10/2026): descrizioni dei 6 short con "Disclaimer:" e senza https (SNAP, LIHEAP, Meals on Wheels, sconti x2, CSFP).
Prossimo passo 8: nuovo lungo con marchio famoso (Costco), formato "X Is Hiding N Discounts From Seniors Over 60 (Here's Every One)", poi lungo CSFP con scatola vera. Gancio nuovo, slide piu dettagliate.
