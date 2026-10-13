// ===== VIDEO 6 (cedolino di novembre) - motore b-sync-80: tempi calcolati su testo + durata del blocco =====
// Regole: scene >= 5 s, comparsa 0,9 s, nessun elemento sparisce nella scena, tutto completo entro l'80 %, poi fermo.
const SPECS={};
const GF_='url(#g_badge)',RF_='url(#g_red)',PF_='url(#g_paper)',DF_='#0B4A50';
const VT=(s,x,y,at,fill,fs)=>I('tag',[s,fill||AMB,(fill&&fill!==AMB)?'#fff':'#5A3300',fs||44],x,y,at);
const VN=(s,x,y,at,o)=>{o=o||{};return I('num',[s,o.fs||76,o.fill||PF_,o.sub,o.subfill,o.minw],x,y,at);};
BUILD.calS=(g,h,b,bs,sub,sc)=>{const w=el('g',{transform:'translate(0 '+(-250*sc)+') scale('+sc+')'},g);calendarPage(w,h,b,bs,sub);};
BUILD.stepRow=(g,n,label,fill,w)=>{w=w||900;el('rect',{x:-w/2,y:-52,width:w,height:104,rx:52,fill:'url(#g_paper)',filter:'url(#g_sh2)'},g);el('circle',{cx:-w/2+52,cy:0,r:44,fill:fill||GF_,stroke:'#fff','stroke-width':6},g);txt(g,n,-w/2+52,16,48,'#fff','900');txt(g,label,-w/2+120,15,40,INK,'900','start');};
BUILD.recap=(g,n,title,text,fill,w)=>{w=w||1560;el('rect',{x:-w/2,y:-75,width:w,height:150,rx:34,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);el('rect',{x:-w/2,y:-75,width:170,height:150,rx:34,fill:fill||GF_},g);el('rect',{x:-w/2+120,y:-75,width:50,height:150,fill:fill||GF_},g);txt(g,n,-w/2+85,24,76,'#fff','900');txt(g,title,-w/2+210,-14,30,GRN,'bold','start');txt(g,text,-w/2+210,46,50,INK,'900','start');};
// ---------- BLOCCO 1 (712 fotogrammi = 23,7 s) ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CEDOLINO DI NOVEMBRE',cap:'PER ALCUNI È PIÙ BASSA, MA NON È UN ERRORE',items:[
  I('cal',['NOVEMBRE','2026',110,''],330,560,'Novembre.'),
  I('pay',['CEDOLINO','? €'],840,540,['Apri il cedolino',0.6]),
  VT('PIÙ BASSA DI OTTOBRE?',1470,430,'più bassa di ottobre',RF_,40),
  I('stamp',['NON È UN ERRORE',GRN,48],1470,700,'non è un errore')]},
 {at:'Per altri, invece',top:'PER ALTRI: ULTIMO MESE',cap:'PRIMA IL CONTO VERO, POI L\'EQUIVOCO DEI TITOLI',items:[
  VT('PER ALTRI',480,225,'Per altri',GF_,44),
  VN('ULTIMO MESE',480,340,"l'ultimo mese",{fs:60,fill:RF_,sub:'SOLDI TOLTI',minw:620}),
  I('arR',[],960,340,'ti toglie dei soldi'),
  VN('DICEMBRE',1440,340,'da dicembre ti arrivano di più',{fs:60,fill:GF_,sub:'TI ARRIVA DI PIÙ',minw:560}),
  I('calc',[],250,650,'Ti faccio il conto vero'),
  VT('IL CONTO VERO',620,650,'il conto vero',GF_,38),
  I('hl',['AUMENTI E ARRETRATI'],1400,620,'quei titoli'),
  I('stamp',['UN EQUIVOCO',RED_,48],1400,790,"c'è un equivoco")]},
]);

