# THE MONEY BACKSTORY — KIT COMPLETO (aggiornato 02/10/2026)
Tutto quello che c'è nelle chat e che Claude sa sul canale. Leggi PRIMA questo file, poi usa il codice (cartella 04) senza cambiare lo stile.

## 0. Indice cartelle
- 01-documenti-precedenti: chat completa 23-28/09, cronologia correzioni, riassunto canale, guida stile e metodo (kit del 28/09)
- 02-chat-questa-sessione: chat 29/09-02/10 leggibile (video 5 slide blocchi 1-31, regole monetizzazione, testi video 3 e 5)
- 03-memoria: preferenze dell'utente + note
- 04-codice: TUTTO il codice delle slide (common.py, common2.py, v3lib, v4*, v5lib, v5b*, blocchi video 1 e 2, miniature) + v5/blocks.py
- 05-copioni: copioni video 1-5
- 06-immagini: miniature fatte, riferimenti stile slide, anteprime video 5, logo
- 07-testi-pubblicazione: titolo/descrizione/tag/commento fissato video 3 e video 5
- 09-screenshot-timeline-ricevuti: tutti gli screenshot della timeline CapCut mandati in questa sessione
- 10-video-slide-video5-mp4: i 93 MP4 delle slide del video 5 (blocchi 1-31)
- 08-font: Gloock + InstrumentSans (nel codice il percorso è F='/mnt/skills/examples/canvas-design/canvas-fonts/' in common.py: cambiarlo con la cartella 08-font)

## 1. Il canale
- Nome: The Money Backstory, handle @TheMoneyBackstoryUSA, creato il 25/09/2026 (account Google di True Story Video, via Chrome desktop). Faceless. Inglese. Pubblico: americani over 50 (pensione). Logo MB oro con grafico, banner "Subscribe for new videos", paese Italia, non per bambini, caricamento predefinito: Istruzione, inglese, fonti + disclaimer, filigrana, doppiaggio automatico attivo.
- Obiettivo: guadagnare con CPM alto (finanza 15-50 $, RPM 7-25 $). Nicchia: pensione USA + Social Security, Medicare, tasse in pensione, debiti dopo i 50, truffe agli anziani, casa. Mai cripto/trading/finanza per giovani.
- Diverso da: The Senior Advantage (vecchio canale 1.700 iscritti, sconti/benefici anziani USA, slide verticali verde bosco/avorio) e da The Real Backstory/True Story Video (storie vere). NON mescolare.

## 2. REGOLE FISSE (applicare sempre senza che lui le ripeta)
1. Formato provato dei video simili che funzionano; niente storie d'archivio; distinguersi con qualità (slide animate blu/oro, numeri verificati).
2. Durata oltre 10 minuti (dal video 2). Aggancio: prima frase con cifra precisa che sorprende + promessa/mistero ("il numero 4 sorprende quasi tutti"); mappa dei punti all'inizio; frasi ponte; dubbi anticipati; numeri a strati tradotti in spese quotidiane; Frank e Mary (presentati da zero in OGNI video, mai "remember"); confronto finale; like/iscrizione solo alla fine + rimando al video successivo.
3. Tutti i dati ufficiali e controllati su più fonti (ssa.gov, medicare.gov, cms.gov, irs.gov, Fidelity, HHS); se discordano: il più recente e prudente. Numeri scritti in lettere nel copione (per la voce).
4. Voce: CapCut "Analista preciso", ≈14 caratteri/s (12-16). Se la durata non torna col testo avvisare subito (manca un pezzo di frase).
5. Niente musica, niente sottotitoli nel video finale (restano quelli automatici di YouTube).
6. Caricamento: IA "No", promozione "No"; schermata finale con video nel riquadro tratteggiato dell'ultima slide + Iscriviti. Nessuna promessa "every week".
7. Per ogni video: titolo, descrizione (parola chiave nella prima frase, capitoli ai tempi reali, fonti, disclaimer, riga Subscribe, 3 hashtag), tag, commento fissato, miniatura aggressiva. Dire PRIMA in quale playlist va.
8. Non spendere crediti vidIQ senza dirgli il costo e chiedere (55 crediti il 30/09/2026, rinnovo 29/10/2026; ricerca nuova ≈5 crediti). Usare ricerca web gratuita.
9. REGOLE MONETIZZAZIONE YOUTUBE (letto sulla pagina ufficiale, 29/09/2026): la norma "inauthentic content" vieta slideshow/testo/voce senza commento o valore educativo, video a stampo con variazione minima, e "persone AI" che danno consigli di finanza/salute/legge. Quindi: il narratore spiega, non si presenta come consulente; mai "ti consiglio", "nella mia esperienza", "tu dovresti"; disclaimer "educazione, non consulenza" in ogni video; fonti ufficiali citate a schermo; calcoli ed esempi originali; struttura e grafiche variate da un video all'altro. Nessuna garanzia assoluta.
10. Prima di consegnare slide: guardare i VIDEO MP4 finiti (frame estratti dai file, non solo le anteprime) e correggere da soli.

