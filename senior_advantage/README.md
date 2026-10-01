# The Senior Advantage — progetto recuperato

Canale YouTube **@TheSeniorAdvantage**: il vecchio canale da ~1.700 iscritti americani (prima parlava di video divertenti), rilanciato il 27/09/2026 con una nuova identità. Recuperato dall'export delle chat (chat "Rilanciare canale YouTube con nicchia ad alto CPM", 27-29/09) e dalla memoria.

## Identità
- Nicchia larga: **sconti, benefici, aiuti e risparmi pratici per gli over 60 negli USA**. Niente pensione, Medicare, tasse e Social Security: quelli sono dell'altro canale (The Money Backstory), per non rubarsi il pubblico.
- Descrizione del canale (inglese, già impostata): "Real benefits, discounts and savings most Americans over 60 never claim. Every video breaks down one program, one discount or one rule in plain English, with official sources... No hype, no sales pitch. Just what you are entitled to, and how to get it."
- Caricamento predefinito già impostato (fonti, Subscribe, disclaimer). Utilizzo dell'IA: **No**. Promozione a pagamento: **No**.

## Regole fisse (decise da te)
1. Slide **verde bosco e avorio**, come la foto profilo. Dettagliate, con movimenti e grafici diversi da quelli di The Money Backstory (qui: cerchi che si riempiono, numeri che salgono, icone che entrano di lato, fondo con anelli incisi che ruotano piano e polvere d'oro). **Niente cornice oro 3D e niente stile "finanza seria".**
2. Gli stessi colori e lo stesso stile **in tutti gli short e nei video lunghi**. Si migliora (più oggetti, più dettagli), non si cambia lo stile.
3. **Oggetti reali** nelle slide legati a quello che dice la voce: soldi, scontrino, carrello, cartellino del prezzo, piatto, telefono, biglietto del cinema.
4. **Gancio iniziale** in ogni video: una cifra o una regola che sorprende.
5. Short: 35-45 secondi, una frase per clip, 1 al giorno (massimo 2, distanziati). Voce CapCut, tu mandi gli screenshot della timeline a fine di ogni frase e le slide si fanno sulla tua timeline.
6. Video lungo: oltre i 10 minuti. Niente musica di sottofondo.
7. Ogni video: titolo con la parola chiave all'inizio, descrizione completa da incollare, tag sotto 500 caratteri, commento fissato, miniatura, playlist (prima ti dico dove va).

## Colori e font (dal codice `code/engine.py`)
| Nome | RGB |
|---|---|
| Verde scuro (sfondo) | 7, 38, 30 |
| Verde medio | 14, 58, 45 |
| Verde chiaro (luce) | 26, 92, 71 |
| Riquadri | 12, 58, 45 |
| Avorio (testo) | 246, 241, 229 |
| Salvia | 154, 200, 170 |
| Salvia scuro (bordi) | 96, 143, 114 |
| Oro (cartellino prezzo) | 228, 179, 99 |
Font: **Lora** (numeri e titoli serif) e **Poppins Bold/Medium** (testi). Sono in `code/fonts/`.

## Come si fanno le slide
`code/engine.py` è il motore: sfondo animato, ombre, riquadri, oggetti disegnati (banconota "SENIOR RATE", cartellino "55+") e funzione `render()` che crea gli MP4 a 30 fps con ffmpeg.
- **Short**: 1080×1920 (verticale). Esempi: `s1.py` (short 1), `s2_7.py`, `scenes2.py` (short 2), `scenes3.py` (short 3), `cover1.py`, `cover2.py`, `cover3.py` (copertine), `logo*.py`, `banner.py`.
- **Video lungo**: lo stesso motore in orizzontale 1920×1080, senza cambiare colori o stile: `SA_W=1920 SA_H=1080 python3 ...`. Provato: stessi colori e stessi oggetti, vedi sotto.
- Serve `ffmpeg` e `pip install pillow numpy`.

## Come lavori (preferenze salvate in memoria, valgono anche qui)
- Risposte corte. Niente "hai ragione" e niente scuse: direttamente la cosa da fare.
- Una cosa alla volta. Il piano completo lo prepara e lo tiene Claude; prima di iniziare un video vuoi il piano completo e pronto.
- Verificare da soli prima di dare un'indicazione: ogni modifica da rifare ti costa tempo.
- **Non spendere crediti vidIQ senza dirtelo e chiederlo prima.** Dirti il costo prima di ogni generazione.
- Slide e grafica le fa Claude con il codice, gratis. Mai generatori a crediti.
- Titolo, descrizione e tag già completi da incollare così come sono (Subscribe e disclaimer compresi).
- Dirti PRIMA, senza che tu chieda, dove va ogni nuovo video (playlist, cosa creare o cancellare su YouTube).
- Le miniature devono avere la frase/hook che hai in mente tu: rileggere i tuoi messaggi prima di rifarle.
- Durate: le detta la tua timeline CapCut. Voce CapCut circa 11 caratteri al secondo (+ qualche decimo per ogni "…" o "—").
- Non farti rifare quello che hai già montato. Non proporti mai di fermarti o rimandare.
- **Mai mischiare questo canale con The Money Backstory** (pensione, Social Security, Medicare, tasse): due canali con argomenti diversi.

## Gli short pubblicati (testi in `chat/`)
1. **"Senior Discounts Start at 55 — Not 65 (Most Never Ask)"** (promo, quello più cercato). Gancio: "Most senior discounts in America start at fifty-five. Not sixty-five." 7 frasi, ~33 s. Dopo 24 ore: 21 view; 18,2% delle view da ricerca "senior discounts". Ritenzione ~75%.
2. **"Senior Discounts Nobody Tells You About (55, 60 & 62+)"**: Chili's 10% da 55, piani telefonici AT&T/T-Mobile/Verizon da 55, AMC da 60, National Parks Senior Pass $80 a vita da 62.
3. (pubblicato il 30/09) **"Senior Meals Can Be Delivered to Your Door (Meals on Wheels 60+)"**: Eldercare Locator 1-800-677-1116, eldercare.acl.gov. Playlist "aiuti" a parte.
- Short 4 previsto: aiuto per pagare le bollette di luce e riscaldamento.
- Playlist: "Senior Discounts" (short 1 e 2), una separata per gli aiuti (short 3 e successivi).

## Dati SEO salvati (vidIQ)
- "senior discounts" 12.828/mese (16.543 in un'altra misura), concorrenza ~26: la ricerca che porta le view.
- "senior discount" e "senior citizen discounts" correlate; "hidden senior discounts" 4.045/mese, concorrenza bassa.
- "senior meals" 7.069/mese; "meals on wheels" 5.242; "senior assistance programs" 4.229 (conc. 21); "low income relief" 24.886.
- Crediti vidIQ: 150 rinnovabili il 29/10 (alcuni usati dopo).
- Scadenza: dal 1/2/2027 la monetizzazione per i nuovi creatori richiede 8.000 ore o 20 milioni di view Short; oggi 1.000 iscritti + 4.000 ore (o 10 M view Short). Hai 1.700 iscritti: mancano le ore, quindi servono i video lunghi.

## Primo video lungo (da fare)
Sulla ricerca **"senior discounts"**, partendo dall'idea del primo short: "Most senior discounts start at 55, not 65, and nobody tells you". Oltre 10 minuti, 1920×1080, stesso stile verde/avorio.
Struttura proposta:
1. Gancio: sconti da 55 anni, non da 65. Promessa + il numero che sorprende.
2. Perché nessuno te lo dice (non è scritto all'ingresso, la cassa non lo offre).
3. La domanda esatta da fare alla cassa.
4. Per categorie, con età e cifre verificate: supermercati e farmacie, ristoranti, telefonia, cinema, viaggi, National Parks Senior Pass, auto e negozi, tessere.
5. Come non farsi imbrogliare (condizioni, "varia per sede").
6. Checklist finale e rimando al video successivo.
Tutti i dati vanno **verificati su più fonti ufficiali** prima del copione.

## Stato al 01/10/2026 (dalla pagina del canale)
- 1,71K iscritti, 3 video (3 short). Views: short 1 "Start at 55 / Not 65" 67; short 2 "4 places" 38; short 3 "Hot meals at your door" 20. Tutte le views degli short arrivano da ricerca YouTube; feed Shorts a zero.
- Short 3 finale: 720x1278 (export CapCut), 33 s, in `riferimenti/short3-finale.mp4`. Pagina del canale e copertina in `riferimenti/`.
- Le chat esportate arrivano fino al 29/09: lo short 4 (bollette) non risulta fatto.
- File export di oggi: memoria completa del canale in `MEMORIA-CANALE.md`.

## Disclaimer e monetizzazione (deciso il 01/10/2026)
- Il disclaimer **non protegge** da YouTube: la monetizzazione dipende da contenuto originale e utile, da dati corretti e da niente promesse esagerate. Resta una buona pratica e si usa **in 4 punti**:
  1. Descrizione (già nel testo predefinito).
  2. Commento fissato.
  3. Scritto in piccolo in ogni slide dei luoghi: "Varies by location · confirm with the business".
  4. Slide finale con il disclaimer in chiaro (`anteprima/3-finale-disclaimer.png`) + una frase detta a voce nel blocco finale.
- Non metterlo all'inizio del video (fa perdere spettatori).
- Rischi da evitare: contenuto "a modello" identico tra i video (regola "inauthentic content": slideshow/modelli senza valore aggiunto), persone/avatar AI che si presentano come esperti, promesse di guadagno. Quindi: ogni video con dati verificati, fonti scritte, struttura e oggetti diversi per argomento.
- Anteprime del video lungo 1 in `anteprima/` (codice: `code/long1_anteprima.py`).
