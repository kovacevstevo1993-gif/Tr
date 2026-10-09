// ===== V4 blocchi: ogni elemento compare quando la voce lo dice (motore sincronizzato) =====
const SPECS={};
const GF_='url(#g_badge)',RF_='url(#g_red)',PF_='url(#g_paper)',DF_='#0B4A50';
const VT=(s,x,y,at,fill,fs)=>I('tag',[s,fill||AMB,(fill&&fill!==AMB)?'#fff':'#5A3300',fs||44],x,y,at);
const VN=(s,x,y,at,o)=>{o=o||{};return I('num',[s,o.fs||76,o.fill||PF_,o.sub,o.subfill,o.minw],x,y,at);};
const VO=(s,x,y,at)=>I('op',[s],x,y,at);

// ---------- BLOCCO 1 ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONI 2027',cap:'L’AUMENTO DI GENNAIO NON ARRIVA UGUALE A TUTTI',items:[
  VN('GENNAIO 2027',960,340,'Pensioni 2027',{fs:84,sub:'L’AUMENTO',minw:900}),
  I('seg',[560,110,GF_,'AUMENTO PIENO'],560,640,'aumento di gennaio'),
  I('seg',[560,110,AMB,'AUMENTO RIDOTTO'],1360,640,'non arriva')]},
 {at:'E per certi invalidi civili',top:'INVALIDI CIVILI · 2026',cap:'PER CERTI INVALIDI IL TOTALE È SALITO DI SOLI 45 CENTESIMI',items:[
  VT('CERTI INVALIDI CIVILI',960,700,'certi invalidi civili',GF_,44),
  VN('0,45 €',960,360,'soli quarantacinque centesimi',{fs:170,fill:RF_,sub:'AL MESE, NEL 2026'})]},
 {at:'Chi sono?',top:'CHI SONO?',cap:'TE LO MOSTRO CON I NUMERI UFFICIALI DELL’INPS, PRIMA DELLA FINE',items:[
  I('q',[110],560,430,'Chi sono?'),
  I('br',['inps.it',620,300],1300,430,'con i numeri ufficiali'),
  VT('NUMERI UFFICIALI INPS',1300,660,'numeri ufficiali',GF_,40),
  VT('PRIMA DELLA FINE',1300,770,'prima della fine',AMB,40)]},
]);
// ---------- BLOCCO 2 ----------
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO VERO',cap:'I TITOLI PARLANO DI PERCENTUALI, A TE INTERESSANO GLI EURO',items:[
  I('calc',[],480,470,'Ti faccio il conto vero'),
  VN('3 %',1280,330,'i titoli parlano di percentuali',{fs:110,sub:'I TITOLI'}),
  VN('EURO',1280,650,'gli euro che arrivano davvero',{fs:110,fill:GF_,sub:'QUELLI CHE ARRIVANO'})]},
 {at:'E pensione, assegno',top:'TRE PRESTAZIONI',cap:'NON SEGUONO LA STESSA REGOLA: QUASI NESSUNO TE LO DICE',items:[
  I('doc',['PENSIONE',440,300,undefined,40],360,430,'E pensione'),
  I('doc',['ASSEGNO',440,300,undefined,40],960,430,'assegno e accompagnamento'),
  I('doc',['ACCOMPAGNAMENTO',500,300,undefined,32],1560,430,'accompagnamento non seguono'),
  VT('REGOLE DIVERSE',960,700,'non seguono la stessa regola',RF_,44),
  VT('QUASI NESSUNO TE LO DICE',960,805,'quasi nessuno te lo dice',AMB,40)]},
]);
// ---------- BLOCCO 3 ----------
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'UNA PREMESSA ONESTA',cap:'LA PERCENTUALE UFFICIALE DEL 2027 NON ESISTE ANCORA',items:[
  VN('2027',560,400,'del duemilaventisette',{fs:130,sub:'% UFFICIALE'}),
  I('stamp',['NON ESISTE ANCORA',RED_,52],1300,400,'non esiste ancora'),
  VT('DECRETO A NOVEMBRE',1300,600,'la fissa un decreto a novembre',AMB,44)]},
 {at:'Uso il tre per cento',top:'COME FACCIAMO',cap:'ESEMPIO AL 3 %, MA GLI IMPORTI DI PARTENZA SONO UFFICIALI',items:[
  VN('3 %',560,400,'Uso il tre per cento',{fs:130,sub:'ESEMPIO'}),
  VN('IMPORTI INPS',1330,400,'gli importi di partenza',{fs:84,fill:GF_,sub:'UFFICIALI'}),
  I('chk',[100],1330,690,'quelli ufficiali')]},
]);
// ---------- BLOCCO 4 ----------
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TRE COSE DIVERSE',cap:'SOTTO IL NOME INVALIDITÀ CI SONO TRE PRESTAZIONI',items:[
  I('circ',['1',GF_],460,430,'Sotto il nome'),
  I('circ',['2','url(#g_head)'],960,430,['Sotto il nome',0.45]),
  I('circ',['3',RF_],1460,430,['Sotto il nome',0.9]),
  VT('INVALIDITÀ',960,640,'il nome invalidità',AMB,44)]},
 {at:'La pensione di inabilità',top:'PENSIONE DI INABILITÀ',cap:'PER CHI HA IL 100 % DI INVALIDITÀ',items:[
  I('doc',['PENSIONE DI INABILITÀ',780,330,undefined,38],620,450,'La pensione di inabilità'),
  VN('100 %',1470,440,'per chi ha il cento per cento',{fs:130,fill:GF_,sub:'INVALIDITÀ'})]},
 {at:'L’assegno mensile',top:'ASSEGNO MENSILE',cap:'PER CHI HA DAL 74 AL 99 % DI INVALIDITÀ',items:[
  I('doc',['ASSEGNO MENSILE',780,330,undefined,38],620,450,'L’assegno mensile'),
  VN('74 – 99 %',1470,440,'dal settantaquattro al novantanove',{fs:110,fill:AMB,sub:'INVALIDITÀ'})]},
 {at:'E l’indennità',top:'ACCOMPAGNAMENTO',cap:'LA TERZA: L’INDENNITÀ DI ACCOMPAGNAMENTO',items:[
  I('circ',['3',RF_],560,440,'E l’indennità'),
  I('doc',['INDENNITÀ DI ACCOMPAGNAMENTO',900,330,undefined,34],1250,450,['E l’indennità',0.5])]},
]);
// ---------- BLOCCO 5 ----------
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONE DI INABILITÀ · 2026',cap:'340,71 € AL MESE, PER 13 MENSILITÀ',items:[
  VN('340,71 €',960,360,'trecentoquaranta euro e settantuno',{fs:150,fill:GF_,sub:'AL MESE NEL 2026'}),
  VT('13 MENSILITÀ',960,640,'per tredici mensilità',AMB,48)]},
 {at:'Spetta tra i diciotto',top:'CHI HA DIRITTO',cap:'DA 18 A 67 ANNI, REDDITO PERSONALE SOTTO 20.029,55 €',items:[
  VN('18 – 67',600,380,'tra i diciotto',{fs:110,sub:'ANNI'}),
  VN('20.029,55 €',1320,380,'ventimilaventinove',{fs:90,fill:AMB,sub:'LIMITE DI REDDITO ANNUO'}),
  VT('REDDITO PERSONALE',1320,640,'reddito personale',GF_,40)]},
]);
// ---------- BLOCCO 6 ----------
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ASSEGNO MENSILE · 2026',cap:'340,71 € AL MESE · INVALIDITÀ DAL 74 AL 99 %',items:[
  VN('74 – 99 %',560,380,'dal settantaquattro',{fs:110,fill:AMB,sub:'INVALIDITÀ'}),
  VN('340,71 €',1380,380,'stesso importo',{fs:120,fill:GF_,sub:'STESSO IMPORTO'})]},
 {at:'Ma il limite di reddito',top:'IL LIMITE DI REDDITO',cap:'MOLTO PIÙ BASSO: 5.852,21 € ALL’ANNO',items:[
  VN('20.029,55 €',520,400,'Ma il limite',{fs:80,sub:'PENSIONE DI INABILITÀ'}),
  I('arR',[],930,400,'molto più basso'),
  VN('5.852,21 €',1400,400,'cinquemilaottocentocinquantadue',{fs:90,fill:RF_,sub:'ASSEGNO MENSILE · ANNO',minw:780}),
  VT('MOLTO PIÙ BASSO',1400,660,'molto più basso',RF_,44)]},
]);
// ---------- BLOCCO 7 ----------
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'L’ACCOMPAGNAMENTO',cap:'552,57 € AL MESE · NON DIPENDE DAL REDDITO',items:[
  VN('552,57 €',960,360,'cinquecentocinquantadue',{fs:150,fill:GF_,sub:'AL MESE NEL 2026'}),
  VT('NON DIPENDE DAL REDDITO',960,640,'non dipende dal reddito',AMB,44)]},
 {at:'Occhio:',top:'OCCHIO',cap:'PER QUESTA NON VALE LA STESSA PERCENTUALE DI AUMENTO',items:[
  I('warn',[],560,430,'Occhio:'),
  VN('% DIVERSA',1300,420,'non vale la stessa percentuale',{fs:84,fill:RF_,sub:'DI AUMENTO',minw:760}),
  VT('CI ARRIVO TRA UN ATTIMO',1300,660,'Ci arrivo tra un attimo',AMB,40)]},
]);
// ---------- BLOCCO 8 ----------
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO AL 3 %',cap:'340,71 € × 3 % = CIRCA 10,22 €',items:[
  ...EQ(400,[['num','340,71 €','Trecentoquaranta euro'],['op','×','per zero virgola'],['num','3 %','per zero virgola'],['op','=','fa circa'],['num','10,22 €','dieci euro e ventidue',{fill:GF_}]],76,260),
  VT('ESEMPIO, NON PREVISIONE',960,640,'solo un esempio',AMB,40)]},
 {at:'La pensione passerebbe',top:'NUOVA PENSIONE',cap:'DA 340,71 € A CIRCA 351 € AL MESE',items:[
  ...EQ(420,[['num','340,71 €','La pensione passerebbe'],['op','+',['La pensione passerebbe',0.5]],['num','10,22 €',['La pensione passerebbe',0.9],{fill:GF_}],['op','=','a circa trecentocinquantuno'],['num','≈ 351 €','a circa trecentocinquantuno',{fill:AMB}]],76,260),
  VT('AL MESE',960,640,'al mese',GF_,44)]},
]);
// ---------- BLOCCO 9 ----------
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IN UN ANNO',cap:'10,22 € × 13 MENSILITÀ = CIRCA 133 € IN PIÙ',items:[
  ...EQ(400,[['num','10,22 €','In un anno'],['op','×','con tredici'],['num','13','con tredici',{sub:'MENSILITÀ'}],['op','=','sono circa'],['num','≈ 133 €','centotrentatré euro',{fill:GF_}]],76,260)]},
 {at:'Pochi, ma',top:'POCHI, MA CONTANO',cap:'PER CHI VIVE DI QUESTO ASSEGNO OGNI EURO CONTA',items:[
  I('chk',[100],560,430,'Pochi, ma'),
  VT('PER CHI VIVE DI QUESTO ASSEGNO',1250,430,'per chi vive',AMB,40)]},
 {at:'E su una cifra',top:'NIENTE FASCE',cap:'SU UNA CIFRA COSÌ BASSA NON SCATTANO LE FASCE',items:[
  VN('FASCE',560,400,'non scattano le fasce',{fs:100,sub:'100 % · 90 % · 75 %'}),
  I('cross',[190,110],560,400,['non scattano le fasce',0.5]),
  VT('RIDUCONO LE PENSIONI ALTE',1380,430,'pensioni alte',AMB,40)]},
]);
// ---------- BLOCCO 10 ----------
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PRIMA TRAPPOLA',cap:'L’ACCOMPAGNAMENTO NON SEGUE IL 3 %',items:[
  I('circ',['1',RF_],460,420,'Prima trappola'),
  VN('3 %',1130,400,'non segue il tre per cento',{fs:130,sub:'NON LO SEGUE'}),
  I('cross',[190,110],1130,400,['non segue il tre per cento',0.2])]},
 {at:'L’Inps usa un altro indice',top:'UN ALTRO INDICE',cap:'INDICE DELLE RETRIBUZIONI DEGLI OPERAI',items:[
  I('doc',['INDICE DI RIVALUTAZIONE',700,320,undefined,36],560,440,'L’Inps usa un altro indice'),
  VT('RETRIBUZIONI DEGLI OPERAI',1410,440,'delle retribuzioni degli operai',AMB,40)]},
 {at:'Nel duemilaventisei è passato',top:'ACCOMPAGNAMENTO 2025-2026',cap:'DA 542,02 € A 552,57 € AL MESE',items:[
  VN('542,02 €',500,400,'da cinquecentoquarantadue',{fs:100,sub:'2025'}),
  I('arR',[],960,400,'a cinquecentocinquantadue'),
  VN('552,57 €',1420,400,'e cinquantasette',{fs:100,fill:GF_,sub:'2026'})]},
]);
// ---------- BLOCCO 11 ----------
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ATTENZIONE AL TITOLO',cap:'CON L’ACCOMPAGNAMENTO IL CONTO NON È IL 3 % DI 552 €',items:[
  VN('3 %',560,400,'aumento del tre per cento',{fs:130,sub:'TITOLO'}),
  I('doc',['ACCOMPAGNAMENTO',560,300,undefined,36],1330,420,'hai l’accompagnamento'),
  I('cross',[250,120],1330,420,['il conto non è',0.5])]},
 {at:'Il suo importo del duemilaventisette',top:'IMPORTO 2027',cap:'DIPENDE DA UN ALTRO INDICE, NON ANCORA PUBBLICATO',items:[
  VN('2027',560,400,'importo del duemilaventisette',{fs:130,sub:'ACCOMPAGNAMENTO'}),
  VT('ALTRO INDICE',1330,380,'quell’altro indice',AMB,44),
  I('stamp',['NON ANCORA PUBBLICATO',RED_,48],1330,600,'non lo ha ancora pubblicato')]},
]);
// ---------- BLOCCO 12 ----------
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SECONDA TRAPPOLA',cap:'I LIMITI DI REDDITO',items:[
  I('circ',['2','url(#g_head)'],460,420,'Seconda trappola'),
  VN('LIMITI',1130,400,'i limiti di reddito',{fs:110,sub:'DI REDDITO'}),
  VT('PUÒ COSTARE CARA',1130,640,'può costare cara',RF_,44)]},
 {at:'Anche loro vengono aggiornati',top:'ANCHE I LIMITI SI AGGIORNANO',cap:'NEL 2026 + 1,3 % · FINO A 20.029,55 € PER L’INVALIDITÀ TOTALE',items:[
  VN('+ 1,3 %',560,400,'più uno virgola tre',{fs:130,sub:'LIMITI · 2026'}),
  I('arR',[],940,400,'fino a ventimilaventinove'),
  VN('20.029,55 €',1400,400,'ventimilaventinove',{fs:90,fill:AMB,sub:'INVALIDITÀ TOTALE',minw:760}),
  VT('PERCENTUALE A PARTE',960,640,'percentuale a parte',GF_,44)]},
]);
// ---------- BLOCCO 13 ----------
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PERCHÉ CONTA?',cap:'SE IL TUO REDDITO SUPERA IL LIMITE, PERDI LA PRESTAZIONE',items:[
  I('q',[100],560,420,'Perché conta?'),
  VN('REDDITO',1100,330,'il tuo reddito supera',{fs:96,sub:'SOPRA IL LIMITE'}),
  I('stamp',['PERDI LA PRESTAZIONE',RED_,52],1100,600,['perdi la prestazione',-0.6])]},
 {at:'Anche un piccolo aumento',top:'ATTENZIONE',cap:'ANCHE UN PICCOLO AUMENTO PUÒ FARTI SUPERARE LA SOGLIA',items:[
  I('warn',[],560,430,'Anche un piccolo aumento'),
  VT('AUMENTO DI UN’ALTRA PENSIONE',1300,430,'un’altra pensione',AMB,40),
  VT('SOGLIA SUPERATA',1300,640,['superare la soglia',-0.7],RF_,44)]},
 {at:'Controlla ogni anno',top:'CONTROLLA OGNI ANNO',cap:'IL TUO REDDITO RISPETTO AL LIMITE',items:[
  I('chk',[100],560,430,'Controlla ogni anno'),
  VN('REDDITO ≤ LIMITE',1250,430,'rispetto al limite',{fs:80,fill:GF_,sub:'OGNI ANNO'})]},
]);
// ---------- BLOCCO 14 ----------
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ASSEGNO MENSILE',cap:'SOGLIA ANCORA PIÙ STRETTA: 5.852,21 € ALL’ANNO',items:[
  VN('5.852,21 €',960,380,'cinquemilaottocentocinquantadue',{fs:150,fill:RF_,sub:'LIMITE ANNUO · ASSEGNO MENSILE',minw:1000}),
  VT('ANCORA PIÙ STRETTA',960,640,'ancora più stretta',AMB,48)]},
 {at:'Qui basta poco',top:'BASTA POCO',cap:'BASTA POCO PER SUPERARLA',items:[
  I('warn',[],960,420,'Qui basta poco'),
  VT('SOGLIA FACILE DA SUPERARE',960,640,['Qui basta poco',0.2],RF_,44)]},
 {at:'E dopo il test',top:'DOPO IL TEST',cap:'IL CASO DEI 45 CENTESIMI, PROMESSO!',items:[
  VN('0,45 €',960,380,'quarantacinque centesimi',{fs:150,fill:RF_,sub:'IL CASO PROMESSO'}),
  VT('DOPO IL TEST',960,640,'dopo il test',AMB,44)]},
]);
// ---------- BLOCCO 15 ----------
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TERZA TRAPPOLA: L’ETÀ',cap:'A 67 ANNI LA PRESTAZIONE SI TRASFORMA',items:[
  I('circ',['3',RF_],440,420,'Terza trappola'),
  VN('67 ANNI',1100,380,'sessantasette anni',{fs:130,sub:'ETÀ'}),
  VT('PENSIONE E ASSEGNO',1100,640,'pensione di inabilità',AMB,44)]},
 {at:'si trasformano in assegno',top:'ASSEGNO SOCIALE SOSTITUTIVO',cap:'SI TRASFORMANO IN ASSEGNO SOCIALE SOSTITUTIVO',items:[
  I('doc',['PENSIONE / ASSEGNO',560,300,undefined,36],480,430,'si trasformano'),
  I('arR',[],900,430,['in assegno sociale',-0.3]),
  I('doc',['ASSEGNO SOCIALE',560,300,undefined,36],1400,430,['in assegno sociale',0.3])]},
 {at:'L’importo base',top:'IMPORTO BASE 2026',cap:'ASSEGNO SOCIALE: 546,24 € AL MESE',items:[
  VN('546,24 €',960,380,'cinquecentoquarantasei',{fs:150,fill:GF_,sub:'ASSEGNO SOCIALE · 2026'})]},
]);
// ---------- BLOCCO 16 ----------
SPECS[16]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DOPO I 67 ANNI',cap:'REGOLE DI REDDITO DIVERSE, CHE GUARDANO ANCHE IL CONIUGE',items:[
  VN('IMPORTO',560,400,'L’importo può salire',{fs:96,fill:GF_,sub:'PUÒ SALIRE',minw:640}),
  VT('REGOLE DI REDDITO DIVERSE',1420,380,'regole di reddito diverse',AMB,40),
  VT('GUARDANO ANCHE IL CONIUGE',1420,520,['che guardano',-0.2],AMB,40)]},
 {at:'Se ti avvicini',top:'SE TI AVVICINI AI 67 ANNI',cap:'CHIEDI ALL’INPS COSA CAMBIA NEL TUO CASO, O A UN PATRONATO',items:[
  VN('67 ANNI',560,400,'ai sessantasette anni',{fs:110,sub:'SE TI AVVICINI'}),
  I('br',['inps.it',620,300],1330,420,'chiedi all’Inps'),
  VT('O A UN PATRONATO',1330,640,'o a un patronato',GF_,44)]},
 {at:'Ora, il test!',top:'ORA, IL TEST!',cap:'TRE DOMANDE: VERO O FALSO',items:[
  I('q',[110],960,430,'Ora, il test!')]},
]);
// ---------- BLOCCO 17 ----------
SPECS[17]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TEST · DOMANDA 1',cap:'L’ACCOMPAGNAMENTO AUMENTA SEMPRE DEL 3 %?',items:[
  I('circ',['1',GF_],440,400,'Tre domande'),
  VN('3 %',1100,400,'del tre per cento',{fs:130,sub:'COME LE PENSIONI'}),
  VT('VERO O FALSO?',1100,640,'Vero o falso?',AMB,48)]},
 {at:'Falso! Segue',top:'RISPOSTA',cap:'FALSO: SEGUE UN ALTRO INDICE, NON ANCORA PUBBLICATO',items:[
  I('vf',[false],560,420,'Falso! Segue'),
  VT('ALTRO INDICE',1330,380,'un altro indice',AMB,44),
  VT('RETRIBUZIONI DEGLI OPERAI',1330,520,'retribuzioni degli operai',AMB,40),
  I('stamp',['NON ANCORA PUBBLICATO',RED_,44],1330,680,'ancora pubblicato')]},
]);
// ---------- BLOCCO 18 ----------
SPECS[18]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TEST · DOMANDA 2',cap:'LA PERCENTUALE LA DECIDE L’INPS A GENNAIO?',items:[
  I('circ',['2','url(#g_head)'],440,400,'Due:'),
  VN('INPS',1100,400,'decide l’Inps',{fs:130,sub:'A GENNAIO?'}),
  VT('VERO O FALSO?',1100,640,'Vero o falso?',AMB,48)]},
 {at:'Falso! La fissa',top:'RISPOSTA',cap:'FALSO: LA FISSA UN DECRETO DEI MINISTERI, DI SOLITO A NOVEMBRE',items:[
  I('vf',[false],560,420,'Falso! La fissa'),
  I('doc',['DECRETO DEI MINISTERI',640,300,undefined,34],1330,420,'un decreto dei ministeri'),
  VT('DI SOLITO A NOVEMBRE',1330,640,'di solito a novembre',AMB,44)]},
 {at:'L’Inps la applica',top:'L’INPS LA APPLICA',cap:'A GENNAIO, CON UN POSSIBILE CONGUAGLIO',items:[
  VN('GENNAIO',560,400,'L’Inps la applica',{fs:110,fill:GF_,sub:'APPLICAZIONE',minw:760}),
  VT('POSSIBILE CONGUAGLIO',1420,430,'possibile conguaglio',AMB,44)]},
]);
// ---------- BLOCCO 19 ----------
SPECS[19]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TEST · DOMANDA 3',cap:'SE LA PENSIONE SALE DI 10 €, IL TOTALE SALE DI 10 €?',items:[
  I('circ',['3',RF_],440,400,'Tre:'),
  VN('+ 10 €',1100,400,'sale di dieci euro',{fs:130,fill:GF_,sub:'LA PENSIONE'}),
  VT('VERO O FALSO?',1100,640,'Vero o falso?',AMB,48)]},
 {at:'Falso! Adesso',top:'RISPOSTA',cap:'FALSO: NEL 2026 IL TOTALE È SALITO DI SOLI 45 CENTESIMI',items:[
  I('vf',[false],560,420,'Falso! Adesso'),
  VN('0,45 €',1330,400,'quarantacinque centesimi',{fs:130,fill:RF_,sub:'NEL 2026'}),
  VT('ADESSO TI MOSTRO UN CASO',1330,640,'ti mostro un caso',AMB,44)]},
]);
// ---------- BLOCCO 20 ----------
SPECS[20]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA CHICCA',cap:'L’INCREMENTO AL MILIONE: UNA SOMMA IN PIÙ',items:[
  VT('ECCO LA CHICCA',960,300,'Ecco la chicca',RF_,56),
  VN('INCREMENTO AL MILIONE',960,500,['Esiste una somma',0.4],{fs:80,fill:GF_,sub:'SOMMA IN PIÙ',minw:1400}),
  VT('UNA SOMMA IN PIÙ',960,740,['Esiste una somma',0.9],AMB,44)]},
 {at:'per gli invalidi totali',top:'PER CHI?',cap:'INVALIDI TOTALI TRA I 18 E I 65 ANNI, REDDITI MOLTO BASSI',items:[
  VN('18 – 65',560,400,'tra i diciotto',{fs:110,sub:'ANNI'}),
  VT('INVALIDI TOTALI',1330,380,'invalidi totali',AMB,44),
  VT('REDDITI MOLTO BASSI',1330,520,'redditi molto bassi',RF_,44)]},
 {at:'Vediamo cosa è successo',top:'2025 · 2026',cap:'COSA È SUCCESSO TRA IL 2025 E IL 2026',items:[
  VN('2025',560,400,'tra il duemilaventicinque',{fs:130,sub:'PRIMA'}),
  I('arR',[],960,400,['e il duemilaventisei',-0.3]),
  VN('2026',1400,400,'e il duemilaventisei',{fs:130,fill:GF_,sub:'DOPO'})]},
]);
// ---------- BLOCCO 21 ----------
SPECS[21]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'NEL 2025',cap:'PENSIONE 336,00 € + INCREMENTO 411,84 €',items:[
  ...EQ(400,[['num','336,00 €','la pensione era',{sub:'PENSIONE'}],['op','+','e l’incremento'],['num','411,84 €','quattrocentoundici',{fill:AMB,sub:'INCREMENTO'}]],68,300)]},
 {at:'Totale:',top:'TOTALE 2025',cap:'TOTALE: 747,84 € AL MESE',items:[
  VN('747,84 €',960,380,'settecentoquarantasette',{fs:150,fill:GF_,sub:'TOTALE · 2025'}),
  VT('SEGNATI QUESTO NUMERO',960,660,'Segnati questo numero',RF_,48)]},
]);
// ---------- BLOCCO 22 ----------
SPECS[22]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'NEL 2026',cap:'LA PENSIONE SALE A 340,71 €',items:[
  VN('340,71 €',960,380,'trecentoquaranta euro',{fs:130,fill:GF_,sub:'PENSIONE · 2026'}),
  VT('TI ASPETTI UN TOTALE PIÙ ALTO?',960,640,'Ti aspetti un totale',AMB,44)]},
 {at:'Invece l’incremento',top:'INVECE',cap:'L’INCREMENTO SCENDE A 407,58 €',items:[
  VN('407,58 €',960,380,'quattrocentosette',{fs:130,fill:RF_,sub:'INCREMENTO · SCENDE'})]},
 {at:'Totale: settecentoquarantotto',top:'TOTALE 2026',cap:'TOTALE: 748,29 € AL MESE',items:[
  VN('748,29 €',960,380,'settecentoquarantotto',{fs:150,fill:GF_,sub:'TOTALE · 2026'})]},
]);
// ---------- BLOCCO 23 ----------
SPECS[23]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA DIFFERENZA',cap:'748,29 € − 747,84 € = 0,45 €',items:[
  ...EQ(400,[['num','748,29 €','settecentoquarantotto'],['op','−','meno'],['num','747,84 €','settecentoquarantasette'],['op','=','Quarantacinque centesimi'],['num','0,45 €','Quarantacinque centesimi',{fill:RF_}]],70,260)]},
 {at:'La pensione è cresciuta',top:'DOVE VANNO I SOLDI',cap:'LA PENSIONE CRESCE DI 4,71 €, L’INCREMENTO SCENDE DI 4,26 €',items:[
  VN('+ 4,71 €',560,400,'quattro euro e settantuno',{fs:120,fill:GF_,sub:'LA PENSIONE CRESCE'}),
  VN('− 4,26 €',1380,400,'sceso di quattro euro e ventisei',{fs:120,fill:RF_,sub:'L’INCREMENTO SCENDE'})]},
]);
// ---------- BLOCCO 24 ----------
SPECS[24]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PERCHÉ?',cap:'L’INCREMENTO ARRIVA FINO A UN TETTO DI REDDITO',items:[
  I('q',[100],440,420,'Perché?'),
  VN('TETTO',1100,380,'un tetto di reddito',{fs:110,sub:'DI REDDITO'}),
  VT('9.727,77 € ALL’ANNO · 2026',1100,640,'novemilasettecentoventisette',AMB,44)]},
 {at:'Se la pensione sale',top:'COME FUNZIONA',cap:'SE LA PENSIONE SALE, L’INCREMENTO SCENDE E RESTA NEL TETTO',items:[
  VN('PENSIONE',520,400,'Se la pensione sale',{fs:90,fill:GF_,sub:'SALE',minw:640}),
  I('arR',[],945,400,'l’incremento fa'),
  VN('INCREMENTO',1420,400,'un passo indietro',{fs:90,fill:AMB,sub:'FA UN PASSO INDIETRO',minw:760}),
  VT('RESTA DENTRO IL TETTO',960,660,'dentro il tetto',GF_,44)]},
]);
// ---------- BLOCCO 25 ----------
SPECS[25]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SENZA ALTRI REDDITI',cap:'VALE PER CHI NON HA ALTRI REDDITI',items:[
  I('chk',[100],560,420,'Vale per chi'),
  VT('NESSUN ALTRO REDDITO',1250,420,'non ha altri redditi',AMB,44)]},
 {at:'Se sei sposato',top:'SE SEI SPOSATO',cap:'TETTO 16.828,89 € · SI GUARDANO ANCHE I REDDITI DEL CONIUGE',items:[
  VN('16.828,89 €',560,400,'sedicimilaottocentoventotto',{fs:90,fill:AMB,sub:'TETTO · SE SEI SPOSATO',minw:760}),
  VT('REDDITI DEL CONIUGE',1380,420,'redditi del coniuge',GF_,44)]},
 {at:'Nel duemilaventisette vedremo',top:'NEL 2027',cap:'NEL 2027 VEDREMO QUANTO CAMBIA',items:[
  VN('2027',960,400,'Nel duemilaventisette vedremo',{fs:140,sub:'NUOVI IMPORTI'}),
  VT('QUANDO ESCONO I NUOVI IMPORTI',960,640,'i nuovi importi',AMB,44)]},
]);
// ---------- BLOCCO 26 ----------
SPECS[26]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COME CONTROLLI',cap:'ENTRA SU MAI INPS CON SPID O CARTA D’IDENTITÀ ELETTRONICA',items:[
  I('br',['inps.it',700,320],560,420,'Come controlli'),
  VT('MAI INPS',1380,360,'Mai Inps',GF_,48),
  VT('SPID O CARTA D’IDENTITÀ',1380,500,'Spid o la carta',AMB,44)]},
 {at:'guarda il cedolino',top:'IL CEDOLINO DI GENNAIO',cap:'IMPORTO BASE, EVENTUALE INCREMENTO, ALTRE VOCI',items:[
  I('doc',['CEDOLINO DI GENNAIO',560,340,undefined,34],560,430,'il cedolino di gennaio'),
  I('row',['IMPORTO BASE',520,true],1380,360,'importo base'),
  I('row',['EVENTUALE INCREMENTO',660,true],1380,460,['importo base',0.7]),
  I('row',['ALTRE VOCI',520,true],1380,560,['importo base',1.4])]},
 {at:'Confrontalo con quello',top:'CONFRONTA',cap:'CONFRONTALO CON QUELLO DI DICEMBRE',items:[
  VN('DICEMBRE',560,400,'Confrontalo',{fs:90,sub:'CEDOLINO',minw:720}),
  VN('GENNAIO',1400,400,['Confrontalo',0.3],{fs:90,fill:GF_,sub:'CEDOLINO',minw:720})]},
]);
// ---------- BLOCCO 27 ----------
SPECS[27]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SE NON TORNA',cap:'RIFAI IL CONTO: IMPORTO BASE × PERCENTUALE',items:[
  ...EQ(420,[['num','IMPORTO','rifai il conto',{sub:'BASE'}],['op','×',['rifai il conto',0.4]],['num','%',['rifai il conto',0.8],{sub:'PERCENTUALE'}]],80,300)]},
 {at:'poi controlla',top:'POI CONTROLLA',cap:'SE HAI L’INCREMENTO E SE IL TETTO È CAMBIATO',items:[
  I('chk',[100],440,420,'poi controlla'),
  VT('HAI L’INCREMENTO?',1250,380,'hai l’incremento',AMB,44),
  VT('IL TETTO È CAMBIATO?',1250,520,'il tetto è cambiato',AMB,44)]},
 {at:'Se hai ancora dubbi',top:'ANCORA DUBBI?',cap:'PORTA IL CEDOLINO A UN PATRONATO: DI SOLITO È GRATUITO',items:[
  I('q',[100],440,420,'Se hai ancora dubbi'),
  I('doc',['CEDOLINO',520,300,undefined,36],1100,420,'porta il cedolino'),
  VT('PATRONATO · DI SOLITO GRATUITO',1100,650,'patronato',GF_,40)]},
]);
// ---------- BLOCCO 28 ----------
SPECS[28]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RICAPITOLO',cap:'UNO: LA PERCENTUALE LA FISSA UN DECRETO A NOVEMBRE',items:[
  I('circ',['1',GF_],440,400,'Uno:'),
  VT('DECRETO A NOVEMBRE',1130,380,'un decreto a novembre',AMB,44),
  VT('L’INPS APPLICA A GENNAIO',1130,520,['un decreto a novembre',0.8],GF_,44)]},
 {at:'Due:',top:'DUE',cap:'L’ACCOMPAGNAMENTO HA UN ALTRO INDICE',items:[
  I('circ',['2','url(#g_head)'],440,420,'Due:'),
  VT('ALTRO INDICE',1130,420,['Due:',0.5],AMB,48)]},
 {at:'Tre:',top:'TRE',cap:'INCREMENTO AL MILIONE: IL TOTALE CRESCE POCHISSIMO',items:[
  I('circ',['3',RF_],440,400,'Tre:'),
  VN('0,45 €',1130,400,'quarantacinque centesimi',{fs:130,fill:RF_,sub:'IL TOTALE · 2026'}),
  VT('CRESCE POCHISSIMO',1130,640,'salire pochissimo',AMB,44)]},
]);
// ---------- BLOCCO 29 ----------
SPECS[29]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'METTI MI PIACE',cap:'METTI MI PIACE E ISCRIVITI A CONTI IN PENSIONE',items:[
  VT('MI PIACE',520,420,'metti mi piace',GF_,56),
  I('btn',['ISCRIVITI'],1150,420,'iscriviti'),
  I('bell',[],1650,420,['iscriviti',0.5])]},
 {at:'a novembre',top:'A NOVEMBRE',cap:'QUANDO ESCE IL DECRETO TI DICO LA PERCENTUALE UFFICIALE',items:[
  I('doc',['DECRETO',520,300,undefined,36],560,420,'quando esce il decreto'),
  I('arR',[],960,420,'ti dico'),
  VN('% UFFICIALE',1400,400,'percentuale ufficiale',{fs:90,fill:GF_,sub:'NOVEMBRE',minw:700})]},
 {at:'Scrivimi nei commenti',top:'SCRIVIMI',cap:'SCRIVIMI NEI COMMENTI COSA PRENDI TU',items:[
  I('bubble',[700,300],960,420,'Scrivimi nei commenti'),
  VT('COSA PRENDI TU?',960,700,'cosa prendi tu',AMB,48)]},
]);
// ---------- BLOCCO 30 (slide finale con il disclaimer, come video 3; centro-basso e destra-basso LIBERI per la schermata finale) ----------
SPECS[30]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'VERIFICA SEMPRE',cap:'VERIFICA SEMPRE SUI CANALI UFFICIALI: INPS.IT. GRAZIE PER AVER GUARDATO!',capSize:42,items:[
  I('dbg',[1060,330],1280,330,'Le informazioni di questo video'),
  I('dline',['INFORMAZIONI A SCOPO DIVULGATIVO','#fff',32],1280,320,'scopo divulgativo'),
  I('dline',['NON SOSTITUISCE UN PATRONATO O L’INPS','#7FF0D2',30],1280,380,'non sostituiscono'),
  I('dline',['IMPORTI 2026 UFFICIALI · AL 3 % SOLO ESEMPI','#FFB838',30],1280,440,'Gli importi del duemilaventisei'),
  I('br',['inps.it',600,330],400,330,'Verifica sempre'),
  I('row',['CANALI UFFICIALI',460,true],400,360,'inps punto it'),
  I('med',[],200,700,'Verifica sempre',1.2),I('medm',[],360,700,['Verifica sempre',1.6],0.45)]},
]);