## 3. METODO DI PRODUZIONE
1. Claude prepara il copione completo (blocchi numerati, un blocco = una voce CapCut) e lo consegna intero in un messaggio in riquadri di codice.
2. Lui genera la voce di ogni blocco in CapCut e manda screenshot della timeline (o una registrazione schermo).
3. Claude legge la fine voce in SECONDI + FOTOGRAMMI a 30 fps (la fine è frazionaria) e calcola il tempo assoluto: (min×60+sec)×30+frame. Durata blocco = END[n]−END[n−1].
4. Lettura righello (screenshot telefono 720×1610): cursore a x=360, ~67 px per fotogramma, etichette "Nf" sui numeri pari centrate sui tick, i punti sono i dispari; se compare "MM:SS" nel righello è il fotogramma 0 del secondo. Frazione = etichetta + (360 − x_etichetta)/67. Solo i suoi screenshot decidono le durate (mai calcoli sul testo).
5. Claude fa le slide animate MP4 1920×1080 30 fps che coprono esattamente il tratto, ogni slide 4-12 s, un grafico/oggetto diverso per slide, tutte le slide di un blocco nello stesso messaggio in ordine. Poi controlla i video finiti (ffprobe frame totali = durata; contact sheet 5/40/75/99%).
6. Lui mette le slide in CapCut, toglie i sottotitoli, esporta, carica.
- Rendering: `python3 v5b21_31.py preview 21,22` (anteprima), `render 21,22` (MP4 in /mnt/user-data/outputs/v5-b{n}-0{i}.mp4). 2 CPU: due processi in parallelo con `setsid nohup ... &`; ~33 slide in 4-5 minuti.

## 4. STILE VISIVO (identico in tutti i video)
- Sfondo blu notte con particelle d'oro e luce che passa; cornice 3D oro con bagliore ai lati; titolo in alto in Gloock (serif) oro; testi InstrumentSans Bold/Regular.
- Palette: navy (10,24,40); card (22,40,64); gold (212,172,82); goldL (246,214,140); white (236,240,245); red (232,84,84); green (84,200,124); blue (110,160,230); purple (170,130,230); grey (150,165,185).
- Oggetti a tema: monete, pile di monete, banconote, sacco di soldi, portafoglio, valigetta, lucchetto, calendari (cal_icon), persone stilizzate, assegno (paycheck), anelli percentuale (ring), barre, frecce, check/croci, chip arrotondati.
- Video 5 (pubblico anziano): MENO movimento, scene un po' più lente, testi grandi ≥44 px, ma KEEP gli oggetti; ogni blocco un po' migliore del precedente; tutto compare entro la fine della slide; qualcosa visibile entro 1-1,5 s; niente glifo "½" nei font (usare "0,5%" o scrivere a mano la frazione).
- Funzioni chiave in v5lib/v5b11_20: Blk(n,S,groups) (.FS frame per slide, .tt(g,marker) secondi di un marker), appear, label, title, person, tile, paycheck, chip, strike, arrow_r/arrow_d, magnifier, money, ring, mcard, bar, lay, cal_icon, capitol, shield, thumb, dashed, pc (in v5b21_31.py).
- Ultima slide di ogni video: riquadro tratteggiato "WATCH NEXT" per l'elemento video della schermata finale.

