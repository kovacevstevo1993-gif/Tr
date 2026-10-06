# Regole permanenti (valgono sempre, in ogni sessione)

**Questo repo ha un hook SessionStart (.claude/settings.json) che carica automaticamente senior_advantage/PASSAGGIO-CHAT.md a ogni nuova chat: tenerlo SEMPRE aggiornato e completo.**

**PRIMA REGOLA: SALVARE TUTTO (04/10/2026): ogni cosa fatta o decisa (copioni, pacchetti, durate, regole, stato dei video) va salvata SUBITO in senior_advantage/PASSAGGIO-CHAT.md o in CLAUDE.md, con commit e push, senza che l'utente lo chieda. Prima di scrivere qualsiasi cosa, leggere CLAUDE.md, PASSAGGIO-CHAT.md e i file modello: l'utente non deve ripetere niente.**

**"TUTTO" = VERAMENTE TUTTO (04/10/2026): quando l'utente dice "tutto" (salvare, passare alla chat nuova, leggere le altre chat) significa ogni singola riga, intera, senza riassumere, senza filtrare per argomento, senza tagliare. Esempio: passaggio chat = file di stato + testo INTERO di tutte le chat del progetto in senior_advantage/chat/ (esportate con list_sessions/list_events). Mai a meta'.**

Due canali YouTube dell'utente, **separati**. Non mescolare mai temi, stile o dati.
- `senior_advantage/` — **The Senior Advantage** (@TheSeniorAdvantage): sconti, benefici e aiuti per over 60 USA. Slide verde bosco e avorio. Short verticali 1080x1920, video lunghi 1920x1080.
- `money_backstory/` — **The Money Backstory** (@TheMoneyBackstoryUSA): pensione USA over 50 (Social Security, Medicare, tasse). Slide blu navy e oro con cornice 3D.

## Disclaimer (deciso il 01/10/2026) — vale per TUTTI i video lunghi di ENTRAMBI i canali, NON per gli short
- Il disclaimer va **alla fine del video**, in una **slide finale** in chiaro (testo grande), con la frase detta a voce nell'ultimo blocco. Modello: `senior_advantage/anteprima/3-finale-disclaimer.png` (nel canale Money Backstory stessa struttura, ma con colori e stile di quel canale).
- Testo (adattare al tema): "Rules, amounts and ages change and differ by location and plan. Always confirm with the official source before you rely on them. General information, not financial advice."
- Non metterlo all'inizio. Negli short non serve.
- In più, sempre: descrizione (riga Subscribe + Disclaimer) e commento fissato.
- Il disclaimer non protegge da YouTube: contano contenuto originale, dati verificati su fonti ufficiali, niente promesse di guadagno, niente persone/avatar AI che si presentano come esperti.

