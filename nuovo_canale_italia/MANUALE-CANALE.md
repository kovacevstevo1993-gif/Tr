# MANUALE DEL CANALE "TRAPPOLE E CONTI VERI" (nome da decidere)
Versione 1 – 11/10/2026. Vale per OGNI video. Tavole visive in `brand/` (tavola-1 colori, tavola-2 fotogramma tipo, tavola-3 miniatura tipo). Codice: `code/tavole_brand.py`.

## 1. Cosa siamo (in una riga)
Ogni video apre una PRATICA su una grande spesa degli italiani, trova le trappole e fa i conti veri in euro. Alla fine: il Verdetto.

## 2. I 6 marchi di fabbrica (sempre presenti, ci fanno riconoscere)
1. **Il Contatore**: riquadro nero con bordo rosso in alto a destra, scritta grigia "STAI PERDENDO" e cifra rossa in IBM Plex Mono. Parte da € 0 al secondo 1 e sale a ogni trappola, con un "tic" sonoro. La cifra finale si scopre solo alla fine.
2. **La Pratica**: foglio color carta, leggermente storto, sulla scrivania scura. In alto "PRATICA N. 00X · ARGOMENTO · RISERVATO". Numerazione continua per tutto il canale (lo spettatore colleziona le pratiche).
3. **L'evidenziatore giallo e la penna rossa**: la riga che conta si evidenzia in giallo, il numero-trappola si cerchia a penna rossa (animazione disegnata a mano).
4. **Il segnatrappole**: pillola rossa "TRAPPOLA 1 DI 3". Si sa sempre quante ne mancano.
5. **"Indovina"**: a metà video la voce chiede una cifra, 3 secondi di conto alla rovescia, poi la risposta.
6. **Il Verdetto**: timbro finale CONVIENE (verde) / NON CONVIENE (rosso) / DIPENDE DA TE (giallo), con colpo sonoro di timbro.

## 2b. Versione 2 della grafica (11/10/2026, richiesta utente: "piu originale e bello da vedere, perfetto dalla A alla Z")
Fotogrammi tipo: `brand/v2-1-gancio.png`, `v2-2-apertura-pratica.png`, `v2-3-trappola.png`, `v2-4-indovina.png`, `v2-5-verdetto.png`. Codice: `code/fotogrammi_v2.py`.
- **Scrivania fotorealistica** (`brand/assets/scrivania.png`): piano scuro, lampada calda in alto a sinistra, calcolatrice, penna stilografica, caffe. Uguale in tutti i video = il nostro "studio".
- **Contatore a rulli meccanici** (come una pompa di benzina/tassametro): cifre rosse su rulli neri, spia rossa, i rulli GIRANO quando la cifra sale (con "tic" sonoro). Nel gancio le ultime cifre girano senza fermarsi: la cifra esatta si vede solo alla fine.
- **Cartellina della pratica** con linguetta "N. 001", etichetta, note scritte a mano, polaroid del prodotto fermata con la graffetta, timbro RISERVATO.
- **Lente d'ingrandimento** che scorre sul contratto e si ferma sulla cifra-trappola (evidenziata in giallo).
- **Post-it giallo** scritto a mano ("riga 4! leggi qui") = la voce interiore dello spettatore.
- **Indovina**: tre cartellini A/B/C sul tavolo + cerchio rosso del conto alla rovescia 3-2-1 + scritta a mano "Scrivilo nei commenti".
- **Verdetto = scontrino**: lo scontrino della pratica elenca ogni trappola con la sua cifra e il TOTALE IN PIU in rosso, firma "Grazie per non aver firmato." + timbro + contatore finale + pillola verde "COME EVITARLO".
- Caratteri aggiunti: Caveat (scrittura a mano), Permanent Marker (riserva).
- Movimento: camera lenta sulla scrivania (zoom e scorrimento 2-4%), fogli che entrano con ombra, lente che scorre, penna che disegna il cerchio, timbro che cade con piccolo scossone dell'immagine.

## 3. Colori (fissi, mai altri)
| Nome | Hex | Uso |
|---|---|---|
| Scrivania | #101114 | fondo di ogni video |
| Carta | #F3F0E8 | fogli della pratica |
| Inchiostro | #16181D | testo sui fogli |
| Rosso trappola | #E32119 | SOLO soldi persi, trappole, contatore, NON CONVIENE |
| Evidenziatore | #FFE14A | la frase/riga che conta |
| Verde conviene | #19A35B | SOLO risparmio e CONVIENE |
| Grigio nota | #8A8F98 | etichette, fonti |
Regola: massimo 3 colori per inquadratura. Diverso da tutti gli altri canali dell'utente (niente blu/oro, niente verde bosco/avorio, niente verde acqua).

