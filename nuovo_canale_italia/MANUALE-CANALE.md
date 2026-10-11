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
- Video lungo 1920x1080, 30 fps, durata 10–14 minuti (sopra gli 8 minuti = pubblicita a meta video, categoria Business).
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
