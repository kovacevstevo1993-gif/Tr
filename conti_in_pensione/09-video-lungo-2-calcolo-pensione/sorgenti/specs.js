const BLK={};
const A=(o,at)=>{o.at=at;return o;};
BLK[21]={scenes:[
 {w:.28,lab:'IL MOMENTO CHE ASPETTAVI',cap:"GUARDA COME CAMBIA IL COEFFICIENTE CON L'ETÀ",items:[C('COEFFICIENTE','?','CAMBIA CON L\'ETÀ','g',480),Q()],tags:[T_('ORA IL MOMENTO CHE ASPETTAVI','a')]},
 {w:.72,lab:'COEFFICIENTE PER ETÀ',cap:'64, 65 E 66 ANNI: COSÌ CAMBIA IL COEFFICIENTE',items:[A(C('64 ANNI','5,088%','COEFFICIENTE','p',420),0),A(C('65 ANNI','5,250%','COEFFICIENTE','p',420),.4),A(C('66 ANNI','5,423%','COEFFICIENTE','p',420),.8)],tags:[T_('PIÙ ASPETTI, PIÙ SALE','g')]}]};
BLK[22]={scenes:[
 {w:.4,lab:'A 67 ANNI',cap:'A 67 ANNI: 5,608%!',items:[C('67 ANNI','5,608%','COEFFICIENTE','g',480)],tags:[T_('HAI VISTO?','a')]},
 {w:.6,lab:'COME UNA SCALA',cap:'PIÙ SALI, PIÙ LA PENSIONE CRESCE',items:[BA(8,[[0,8,'g']])],tags:[T_('OGNI ANNO CHE ASPETTI, SALE','g'),T_('E NESSUNO TE LO DICE','r')]}]};
BLK[23]={scenes:[
 {w:1,lab:'TRADOTTO IN EURO',cap:'LA PENSIONE DI BRUNO, ETÀ PER ETÀ',items:[A(C('64 ANNI','1.808 €','LORDI AL MESE','p',400),.05),A(C('65 ANNI','1.866 €','LORDI AL MESE','p',400),.33),A(C('66 ANNI','1.927 €','LORDI AL MESE','p',400),.58),A(C('67 ANNI','1.993 €','LORDI AL MESE','g',400),.82)],tags:[T_('SEMPRE PER BRUNO','a')]}]};
BLK[24]={scenes:[
 {w:.5,lab:'UN ANNO IN PIÙ',cap:'OGNI ANNO IN PIÙ VALE CIRCA 60 € AL MESE',items:[C('OGNI ANNO IN PIÙ','+ 60 €','LORDI AL MESE','g',480)],tags:[T_('PER TUTTA LA VITA DA PENSIONATO','g')]},
 {w:.5,lab:'UNA SORPRESA',cap:"IL CONTO TOTALE LO FACCIO ALLA FINE!",items:[C('DA 64 A 67 ANNI','? €','DIFFERENZA TOTALE','d',480),Q()],tags:[T_("C'È UNA SORPRESA!",'a')]}]};
BLK[25]={scenes:[
 {w:.5,lab:'EFFETTO NUMERO UNO',cap:'UN ANNO IN PIÙ AGGIUNGE CONTRIBUTI AL SALVADANAIO',items:[PG(),OP('+'),C('UN ANNO IN PIÙ','+ 11.550 €','NEL SALVADANAIO','g',460)],tags:[T_('PIÙ CONTRIBUTI','g')]},
 {w:.5,lab:'EFFETTO NUMERO DUE',cap:'E ALZA IL COEFFICIENTE: DUE EFFETTI INSIEME',items:[C('COEFFICIENTE','▲','PIÙ ALTO','a',380),OP('+'),C('CONTRIBUTI','▲','PIÙ ALTI','g',380)],tags:[T_('DUE EFFETTI NELLO STESSO MOMENTO','a')]}]};