## 4. Caratteri (file in `brand/fonts/`)
- Titoli: **Archivo Black**.
- Numeri, pratica, contatore, etichette: **IBM Plex Mono** (Bold/Medium).
- Testi e sottotitoli: **Inter SemiBold**.

## 5. Formato
- Video lungo progettato in 1920x1080 ma ESPORTATO in 2560x1440 (o 3840x2160): YouTube da piu qualita (codec migliore) ai video caricati sopra il 1080p. 30 fps, durata 10–14 minuti (sopra gli 8 minuti = pubblicita a meta video, categoria Business).
- Audio voce: -14 LUFS integrati, picchi sotto -1 dB, niente fruscio; musica a -24 dB sotto la voce.
- Voce: A (Gemini TTS, voce Charon), montata da Claude. Controllo pronuncia con trascrizione su ogni blocco.
- Sottotitolo della frase chiave in basso (barra nera arrotondata, Inter bianco), solo le frasi forti, non tutto.
- Short verticali 1080x1920: una trappola sola, contatore grande al centro, rimando al video lungo come "Video correlato".

## 6. Struttura di ogni video lungo (sempre questa)
| Tempo | Parte | Cosa succede |
|---|---|---|
| 0:00–0:20 | **Gancio** | La cifra finale a meta (es. "€ 2.8__") o una frase che spiazza. Il contatore appare a € 0. Si promette il Verdetto. |
| 0:20–0:45 | **Apertura pratica** | Timbro "PRATICA N. 00X". Chi riguarda (es. "se stai per comprare un'auto a rate"). Si dice quante trappole ci sono. |
| 0:45–3:00 | **Trappola 1** | La piu piccola. Contratto, evidenziatore, conto. Contatore sale. |
| 3:00–6:00 | **Trappola 2** | Media. Si annuncia: "la terza e quella che costa di piu, ci arrivo". |
| a meta | **Indovina** | Domanda allo spettatore + 3 secondi + risposta. Invito a scriverla nei commenti. |
| 6:00–9:30 | **Trappola 3** | La piu grossa. Il contatore fa il salto piu grande. |
| 9:30–11:00 | **Come evitarle** | 3 mosse pratiche, in verde. Lo spettatore esce con qualcosa di utile (per questo torna). |
| 11:00–11:40 | **Il Verdetto** | Contatore finale + timbro. |
| 11:40–12:00 | **Prossima pratica** | Anticipo della pratica successiva (schermata finale 20 s). |
| fine | **Disclaimer** | Slide finale + voce: "Regole, importi e condizioni cambiano. Controlla sempre la fonte ufficiale. Informazione generale, non consulenza finanziaria." |

## 7. Psicologia (decisione: si usa quella che tiene di piu, l'utente ha lasciato scegliere)
Base del canale = psicologia diretta, perche e quella che tiene lo spettatore per tutto il video:
- **Paura di perdere soldi** (piu forte del desiderio di guadagnarli): il Contatore mostra la perdita, non il risparmio.
- **Curiosita aperta**: cifra finale nascosta, "TRAPPOLA 1 DI 3", "la terza e la peggiore, ci arrivo". Ogni domanda si chiude solo dopo averne aperta un'altra.
- **Coinvolgimento**: "Indovina" + commenti; "scrivi nei commenti la rata che paghi".
- **Riprova sociale**: "8 italiani su 10 firmano senza leggere questa riga" (solo con dato vero e fonte).
Psicologia inversa = solo dove funziona meglio, cioe nel gancio iniziale e in qualche passaggio (max 2 per video), detta con naturalezza, mai ripetuta uguale:
- "Firma pure. Davvero. Questo video non ti serve… a meno che la rata non sia sotto i 200 euro."
- "Se ti basta sapere che la rata e bassa, puoi chiudere qui."
- "Le banche preferirebbero che non arrivassi al minuto 6."
Mai usata in modo falso: la promessa del gancio va SEMPRE mantenuta nel video (YouTube penalizza i titoli ingannevoli e lo spettatore non torna).

