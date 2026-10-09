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
// ---------- BLOCCO 31 ----------
SPECS[31]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL DECRETO DICE DUE COSE',cap:'IL DECRETO DICE DUE COSE: LA PERCENTUALE DEFINITIVA E QUELLA PROVVISORIA',capSize:40,items:[
  I('doc',['DECRETO',380,330,GRN,40],330,470,'Il decreto dice due cose'),
  VN('DEFINITIVA',1250,340,'Primo: la percentuale definitiva',{fs:80,fill:GF_,sub:'DELL’AUMENTO CHE HAI GIÀ PRESO QUEST’ANNO',minw:900}),
  VN('PROVVISORIA',1250,600,'Secondo: la percentuale provvisoria',{fs:80,fill:AMB,sub:'PER QUELLO CHE ARRIVA A GENNAIO',minw:900})]},
 {at:'Provvisoria! Perché',top:'PERCHÉ PROVVISORIA?',cap:'PROVVISORIA: L’ANNO NON È FINITO E I PREZZI DI DICEMBRE NON CI SONO',capSize:40,items:[
  I('cal',['DICEMBRE','2026',110,'NON ANCORA'],440,490,'prezzi di dicembre',0.85),
  VT('PROVVISORIA!',1300,330,'Provvisoria! Perché',RF_,44),
  VT('L’ANNO NON È ANCORA FINITO',1300,500,'non è ancora finito',AMB,40),
  VT('I PREZZI DI DICEMBRE NON CI SONO',1300,660,'prezzi di dicembre non ci sono',GF_,40)]},
]);
// ---------- BLOCCO 32 ----------
SPECS[32]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'I NUMERI VERI',cap:'GENNAIO 2025: DEFINITIVA 0,8 %   |   GENNAIO 2026: PROVVISORIA 1,4 %',capSize:42,items:[
  VN('0,8 %',500,430,'zero virgola otto per cento',{fs:130,fill:GF_,sub:'GENNAIO 2025: DEFINITIVA',minw:640}),
  VN('1,4 %',1380,430,'uno virgola quattro per cento',{fs:130,fill:AMB,sub:'GENNAIO 2026: PROVVISORIA',minw:700})]},
 {at:'Lo dice la circolare',top:'LA CIRCOLARE INPS',cap:'LO DICE LA CIRCOLARE DELL’INPS NUMERO 153 DEL 19 DICEMBRE',items:[
  I('doc',['CIRCOLARE INPS',560,330,GRN,44],960,450,'Lo dice la circolare'),
  VT('NUMERO 153 DEL 19 DICEMBRE',960,700,'numero centocinquantatré',AMB,44)]},
]);
// ---------- BLOCCO 33 ----------
SPECS[33]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONGUAGLIO',cap:'TERZA TRAPPOLA: IL CONGUAGLIO. PROVVISORIA VUOL DIRE CHE PUÒ ESSERCI UNA CORREZIONE',capSize:38,items:[
  I('circ',['3',GF_],240,440,'Terza trappola'),
  VN('CONGUAGLIO',720,440,'il conguaglio',{fs:70,minw:640}),
  VT('UNA CORREZIONE',1450,440,'una correzione',AMB,44)]},
 {at:'Se a novembre',top:'SE È UGUALE',cap:'SE A NOVEMBRE IL DATO DEFINITIVO È UGUALE AL PROVVISORIO, NON SUCCEDE NIENTE',capSize:40,items:[
  ...EQ(380,[['num','DEFINITIVO','Se a novembre'],['op','=','uguale a quello provvisorio'],['num','PROVVISORIO','uguale a quello provvisorio']],56,360),
  VT('NON SUCCEDE NIENTE',960,640,'non succede niente',GF_,48)]},
 {at:'Se è diverso',top:'SE È DIVERSO',cap:'SE È DIVERSO, A GENNAIO C’È IL CONGUAGLIO',items:[
  ...EQ(380,[['num','DEFINITIVO','Se è diverso'],['op','≠',['Se è diverso',0.4]],['num','PROVVISORIO',['Se è diverso',0.7]]],56,360),
  VT('A GENNAIO C’È IL CONGUAGLIO',960,640,'a gennaio c’è il conguaglio',RF_,48)]},
 {at:'A gennaio duemilaventisei, per esempio',top:'UN ESEMPIO: GENNAIO 2026',cap:'A GENNAIO 2026: NESSUN CONGUAGLIO DOVUTO',items:[
  I('cal',['GENNAIO','2026',150,'PER ESEMPIO'],560,490,'A gennaio duemilaventisei, per esempio',0.85),
  I('stamp',['NESSUN CONGUAGLIO',GRN,56],1330,470,'nessun conguaglio dovuto')]},
]);
// ---------- BLOCCO 34 ----------
SPECS[34]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RIASSUNTO',cap:'IL TITOLO È L’INFLAZIONE DI UN MESE. LA TUA PERCENTUALE È LA MEDIA DEL FOI, DI NOVEMBRE, PROVVISORIA',capSize:36,items:[
  VN('IL TITOLO',520,400,'il titolo spesso',{fs:84,fill:RF_,sub:'INFLAZIONE DI UN MESE',minw:600}),
  VN('LA TUA %',1400,400,'La tua percentuale',{fs:84,fill:GF_,sub:'MEDIA DELL’INDICE FOI',minw:640}),
  VT('FISSATA A NOVEMBRE E PROVVISORIA',960,660,'fissata a novembre e provvisoria',AMB,44)]},
 {at:'Davanti a una cifra',top:'DAVANTI A UNA CIFRA',cap:'DAVANTI A UNA CIFRA CHIEDITI: QUALE INDICE? QUALE PERIODO? UFFICIALE O STIMA?',capSize:40,items:[
  I('q',[100],300,450,'chiediti'),
  VT('QUALE INDICE?',1100,300,'quale indice?',GF_,50),
  VT('QUALE PERIODO?',1100,470,'Quale periodo?',AMB,50),
  VT('UFFICIALE O STIMA?',1100,640,'È ufficiale o è una stima?',RF_,50)]},
]);
// ---------- BLOCCO 35 ----------
SPECS[35]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FAI IL CONTO DA SOLO',cap:'FAI IL CONTO DA SOLO, IN TRE PASSI: PASSO 1, PASSO 2, PASSO 3',items:[
  I('trow',[1500,'LA PENSIONE LORDA MENSILE DAL CEDOLINO','PASSO 1',GF_],960,330,'Passo uno: prendi'),
  VT('QUELLA PRIMA DELLE TASSE',1000,470,'quella prima delle tasse',AMB,44)]},
 {at:'Passo due',top:'PASSO 2: LA FASCIA',cap:'PASSO 2: IN QUALE FASCIA SEI? SUPERI CIRCA 2.450 € AL MESE?',items:[
  I('trow',[1500,'LA PENSIONE LORDA MENSILE DAL CEDOLINO','PASSO 1',GF_],960,300,0.4),
  I('trow',[1500,'IN QUALE FASCIA SEI?','PASSO 2',AMB],960,470,'Passo due'),
  VN('≈ 2.450 €',960,700,'duemilaquattrocentocinquanta',{fs:90,fill:GF_,sub:'SUPERI QUESTA SOGLIA AL MESE?',minw:700})]},
]);
// ---------- BLOCCO 36 ----------
SPECS[36]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PASSO 3: SOTTO SOGLIA',cap:'SOTTO SOGLIA: PENSIONE × 0,03 (IL 3 %) = AUMENTO',items:[
  VT('SE SEI SOTTO SOGLIA',960,280,'se sei sotto soglia',AMB,44),
  ...EQ(470,[['num','PENSIONE','moltiplichi per la percentuale'],['op','×','Con il tre per cento'],['num','0,03','zero virgola zero tre',{sub:'IL 3 %'}],['op','=','zero virgola zero tre'],['num','AUMENTO','zero virgola zero tre',{fill:GF_,fs:50}]],56,340),
  VT('CON IL 3 % MOLTIPLICHI PER 0,03',960,720,'Con il tre per cento',GF_,44)]},
 {at:'Se sei sopra',top:'SE SEI SOPRA LA SOGLIA',cap:'SOPRA SOGLIA: LA PARTE PIENA + LA PARTE NELLA FASCIA AL 90 % O AL 75 %',capSize:40,items:[
  I('seg',[640,150,GF_,'PARTE PIENA','AL 100 %'],500,440,'calcoli la parte piena'),
  VO('+',960,440,['poi aggiungi',0]),
  I('seg',[640,150,AMB,'PARTE NELLA FASCIA','AL 90 % O AL 75 %'],1420,440,'nella fascia al novanta')]},
]);
// ---------- BLOCCO 37 ----------
SPECS[37]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'UN MINUTO',cap:'CON LA CALCOLATRICE DEL TELEFONO CI METTI UN MINUTO',items:[
  I('calc',[],560,470,'Con la calcolatrice',1.5),
  VT('CON LA CALCOLATRICE: UN MINUTO',1330,470,'ci metti un minuto',AMB,44)]},
 {at:'Quando uscirà',sh:0.4,top:'LA PERCENTUALE UFFICIALE',cap:'CAMBI SOLO QUEL NUMERO E RIFAI IL CONTO',items:[
  VN('3 %',480,430,'Quando uscirà',{fs:130,minw:420,sub:'ESEMPIO'}),
  I('arR',[],900,430,'cambi solo quel numero',1),
  VN('% UFFICIALE',1350,430,'cambi solo quel numero',{fs:90,fill:GF_,minw:560,sub:'DAL DECRETO'}),
  VT('RIFAI IL CONTO',960,700,'rifai il conto',AMB,50)]},
 {at:'Ecco perché il metodo',sh:0.5,top:'IL METODO',cap:'IL METODO CONTA PIÙ DELLA CIFRA: VALE OGGI E ANCHE L’ANNO PROSSIMO',capSize:42,items:[
  I('chk',[110],400,440,'Ecco perché il metodo'),
  VT('IL METODO CONTA PIÙ DELLA CIFRA',1130,340,'conta più della cifra',GF_,44),
  VT('VALE OGGI',1130,500,'vale oggi',AMB,44),
  VT('E VARRÀ ANCHE L’ANNO PROSSIMO',1130,640,'varrà anche l’anno prossimo',GF_,44)]},
]);
// ---------- BLOCCO 38 ----------
SPECS[38]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TEST',cap:'IL TEST: TRE DOMANDE, VERO O FALSO. RISPONDI A VOCE ALTA!',items:[
  I('circ',['1',GF_],560,430,'tre domande'),I('circ',['2','url(#g_head)'],960,430,['tre domande',0.5]),I('circ',['3',RF_],1360,430,['tre domande',1.0]),
  VT('VERO O FALSO',960,640,'vero o falso!',AMB,50),
  VT('RISPONDI A VOCE ALTA',960,770,'Rispondi a voce alta',GF_,44)]},
 {at:'Domanda uno',top:'DOMANDA 1',cap:'DOMANDA 1: LA RIVALUTAZIONE È UGUALE PER TUTTE LE PENSIONI?',capSize:42,items:[
  VT('LA RIVALUTAZIONE È UGUALE PER TUTTE LE PENSIONI',960,280,'la rivalutazione è uguale',AMB,40),
  I('vf',[true],760,440,'Vero o falso?'),I('vf',[false],1160,440,['Vero o falso?',0.3]),
  I('stamp',['FALSO!',RED_,70],960,630,'Falso!'),
  VT('SOPRA LA PRIMA SOGLIA PRENDE IL 90 % O IL 75 %',960,810,'Sopra la prima soglia',GF_,40)]},
]);
// ---------- BLOCCO 39 ----------
SPECS[39]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DOMANDA 2',cap:'DOMANDA 2: LA PERCENTUALE LA DECIDE L’INPS A GENNAIO?',items:[
  I('circ',['2','url(#g_head)'],240,380,'Domanda due'),
  VT('LA DECIDE L’INPS, A GENNAIO, GUARDANDO L’INFLAZIONE',1180,380,'la percentuale la decide',AMB,32),
  I('vf',[true],760,600,'Vero o falso?'),I('vf',[false],1160,600,['Vero o falso?',0.3])]},
 {at:'Falso!',top:'FALSO!',cap:'LA FISSA UN DECRETO DEI MINISTERI, DI SOLITO A NOVEMBRE: ALL’INIZIO È PROVVISORIA',capSize:38,items:[
  I('stamp',['FALSO!',RED_,70],400,330,'Falso!'),
  VT('LA FISSA UN DECRETO DEI MINISTERI',1300,330,'La fissa un decreto',GF_,40),
  VT('DI SOLITO A NOVEMBRE',1300,470,'di solito a novembre',AMB,40),
  VT('L’INPS LA APPLICA',1300,610,'L’Inps la applica',GF_,40),
  VT('ALL’INIZIO È PROVVISORIA, CON CONGUAGLIO',960,780,'E all’inizio è provvisoria',RF_,40)]},
]);
// ---------- BLOCCO 40 ----------
SPECS[40]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DOMANDA 3',cap:'DOMANDA 3: SE LA RIVALUTAZIONE È IL 3 %, TI ARRIVA IL 3 % IN PIÙ?',capSize:42,items:[
  I('circ',['3',RF_],230,400,'Domanda tre'),
  VT('IL 3 % SUL CONTO: TI ARRIVA IL 3 % IN PIÙ?',1090,400,'sul conto ti arriva',AMB,36),
  I('vf',[true],760,620,'Vero o falso?'),I('vf',[false],1160,620,['Vero o falso?',0.2])]},
 {at:'Falso!',sh:0.5,top:'FALSO!',cap:'IL 3 % È SUL LORDO. IL NETTO SALE MENO. QUANTE NE HAI AZZECCATE?',capSize:42,items:[
  I('stamp',['FALSO!',RED_,70],480,360,'Falso!'),
  VT('IL 3 % È SUL LORDO',1230,320,'sull’importo lordo',AMB,40),
  VT('IL NETTO SALE MENO',1230,470,'sale meno',GF_,40),
  VT('QUANTE NE HAI AZZECCATE?',960,720,'Quante ne hai azzeccate',RF_,50)]},
]);
// ---------- BLOCCO 41 ----------
SPECS[41]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LORDO E NETTO',cap:'LORDO E NETTO: LA DOMANDA CHE SI FANNO TUTTI',items:[
  VN('LORDO',560,430,'Parliamo di lordo',{fs:100,fill:AMB,sub:'PRIMA DELLE TASSE',minw:560}),
  VN('NETTO',1360,430,'e netto',{fs:100,fill:GF_,sub:'QUELLO CHE INCASSI',minw:560})]},
 {at:'Se la pensione lorda sale',top:'+ 60 € LORDI',cap:'SE IL LORDO SALE DI 60 €, UNA PARTE VA IN IRPEF E ADDIZIONALI: SUL CONTO ARRIVA MENO',capSize:36,items:[
  VN('+ 60 €',400,430,'sale di sessanta euro',{fs:110,fill:AMB,sub:'LORDI',minw:440}),
  I('arR',[],780,430,'una parte di quei sessanta',1),
  VT('IRPEF',1330,300,'va in Irpef',RF_,44),
  VT('ADDIZIONALE REGIONALE',1330,420,'regionale',RF_,40),
  VT('ADDIZIONALE COMUNALE',1330,540,'comunale',RF_,40),
  VN('< 60 €',1330,730,'arriva meno di sessanta',{fs:90,fill:GF_,sub:'SUL CONTO',minw:520})]},
]);
// ---------- BLOCCO 42 ----------
SPECS[42]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO MENO?',cap:'QUANTO MENO? DIPENDE DA TE',items:[
  I('q',[85],260,450,'Quanto meno?'),
  VT('QUANTO PERCEPISCI IN TOTALE',1150,280,'da quanto percepisci',AMB,42),
  VT('LA REGIONE',1150,420,'dalla regione',GF_,42),
  VT('IL COMUNE',1150,560,'dal comune',AMB,42),
  VT('LE DETRAZIONI',1150,700,'dalle detrazioni',GF_,42)]},
 {at:'Per questo non ti do',top:'NIENTE CIFRA UNICA',cap:'LA CIFRA GIUSTA È NEL TUO CEDOLINO, ALLA VOCE IMPORTO NETTO',items:[
  I('stamp',['NESSUNA CIFRA UNICA',AMB,50],560,330,'Per questo non ti do'),
  I('pay',['CEDOLINO','NETTO'],1350,440,'La cifra giusta è nel tuo cedolino',1.1),
  VT('VOCE: IMPORTO NETTO',1350,740,'importo netto',GF_,42)]},
]);
// ---------- BLOCCO 43 ----------
SPECS[43]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'UNA POSSIBILE NOVITÀ',cap:'NEL DIBATTITO SULLA MANOVRA: CAMBIARE L’IRPEF, ANCHE PER I PENSIONATI',capSize:42,items:[
  I('doc',['MANOVRA',420,330,GRN,38],430,450,'sulla manovra'),
  VN('IRPEF',1000,430,'cambiare l’Irpef',{fs:100,fill:AMB,minw:420}),
  VT('ANCHE PER I PENSIONATI',1420,640,'anche per i pensionati',GF_,40)]},
 {at:'Ma attenzione',top:'MA ATTENZIONE',cap:'AL MOMENTO È SOLO UNA PROPOSTA, NON È LEGGE',items:[
  I('warn',[],360,430,'Ma attenzione',0.9),
  I('stamp',['SOLO UNA PROPOSTA',AMB,56],1150,330,'solo una proposta'),
  I('stamp',['NON È LEGGE',RED_,56],1150,520,'non è legge')]},
 {at:'Se passerà',sh:0.5,top:'SE PASSERÀ',cap:'CAMBIERÀ IL NETTO, NON LA RIVALUTAZIONE LORDA',items:[
  VN('NETTO',540,430,'cambierà il netto',{fs:100,fill:GF_,sub:'CAMBIA',minw:520}),
  VN('LORDA',1380,430,'non la rivalutazione lorda',{fs:100,minw:520,sub:'RIVALUTAZIONE'}),
  I('cross',[200,100],1380,430,['non la rivalutazione lorda',0.4])]},
]);
// ---------- BLOCCO 44 ----------
SPECS[44]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COME CONTROLLI',cap:'CON IL TUO CEDOLINO, SU MAI INPS',items:[
  I('br',['inps.it',1000,560],620,470,'Come controlli'),
  I('row',['MAI INPS',820,true],620,380,'su Mai Inps'),
  I('row',['CEDOLINO DELLA PENSIONE',820,true],620,480,'cedolino'),
  I('chk',[100],1560,470,'Con il tuo cedolino')]},
 {at:'Entra su inps punto it',sh:0.5,top:'COME ENTRI',cap:'ENTRA SU INPS.IT CON LO SPID, LA CARTA D’IDENTITÀ ELETTRONICA O LA CARTA NAZIONALE DEI SERVIZI',capSize:34,items:[
  VT('SPID',960,280,'con lo Spid',GF_,48),
  VT('CARTA D’IDENTITÀ ELETTRONICA',960,420,'la carta d’identità elettronica',AMB,44),
  VT('CARTA NAZIONALE DEI SERVIZI',960,560,'la carta nazionale dei servizi',GF_,44),
  VT('POI: CERCA IL CEDOLINO DELLA PENSIONE',960,730,'cerca il cedolino',RF_,44)]},
]);
// ---------- BLOCCO 45 ----------
SPECS[45]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CONFRONTA DUE CEDOLINI',cap:'DICEMBRE E GENNAIO: LA DIFFERENZA DELL’IMPORTO LORDO È IL TUO AUMENTO',capSize:40,items:[
  I('pay',['DICEMBRE','LORDO'],420,450,'quello di dicembre',1),
  VO('−',770,450,'quello di gennaio'),
  I('pay',['GENNAIO','LORDO'],1120,450,['quello di gennaio',0.12],1),
  VO('=',1470,450,'la differenza'),
  VN('AUMENTO',1700,450,'è il tuo aumento',{fs:44,fill:GF_,minw:240})]},
 {at:'Poi guarda se compare',top:'LA VOCE DI CONGUAGLIO',cap:'SE C’È UNA VOCE DI CONGUAGLIO È LA CORREZIONE DELL’ANNO PRIMA: VA LETTA A PARTE',capSize:36,items:[
  I('row',['VOCE: CONGUAGLIO',820,true],700,360,'voce di conguaglio'),
  VT('LA CORREZIONE DELL’ANNO PRIMA',1130,560,'la correzione dell’anno prima',AMB,42),
  VT('VA LETTA A PARTE',1130,710,'va letta a parte',GF_,44)]},
]);
// ---------- BLOCCO 46 ----------
SPECS[46]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RIFAI IL CONTO',cap:'RIFAI IL CONTO CON IL METODO DI PRIMA: SE LA DIFFERENZA TORNA, TUTTO BENE',capSize:40,items:[
  I('calc',[],420,470,'Rifai il conto',1.3),
  I('chk',[110],1200,430,'tutto bene'),
  VT('LA DIFFERENZA TORNA: TUTTO BENE',1200,640,'tutto bene',GF_,44)]},
 {at:'Se non torna',sh:0.7,top:'SE NON TORNA',cap:'NIENTE PANICO: PRIMA LA FASCIA, POI IL CONGUAGLIO',items:[
  I('circ',['1',GF_],520,380,'guarda prima la fascia'),VT('LA FASCIA',1150,380,'guarda prima la fascia',GF_,48),
  I('circ',['2','url(#g_head)'],520,560,'poi il conguaglio'),VT('IL CONGUAGLIO',1150,560,'poi il conguaglio',AMB,48)]},
 {at:'Se hai ancora dubbi',sh:0.5,top:'ANCORA DUBBI?',cap:'PORTA IL CEDOLINO A UN PATRONATO: DI SOLITO IL SERVIZIO È GRATUITO',capSize:40,items:[
  I('pay',['CEDOLINO',''],440,450,'porta il cedolino',1),
  VT('PORTA IL CEDOLINO A UN PATRONATO',1230,380,'a un patronato',AMB,42),
  VT('DI SOLITO IL SERVIZIO È GRATUITO',1230,540,'è gratuito',GF_,42)]},
]);
// ---------- BLOCCO 47 ----------
SPECS[47]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'I TRE ERRORI PIÙ COMUNI',cap:'ERRORE 3: SPENDERE L’AUMENTO PRIMA DI VEDERE IL CEDOLINO',items:[
  I('circ',['3',RF_],300,430,'Errore numero tre'),
  VT('SPENDERE L’AUMENTO PRIMA DI VEDERE IL CEDOLINO',1150,430,'spendere l’aumento',RF_,34)]},
 {at:'Fino a novembre',top:'PERCHÉ?',cap:'FINO A NOVEMBRE È UNA STIMA; A GENNAIO IL NETTO DIPENDE DA TASSE E CONGUAGLI',capSize:38,items:[
  VT('FINO A NOVEMBRE: UNA STIMA',960,330,'è una stima',AMB,46),
  VT('A GENNAIO IL NETTO DIPENDE DA TASSE E CONGUAGLI',960,520,'l’importo netto dipende',GF_,42)]},
]);
// ---------- BLOCCO 48 ----------
SPECS[48]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ERRORE NUMERO DUE',cap:'ERRORE 2: ASPETTARSI LO STESSO AUMENTO DI UN AMICO O DI UN VICINO',capSize:40,items:[
  I('circ',['2','url(#g_head)'],220,430,'Errore numero due'),
  I('med',[],560,430,'di un amico',0.55),I('medm',[],940,430,'o di un vicino',0.55),
  VT('LO STESSO AUMENTO?',1530,430,'lo stesso aumento',AMB,44)]},
 {at:'Con fasce diverse',top:'EURO DIVERSI',cap:'FASCE DIVERSE, IMPORTI DIVERSI, SITUAZIONI FISCALI DIVERSE: EURO DIVERSI SUL CONTO',capSize:36,items:[
  VT('FASCE DIVERSE',560,330,'Con fasce diverse',GF_,44),
  VT('IMPORTI DIVERSI',1280,330,'importi diversi',AMB,44),
  VT('SITUAZIONI FISCALI DIVERSE',960,500,'situazioni fiscali diverse',GF_,44),
  VT('LA STESSA PERCENTUALE: EURO DIVERSI SUL CONTO',960,700,'euro diversi sul conto',RF_,44)]},
]);
// ---------- BLOCCO 49 ----------
SPECS[49]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ERRORE NUMERO UNO',cap:'ERRORE 1: FIDARSI DELLA PRIMA CIFRA CHE TROVANO',items:[
  I('circ',['1',RF_],260,430,'E l’errore numero uno'),
  VT('FIDARSI DELLA PRIMA CIFRA CHE TROVANO',1100,430,'fidarsi della prima cifra',RF_,42)]},
 {at:'Titoli con il tre',top:'TITOLI SENZA CONTESTO',cap:'TITOLI CON IL 3, IL 4, IL 5 %, SENZA DIRE QUALE INDICE, QUALE PERIODO, SE È UNA STIMA',capSize:36,items:[
  I('hl',['3 %'],480,330,'Titoli con il tre',1.25),I('hl',['4 %'],960,330,'il quattro',1.25),I('hl',['5 %'],1440,330,'il cinque per cento',1.25),
  VT('QUALE INDICE?',480,540,'quale indice',GF_,44),VT('QUALE PERIODO?',1070,540,'quale periodo',AMB,44),VT('È UNA STIMA?',960,690,'se è una stima',RF_,44)]},
 {at:'Se manca questo',sh:0.5,top:'NON È UNA NOTIZIA',cap:'SE MANCA QUESTO, NON È UNA NOTIZIA: È SOLO UN TITOLO',items:[
  I('stamp',['NON È UNA NOTIZIA',RED_,64],960,400,'non è una notizia'),
  VT('È SOLO UN TITOLO',960,620,'è solo un titolo',AMB,50)]},
]);
// ---------- BLOCCO 50 ----------
SPECS[50]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RICAPITOLIAMO',cap:'1: POTERE D’ACQUISTO, INDICE FOI   2: DECRETO DI NOVEMBRE   3: FASCE 100 / 90 / 75 %',capSize:36,items:[
  I('circ',['1',GF_],180,340,'Uno:'),VT('DIFENDE IL POTERE D’ACQUISTO: INDICE FOI',1080,340,'difende il potere',GF_,36),
  I('circ',['2','url(#g_head)'],180,520,'Due:'),VT('DECRETO DI NOVEMBRE: PROVVISORIA, CON CONGUAGLIO',1080,520,'la fissa un decreto',AMB,36),
  I('circ',['3',RF_],180,700,'Tre:'),VT('SI APPLICA PER FASCE: 100 %, 90 %, 75 %',1080,700,'si applica per fasce',RF_,36)]},
]);
// ---------- BLOCCO 51 ----------
SPECS[51]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E MARTA?',cap:'MARTA: 1.500 € × 3 % = 45 € IN PIÙ AL MESE, FASCIA PIENA',items:[
  I('med',[],170,440,'E Marta?',0.6),
  ...EQ(440,[['num','1.500 €','millecinquecento euro lordi'],['op','×','al tre per cento'],['num','3 %','al tre per cento'],['op','=','quarantacinque euro'],['num','45 €','quarantacinque euro',{fill:GF_}]],76,260).map(it=>({...it,x:it.x+90})),
  VT('FASCIA PIENA',1500,640,'fascia piena',GF_,40)]},
 {at:'Chi supera la soglia',sh:0.5,top:'CHI SUPERA LA SOGLIA',cap:'CHI SUPERA LA SOGLIA NE PRENDE MENO, E IL NETTO È DIVERSO',items:[
  VT('CHI SUPERA LA SOGLIA NE PRENDE MENO',960,380,'ne prende meno',AMB,46),
  VT('IL NETTO È DIVERSO',960,560,'il netto è diverso',GF_,46)]},
 {at:'La percentuale vera arriva',sh:0.4,top:'A NOVEMBRE',cap:'LA PERCENTUALE VERA ARRIVA A NOVEMBRE. TU HAI GIÀ IL METODO!',items:[
  I('cal',['NOVEMBRE','',150,'LA % VERA'],420,490,'La percentuale vera arriva',0.85),
  I('chk',[110],1100,450,'Tu però hai già il metodo'),
  VT('TU HAI GIÀ IL METODO!',1330,700,'hai già il metodo',GF_,46)]},
]);
// ---------- BLOCCO 52 ----------
SPECS[52]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ADESSO TOCCA A TE',cap:'SCRIVIMI NEI COMMENTI: QUANTO PRENDI DI PENSIONE LORDA E QUANTO TI ASPETTI DI AUMENTO?',capSize:36,items:[
  I('bubble',[560,300],330,420,'Scrivimi nei commenti',0.9),
  VT('QUANTO PRENDI DI PENSIONE LORDA?',1330,330,'quanto prendi di pensione lorda',AMB,40),
  VT('QUANTO TI ASPETTI DI AUMENTO?',1330,490,'quanto ti aspetti di aumento',GF_,40),
  VT('NON SERVE L’IMPORTO ESATTO',1330,650,'Non serve l’importo esatto',GF_,40)]},
 {at:'Leggo tutto',top:'LE VOSTRE DOMANDE',cap:'LEGGO TUTTO, E LE VOSTRE DOMANDE DIVENTANO I PROSSIMI VIDEO!',items:[
  VT('LEGGO TUTTO',960,330,'Leggo tutto',AMB,56),
  VT('LE VOSTRE DOMANDE DIVENTANO I PROSSIMI VIDEO',960,520,'diventano i prossimi video',GF_,48)]},
]);
// ---------- BLOCCO 53 ----------
SPECS[53]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ISCRIVITI',cap:'ISCRIVITI A CONTI IN PENSIONE E ATTIVA LA CAMPANELLA',items:[
  I('btn',['ISCRIVITI'],700,420,'Iscriviti a Conti in Pensione'),
  I('bell',[],1300,420,'attiva la campanella',1.4),
  VT('CONTI IN PENSIONE',700,600,'Conti in Pensione e',AMB,44)]},
 {at:'quando uscirà il decreto',top:'QUANDO ESCE IL DECRETO',cap:'QUANDO ESCE IL DECRETO, TI SPIEGO SUBITO COSA CAMBIA PER LA TUA PENSIONE, CON FONTI UFFICIALI',capSize:34,items:[
  I('doc',['DECRETO',380,300,GRN,40],400,450,'quando uscirà il decreto'),
  VT('TI SPIEGO SUBITO COSA CAMBIA',1250,380,'ti spiego subito',GF_,42),
  VT('CON FONTI UFFICIALI',1250,540,'con fonti ufficiali',AMB,42)]},
]);
// ---------- BLOCCO 54 (slide finale con il disclaimer, stile video 2; centro-basso e destra-basso LIBERI per la schermata finale) ----------
SPECS[54]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'VERIFICA SEMPRE',cap:'VERIFICA SEMPRE SUI CANALI UFFICIALI: INPS.IT. GRAZIE PER AVER GUARDATO!',capSize:42,items:[
  I('dbg',[1060,330],1280,330,'Le informazioni di questo video'),
  I('dline',['INFORMAZIONI A SCOPO DIVULGATIVO','#fff',32],1280,320,'scopo divulgativo'),
  I('dline',['NON SOSTITUISCE UN PATRONATO O L’INPS','#7FF0D2',30],1280,380,'non sostituiscono'),
  I('dline',['GLI IMPORTI SONO ESEMPI, NON PREVISIONI','#FFB838',30],1280,440,'Gli importi sono esempi'),
  I('br',['inps.it',600,330],400,330,'Verifica sempre'),
  I('row',['CANALI UFFICIALI',460,true],400,360,'canali ufficiali'),
  I('med',[],200,700,'Grazie per aver guardato',0.45),I('medm',[],360,700,['Grazie per aver guardato',0.4],0.45)]},
]);
