// ===== V5 (tredicesima 2026): ogni elemento compare quando la voce lo dice (motore sincronizzato, regola 80 %) =====
const SPECS={};
const GF_='url(#g_badge)',RF_='url(#g_red)',PF_='url(#g_paper)',DF_='#0B4A50';
const VT=(s,x,y,at,fill,fs)=>I('tag',[s,fill||AMB,(fill&&fill!==AMB)?'#fff':'#5A3300',fs||44],x,y,at);
const VN=(s,x,y,at,o)=>{o=o||{};return I('num',[s,o.fs||76,o.fill||PF_,o.sub,o.subfill,o.minw],x,y,at);};
const VO=(s,x,y,at)=>I('op',[s],x,y,at);
const MI='GFMAMGLASOND'.split('');
// riga di mesi (12 o 11 quadratini): fillf(i) dà il colore di ogni mese
function MESI(y,at,fillf,n){n=n||12;const out=[];const step=n==11?132:118;
 for(let i=0;i<n;i++){const x=960+(i-(n-1)/2)*step;out.push(I('seg',[100,90,fillf(i),MI[i]],x,y,[at,i*0.06]));}return out;}

// ---------- BLOCCO 1 ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DICEMBRE 2026',cap:'L’INPS TI PAGA UNA MENSILITÀ IN PIÙ',items:[
  I('cal',['DICEMBRE','13ª',200,'MENSILITÀ'],560,540,'Dicembre.'),
  VN('+ 1 RATA',1330,400,'una mensilità in più',{fs:120,fill:GF_,sub:'IN PIÙ A DICEMBRE'})]},
 {at:'Se la tua pensione',top:'PENSIONE DI MILLE EURO',cap:'MILLE EURO LORDI: IN BANCA ARRIVANO MOLTI MENO',items:[
  VN('1.000 €',480,400,'Se la tua pensione',{fs:110,sub:'LORDI'}),
  I('arR',[],960,420,'in banca non arrivano'),
  VN('? €',1430,400,'Arrivano molti meno',{fs:110,fill:RF_,sub:'IN BANCA',minw:520})]},
 {at:'E il motivo',top:'IL MOTIVO',cap:'NON È QUELLO CHE TI HANNO RACCONTATO',items:[
  I('q',[110],400,430,'E il motivo'),
  VT('NON È QUELLO CHE TI HANNO RACCONTATO',1260,430,'quello che ti hanno raccontato',AMB,36)]},
]);
// ---------- BLOCCO 2 ----------
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'I TITOLONI',cap:'TREDICESIMA DETASSATA? TREDICESIMA PIÙ ALTA?',items:[
  I('hl',['TREDICESIMA DETASSATA'],960,350,'tredicesima detassata'),
  I('hl',['TREDICESIMA PIÙ ALTA'],960,620,'tredicesima più alta')]},
 {at:'Non ti dico adesso',top:'VERO O FALSO?',cap:'TE LO DICO DOPO AVER FATTO I CONTI',items:[
  I('q',[110],560,430,'Non ti dico adesso'),
  I('vf',[true],1130,330,'è vero'),
  I('vf',[false],1130,520,'o falso')]},
 {at:'Prima ti faccio vedere',top:'I CONTI VERI',cap:'CINQUE PENSIONI DIVERSE, UNA ALLA VOLTA',items:[
  I('calc',[],960,330,'i conti veri'),
  I('circ',['1',GF_],560,700,'uno alla volta'),
  I('circ',['2','url(#g_head)'],760,700,['uno alla volta',0.3]),
  I('circ',['3',GF_],960,700,['uno alla volta',0.6]),
  I('circ',['4','url(#g_head)'],1160,700,['con cinque pensioni',0.1]),
  I('circ',['5',GF_],1360,700,['con cinque pensioni',0.5])]},
]);
// ---------- BLOCCO 3 ----------
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ALLA FINE DEL VIDEO',cap:'DUE COSE CHE TI DICO SOLO ALLA FINE',items:[
  VN('2 COSE',960,380,'Ci sono due cose',{fs:150,sub:'SOLO ALLA FINE',minw:700})]},
 {at:'Un caso in cui',top:'COSA NUMERO 1',cap:'UN CASO IN CUI LA TREDICESIMA ARRIVA INTERA',items:[
  I('circ',['1',GF_],440,420,'Un caso in cui'),
  VN('INTERA',1150,400,'arriva intera',{fs:120,fill:GF_,sub:'SENZA PERDERE UN EURO'})]},
 {at:'E una voce di dicembre',top:'COSA NUMERO 2',cap:'UNA VOCE DI DICEMBRE CHE FA SALIRE QUELLO CHE ARRIVA',items:[
  I('circ',['2','url(#g_head)'],440,420,'E una voce di dicembre'),
  I('doc',['VOCE DI DICEMBRE',620,300,undefined,38],900,430,'voce di dicembre'),
  I('arR',[],1330,430,'fa salire',1,-90),
  VT('IN BANCA',1620,430,'in banca',GF_,40),
  VT('QUASI NESSUNO LA CONTA',960,700,'quasi nessuno conta',AMB,44)]},
 {at:'Io sono Conti in Pensione',top:'CONTI IN PENSIONE',cap:'COMINCIAMO',items:[
  VN('CONTI IN PENSIONE',960,400,'Conti in Pensione',{fs:96,sub:'COMINCIAMO',minw:900})]},
]);
// ---------- BLOCCO 4 ----------
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PARTIAMO DAL SEMPLICE',cap:'LA TREDICESIMA È UNA MENSILITÀ IN PIÙ',items:[
  I('pay',['CEDOLINO'],480,500,'La tredicesima è una mensilità'),
  VN('+ 1 RATA',1330,380,'una mensilità in più',{fs:120,fill:GF_,sub:'TREDICESIMA'}),
  VT('CON LA RATA DI DICEMBRE',1330,640,'insieme alla rata di dicembre',AMB,44)]},
 {at:'Quest’anno la rata',top:'QUANDO ARRIVA',cap:'MARTEDÌ 1 DICEMBRE 2026 · DATA DA CONFERMARE',items:[
  I('cal',['DICEMBRE','1',230,'MARTEDÌ'],560,540,'primo dicembre'),
  VT('DOVREBBE ARRIVARE',1330,420,'dovrebbe arrivare',AMB,48),
  VT('RATA DI DICEMBRE',1330,560,'Quest’anno la rata',GF_,44)]},
 {at:'Non devi fare',top:'NESSUNA DOMANDA',cap:'ARRIVA DA SOLA, INSIEME ALLA PENSIONE',items:[
  I('chk',[100],560,430,'Non devi fare'),
  I('stamp',['NESSUNA DOMANDA',GRN,60],1250,430,'nessuna domanda')]},
]);
// ---------- BLOCCO 5 ----------
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO È, IN LORDO?',cap:'SE SEI IN PENSIONE DA TUTTO L’ANNO: UNA RATA INTERA',items:[
  I('q',[110],480,430,'Quanto è'),
  VN('12 MESI',1250,400,'da tutto l’anno',{fs:120,sub:'IN PENSIONE'})]},
 {at:'Mille euro lordi al mese',top:'ESEMPIO',cap:'1.000 € LORDI AL MESE = 1.000 € LORDI DI TREDICESIMA',items:[
  VN('1.000 €',480,400,'Mille euro lordi al mese',{fs:110,sub:'RATA MENSILE'}),
  VO('=',960,400,['mille euro lordi di tredicesima',-0.4]),
  VN('1.000 €',1440,400,'mille euro lordi di tredicesima',{fs:110,fill:GF_,sub:'TREDICESIMA'})]},
 {at:'Fin qui',top:'FIN QUI',cap:'FIN QUI, NESSUNA SORPRESA',items:[
  I('chk',[110],960,400,'Fin qui'),
  VT('NESSUNA SORPRESA',960,640,'nessuna sorpresa',GF_,52)]},
]);
// ---------- BLOCCO 6 ----------
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'USCITO DURANTE L’ANNO',cap:'LA TREDICESIMA È PIÙ PICCOLA',items:[
  ...MESI(400,'durante l’anno',i=>'#2B6F77'),
  VT('MENO MESI DI PENSIONE',960,640,'più piccola',AMB,48)]},
 {at:'Ne prendi un dodicesimo',top:'UN DODICESIMO A MESE',cap:'1/12 DELLA RATA PER OGNI MESE DI PENSIONE',items:[
  VN('1/12',560,400,'un dodicesimo',{fs:150,sub:'DELLA RATA'}),
  VT('PER OGNI MESE',1350,360,'per ogni mese',AMB,48),
  VT('DI PENSIONE',1350,480,'mese di pensione',AMB,48)]},
 {at:'Esempio: pensione da luglio',top:'ESEMPIO: DA LUGLIO',cap:'LUGLIO–DICEMBRE = 6 MESI = LA METÀ DI UNA RATA',items:[
  ...MESI(380,'Esempio: pensione da luglio',i=>i<6?'#2B6F77':GF_),
  VN('½ RATA',960,650,'la metà di una rata',{fs:100,fill:GF_,sub:'6 MESI SU 12'})]},
]);
// ---------- BLOCCO 7 ----------
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA DOMANDA DI TUTTI',cap:'QUEST’ANNO LA TREDICESIMA È PIÙ ALTA?',items:[
  I('q',[110],480,430,'la domanda che si fanno tutti'),
  VT('PIÙ ALTA?',1250,430,'è più alta',AMB,64)]},
 {at:'La risposta è sì',top:'LA RISPOSTA',cap:'SÌ, MA NON PER UN REGALO DI DICEMBRE',items:[
  I('chk',[100],480,430,'è sì'),
  VT('MA NON È UN REGALO',1230,430,'non per un regalo di dicembre',RF_,48)]},
 {at:'Ti spiego da dove',top:'DA DOVE VIENE',cap:'IL POCO IN PIÙ NON VIENE DA DOVE PENSI',items:[
  I('q',[100],560,430,'da dove viene'),
  VT('NON È DOVE PENSI',1330,430,'non è dove pensi',AMB,52)]},
]);
// ---------- BLOCCO 8 ----------
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'GENNAIO 2026',cap:'L’INPS HA RIVALUTATO LE PENSIONI DELL’1,4 %',items:[
  I('cal',['GENNAIO','1',230,'2026'],520,540,'A gennaio'),
  VN('+ 1,4 %',1330,400,'uno virgola quattro per cento',{fs:130,sub:'IN VIA PROVVISORIA'})]},
 {at:'Quella rivalutazione è già',top:'GIÀ DENTRO OGNI RATA',cap:'ANCHE DENTRO LA TREDICESIMA: È GIÀ NEI TUOI IMPORTI',items:[
  ...MESI(330,'già dentro ogni rata',i=>'#2B6F77'),
  I('seg',[420,100,GF_,'TREDICESIMA'],960,540,'anche dentro la tredicesima'),
  VT('+ 1,4 % GIÀ APPLICATO',960,740,'già dentro ogni rata',AMB,44)]},
 {at:'A dicembre non scatta',top:'A DICEMBRE',cap:'A DICEMBRE NON SCATTA NESSUN AUMENTO NUOVO',items:[
  I('cal',['DICEMBRE','1',230,'2026'],520,540,'A dicembre non scatta'),
  I('stamp',['NESSUN AUMENTO NUOVO',RED_,52],1350,430,'nessun aumento nuovo')]},
]);
// ---------- BLOCCO 9 ----------
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FACCIAMO UN ESEMPIO',cap:'RATA DI 1.000 € + 1,4 % = 1.014 €',items:[
  ...EQ(420,[['num','1.000 €','rata era di mille euro',{fs:70,sub:'L’ANNO SCORSO'}],['op','+','con l’uno'],['num','1,4 %','uno virgola quattro per cento',{fs:70,sub:'RIVALUTAZIONE'}],['op','=','diventa'],['num','1.014 €','mille e quattordici',{fs:70,fill:GF_,sub:'ORA'}]],70,300)]},
 {at:'La tredicesima lorda',top:'LA DIFFERENZA',cap:'SOLO 14 € IN PIÙ: QUATTORDICI, NON CENTO',items:[
  VN('+ 14 €',560,400,'più alta di quattordici euro',{fs:140,fill:GF_,sub:'IN PIÙ'}),
  VN('100 €',1330,400,'non cento',{fs:140,fill:RF_,sub:'NON CENTO'}),
  ]},
]);
// ---------- BLOCCO 10 ----------
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TITOLO CHE FA RUMORE',cap:'TREDICESIMA DETASSATA',items:[
  I('hl',['TREDICESIMA DETASSATA'],960,420,'Tredicesima detassata')]},
 {at:'Cioè senza tasse',top:'DETASSATA?',cap:'SENZA TASSE, O CON MENO TASSE',items:[
  VN('0 TASSE',520,400,'senza tasse',{fs:100,sub:'SENZA TASSE'}),
  VN('MENO TASSE',1400,400,'con meno tasse',{fs:96,fill:AMB,sub:'O CON MENO'})]},
 {at:'Vediamo cosa',top:'VEDIAMO I FATTI',cap:'COSA C’È DAVVERO DI SCRITTO, E COSA È SOLO PROMESSA',items:[
  I('doc',['SCRITTO NELLA LEGGE',600,300,GRN,36],520,430,'davvero di scritto'),
  I('doc',['PROMESSA POLITICA',600,300,RED_,36],1400,430,'promessa politica')]},
]);
// ---------- BLOCCO 11 ----------
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FATTO NUMERO 1',cap:'AD OGGI NESSUNA NORMA APPROVATA',items:[
  I('circ',['1',GF_],440,420,'Primo fatto'),
  I('doc',['DETASSAZIONE TREDICESIMA',760,260,undefined,36],1150,360,'Ad oggi'),
  I('stamp',['NESSUNA NORMA APPROVATA',RED_,52],1150,640,'nessuna norma approvata')]},
 {at:'Quello che c’è',top:'COSA C’È DAVVERO',cap:'SOLO PROPOSTE, NATE NEL DIBATTITO SULLA MANOVRA',items:[
  I('doc',['PROPOSTE',520,300,AMB,40],520,430,'sono proposte'),
  VT('DIBATTITO SULLA MANOVRA',1350,430,'dibattito sulla manovra',GF_,40)]},
 {at:'E una proposta non è',top:'PROPOSTA ≠ AUMENTO',cap:'UNA PROPOSTA NON È UN AUMENTO',items:[
  ...EQ(420,[['num','PROPOSTA','una proposta',{fs:100,sub:'UNA PROPOSTA'}],['op','≠','non è'],['num','AUMENTO','un aumento',{fs:100,fill:GF_,sub:'UN AUMENTO'}]],100,300)]},
]);
// ---------- BLOCCO 12 ----------
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FATTO NUMERO 2',cap:'LE PROPOSTE SONO DUE',items:[
  I('circ',['2','url(#g_head)'],440,420,'Secondo fatto'),
  VN('2 PROPOSTE',1150,400,'sono due',{fs:130,sub:'SUL TAVOLO'})]},
 {at:'Una vorrebbe azzerare',top:'PROPOSTA A',cap:'TASSE A ZERO SULLE TREDICESIME PIÙ BASSE',items:[
  VN('0 %',540,400,'azzerare le tasse',{fs:150,fill:GF_,sub:'DI TASSE'}),
  VT('FINO A CIRCA 15.000 €',1350,380,'circa quindicimila euro',AMB,44),
  VT('DI REDDITO',1350,500,'di reddito',AMB,44)]},
 {at:'L’altra vorrebbe',top:'PROPOSTA B',cap:'IMPOSTA RIDOTTA, AL 10 % O AL 15 %',items:[
  VN('10 %',500,400,'al dieci',{fs:130,sub:'IMPOSTA RIDOTTA'}),
  VO('O',960,400,'o al quindici'),
  VN('15 %',1420,400,'al quindici per cento',{fs:130,fill:AMB,sub:'IMPOSTA RIDOTTA'})]},
]);
// ---------- BLOCCO 13 ----------
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FATTO NUMERO 3',cap:'QUESTE IDEE COSTANO',items:[
  I('circ',['3',RF_],440,420,'Terzo fatto'),
  VN('COSTANO',1150,400,'Queste idee costano',{fs:120,fill:RF_,sub:'IL PIÙ IMPORTANTE'})]},
 {at:'Per le sole tredicesime',top:'QUANTO COSTANO',cap:'SOLO PER LE TREDICESIME PIÙ BASSE: CIRCA MEZZO MILIARDO',items:[
  VN('≈ 500 MILIONI €',960,400,'mezzo miliardo di euro',{fs:96,fill:RF_,sub:'PER LE SOLE TREDICESIME PIÙ BASSE'})]},
 {at:'Con la manovra già piena',top:'MANOVRA PIENA DI SPESE',cap:'LE MISURE COSTOSE RISCHIANO DI SLITTARE O RESTARE RIDOTTE',items:[
  I('doc',['MANOVRA',520,300,undefined,40],520,430,'la manovra già piena'),
  VT('RISCHIANO DI SLITTARE',1350,380,'slittare',AMB,40),
  VT('O DI RESTARE RIDOTTE',1350,500,'restare ridotte',AMB,40)]},
]);
// ---------- BLOCCO 14 ----------
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E I PENSIONATI?',cap:'NON È DETTO CHE RIGUARDINO ANCHE I PENSIONATI',items:[
  I('q',[110],480,430,'non è detto'),
  VT('NON È DETTO',1250,430,'riguardino anche',RF_,60)]},
 {at:'Quindi, per questo dicembre',top:'PER QUESTO DICEMBRE',cap:'I CONTI SI FANNO CON LE REGOLE DI OGGI',items:[
  I('cal',['DICEMBRE','2026',130,'REGOLE DI OGGI'],520,540,'per questo dicembre'),
  VT('REGOLE DI OGGI',1350,430,'le regole di oggi',GF_,52)]},
 {at:'Ed è proprio qui',top:'NESSUNO TE LO SPIEGA',cap:'UNA COSA CHE CAMBIA IL TUO NETTO',items:[
  I('warn',[],480,430,'nessuno ti spiega'),
  VN('NETTO',1250,400,'cambia il tuo netto',{fs:120,fill:AMB,sub:'CHE CAMBIA'})]},
]);
// ---------- BLOCCO 15 ----------
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO LASCIA DAVVERO?',cap:'LA TREDICESIMA NETTA',items:[
  I('q',[110],480,430,'quanto lascia davvero'),
  VN('NETTO',1250,400,'la tredicesima?',{fs:130,sub:'DELLA TREDICESIMA'})]},
 {at:'Ti faccio vedere perché',top:'PIÙ BASSA DI UNA RATA',cap:'STESSO LORDO, NETTO PIÙ BASSO',items:[
  VN('RATA NORMALE',500,400,'rata normale',{fs:80,sub:'NETTO PIÙ ALTO'}),
  VN('TREDICESIMA',1440,400,'tredicesima netta',{fs:80,fill:AMB,sub:'NETTO PIÙ BASSO'})]},
 {at:'Il motivo sono',top:'IL MOTIVO',cap:'LE DETRAZIONI',items:[
  VN('DETRAZIONI',960,400,'le detrazioni',{fs:130,fill:GF_,sub:'IL MOTIVO',minw:900})]},
]);
// ---------- BLOCCO 16 ----------
SPECS[16]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA REGOLA',cap:'TASSATA CON LE ALIQUOTE IRPEF NORMALI, MA SENZA DETRAZIONI',items:[
  I('doc',['TREDICESIMA',520,300,GRN,40],480,430,'La tredicesima viene tassata'),
  VT('ALIQUOTE IRPEF NORMALI',1350,360,'aliquote Irpef normali',GF_,40),
  VT('SENZA DETRAZIONI',1350,500,'senza le detrazioni',RF_,44)]},
 {at:'Le detrazioni, cioè',top:'COSA SONO LE DETRAZIONI',cap:'LO SCONTO FISCALE SULLA PENSIONE',items:[
  VN('SCONTO',540,400,'lo sconto fiscale',{fs:120,fill:GF_,sub:'FISCALE'}),
  VT('SULLA PENSIONE',1350,430,'sulla pensione',AMB,52)]},
 {at:'l’Inps le applica',top:'DOVE LE APPLICA L’INPS',cap:'SULLE ALTRE RATE, NON SULLA TREDICESIMA',items:[
  ...MESI(360,'sulle altre rate',i=>GF_),
  I('seg',[420,100,RF_,'TREDICESIMA'],960,560,'sulle altre rate'),
  VT('DETRAZIONI SOLO SULLE ALTRE RATE',960,740,'altre rate',AMB,40)]},
]);
// ---------- BLOCCO 17 ----------
SPECS[17]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IN PRATICA',cap:'RATE NORMALI: MENO TASSE · TREDICESIMA: PIÙ TASSE',items:[
  VN('MENO TASSE',540,400,'le rate normali pagano meno tasse',{fs:84,fill:GF_,sub:'RATE NORMALI'}),
  VN('PIÙ TASSE',1380,400,'ne paga di più',{fs:84,fill:AMB,sub:'TREDICESIMA'})]},
 {at:'Alla fine dell’anno',top:'A FINE ANNO',cap:'IL TOTALE DELLE TASSE È LO STESSO',items:[
  VN('TOTALE',960,380,'il totale è lo stesso',{fs:120,sub:'LO STESSO',minw:700}),
  I('chk',[90],1500,420,['è lo stesso',0.5])]},
 {at:'Ma a dicembre',top:'MA A DICEMBRE',cap:'LA MENSILITÀ IN PIÙ SEMBRA PIÙ MAGRA',items:[
  VN('PIÙ MAGRA',960,380,'più magra',{fs:130,fill:AMB,sub:'LA TREDICESIMA',minw:800}),
  VT('ADESSO VEDI DI QUANTO',960,680,'Adesso vedi di quanto',GF_,48)]},
]);
// ---------- BLOCCO 18 ----------
SPECS[18]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 1 · IL CASO PROMESSO',cap:'PENSIONE FINO A CIRCA 650 € AL MESE',items:[
  I('circ',['1',GF_],440,420,'Primo caso'),
  VN('650 €',1150,400,'seicentocinquanta euro al mese',{fs:130,sub:'AL MESE, CIRCA'})]},
 {at:'Sul totale dell’anno',top:'SUL TOTALE DELL’ANNO',cap:'SOTTO 8.500 € ALL’ANNO L’IRPEF NON SI PAGA',items:[
  VN('< 8.500 €',520,400,'sotto ottomilacinquecento euro',{fs:110,sub:'IN UN ANNO'}),
  I('stamp',['IRPEF: 0 €',GRN,60],1420,400,'non si paga')]},
 {at:'Seicento lordi',top:'RISULTATO',cap:'600 € LORDI = 600 € NETTI: ARRIVA INTERA',items:[
  VN('600 €',480,400,'Seicento lordi',{fs:120,sub:'LORDI'}),
  VO('=',960,400,['seicento netti',-0.5]),
  VN('600 €',1440,400,'seicento netti',{fs:120,fill:GF_,sub:'NETTI'})]},
]);
// ---------- BLOCCO 19 ----------
SPECS[19]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 2',cap:'MILLE EURO AL MESE',items:[
  I('circ',['2','url(#g_head)'],440,420,'Secondo caso'),
  VN('1.000 €',1150,400,'Mille euro al mese',{fs:130,sub:'AL MESE'})]},
 {at:'Il reddito dell’anno',top:'IL CALCOLO',cap:'1.000 € × 13 = 13.000 € ALL’ANNO · ALIQUOTA 23 %',items:[
  ...EQ(380,[['num','1.000 €','Il reddito',{fs:80,sub:'× 13 MESI'}],['op','=','dell’anno è'],['num','13.000 €','tredicimila euro',{fs:80,fill:GF_,sub:'REDDITO ANNUO'}]],80,300),
  VN('23 %',960,720,'aliquota ventitré per cento',{fs:90,fill:AMB,sub:'ALIQUOTA'})]},
 {at:'Sulla tredicesima si pagano',top:'LA TREDICESIMA',cap:'1.000 € − 230 € DI IRPEF = 770 € NETTI',items:[
  ...EQ(420,[['num','1.000 €','Sulla tredicesima',{fs:70,sub:'LORDI'}],['op','−','si pagano'],['num','230 €','duecentotrenta euro',{fs:70,fill:RF_,sub:'IRPEF'}],['op','=','Netti,'],['num','770 €','settecentosettanta',{fs:70,fill:GF_,sub:'NETTI'}]],70,300)]},
]);
// ---------- BLOCCO 20 ----------
SPECS[20]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CONFRONTO',cap:'RATA NORMALE DA 1.000 € ≈ 900 € NETTI, CON LE DETRAZIONI',items:[
  VN('≈ 900 €',560,400,'circa novecento euro netti',{fs:110,fill:GF_,sub:'RATA NORMALE · NETTI'}),
  VT('CON LE DETRAZIONI',1380,430,'le detrazioni',AMB,48)]},
 {at:'La tredicesima è più magra',top:'LA TREDICESIMA',cap:'770 € NETTI: CIRCA 140 € IN MENO DI UNA RATA',items:[
  VN('770 €',540,400,'La tredicesima è più magra',{fs:110,fill:AMB,sub:'TREDICESIMA · NETTI'}),
  VN('− 140 €',1380,400,'centoquaranta euro',{fs:110,fill:RF_,sub:'CIRCA, IN MENO'})]},
 {at:'E più sale la pensione',top:'PIÙ SALE LA PENSIONE',cap:'PIÙ SALE LA PENSIONE, PIÙ LA DIFFERENZA SI SENTE',items:[
  I('arR',[],960,400,'più sale',1.4,-90),
  VT('PIÙ LA DIFFERENZA SI SENTE',960,680,'più la differenza si sente',AMB,48)]},
]);
// ---------- BLOCCO 21 ----------
SPECS[21]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 3',cap:'1.500 € AL MESE',items:[
  I('circ',['3',GF_],440,420,'Terzo caso'),
  VN('1.500 €',1150,400,'Millecinquecento euro al mese',{fs:130,sub:'AL MESE'})]},
 {at:'Reddito annuo',top:'IL CALCOLO',cap:'1.500 € × 13 = 19.500 € ALL’ANNO · ALIQUOTA 23 %',items:[
  ...EQ(380,[['num','1.500 €','Reddito annuo',{fs:80,sub:'× 13 MESI'}],['op','=',['Reddito annuo',0.7]],['num','19.500 €','diciannovemilacinquecento',{fs:80,fill:GF_,sub:'REDDITO ANNUO'}]],80,300),
  VN('23 %',960,720,'sempre aliquota ventitré per cento',{fs:90,fill:AMB,sub:'ALIQUOTA'})]},
 {at:'Tredicesima lorda',top:'LA TREDICESIMA',cap:'1.500 € − 345 € DI IRPEF = 1.155 € NETTI',items:[
  ...EQ(420,[['num','1.500 €','Tredicesima lorda',{fs:70,sub:'LORDI'}],['op','−','Irpef trecentoquarantacinque'],['num','345 €','trecentoquarantacinque',{fs:70,fill:RF_,sub:'IRPEF'}],['op','=','netti millecentocinquantacinque'],['num','1.155 €','millecentocinquantacinque',{fs:70,fill:GF_,sub:'NETTI'}]],70,300)]},
]);
// ---------- BLOCCO 22 ----------
SPECS[22]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 4',cap:'2.000 € AL MESE',items:[
  I('circ',['4','url(#g_head)'],440,420,'Quarto caso'),
  VN('2.000 €',1150,400,'Duemila euro al mese',{fs:130,sub:'AL MESE'})]},
 {at:'Reddito ventiseimila',top:'IL CALCOLO',cap:'2.000 € × 13 = 26.000 € · SOTTO I 28.000 € = 23 %',items:[
  VN('26.000 €',540,420,'Reddito ventiseimila euro',{fs:100,sub:'REDDITO ANNUO'}),
  VT('SOTTO I 28.000 €',1380,330,'sotto i ventottomila',AMB,44),
  VN('23 %',1380,560,'ancora ventitré per cento',{fs:100,fill:GF_,sub:'ALIQUOTA'})]},
 {at:'Irpef quattrocentosessanta',top:'LA TREDICESIMA',cap:'2.000 € − 460 € DI IRPEF = 1.540 € NETTI',items:[
  ...EQ(420,[['num','2.000 €','Irpef quattrocentosessanta',{fs:70,sub:'LORDI'}],['op','−',['quattrocentosessanta euro',-0.3]],['num','460 €','quattrocentosessanta euro',{fs:70,fill:RF_,sub:'IRPEF'}],['op','=','netti millecinquecentoquaranta'],['num','1.540 €','millecinquecentoquaranta euro',{fs:70,fill:GF_,sub:'NETTI'}]],70,300)]},
]);
// ---------- BLOCCO 23 ----------
SPECS[23]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CASO 5 · LA SORPRESA',cap:'3.000 € AL MESE',items:[
  I('circ',['5',RF_],440,420,'quinto caso'),
  VN('3.000 €',1150,400,'Tremila euro al mese',{fs:130,sub:'AL MESE'})]},
 {at:'Il reddito dell’anno',top:'IL REDDITO DELL’ANNO',cap:'3.000 € × 13 = 39.000 €',items:[
  ...EQ(400,[['num','3.000 €','Il reddito',{fs:100,sub:'× 13 MESI'}],['op','=',['Il reddito',0.8]],['num','39.000 €','trentanovemila euro',{fs:100,fill:GF_,sub:'REDDITO ANNUO'}]],100,300)]},
 {at:'e l’ultima parte',top:'SCAGLIONI IRPEF',cap:'OLTRE I 28.000 € ENTRA LO SCAGLIONE DEL 33 %',items:[
  I('step',[260,140,'#2B6F77','23 %'],640,720,'l’ultima parte'),
  I('step',[260,230,AMB,'33 %'],960,720,'trentatré per cento'),
  I('step',[260,320,RF_,'43 %'],1280,720,['trentatré per cento',0.8])]},
]);
// ---------- BLOCCO 24 ----------
SPECS[24]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA TREDICESIMA DA 3.000 €',cap:'3.000 € − 990 € DI IRPEF = 2.010 € NETTI',items:[
  ...EQ(420,[['num','3.000 €','Sulla tredicesima',{fs:70,sub:'LORDI'}],['op','−','l’Irpef è'],['num','990 €','novecentonovanta euro',{fs:70,fill:RF_,sub:'IRPEF 33 %'}],['op','=','Restano'],['num','2.010 €','duemiladieci euro netti',{fs:70,fill:GF_,sub:'NETTI'}]],70,300)]},
 {at:'Quasi mille euro',top:'LA DIFFERENZA',cap:'QUASI MILLE EURO IN MENO DEL LORDO',items:[
  VN('− 990 €',480,400,'Quasi mille euro in meno',{fs:120,fill:RF_,sub:'DAL LORDO'}),
  VT('LA RATA PIÙ RICCA DELL’ANNO?',1360,430,'la rata più ricca dell’anno',AMB,34)]},
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
 {at:0,top:'ATTENZIONE',cap:'SONO ESEMPI',items:[
  I('warn',[],480,430,'Attenzione'),
  VT('SONO SOLO ESEMPI',1250,430,'sono esempi',AMB,60)]},
 {at:'Ho preso un pensionato',top:'LE IPOTESI',cap:'SENZA ALTRI REDDITI · SENZA ADDIZIONALI',items:[
  I('doc',['SENZA ALTRI REDDITI',620,280,GRN,36],520,430,'senza altri redditi'),
  I('doc',['SENZA ADDIZIONALI',620,280,AMB,36],1400,430,'le addizionali')]},
 {at:'Se hai altri redditi',top:'SE HAI ALTRI REDDITI',cap:'IL TUO NETTO CAMBIA · IL NUMERO ESATTO LO DICE L’INPS',items:[
  VN('NETTO',540,400,'il tuo netto cambia',{fs:110,fill:AMB,sub:'CAMBIA'}),
  I('br',['inps.it',620,300],1380,430,'te lo dice l’Inps')]},
]);
// ---------- BLOCCO 27 ----------
SPECS[27]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO NON È FINITO',cap:'MANCANO DUE VOCI',items:[
  I('calc',[],480,420,'Ma il conto di dicembre'),
  VN('2 VOCI',1330,400,'Mancano due voci',{fs:150,sub:'ANCORA DA VEDERE',minw:700})]},
 {at:'Una è un extra',top:'VOCE 1',cap:'UN EXTRA PER LE PENSIONI BASSE',items:[
  I('circ',['1',GF_],440,420,'Una è un extra'),
  VN('EXTRA',1150,400,'per le pensioni basse',{fs:130,fill:GF_,sub:'PENSIONI BASSE'})]},
 {at:'L’altra riguarda',top:'VOCE 2',cap:'RIGUARDA QUASI TUTTI: PIÙ SOLDI IN BANCA',items:[
  I('circ',['2','url(#g_head)'],440,420,'L’altra riguarda'),
  VN('PIÙ SOLDI',1150,400,'più soldi di quanto pensi',{fs:120,fill:GF_,sub:'IN BANCA'})]},
 {at:'Parto dall’extra',top:'PARTO DALL’EXTRA',cap:'PRIMA L’EXTRA PER LE PENSIONI BASSE',items:[
  I('circ',['1',GF_],600,430,'Parto dall’extra'),
  I('arR',[],1000,430,['Parto dall’extra',0.4]),
  VT('EXTRA',1420,430,['Parto dall’extra',0.7],AMB,56)]},
]);
// ---------- BLOCCO 28 ----------
SPECS[28]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE PENSIONI BASSE',cap:'A DICEMBRE C’È ANCHE UN EXTRA',items:[
  VT('PENSIONI BASSE',520,430,'pensioni basse',AMB,48),
  VN('EXTRA',1380,400,'un extra',{fs:130,fill:GF_,sub:'A DICEMBRE'})]},
 {at:'Si chiama importo aggiuntivo',top:'IMPORTO AGGIUNTIVO',cap:'154,94 € · ESENTASSE',items:[
  I('doc',['IMPORTO AGGIUNTIVO',700,300,GRN,38],540,420,'importo aggiuntivo'),
  VN('154,94 €',1400,380,'centocinquantaquattro euro',{fs:96,fill:GF_,sub:'ESENTASSE'}),
  I('stamp',['ESENTASSE',GRN,52],1400,650,'esentasse')]},
]);
// ---------- BLOCCO 29 ----------
SPECS[29]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CHI LO RICEVE',cap:'PENSIONE TOTALE FINO A CIRCA 7.954 € ALL’ANNO',items:[
  I('doc',['PENSIONE TOTALE',560,300,undefined,38],520,430,'la pensione totale'),
  VN('≈ 7.954 €',1380,400,'settemilanovecentocinquantaquattro euro',{fs:100,sub:'ALL’ANNO · LIMITE'})]},
 {at:'e il reddito personale',top:'REDDITO PERSONALE',cap:'REDDITO PERSONALE SOTTO 11.931 €',items:[
  VN('< 11.931 €',960,380,'undicimilanovecentotrentuno euro',{fs:130,sub:'REDDITO PERSONALE'})]},
 {at:'Per chi è sposato',top:'PER CHI È SPOSATO',cap:'LIMITE DI COPPIA: 23.862 €',items:[
  VN('< 23.862 €',960,380,'ventitremilaottocentosessantadue euro',{fs:130,fill:GF_,sub:'LIMITE DI COPPIA'})]},
]);
// ---------- BLOCCO 30 ----------
SPECS[30]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'A CHI NON SPETTA',cap:'SOLO ASSEGNO SOCIALE, PENSIONE SOCIALE O INVALIDITÀ CIVILE',items:[
  I('doc',['ASSEGNO SOCIALE',440,260,undefined,34],440,430,'assegno sociale'),
  I('doc',['PENSIONE SOCIALE',440,260,undefined,34],960,430,'pensione sociale'),
  I('doc',['INVALIDITÀ CIVILE',440,260,undefined,34],1480,430,'invalidità civile'),
  I('cross',[100,55],440,430,['assegno sociale',0.5]),
  I('cross',[100,55],960,430,['pensione sociale',0.5]),
  I('cross',[100,55],1480,430,['invalidità civile',0.5])]},
 {at:'Non serve domanda',top:'NESSUNA DOMANDA',cap:'LO PAGA L’INPS DA SOLO',items:[
  I('stamp',['NESSUNA DOMANDA',GRN,60],960,400,'Non serve domanda'),
  VT('LO PAGA L’INPS',960,640,'lo paga l’Inps',GF_,52)]},
 {at:'Non ci rientri?',top:'NON CI RIENTRI?',cap:'RESTA: SUBITO DOPO C’È LA VOCE CHE RIGUARDA TUTTI',items:[
  I('q',[110],480,430,'Non ci rientri'),
  VT('RESTA',1250,430,'Resta',AMB,72)]},
]);
// ---------- BLOCCO 31 ----------
SPECS[31]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA VOCE PER TUTTI',cap:'L’ADDIZIONALE REGIONALE DELL’ANNO PRIMA, A RATE',items:[
  I('doc',['ADDIZIONALE REGIONALE',760,300,GRN,36],560,430,'l’addizionale regionale'),
  VT('TRATTENUTA A RATE',1480,430,'ti trattiene a rate',AMB,44)]},
 {at:'undici rate',top:'UNDICI RATE',cap:'DA GENNAIO A NOVEMBRE',items:[
  ...MESI(380,'undici rate',i=>i==10?AMB:GF_,11),
  VT('DA GENNAIO A NOVEMBRE',960,640,'da gennaio a novembre',GF_,48)]},
 {at:'Novembre è l’ultima rata',top:'NOVEMBRE: L’ULTIMA',cap:'POI LA TRATTENUTA FINISCE',items:[
  VN('NOVEMBRE',500,400,'Novembre è l’ultima rata',{fs:100,fill:AMB,sub:'ULTIMA RATA'}),
  I('arR',[],960,420,['la trattenuta finisce',-0.5]),
  I('stamp',['FINE TRATTENUTA',GRN,52],1420,400,'la trattenuta finisce')]},
]);
// ---------- BLOCCO 32 ----------
SPECS[32]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CONGUAGLIO DEL 730',cap:'SE AVEVI ANCHE LE RATE DEL CONGUAGLIO DEL 730',items:[
  I('doc',['MODELLO 730',520,300,GRN,42],520,430,'del settecentotrenta'),
  VT('RATE DI CONGUAGLIO',1350,430,'rate del conguaglio',AMB,44)]},
 {at:'devono chiudersi entro novembre',top:'ENTRO NOVEMBRE',cap:'DEVONO CHIUDERSI ENTRO NOVEMBRE',items:[
  VN('NOVEMBRE',960,380,'entro novembre',{fs:130,fill:AMB,sub:'ULTIMA RATA',minw:800})]},
 {at:'Risultato:',top:'RISULTATO',cap:'A DICEMBRE LE TRATTENUTE NON CI SONO PIÙ: LA RATA SALE',items:[
  VN('TRATTENUTE',520,400,'quelle trattenute non ci sono più',{fs:84,fill:RF_,sub:'NON CI SONO PIÙ'}),
  I('arR',[],1060,420,'nella rata di dicembre',1,-90),
  VN('RATA',1440,400,'la rata, di solito, sale',{fs:110,fill:GF_,sub:'SALE'})]},
]);
// ---------- BLOCCO 33 ----------
SPECS[33]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO?',cap:'GUARDA IL CEDOLINO DI NOVEMBRE',items:[
  I('q',[100],400,430,'Quanto?'),
  I('pay',['CEDOLINO'],840,500,'Guarda il cedolino'),
  VT('ADDIZIONALE REGIONALE',1480,430,'addizionale regionale',AMB,40)]},
 {at:'Quella cifra',top:'QUELLA CIFRA',cap:'A DICEMBRE RESTA A TE',items:[
  VN('QUELLA CIFRA',960,380,'Quella cifra',{fs:100,fill:GF_,sub:'A DICEMBRE RESTA A TE'}),
  I('chk',[80],1640,380,'resta a te')]},
 {at:'Non è un aumento',top:'NON È UN AUMENTO',cap:'SONO SOLDI TUOI CHE PRIMA TI VENIVANO TOLTI',items:[
  I('stamp',['NON È UN AUMENTO',RED_,52],960,380,'Non è un aumento'),
  VT('SONO SOLDI TUOI',960,620,'sono soldi tuoi',GF_,48)]},
 {at:'Ma da gennaio',top:'DA GENNAIO',cap:'DA GENNAIO LE TRATTENUTE RIPARTONO',items:[
  I('cal',['GENNAIO','1',230,'2027'],520,540,'Ma da gennaio'),
  VT('RIPARTONO',1350,430,'ripartono',AMB,56)]},
]);
// ---------- BLOCCO 34 ----------
SPECS[34]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TRUCCO PRATICO',cap:'PER NON FARE CALCOLI A MANO',items:[
  I('calc',[],480,420,'Ora il trucco pratico'),
  VT('NIENTE CALCOLI A MANO',1350,430,'calcoli a mano',GF_,44)]},
 {at:'Entra in Mai Inps',top:'ENTRA IN MYINPS',cap:'ENTRA IN MYINPS CON LO SPID',items:[
  I('br',['inps.it',760,300],560,430,'Entra in Mai Inps'),
  VT('CON LO SPID',1400,430,'con lo Spid',AMB,52)]},
 {at:'Vai su Pensione e previdenza',top:'IL PERCORSO',cap:'PENSIONE E PREVIDENZA → CEDOLINO → CERTIFICATO DI PENSIONE',items:[
  I('row',['PENSIONE E PREVIDENZA',900,true],960,330,'Pensione e previdenza'),
  I('row',['CEDOLINO DELLA PENSIONE',900,true],960,470,'Cedolino della pensione'),
  I('row',['CERTIFICATO DI PENSIONE',900,true],960,610,'Certificato di pensione')]},
 {at:'il modello Obis emme',top:'IL MODELLO',cap:'CERTIFICATO DI PENSIONE · MODELLO OBISM',items:[
  I('doc',['OBISM',700,320,GRN,52],960,430,'Obis emme'),
  VT('CERTIFICATO DI PENSIONE',960,700,['Obis emme',0.5],AMB,44)]},
]);
// ---------- BLOCCO 35 ----------
SPECS[35]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DENTRO IL CERTIFICATO',cap:'LA TUA PENSIONE, RATA PER RATA',items:[
  I('row',['PENSIONE, RATA PER RATA',900,true],960,300,'rata per rata'),
  I('row',['LA TREDICESIMA',900,true],960,430,'la tredicesima'),
  I('row',['LE TRATTENUTE FISCALI',900,true],960,560,'le trattenute fiscali'),
  I('row',['IL LORDO E IL NETTO',900,true],960,690,'il lordo e il netto')]},
 {at:'Quando l’Inps pubblica',top:'A DICEMBRE',cap:'QUANDO L’INPS PUBBLICA IL CEDOLINO DI DICEMBRE, CONTROLLA LÌ',items:[
  I('pay',['CEDOLINO'],560,500,'il cedolino di dicembre'),
  I('arR',[],1000,500,'controlla lì'),
  I('chk',[100],1400,500,['controlla lì',0.4])]},
 {at:'È il numero vero',top:'IL NUMERO VERO',cap:'È IL NUMERO VERO, NON UNA STIMA',items:[
  I('chk',[100],480,430,'numero vero'),
  VT('NON UNA STIMA',1250,430,'non una stima',AMB,60)]},
]);
// ---------- BLOCCO 36 ----------
SPECS[36]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RICAPITOLO',cap:'LA TREDICESIMA È UNA RATA LORDA IN PIÙ',items:[
  I('circ',['1',GF_],440,420,'Ricapitolo'),
  VN('RATA IN PIÙ',1150,400,'una rata lorda in più',{fs:110,sub:'LA TREDICESIMA'})]},
 {at:'La detassazione',top:'RICAPITOLO',cap:'LA DETASSAZIONE È SOLO UNA PROPOSTA',items:[
  I('circ',['2','url(#g_head)'],440,420,'La detassazione'),
  VN('PROPOSTA',1150,400,'solo una proposta',{fs:110,fill:AMB,sub:'LA DETASSAZIONE'})]},
 {at:'E il tuo netto',top:'RICAPITOLO',cap:'IL TUO NETTO DI DICEMBRE SALE: LE TRATTENUTE FINISCONO',items:[
  I('circ',['3',RF_],440,420,'E il tuo netto'),
  VN('NETTO',1050,400,'il tuo netto di dicembre',{fs:100,fill:GF_,sub:'DI DICEMBRE'}),
  I('arR',[],1560,420,'sale anche',1,-90)]},
 {at:'Scrivimi quanto prendi',top:'SCRIVIMI NEI COMMENTI',cap:'SCRIVIMI QUANTO PRENDI, TI RISPONDO CON IL TUO NETTO',items:[
  I('bubble',[560,300],540,430,'Scrivimi quanto prendi'),
  VN('IL TUO NETTO',1400,400,'con il tuo netto',{fs:90,fill:GF_,sub:'TI RISPONDO'})]},
]);
// ---------- BLOCCO 37 (slide finale con il disclaimer; destra-basso libero per la schermata finale) ----------
SPECS[37]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'A NOVEMBRE',cap:'ESCE IL DECRETO SULLA RIVALUTAZIONE DELL’ANNO PROSSIMO',items:[
  I('cal',['NOVEMBRE','2026',130,'DECRETO'],520,540,'A novembre'),
  I('doc',['DECRETO',560,300,undefined,40],1380,430,'il decreto')]},
 {at:'iscriviti e attiva',top:'ISCRIVITI',cap:'ISCRIVITI E ATTIVA LA CAMPANELLA',items:[
  I('btn',['ISCRIVITI'],700,430,'iscriviti'),
  I('bell',[],1300,430,'la campanella')]},
 {at:'Regole e importi cambiano',top:'VERIFICA SEMPRE',cap:'VERIFICA SEMPRE SUL SITO DELL’INPS · GRAZIE PER AVER GUARDATO!',capSize:42,items:[
  I('dbg',[1120,500],700,450,['Regole e importi cambiano',-0.5]),
  I('dline',['REGOLE E IMPORTI CAMBIANO','#fff',44],700,380,['Regole e importi cambiano',0.9]),
  I('dline',['VERIFICA SUL SITO DELL’INPS','#7FF0D2',40],700,470,'verifica sul sito'),
  I('dline',['INFORMAZIONE GENERALE, NON CONSULENZA','#FFB838',40],700,560,'Informazione generale'),
  I('dline',['CANALE NON AFFILIATO ALL’INPS','#fff',40],700,650,'Canale non affiliato')]},
]);