## 8. Regole di montaggio (per tenerli "in catalessi")
- Cambio visivo ogni 4–6 secondi (zoom lento sulla pratica, nuova riga che si scrive, evidenziatore, cerchio, foglio che entra). Mai un'immagine ferma oltre 6 s.
- Ogni elemento compare quando la voce lo dice; l'ultimo elemento di ogni slide compare all'80% della durata della slide; tutto completo prima che la voce passi oltre (regole generali del repo).
- Movimento lento e morbido (easing), niente effetti PowerPoint.
- Controllo di OGNI fotogramma prima della consegna (regola del repo).

## 9. Suono (riconoscibile come i colori)
- Firma sonora di 2 secondi all'apertura pratica: macchina da scrivere + timbro.
- Contatore: "tic" metallico a ogni scatto; salto grande = registratore di cassa.
- Timbro del Verdetto: colpo sordo.
- Musica di sottofondo bassa, tesa (stile indagine), senza copyright, a -24 dB sotto la voce.

## 10. Titoli (formule)
- Cifra + trappola: "La rata bassa che ti costa 2.847 €".
- Inversa: "Firma pure il finanziamento (prima guarda la riga 4)".
- Domanda: "Fotovoltaico: conviene davvero? Ho fatto i conti veri".
- Niente MAIUSCOLO tutto intero, max 60 caratteri, senza hashtag nel titolo.

## 11. Miniature (sempre riconoscibili)
- Fondo scrivania scura, 2 righe di titolo in Archivo Black bianco, il Contatore rosso grande, un pezzo di pratica storto con riga gialla, un timbro rosso (NON FIRMARE / TRAPPOLA / ATTENZIONE).
- Max 5 parole. Nessuna faccia (il marchio e il Contatore).
- Modello: `brand/tavola-3-miniatura-tipo.png`.
- Attrazione massima (richiesta utente 11/10/2026): 3 miniature diverse per ogni video, punteggio vidIQ prima di pubblicare (chiedere prima, costa crediti), poi test A/B gratuito di YouTube Studio ("Prova e confronta") con tutte e 3: vince quella con piu tempo di visione. Nella miniatura il foglio chiaro e il contatore rosso devono occupare almeno meta immagine (visibili anche in modalita scura).

## 12. Pubblicazione
- Ritmo consigliato: 1 video lungo a settimana + 3 short (uno per trappola) che rimandano al lungo.
- Playlist per settore: Auto, Casa e mutui, Energia e bollette, Banca e carte, Assicurazioni, Spesa e acquisti.
- Descrizione: gancio, capitoli, "Fonti: nome dei siti ufficiali" (senza link lunghi), riga Iscriviti, Disclaimer. Commento fissato: una domanda al pubblico.
- Impostazioni: come negli altri canali dell'utente; nessuna persona finta che si presenta come esperto, dati solo da fonti ufficiali (Banca d'Italia, ARERA, ISTAT, IVASS, siti delle aziende).

---
# PARTE 2 – MONETIZZAZIONE SENZA RISCHI E MEDIA BRAND (11/10/2026)
Richiesta utente: "Deve essere sempre monetizzabile il canale senza rischiare niente quando avrò accesso alla monetizzazione non devo aver nessun problema." Controllato sulle pagine ufficiali di YouTube (Norme sulla monetizzazione dei canali, Contenuti alterati o sintetici, Programma partner) e sulle Linee guida AGCOM influencer (luglio 2025).

## 13. Le 4 regole YouTube che potrebbero toglierci la monetizzazione (e come le rispettiamo)
1. **Contenuti "non autentici" (ex "ripetitivi", dal 15/07/2025).** Vietati: slideshow, storie a modello o testo che scorre "con poca o nessuna narrazione, commento o valore educativo", contenuti fatti con l'AI "con modelli generici" che danno l'idea di produzione di massa. Permessi: stessa intro/outro con contenuto diverso, serie in cui ogni video ha un focus distinto.
   -> Ogni video ha: ricerca nuova, conti fatti apposta, copione originale scritto per quel tema, oggetti di scena diversi per settore (chiavi auto, bolletta, chiavi di casa, polizza…), trappole diverse. Mai due video con la stessa struttura di frasi. Mai piu di 1 video lungo al giorno. L'utente sceglie i temi e approva ogni copione (direzione creativa umana).