## 5. MINIATURE (formula)
Si capisce l'argomento al volo (parola chiave in banner bianco in alto), numeri enormi con bordo nero, contrasto rosso/verde o rosso/giallo, banner giallo in basso con frase che crea curiosità, 1280×720. Aggressiva da clic (la prima con 37 impressioni non ha avuto clic). Fatte: video 1 (62 vs 70, rosso/verde, "$124,800 MISTAKE?"), video 2 (stile USA chiaro: "5 RETIREMENT MISTAKES… BROKE AT 85", "#3 SHOCKS EVERYONE"), video 3 (rosso scuro: "5 THINGS CHANGE AT 59½", lucchetto, "#4 TRAPS THOUSANDS"). Video 5: da fare. File in 06-immagini; script in 04-codice/miniature.

## 6. RICERCHE vidIQ / MERCATO
credit/debiti scartati (credit repair 108K, get out of debt 67K); pensione: retirement 544K/mese, retirement planning 396K, social security 317K; domande 8-21K concorrenza 7-15; canali minuscoli esplodono (1.590 iscritti → 203K view). 26/09: "social security 62 vs 70" 4,4K conc. 23; "when to claim social security" 47,6K; "social security at 62" 40K; "social security benefits explained" 17K (+240%); "retirement planning at 62" 8,7K. 27/09: "59 1/2 rule retirement" 4.602/mese conc. 12; "401k withdrawal rules" 4.683 conc. 13. Concorrenti faceless: John's Money (lavagna animata, immagine ogni 2-4 s, 140-150 parole/min), Harry/Mark/Anderson/James/Josh "X Invests", Primate Economics, EverythingProfessor, MoneyCoach; Trevor Phibbs (11K iscritti → 1,95M view "Social Security at 62 vs 70. The Math Will Surprise You."). Su 10 concorrenti solo 1 usa musica.

## 7. PIANO 20 VIDEO
1 When to Claim Social Security; 2 How Most Americans Ruin Retirement; 3 What Changes at Age 59½; 4 Why 61 Is the Most Important Age; 5 Social Security Benefits Explained; 6 No Retirement Savings in Your 60s; 7 What Medicare Doesn't Tell Seniors; 8 401(k) Fees; 9 Retire at 55 and Social Security; 10 Taxes on Social Security; 11 What $1M/$2M/$3M Gets You; 12 Health Insurance Before Medicare; 13 Why People Get Richer After Retirement; 14 IRMAA; 15 Medicare and Long-Term Care; 16 What You Keep Paying For; 17 Medicare Cost; 18 Social Security When You Die; 19 2 Bucket Strategy; 20 How to Plan for Retirement.

