# Fonti e verifiche - video lungo 16 (rivalutazione pensioni 2027, ddl di bilancio art. 55) - 05/11/2026
Regola N.31: ogni cifra e regola trovata su fonte ufficiale PRIMA del copione.

## Testo del disegno di legge (letto per intero l'articolo)
- Camera dei Deputati, A.C. 3174, "Bilancio di previsione dello Stato per l'anno finanziario 2027 e bilancio pluriennale per il triennio 2027-2029", presentato il 30/10/2026 dal Ministro dell'economia e delle finanze (Giorgetti). PDF tomo II: https://documenti.camera.it/leg19/pdl/pdf/leg.19.pdl.camera.3174.19PDL0221150.pdf. Estratto in fonti-ufficiali/ddl-AC3174-art53-56-testo-estratto.txt.
- Art. 55 (rubrica: "Modifiche alla disciplina in materia di rivalutazione automatica dei trattamenti pensionistici"): per l'anno 2027, rivalutazione secondo il meccanismo dell'art. 34 c.1 L. 448/1998 riconosciuta: a) 100% per i trattamenti complessivamente pari o inferiori a 4 volte il trattamento minimo INPS; b) per i trattamenti complessivamente superiori a 4 volte, "con riferimento all'importo complessivo dei trattamenti medesimi": 1) 85% fino a 5 volte; 2) 53% oltre 5 e fino a 6; 3) 47% oltre 6 e fino a 8; 4) 37% oltre 8 e fino a 10; 5) 32% oltre 10. Per ogni scalino vale il "limite maggiorato": per le pensioni sopra la soglia e sotto "tale limite incrementato della quota di rivalutazione automatica spettante" l'aumento e' comunque attribuito fino a concorrenza del limite maggiorato.
- NON E' LEGGE: ddl alla Camera (presentato il 30/10/2026), puo' cambiare. L'indice 2027 non e' nel testo.

## Metodo di quest'anno (fasce) e riferimento del minimo
- Camera dei deputati, temi.camera.it "Politiche previdenziali" (https://temi.camera.it/leg19/temi/politiche-previdenziali-1.html): dal 2025 torna la disciplina generale (L. 160/2019 art. 1 c. 478): 100% della variazione dell'indice "per la fascia di importo complessivo dei trattamenti pensionistici del soggetto fino a 4 volte" il minimo; 90% "per la fascia ... compresa tra 4 e 5 volte"; 75% "per la fascia ... superiore a 5 volte" = percentuali per fascia (pezzi di pensione). Per il biennio 2023-2024 (L. 197/2022 c. 309; L. 213/2023 c. 135): 100/85/53/47/37/32% "per i trattamenti ... complessivamente superiori" (importo complessivo); nel 2024 l'ultimo scalino al 22%. Stessa pagina: "(in via interpretativa) ... l'importo del trattamento minimo INPS nell'anno precedente a quello di applicazione della perequazione" (Circ. INPS 1/2024). Il testo dell'art. 55 ha le stesse percentuali del 2023.
- Inps circolare 153 del 19/12/2025 (testo + allegato 2, letti): minimo 2026 = 611,85 (da V3); tabella 2026: fino a 4 volte il TM 100% (1,400%) fino a 2.413,60; 90% (1,260%) fino a 3.017,00; oltre 75% (1,050%); le soglie 2026 usano il minimo 2025 (603,40). La rivalutazione e' attribuita "sulla base dell'importo del cosiddetto cumulo perequativo di dicembre dell'anno precedente, considerando come un unico trattamento tutte le pensioni di cui il soggetto e' titolare" (con esclusioni: prestazioni assistenziali, ecc.).
- Soglie 2027 (se l'Imps usa il minimo dell'anno prima = 611,85): 4x = 2.447,40; 5x = 3.059,25; 6x = 3.671,10; 8x = 4.894,80; 10x = 6.118,50. Il ddl non scrive i valori in euro: nel copione detto "se anche stavolta fa cosi".
- Indice 2027: decreto MEF-Lavoro atteso a novembre (prassi: 19/11/2025). Al 05/11/2026 non risulta pubblicato (nessuna notizia di decreto). Nel copione: ipotesi nostra del 3%.

## Conti (script /tmp/claude-0/gen/calc2.py, salvato in conti/conti-rivalutazione-2027.py)
Indice 3%, minimo 611,85. "Oggi" = metodo per fasce (100% fino a 4x, 90% tra 4x e 5x, 75% oltre), "testo" = art. 55 con limite maggiorato. Importi mensili lordi; annuo = differenza x 13.
- 7.000: oggi 178,61 / testo 67,20 / differenza 111,41 / 1.448,31 l'anno (scalino > 10x)
- 5.100: 135,86 / 56,61 / 79,25 / 1.030,23 (8x-10x)
- 3.800: 106,61 / 53,58 / 53,03 / 689,37 (6x-8x)
- 3.300: 95,36 / 52,47 / 42,89 / 557,55 (5x-6x)
- 2.700: 80,24 / 68,85 / 11,39 / 148,10 (4x-5x)
- 2.450 (appena sopra la soglia): oggi 73,49; testo con limite maggiorato 70,82 (la pensione arriva a 2.520,82 = 2.447,40 x 1,03); differenza 2,67 al mese
- 1.500: +45 (585 l'anno); 2.000: +60 (780 l'anno) = identico oggi/testo.
Nel copione tutti gli importi sono arrotondati all'euro ("circa") e detti "lordi e arrotondati".

## Punti NON detti (non verificati o non ufficiali)
- 3,5 milioni di pensionati / "fino a 1.300 euro" (stampa, Il Messaggero 05/11): non usati.
- Sentenze Corte costituzionale 19/2025 e 167/2025 sul sistema a blocchi (da ricerca web, non letto il testo): non usate.