2. **Contenuti riutilizzati.** Vietato leggere testi di altri (articoli, siti, notizie) o copiare video. -> Copioni sempre originali; le fonti ufficiali si citano, non si leggono.
3. **Persona AI che si presenta come esperto umano su temi finanziari = NON monetizzabile.** -> La voce e una VOCE NARRANTE: non dice mai "sono un consulente/esperto/avvocato", non ha nome e cognome finti, nessun avatar o faccia AI. Parla di "noi" come canale e di "i conti" e "i documenti".
4. **Truffe / soldi facili / titoli ingannevoli.** Vietati "diventa ricco", "guadagno garantito", promesse di soldi facili. Le regole valgono anche per titolo, miniatura, descrizione e tag. -> Noi spieghiamo come NON perdere soldi; ogni promessa del titolo si mantiene nel video.

## 14. Etichetta "contenuti alterati o sintetici" (YouTube)
- Va dichiarato solo il contenuto realistico che fa sembrare vero qualcosa che non e successo (persona reale che dice cose mai dette, scena realistica mai avvenuta, evento reale alterato, musica AI protagonista).
- Non serve per: voce narrante sintetica generica (non imita una persona reale), grafiche, contatore, fogli, scritte, elementi non realistici, sfondi.
- Nostra regola prudente: niente scene fotorealistiche AI di persone o eventi; per le foto dei prodotti (auto, case, pannelli) usare foto con licenza libera (Pexels/Unsplash) o grafiche disegnate. Se in un video serve un'immagine AI realistica di una scena -> si spunta "Si" in YouTube Studio (zero rischio).