// ---------- BLOCCO 2 (495 f) ----------
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA DATA DEL PAGAMENTO',cap:'ACCREDITO: LUNEDÌ 2 NOVEMBRE, NON È UN RITARDO',items:[
  I('calS',['NOVEMBRE','1',220,'DOMENICA',0.8],250,590,'Il primo novembre è domenica'),
  VT('ANCHE OGNISSANTI',360,260,'anche Ognissanti',AMB,38),
  VT('PRIMO GIORNO BANCABILE',1150,260,'primo giorno bancabile',GF_,38),
  I('arR',[],620,590,"quest'anno l'accredito"),
  I('calS',['NOVEMBRE','2',220,'LUNEDÌ',0.8],990,590,'lunedì due novembre'),
  VT('BANCA E POSTE',1520,450,'in banca e alle Poste',GF_,40),
  I('stamp',['NON È UN RITARDO',GRN,40],1500,720,'Non è un ritardo')]},
]);
// ---------- BLOCCO 3 (643 f) ----------
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'I TITOLI DI NOVEMBRE',cap:'AUMENTI E ARRETRATI: PER I MEDICI DELL\'ENPAM',items:[
  I('hl',['AUMENTI E ARRETRATI'],560,300,'Aumenti e arretrati a novembre'),
  VT('A CHI SONO RIVOLTI?',1450,300,'Guarda bene a chi sono rivolti',RF_,44),
  VN('ENPAM',480,580,'Riguardano i pensionati della cassa',{fs:90,fill:GF_,sub:'MEDICI E ODONTOIATRI',minw:620}),
  VT('ADEGUAMENTO IN RITARDO',1400,500,"che hanno ricevuto in ritardo l'adeguamento",AMB,40),
  VT('AL COSTO DELLA VITA',1400,640,'al costo della vita',GF_,40)]},
 {at:'Se la tua pensione la paga',top:'PENSIONE PAGATA DALL\'INPS',cap:'A NOVEMBRE NESSUN AUMENTO GENERALE',items:[
  VN('INPS',440,330,'Se la tua pensione la paga',{fs:90,sub:'LA TUA PENSIONE',minw:560}),
  I('stamp',['NESSUN AUMENTO',RED_,56],1330,330,'non scatta nessun aumento generale'),
  I('calS',['GENNAIO','+1,4 %',100,'RIVALUTAZIONE',0.58],440,700,"l'hai già avuta a gennaio"),
  VN('1,4 %',1330,660,'uno virgola quattro per cento',{fs:100,fill:GF_,sub:'GIÀ AVUTA A GENNAIO',minw:700})]},
]);
// ---------- BLOCCO 4 (567 f) ----------
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DUE VOCI FISCALI',cap:'UNA ARRIVA, UNA FINISCE: PARTO DA QUELLA CHE PESA',items:[
  VT('COSA CAMBIA NEL CEDOLINO?',960,260,'Allora cosa cambia davvero',GF_,46),
  VN('ARRIVA',500,480,'una arriva',{fs:84,fill:RF_,sub:'MENO SOLDI A NOVEMBRE',minw:660}),
  VN('FINISCE',1420,480,'una finisce',{fs:84,fill:GF_,sub:'PIÙ SOLDI A DICEMBRE',minw:660}),
  VT('QUASI NESSUNO LA SPIEGA',500,700,'quasi nessuno te la spiega',AMB,40),
  VT('PIÙ SOLDI A DICEMBRE',1420,700,'ti lascia più soldi a dicembre',GF_,40),
  I('stamp',['PARTO DA QUELLA CHE ARRIVA',GRN,44],960,820,'Parto da quella che arriva')]},
]);
// ---------- BLOCCO 5 (673 f) ----------
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SECONDO ACCONTO IRPEF',cap:'CHI HA FATTO IL 730 E DEVE PAGARE IMPOSTA',items:[
  I('stamp',['SECONDO ACCONTO IRPEF',RED_,54],960,270,'Si chiama secondo acconto Irpef'),
  I('doc',['MODELLO 730',420,330,GRN,44],440,590,'il modello settecentotrenta'),
  VT("L'INPS TRATTIENE LE TASSE",1330,470,"con l'Inps che trattiene le tasse",AMB,42),
  VN('IMPOSTA DA PAGARE',1330,660,"risulta un'imposta da pagare",{fs:56,fill:RF_,minw:700})]},
 {at:'Capita, per esempio',top:'A CHI CAPITA',cap:'UN ANTICIPO DELLE TASSE, TOLTO DALLA PENSIONE',items:[
  VN('PENSIONE',440,330,'a chi oltre alla pensione',{fs:64,minw:520}),
  I('op',['+'],790,330,'ha un affitto'),
  VN('AFFITTO O LAVORO',1330,330,'ha un affitto o un piccolo lavoro',{fs:56,fill:GF_,minw:720}),
  VN('ACCONTO',420,600,"L'acconto è un anticipo",{fs:76,fill:AMB,sub:'ANTICIPO DELLE TASSE',minw:640}),
  VT('TOLTO DALLA PENSIONE',1330,640,'lo toglie direttamente dalla pensione',RF_,42)]},
]);

