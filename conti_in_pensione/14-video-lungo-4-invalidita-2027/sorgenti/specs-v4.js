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