## 15. Regole italiane
- **AGCOM influencer (delibera luglio 2025):** valgono per chi supera 500.000 iscritti o 1 milione di visualizzazioni medie al mese. Obblighi: pubblicita sempre dichiarata (#adv / "Contenuto sponsorizzato" + funzione YouTube "Include promozione a pagamento"), segnalare l'uso dell'AI, iscrizione al registro. -> Le applichiamo DA SUBITO: nella descrizione di ogni video la riga "Voce narrante e alcune immagini realizzate con strumenti digitali/AI. Dati da fonti ufficiali."; ogni sponsor o affiliazione dichiarata.
- **Niente consulenza finanziaria personalizzata** (attivita riservata in Italia): mai "compra questo prodotto/titolo", sempre spiegazioni generali + disclaimer "Informazione generale, non consulenza finanziaria."
- **Aziende citate:** solo dati pubblici e verificabili (contratti tipo, fogli informativi, Banca d'Italia, ARERA, IVASS, ISTAT), linguaggio neutro ("questa clausola costa X"), mai "truffa" riferito a un'azienda con nome. Niente loghi di marchi nelle miniature.
- **Musica:** solo Libreria audio di YouTube (zero reclami Content ID). Caratteri: tutti con licenza libera OFL (gia controllato).
- Prima di attivare affiliazioni su prestiti, mutui o carte (prodotti di credito): farle controllare a un commercialista/avvocato, perche in Italia la promozione del credito ha regole proprie. Le affiliazioni su comparatori e prodotti non finanziari sono piu semplici.

## 16. Requisiti per la monetizzazione (da sapere)
- Oggi (ufficiale): 1.000 iscritti + 4.000 ore di visualizzazione in 12 mesi, oppure 10 milioni di visualizzazioni Short in 90 giorni; verifica in 2 passaggi attiva; nessun avvertimento attivo; account AdSense.
- Dal 1/02/2027 YouTube cambia il Programma partner (ufficiale: "aggiornamenti dal 1 febbraio 2027", termini da accettare entro il 31/01/2027). Fonti non ufficiali riportano soglie nuove per chi entra: 8.000 ore o 20 milioni di visualizzazioni Short. -> Strategia: video lunghi 10–14 minuti (piu ore per ogni visualizzazione) e video "sempreverdi" che fanno ore per anni.
- Livello intermedio (500 iscritti, abbonamenti e Super Thanks) da usare appena possibile.

## 17. Il canale come media brand (adattato dal piano dell'utente)
- **Nicchia dominante:** le grandi spese delle famiglie italiane (auto, casa, energia, banca, assicurazioni, acquisti). Non "tutta la finanza".
- **Valore unico:** competenza (conti veri e fonti ufficiali) + racconto visivo (la Pratica) + produzione da cinema (scrivania, contatore a rulli, suono).
- **Entrate multiple, in ordine di arrivo:**
  1. Pubblicita YouTube (AdSense).
  2. Affiliazioni dichiarate: comparatori (luce/gas, assicurazioni, conti), strumenti utili (es. calcolatrici, app di budget). Controllo legale prima, vedi sez. 15.
  3. "Kit anti-trappola": checklist PDF + calcolatore (foglio o pagina web) per ogni settore, fatti da Claude, venduti a pochi euro o dati in cambio dell'email (newsletter).
  4. Sponsor di settore (dopo i primi 10.000 iscritti), sempre dichiarati.
  5. Abbonamenti al canale (membership) con pratiche in anteprima.
- **Attrezzatura:** non servono telecamere, microfoni o luci (canale senza volto): l'equivalente e la qualita digitale = voce pulita a -14 LUFS, render 1440p/4K, grafica a 30 fps controllata fotogramma per fotogramma, suono curato.

## 18. Catena di produzione di ogni video (pipeline)
1. **Ricerca:** tema con domanda alta (YouTube Italia + vidIQ), concorrenza, fonti ufficiali. Si annota tutto in RICERCHE-VIDIQ.md.
2. **Titolo + 3 miniature PRIMA del copione** (se non si riesce a fare un titolo forte, il tema si scarta).
3. **Copione con mappa della ritenzione:** gancio 0–30 s (promessa confermata entro 10 s, nessuna sigla), un nuovo "anello di curiosita" ogni 60–90 s, cambio visivo ogni 4–6 s, effetto/sorpresa ogni 10–15 s. Obiettivo: oltre il 60% degli spettatori dopo 30 s, oltre il 50% a meta video. L'utente approva.
4. **Voce** (Gemini, voce A) + controllo con trascrizione.
5. **Animazione e montaggio** da codice, controllo di ogni fotogramma.
6. **Pacchetto:** titolo, descrizione con capitoli e fonti, tag, commento fissato, schermata finale verso il video successivo (tempo di sessione).
7. **Pubblicazione** + test A/B miniature (Prova e confronta).
8. **Analisi a 48 ore e 7 giorni** (CTR, durata media, punto dove escono) -> correzioni sul video dopo.

## 19. Short e imbuto di crescita
- 3–5 Short a settimana: ognuno = una trappola sola presa dal video lungo (non tagliata: rifatta in verticale con contatore grande), "Video correlato" = il lungo.
- Video lungo 1 a settimana (stesso giorno e ora).
- Post della community: sondaggi ("Quanto paghi di rata?", "Prossima pratica: auto o mutuo?"), anteprima della miniatura della prossima pratica.
- Playlist per settore + "Tutte le pratiche" in ordine di numero (fa guardare piu video di fila).
- Dirette: no (canale senza volto); al loro posto, una volta al mese, "Pratica dei vostri commenti": si analizza un caso arrivato nei commenti.

## 20. Continuita: ogni video identico anche se un servizio si blocca (11/10/2026)
Domanda utente: "Si ma se ogni volta ti blocchi così come farà ad essere uguale ogni video?"
- Tutto cio che si ripete in ogni video e GIA salvato nel repo e non dipende da nessun servizio esterno: scrivania (`brand/assets/scrivania.png`), caratteri (`brand/fonts/`), contatore a rulli, cartellina, lente, post-it, cartellini, scontrino, timbri, colori (tutto in `code/fotogrammi_v2.py`). Si rigenerano uguali al pixel, gratis, sempre.
- Le foto che cambiano per ogni tema (auto, casa, pannelli, bollette): da archivi di foto libere senza limiti (Openverse CC0, Pexels, Unsplash, Wikimedia) + scontorno automatico in locale (rembg). Nessun credito necessario.
- Immagini AI (Pollinations, Gemini): solo extra facoltativo. 11/10/2026: credito Pollinations esaurito, quota immagini Gemini gratuita = 0.
- Voce A (Gemini TTS gratuito): ha limiti giornalieri (il modello "pro" ha dato errore 429; il modello della voce A ha funzionato). Per non dipendere dai limiti: attivare la fatturazione sulla chiave Gemini (costo di pochi centesimi a video) – DECIDE L'UTENTE.
- Ricerche gia fatte (11/10/2026): il 44% delle ore di YouTube negli USA si guarda sulla TV (eMarketer 2026) -> grafica pensata per TV e telefono (testi grandi, niente dettagli minuscoli). Studio su 300.000 video virali: miniature con o senza faccia rendono in media uguale. Miniature con 1–5 parole rendono di piu di quelle con 11+. Miniature italiane che vincono nella nicchia (Quattroruote, Geopop, Macchinando, Italia In Scaffale, Alberto Filippini): oggetto concreto grande (auto, pannello, prodotto), cerchio rosso, 2–3 parole in riquadro bianco/giallo, colori accesi -> le nostre avranno sempre l'oggetto vero grande sotto la luce della lampada + contatore + timbro.
