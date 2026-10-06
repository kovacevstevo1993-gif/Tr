# RICERCHE vidIQ E DATI ANALYTICS GIA FATTI (The Senior Advantage)

REGOLA: prima di spendere crediti vidIQ leggere questo file. Se la ricerca e gia qui, NON rifarla. Ogni nuova ricerca va aggiunta qui subito (commit + push). Costi: ogni chiamata a keyword_research, outliers, score_thumbnail, channel_analytics, video_stats, user_videos costa 5 crediti. balance e user_channels costano 0.
Saldo al 06/10/2026 dopo queste ricerche: 30 crediti (renewable 10 + add-on 20; rinnovo renewable il 25/10/2026, max 150).
Canale connesso a vidIQ: UC3mqeyFLRtxoHy5unytlNwQ (account s_s_corporation@hotmail.com).

Dati pubblici gratuiti (senza crediti) si leggono da YouTube con curl su youtubei/v1/next, /browse, /search e oembed (vedi script in sessione 06/10/2026: POST https://www.youtube.com/youtubei/v1/next con clientName WEB). Si puo vedere: titolo, descrizione, capitoli (chapterRenderer), view, iscritti, tab del canale, ricerche concorrenti. Non si vedono: impressioni, CTR, schermata finale, commento fissato, Video correlato.

---------------------------------------------------------------------
## 1. ANALYTICS DEL CANALE (vidiq_channel_analytics, 06/10/2026, periodo 2026-09-06 / 2026-10-06) - 10 crediti

### Fonti di traffico (report traffic_sources)
Colonne: fonte, view, view coinvolte, minuti guardati, durata media (s), percentuale media guardata
- YT_CHANNEL: 2, 1, 0, 44, 113,85
- PLAYLIST: 1, 1, 0, 8, 22,86
- SUBSCRIBER: 2, 0, 0, 0, 0
- EXT_URL: 2, 1, 0, 32, 115,36
- SHORTS (feed Shorts): 62, 8, 4, 26, 73,15
- NO_LINK_OTHER: 0
- YT_SEARCH (ricerca): 156, 62, 38, 35, 109,0
Totale circa 225 view in 30 giorni. Nessuna view da browse (home) ne da video suggeriti.

### Video principali (report top_videos)
Colonne: video, view, view coinvolte, minuti, durata media (s), percentuale media guardata, iscritti guadagnati
- XCRw0E4eTaE (short "Senior Discounts Start at 55 - Not 65"): 76, 29, 17, 34, 97,51, 0
- sj4vzbjii_k (short "Senior Discounts Nobody Tells You About"): 62, 22, 13, 33, 120,72, 1
- bkZ8pOaoX3g (short Meals on Wheels): 30, 10, 7, 40, 118,19, 0
- 96JkWmUbRF4 (short SNAP): 30, 7, 4, 37, 103,85, 0
- EGDTj4NTlQw (short LIHEAP): 26, 5, 2, 21, 55,31, 0
- Tqw_9LMUJYE (lungo 1): 1, 0, 0, 0, 0, 0
(Il lungo SNAP KDYxb4tKm1Q e lo short CSFP Mk6ZIS9JMBQ non erano ancora nel report.)
Conclusione: gli short tengono bene (si guarda quasi tutto), il problema e la distribuzione.

---------------------------------------------------------------------
## 2. PUNTEGGIO MINIATURE (vidiq_score_thumbnail, 06/10/2026) - 10 crediti

### Lungo 1 (Tqw_9LMUJYE), miniatura nonno "STOP PAYING FULL PRICE" (poi sostituita con "55 NOT 65"): 60/100
Punti forti: luminosita buona (+12), intensita sensoriale bilanciata (+7).
Da migliorare: immagine poco energica (-13, "aumenta saturazione, effetti di movimento"); layout sbilanciato (-11, "regola dei terzi"); promessa che sembra esagerata (-8); il volto domina il frame (-7).

### Lungo SNAP (KDYxb4tKm1Q), miniatura nonno "THE $35 RULE": 77/100
Punti forti: luminosita buona (+38), immagine nitida (+26), intensita bilanciata (+18).
Da migliorare: composizione troppo piena o troppo vuota (-8, spazio negativo); confronto non chiaro (-7); poca energia (-7).
NON ancora valutata la nuova miniatura "55 NOT 65" del lungo 1 (se serve, 5 crediti).

---------------------------------------------------------------------
## 3. OUTLIER: VIDEO LUNGHI CHE ESPLODONO (vidiq_outliers) - 10 crediti

### 3a. keyword "senior discounts", lunghi, canali fino a 20.000 iscritti, ultimi 3 mesi, ordinati per view
Colonne: titolo | canale (iscritti) | view | durata | punteggio breakout
1. Senior Citizen Card 2026 (Tamil, 15 benefici) | Money Coach Tamil (8.300) | 233.816 | 27:30 | 474,5 (India, non pertinente)
2. Every Senior Must Do This Before September 30: Miss It and You Pay All Year | Franklin Law (7.620) | 103.652 | 21:07 | 33,6 (Medicare, altro canale)
3. Sarees (India, fuori tema) | MegaFactory (6.380) | 47.144 | 2:13
4. The Senior Driver Setup That Will Add 30+ Yards (golf, fuori tema) | Michael Kanev Golf (1.650) | 31.637 | 5:35
5. Amazon Prime Day Sales & Discounts Explained | Brick Bandit (4.220) | 22.056 | 15:17
6. **Aldi Is Hiding 15 Discounts From Seniors Over 60 (Here's Every One)** | The Smart Steward (8.440) | 21.451 | 9:46 | 134,0 | engagement 4,6%
7. Nifty Down 11% (India) | GetMoneyRich (4.830) | 17.844
8. Helium 10 Coupon Code | Tutorial Stack (17.900) | 11.987
9. Come thrift with me at the Goodwill Bins | Aela sentner (2.580) | 11.593
10. **Costco Is Hiding 17 Discounts From Seniors Over 60 (Here's Every One)** | The Smart Steward (8.440) | 11.258 | 10:19 | 27,0 | engagement 2,5%
11. Senior box for September 2026 #SeniorFoodBank | CrazyForJesus (3.610) | 7.621 | 7:55 | 10,9 (scatola senior mostrata)
12. The Pricing Trick Behind Fake Discounts | The Real Facts Insight (1.230) | 1.618 | 1:42 | 169,9
Utili per noi: i due video The Smart Steward (formato "[Marchio] Is Hiding N Discounts From Seniors Over 60 (Here's Every One)", circa 10 minuti, canale piccolo) e la scatola senior mensile.

### 3b. keyword "seniors food help benefits", lunghi, canali fino a 20.000 iscritti, ultimi 3 mesi, ordinati per view
1. Senior Citizen Card 2026 (Tamil) | Money Coach Tamil (8.300) | 233.816
2. **New Food Assistance Rules for Seniors Starting This October 1 (One Erases Your Old Denial)** | Robin MBA (6.290) | 231.229 | 10:21 | breakout 252,5 | engagement 1,3%
3. Japanese 29 Clever Cooking Tricks For Seniors Living Alone | Granny Yuki (4.840) | 209.682 | 19:36
4. 92 year Old Okinawan Reveals 15 Clever Cooking Tricks For Seniors Living Alone | Michiko Tanaka (4.350) | 108.662 | 15:27
5. 15 Slow Cooker Dinners Nobody Told Seniors About Until Now (Dump It In, Walk Away) | Grandma Edith Cooks (2.680) | 56.369 | 23:09
6. Japanese 10-minute Meals For Seniors | Granny Yuki (4.840) | 39.743
7. **New Food Stamp Rules for Seniors - Do This Before They Hit** | Robin MBA (6.290) | 20.248 | 15:03
8. FIGHTING FOR FOOD AT THE FOOD PANTRY! | MamaKitaLIVE (12.600) | 17.580 | 31:51
9. Food pantry haul (free food) September 2026 | Life with Misty (3.550) | 15.176 | 14:55
10. Simple Sitting Exercises for Seniors | Yoga with Subramanian (5.700) | 14.061
11. 25 Japanese Soups Strong Seniors Eat | Granny Yuki (4.840) | 12.816
12. Monthly Food Pantry Haul for Seniors | Come See What We Got! | Belinda's Country Living (9.970) | 9.050 | 13:24
Utili per noi: Robin MBA (SNAP con data 1 ottobre), e i video "haul" mensili (scatola/dispensa vera mostrata).

---------------------------------------------------------------------
## 4. PAROLE CHIAVE: "costco senior discount" (vidiq_keyword_research, paese US, modalita research) - 5 crediti
Colonne: parola | ricerche/mese | concorrenza (0-100) | punteggio generale
- costco senior discount (seme) | 3.269 | 19,1 | 63,8
- costco for seniors | 5.235 | 12,3 | 68,4 (migliore opportunita)
- costco senior discounts | <750 | 11,3 | 35,5
- senior discounts | 8.964 ora (base 30 giorni 20.150, quindi -55,5%) | 28,5 | 64,0
- costco senior savings | <750 | 15,3 | 33,9
- costco benefits for seniors | <750 | 14,6 | 34,2
- costco no senior discount | <750 | 21,5 | 31,4
- costco return policy | 3.889 | 36,3 | 57,6
- costco hacks | 5.292 | 41,9 | 56,6
- costco | 338.300 (base 318.720, +6,1%) | 62,2 | 64,6 (US in-country 61.286; paesi principali US 18%, VN 11%, PK 10%, MA 9%, IN 7%)
- costco shopping tips | 4.339 | 47,5 | 53,6
- costco tips | 4.234 | 52,0 | 51,7
- costco membership | 18.372 (base 9.955, +84,6%) | 36,6 | 63,6
- costco price adjustment | <750 | 19,6 | 32,2
- costco secrets | 4.301 | 50,5 | 52,3
- costco executive membership | <750 | 22,3 | 31,1
- costco gas savings | <750 | 25,8 | 29,7
- senior savings | 3.786 | 25,2 | 62,0
- costco deals | 40.773 (base 14.383, +183,5%) | 40,8 | 65,0 (US in-country 6.273; Pakistan 38%)
- costco pharmacy no membership | <750 | 23,5 | 30,6
- costco membership worth it | 4.109 | 35,7 | 58,1
Conclusione: "costco for seniors" (5.235, concorrenza 12) e "costco senior discount" (3.269, concorrenza 19) sono le migliori per un video Costco.

---------------------------------------------------------------------
## 5. RICERCHE PUBBLICHE GRATUITE SU YOUTUBE (06/10/2026, 0 crediti)
Stato del canale: 1,71K iscritti, 8 video (2 lunghi, 6 short). Lungo 1: 1 view dopo 4 giorni. Lungo SNAP: 5 view dopo 1 giorno. Short: CSFP 15, SNAP 58, LIHEAP 35, Meals on Wheels 30, sconti 77 e 84.
Playlist: "Help Programs for Seniors: Meals, Bills & More" (PLHKlqg-5s6k4) e "Senior Discounts & Savings for Ages 55+" (PLe_g_w48cB3c).
Descrizione canale prima: "over 50", keyword con Social Security, Medicare, Medicaid, VA, scams (messe dalla chat del 27-29/09). Sistemata il 06/10.

Risultati di ricerca YouTube (titolo | canale | view | eta | durata):
- "SNAP benefits for seniors over 60": 7 SNAP Rules for Seniors 60+ That Change October 1, 2026 | Sam USA | 84 | 2 giorni | 11:04. SNAP Benefits for Seniors - Everything You Need to Know! | DailyCaring.com | 16.452 | 1 anno | 5:00. SNAP Rules Just Changed for Seniors | Smart Retirement | 504 | 4 sett. | 9:16. SNAP Changes October 1st: Three Rules That Help Seniors Over 60 | SeniorBenefitsHub | 42 | 10 giorni | 8:13. Free Food Benefits Start at Age 60 (Not 65) | Robin MBA and 4 more | 838 | 21 ore | 14:30. Over 60? SNAP Changed October 1 - Check Your Medical Bills | Money Instructor | 3.435 | 4 giorni | 10:55. New Food Assistance Rules for Seniors Start October 1 | The Retirement Wire | 16.111 | 11 giorni | 13:26. SNAP Over 60? Your Medical Receipts May Change the Math | Retirement Desk | 134 | 4 giorni | 3:57.
- "food stamps for seniors": Every Senior Getting $25 in Food Stamps Must Do This to Get Up to $306 Before January | Robin MBA | 21.783 | 2 giorni | 15:45. **New Food Assistance Rules for Seniors Start October 1 (One Erases Your Old Denial)** | Vision Tribe Money | 530.908 | 2 sett. | 11:00. Stesso titolo | Robin MBA | 231.229 | 10 giorni | 10:21. New Food Stamp Rules for Seniors - Do This Before They Hit | Robin MBA | 20.251 | 5 giorni | 15:03. SNAP & EBT Changes 2026 | Seniors Post | 2.132 | 9 mesi | 15:13. Why Seniors Get The Least In SNAP Benefits | Crystal the Social Worker | 26.551 | 1 anno | 8:02. SNAP Food Stamps 2026: New Work Rules + How Seniors Get MORE Benefits | Benefits Insider | 9.873 | 7 mesi | 22:53.
- "senior discounts": 25 Hidden Senior Discounts You Probably Don't Know About | Help For Seniors | 8.174 | 10 mesi | 7:23. Seniors! Did you know that these places offer you discounts? | How To Pay Less For Everything | 7.901 | 1 anno | 13:07. The Best Senior Discounts | SeniorLiving.Org | 12.060 | 1 anno | 7:19. **15 Places Seniors DON'T know give BIG Discounts** | The Good Steward | 462.602 | 7 mesi | 10:00. 15 "Hidden" Senior Discounts Aldi Never Advertises | FastSave | 66.333 | 3 mesi | 25:20. **15 HIDDEN Costco Senior Discounts They Never Advertise in 2026** | Walt - Senior Money Watch | 335.591 | 3 mesi | 21:52. 50 Senior Discounts Every American Over 60 Should Know | Retire Better | 185 | 3 mesi | 8:59. Senior Discounts You May Be Missing After 50 | ReInspired | 43.916 | 2 sett. | 8:14.
- "senior discounts you are missing": 10 Discounts You Unlock at 62+ | Golden Years Finance | 2 | 12 ore | 6:53. 11 Senior Discounts You May Be Missing in 2026 | Julie Money Matters | 33 | 3 giorni | 17:26. 5 Senior Discounts & Benefits You May Be Missing | Kevin's Retirement Guide | 1.355 | 1 mese | 27:24. Are you missing out on one HUGE SENIOR DISCOUNT? | Vicki Retired | 1.472 | 7 mesi | 8:40. 12 Hidden Senior Discounts You've Never Heard Of | Senior Life Friends | 30 | 1 mese | 9:16. (altri sotto le 50 view)
- "benefits seniors never claim": tutti sotto le 320 view (Money Clarity 314, Digital Silver John 66, Medicare Made Simple 76, ecc.): tema inflazionato, nessuno decolla.
- "CSFP senior food box": What's Inside A Senior Food Commodity Box? May 2026 | Melonie Tries Recipes | 45.377 | 4 mesi | 9:46; April 2026 | 11.265; **September 2026 | 57.860 | 1 mese | 7:20**; August 2026 | 21.676. USDA Monthly Senior Food Box also known as: CSFP | My Mountain Home and Kitchen | 15.263 | 1 anno | 6:43. Formato che vince: serie mensile, scatola vera mostrata.
- "LIHEAP seniors help paying bills": tutti sotto le 1.200 view (The Senior Plug 928, Grants Buddy 1.138): tema debole.
- "government benefits for seniors 2026": Low Income Relief | 10 FREE Benefits Most Seniors MISS | 10.851 | 10 mesi | 7:21 (altri risultati fuori tema: India, tasse).

---------------------------------------------------------------------
## 6. DATI vidIQ PIU VECCHI (dalle chat precedenti, vedi anche PASSAGGIO-CHAT.md sezione DATI vidIQ)
"senior discounts" 12.828/mese (concorrenza 26,3). "senior discount" 9.826 (20,7). "senior citizen discounts" 4.821 (30,8). "hidden senior discounts" 4.045 (23,6). "senior savings" 3.786 (26,2). "senior assistance programs" 4.229 (21). "low income relief" 24.886. "senior meals" 7.069. "snap benefits" 11.295 (+164%). "snap for seniors" 5.338 (28). "food stamps" 6.331 (+84%). "government benefits for seniors" 4.323 (19,6). Titolo lungo 1 punteggio vidIQ 94/100 ("Senior Discounts Start at 55, Not 65: 12 Hidden Places (Most Never Ask)"), alternativa 90/100. Le chat 01LADT (short 5) hanno speso 15 crediti (ricerca keyword, video virali, video concorrenti SNAP): risultati nel file chat/2026-10-03_sessione-01LADT-short5.md.

---------------------------------------------------------------------
## 7. FATTI UFFICIALI COSTCO (06/10/2026, ricerca web gratuita su siti Costco) - per il video lungo Costco
- Costco NON offre sconti ne iscrizioni scontate per gli over 60 (pagina ufficiale: customerservice.costco.com, "Does Costco offer free or discounted memberships?"). Iscrizione Gold Star 65 dollari l'anno, Executive 65 dollari in piu, uguale per tutte le eta.
- Farmacia: non serve essere iscritti per comprare farmaci con ricetta, online o in magazzino (customerservice.costco.com, "Do I need a membership to purchase prescription drugs?").
- Centro apparecchi acustici: test dell'udito gratuito per iscritti dai 18 anni, assistenza gratuita inclusa con l'acquisto; prezzi da 1.599,99 dollari (Philips HearLink 9050, ricaricabile con caricatore) e 1.699,99 (Jabra Enhance Pro 30). Serve la tessera.
- Ottica: lenti a contatto online solo per iscritti.
- Conseguenza: un titolo "Costco Is Hiding N Discounts From Seniors" sarebbe falso. Angolo onesto: "Costco has no senior discount, but these N things save seniors money" (parole chiave: "costco for seniors" 5.235/mese conc. 12; "costco senior discount" 3.269 conc. 19).

---------------------------------------------------------------------
## 8. RICERCA VIDEO COSTCO (06/10/2026) - 5 crediti vidIQ (saldo 25) + ricerche pubbliche gratuite
Autorizzata dall'utente ("fai tutte le ricerche, parole chiave SEO").

### 8a. Video Costco per over 60 che vanno (YouTube, ricerca "costco senior discount" e "costco for seniors"; titolo | canale | view | eta | durata)
- **If You're Over 60, Costco Owes You These 15 Free Things** | Robin MBA | 457.040 | 3 sett. | 15:42 (15 servizi inclusi nella tessera; alla fine 2 a pagamento con costi dichiarati: vaccini e upgrade Executive)
- **15 HIDDEN Costco Senior Discounts They Never Advertise in 2026** | Walt - Senior Money Watch | 335.640 | 3 mesi | 21:52 (apre con: apparecchi acustici 1.500 contro 3.500-7.000, "usati una volta pagano 20 anni di tessera"; rivolto a coppie di over 60 in due)
- 15 "Hidden" Senior Discounts Costco Never Advertises | The Retiree Wallet | 177.195 | 4 mesi | 25:06 (apre con storia di una donna di 60 anni, apparecchi acustici, 3.000 dollari risparmiati; ammette "Costco non ha un vero sconto senior")
- **13 Ways Seniors Can Shop Costco Without Ever Paying for a Membership** | The Retiree Wallet | 101.960 | 3 mesi | 21:59
- Costco Senior Deals Most Members Never Find | FrugalFinds4U | 95.738 | 4 mesi | 22:31
- 15 "Hidden" Senior Discounts Costco Canada Never Advertises | The Canadian Senior Wallet | 44.057 | 3 mesi
- 13 Senior Secrets Only Costco Employees Know | The Smart Steward | 20.418 | 1 mese | 13:53
- 18 Costco Senior Deals You'll Regret Missing This Month | John Prepares | 15.616 | 4 mesi | 38:03
- Costco Is Hiding 17 Discounts From Seniors Over 60 | The Smart Steward | 11.258 | 1 mese | 10:19
- Over 55? Then You Can Use These Costco HIDDEN Senior Discounts | Tragic Faith | 6.972 | 12:36
- Decine di copie dello stesso titolo ("15 Hidden Senior Discounts Costco Never Advertises") fanno 100-700 view: il formato inflazionato non basta, vince chi e primo/ha canale forte o titolo diverso.
Durata dei video che vincono: 15-25 minuti (i vincitori Robin MBA 15:42, Walt 21:52, Retiree Wallet 22-25). Il canale piccolo Smart Steward fa solo 10-14 min e 11-20K.

### 8b. Cosa contengono (trascrizioni dei 4 migliori)
- Robin MBA (15 cose incluse nella tessera): assistenza tecnica telefonica gratis (Concierge) per elettronica; seconda garanzia di 2 anni su articoli selezionati; manutenzione gomme gratis se comprate li; test dell'udito gratis (dai 18 anni); controllo 30 giorni sul prezzo (rimborso differenza); reso 100% soddisfatti senza limite di tempo sulla maggior parte; programma farmaci per iscritti gratis; farmacia senza tessera; ecc.
- Walt (15): farmacia senza tessera; apparecchi acustici (Kirkland non esiste piu); esame vista senza tessera; Member Prescription Program; 4,9 dollari pollo arrosto; Kirkland Signature; benzina; carta Costco Anywhere Visa (cashback); libretto coupon mensile; adeguamento prezzo 30 giorni; garanzia al posto della garanzia estesa; la tessera piu famosa (pranzo/food court); seconda porta senza tessera propria (tessera familiare).
- Retiree Wallet "senza tessera" (13): accompagnare un socio; tessera familiare gratuita; shop card; farmacia; vaccini; alcol in certi Stati; esame vista; test udito; Costco.com da non socio; Instacart; Uber Eats; garanzia 100% come prova gratuita; bonus carta regalo all'iscrizione.
- Retiree Wallet "15 hidden": programma farmaci fino a 80%; apparecchi acustici; occhiali; Executive 2% cashback; orari mattina per Executive; viaggi; assicurazioni; Kirkland; vitamine; assaggi; benzina; consegna farmaci; Costco Auto; resi; carta Visa.
- Parola chiave usata da Walt (tag): costco senior discounts, costco for seniors, costco discounts 2026, senior savings, costco membership worth it, costco pharmacy no membership, costco hearing aids, costco executive membership, kirkland signature, costco price adjustment, costco return policy, costco gas savings, fixed income savings, retirement savings, discounts for seniors over 60, costco tips, senior money, warehouse club savings, costco coupon book, costco anywhere visa.
Descrizione di Robin MBA: gancio ("Bring a question, not a coupon"), disclaimer con "not affiliated with Costco Wholesale Corporation", fonti = nomi pagine costco.com.

### 8c. Autocompletamento YouTube (gratis)
"costco senior" -> costco seniors, costco special, costco services. "costco for seniors" -> costco food warning for seniors, costco for single person. "does costco have a senior discount" -> ... senior discount card, ... senior discount day. (le persone cercano anche "senior discount day" e "senior discount card": rispondere nel video che NON esistono).

### 8d. vidIQ matching_terms "costco seniors" (US, 5 crediti): parola | ricerche/mese | concorrenza | punteggio
- costco free seniors | 9.292 | 14,5 | 69,7 (MIGLIORE)
- costco for seniors | 5.235 | 12,3 | 68,4
- items seniors should never buy at costco | 4.632 | 19,1 | 65,2
- costco food warning seniors | 4.384 | 18,3 | 65,3
- something is changing at costco - what seniors need to know | 4.431 | 17,9 | 65,5
- 12 ways seniors can shop costco without ever paying for a membership | 4.340 | 19,1 | 64,9
- costco discounts for seniors | 4.449 | 38,7 | 57,2
- costco worth for seniors | 3.945 | 24,2 | 62,5
- seniors saving at costco | 3.602 | 21,5 | 63,3
- seniors costco | 3.594 | 20,9 | 63,5
- 13 ways seniors can shop costco without ever paying for a membership | 3.609 | 22,1 | 63,0
- 15 costco discounts seniors never use | 3.394 | 22,7 | 62,5
- 13 more things seniors don't know costco gives for free | 3.989 | 37 | 57,5
- (titoli di video usati come parole: "costco weird facts", "shopping mistakes", "never buy" = altri angoli ma allarmisti, non adatti: niente promesse false)

### 8e. Fatti ufficiali Costco verificati (ricerca web su costco.com e customerservice.costco.com, 06/10/2026)
- Member Prescription Program: NON e assicurazione, sconti sui farmaci fino a 80% o piu secondo il farmaco, nessuna iscrizione ne costo extra, si usa la tessera Costco gia in tasca, vale anche in farmacie partecipanti (Albertsons, Kroger, Safeway, Walgreens...) (costco.com/member-prescription-program.html).
- Centro apparecchi acustici: test udito gratis, prezzo esposto = prezzo pagato, garanzia gratis (varia per modello), perdita/danno senza franchigia, controlli e pulizie gratis (costco.com/hearing-aid-information.html). L'uso e un beneficio per i soci.
- Ottica: NON serve la tessera per fissare la visita dall'ottico indipendente in/vicino al magazzino; la tessera serve per comprare occhiali e lenti (customerservice.costco.com, "Do I need a membership to purchase glasses or contacts?").
- Adeguamento prezzo: acquisti scesi di prezzo entro 30 giorni danno diritto al rimborso della differenza (customerservice.costco.com a_id 628); credito di solito in 5-10 giorni lavorativi.
- Reso: "Risk-Free 100% Satisfaction Guarantee"; alcuni elettronici (TV, computer, tablet, telefoni, ecc.) entro 90 giorni (customerservice.costco.com a_id 1191).
- Ancora da verificare sul sito prima del copione: Concierge (assistenza tecnica, numero), garanzia 2 anni, manutenzione gomme, vaccini farmacia, tessera familiare gratuita, shop card, benzina, libretto coupon, carta Visa, prezzo pollo, regole alcol per Stato.

### 8f. Fatti ufficiali Costco verificati (seconda tornata, 06/10/2026, costco.com / customerservice.costco.com / citi.com)
- Concierge (assistenza tecnica gratis): 1-866-861-0450, tutti i giorni 5-20 Pacific time (le trascrizioni dei concorrenti dicono 22: vale il sito Costco). Prodotti: TV, proiettori, desktop, laptop, all-in-one, grandi elettrodomestici, tablet touch, fotocamere, videocamere, home theater, lettori DVD, stampanti. Servono: nome, numero tessera, numero articolo dallo scontrino, modello, seriale, data acquisto (customerservice.costco.com a_id 9004).
- Seconda garanzia: TV, schermi, proiettori, computer e grandi elettrodomestici fino a 2 anni dalla data di acquisto; replica la garanzia del produttore; tablet touch ESCLUSI (customerservice.costco.com a_id 9005).
- Gomme: installazione inclusa + manutenzione per la vita delle gomme (rotazione, equilibratura, controllo pressione, riparazione forature) + garanzia road hazard 5 anni; solo gomme comprate da Costco (tires.costco.com/CostcoAdvantage).
- Tessera Household gratis: una per persona sopra i 16 anni che vive allo stesso indirizzo (Gold Star 65 dollari, Executive 130; customerservice.costco.com a_id 855/857).
- Vaccini in farmacia (influenza, covid, fuoco di Sant'Antonio/Shingrix, polmonite): i non soci possono usare la farmacia e le vaccinazioni; walk-in o app; i soci hanno prezzo scontato, i non soci prezzo cash (costco.com/pharmacy/adult-immunization-program.html, customerservice.costco.com a_id 796).
- Executive: 130 dollari l'anno (65 in piu della base). Premio 2% fino a 1.250 dollari ogni 12 mesi (dal 1/9/2024). "Il premio non e garantito pari o superiore alla quota dell'upgrade." Pareggio dell'upgrade (65 dollari): 3.250 dollari di acquisti l'anno (65 / 0,02).
- Carta Costco Anywhere Visa Citi: 5% benzina Costco, 4% altra benzina/EV fino a 7.000 dollari l'anno, 3% ristoranti e viaggi, 2% Costco, 1% resto. (Prodotto finanziario: NON inserita nel video.)
- Non verificati, quindi NON nel video: benzina prezzo, libretto coupon, alcol per Stato, shop card come "senza tessera", viaggi, assicurazioni.