## 8. STATO DEI VIDEO (02/10/2026)
- VIDEO 1 pubblicato 26/09: "Social Security at 62 vs 70: The $124,800 Mistake (Exact Math)", 7:41, youtu.be/rPaLdR1E31s; Frank (62) e Mary (70); capitoli 0:00, 0:49, 1:41, 2:12, 3:04, 3:34, 3:50, 4:24, 4:51, 5:12, 5:48, 6:22, 6:40, 7:05; schermata finale 7:29:29-7:40:11 (da sostituire con video 2 quando esce).
- VIDEO 2 "5 mistakes that quietly ruin retirement" (25 blocchi, 11:09), programmato 28/09 16:00 ora italiana. Dati: Fidelity 2026 $185.500, $75.000 attesi, ~70% assistenza, Part B $202,90, HSA $4.400/$8.750, casa di cura ~$115.000/anno, RMD 73/75, "1 su 4 supera i 90".
- VIDEO 3 "The 59½ Rule: 5 Things That Change (Number 4 Traps Thousands)", 21 blocchi, 7:33 (13.600 frame). Slide consegnate. Testi pronti in 07. Capitoli: 0:00, 0:23, 0:51, 1:11, 2:10, 3:06, 3:59, 5:09, 6:03, 6:33, 7:16. DA DECIDERE da lui: nel blocco 14 la voce dice "three years past this milestone" ma da 59½ a 61 è 1,5 anni (se rigenera la frase, rifare solo le slide del blocco 14). Copione NON si tocca (registrato, accettato).
- VIDEO 4 "Why 61 Is the Most Important Age for Retirement (The $974 Medicare Trap)", 31 blocchi, 11:22, slide consegnate; schermata finale → video 3. DA FARE: titolo, descrizione con capitoli (servono gli orari della timeline), tag, miniatura, commento.
- VIDEO 5 "Social Security Benefits Explained", 31 blocchi, 22.336 frame = 12:24,5; slide TUTTE consegnate (blocchi 1-31). Testi in 07 (capitoli già calcolati). DA FARE: miniatura. Fine voce assoluta (frame 30 fps): 1:810, 2:1538, 3:2410, 4:3270, 5:4013, 6:4659, 7:5515, 8:6207, 9:6893, 10:7513, 11:8367, 12:9117, 13:9837, 14:10512, 15:11235, 16:11989, 17:12668, 18:13469, 19:14151, 20:14846, 21:15494, 22:16366, 23:17100, 24:17633, 25:18442, 26:19018, 27:19757, 28:20485, 29:21113, 30:21955, 31:22336. Blocchi 2-10 consegnati un po' spogli ma "restano come sono". Ultimo MP4 (blocco 31, slide 2) ha il riquadro tratteggiato.
- Dati 2026 verificati ssa.gov: COLA 2,8%, assegno medio $2.071, tetto contributivo $184.500, massimo a FRA $4.152, bend point $1.286/$7.749 (90/32/15), limite guadagni $24.480 (1 ogni 2) e $65.160 anno FRA (1 ogni 3), coniuge fino 50% (37,5% se 36 mesi prima), superstite 71,5% a 60 → 100% a FRA, Trustees giugno 2026: fondo pensioni 4° trimestre 2032 (78%), combinato 2034 (83%).

## 9. ERRORI GIÀ FATTI (non ripetere)
- Altra chat senza il codice → stile diverso, slide ferme 20-30 s → tutto rifatto: usare SEMPRE il codice in 04.
- Fine voce letta solo in secondi (mancavano i fotogrammi) → sempre secondi + fotogrammi.
- "Meno movimento" capito come "togli gli oggetti" → slide spoglie: tenere gli oggetti.
- Slide inviate senza guardare gli MP4 finiti → testo tagliato: controllare sempre i frame estratti.
- Creduto "titolo/descrizione" fosse per il video 5 mentre era per il video 3: confermare il video.
- Spesi crediti vidIQ senza chiedere (miniatura da 5 crediti rifiutata).
- Messaggi lunghi, elenchi, scuse: l'utente vuole risposte corte, una cosa alla volta, esegui solo gli ordini.
- Quando chiede UN file, consegnare UN file (questo zip).

## 10. COSE CHE POTREBBE AVER DIMENTICATO (da Claude)
- Per monetizzare servono i requisiti del Programma Partner YouTube (di norma 1.000 iscritti + 4.000 ore di visualizzazione pubbliche in 12 mesi; verificare la pagina ufficiale): il canale è nuovo, quindi pubblicare con costanza e controllare la pagina.
- Prima del caricamento: togliere i sottotitoli CapCut, impostare "contenuto sintetico: No" come da regola, aggiungere fonti e disclaimer, inserire schermata finale e playlist.
- Il video 3 va nella playlist "Retirement After 50" (crearla); schermata finale → video 1. Il video 4 → video 3. Il video 5 → video 1.
- Aggiornare la schermata finale del video 1 dopo l'uscita del video 2.
- Nei video non dare consigli personali (regola monetizzazione, sezione 2.9).


NOTA: la cartella 10 (93 MP4 del video 5) non è in questo zip per il limite di peso: gli MP4 sono già stati inviati uno per uno in chat.

NOTA 02/10 (riordino): la cartella 10 contiene 97 MP4 (blocchi 1-31). Quelli del blocco 3 (v5-b3-01..04, 188+199+236+249 = 872 frame) mancavano nei file ricevuti e sono stati rigenerati dal codice in 04-codice/v5b2_5.py. Le versioni vecchie del kit (28/09) sono in 01-documenti-precedenti/versioni-28-09 e 11-archivio-zip-kit-vecchi. La cartella 09 contiene solo gli screenshot della timeline.
