// ===== V3 blocchi 6-30: ogni elemento compare quando la voce lo dice =====
const SPECS={};
const GF_='url(#g_badge)',RF_='url(#g_red)',PF_='url(#g_paper)',DF_='#0B4A50';
const VT=(s,x,y,at,fill,fs)=>I('tag',[s,fill||AMB,(fill&&fill!==AMB)?'#fff':'#5A3300',fs||44],x,y,at);
const VN=(s,x,y,at,o)=>{o=o||{};return I('num',[s,o.fs||76,o.fill||PF_,o.sub,o.subfill,o.minw],x,y,at);};
const VO=(s,x,y,at)=>I('op',[s],x,y,at);

// ---------- BLOCCO 6 ----------
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO SUBITO',cap:'ESEMPIO AL 3 %: UN NUMERO TONDO, NON UNA PREVISIONE',items:[
  VN('3 %',960,400,'Esempio con',{fs:150,sub:'ESEMPIO'}),
  VT('UN NUMERO TONDO, NON UNA PREVISIONE',960,650,'un numero tondo'),
  VT('IMPORTI LORDI AL MESE',960,770,'Importi lordi',GF_)]},
 {at:'Pensione da mille euro',top:'PENSIONE DA 1.000 €',cap:'1.000 € × 3 % = 30 €  →  NUOVA PENSIONE: 1.030 €',items:[
  ...EQ(330,[['num','1.000 €','Pensione da mille'],['op','×','il tre per cento di mille'],['num','3 %','il tre per cento di mille'],['op','=','fa trenta'],['num','30 €','fa trenta',{fill:GF_}]]),
  ...EQ(640,[['num','1.000 €',['Nuova pensione',0],{fs:64}],['op','+',['Nuova pensione',0.5]],['num','30 €',['Nuova pensione',0.8],{fs:64,fill:GF_}],['op','=',['milletrenta',-0.5]],['num','1.030 €','milletrenta',{fs:64,fill:AMB}]],64,260),
  VT('NUOVA PENSIONE',960,775,'Nuova pensione',GF_,40)]},
]);
// ---------- BLOCCO 7 ----------
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA NOSTRA MARTA',cap:'MARTA: 1.500 € × 3 % = 45 € IN PIÙ AL MESE',items:[
  I('med',[],170,440,'la nostra Marta',0.6),
  ...EQ(440,[['num','1.500 €','Pensione da millecinquecento'],['op','×','il tre per cento'],['num','3 %','il tre per cento'],['op','=','fa quarantacinque'],['num','45 €','fa quarantacinque',{fill:GF_}]],76,260).map(it=>({...it,x:it.x+90})),
  VT('45 EURO IN PIÙ',1500,640,'quarantacinque euro in più',GF_,40)]},
 {at:'Nuova pensione',top:'NUOVA PENSIONE',cap:'1.500 € + 45 € = 1.545 € AL MESE',items:[
  ...EQ(470,[['num','1.500 €','Nuova pensione'],['op','+',['Nuova pensione',0.5]],['num','45 €',['Nuova pensione',0.9],{fill:GF_}],['op','=',['millecinquecentoquarantacinque',-0.5]],['num','1.545 €','millecinquecentoquarantacinque',{fill:AMB}]])]},
 {at:'Sono cinquecentoottantacinque',top:'IN UN ANNO',cap:'45 € × 13 MENSILITÀ = 585 € LORDI IN PIÙ ALL’ANNO',items:[
  VN('585 €',960,330,'Sono cinquecentoottantacinque',{fs:130,fill:GF_,sub:'LORDI IN PIÙ ALL’ANNO'}),
  ...EQ(660,[['num','45 €','con le tredici'],['op','×','con le tredici'],['num','13','con le tredici',{sub:'MENSILITÀ'}]],66,240)]},
]);
// ---------- BLOCCO 8 ----------
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONE DA 2.000 €',cap:'2.000 € × 3 % = 60 € IN PIÙ → 2.060 €',items:[
  ...EQ(330,[['num','2.000 €','Pensione da duemila'],['op','×','tre per cento esatto'],['num','3 %','tre per cento esatto'],['op','=','Sessanta euro'],['num','60 €','Sessanta euro',{fill:GF_}]]),
  VT('ANCORA FASCIA PIENA',960,560,'ancora fascia piena',GF_),
  VN('2.060 €',960,730,'duemilasessanta in tutto',{fs:80,fill:AMB,sub:'NUOVA PENSIONE'})]},
 {at:'Sono settecentoottanta',top:'IN UN ANNO',cap:'60 € × 13 = 780 € LORDI IN PIÙ IN UN ANNO',items:[
  ...EQ(380,[['num','60 €','Sono settecentoottanta'],['op','×','Sono settecentoottanta'],['num','13','Sono settecentoottanta',{sub:'MENSILITÀ'}]],66,240),
  VN('780 €',960,680,['Sono settecentoottanta',1.0],{fs:120,fill:GF_,sub:'LORDI IN PIÙ IN UN ANNO'})]},
 {at:'Fin qui è semplice',top:'ORA COMINCIA IL BELLO',cap:'FIN QUI È SEMPLICE, VERO? ORA COMINCIA IL BELLO!',items:[
  I('chk',[110],560,430,'Fin qui è semplice'),
  I('warn',[],1360,430,'Ora comincia il bello',0.9),
  VT('FIN QUI È SEMPLICE, VERO?',560,600,'vero?',GF_,40),
  VT('ORA COMINCIA IL BELLO!',1360,740,'Ora comincia il bello',RF_,40)]},
]);
// ---------- BLOCCO 9 ----------
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ATTENZIONE',cap:'OLTRE UNA CERTA CIFRA IL CONTO CAMBIA!',items:[
  I('warn',[],330,430,'Ma attenzione',0.85),
  I('seg',[500,110,GF_,'FINO A QUI: 3 %'],900,430,'oltre una certa cifra'),
  I('seg',[500,110,AMB,'OLTRE: MENO'],1500,430,'il conto cambia'),
  VT('IL CONTO CAMBIA!',1200,620,'il conto cambia',RF_)]},
 {at:'E non è l’unica',sh:0.45,top:'LE TRAPPOLE',cap:'NON È L’UNICA TRAPPOLA: PARTIAMO DALLA PRIMA, LE FASCE',items:[
  I('circ',['1',RF_],560,430,'unica trappola'),I('circ',['2','url(#g_head)'],960,430,'unica trappola',1),I('circ',['3',GF_],1360,430,'unica trappola',1),
  VT('LA PRIMA: LE FASCE',560,610,'partiamo dalla prima',RF_,40)]},
]);
// ---------- BLOCCO 10 ----------
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PRIMA TRAPPOLA: LE FASCE',cap:'LA PERCENTUALE NON VALE PER TUTTA LA PENSIONE ALLO STESSO MODO',items:[
  I('circ',['1',RF_],400,420,'Prima trappola'),
  VN('3 %',960,400,'la percentuale non vale',{fs:120,sub:'LA PERCENTUALE'}),
  VT('NON VALE ALLO STESSO MODO PER TUTTA LA PENSIONE',960,650,'per tutta la pensione',RF_,40)]},
 {at:'La legge divide',top:'LA LEGGE DIVIDE IN FASCE',cap:'LA LEGGE DIVIDE L’IMPORTO IN FASCE: PIÙ SALI, MENO TI VIENE RIVALUTATO',items:[
  I('seg',[360,120,GF_,'FASCIA 1'],560,380,'divide l’importo in fasce'),
  I('seg',[360,120,AMB,'FASCIA 2'],960,380,['divide l’importo in fasce',0.6]),
  I('seg',[360,120,RF_,'FASCIA 3'],1360,380,['divide l’importo in fasce',1.2]),
  VT('PIÙ SALI, MENO TI VIENE RIVALUTATO',960,640,'più sali, meno ti viene',GF_,44)]},
 {at:'Immagina tre gradini',top:'TRE GRADINI',cap:'TRE GRADINI: PIÙ SALI, PIÙ OGNI GRADINO RENDE DI MENO',items:[
  I('step',[340,150,GF_,'1'],620,760,'Immagina tre gradini'),I('step',[340,260,AMB,'2'],960,760,['Immagina tre gradini',0.7]),I('step',[340,370,RF_,'3'],1300,760,['Immagina tre gradini',1.4]),
  VT('PIÙ SALI, PIÙ OGNI GRADINO RENDE DI MENO',960,330,'più ogni gradino rende',GF_,40)]},
]);
// ---------- BLOCCO 11 ----------
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TRATTAMENTO MINIMO',cap:'LE FASCE SI MISURANO IN MULTIPLI DEL TRATTAMENTO MINIMO',items:[
  VT('MULTIPLI DEL TRATTAMENTO MINIMO',960,300,'in multipli del trattamento minimo',AMB,44),
  VN('611,85 €',960,540,'seicentoundici',{fs:130,fill:GF_,sub:'TRATTAMENTO MINIMO NEL 2026'})]},
 {at:'Prima fascia',top:'PRIMA FASCIA',cap:'PRIMA FASCIA: FINO A 4 × IL MINIMO → RIVALUTAZIONE PIENA, 100 %',items:[
  I('seg',[900,150,GF_,'FINO A 4 × IL MINIMO','PRIMA FASCIA'],960,400,'fino a quattro volte il minimo'),
  VN('100 %',960,700,'cento per cento',{fs:130,fill:GF_,sub:'RIVALUTAZIONE PIENA'})]},
]);
// ---------- BLOCCO 12 ----------
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE TRE FASCE',cap:'FASCIA 2: TRA 4 E 5 VOLTE IL MINIMO → 90 %   |   FASCIA 3: OLTRE 5 VOLTE → 75 %',capSize:40,items:[
  I('seg',[560,130,GF_,'FINO A 4 ×','FASCIA 1'],440,360,0.6),
  VN('100 %',440,640,0.9,{fs:90,fill:GF_,minw:300}),
  I('seg',[340,130,AMB,'4 × → 5 ×','FASCIA 2'],1000,360,'Seconda fascia'),
  VN('90 %',1000,640,'novanta per cento',{fs:90,fill:AMB,minw:300}),
  I('seg',[380,130,RF_,'OLTRE 5 ×','FASCIA 3'],1470,360,'Terza fascia'),
  VN('75 %',1470,640,'settantacinque per cento',{fs:90,fill:RF_,minw:300})]},
]);
// ---------- BLOCCO 13 ----------
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ATTENZIONE',cap:'LE FASCE SI APPLICANO ALLA PARTE DI IMPORTO, NON A TUTTA LA PENSIONE!',items:[
  I('warn',[],400,440,'Attenzione',0.85),
  VT('ALLA PARTE DI IMPORTO',1160,330,'alla parte di importo',GF_,46),
  VT('NON A TUTTA LA PENSIONE',1160,520,'non a tutta la pensione',RF_,46),
  I('cross',[40,40],1740,520,'non a tutta la pensione',0.9)]},
 {at:'Come per le tasse',top:'COME PER LE TASSE',cap:'SOLO LA PARTE CHE SUPERA LA SOGLIA È RIVALUTATA DI MENO',items:[
  I('seg',[840,130,GF_,'RESTA NELLA FASCIA PIENA'],520,420,'il resto resta nella fascia piena'),
  I('seg',[620,130,AMB,'RIVALUTATA DI MENO'],1450,420,'solo la parte che supera la soglia'),
  VT('LA SOGLIA',1040,640,'la soglia',RF_,40)]},
]);
// ---------- BLOCCO 14 ----------
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SOGLIE UFFICIALI 2026',cap:'TABELLA UFFICIALE INPS 2026: LE TRE SOGLIE',items:[
  VT('TABELLA UFFICIALE INPS 2026',960,250,'dalla tabella ufficiale dell’Inps',AMB,44),
  I('trow',[1500,'FINO A 2.413,60 €','100 %',GF_],960,420,'fino a duemilaquattrocentotredici'),
  I('trow',[1500,'DA 2.413,61 A 3.017,00 €','90 %',AMB],960,580,'Da lì a tremiladiciassette'),
  I('trow',[1500,'OLTRE 3.017,00 €','75 %',RF_],960,740,'Oltre tremiladiciassette')]},
]);
// ---------- BLOCCO 15 ----------
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'L’AUMENTO REALE DEL 2026',cap:'STESSA PERCENTUALE, AUMENTI DIVERSI',items:[
  VN('1,4 %',420,430,'Con l’uno virgola quattro',{fs:130,sub:'LA RIVALUTAZIONE 2026',minw:520}),
  I('trow',[860,'FASCIA 1','1,400 %',GF_],1280,330,'uno virgola quattro nella prima'),
  I('trow',[860,'FASCIA 2','1,260 %',AMB],1280,480,'uno virgola ventisei'),
  I('trow',[860,'FASCIA 3','1,050 %',RF_],1280,630,'uno virgola zero cinquanta'),
  VT('STESSA PERCENTUALE, AUMENTI DIVERSI',960,800,'Ecco perché',GF_,44)]},
]);
// ---------- BLOCCO 16 ----------
SPECS[16]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE SOGLIE DEL 2027',cap:'SOGLIE 2027 NON ANCORA PUBBLICATE: NEGLI ESEMPI USO VALORI APPROSSIMATI',capSize:42,items:[
  VN('?',520,420,'non sono ancora pubblicate',{fs:150,sub:'NON PUBBLICATE',minw:560}),
  VN('≈ 2.450 €',1300,330,'duemilaquattrocentocinquanta',{fs:76,minw:560,fill:GF_}),
  VN('≈ 3.060 €',1300,500,'tremilasessanta',{fs:76,minw:560,fill:AMB}),
  VT('NEGLI ESEMPI: VALORI APPROSSIMATI',960,700,'Negli esempi uso valori approssimati',GF_,44),
  VT('ERRORE: POCHI EURO. IL METODO NON CAMBIA',960,810,'L’errore è di pochi euro',AMB,44)]},
]);
// ---------- BLOCCO 17 ----------
SPECS[17]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONE DA 3.000 €',cap:'3.000 €: QUI SCATTA LA SECONDA FASCIA',items:[
  VN('3.000 €',960,300,'Pensione da tremila',{fs:110,fill:PF_}),
  I('seg',[760,120,GF_,'FINO A ≈ 2.450 €','FASCIA PIENA: 3 %'],700,560,['Pensione da tremila',0.5]),
  I('seg',[300,120,AMB,'≈ 550 €','SECONDA FASCIA'],1350,560,['Pensione da tremila',1.0]),
  VT('QUI SCATTA LA SECONDA FASCIA!',960,800,'Qui scatta la seconda fascia',RF_,44)]},
 {at:'Fino a circa duemilaquattrocentocinquanta euro, il tre',top:'LA PRIMA PARTE',cap:'2.450 € × 3 % = 73,50 €',items:[
  ...EQ(430,[['num','2.450 €','Fino a circa duemilaquattrocentocinquanta euro, il tre'],['op','×','il tre per cento pieno'],['num','3 %','il tre per cento pieno'],['op','=','settantatré euro e mezzo'],['num','73,50 €','settantatré euro e mezzo',{fill:GF_}]]),
  VT('CIRCA SETTANTATRÉ EURO E MEZZO',960,650,'circa settantatré euro e mezzo',GF_,44)]},
 {at:'Sui restanti',top:'LA SECONDA PARTE',cap:'550 € × 90 % DI 3 % = 550 € × 2,7 %',items:[
  ...EQ(380,[['num','550 €','Sui restanti'],['op','×','conta il novanta'],['num','2,7 %','due virgola sette',{fill:AMB}]]),
  VT('90 % DI 3 % = 2,7 %',960,620,'conta il novanta per cento',AMB,48)]},
]);
// ---------- BLOCCO 18 ----------
SPECS[18]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TOTALE',cap:'73,50 € + 15 € = CIRCA 88 € LORDI IN PIÙ. NON 90!',items:[
  ...EQ(380,[['num','73,50 €','settantatré euro e mezzo'],['op','+','più circa quindici'],['num','15 €','più circa quindici'],['op','=','fa circa ottantotto'],['num','88 €','fa circa ottantotto',{fill:GF_}]]),
  VT('CIRCA 88 EURO LORDI IN PIÙ',960,610,'euro lordi in più',GF_,44),
  VN('90 €',560,780,'Non novanta',{fs:70,minw:240}),I('cross',[110,60],560,780,['Non novanta',0.15]),
  VT('NON NOVANTA!',1100,780,'Non novanta',RF_,44)]},
 {at:'La pensione diventa',sh:0.4,top:'LA NUOVA PENSIONE',cap:'3.000 € + 88 € = CIRCA 3.088 €',items:[
  ...EQ(430,[['num','3.000 €','La pensione diventa'],['op','+',['La pensione diventa',0.4]],['num','88 €',['La pensione diventa',0.8],{fill:GF_}],['op','=','circa tremilaottantotto'],['num','3.088 €','circa tremilaottantotto',{fill:AMB}]])]},
 {at:'L’aumento in percentuale',top:'IN PERCENTUALE',cap:'L’AUMENTO È CIRCA 2,9 %, NON 3 %',items:[
  VN('2,9 %',640,430,'circa due virgola nove',{fs:150,fill:GF_,sub:'AUMENTO REALE'}),
  VN('3 %',1280,430,'non tre',{fs:150,minw:420}),I('cross',[130,80],1280,430,['non tre',0.3])]},
]);
// ---------- BLOCCO 19 ----------
SPECS[19]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONE DA 4.000 €',cap:'4.000 €: SCATTANO TUTTE E TRE LE FASCE',items:[
  VN('4.000 €',960,260,'Pensione da quattromila',{fs:90}),
  I('trow',[1560,'FASCIA 1:  2.450 € × 3 %  =','73,50 €',GF_],960,450,'Prima, circa'),
  I('trow',[1560,'FASCIA 2:  610 € × 2,7 %  =','16,50 €',AMB],960,610,'Seconda, novanta'),
  I('trow',[1560,'FASCIA 3:  940 € × 2,25 %  =','21 €',RF_],960,770,'Terza, settantacinque')]},
]);
// ---------- BLOCCO 20 ----------
SPECS[20]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TOTALE',cap:'73,50 + 16,50 + 21 = CIRCA 111 € LORDI IN PIÙ',items:[
  ...EQ(380,[['num','73,50 €',0.6,{fs:56}],['op','+',0.9],['num','16,50 €',1.2,{fs:56}],['op','+',1.5],['num','21 €',1.8,{fs:56}],['op','=','Totale: circa centoundici'],['num','111 €','centoundici',{fs:56,fill:GF_}]],56,200),
  VT('CIRCA 111 EURO LORDI IN PIÙ',960,590,'euro lordi in più',GF_,44)]},
 {at:'La pensione sale',top:'LA NUOVA PENSIONE',cap:'4.000 € + 111 € = CIRCA 4.111 €',items:[
  VN('4.111 €',960,430,'quattromilacentoundici',{fs:150,fill:AMB,sub:'NUOVA PENSIONE'})]},
 {at:'In percentuale',top:'IN PERCENTUALE',cap:'IL 3 % DEL TITOLO SI È RIDOTTO A 2,8 %, SENZA CHE NESSUNO TE LO DICA',capSize:40,items:[
  VN('2,8 %',640,400,'due virgola otto',{fs:150,fill:GF_,sub:'AUMENTO REALE'}),
  VN('3 %',1280,400,'il tre per cento del titolo',{fs:150,minw:420}),I('cross',[130,80],1280,400,['il tre per cento del titolo',0.3]),
  VT('SI È RIDOTTO, SENZA CHE NESSUNO TE LO DICA!',960,720,'senza che nessuno te lo dica',RF_,44)]},
]);
// ---------- BLOCCO 21 ----------
SPECS[21]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE PENSIONI AL MINIMO',cap:'611,85 € × 3 % = CIRCA 630 €',items:[
  I('q',[75],960,250,'E le pensioni al minimo?'),
  ...EQ(480,[['num','611,85 €','Il trattamento minimo'],['op','×','con il tre per cento'],['num','3 %','con il tre per cento'],['op','=','arriverebbe a circa'],['num','≈ 630 €','seicentotrenta',{fill:GF_}]]),
  VT('IL TRATTAMENTO MINIMO NEL 2026',960,700,'Il trattamento minimo',AMB,44)]},
 {at:'Ma nel duemilaventisei',top:'L’EXTRA DEL 2026',cap:'NEL 2026 C’ERA UN EXTRA: + 1,3 %, PREVISTO DALLA LEGGE SOLO FINO AL 2026',capSize:40,items:[
  VN('+ 1,3 %',600,440,'uno virgola tre per cento',{fs:130,fill:GF_,sub:'EXTRA SULLE MINIME',minw:560}),
  I('cal',['GENNAIO','2026',150,'SOLO FINO AL'],1450,490,'solo fino al duemilaventisei',0.85),
  VT('PREVISTO DALLA LEGGE SOLO FINO AL 2026',960,800,'previsto dalla legge',RF_,44)]},
]);
// ---------- BLOCCO 22 ----------
SPECS[22]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DAL 2027',cap:'DAL 2027 QUELL’EXTRA NON È GARANTITO: DIPENDE DALLA MANOVRA DI DICEMBRE',capSize:40,items:[
  VN('+ 1,3 %',440,450,'quell’extra non è garantito',{fs:120,fill:GF_,minw:480}),
  I('q',[75],880,300,'non è garantito'),
  I('doc',['MANOVRA',420,330,GRN,38],1230,470,'dipende dalla manovra'),
  I('cal',['DICEMBRE','12',150,'DI SOLITO'],1670,490,['dipende dalla manovra',0.9],0.75)]},
 {at:'Si parla di aumentare',top:'SOLO UNA PROPOSTA',cap:'SI PARLA DI AUMENTARE LE MINIME, MA È SOLO UNA PROPOSTA, NON È LEGGE',capSize:42,items:[
  I('stamp',['SOLO UNA PROPOSTA',AMB,60],960,330,'è solo una proposta'),
  I('stamp',['NON È LEGGE',RED_,60],960,520,'non è legge'),
  VT('NON CONTARCI FINCHÉ NON VEDI IL TESTO APPROVATO',960,740,'Non contarci',GF_,44)]},
]);
// ---------- BLOCCO 23 ----------
SPECS[23]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DA DOVE ARRIVA IL 3 %?',cap:'LA PEREQUAZIONE AUTOMATICA: OGNI 1° GENNAIO L’INPS ADEGUA LE PENSIONI',capSize:42,items:[
  VN('3 %',330,440,'quel tre per cento',{fs:120,sub:'DA DOVE ARRIVA?',minw:420}),
  I('cal',['GENNAIO','1',150,'OGNI ANNO'],820,490,'ogni primo gennaio',0.8),
  VT('PEREQUAZIONE AUTOMATICA',1480,300,'perequazione automatica',GF_,40),
  VT('L’INPS ADEGUA AI PREZZI',1480,470,'l’Inps adegua',AMB,40),
  VT('SENZA DOMANDA',1480,640,'senza che tu faccia domanda',GF_,40)]},
 {at:'Serve a difendere',top:'IL POTERE D’ACQUISTO',cap:'SERVE A DIFENDERE IL TUO POTERE D’ACQUISTO, PERCHÉ I PREZZI SALGONO',capSize:42,items:[
  I('shield',[],560,430,'difendere il tuo potere',0.9),
  VT('POTERE D’ACQUISTO',560,720,'potere d’acquisto',GF_,44),
  I('arD',[],1250,380,'i prezzi salgono',1),
  VT('I PREZZI SALGONO',1250,640,'i prezzi salgono',RF_,44)]},
]);
// ---------- BLOCCO 24 ----------
SPECS[24]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'L’INDICE ISTAT',cap:'L’INDICE FOI: FAMIGLIE DI OPERAI E IMPIEGATI, AL NETTO DEI TABACCHI',capSize:42,items:[
  VN('FOI',420,420,'Foi',{fs:150,fill:GF_,sub:'INDICE ISTAT',minw:460}),
  VT('FAMIGLIE DI OPERAI E IMPIEGATI',1250,340,'famiglie di operai',AMB,42),
  VT('AL NETTO DEI TABACCHI',1250,520,'al netto dei tabacchi',RF_,42)]},
 {at:'È un paniere di prezzi',top:'UN PANIERE DI PREZZI',cap:'L’ISTAT MISURA QUANTO COSTA QUELLO CHE COMPRA UNA FAMIGLIA DI LAVORATORI',capSize:40,items:[
  I('basket',[],460,480,'È un paniere di prezzi',1.5),
  VT('UN PANIERE DI PREZZI',1320,330,'È un paniere di prezzi',GF_,44),
  VT('QUANTO COSTA QUELLO CHE COMPRA',1320,500,'quanto costa quello che compra',AMB,40),
  VT('UNA FAMIGLIA DI LAVORATORI',1320,660,'una famiglia di lavoratori',GF_,40)]},
]);
// ---------- BLOCCO 25 ----------
SPECS[25]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SECONDA TRAPPOLA',cap:'A SETTEMBRE L’ISTAT: INFLAZIONE GENERALE AL 4,2 %',items:[
  I('circ',['2','url(#g_head)'],300,460,'seconda trappola'),
  I('cal',['SETTEMBRE','2026',130,'ISTAT'],720,490,'A settembre l’Istat',0.85),
  VN('4,2 %',1360,460,'quattro virgola due',{fs:150,fill:RF_,sub:'INFLAZIONE GENERALE',minw:560})]},
 {at:'Sembra tantissimo',top:'MA NON È LA TUA PERCENTUALE',cap:'SEMBRA TANTISSIMO! MA NON È LA PERCENTUALE DELLE PENSIONI: I MOTIVI SONO DUE',capSize:40,items:[
  VN('4,2 %',460,360,'Sembra tantissimo',{fs:120,fill:RF_,sub:'INFLAZIONE'}),
  VO('≠',820,360,'Ma quella non è'),
  VN('PENSIONI',1250,360,'delle pensioni',{fs:100,fill:GF_,sub:'LA TUA PERCENTUALE',minw:560}),
  I('circ',['1',RF_],760,680,'i motivi sono due'),I('circ',['2','url(#g_head)'],1160,680,['i motivi sono due',0.5]),
  VT('DUE MOTIVI',960,830,'i motivi sono due',AMB,44)]},
]);