// ---------- BLOCCO 6 (781 f) ----------
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FACCIAMO UN ESEMPIO',cap:'IMPOSTA 800 €: ACCONTO 100 %, SI DIVIDE IN DUE RATE',items:[
  VT('UN ESEMPIO CON NUMERI SEMPLICI',960,260,'Facciamo un esempio',GF_,44),
  VN('800 €',480,480,"un'imposta di ottocento euro",{fs:100,sub:'IMPOSTA DAL 730',minw:560}),
  I('arR',[],900,480,"L'acconto è di norma"),
  VN('100 %',1330,480,'il cento per cento',{fs:100,fill:GF_,sub:'ACCONTO = 800 €',minw:620}),
  VN('SUPERA 257,52 €',430,760,'Siccome supera',{fs:50,fill:AMB,minw:600}),
  I('arR',[],900,760,'si divide'),
  VN('DUE RATE',1330,760,'in due rate',{fs:70,fill:RF_,minw:560})]},
 {at:'Il quaranta per cento',top:'DUE RATE',cap:'40 % IN ESTATE, 60 % A NOVEMBRE',items:[
  VN('40 %',500,380,'Il quaranta per cento',{fs:100,fill:'#2B6F77',sub:'320 €',minw:520}),
  VT('GIÀ TRATTENUTO',500,580,'di solito è già stato trattenuto',GF_,42),
  VT('ESTATE E INIZIO AUTUNNO',500,700,"tra l'estate e l'inizio dell'autunno",AMB,38),
  VN('60 %',1400,380,'Il sessanta per cento',{fs:100,fill:RF_,sub:'480 €',minw:520}),
  VT('ARRIVA A NOVEMBRE',1400,580,'arriva a novembre',RF_,42)]},
]);
// ---------- BLOCCO 7 (631 f) ----------
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CEDOLINO DI NOVEMBRE',cap:'NETTO 1.400 €: A NOVEMBRE ARRIVANO 920 €',items:[
  VT('COSA VEDI NEL CEDOLINO?',960,255,'Cosa vedi nel cedolino',AMB,46),
  VN('1.400 €',460,400,'mille e quattrocento euro',{fs:96,sub:'PENSIONE NETTA',minw:580}),
  I('arR',[],900,400,'a novembre ne arrivano'),
  VN('920 €',1360,400,'novecentoventi',{fs:96,fill:RF_,sub:'A NOVEMBRE',minw:580}),
  VN('- 480 €',910,700,'Quattrocentottanta euro in meno',{fs:110,fill:RF_,sub:'IN UNA VOLTA SOLA',minw:760})]},
 {at:'Non è un errore',top:'NON È UN ERRORE',cap:"SONO LE TASSE DI QUEST'ANNO PAGATE IN ANTICIPO",items:[
  I('stamp',['NON È UN ERRORE',GRN,48],480,290,"Non è un errore dell'Inps"),
  I('stamp',['NON È UNA MULTA',RED_,48],1400,290,'non è una multa'),
  VT("TASSE DI QUEST'ANNO IN ANTICIPO",960,470,"sono le tasse di quest'anno",GF_,42),
  VT("SE L'ACCONTO ERA TROPPO ALTO",470,650,"E se l'acconto era troppo alto",AMB,36),
  VN('RECUPERI',1400,640,'la differenza la recuperi',{fs:70,fill:GF_,sub:'CON LA DICHIARAZIONE',minw:640}),
  VT("DELL'ANNO PROSSIMO",1400,810,"dell'anno prossimo",AMB,38)]},
]);
// ---------- BLOCCO 8 (899 f) ----------
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:"SE L'ACCONTO È PIÙ PICCOLO",cap:'DUE SOGLIE: 257,52 € E 51,65 €',items:[
  VT('ACCONTO PIÙ PICCOLO',960,215,"Se l'acconto è più piccolo",GF_,44),
  VN('SOTTO 257,52 €',430,350,'Sotto duecentocinquantasette euro',{fs:56,sub:'NON SI DIVIDE',minw:640}),
  I('arR',[],900,350,'non si divide'),
  VN('UNA RATA',1400,350,'si paga tutto a novembre',{fs:70,fill:RF_,sub:'TUTTO A NOVEMBRE',minw:600}),
  VN('SOTTO 51,65 €',430,650,'non supera cinquantuno euro',{fs:56,sub:"IMPOSTA DI RIFERIMENTO",minw:640}),
  I('arR',[],900,650,"l'acconto non si paga proprio"),
  I('stamp',['ACCONTO NON DOVUTO',GRN,46],1400,650,'non si paga proprio')]},
 {at:'Se hai solo la pensione',top:'SE HAI SOLO LA PENSIONE',cap:"DI SOLITO QUESTA VOCE NON C'È",items:[
  VN('SOLO PENSIONE',480,330,'Se hai solo la pensione',{fs:64,sub:'NESSUN ALTRO REDDITO',minw:640}),
  I('stamp',["DI SOLITO NON C'È",GRN,52],1400,330,'questa voce di solito'),
  I('calS',['OTTOBRE','10',200,'SCADENZA',0.62],300,650,'entro il dieci ottobre'),
  VT('DOMANDA PER RIDURLO',1000,560,'La domanda per ridurlo',AMB,40),
  VT('SE È PASSATO: CONTROLLA IL CEDOLINO',1150,690,'se è passato, controlla il cedolino',GF_,38),
  VT('PARLANE CON UN CAF',1150,810,'parlane con un Caf',GF_,38)]},
]);