BLK[26]={scenes:[
 {w:.6,lab:'UN ANNO IN PIÙ, QUANTO VALE?',cap:'BRUNO A 66 ANNI E A 67 ANNI',items:[A(C('66 ANNI · 39 ANNI CONTR.','1.879 €','LORDI AL MESE','p',500),0),A(AR(),.4),A(C('67 ANNI · 40 ANNI CONTR.','1.993 €','LORDI AL MESE','g',500),.7)],tags:[]},
 {w:.4,lab:'LA DIFFERENZA',cap:'UN SOLO ANNO IN PIÙ VALE CIRCA 114 € AL MESE',items:[C('UN SOLO ANNO IN PIÙ','+ 114 €','AL MESE, LORDI','g',520)],tags:[T_('PER TUTTA LA VITA','g')]}]};
BLK[27]={scenes:[
 {w:.45,lab:'ATTENZIONE',cap:'NELLA REALTÀ, CHI ESCE PRIMA HA MENO CONTRIBUTI',items:[W_()],tags:[T_('CHI ESCE PRIMA','r'),T_('HA MENO CONTRIBUTI','a')]},
 {w:.55,lab:'NEL NOSTRO ESEMPIO',cap:"IL SALVADANAIO RESTA UGUALE: CAMBIA SOLO L'ETÀ",items:[PG(),OP('='),C('SALVADANAIO','UGUALE','SOLO L\'ETÀ CAMBIA','g',480)],tags:[T_("SI VEDE SOLO L'EFFETTO DELL'ETÀ",'a')]}]};
BLK[28]={scenes:[
 {w:.5,lab:'NUMERO UNO',cap:"IL NUMERO UNO: L'ETÀ IN CUI ESCI",items:[C('NUMERO UNO',"L'ETÀ",'IN CUI ESCI','g',460),K()],tags:[T_('DECIDE LA TUA PENSIONE','a')]},
 {w:.5,lab:'PRIMA, IL NUMERO DUE',cap:'IL NUMERO TRE COSTA DI PIÙ... CI ARRIVIAMO!',items:[C('NUMERO TRE','?','COSTA DI PIÙ','r',420),AR(),C('PRIMA','NUMERO DUE','','d',420)],tags:[T_('QUASI NESSUNO CI PENSA','r')]}]};
BLK[29]={scenes:[
 {w:.25,lab:'NUMERO DUE',cap:'NUMERO DUE: QUANTO GUADAGNI',items:[C('NUMERO DUE','QUANTO|GUADAGNI','','g',520)],tags:[]},
 {w:.3,lab:'TRE PERSONE',cap:"STESSO PERCORSO: 40 ANNI DI CONTRIBUTI, USCITA A 67",items:[PE(true),PE(false),PE(true)],tags:[T_('ANNA · BRUNO · CARLA','a'),T_('40 ANNI DI CONTRIBUTI','g')]},
 {w:.45,lab:'LO STIPENDIO',cap:'ANNA, BRUNO E CARLA GUADAGNANO...',items:[A(C('ANNA','25.000 €','LORDI L\'ANNO','p',420),.05),A(C('BRUNO','35.000 €','LORDI L\'ANNO','p',420),.4),A(C('CARLA','50.000 €','LORDI L\'ANNO','p',420),.75)],tags:[]}]};
BLK[30]={scenes:[
 {w:1,lab:'RISULTATI',cap:'PIÙ GUADAGNI, PIÙ IL SALVADANAIO SI RIEMPIE!',items:[A(C('ANNA','1.424 €','AL MESE, LORDI','p',420),.02),A(C('BRUNO','1.993 €','AL MESE, LORDI','p',420),.3),A(C('CARLA','2.847 €','AL MESE, LORDI','g',420),.58)],tags:[T_('NEL NOSTRO ESEMPIO','a',null,40),T_('PIÙ GUADAGNI, PIÙ SI RIEMPIE','g',null,40)]}]};
