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

### 8g. Terza tornata di verifica (06/10/2026, costco.com e customerservice.costco.com)
- Adeguamento prezzo in magazzino: entro 30 giorni dall'acquisto; si chiede al banco RESI (Returns counter) del magazzino dove si e comprato, con lo scontrino (NON al banco iscrizioni). Scontrini degli acquisti in magazzino degli ultimi 2 anni visibili su Costco.com > Orders & Purchases > scheda In-Warehouse (customerservice.costco.com a_id 628, 10306, 696).
- Libretto sconti (Savings Booklet): inviato al titolare principale (Gold Star, Executive, Business) dei soci attivi; nessun coupon da ritagliare, lo sconto si applica alla cassa; si trovano anche su Costco.com (View Warehouse Savings) e nell'app. Se non arriva: puo essere stato disattivato, indirizzo sbagliato o cambiato da meno di 3 mesi, iscritto da meno di 2 mesi, tessera scaduta: si chiede al banco iscrizioni (customerservice.costco.com a_id 623).
- Benzina: solo per soci (eccezione: chi paga con Costco Shop Card prepagata); benzina Kirkland Signature certificata TOP TIER, 5 volte il detergente richiesto dall'EPA. Il sito NON dice che costa meno: NON promettere risparmio (costco.com/f/-/gasoline-qanda).
- Food court: serve la tessera; hot dog con bibita 1,50 dollari e pollo arrosto 4,99 compaiono nei risultati ma NON confermati da una pagina ufficiale letta: NON inserire finche non confermati.
- Punti verificati per il video: 14 (farmacia senza tessera; programma farmaci; apparecchi acustici; esame vista; Concierge; 2o anno garanzia; gomme; adeguamento prezzo; resi; tessera Household; vaccini; libretto sconti; scontrini online; Executive con conto onesto). Decisione: 14 punti (i video virali ne hanno 13-15).