// ---------- BLOCCO 9 (549 f) ----------
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA VOCE CHE FINISCE',cap:'NOVEMBRE: ULTIMA RATA DELLE ADDIZIONALI',items:[
  VT('LA VOCE CHE FINISCE',960,255,'la voce che finisce',GF_,46),
  VT('ADDIZIONALE REGIONALE',560,400,'quella regionale',AMB,40),
  VT('ADDIZIONALE COMUNALE',1360,400,'quella comunale',AMB,40),
  I('calS',['NOVEMBRE','ULTIMA',84,'RATA',0.62],330,650,'Novembre è l\'ultimo mese'),
  VN('RATE DEL 730',1100,620,'rate di un debito del modello',{fs:60,sub:'DEVONO CONCLUDERSI ENTRO NOVEMBRE',minw:900}),
  I('stamp',['DICEMBRE: NON CI SONO PIÙ',GRN,44],1100,795,'nella rata di dicembre')]},
]);
// ---------- BLOCCO 10 (744 f) ----------
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'UN ESEMPIO',cap:'A DICEMBRE QUEI SOLDI RESTANO A TE',items:[
  VT('UN ESEMPIO',960,250,'Un esempio',GF_,46),
  VN('- 50 €',480,400,'cinquanta euro di addizionali',{fs:96,fill:RF_,sub:'ADDIZIONALI OGGI',minw:580}),
  I('arR',[],940,400,'a dicembre'),
  VN('+ 50 €',1400,400,'quei cinquanta euro restano a te',{fs:96,fill:GF_,sub:'RESTANO A TE',minw:580}),
  I('stamp',['NON È UN AUMENTO',AMB,50],960,660,'Non è un aumento'),
  VT('SOLDI CHE TI VENIVANO TOLTI',960,810,'soldi che prima ti venivano tolti',GF_,42)]},
 {at:'In più a dicembre',top:'TREDICESIMA E GENNAIO',cap:'LA TREDICESIMA NON PAGA LE ADDIZIONALI',items:[
  I('calS',['DICEMBRE','13ª',170,'TREDICESIMA',0.75],380,560,"c'è la tredicesima"),
  VN('NIENTE ADDIZIONALI',1250,350,'che le addizionali non le paga',{fs:56,fill:GF_,minw:760}),
  VT('DA GENNAIO RIPARTONO',1250,520,'da gennaio le trattenute ripartono',RF_,42),
  VT('TREDICESIMA: DA 600 A 3.000 €',1250,680,'da seicento a tremila euro',AMB,40),
  VT('NEL VIDEO PRECEDENTE',1250,800,'nel video precedente del canale',GF_,40)]},
]);
// ---------- BLOCCO 11 (666 f) ----------
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL NUMERO ESATTO',cap:'ENTRA IN MY INPS CON LO SPID',items:[
  VT('SENZA STIME',960,235,'Come vedere il numero esatto',AMB,46),
  I('br',['MY INPS',760,380],500,560,'Entra in Mai Inps'),
  VT('ACCEDI CON SPID',500,590,'con lo Spid',GF_,44),
  I('stepRow',['1','PENSIONE E PREVIDENZA',GF_,780],1400,420,'Vai su Pensione e previdenza'),
  I('stepRow',['2','CEDOLINO DELLA PENSIONE',GF_,780],1400,560,'poi su Cedolino della pensione'),
  I('stepRow',['3','APRI QUELLO DI NOVEMBRE',RF_,780],1400,700,'e apri quello di novembre')]},
 {at:'Cerca tre voci',top:'LE TRE VOCI DA CERCARE',cap:'ACCONTO IRPEF, ADDIZIONALE REGIONALE E COMUNALE',items:[
  I('stepRow',['1','ACCONTO IRPEF',GF_,860],500,330,'acconto Irpef'),
  I('stepRow',['2','ADDIZIONALE REGIONALE',GF_,860],500,470,'addizionale regionale'),
  I('stepRow',['3','ADDIZIONALE COMUNALE',GF_,860],500,610,'addizionale comunale'),
  I('doc',['CERTIFICATO DI PENSIONE',640,300,GRN,38],1440,470,'scarica il certificato di pensione'),
  I('stamp',['MODELLO ObisM',AMB,50],1440,720,'il modello Obis emme')]},
]);
// ---------- BLOCCO 12 (792 f) ----------
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RICAPITOLO',cap:'DATA E AUMENTI: I NUMERI GIUSTI',items:[
  VT('RICAPITOLO CON I NUMERI',960,195,'Ricapitolo, con i numeri',GF_,42),
  I('recap',['1','PAGAMENTO','LUNEDÌ 2 NOVEMBRE',GF_],960,340,'Il primo novembre è domenica'),
  I('recap',['2','AUMENTI','NESSUN AUMENTO GENERALE',RED_],960,540,'Nessun aumento generale'),
  VT('GLI AUMENTI SONO PER I MEDICI ENPAM',960,740,"gli aumenti dei titoli sono per i medici dell'Enpam",AMB,40)]},
 {at:'Se hai fatto il settecentotrenta',top:'RICAPITOLO',cap:'ACCONTO E ADDIZIONALI',items:[
  I('recap',['3','ACCONTO IRPEF','60 % A NOVEMBRE',RED_],960,330,'Se hai fatto il settecentotrenta'),
  VT('NELL\'ESEMPIO: 480 €',1300,480,'quattrocentottanta euro',RF_,44),
  I('recap',['4','ADDIZIONALI','FINISCONO A NOVEMBRE',GF_],960,640,'E le addizionali finiscono'),
  VT('A DICEMBRE QUEI SOLDI RESTANO A TE',960,810,'a dicembre quei soldi restano a te',GF_,40)]},
]);
// ---------- BLOCCO 13 (614 f) - schermata finale: contenuti solo in alto, zona bassa libera ----------
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'GRAZIE PER AVER GUARDATO',cap:'',items:[
  VT('SCRIVIMI QUANTO PRENDI',460,235,'quanto prendi',GF_,38),
  VT('TI RISPONDO CON IL CONTO',1380,235,'ti rispondo con il conto',AMB,38),
  VT('MI PIACE',330,335,'metti mi piace',GF_,38),
  VT('ISCRIVITI',770,335,'iscriviti',RF_,38),
  VT('ATTIVA LA CAMPANELLA',1450,335,'attiva la campanella',AMB,38),
  I('dbg',[1500,300],960,560,'Regole e importi cambiano'),
  I('dline',['REGOLE E IMPORTI CAMBIANO: VERIFICA SUL SITO DELL\'INPS','#fff',40],960,552,'verifica sempre sul sito'),
  I('dline',['INFORMAZIONE GENERALE, NON CONSULENZA','#fff',40],960,614,'Informazione generale'),
  I('dline',['IL CANALE NON È AFFILIATO ALL\'INPS','#7FF0D2',40],960,676,"Il canale non è affiliato")]},
]);
