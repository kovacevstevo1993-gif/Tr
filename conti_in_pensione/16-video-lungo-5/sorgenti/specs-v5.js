// ===== V5 (tredicesima 2026) - VERSIONE 2: UNA SCENA PER BLOCCO (due solo per il blocco 37), elementi che restano fino a fine scena =====
// Regola N.18: scene >= 5 s, nessun elemento sparisce dentro la scena, comparsa 0,9 s, tutto finito entro l'80 %.
const SPECS={};
const GF_='url(#g_badge)',RF_='url(#g_red)',PF_='url(#g_paper)',DF_='#0B4A50';
const VT=(s,x,y,at,fill,fs)=>I('tag',[s,fill||AMB,(fill&&fill!==AMB)?'#fff':'#5A3300',fs||44],x,y,at);
const VN=(s,x,y,at,o)=>{o=o||{};return I('num',[s,o.fs||76,o.fill||PF_,o.sub,o.subfill,o.minw],x,y,at);};
const VO=(s,x,y,at)=>I('op',[s],x,y,at);
const MI='GFMAMGLASOND'.split('');
// riga di mesi: UN SOLO elemento (compare tutta insieme). fills = colore di ogni mese
BUILD.mesi=(g,fills,step,w,h)=>{const n=fills.length;for(let i=0;i<n;i++){const e=el('g',{transform:'translate('+((i-(n-1)/2)*step)+' 0)'},g);BUILD.seg(e,w,h,fills[i],MI[i]);}};
const MESI=(x,y,at,fillf,n,step)=>{n=n||12;step=step||118;const f=[];for(let i=0;i<n;i++)f.push(fillf(i));return I('mesi',[f,step,Math.min(100,step-16),Math.min(90,step-26)],x,y,at);};