BLK[31]={scenes:[
 {w:.5,lab:'HAI NOTATO?',cap:'IN TUTTI E TRE I CASI: CIRCA IL 74% DELLO STIPENDIO',items:[C('ANNA','74%','DELLO STIPENDIO','g',400),C('BRUNO','74%','DELLO STIPENDIO','g',400),C('CARLA','74%','DELLO STIPENDIO','g',400)],tags:[]},
 {w:.5,lab:'ATTENZIONE',cap:'IL CASO PERFETTO: LA VITA VERA NON È COSÌ',items:[W_(),C('CASO PERFETTO','STIPENDIO UGUALE|NESSUN BUCO','','d',560)],tags:[T_('LA VITA VERA NON È COSÌ','r')]}]};
BLK[32]={scenes:[
 {w:.5,lab:'E SE LAVORI PART-TIME?',cap:"LO STIPENDIO È PIÙ BASSO: NEL SALVADANAIO ENTRA MENO",items:[Q(),C('PART-TIME','STIPENDIO|PIÙ BASSO','','a',460)],tags:[T_('NEL SALVADANAIO ENTRA MENO','r')]},
 {w:.5,lab:'ANNO PER ANNO',cap:'CONTA QUANTO È STATO VERSATO DAVVERO, ANNO PER ANNO',items:[DN(0.33),OP('×'),C('CIFRA PIÙ PICCOLA','?','','p',380)],tags:[T_('SEMPRE IL 33%','g'),T_('GUARDA QUANTO È STATO VERSATO','a')]}]};
BLK[33]={scenes:[
 {w:.5,lab:'NUMERO TRE',cap:'NUMERO TRE, IL PIÙ PERICOLOSO: GLI ANNI SENZA CONTRIBUTI',items:[C('NUMERO TRE','I BUCHI','ANNI SENZA CONTRIBUTI','r',500),W_()],tags:[T_('IL PIÙ PERICOLOSO','r')]},
 {w:.5,lab:'COSA SORPRENDE',cap:'UN BUCO NON SI VEDE SULLO STIPENDIO... SI VEDE DOPO',items:[C('SULLO STIPENDIO','NON|SI VEDE','','d',420),AR(),C('SULLA PENSIONE','SI|VEDE','','r',420)],tags:[T_('SI VEDE SOLO DOPO','a')]}]};
BLK[34]={scenes:[
 {w:.33,lab:'TORNIAMO A BRUNO',cap:'UN SOLO ANNO SENZA CONTRIBUTI',items:[PE(false),C('UN ANNO SENZA','0 €','CONTRIBUTI','r',420)],tags:[]},
 {w:.33,lab:'NEL SALVADANAIO',cap:'NON AGGIUNGE 11.550 € AL SALVADANAIO',items:[PG(),OP('−'),C('MANCANO','11.550 €','','r',440)],tags:[]},
 {w:.34,lab:'A 67 ANNI',cap:'CIRCA 50 € LORDI IN MENO, OGNI MESE!',items:[C('PENSIONE A 67 ANNI','− 50 €','AL MESE, LORDI','r',520)],tags:[T_('PER UN SOLO ANNO DI BUCO','a')]}]};
BLK[35]={scenes:[
 {w:.65,lab:'50 € SEMBRANO POCHI?',cap:"50 € AL MESE, PER 13 MENSILITÀ: 650 € L'ANNO",items:[A(C('AL MESE','50 €','','p',300),0),A(OP('×'),.2),A(C('MENSILITÀ','13','','p',300),.4),A(OP('='),.6),A(C("ALL'ANNO",'650 €','','g',340),.8)],tags:[T_('OGNI ANNO, PER TUTTA LA VITA DA PENSIONATO','r',null,40)]},
 {w:.35,lab:'E SE I BUCHI SONO 5?',cap:'E SE GLI ANNI DI BUCO SONO CINQUE?',items:[C('ANNI DI BUCO','5','','r',320),Q()],tags:[]}]};
BLK[36]={scenes:[
 {w:.5,lab:'CINQUE ANNI DI BUCO',cap:'5 ANNI SENZA CONTRIBUTI: CIRCA 249 € IN MENO AL MESE',items:[C('5 ANNI','SENZA|CONTRIBUTI','','r',420),AR(),C('PENSIONE','− 249 €','AL MESE, LORDI','r',440)],tags:[]},
 {w:.5,lab:'COME USCIRE PRIMA',cap:'QUASI COME USCIRE A 64 ANNI... SENZA SCEGLIERLO',items:[C('USCIRE A 64 ANNI','− 185 €','AL MESE','d',440),OP('≈'),C('5 ANNI DI BUCO','− 249 €','AL MESE','r',440)],tags:[T_('MA SENZA AVERLO SCELTO!','r')]}]};