---------------------------------------------------------------------
## 9. RICERCA PROSSIMO VIDEO LUNGO + DIAGNOSI CANALE (08/10/2026, 0 crediti, ricerca YouTube "questo mese" ordinata per view)
### 9a. Stato canale (letto da YouTube)
Lungo 1 (Tqw_9LMUJYE, 1/10) 2 view; lungo SNAP (KDYxb4tKm1Q, 4/10) 7 view; lungo Costco (w-GQwECwTXA, 7/10) 6 view in 1 giorno. Short: 87, 78, 72, 41, 37, 28, short 7 Costco (gxin3OHc7aQ) 16.
Cause probabili: iscritti vecchi inattivi (2 view dagli iscritti in 30 giorni: YouTube mostra il video prima a loro, nessuno clicca, segnale negativo); 0 view da home e suggeriti (69% solo ricerca); solo 3 lunghi; arriviamo sui formati gia saturi (Costco 4 settimane dopo); titoli in negativo/tecnici invece della promessa dei vincenti ("Costco Has No Senior Discount" contro "Costco Owes You These 15 Free Things"); durata 11-13 min contro 15-25; miniature 60-77/100. Mancano CTR, impressioni e durata media (Studio o vidIQ analytics 10 crediti).
### 9b. Video virali della nicchia (ultime 4 settimane; view | eta | durata | canale | titolo)
- 2.094.057 | 3 sett | 13:08 | Vision Tribe Money | 5 Bills You Don't Have To Pay After 65 (Most People Don't Know) (capitoli: gancio "born before 1961, legally exempt and still paying"; 5 bollette 1-2 min l'una; Bonus a 7:45; colpo finale "Being exempt and keeping the money are two different things"; "Send this to one person over 65". Contenuto: deduzione 6.000, tassa casa, Medicare Part B/MSP, telefono-internet-utenze Lifeline e LIHEAP, deduzione standard)
- 980.196 | 2 sett | 9:23 | Nia Prescott | Every Senior Must Do This Before October 1 - Most Never Do (capitoli misteriosi che non rivelano: "The paper already inside your house", "Thirty days that belong to the over-sixties alone"; dopo la lista "The one line that decides all five"; "What does NOT happen"; riepilogo con date)
- 543.422 e 232.000 | New Food Assistance Rules for Seniors Start October 1 (Vision Tribe Money, Robin MBA)
- 465.561 | 4 sett | 15:42 | Robin MBA | If You're Over 60, Costco Owes You These 15 Free Things
- 378.021 | 3 sett | 19:37 | Saving Savers | Grandma's 25 Winter Survival Tricks for Seniors Living Alone (That Cost Pennies!)
- 312.425 | 3 sett | 25:07 | Kevin Explains | 6 Places Seniors Should Never Keep Their Cash Before Nov 1
- 210.214 | 3 sett | 11:20 | Low Income Relief | These Senior Benefits Start at Age 50 (Not 65!)
- 128.833 | 2 giorni | 23:31 | The Smart Steward | If You're Over 65, Aldi Will Give You These 9 Things (If You Ask); 63.061 Aldi Owes You 13 Free Things
- 102.348 | 4 sett | 22:38 | The Airport Lounge Secret Most Seniors Never Use (And It's Free); 64.941 7 Things Travelers Over 60 Should ALWAYS Ask for at the Airport; Amtrak per senior 10-33K
- Walmart Owes You 11 Free Things (Frugal Frannie) 5.737 in 2 giorni; Sam's Club Owes You 15 Things (Robin MBA) 644; National Park Senior Pass: tutti sotto 1.000 (tema senza domanda)
### 9c. Struttura dei virali (dai capitoli)
Gancio identita + perdita + data nei primi 30 s; numero di punti annunciato; titoli dei punti misteriosi (non svelano la risposta); il punto piu forte NON per primo; "bonus" verso la fine; dopo la lista "la regola che decide tutti" (anello aperto chiuso solo alla fine); "cosa NON succede/errori"; riepilogo con date; "mandalo a una persona over 60/65". Durata 13-25 min.
### 9d. vidIQ 08/10/2026 (autorizzato dall'utente; 20 crediti spesi, saldo 15, rinnovo 29/10)
Outliers "seniors over 60 benefits bills discounts", lunghi, questo mese, canali <100K (view | iscritti canale | durata | titolo):
- 2.094.048 | 22.700 | 13:08 | 5 Bills You Don't Have To Pay After 65 (Most People Don't Know) (breakout 15.308)
- 1.103.083 | 6.570 | 17:13 | Flying Over 65? Why Airlines Quietly Treat You Different (Flight Attendants Wish Seniors Knew This!)
- 980.195 | 28.300 | 9:23 | Every Senior Must Do This Before October 1 - Most Never Do
- 546.051 | 7.690 | 14:22 | New Laws Start OCTOBER 1st - Is Your State on the List?
- 543.266 | Vision Tribe | New Food Assistance Rules for Seniors Start October 1
- 465.442 | 6.670 | 15:42 | If You're Over 60, Costco Owes You These 15 Free Things
- **401.168 | 1.770 iscritti! | 16:14 | 5 Bills You Can Legally Stop Paying the Day You Turn 65 (Joseph Retires)**: un canale piu piccolo del nostro ha copiato il formato e fatto 400K in 4 settimane.
- 326.056 | 17.700 | 17:22 | 7 Things They Can't Take From You After 65 - Not Even the IRS
- 247.236 | Kevin Explains | 9 Programs. One Call. Nobody Ever Tells You.
- 234.777 | UK | 5 Bills You Don't Have to Pay After 65 in the UK
- 230.271 | 10 Things I Avoid Now That I Live Alone at 69; 126.991 Aldi 9 Things (If You Ask); 108.051 Flight Attendants 12 Things
- 10.133 | 2.060 | Seniors STOP Paying Property Tax - You're Legally Exempt
Parole chiave (matching_terms "bills seniors", ricerche/mese | concorrenza): "5 bills seniors should be" 21.779 | 22; "seniors stop paying these 5 bills after 65 - you're legally exempt" 16.319 | 30; "the government quietly erases these 5 bills for seniors after 65" 14.839 | 24 (+240%); "5 bills seniors" 9.592 | 22 (+85%); "seniors over 65: check these 7 bills - you may be paying more than required" 7.417 | 13; "6 bills you can legally stop paying after 65" 7.113 | 19; "seniors never pay these 5 bills" 5.380 | 11. Seme "bills seniors don't have to pay" 4.951 | 22,7; "seniors in debt" 3.723 | 17,5.
Trascrizione "5 Bills You Don't Have To Pay After 65" (struttura): gancio "born before 1961... legally exempt... and you're paying every one right now; nobody whose paycheck depends on it will call you"; anticipa le obiezioni di 3 gruppi ("se hai la casa pagata... se vivi di Social Security... se sei in affitto non andare via: uno di questi decide quanto sale l'affitto"); "Stick around for the fifth one: it's the highest value item and the easiest to claim" (anello aperto); ogni voce = cos'e + errore comune ("people get wrong constantly") + chi aiuta di piu + azione in 1 frase; voce 4 piccola ammessa ("smaller in dollars but still real"); voce 5 = la promessa; bonus; frase finale "being exempt and keeping the money are two different things; the only bridge is a form"; "what to do this week, none of it costs a dollar"; disclaimer; "send it to one person over 65". Contenuto: deduzione 6.000 (tasse), tassa casa (3 moduli), Medicare Part B + Medicare Savings Program, Lifeline + LIHEAP, deduzione standard senior. CIOE quasi tutto tasse e Medicare.

---------------------------------------------------------------------
## 10. RICERCA PROSSIMO LUNGO (12/10/2026, autorizzata dall'utente "cerca anche su vidiq"; 20 crediti spesi: 2 outliers + 2 keyword matching_terms; saldo 55 = add-on; il saldo reale era 75, non 15) + ricerche YouTube gratuite
### 10a. Idea vidIQ (feed idee) "What Changes for Seniors 60+": claim a 62 anni taglia fino a 30% (Social Security), spese mediche sopra 35 dollari (SNAP, gia nel lungo 2), scadenza 60 giorni per contestare. Giudizio: punto 1 = Social Security, tema Money Backstory; punto 2 doppione lungo SNAP; punto 3 non verificato.
### 10b. Cosa va ora (view | eta | durata | canale (iscritti) | titolo)
- 1.118.352 | 3 sett | 17:13 | Sharon Dawson (6.940) | Flying Over 65? Why Airlines Quietly Treat You Different (Flight Attendants Wish Seniors Knew This!) (breakout 464)
- 562.635 | Vision Tribe Money (23.000) | New Food Assistance Rules for Seniors Start October 1 (One Erases Your Old Denial) (breakout 3.576)
- 465.792 | Joseph Retires (2.000) | 5 Bills You Can Legally Stop Paying the Day You Turn 65
- 217.140 | 6 giorni | 23:31 | The Smart Steward (11.600) | If You're Over 65, Aldi Will Give You These 9 Things (If You Ask) (breakout 273; vph 306)
- 202.256 | The Senior Traveler (24.400) | 15 Free Airline Perks Seniors Can Ask For Today (Almost Nobody Does)
- 66.149 | Smart Steward | If You're Over 60, Aldi Owes You These 13 Free Things; 64.990 The Senior Traveler | 7 Things Travelers Over 60 Should ALWAYS Ask for at the Airport
- 38.609 | Rooster Roadie (839 iscritti!) | 7 Best Cruise Lines for Seniors (breakout 207); 35.155 | Susan Parker | 9 Free Cabin Upgrades Stewards Will Quietly Give Seniors Over 60 (Just Ask)
- 12.395 Disney World Perks Seniors 60+ (23:54); 11.289 Walmart Owes You 11 Free Things; Amtrak (TheOriginPlate) 8-12K a video.
- Il nostro lungo 4 BOLLETTE (The Senior Advantage, 13:14): 25 view in circa 2 giorni. Concorrenti stesso tema bollette: Kevin Explains 54K (30:05), 4,9K; copie piccole 560-1.600.
- Tema "new rules October 1" (SNAP/pensione): gia pieno di copie (decine di canali, anche UK/DE/ES), la finestra (1 ottobre) e passata.
### 10c. Parole chiave vidIQ (US, matching_terms)
"seniors airport": "flying after 60 unlock 7 hidden airport perks seniors miss" 13.492/mese conc. 30 (+123%); "13 airport tips seniors should know before their next flight" 12.548 conc. 12; "6 new airport rules seniors are learning the hard way" 10.120 conc. 36; "what seniors should never wear through airport security" 9.082 conc. 9,8; "12 seniors secrets only airport employees know" 6.304 conc. 29; "airport hacks for seniors" 5.403 conc. 43; "flying over 60 seniors airport tips" 5.361 conc. 8,6.
"senior travel discounts": "senior discounts travel deals over 65" 4.894 conc. 10; "the truth about senior travel discounts flight" 4.782 conc. 6.
### 10d. Fatti da usare se si sceglie viaggio/aeroporto (DA VERIFICARE su tsa.gov, transportation.gov, amtrak.com PRIMA del copione): assistenza sedia a rotelle gratis per legge (ACAA), TSA Cares, regole speciali screening 75+, rimborso/compenso voli cancellati, sconto senior Amtrak 65+ (verificare %), Senior Pass parchi nazionali (gia visto: tema senza domanda, view <1.000).

### 10e. Spesi altri 5 crediti (trascrizione vidiq_video_transcript del virale PX24ZIMSst8, 1,12M view): struttura = gancio identita+perdita, 7 'differenze', ogni punto con frase da dire parola per parola, storia delle due donne al banco come filo, 'cosa e quando', riepilogo, 'tre cose', libro/link. Saldo 50 crediti. Fatti verificati su pagine ufficiali TSA/eCFR: in COPIONE-VIDEO-AEROPORTO.md.

## 11. SHORT 9 AEROPORTO (14/10/2026, autorizzata dall'utente "falla allora"; 10 crediti: score_title 5 + keyword research 5; saldo 40 -> 30, solo add-on, rinnovo 25/10)
- Titolo short "Flying Over 60? 8 Things You Can Ask for at the Airport (Almost Nobody Does) ✈️": punteggio vidIQ 96/100.
- keyword "seniors airport" (research, US): seme <750/mese. Correlate utili: senior travel 57.592/mese (conc. 27); senior flights 36.240 (conc. 15); airport tips 34.006 (conc. 29, +27%); senior travel tips 32.126 (conc. 30); travel tips for seniors 24.138 (conc. 24, +381%); airport security 32.761 (conc. 64, alta). Nomi di canali concorrenti (the senior traveler, susan parker travel, passport pro) NON usati nei tag. Titoli concorrenti: "flight attendants wish seniors knew these 10 boarding secrets" 29.818; "flying after 60 in uk: 7 legally protected rights airlines hope you never claim" 33.797.
- Tag short 9 aggiornati con: travel tips for seniors, senior flights, airport tips.

## 12. RICERCA PROSSIMO LUNGO 6 (16/10/2026, 0 crediti, ricerca YouTube "questo mese" ordinata per view)
### 12a. Stato canale (letto da YouTube 16/10)
Short 9 AEROPORTO (v-u3n1zHSno) 309 view = l'unico partito (gli altri short 32-107). Lunghi: Aeroporto (ovA7BP_I-rU, 2 giorni) 2 view; Bollette (91MmakhwyjM) 41; Costco (w-GQwECwTXA) 9; SNAP 10; lungo 1 5. Conclusione: il tema VIAGGI funziona col nostro pubblico.
### 12b. Cosa va ora (view | eta | durata | canale | titolo)
- 1.122.723 | 3 sett | 17:13 | Sharon Dawson | Flying Over 65? Why Airlines Quietly Treat You Different
- 411.334 | 2 sett | 14:12 | The Terminal Traveler | I Learned This Packing Trick From a Flight Attendant
- **177.401 | 8 giorni | 17:48 | TheOriginPlate | 12 Things Amtrak Never Tells Seniors Until They're Onboard** (U4EAHZMKHLM); stesso canale 15.851 in 3 giorni "...Until They Get Off the Train"; 28K "7 Amtrak Mistakes Seniors Make on Their First Sleeper Trip"; 9,5K "5 Free Amtrak Perks Seniors Over 65 Almost Never Claim"
- Olivia Brooks On Amtrak: 39.906 "Seniors: Don't Book an Amtrak Bedroom - Do This Instead!", 19.869, 19.595, 11.127
- 102.108 | The Senior Traveler | Flying Over 60? What to Say When Asking for a First Class Upgrade!
- 93.825 | 2 sett | 20:50 | Senior Travel Insider | 9 TSA Secrets Every Traveler Over 60 Should Know in 2026
- 36.157 | 2 giorni | Sharon Dawson | If You're Over 65, Airlines Will Quietly Give You These 9 Things (If You Ask); 30.049 | 1 giorno | The Airport Lounge Secret Most Seniors Never Use (And It's FREE)
- Crociere: 84.818 repositioning cruises; 70.424 15 cruise hacks; 47.410 7 best cruise lines; "Why Cruise Lines Quietly Treat Passengers Over 65 Differently" 20.175
- Fuori tema canale (salute, Messico, Canada, banca): ignorati. Hotel: tutto sotto 300 view (tema morto). "Senior Benefits Start at Age 55 (Not 65!)" Low Income Relief 307.898.
### 12c. Proposta: lungo 6 = AMTRAK / TRENO over 65 (seguito naturale dell'aeroporto, stessa formula dello short 9 che e partito). Fatti DA VERIFICARE su amtrak.com prima del copione (sconto senior 65+, assistenza, bagagli, posti, cancellazioni).
### 12d. vidIQ 16/10/2026 (autorizzato dall'utente; 15 crediti: keyword research 5 + trascrizione 5 + score_title 5; saldo 16 -> 1, rinnovo 11/11/2026)
- "amtrak seniors" 3.918/mese conc. 17,5 (overall 65); "amtrak" 25.993 conc. 64,6; "amtrak tips" 4.480 conc. 44; "amtrak trains" 6.801 conc. 36; "amtrak roomette" 4.658 conc. 22,8; "amtrak accessible bedroom" 4.739 conc. 25; "amtrak sleeper car" 4.634 conc. 28,5; "amtrak bedroom" 4.396 conc. 42; "train travel for seniors" 3.369 conc. 16; "senior travel tips" 25.005 conc. 30 (-43%); "california zephyr" 8.164 (+80%). Sotto 750: amtrak senior discount, amtrak for seniors, amtrak tips for seniors, senior train travel.
- Trascrizione U4EAHZMKHLM (177K): narratore anziano in prima persona, gancio storia (porta che non c'era), "due regolamenti", 12 sorprese pratiche a bordo, guida venduta a meta, riepilogo, parte onesta, "card" con 3 cose. Contenuto diverso dal nostro (noi: soldi e aiuti verificati).
- Titolo "If You're Over 65, Amtrak Gives You These 10 Things (If You Ask)": 92/100.
### 12f. vidIQ 17/10/2026 per pacchetto Amtrak (autorizzato: "controlla su vidiq tutto"; 20 crediti, saldo 150, rinnovo 16/11)
- matching_terms "amtrak senior": amtrak senior fares news report 4.924 conc. 43,5; amtrak senior discount tips older travelers 4.329 conc. 15,9; the amtrak senior discount mistake that costs retirees hundreds 4.139 conc. 11; amtrak trains senior tip 4.011 conc. 10,2; amtrak trains senior 3.702 conc. 19,2; former amtrak employee 17 things i would never do as a senior 3.366.
- matching_terms "train travel seniors": amtrak train travel for seniors tips 3.635 conc. 20,3; train travel for seniors 3.369 conc. 16,1.
- Titoli: "If You're Over 65, Amtrak Gives You These 10 Things (If You Ask)" 92; "Over 65 and Riding Amtrak? 10 Things You Can Ask For (Most Seniors Never Do)" 92; "Amtrak Senior Discount Mistake: 10 Things Riders Over 65 Should Ask For" 87.
- vidiq_score_thumbnail NON accetta immagini da URL esterni (raw.githubusercontent rifiutato): si puo valutare solo la miniatura gia caricata su YouTube (videoId).
### 12g. vidIQ 18/10/2026 titolo SHORT 10 AMTRAK (autorizzato: "controlla anche su vidiq"; 15 crediti, saldo 150 -> 135, rinnovo 16/11)
- "Over 65 and Riding Amtrak? 3 Things You Can Ask For (Almost Nobody Does) 🚆" 88 (scelto); "Riding Amtrak Over 65? 10 Things You Can Ask For (Almost Nobody Does) 🚆" 87; "Amtrak Over 65? The 1 Box Most Seniors Never Click 🚆" 83. Keyword: riusate 12d/12f (nessuna ricerca nuova).

## 13. RICERCA PROSSIMO LUNGO 7 (20/10/2026, autorizzata: "fai anche su vidiq le ricerche"; 10 crediti: outliers 5 + keyword research 5; saldo reale 10 -> 0, rinnovo 16/11/2026. NB: il file diceva 135, il saldo vero era 10)
### 13a. Stato canale (YouTube 20/10)
Lunghi: Amtrak (iiUOHdoQbPA, 3 giorni) 1 view; Aeroporto 2; Bollette 41; Costco 9; SNAP 10; lungo 1 8. Short: Aeroporto 327, Amtrak 27, sconti 115/79, SNAP 95, CSFP 92, Meals 53, LIHEAP 41, Bollette 40, Costco 33. Nessun lungo partito.
### 13b. vidIQ outliers (lunghi, questo mese, canali <100K, per view) - nuovi rispetto alle sezioni 9-12:
- 446.191 | Living Like It's 1950 (3.280 iscr.) | Why I Went Back To 1970s Winter Heating Habits At 52 (And Saved Hundreds) (vph 287)
- 360.449 | Earl Whitaker USA (1.300) | Seniors: 3 Pieces of Good News for Your Money in January (Social Security: no)
- 247.691 | Marilyn Vance (10.400) | 10 Things That Make Living Alone Easier After 65 (I Wish I'd Done #1 Sooner) (vph 1.234)
- 245.957 | 10 Things I Avoid Now That I Live Alone at 69
- **148.269 | Donna Fixes (1.840 iscr.) | 12 Cheap Things That Make Living Alone Easier This Winter After 60** (24 min)
- **90.212 | Donna Fixes (1.840) | 9 Home Services You Don't Actually Have to Pay For After 60** (23 min, breakout 266)
- **38.356 | Donna Fixes (1.840) | 11 Home Repairs You Can Get Done Free After 60 (Most People Never Ask)**
- 139.071 Dollar Tree 15 items seniors; 102.531 11 Dollar Tree Heating Items ... Winter Blackout (1.860 iscr.); 103.480 12 Walmart Items Seniors Should Buy Before the First Winter Blackout; 70.462 10 Dollar Tree Items Every Over 50 Needs (vph 2.678)
- 161.828 Robin MBA Aldi 14 Things; 131.022 Sharon Dawson Airlines 9 Things (If You Ask) (vph 1.572); 89.833 5 Bills You Legally Stop Paying After 65 (copia)
- 13.706 Frugal Flow "If You're Over 60, Costco Owes You These 12 Free Things" (1 giorno)
### 13c. YouTube gratis (questo mese): living alone/inverno (25 Winter Survival Tricks 334K; 10 Dump and Bake Dinners 495K: cucina, fuori tema); "They're Mailing THIS Card to Seniors - DON'T Activate It!" 321K (truffe); UK "15 Things You Stop Paying For at 60" 216K; "Senior Benefits Start at Age 55 (Not 65!)" 338K.
### 13d. vidIQ keyword "free home repairs for seniors" (US): seme <750; "senior home safety" 21.501/mese conc. 27,5 (overall 67,8, la migliore); "home repair grants" 4.364 conc. 25,9; sotto 750: home repair grants for senior citizens (conc. 15,6), usda section 504 home repair (6,6), home services seniors don't have to pay for, weatherization assistance program, free smoke alarms, area agency on aging, eldercare locator.
### 13e. Proposta lungo 7: SERVIZI E LAVORI DI CASA GRATIS DOPO I 60 + INVERNO (modello Donna Fixes, canale piccolo come il nostro: 148K, 90K, 38K). Titolo da confermare. Attenzione: Weatherization e USDA 504 gia nel lungo Bollette (usarli poco o con angolo diverso). Fatti da verificare su fonti ufficiali solo dopo conferma.

## 14. LUNGO 7 CASA-INVERNO: TITOLO (21/10/2026, ordine utente "vedi su vidiq"; 15 crediti: score_title 5 + generate_titles 5 + keyword matching_terms 5)
SALDO REALE (vidiq_balance 21/10): 172 = 150 rinnovabili (reset 14/11/2026) + 22 add-on. Dopo la spesa: 157. ERRORE MIO: avevo dato il saldo per 0 (nota sezione 13 sbagliata); controllare SEMPRE vidiq_balance (gratis) prima di dire che i crediti sono finiti.
- score_title "Over 60? 9 Kinds of Help You Can Get at Home This Winter (Most Never Ask)" = 97/100 (long, canale Senior).
- generate_titles (8): 97 "9 Things Seniors Over 60 Should Claim Before Winter (Most People Don't Know)"; 97 "Don't Struggle This Winter: 9 Types of Help Seniors Over 60 Can Get (If You Ask)"; 96 "Home Repairs and Help for Seniors Over 60: 9 Things You Can Get This Winter (If You Ask)"; 96 "9 Ways to Make Your Home Safer This Winter: Free Help..." (free non verificato: non usare); 94 "Over 60? 9 Types of Help You Can Get This Winter (Most Never Ask)"; 93 x3.
- keyword_research matching_terms "help for seniors at home": 0 risultati.

## 15. SHORT 11 CASA-INVERNO: TITOLO (22/10/2026, ordine utente "pacchetto da professionista"; 15 crediti: 2 score_title short + 1 generate_titles short; saldo 157 -> 142)
- score_title short: "Over 60? 9 Kinds of Help That Come to Your Home This Winter ❄️" = 88; "Over 60? Help Can Come to Your Home This Winter (Almost Nobody Asks) ❄️" = 94 (SCELTO).
- generate_titles (6): 94 "Over 60? 9 Types of Winter Help You're Missing Out On #seniors #freehelp #winter"; 91 "9 Essential Winter Services Seniors Over 60 Are Ignoring"; 90 x4 (tutti con "free"/hashtag nel titolo: "free" non verificato, non usato).

## 16. RICERCA PROSSIMO LUNGO 8 (22/10/2026, 0 crediti, ricerca YouTube gratuita "questo mese" ordinata per view + tutti i tempi; ordine utente "crea il nuovo video come un professionista, cerca cosa funziona")
### 16a. Canale (YouTube 22/10): short Aeroporto 336, sconti 132/80, CSFP 99, SNAP 95, Meals 58, LIHEAP 41, Bollette 40, Costco 33, Amtrak 27, Casa-inverno 5. Lunghi: nessuno partito (vedi 13a).
### 16b. Cosa va ora (view | eta | durata | canale | titolo)
- 239.425 | 2 sett | 23:31 | The Smart Steward | If You're Over 65, Aldi Will Give You These 9 Things (If You Ask) (stesso canale poi: Thanksgiving 11K, Winter 5K, 11 Free Perks 3,6K = Aldi in saturazione)
- 188.256 | 2 sett | 13:50 | Robin MBA | If You're Over 60, Aldi Will Give You These 14 Things (If You Ask)
- 153.092 | 8 giorni | 15:45 | Sharon Dawson | If You're Over 65, Airlines Will Quietly Give You These 9 Things (If You Ask)
- 143.759 | 2 sett | 14:30 | Robin MBA | Free Food Benefits Start at Age 60 (Not 65) - Many Seniors Never Claim Them
- 353.957 | 4 sett | 15:49 | Low Income Relief | These Senior Benefits Start at Age 55 (Not 65!)
- 49.175 | 2 giorni | 18:51 | Elaine Hargreaves | If You're Over 65, Your UK Supermarket Will Give You These 12 Things (If You Ask)
- Costco "Owes You" copie questo mese: 59K (Canada), 26K, 15,6K, 6K, 5K, 4K = saturo.
- Crociere "Will Quietly Give You 9 Things" 17K; hotel tutto sotto 400 (morto); Walgreens/CVS/Kroger/Home Depot/Target/telefonia sotto 3.600 (poca domanda).
- Bollette "5 Bills After 65": decine di copie (100K, 83K, 50K, poi centinaia di view) = saturo e tema tasse/Medicare (non nostro).
### 16c. WALMART (domanda alta e continua, nessun video forte nelle ultime 2 settimane)
- Tutti i tempi: 499.377 | 3 mesi | 12:04 | Vital Over 60 | Walmart Is Hiding 14 Discounts From Seniors Over 60 (Here's Every One) (1TyPvFJlCrc); 369.514 | 4 mesi | 27:05 | The Retiree Wallet | 18 Walmart Senior Discounts Cashiers Won't Mention (-tvHAmhsWHc); 103.547 | 3 mesi | 9:18 | Smart Steward | 11 MORE Things Seniors DON'T Know Walmart Gives For FREE (BMcbTp4kqzc).
- Questo mese: 24.313 | 9 giorni | Silas Invests | If You're Over 55, Walmart Will Give You These 7 Things For FREE (If You Ask); 14.347 | Frugal Frannie | If You're Over 60, Walmart Owes You These 11 Free Things; 913 Smart Steward stesso titolo; 37 "Does Walmart Owe You After 60? (Fact-Checked)".
- Capitoli del 499K: $4 generic prescriptions, $10 per 90 giorni, Walmart+ Assist a meta prezzo, "AARP discount", carta spesa Medicare Advantage, "codice segreto nel cartellino", scanner prezzi app, programma valore cliente, chiedere al capo reparto, ribassi di fine giornata su carne/pane/frutta, Walmart si allinea ai propri prezzi, 10 centesimi sulla benzina, Walmart Cash, ritiro gratis senza minimo. ATTENZIONE: diverse voci non verificate o dubbie (AARP, codice cartellino, benzina, ritiro senza minimo): NON copiarle; ogni voce va verificata su walmart.com / corporate.walmart.com prima del copione. Medicare Advantage = tema Money Backstory: escluso.
### 16d. Proposta lungo 8 (da confermare dall'utente): WALMART over 60, formula vincente "If You're Over 60, Walmart Will Give You These N Things (If You Ask)", N = solo le voci verificate su fonti ufficiali Walmart; durata 15-20 min.
### 16e. vidIQ 22/10/2026 (ordine utente "devi controllare anche su vidiq"; saldo reale 67 = 25 rinnovabili + 42 add-on, reset 14/11; spesi 35: 2 outliers + 2 keyword + 3 score_title; saldo 32)
- Outliers "cose che gli over 60 possono avere" (questo mese, canali <100K, per view): 982K Every Senior Must Do This Before October 1; 738K 12 New Costco Rules Coming This Fall (Frugal Flow 66K); 577K New Laws Start October 1st; 468K 9 Ways I Keep My Bed Warm With No Heat (1,6K iscritti); 467K 1970s Winter Heating Habits; 369K 3 Pieces of Good News January; 354K 5 Bills UK; 292K Food Assistance Oct 1; 289K Living Alone After 65; 241K Amtrak 12 Things; 239K Aldi 9 Things (If You Ask); 191K Dollar Tree Over 50; 153K Airlines 9 Things (If You Ask); 152K Donna Fixes winter; 144K Free Food Benefits Start at 60; 143K/120K Dollar Tree winter; 91K Donna Fixes 9 Home Services; 39K Donna Fixes 11 Home Repairs; 8,8K 11 Senior Discounts They Don't Want You To Know.
- Outliers "Walmart for seniors over 60" (6 mesi, per view): 499K Walmart Is Hiding 14 Discounts From Seniors Over 60 (Vital Over 60, 6,2K iscritti, breakout 3128x, giugno); 554K 12 Restaurants Where Seniors Eat Free (Retiree Wallet, maggio); 457K In Case You Don't Believe What WALMART Is Doing (non senior); 196K 17 Stores That Give Seniors 40% Off; 158K 17 Stores That Give Seniors HUGE Discounts; 104K 11 MORE Things Seniors DON'T Know Walmart Gives For FREE (Smart Steward, breakout 588x).
- Keyword (US): "walmart senior discount" <750/mese conc. 17,3; "seniors walmart" 4.926/mese conc. 7,7 (overall 70, la migliore); "10 things seniors should never buy at walmart" 4.384 conc. 15,5; "walmart is hiding 14 discounts from seniors over 60" 3.815 conc. 23,5; "seniors money costco walmart warning" 3.348 conc. 13,5; "walmart secrets" 6.610 (+82%); "walmart deals" 20.914 (+447%, stagione feste); "walmart shopping tips" 4.048 conc. 32,9; "walmart clearance secrets" 4.935 conc. 27,8; "senior discounts" 16.912 conc. 32,9 (-16%).
- score_title (long, canale Senior): "If You're Over 60, Walmart Will Give You These 12 Things (If You Ask)" 92; "Over 60? Walmart Will Quietly Give You These 12 Things (Most Seniors Never Ask)" 88; "12 Things Walmart Gives Seniors Over 60 That Cashiers Never Mention" 86. (12 = numero di prova: quello vero dopo la verifica dei fatti.)
- Decisione proposta: WALMART, titolo da 92.