## Come lavora l'utente
- REGOLA ASSOLUTA (03/10/2026): rispondere SOLO a quello che chiede, il minimo. Niente spiegazioni, riepiloghi, tabelle, note, offerte o domande non richieste. Ogni parola in più spreca crediti e chat (non sono illimitati). Se chiede il pacchetto (titolo, descrizione, tag), dare solo quello.
- REGOLA ASSOLUTA (03/10/2026): i blocchi di voce / copioni vanno SEMPRE scritti direttamente in chat, numerati, uno per blocco, pronti da copiare in CapCut. MAI in un file, MAI con SendUserFile. Solo gli MP4 si mandano come file.
- Eccezione: passaggio chat e riepiloghi lunghi richiesti: file con SendUserFile, non in chat. I copioni e i blocchi di voce restano SEMPRE in chat.
- Gancio (04/10/2026): ogni video ha un gancio DIVERSO. Mai ripetere la stessa apertura (es. "Wait." l'hanno già short 5 e 6: non riusarla). Variare formula e primo suono.
- Sigle per la voce (vale per TUTTI i video lunghi e gli short): SNAP = "snap" (parola, minuscolo). CSFP, USDA, LIHEAP ecc. a lettere separate: "C S F P", "U S D A". Siti: "f n s dot u s d a dot gov".
- Slide (04/10/2026): dal prossimo video, montaggio PIÙ DETTAGLIATO (non più tagliato) e slide che si capiscono meglio. Ogni slide deve FINIRE dentro la sua frase/blocco: tutto ciò che compare deve essere completo e ben visibile prima che la voce passi al blocco dopo; niente elementi tagliati, coperti o ancora in animazione a fine blocco.
- PACCHETTO (formato FISSO, identico per ogni video e per ogni chat, mai cambiarlo): scrivere TUTTO in chat, ogni campo in un suo BLOCCO DI CODICE (```) da copiare con un tocco, con etichetta in grassetto sopra, in quest'ordine: **Dove va** (playlist, cosa creare/cancellare: di solito niente), **Titolo**, **Descrizione**, **Tag**, **Commento da fissare**, **Impostazioni** (IA No, promozione No, miniatura, schermata finale 20 s per i lunghi; per gli SHORT anche "Video correlato" = il video lungo del tema. Il video correlato si imposta SOLO sullo short, mai nelle impostazioni del video lungo). Contenuto sul modello di senior_advantage/MODELLO-DESCRIZIONE-VIDEO-1.md (LEGGERLO SEMPRE prima): descrizione con gancio, paragrafo "The one rule...", CHAPTERS (orari dalla timeline dell'utente, arrotondati per difetto), "Sources: official pages of ..." senza link lunghi, Subscribe, Disclaimer, 3 hashtag. Tag con virgole senza spazi. Niente note, niente spiegazioni. Mai usare i titoli ### in chat. NIENTE LINK/URL interi nella descrizione (ne' di fonti ne' di siti): solo il nome del sito (es. "fns.usda.gov") nella riga Sources; l'unico link ammesso e' quello Subscribe. Vale anche per gli SHORT.
- DISCLAIMER NELLA DESCRIZIONE (04/10/2026): SEMPRE presente e ben visibile, con l'etichetta "Disclaimer:", in TUTTE le descrizioni (lunghi E short): "Disclaimer: Rules, amounts and ages change and differ by location and plan. Always confirm with the official source before you rely on them. General information, not financial advice. This channel is not affiliated with [ente/aziende citati]." Nel video lungo anche slide finale e voce; nello short solo descrizione.
- MODELLI: pacchetto video lungo = senior_advantage/MODELLO-DESCRIZIONE-VIDEO-1.md (tag senza spazi); pacchetto SHORT = senior_advantage/MODELLO-PACCHETTO-SHORT.md (tag con ", "). Leggerli SEMPRE prima.
- CONTROLLARE PRIMA, SEMPRE (04/10/2026): prima di produrre QUALSIASI cosa (pacchetto, descrizione, copione, slide, miniatura) guardare COME sono stati fatti i precedenti dello stesso tipo: file modello in senior_advantage/ (MODELLO-*), PASSAGGIO-CHAT.md e, se non bastano, le altre chat (tool list_sessions/list_events). Poi farlo IDENTICO. Quando manca un modello nel repo, recuperarlo dalle chat e SALVARLO subito in un file MODELLO-*.md con commit e push. Mai inventare un formato nuovo.
- Risposte corte, niente scuse né "hai ragione". Una cosa alla volta. Verificare prima di dare un'indicazione.
- RICERCHE vidIQ (06/10/2026): TUTTE le ricerche vidIQ e i dati analytics gia fatti sono in senior_advantage/RICERCHE-VIDIQ.md. LEGGERLO PRIMA di spendere crediti: non rifare mai una ricerca gia salvata. Ogni nuova ricerca va aggiunta subito a quel file (commit + push). Le informazioni pubbliche di YouTube (view, titoli, descrizioni, capitoli, concorrenti) si leggono gratis con curl, senza crediti.
- Mai spendere crediti vidIQ senza dirlo e chiedere prima (eccetto quando l'utente lo autorizza esplicitamente nel messaggio).
- Slide e grafica le fa Claude con il codice (gratis). Titolo, descrizione e tag già completi da incollare, Subscribe e disclaimer compresi.
- Dire PRIMA dove va ogni nuovo video (playlist, cosa creare o cancellare su YouTube).
- Gli orari dei capitoli si prendono dalla timeline dell'utente, non si stimano dal testo.
- Non rifare quello che ha già montato. Non proporgli mai di fermarsi.
- Le miniature devono avere la frase che ha in mente lui; stile rosso/verde dei suoi video 1 e 2 (Money Backstory), font Montserrat ExtraBold.

## Stile slide (feedback utente 01/10/2026, dopo il primo video lungo di Senior Advantage)
- Il primo video va bene ma è "sciatto e basico". Dai prossimi video: slide più movimentate, più dettagliate, più oggetti disegnati in ogni didascalia (più guardabili, anche se il pubblico è anziano).
- Durate dei blocchi: partire SEMPRE dalla fine del blocco precedente letta nello screenshot dell'utente, mai dalla somma dei miei clip.