BLK[37]={scenes:[
 {w:.62,lab:'DA DOVE NASCONO I BUCHI?',cap:"LAVORO NON VERSATO, DIMENTICANZE, CARRIERE SPEZZATE",items:[A(C('CAUSA 1','LAVORO|NON VERSATO','','p',400),0),A(C('CAUSA 2','DIMENTICANZE|DELL\'AZIENDA','','p',400),.3),A(C('CAUSA 3','PERIODI SENZA|CONTRIBUTI','','p',400),.6),A(C('CAUSA 4','CARRIERE|SPEZZATE','','p',400),.9)],tags:[]},
 {w:.38,lab:'LA BUONA NOTIZIA',cap:'SE LI TROVI, LI PUOI SEGNALARE E FAR CORREGGERE',items:[C('LI TROVI','','','d',380),AR(),C('LI CORREGGI','','','g',380),K()],tags:[T_('CON I DOCUMENTI','g')]}]};
BLK[38]={scenes:[
 {w:.3,lab:'ORA IL TEST',cap:'ORA IL TEST! TRE DOMANDE, VERO O FALSO',items:[C('IL TEST','3 DOMANDE','VERO O FALSO?','g',520),Q()],tags:[T_('RISPONDI A VOCE ALTA','a')]},
 {w:.4,lab:'DOMANDA UNO',cap:"LA PENSIONE È SEMPRE UN % DELL'ULTIMO STIPENDIO?",items:[C('DOMANDA 1','PENSIONE = %|ULTIMO STIPENDIO','','p',600)],tags:[T_('VERO','g',300),T_('FALSO','r',300)]},
 {w:.3,lab:'LA RISPOSTA',cap:'FALSO! NEL CONTRIBUTIVO CONTA TUTTA LA CARRIERA',items:[C('RISPOSTA','FALSO!','','r',420),K()],tags:[T_('CONTA TUTTA LA CARRIERA','g')]}]};
BLK[39]={scenes:[
 {w:.4,lab:'DOMANDA DUE',cap:'IL MONTANTE CONTRIBUTIVO SI RIVALUTA OGNI ANNO?',items:[C('DOMANDA 2','MONTANTE|SI RIVALUTA?','','p',560)],tags:[T_('VERO','g',300),T_('FALSO','r',300)]},
 {w:.6,lab:'LA RISPOSTA',cap:'VERO! SI RIVALUTA CON IL PIL NOMINALE DEGLI ULTIMI 5 ANNI',cs:46,items:[C('RISPOSTA','VERO!','','g',400),C('PIL NOMINALE','ULTIMI|5 ANNI','','d',400),C('RISULTATO','NON RESTANO|FERMI','','p',420)],tags:[T_('I CONTRIBUTI PIÙ VECCHI NON RESTANO FERMI','a',null,38)]}]};
BLK[40]={scenes:[
 {w:.45,lab:'DOMANDA TRE',cap:"USCIRE PRIMA NON CAMBIA L'IMPORTO DELLA PENSIONE?",items:[C('DOMANDA 3','USCIRE PRIMA|NON CAMBIA?','','p',560)],tags:[T_('VERO','g',300),T_('FALSO','r',300)]},
 {w:.55,lab:'LA RISPOSTA',cap:"FALSO! IL COEFFICIENTE CAMBIA CON L'ETÀ",items:[C('RISPOSTA','FALSO!','','r',380),C('COEFFICIENTE','▼','PIÙ BASSO SE ESCI PRIMA','d',460)],tags:[T_('QUANTE NE HAI AZZECCATE?','a')]}]};