// ---------- BLOCCO 1 ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DICEMBRE 2026',cap:'MILLE EURO LORDI: IN BANCA ARRIVANO MOLTI MENO',items:[
  I('cal',['DICEMBRE','13ª',200,'MENSILITÀ'],330,560,'Dicembre.'),
  VN('+ 1 RATA',1230,330,'una mensilità in più',{fs:100,fill:GF_,sub:'IN PIÙ A DICEMBRE'}),
  VN('1.000 €',880,600,'Se la tua pensione',{fs:80,sub:'LORDI'}),
  I('arR',[],1260,610,'in banca non arrivano'),
  VN('? €',1600,600,'Arrivano molti meno',{fs:80,fill:RF_,sub:'IN BANCA',minw:400}),
  VT('NON È QUELLO CHE TI HANNO RACCONTATO',1100,800,'quello che ti hanno raccontato',AMB,36)]},
]);
// ---------- BLOCCO 2 ----------
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'I TITOLONI',cap:'TE LO DICO DOPO AVER FATTO I CONTI VERI',items:[
  I('hl',['TREDICESIMA DETASSATA'],620,290,'tredicesima detassata'),
  I('hl',['TREDICESIMA PIÙ ALTA'],620,470,'tredicesima più alta'),
  I('vf',[true],1500,290,'è vero'),
  I('vf',[false],1500,470,'o falso'),
  VT('I CONTI VERI',440,700,'i conti veri',GF_,48),
  I('circ',['1',GF_],900,700,'uno alla volta'),
  I('circ',['2','url(#g_head)'],1100,700,['uno alla volta',0.5]),
  I('circ',['3',GF_],1300,700,'con cinque pensioni'),
  I('circ',['4','url(#g_head)'],1500,700,['con cinque pensioni',0.6]),
  I('circ',['5',GF_],1700,700,['con cinque pensioni',1.2])]},
]);
// ---------- BLOCCO 3 ----------
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ALLA FINE DEL VIDEO',cap:'DUE COSE CHE TI DICO SOLO ALLA FINE',items:[
  VN('2 COSE',960,320,'Ci sono due cose',{fs:100,sub:'SOLO ALLA FINE',minw:620}),
  I('circ',['1',GF_],330,600,'Un caso in cui'),
  VN('INTERA',800,600,'arriva intera',{fs:80,fill:GF_,sub:'SENZA PERDERE UN EURO'}),
  I('circ',['2','url(#g_head)'],1230,600,'E una voce di dicembre'),
  VT('VOCE DI DICEMBRE',1580,560,'voce di dicembre',AMB,34),
  VT('QUASI NESSUNO LA CONTA',1520,720,'quasi nessuno conta',GF_,32),
  VT('CONTI IN PENSIONE',960,820,'Conti in Pensione',GF_,40)]},
]);
// ---------- BLOCCO 4 ----------
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PARTIAMO DAL SEMPLICE',cap:'ARRIVA CON LA RATA DI DICEMBRE, SENZA FARE DOMANDA',items:[
  I('pay',['CEDOLINO'],300,520,'La tredicesima è una mensilità'),
  VN('+ 1 RATA',900,330,'una mensilità in più',{fs:90,fill:GF_,sub:'TREDICESIMA'}),
  VT('CON LA RATA DI DICEMBRE',900,470,'insieme alla rata di dicembre',AMB,40),
  I('cal',['DICEMBRE','1',230,'MARTEDÌ'],1600,520,'primo dicembre'),
  VT('DOVREBBE ARRIVARE',900,600,'dovrebbe arrivare',GF_,44),
  I('stamp',['NESSUNA DOMANDA',GRN,50],900,760,'nessuna domanda')]},
]);
// ---------- BLOCCO 5 ----------
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO È, IN LORDO?',cap:'1.000 € LORDI AL MESE = 1.000 € LORDI DI TREDICESIMA',items:[
  I('q',[100],300,330,'Quanto è'),
  VN('12 MESI',900,330,'da tutto l’anno',{fs:90,sub:'IN PENSIONE'}),
  VN('1.000 €',520,600,'Mille euro lordi al mese',{fs:80,sub:'RATA MENSILE'}),
  VO('=',960,600,['mille euro lordi di tredicesima',-0.4]),
  VN('1.000 €',1400,600,'mille euro lordi di tredicesima',{fs:80,fill:GF_,sub:'TREDICESIMA'}),
  VT('NESSUNA SORPRESA',960,800,'nessuna sorpresa',GF_,48)]},
]);
// ---------- BLOCCO 6 ----------
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'USCITO DURANTE L’ANNO',cap:'1/12 DELLA RATA PER OGNI MESE: DA LUGLIO È LA METÀ DI UNA RATA',capSize:40,items:[
  MESI(960,290,'durante l’anno',i=>'#2B6F77'),
  VT('MENO MESI DI PENSIONE',960,430,'più piccola',AMB,44),
  VN('1/12',420,600,'un dodicesimo',{fs:80,sub:'DELLA RATA'}),
  VT('PER OGNI MESE',1000,570,'per ogni mese',AMB,44),
  VT('DI PENSIONE',1000,660,'mese di pensione',AMB,44),
  VN('½ RATA',1560,600,'la metà di una rata',{fs:70,fill:GF_,sub:'DA LUGLIO'}),
  MESI(960,800,'Esempio: pensione da luglio',i=>i<6?'#2B6F77':GF_)]},
]);
// ---------- BLOCCO 7 ----------
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA DOMANDA DI TUTTI',cap:'QUEST’ANNO È PIÙ ALTA? SÌ, MA NON PER UN REGALO DI DICEMBRE',capSize:42,items:[
  I('q',[110],330,330,'la domanda che si fanno tutti'),
  VT('PIÙ ALTA?',900,330,'è più alta',AMB,64),
  I('chk',[100],330,560,'è sì'),
  VT('MA NON È UN REGALO',1000,560,'non per un regalo di dicembre',RF_,52),
  I('q',[70],330,780,'da dove viene'),
  VT('NON È DOVE PENSI',900,780,'non è dove pensi',AMB,52)]},
]);
// ---------- BLOCCO 8 ----------
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'GENNAIO 2026',cap:'+ 1,4 % GIÀ DENTRO OGNI RATA, ANCHE NELLA TREDICESIMA',items:[
  I('cal',['GENNAIO','1',230,'2026'],330,540,'A gennaio'),
  VN('+ 1,4 %',1240,310,'uno virgola quattro per cento',{fs:100,sub:'IN VIA PROVVISORIA'}),
  MESI(1240,500,'già dentro ogni rata',i=>'#2B6F77',12,96),
  I('seg',[420,90,GF_,'TREDICESIMA'],1240,620,'anche dentro la tredicesima'),
  VT('+ 1,4 % GIÀ APPLICATO',1240,730,['già dentro ogni rata',1.0],AMB,40),
  I('stamp',['NESSUN AUMENTO NUOVO',RED_,44],1240,830,'nessun aumento nuovo')]},
]);
// ---------- BLOCCO 9 ----------
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FACCIAMO UN ESEMPIO',cap:'RATA DI 1.000 € + 1,4 % = 1.014 €: SOLO 14 € IN PIÙ, NON 100',capSize:42,items:[
  ...EQ(300,[['num','1.000 €','rata era di mille euro',{fs:64,sub:'L’ANNO SCORSO'}],['op','+','con l’uno'],['num','1,4 %','uno virgola quattro per cento',{fs:64,sub:'RIVALUTAZIONE'}],['op','=','diventa'],['num','1.014 €','mille e quattordici',{fs:64,fill:GF_,sub:'ORA'}]],64,300),
  VN('+ 14 €',540,620,'più alta di quattordici euro',{fs:90,fill:GF_,sub:'IN PIÙ'}),
  VN('100 €',1380,620,'non cento',{fs:90,fill:RF_,sub:'NON CENTO'})]},
]);
// ---------- BLOCCO 10 ----------
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TITOLO CHE FA RUMORE',cap:'SENZA TASSE, O CON MENO TASSE? COSA C’È DAVVERO DI SCRITTO',capSize:42,items:[
  I('hl',['TREDICESIMA DETASSATA'],960,290,'Tredicesima detassata'),
  VN('0 TASSE',520,550,'senza tasse',{fs:80,sub:'SENZA TASSE'}),
  VN('MENO TASSE',1400,550,'con meno tasse',{fs:80,fill:AMB,sub:'O CON MENO'}),
  VT('SCRITTO NELLA LEGGE',520,780,'davvero di scritto',GF_,40),
  VT('PROMESSA POLITICA',1400,780,'promessa politica',RF_,40)]},
]);
// ---------- BLOCCO 11 ----------
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FATTO NUMERO 1',cap:'AD OGGI NESSUNA NORMA APPROVATA: SOLO PROPOSTE, NON AUMENTI',capSize:42,items:[
  I('circ',['1',GF_],300,300,'Primo fatto'),
  I('doc',['DETASSAZIONE TREDICESIMA',760,240,undefined,36],820,310,'Ad oggi'),
  I('doc',['PROPOSTE',440,240,AMB,40],1560,310,'sono proposte'),
  I('stamp',['NESSUNA NORMA APPROVATA',RED_,44],680,540,'nessuna norma approvata'),
  VT('DIBATTITO SULLA MANOVRA',1480,540,'dibattito sulla manovra',GF_,32),
  ...EQ(770,[['num','PROPOSTA','una proposta',{fs:60,sub:'UNA PROPOSTA'}],['op','≠','non è'],['num','AUMENTO','un aumento',{fs:60,fill:GF_,sub:'UN AUMENTO'}]],60,300)]},
]);
// ---------- BLOCCO 12 ----------
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FATTO NUMERO 2',cap:'DUE PROPOSTE: TASSE A ZERO, OPPURE IMPOSTA RIDOTTA AL 10 O 15 %',capSize:40,items:[
  I('circ',['2','url(#g_head)'],300,290,'Secondo fatto'),
  VN('2 PROPOSTE',800,290,'sono due',{fs:80,sub:'SUL TAVOLO'}),
  VN('0 %',460,560,'azzerare le tasse',{fs:80,fill:GF_,sub:'DI TASSE'}),
  VT('FINO A CIRCA 15.000 €',1150,520,'circa quindicimila euro',AMB,36),
  VT('DI REDDITO',1150,610,'di reddito',AMB,36),
  VN('10 %',420,780,'al dieci',{fs:70,sub:'IMPOSTA RIDOTTA'}),
  VO('O',800,780,'o al quindici'),
  VN('15 %',1180,780,'al quindici per cento',{fs:70,fill:AMB,sub:'IMPOSTA RIDOTTA'})]},
]);
// ---------- BLOCCO 13 ----------
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FATTO NUMERO 3',cap:'LE IDEE COSTANO: CIRCA MEZZO MILIARDO, E LA MANOVRA È PIENA',capSize:42,items:[
  I('circ',['3',RF_],300,290,'Terzo fatto'),
  VN('COSTANO',900,290,'Queste idee costano',{fs:90,fill:RF_,sub:'IL PIÙ IMPORTANTE'}),
  VN('≈ 500 MILIONI €',960,540,'mezzo miliardo di euro',{fs:80,fill:RF_,sub:'PER LE SOLE TREDICESIME PIÙ BASSE'}),
  VT('MANOVRA PIENA DI SPESE',500,790,'la manovra già piena',GF_,36),
  VT('RISCHIANO DI SLITTARE',1330,730,'slittare',AMB,34),
  VT('O DI RESTARE RIDOTTE',1330,820,'restare ridotte',AMB,34)]},
]);
// ---------- BLOCCO 14 ----------
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E I PENSIONATI?',cap:'PER QUESTO DICEMBRE, REGOLE DI OGGI: E UNA COSA CAMBIA IL NETTO',capSize:40,items:[
  I('q',[110],300,300,'non è detto'),
  VT('NON È DETTO',850,300,'riguardino anche',RF_,56),
  VT('REGOLE DI OGGI',960,520,'le regole di oggi',GF_,56),
  I('warn',[],330,730,'nessuno ti spiega'),
  VN('NETTO',1000,730,'cambia il tuo netto',{fs:80,fill:AMB,sub:'CHE CAMBIA'})]},
]);
// ---------- BLOCCO 15 ----------
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO LASCIA DAVVERO?',cap:'STESSO LORDO, NETTO PIÙ BASSO: IL MOTIVO SONO LE DETRAZIONI',capSize:42,items:[
  I('q',[100],340,300,'quanto lascia davvero'),
  VN('NETTO',900,300,'la tredicesima?',{fs:80,sub:'DELLA TREDICESIMA'}),
  VN('RATA NORMALE',500,550,'rata normale',{fs:70,sub:'NETTO PIÙ ALTO'}),
  VN('TREDICESIMA',1440,550,'tredicesima netta',{fs:70,fill:AMB,sub:'NETTO PIÙ BASSO'}),
  VT('LE DETRAZIONI',960,790,'le detrazioni',GF_,56)]},
]);
// ---------- BLOCCO 16 ----------
SPECS[16]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA REGOLA',cap:'TASSATA SENZA DETRAZIONI: LO SCONTO LO HANNO LE ALTRE RATE',capSize:42,items:[
  I('doc',['TREDICESIMA',440,240,GRN,40],330,300,'La tredicesima viene tassata'),
  VT('ALIQUOTE IRPEF NORMALI',1100,260,'aliquote Irpef normali',GF_,36),
  VT('SENZA DETRAZIONI',1100,370,'senza le detrazioni',RF_,40),
  VN('SCONTO',500,540,'lo sconto fiscale',{fs:70,fill:GF_,sub:'FISCALE'}),
  VT('SULLA PENSIONE',1200,540,'sulla pensione',AMB,40),
  MESI(960,700,'sulle altre rate',i=>GF_),
  I('seg',[380,80,RF_,'TREDICESIMA'],960,810,['sulle altre rate',1.2])]},
]);
// ---------- BLOCCO 17 ----------
SPECS[17]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IN PRATICA',cap:'RATE NORMALI: MENO TASSE · TREDICESIMA: PIÙ TASSE · TOTALE UGUALE',capSize:40,items:[
  VN('MENO TASSE',500,300,'le rate normali pagano meno tasse',{fs:70,fill:GF_,sub:'RATE NORMALI'}),
  VN('PIÙ TASSE',1400,300,'ne paga di più',{fs:70,fill:AMB,sub:'TREDICESIMA'}),
  VN('TOTALE',800,540,'il totale è lo stesso',{fs:80,sub:'LO STESSO'}),
  I('chk',[80],1300,540,['è lo stesso',0.6]),
  VN('PIÙ MAGRA',500,770,'più magra',{fs:70,fill:AMB,sub:'LA TREDICESIMA'}),
  VT('ADESSO VEDI DI QUANTO',1480,770,'Adesso vedi di quanto',GF_,36)]},
]);
// ---------- BLOCCO 18 ----------
SPECS[18]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 1 · IL CASO PROMESSO',cap:'SOTTO 8.500 € ALL’ANNO L’IRPEF NON SI PAGA: 600 € NETTI',capSize:42,items:[
  I('circ',['1',GF_],300,290,'Primo caso'),
  VN('650 €',800,290,'seicentocinquanta euro al mese',{fs:80,sub:'AL MESE, CIRCA'}),
  VN('< 8.500 €',520,540,'sotto ottomilacinquecento euro',{fs:80,sub:'IN UN ANNO'}),
  I('stamp',['IRPEF: 0 €',GRN,50],1400,540,'non si paga'),
  VN('600 €',500,770,'Seicento lordi',{fs:70,sub:'LORDI'}),
  VO('=',860,770,['seicento netti',-0.5]),
  VN('600 €',1220,770,'seicento netti',{fs:70,fill:GF_,sub:'NETTI'})]},
]);
// ---------- BLOCCO 19 ----------
SPECS[19]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 2',cap:'1.000 € × 13 = 13.000 € · ALIQUOTA 23 % · NETTI 770 €',capSize:42,items:[
  I('circ',['2','url(#g_head)'],300,290,'Secondo caso'),
  VN('1.000 €',700,290,'Mille euro al mese',{fs:70,sub:'AL MESE'}),
  VT('ALIQUOTA 23 %',1400,290,'aliquota ventitré per cento',AMB,44),
  ...EQ(520,[['num','1.000 €','Il reddito',{fs:64,sub:'× 13 MESI'}],['op','=','dell’anno è'],['num','13.000 €','tredicimila euro',{fs:64,fill:GF_,sub:'REDDITO ANNUO'}]],64,300),
  ...EQ(760,[['num','1.000 €','Sulla tredicesima',{fs:60,sub:'LORDI'}],['op','−','si pagano'],['num','230 €','duecentotrenta euro',{fs:60,fill:RF_,sub:'IRPEF'}],['op','=','Netti,'],['num','770 €','settecentosettanta',{fs:60,fill:GF_,sub:'NETTI'}]],60,300)]},
]);
// ---------- BLOCCO 20 ----------
SPECS[20]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CONFRONTO',cap:'RATA NORMALE ≈ 900 € · TREDICESIMA 770 €: CIRCA 140 € IN MENO',capSize:42,items:[
  VN('≈ 900 €',500,300,'circa novecento euro netti',{fs:80,fill:GF_,sub:'RATA NORMALE · NETTI'}),
  VT('CON LE DETRAZIONI',1200,300,'le detrazioni',AMB,40),
  VN('770 €',500,560,'La tredicesima è più magra',{fs:80,fill:AMB,sub:'TREDICESIMA · NETTI'}),
  VN('− 140 €',1300,560,'centoquaranta euro',{fs:80,fill:RF_,sub:'CIRCA, IN MENO'}),
  I('arR',[],450,790,'più sale',0.8,-90),
  VT('PIÙ LA DIFFERENZA SI SENTE',1100,790,'più la differenza si sente',AMB,40)]},
]);
// ---------- BLOCCO 21 ----------
SPECS[21]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 3',cap:'1.500 € × 13 = 19.500 € · ALIQUOTA 23 % · NETTI 1.155 €',capSize:42,items:[
  I('circ',['3',GF_],300,290,'Terzo caso'),
  VN('1.500 €',700,290,'Millecinquecento euro al mese',{fs:70,sub:'AL MESE'}),
  VT('ALIQUOTA 23 %',1400,290,'sempre aliquota ventitré per cento',AMB,44),
  ...EQ(520,[['num','1.500 €','Reddito annuo',{fs:64,sub:'× 13 MESI'}],['op','=',['Reddito annuo',0.7]],['num','19.500 €','diciannovemilacinquecento',{fs:64,fill:GF_,sub:'REDDITO ANNUO'}]],64,300),
  ...EQ(760,[['num','1.500 €','Tredicesima lorda',{fs:60,sub:'LORDI'}],['op','−','Irpef trecentoquarantacinque'],['num','345 €','trecentoquarantacinque',{fs:60,fill:RF_,sub:'IRPEF'}],['op','=','netti millecentocinquantacinque'],['num','1.155 €','millecentocinquantacinque',{fs:60,fill:GF_,sub:'NETTI'}]],60,300)]},
]);
// ---------- BLOCCO 22 ----------
SPECS[22]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 4',cap:'2.000 € × 13 = 26.000 € · ALIQUOTA 23 % · NETTI 1.540 €',capSize:42,items:[
  I('circ',['4','url(#g_head)'],300,290,'Quarto caso'),
  VN('2.000 €',700,290,'Duemila euro al mese',{fs:70,sub:'AL MESE'}),
  VT('SOTTO I 28.000 €',1350,250,'sotto i ventottomila',AMB,40),
  VT('ALIQUOTA 23 %',1350,360,'ancora ventitré per cento',GF_,44),
  ...EQ(520,[['num','2.000 €','Reddito ventiseimila',{fs:64,sub:'× 13 MESI'}],['op','=',['Reddito ventiseimila',0.5]],['num','26.000 €','ventiseimila euro',{fs:64,fill:GF_,sub:'REDDITO ANNUO'}]],64,300),
  ...EQ(760,[['num','2.000 €','Irpef quattrocentosessanta',{fs:60,sub:'LORDI'}],['op','−',['quattrocentosessanta euro',-0.3]],['num','460 €','quattrocentosessanta euro',{fs:60,fill:RF_,sub:'IRPEF'}],['op','=','netti millecinquecentoquaranta'],['num','1.540 €','millecinquecentoquaranta euro',{fs:60,fill:GF_,sub:'NETTI'}]],60,300)]},
]);
// ---------- BLOCCO 23 ----------
SPECS[23]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 5 · LA SORPRESA',cap:'OLTRE I 28.000 € L’ULTIMA PARTE ENTRA NELLO SCAGLIONE DEL 33 %',capSize:40,items:[
  I('circ',['5',RF_],300,280,'quinto caso'),
  VN('3.000 €',700,280,'Tremila euro al mese',{fs:70,sub:'AL MESE'}),
  ...EQ(480,[['num','3.000 €','Il reddito',{fs:60,sub:'× 13 MESI'}],['op','=',['Il reddito',0.8]],['num','39.000 €','trentanovemila euro',{fs:60,fill:GF_,sub:'REDDITO ANNUO'}]],60,300),
  I('step',[240,90,'#2B6F77','23 %'],700,850,'l’ultima parte'),
  I('step',[240,140,AMB,'33 %'],960,850,'trentatré per cento'),
  I('step',[240,190,RF_,'43 %'],1220,850,['trentatré per cento',0.8])]},
]);
// ---------- BLOCCO 24 ----------
SPECS[24]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA TREDICESIMA DA 3.000 €',cap:'3.000 € − 990 € DI IRPEF = 2.010 € NETTI: QUASI MILLE EURO IN MENO',capSize:40,items:[
  ...EQ(300,[['num','3.000 €','Sulla tredicesima',{fs:64,sub:'LORDI'}],['op','−','l’Irpef è'],['num','990 €','novecentonovanta euro',{fs:64,fill:RF_,sub:'IRPEF 33 %'}],['op','=','Restano'],['num','2.010 €','duemiladieci euro netti',{fs:64,fill:GF_,sub:'NETTI'}]],64,300),
  VN('− 990 €',500,580,'Quasi mille euro in meno',{fs:80,fill:RF_,sub:'DAL LORDO'}),
  VT('LA RATA PIÙ RICCA DELL’ANNO?',1300,580,'la rata più ricca dell’anno',AMB,34)]},
]);
// ---------- BLOCCO 25 ----------
SPECS[25]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'NETTO PER 5 PENSIONI',cap:'LA TREDICESIMA NETTA PER CINQUE PENSIONI',items:[
  I('trow',[1300,'PENSIONE DA 600 €','600 €',GF_],960,250,'Seicento euro per chi'),
  I('trow',[1300,'PENSIONE DA 1.000 €','770 €',GF_],960,375,'Settecentosettanta'),
  I('trow',[1300,'PENSIONE DA 1.500 €','1.155 €',GF_],960,500,'Millecentocinquantacinque'),
  I('trow',[1300,'PENSIONE DA 2.000 €','1.540 €',GF_],960,625,'Millecinquecentoquaranta'),
  I('trow',[1300,'PENSIONE DA 3.000 €','2.010 €',AMB],960,750,'Duemiladieci')]},
]);
// ---------- BLOCCO 26 ----------
SPECS[26]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ATTENZIONE',cap:'SONO ESEMPI: SENZA ALTRI REDDITI E SENZA ADDIZIONALI',items:[
  I('warn',[],300,300,'Attenzione'),
  VT('SONO SOLO ESEMPI',900,300,'sono esempi',AMB,56),
  I('doc',['SENZA ALTRI REDDITI',560,240,GRN,36],520,560,'senza altri redditi'),
  I('doc',['SENZA ADDIZIONALI',560,240,AMB,36],1300,560,'le addizionali'),
  VT('IL TUO NETTO CAMBIA',500,800,'il tuo netto cambia',AMB,44),
  VT('IL NUMERO ESATTO: INPS.IT',1250,800,'te lo dice l’Inps',GF_,40)]},
]);
// ---------- BLOCCO 27 ----------
SPECS[27]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO NON È FINITO',cap:'MANCANO DUE VOCI: UN EXTRA PER LE BASSE, UNA PER QUASI TUTTI',capSize:42,items:[
  I('calc',[],300,300,'Ma il conto di dicembre'),
  VN('2 VOCI',900,300,'Mancano due voci',{fs:80,sub:'ANCORA DA VEDERE'}),
  I('circ',['1',GF_],300,560,'Una è un extra'),
  VN('EXTRA',700,560,'per le pensioni basse',{fs:70,fill:GF_,sub:'PENSIONI BASSE'}),
  I('circ',['2','url(#g_head)'],1100,560,'L’altra riguarda'),
  VN('PIÙ SOLDI',1500,560,'più soldi di quanto pensi',{fs:70,fill:GF_,sub:'IN BANCA'}),
  VT('PARTO DALL’EXTRA',700,790,'Parto dall’extra',AMB,44)]},
]);
// ---------- BLOCCO 28 ----------
SPECS[28]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IMPORTO AGGIUNTIVO',cap:'A DICEMBRE UN EXTRA DI 154,94 €, ESENTASSE',items:[
  VT('PENSIONI BASSE',500,300,'pensioni basse',AMB,44),
  VN('EXTRA',1300,300,'un extra',{fs:80,fill:GF_,sub:'A DICEMBRE'}),
  I('doc',['IMPORTO AGGIUNTIVO',640,250,GRN,38],500,590,'importo aggiuntivo'),
  VN('154,94 €',1350,560,'centocinquantaquattro euro',{fs:80,fill:GF_,sub:'ESENTASSE'}),
  I('stamp',['ESENTASSE',GRN,46],1350,760,'esentasse')]},
]);
// ---------- BLOCCO 29 ----------
SPECS[29]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CHI LO RICEVE',cap:'PENSIONE FINO A 7.954 €, REDDITO SOTTO 11.931 €, COPPIA 23.862 €',capSize:40,items:[
  I('doc',['PENSIONE TOTALE',520,240,undefined,38],400,320,'la pensione totale'),
  VN('≈ 7.954 €',1200,300,'settemilanovecentocinquantaquattro euro',{fs:80,sub:'ALL’ANNO · LIMITE'}),
  VN('< 11.931 €',620,580,'undicimilanovecentotrentuno euro',{fs:80,sub:'REDDITO PERSONALE'}),
  VN('< 23.862 €',1450,580,'ventitremilaottocentosessantadue euro',{fs:80,fill:GF_,sub:'LIMITE DI COPPIA'}),
  VT('PER CHI È SPOSATO',1450,780,'Per chi è sposato',AMB,40)]},
]);
// ---------- BLOCCO 30 ----------
SPECS[30]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'A CHI NON SPETTA',cap:'NON SPETTA A CHI HA SOLO ASSEGNO O PENSIONE SOCIALE, O INVALIDITÀ CIVILE',capSize:36,items:[
  I('doc',['ASSEGNO SOCIALE',440,240,undefined,34],440,300,'assegno sociale'),
  I('doc',['PENSIONE SOCIALE',440,240,undefined,34],960,300,'pensione sociale'),
  I('doc',['INVALIDITÀ CIVILE',440,240,undefined,34],1480,300,'invalidità civile'),
  I('cross',[100,55],440,300,['assegno sociale',0.6]),
  I('cross',[100,55],960,300,['pensione sociale',0.6]),
  I('cross',[100,55],1480,300,['invalidità civile',0.6]),
  I('stamp',['NESSUNA DOMANDA',GRN,50],700,600,'Non serve domanda'),
  VT('LO PAGA L’INPS',1450,600,'lo paga l’Inps',GF_,48),
  VT('NON CI RIENTRI? RESTA!',960,790,'Non ci rientri',AMB,56)]},
]);
// ---------- BLOCCO 31 ----------
SPECS[31]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA VOCE PER TUTTI',cap:'NOVEMBRE È L’ULTIMA RATA: POI LA TRATTENUTA FINISCE',items:[
  I('doc',['ADDIZIONALE REGIONALE',760,240,GRN,36],560,290,'l’addizionale regionale'),
  VT('TRATTENUTA A RATE',1480,290,'ti trattiene a rate',AMB,44),
  MESI(960,540,'undici rate',i=>i==10?AMB:GF_,11,132),
  VT('DA GENNAIO A NOVEMBRE',960,670,'da gennaio a novembre',GF_,44),
  I('stamp',['FINE TRATTENUTA',GRN,52],960,790,'la trattenuta finisce')]},
]);
// ---------- BLOCCO 32 ----------
SPECS[32]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CONGUAGLIO DEL 730',cap:'LE RATE DEL 730 FINISCONO A NOVEMBRE: A DICEMBRE LA RATA SALE',capSize:40,items:[
  I('doc',['MODELLO 730',520,240,GRN,42],400,290,'del settecentotrenta'),
  VT('RATE DI CONGUAGLIO',1200,290,'rate del conguaglio',AMB,44),
  VN('NOVEMBRE',440,560,'entro novembre',{fs:70,fill:AMB,sub:'ULTIMA RATA'}),
  VN('TRATTENUTE',1100,560,'quelle trattenute non ci sono più',{fs:70,fill:RF_,sub:'NON CI SONO PIÙ'}),
  VN('RATA',1650,560,'la rata, di solito, sale',{fs:70,fill:GF_,sub:'SALE'}),
  VT('A DICEMBRE: NIENTE TRATTENUTE, RATA PIÙ ALTA',960,780,'nella rata di dicembre',GF_,40)]},
]);
// ---------- BLOCCO 33 ----------
SPECS[33]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO?',cap:'LA CIFRA DELL’ADDIZIONALE DI NOVEMBRE, A DICEMBRE RESTA A TE',capSize:42,items:[
  I('q',[100],300,290,'Quanto?'),
  I('pay',['CEDOLINO'],760,330,'Guarda il cedolino'),
  VT('ADDIZIONALE REGIONALE',1400,300,'addizionale regionale',AMB,40),
  VN('QUELLA CIFRA',600,700,'Quella cifra',{fs:70,fill:GF_,sub:'A DICEMBRE RESTA A TE'}),
  I('chk',[60],1100,700,'resta a te'),
  I('stamp',['NON È UN AUMENTO',RED_,44],1500,640,'Non è un aumento'),
  VT('SONO SOLDI TUOI',1500,740,'sono soldi tuoi',GF_,40),
  VT('DA GENNAIO RIPARTONO',1500,830,'ripartono',AMB,36)]},
]);
// ---------- BLOCCO 34 ----------
SPECS[34]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TRUCCO PRATICO',cap:'MYINPS CON LO SPID → CEDOLINO → CERTIFICATO DI PENSIONE',capSize:42,items:[
  I('calc',[],260,300,'Ora il trucco pratico'),
  VT('NIENTE CALCOLI A MANO',900,300,'calcoli a mano',GF_,40),
  I('br',['inps.it',600,280],1500,330,'Entra in Mai Inps'),
  VT('CON LO SPID',1500,520,'con lo Spid',AMB,44),
  I('row',['PENSIONE E PREVIDENZA',860,true],500,620,'Pensione e previdenza'),
  I('row',['CEDOLINO DELLA PENSIONE',860,true],500,700,'Cedolino della pensione'),
  I('row',['CERTIFICATO DI PENSIONE',860,true],500,780,'Certificato di pensione'),
  I('doc',['OBISM',520,240,GRN,52],1450,700,'Obis emme')]},
]);
// ---------- BLOCCO 35 ----------
SPECS[35]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DENTRO IL CERTIFICATO',cap:'LA TUA PENSIONE, LA TREDICESIMA, LE TRATTENUTE, LORDO E NETTO',capSize:42,items:[
  I('row',['PENSIONE, RATA PER RATA',860,true],500,290,'rata per rata'),
  I('row',['LA TREDICESIMA',860,true],500,410,'la tredicesima'),
  I('row',['LE TRATTENUTE FISCALI',860,true],500,530,'le trattenute fiscali'),
  I('row',['IL LORDO E IL NETTO',860,true],500,650,'il lordo e il netto'),
  I('pay',['CEDOLINO'],1450,420,'il cedolino di dicembre'),
  I('chk',[70],1450,720,'controlla lì'),
  VT('IL NUMERO VERO, NON UNA STIMA',800,810,'numero vero',AMB,44)]},
]);
// ---------- BLOCCO 36 ----------
SPECS[36]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RICAPITOLO',cap:'RATA LORDA IN PIÙ · DETASSAZIONE SOLO PROPOSTA · NETTO DI DICEMBRE SU',capSize:38,items:[
  I('circ',['1',GF_],400,270,'Ricapitolo'),
  VN('RATA IN PIÙ',900,270,'una rata lorda in più',{fs:64,sub:'LA TREDICESIMA'}),
  I('circ',['2','url(#g_head)'],400,440,'La detassazione'),
  VN('PROPOSTA',900,440,'solo una proposta',{fs:64,fill:AMB,sub:'LA DETASSAZIONE'}),
  I('circ',['3',RF_],400,610,'E il tuo netto'),
  VN('NETTO',900,610,'il tuo netto di dicembre',{fs:64,fill:GF_,sub:'DI DICEMBRE'}),
  I('arR',[],1300,610,'sale anche',1,-90),
  VT('SCRIVIMI QUANTO PRENDI → IL TUO NETTO',960,800,'Scrivimi quanto prendi',GF_,44)]},
]);
// ---------- BLOCCO 37 (slide finale con il disclaimer; destra-basso libero per la schermata finale) ----------
SPECS[37]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'A NOVEMBRE',cap:'ESCE IL DECRETO SULLA RIVALUTAZIONE · ISCRIVITI E ATTIVA LA CAMPANELLA',capSize:38,items:[
  I('cal',['NOVEMBRE','2026',130,'DECRETO'],330,540,'A novembre'),
  I('doc',['DECRETO',520,240,undefined,40],900,330,'il decreto'),
  I('btn',['ISCRIVITI'],900,640,'iscriviti'),
  I('bell',[],1500,520,'la campanella')]},
 {at:'Regole e importi cambiano',top:'VERIFICA SEMPRE',cap:'VERIFICA SEMPRE SUL SITO DELL’INPS · GRAZIE PER AVER GUARDATO!',capSize:42,items:[
  I('dbg',[1120,500],700,450,['Regole e importi cambiano',-0.5]),
  I('dline',['REGOLE E IMPORTI CAMBIANO','#fff',44],700,380,['Regole e importi cambiano',0.9]),
  I('dline',['VERIFICA SUL SITO DELL’INPS','#7FF0D2',40],700,470,'verifica sul sito'),
  I('dline',['INFORMAZIONE GENERALE, NON CONSULENZA','#FFB838',40],700,560,'Informazione generale'),
  I('dline',['CANALE NON AFFILIATO ALL’INPS','#fff',40],700,650,'Canale non affiliato')]},
]);
