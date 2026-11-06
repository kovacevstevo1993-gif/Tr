# STATO PAGINA FACEBOOK "Conti in Pensione" (02/11/2026) - per la chat nuova

Ramo con tutto il lavoro: claude/loving-faraday-bfoxin (NON ancora unito a main). Leggere anche REGOLE-FISSE.md (in fondo: errori e regole del 27/10-01/11).
Canale YouTube: https://www.youtube.com/@ContiInPensione . Non esiste un sito: solo il canale e la pagina Facebook. I post li pubblica l'utente.

## ID dei video su YouTube (letti da curl/oembed il 27-31/10)
- Video lungo 1 "Pensione anticipata 2027: requisiti, regole e proposte" (in origine "Pensione a 64 anni"): biWx9vHQ4CA
- Video lungo 2 "Pensione: l'eta' giusta, il guadagno e i contributi fanno la differenza" (11:47): XxlBn1_HXvc
- Video lungo 3 "Pensioni 2027: quanto ci guadagni davvero? Esempi da 1.000 a 4.000 euro" (12:55): bQhQomfdstA
- Short 1 "Come verificare il cedolino della pensione in 30 secondi": 1tZ26acMHgU
- Short 2 "Pensione 2027: le scadenze che devi conoscere subito" (0:50): uJcX8JVR28E
- Short 5 "Pensioni 2027: la verita' sul 3%": FhgrsxmTe74
- Video 4: pacchetto FB fatto (03/11): 14-video-lungo-4-invalidita-2027/facebook (pacchetto-fb.txt + miniatura-fb-video4.png). Titolo YouTube attuale: "Accompagnamento vs assegno mensile: chi perde davvero nel 2027?"
- Video 5: pacchetto FB fatto (03/11): 16-video-lungo-5/facebook (pacchetto-fb.txt + miniatura-fb-video5.png).
- Short tredicesima detassata (short 7, hVGOrlvFG8U): pacchetto FB fatto (03/11): 17-short-7-teaser-video-lungo-5/facebook (pacchetto-fb.txt + copertina-reel.png).
- Video 6 (tpGncD3fN44, pensioni novembre): pacchetto FB fatto (03/11): 18-video-lungo-6/facebook (pacchetto-fb.txt + miniatura-fb-video6.png).
- Short novembre -480 (iiqWHNmrMSk): pacchetto FB fatto (03/11): 19-short-8-teaser-video-lungo-6/facebook (pacchetto-fb.txt + copertina-reel.png).
- Video 7 (GBMYERVdbMY, cosa succedera ai tuoi assegni): pacchetto FB fatto (04/11): 20-video-lungo-7/facebook (pacchetto-fb.txt + miniatura-fb-video7.png).
- Short rivalutazione tagliata (R6e_pZ_aRFE): pacchetto FB fatto (06/11): 21-short-9-teaser-video-lungo-7/facebook (pacchetto-fb.txt + copertina-reel.png).
- Short cedolino dove spariscono i soldi (thWP1pSh1lY, iscrizione): pacchetto FB fatto (06/11): 22-short-10-iscrizione/facebook (pacchetto-fb.txt + copertina-reel.png). Per Facebook: "Seguici", niente "mille iscritti" (pagina 8.5K follower).
- Short 6 "Stop: prima di contare l'aumento, guarda questo" (teaser invalidita', 1:05): pSVNnae7ORU; video lungo 4 invalidita' 2027: T1JdRgHYmUg. Pacchetto FB fatto (copertina in 15-short-6-teaser-video-lungo-4/facebook).
- Altri video sul canale (non ancora fatti per Facebook): -WzZ_fQi_vk (casalinghe vs assegno sociale), 1XkoYu1SQpM (pensionati all'estero), 9jsMe2Bk8uM (dicembre tredicesima e bonus 154,94), GyQh_nMvKTo (aumento pensioni 2027 tabella netti), T1JdRgHYmUg (invalidita 2027), aMi8UjEO378 (tredicesima detassata netto), tpGncD3fN44 (pensioni a novembre), e gli altri short della lista /shorts.

## COSA E' FATTO PER FACEBOOK (file nelle cartelle dei video, sottocartella facebook/)
- Video 1: miniatura orizzontale 1920x1080 miniatura-fb-orizzontale-v2.png (la v1 era uguale a quella YouTube: errore); copertina verticale copertina-fb-verticale.png (per Reel). Testo post consegnato in chat.
- Short 1: copertina Reel 02-short-1-cedolino-ottobre/facebook/copertina-reel.png (1080x1920, contenuto dentro la zona sicura). Descrizione in chat.
- Short 2: 05-short-2-requisiti-2027/facebook/copertina-reel.png. Descrizione in chat.
- Video 2: miniatura orizzontale 09-video-lungo-2-calcolo-pensione/facebook/miniatura-fb-video2.png (importi coperti da "?").
- Short 5 (3%): 13-short-5-teaser-video-lungo-3/facebook/copertina-reel.png (+120 barrato, risultato coperto da "?", fasce 100/90/75).
- Video 3: miniatura orizzontale 12-video-lungo-3-rivalutazione-2027/facebook/miniatura-fb-video3.png.
- Generatori: gen_fb*.py / gen_reel.py + shot_*.js (SVG -> PNG con playwright node, python playwright NON installato). Testi misurati con getBBox e immagine guardata.

## REGOLE FACEBOOK DELL'UTENTE (tutte anche in REGOLE-FISSE.md)
1. Nel testo del post i LINK stanno quasi all'inizio (nessuno arriva in fondo): link del video + link del canale. I link su Facebook sono cliccabili (parole dell'utente).
2. Primo commento SEMPRE con il link del canale https://www.youtube.com/@ContiInPensione (e del video), piu' una domanda ai commenti CON UN MOTIVO ("scrivi quanto prendi: ti rifaccio il conto").
3. Video lungo caricato su Facebook = stesso video: scrivere "Guardalo anche su YouTube: <link>", MAI "il video completo (N minuti)". "Il video completo" solo negli short (rimandano a un video lungo diverso).
4. Descrizione SENZA spoiler: niente cifre-risposta, tabelle o meccanismo; solo domanda e curiosita'. Fonti, disclaimer ("Canale non affiliato..."), 5 hashtag restano.
5. Miniatura/copertina: impianto NUOVO (non lo stesso della miniatura YouTube con dettagli cambiati), professionale, risposta nascosta da "?", testi misurati, nessun testo tagliato; Reel 1080x1920 con contenuto tra y 250 e y 1670; video orizzontale 1920x1080.
6. Rispondere SOLO a quello che chiede: una critica/domanda = risposta breve, mai rifare o mandare altro non ordinato (errore 01/11: 3 descrizioni mandate).
7. Dati dei video gia' pubblicati: sono gia' verificati nei file (fonti-e-verifiche.md, ricerca-e-fonti.md, pacchetto.txt): NON ricontrollare su internet, non togliere dati verificati (4,2% Istat NIC settembre e' verificato).
8. L'hook Stop blocco-revisione.py (controllo revisione copioni) resta attivo, con DAL='2026-10-27T23:30:00Z' per non segnalare i vecchi copioni. Non toglierlo senza ordine.

## TESTI FINALI DA USARE (ultime versioni consegnate)
### Video 3 - descrizione (senza spoiler)
Pensioni 2027: il 3% NON e' il 3%! 😱 Quanto aumenta DAVVERO la tua pensione a gennaio? Il conto che nessuno ti fa vedere.
(righe link: "▶️ Guardalo anche su YouTube: https://www.youtube.com/watch?v=bQhQomfdstA" e "📺 Tutti i video del canale: https://www.youtube.com/@ContiInPensione"; poi: esempi da 1.000 a 4.000 euro lordi, calcolo passo passo, 3 trappole (percentuale dei titoli, un'altra gia' a gennaio sul cedolino); percentuale ufficiale 2027 con decreto a novembre, cifre = esempi al 3%; domanda commenti con motivo; Iscriviti; Fonti Inps circolare 153 del 19/12/2025, DI 19/11/2025, Istat; disclaimer; #pensioni2027 #rivalutazionepensioni #aumentopensioni #inps #pensionati)
### Video 3 - primo commento
Tutti i video sul canale YouTube 👉 https://www.youtube.com/@ContiInPensione / Guardalo anche su YouTube 👉 https://www.youtube.com/watch?v=bQhQomfdstA / Scrivi qui sotto quanto prendi di pensione lorda, piu' o meno: ti rifaccio il conto con il 3% e ti dico quanto ti arriva davvero 👇
### Video 2 - descrizione corretta (gancio senza cifra)
"Stesso stipendio, stessi contributi: uscire a 64 anni invece che a 67 quanto ti costa ogni mese? 👀 Il conto vero, passo passo." + link (Guardalo anche su YouTube XxlBn1_HXvc + canale) + i 3 numeri (eta', quanto guadagni, anni coperti da contributi) + esempio semplificato (stipendio costante, 40 anni, lordi) + commenti "a che eta' pensi di andare in pensione: 64, 65, 66 o 67?" (aggiungere il MOTIVO) + Iscriviti + disclaimer + #pensione #calcolopensione #inps #pensionati #myinps. Il 185 euro NON va scritto.
### Short 5 (3%) - descrizione corretta
"Pensione da 4.000 euro lordi, aumento del 3%: fai il conto. Quanto arriva davvero? 😱 Non e' quello che pensi, e il motivo non lo dice quasi nessuno." + link "Il video completo con il calcolo passo passo" (bQhQomfdstA) + canale + "C'entra la legge e un dettaglio sull'inflazione che quasi tutti confondono." + 3% = esempio, percentuale ufficiale a novembre + commenti + Iscriviti + fonti + disclaimer + 5 hashtag. Il 111/120 NON va scritto.
### Primo commento Reel/short
Tutti i video sul canale YouTube 👉 canale / Questo short su YouTube 👉 https://www.youtube.com/shorts/<id> / domanda con motivo.

## DA RIFARE (solo su ordine dell'utente)
- Descrizione video 1 (testo post FB del 27/10: ha "Il video completo", da cambiare in "Guardalo anche su YouTube"; controllare che non spoileri) e miniatura gia' consegnata.
- Descrizione short 1 e short 2 consegnate PRIMA delle regole 3-4: short 2 spoilera "67 anni e 1 mese", short 1 va bene ma controllare; commento con motivo.
- Pacchetti Facebook per gli altri video lunghi e short (lista ID sopra), sempre con le regole 1-8.
- Pagina Facebook: categoria "Creatore di contenuti digitali", biografia, foto profilo e copertina in 01-identita-canale/facebook/.

## COME LEGGERE LA PAGINA FACEBOOK (03/11/2026) - FUNZIONA
- Pagina: "Conti In Pensione A Pillole" https://www.facebook.com/people/Conti-In-Pensione-A-Pillole/61572856361386/ (share link: https://www.facebook.com/share/1JMmMPf8Mx/). 8515 follower.
- curl e WebFetch NON funzionano (login). FUNZIONA playwright chromium (node, NODE_PATH=$(npm root -g)) con locale it-IT e user agent desktop: aprire `<pagina>?sk=reels_tab`, scorrere, raccogliere i link a[href*="/reel/"], aprire ogni reel e leggere il testo (descrizione). Script: scratchpad fb3.js (copia in conti_in_pensione/facebook-lettura/fb3.js).
- PUBBLICATI su Facebook al 03/11 (8 reel): short invalidita' (2/11), video 3 ("il 3% NON e' il 3%"), short 5 (3%), video 2 (descrizione vecchia con "185 euro": da rifare), short 2 scadenze ("sale l'eta'! Tu ci rientri?", da rifare), short 1 cedolino, video 1 ("Pensione a 64 anni nel 2027: esiste davvero...", descrizione vecchia "Il video completo": da rifare), "Due colleghi... 64 e 67 anni" (probabilmente short 4, teaser video 2).
- MANCANO (ordine YouTube): short 3 "Non andare in pensione prima di aver visto questo", video 4, video 5, short tredicesima detassata, video 6, short novembre -480, video 7, short rivalutazione tagliata, short cedolino dove spariscono, video 8, short estero, video 9, short dicembre, video 10, short casalinghe, video 11, short aumento 1.000 lordi, video 12, short rientri nel taglio, video 13, video 14, short manovra, short reversibilita'.