BLK[41]={scenes:[
 {w:.2,lab:'FAI IL CONTO DA SOLO',cap:'ADESSO FAI IL CONTO DA SOLO, IN TRE PASSI!',items:[CA()],tags:[T_('TRE PASSI','a')]},
 {w:.8,lab:'TRE PASSI',cap:'33%, ANNI DI CONTRIBUTI, COEFFICIENTE',items:[A(C('PASSO 1','STIPENDIO|× 33%','LORDO ANNUO','g',420),0),A(C('PASSO 2','× ANNI|DI CONTRIBUTI','','p',420),.4),A(C('PASSO 3','× COEFFICIENTE','DELL\'ETÀ DI USCITA','d',420),.78)],tags:[]}]};
BLK[42]={scenes:[
 {w:.5,lab:'POI DIVIDI PER TREDICI',cap:'POI DIVIDI PER 13: ECCO LA PENSIONE LORDA AL MESE',items:[C('PENSIONE ANNUA','','','p',380),OP('÷'),C('MENSILITÀ','13','','p',300),OP('='),C('AL MESE','LORDA','','g',360)],tags:[]},
 {w:.5,lab:'È UNA STIMA',cap:'UNA STIMA SEMPLIFICATA: SERVE IL CONTROLLO UFFICIALE',items:[CA(),C('CON LA CALCOLATRICE','1 MINUTO','','p',420),W_()],tags:[T_('PER LA CIFRA VERA: CONTROLLO UFFICIALE','a')]}]};
BLK[43]={scenes:[
 {w:.35,lab:'COME CONTROLLI',cap:'COME CONTROLLI IL TUO SALVADANAIO?',items:[PG(),Q()],tags:[T_('CONTROLLO DA 5 MINUTI SU MAI INPS','a')]},
 {w:.65,lab:'ENTRA SU INPS PUNTO IT',cap:'SPID, CARTA D\'IDENTITÀ ELETTRONICA O CARTA SERVIZI',cs:48,items:[BR('inps.it · Mai Inps',['Accedi con Spid','Carta d\'identità elettronica','Carta nazionale dei servizi','Fascicolo previdenziale'],1000,540)],tags:[]}]};
BLK[44]={scenes:[
 {w:.45,lab:'ESTRATTO CONTO',cap:"L'ELENCO DI TUTTI I TUOI CONTRIBUTI, ANNO PER ANNO",items:[DC('ESTRATTO CONTO CONTRIBUTIVO',['2019 · contributi versati','2020 · contributi versati','2021 · ANNO MANCANTE?','2022 · contributi versati'],720,460)],tags:[]},
 {w:.55,lab:'CONTROLLA DUE COSE',cap:"PER OGNI RIGA, CHIEDITI: QUESTO ANNO C'È?",items:[C('CONTROLLA 1','NON|MANCANO ANNI','','p',440),C('CONTROLLA 2','RETRIBUZIONI|GIUSTE','','p',440)],tags:[T_("QUESTO ANNO C'È?",'a')]}]};
BLK[45]={scenes:[
 {w:.45,lab:'LE TRE PORTE',cap:'TI RICORDI LE TRE PORTE?',items:[DR(1),DR(2),DR(3)],tags:[T_('CONTRIBUTIVO PURO · MISTO · FORNERO','a',null,38)]},
 {w:.55,lab:'LA TUA PORTA',cap:"GUARDA L'ANNO DEL TUO PRIMO CONTRIBUTO",items:[C('PRIMO CONTRIBUTO','ANNO ?','','p',440),AR(),C('LA TUA PORTA','1 · 2 · 3','','g',440)],tags:[T_('DUE MINUTI, E SAI QUAL È LA TUA','g')]}]};
BLK[46]={scenes:[
 {w:.45,lab:'SE TROVI UN BUCO',cap:"USA LA FUNZIONE PER SEGNALARE L'ANOMALIA",items:[W_(),C('SEGNALA','L\'ANOMALIA','','d',440)],tags:[]},
 {w:.55,lab:'POI IL PATRONATO',cap:'PORTA BUSTE PAGA E CONTRATTI A UN PATRONATO',items:[DC('BUSTE PAGA',['2020','2021'],380,330),DC('CONTRATTI',['lavoro','periodi'],380,330,'#0B4A50'),AR(),C('PATRONATO','TI AIUTA','A CORREGGERE','g',420)],tags:[]}]};