// ---------- BLOCCO 26 ----------
SPECS[26]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PRIMO MOTIVO',cap:'IL 4,2 % RIGUARDA L’INDICE GENERALE DEI PREZZI, NON L’INDICE FOI',capSize:42,items:[
  I('circ',['1',RF_],240,440,'Primo motivo'),
  VN('4,2 %',680,440,'quel quattro virgola due',{fs:120,fill:RF_,sub:'INDICE GENERALE',minw:520}),
  VO('≠',1010,440,'non l’indice Foi'),
  VN('FOI',1460,440,'non l’indice Foi',{fs:120,fill:GF_,sub:'INDICE DELLE PENSIONI',minw:520})]},
 {at:'Per i numeri dell’indice Foi',top:'I NUMERI DEL FOI',cap:'IL FOI DI SETTEMBRE: DAL 16 OTTOBRE, QUANDO L’ISTAT PUBBLICA I DATI COMPLETI',capSize:40,items:[
  VT('FOI DI SETTEMBRE: BISOGNA ASPETTARE',960,235,'bisogna aspettare',AMB,40),
  I('cal',['OTTOBRE','16',230,'ISTAT PUBBLICA'],520,520,'il sedici ottobre',0.8),
  I('doc',['DATI COMPLETI',520,330,GRN,40],1250,520,'pubblica i dati completi')]},
]);
// ---------- BLOCCO 27 ----------
SPECS[27]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SECONDO MOTIVO',cap:'LA RIVALUTAZIONE NON GUARDA L’ULTIMO MESE, MA LA MEDIA DELL’ANNO INTERO',capSize:42,items:[
  I('circ',['2','url(#g_head)'],200,440,'Secondo motivo'),
  VN('ULTIMO MESE',680,440,'non guarda l’ultimo mese',{fs:70,minw:500}),I('cross',[150,60],680,440,['non guarda l’ultimo mese',0.5]),
  VN('MEDIA DELL’ANNO',1450,440,'ma la media dell’anno intero',{fs:62,fill:GF_,sub:'DA GENNAIO A DICEMBRE',minw:560})]},
 {at:'A settembre i prezzi',top:'LA MEDIA',cap:'A SETTEMBRE I PREZZI SONO SALITI, MA I MESI PRIMA PESAVANO MENO: LA MEDIA LI METTE INSIEME',capSize:38,items:[
  I('mbars',[],480,700,'A settembre i prezzi',1),
  VT('PREZZI SALITI TANTO',1420,330,'sono saliti tanto',RF_,40),
  VT('MESI PRIMA: PESANO MENO',1420,470,'i mesi prima pesavano meno',GF_,40),
  I('avg',[],480,640,'la media li mette tutti insieme',1),
  VT('LA MEDIA LI METTE INSIEME',1420,610,'li mette tutti insieme',AMB,40)]},
]);
// ---------- BLOCCO 28 ----------
SPECS[28]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'UN ESEMPIO VERO',cap:'A SETTEMBRE: INFLAZIONE MEDIA 2026 GIÀ ACQUISITA = 3,1 %',capSize:42,items:[
  I('cal',['SETTEMBRE','2026',130,'ESEMPIO VERO'],420,490,'a settembre l’inflazione',0.85),
  VN('3,1 %',1190,440,'tre virgola uno per cento',{fs:140,fill:GF_,sub:'INFLAZIONE MEDIA 2026 ACQUISITA',minw:760}),
  VT('SULL’INDICE GENERALE',1190,660,'sull’indice generale',AMB,40)]},
 {at:'Molto meno del quattro',top:'MOLTO MENO DEL 4,2 %',cap:'3,1 % È MOLTO MENO DEL 4,2 %',items:[
  VN('3,1 %',500,430,'Molto meno del quattro virgola due',{fs:140,fill:GF_,minw:400}),
  VO('<',960,430,'Molto meno del quattro virgola due'),
  VN('4,2 %',1420,430,['Molto meno del quattro virgola due',0.8],{fs:140,fill:RF_,minw:400})]},
 {at:'Per le pensioni conta',top:'PER LE PENSIONI',cap:'PER LE PENSIONI CONTA QUESTO TIPO DI MEDIA, CALCOLATA SULL’INDICE FOI',capSize:42,items:[
  VT('CONTA LA MEDIA DELL’ANNO',560,430,'questo tipo di media',AMB,44),
  VN('FOI',1400,430,'calcolata sull’indice Foi',{fs:130,fill:GF_,sub:'L’INDICE DELLE PENSIONI',minw:520})]},
]);
// ---------- BLOCCO 29 ----------
SPECS[29]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'L’INDICE FOI AD AGOSTO',cap:'FOI DI AGOSTO: + 3,4 % RISPETTO A UN ANNO PRIMA',items:[
  I('cal',['AGOSTO','FOI',130,'INDICE ISTAT'],450,490,'ad agosto',0.85),
  VN('+ 3,4 %',1250,450,'Più tre virgola quattro',{fs:140,fill:GF_,sub:'RISPETTO A UN ANNO PRIMA',minw:700})]},
 {at:'Da qui nascono',top:'LE STIME CHE GIRANO',cap:'STIME DI TERZI TRA 2,6 % E 2,9 %: NON SONO UFFICIALI!',items:[
  VN('2,6 % – 2,9 %',960,360,'tra due virgola sei',{fs:120,sub:'LE STIME CHE GIRANO',minw:760}),
  I('stamp',['STIME DI TERZI',AMB,56],540,660,'stime di terzi'),
  I('stamp',['NON UFFICIALI',RED_,56],1400,660,'non sono ufficiali')]},
]);
// ---------- BLOCCO 30 ----------
SPECS[30]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CHI FISSA LA PERCENTUALE?',cap:'UN DECRETO FIRMATO DAL MINISTERO DELL’ECONOMIA E DAL MINISTERO DEL LAVORO',capSize:40,items:[
  I('q',[90],260,450,'Allora chi fissa la percentuale vera'),
  I('doc',['DECRETO',380,330,GRN,40],700,460,'Un decreto firmato'),
  VT('MINISTERO DELL’ECONOMIA',1350,360,'Ministero dell’Economia',AMB,38),
  VT('MINISTERO DEL LAVORO',1350,520,'Ministero del Lavoro',GF_,38)]},
 {at:'Di solito esce a novembre',top:'QUANDO ESCE',cap:'DI SOLITO A NOVEMBRE: L’ANNO SCORSO IL 19 NOVEMBRE',items:[
  I('cal',['NOVEMBRE','19',230,'DI SOLITO'],480,490,'esce a novembre',0.85),
  VT('L’ANNO SCORSO: 19 NOVEMBRE',1370,380,'l’anno scorso è stato il diciannove',GF_,44),
  VT('QUEST’ANNO: PIÙ O MENO UGUALE',1370,560,'Quest’anno, probabilmente',AMB,40)]},
]);