BLK[47]={scenes:[
 {w:.45,lab:'PENSAMI',cap:"PENSAMI, IL SIMULATORE DELL'INPS",items:[BR('inps.it · Pensami',['Simulatore pensione','Stima in base ai tuoi dati'],900,440)],tags:[T_('UNA STIMA DELLA TUA PENSIONE','a')]},
 {w:.55,lab:'PROVALO',cap:"PROVALO CON ETÀ DI USCITA DIVERSE",items:[A(C('USCITA A 64','? €','','p',300),.0),A(C('USCITA A 65','? €','','p',300),.25),A(C('USCITA A 66','? €','','p',300),.5),A(C('USCITA A 67','? €','','g',300),.75)],tags:[T_("È QUELLO CHE ABBIAMO FATTO NOI ADESSO",'g',null,38)]}]};
BLK[48]={scenes:[
 {w:1,lab:'IN TRE MOSSE',cap:'RIASSUNTO DA FARE OGGI, IN TRE MOSSE!',items:[A(C('UNO','APRI|ESTRATTO CONTO','SU MAI INPS','g',430),.0),A(C('DUE','CONTA GLI ANNI|CERCA I BUCHI','','p',430),.38),A(C('TRE','SEGNALA|VAI AL PATRONATO','SE NON TORNA','d',430),.72)],tags:[T_('POCHI MINUTI','a')]}]};
BLK[49]={scenes:[
 {w:.4,lab:'OCCHIO',cap:'OCCHIO A TRE ERRORI!',items:[W_()],tags:[T_('TRE ERRORI','r')]},
 {w:.6,lab:'ERRORE 1 E 2',cap:'PRIMO E SECONDO ERRORE',items:[C('ERRORE 1','FIDARTI DI|UN CALCOLO IN RETE','SENZA CONTROLLARE','r',520),C('ERRORE 2','LASCIARE IL LAVORO|PRIMA DI VERIFICARE','L\'ESTRATTO CONTO','r',520)],tags:[]}]};
BLK[50]={scenes:[
 {w:.5,lab:'ERRORE 3',cap:"ASPETTARE L'ULTIMO ANNO PER GUARDARE LA POSIZIONE",cs:48,items:[C('ERRORE 3','ASPETTARE|L\'ULTIMO ANNO','','r',460),CAL('ULTIMO','1','ANNO',170)],tags:[]},
 {w:.5,lab:'MEGLIO OGGI',cap:'MEGLIO GUARDARLA OGGI, CON ANCORA TUTTO IL TEMPO',items:[C('OGGI','HAI ANCORA|TUTTO IL TEMPO','','g',480),K()],tags:[T_('CORREGGERE UN BUCO RICHIEDE TEMPO E DOCUMENTI','a',null,38)]}]};
BLK[51]={scenes:[
 {w:1,lab:'RICAPITOLIAMO',cap:'TRE NUMERI DECIDONO LA TUA PENSIONE',items:[A(C('NUMERO UNO','L\'ETÀ','CHE SCEGLIE IL COEFFICIENTE','g',500),.0),A(C('NUMERO DUE','QUANTO|GUADAGNI','RIEMPIE IL SALVADANAIO','p',500),.38),A(C('NUMERO TRE','ANNI|COPERTI','DA CONTRIBUTI','r',500),.72)],tags:[]}]};
BLK[52]={scenes:[
 {w:.3,lab:'IL CONTO PROMESSO',cap:'ECCO IL CONTO CHE TI AVEVO PROMESSO!',items:[CA(),Q()],tags:[T_('STESSO STIPENDIO, STESSI CONTRIBUTI','a',null,40)]},
 {w:.7,lab:'64 CONTRO 67 ANNI',cap:'USCIRE A 64 INVECE CHE A 67 COSTA CIRCA 185 € AL MESE',cs:46,items:[A(C('67 ANNI','1.993 €','LORDI AL MESE','p',380),0),A(OP('−'),.2),A(C('64 ANNI','1.808 €','LORDI AL MESE','p',380),.4),A(OP('='),.6),A(C('COSTA','185 €','AL MESE, LORDI','r',380),.8)],tags:[]}]};
BLK[53]={scenes:[
 {w:.65,lab:'LA SORPRESA',cap:'SE LA PENSIONE DURA 20 ANNI: CIRCA 48.000 € IN MENO',items:[A(C('PERDI','185 €','AL MESE','r',300),0),A(OP('×'),.18),A(C('MENSILITÀ','13','','p',260),.34),A(OP('×'),.5),A(C('ANNI','20','','p',260),.64),A(AR(),.78),A(C('IN TOTALE','48.000 €','LORDI','r',420),.9)],tags:[]},
 {w:.35,lab:'UNA SCELTA DI TRE ANNI',cap:'48.000 €, PER UNA SCELTA DI TRE ANNI!',items:[C('SCELTA DI','3 ANNI','','d',380),AR(),C('COSTO','≈ 48.000 €','','r',460)],tags:[T_('GUARDA I NUMERI PRIMA DI DECIDERE','g')]}]};
BLK[54]={scenes:[
 {w:.3,lab:'RICORDA',cap:'È UN ESEMPIO SEMPLIFICATO, CON NUMERI TONDI',items:[ST('ESEMPIO SEMPLIFICATO',RED_),W_()],tags:[]},
 {w:.4,lab:'NELLA REALTÀ CONTANO',cap:'NELLA REALTÀ CONTANO QUATTRO COSE',items:[C('1','SISTEMA|DI CALCOLO','','p',330),C('2','RIVALUTAZIONE','','p',330),C('3','CARRIERA','','p',330),C('4','ANNI|COPERTI','','p',330)],tags:[]},
 {w:.3,lab:'PER LA TUA CIFRA',cap:'CONTROLLA INPS PUNTO IT, OPPURE CHIEDI A UN PATRONATO',cs:48,items:[BR('inps.it',['La tua posizione ufficiale'],760,360),C('OPPURE','PATRONATO','','g',380)],tags:[]}]};
BLK[55]={scenes:[
 {w:.6,lab:'TOCCA A TE',cap:'SCRIVIMI NEI COMMENTI: IN CHE ANNO SEI NATO?',items:[DC('COMMENTI',['Sono nato nel 1968…','Penso di uscire a 67 anni…'],640,380,'#0B4A50'),Q()],tags:[T_('IN CHE ANNO SEI NATO?','a'),T_('A CHE ETÀ VAI IN PENSIONE?','g')]},
 {w:.4,lab:'I PROSSIMI VIDEO',cap:'LE VOSTRE DOMANDE DIVENTANO I PROSSIMI VIDEO',items:[C('LE VOSTRE DOMANDE','I PROSSIMI|VIDEO','LEGGO TUTTO','g',560)],tags:[]}]};

BLK[56]={scenes:[
 {w:.55,lab:'ISCRIVITI',cap:'ISCRIVITI A CONTI IN PENSIONE E ATTIVA LA CAMPANELLA',cs:50,items:[C('CONTI IN PENSIONE','ISCRIVITI','ATTIVA LA CAMPANELLA','r',560),K()],tags:[]},
 {w:.45,lab:'IL PROSSIMO VIDEO',cap:'UN TEMA CHE TOCCA TUTTI I PENSIONATI. NON PERDERLO!',cs:50,items:[C('PROSSIMO VIDEO','UN TEMA CHE|TOCCA TUTTI','I PENSIONATI','g',560)],tags:[T_('NON PERDERLO!','a')]}]};
BLK[57]={scenes:[
 {w:1,lab:'VERIFICA SEMPRE',cap:'VERIFICA SEMPRE SUI CANALI UFFICIALI: INPS.IT',cs:50,items:[BR('inps.it',['Canali ufficiali'],760,380),C('DISCLAIMER','CONTENUTO INFORMATIVO','NON È CONSULENZA PREVIDENZIALE','d',900)],tags:[]}]};
