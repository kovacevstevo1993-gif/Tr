// ---------- BLOCCO 1 (619 f = 20,6 s) ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DICEMBRE: TRE VICINI DI CASA',cap:'QUASI LA STESSA PENSIONE, MA TRE DICEMBRI DIVERSI',items:[
  I('per',['F','FRANCO',null,105],460,330,'Franco'),
  I('per',['A','ANNA',null,105],960,330,'Anna'),
  I('per',['L','LUCIA',null,105],1460,330,'Lucia'),
  I('calS',['DICEMBRE','1',150,'MARTEDÌ',0.5],560,700,'Martedì primo dicembre'),
  VT('LA RATA ARRIVA A TUTTI E TRE',1260,690,'arriva a tutti e tre',GF_,38)]},
 {at:'Ma uno troverà',top:'COSA TROVERANNO NELLA RATA',cap:'ALLA FINE CAPISCI QUALE DEI TRE SEI TU',items:[
  I('q',[56],330,290,'Ma uno troverà'),I('coin',['13ª',70],520,290,['solo la tredicesima',-0.3]),
  VT('SOLO LA TREDICESIMA',1400,290,'solo la tredicesima',DF_,38),
  I('q',[56],330,490,'Una troverà anche'),I('coin',['13ª',70],520,490,['Una troverà anche',0.1]),I('coin',['BONUS',70,GRN,28],700,490,'un bonus'),
  VT('+ BONUS DI 154,94 €',1400,490,'centocinquantaquattro euro',GF_,38),
  I('q',[56],330,690,'E una troverà'),I('coin',['13ª',70],520,690,['E una troverà',0.1]),I('coin',['BONUS',70,GRN,28],700,690,['tre soldi',-0.2]),I('coin',['14ª',70,RED_],880,690,'tre soldi'),
  VT('TRE PAGAMENTI INSIEME',1400,690,'nella stessa rata',AMB,34)]},
]);
// ---------- BLOCCO 2 (618 f = 20,6 s) ----------
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUELLO CHE HANNO IN COMUNE',cap:'LA PENSIONE SI PAGA IL PRIMO GIORNO BANCABILE DEL MESE',items:[
  I('per',['F',null,null,62],760,250,'Partiamo da quello'),I('per',['A',null,null,62],960,250,['Partiamo da quello',0.15]),I('per',['L',null,null,62],1160,250,['Partiamo da quello',0.3]),
  I('calS',['DICEMBRE 2026','1',170,'MARTEDÌ',0.5],460,690,'martedì primo dicembre'),
  I('ico',['banca','IN BANCA',280,280],1060,600,'in banca'),
  I('posta',['ALLE POSTE'],1440,600,'alle Poste')]},
 {at:'In quella rata',top:'NELLA RATA DI DICEMBRE',cap:'NIENTE ADDIZIONALI E IN PIÙ LA TREDICESIMA, SENZA DOMANDA',items:[
  I('mon',[[[0,10,RED_,'ADDIZIONALI: 11 RATE, GENNAIO-NOVEMBRE'],[11,11,GRN]],900,28],600,330,'trattenute delle addizionali'),
  VT('DICEMBRE: NESSUNA TRATTENUTA',600,500,'non ci sono più',GF_,36),
  I('ced',['CEDOLINO DI DICEMBRE',[['Addizionali','0 €',GRN],['Tredicesima','+1 RATA',GRN]],560],1400,400,'E c\'è la tredicesima'),
  VT('13ª: UNA RATA IN PIÙ, LORDA',600,660,'una rata in più',AMB,38),
  I('chk',[60],1120,700,'senza fare domanda'),VT('SENZA DOMANDA',1470,700,['senza fare domanda',0.15],GF_,38)]},
]);
// ---------- BLOCCO 3 (709 f = 23,6 s) ----------
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA TREDICESIMA E LE TASSE',cap:'IL NETTO PENSIONE PER PENSIONE: C\'È UN VIDEO INTERO SUL CANALE',items:[
  I('tax2',[],560,620,'le tasse pesano più'),
  VT('PIÙ TASSE CHE SU UNA RATA NORMALE',560,220,'che su una rata normale',RF_,34),
  I('vid',['TREDICESIMA: IL NETTO','PENSIONE PER PENSIONE'],1360,430,'in un video intero'),
  VT('LO TROVI SUL CANALE',1360,700,'che trovi sul canale',GF_,38)]},
 {at:'Oggi guardiamo',top:'IL SECONDO PAGAMENTO: IL BONUS',cap:'L\'ANNO SCORSO L\'IMPORTO AGGIUNTIVO È ANDATO A OLTRE 400.000 PENSIONATI',items:[
  VT('OGGI: GLI ALTRI DUE PAGAMENTI',560,220,'Oggi guardiamo',DF_,34),
  VN('154,94 €',560,400,'centocinquantaquattro euro',{fs:92,sub:'IMPORTO AGGIUNTIVO',minw:560}),
  I('doc',['PREVISTO PER LEGGE',440,230,GRN,30],560,700,'previsto per legge'),
  VT('L\'ANNO SCORSO',1380,230,'L\'anno scorso',AMB,36),
  I('crowd',[9,4,LT],1380,450,'l\'hanno ricevuto'),
  VN('OLTRE 400.000',1380,700,'più di quattrocentomila',{fs:62,sub:'PENSIONATI',fill:GF_,minw:520})]},
]);
// ---------- BLOCCO 4 (642 f = 21,4 s) ----------
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FRANCO',cap:'SEMBRA IL CANDIDATO PERFETTO PER IL BONUS. INVECE: ZERO',items:[
  I('per',['F','FRANCO','630 € AL MESE',130],430,370,'Franco prende'),
  VN('630 €',900,280,'seicentotrenta euro',{fs:84,sub:'PENSIONE AL MESE',minw:440}),
  I('rw',['È solo',true,38,true],680,480,'È solo'),
  I('rw',['Nessun altro reddito',true,38,true],680,600,'non ha altri redditi'),
  VT('CANDIDATO PERFETTO?',1500,280,'candidato perfetto',AMB,36),
  I('stamp',['BONUS: 0 €',RED_,50],1560,440,'prenderà zero')]},
 {at:'Il motivo',top:'CONDIZIONE 1: LA PENSIONE',cap:'TRATTAMENTO MINIMO 2026: 611,85 € AL MESE, CIOÈ 7.954,05 € L\'ANNO',items:[
  I('circ',['1'],300,250,'Il motivo'),VT('PRIMA CONDIZIONE: LA PENSIONE',900,250,'la prima condizione',AMB,38),
  VN('611,85 €',560,520,'seicentoundici euro',{fs:84,sub:'MINIMO AL MESE',minw:560}),
  I('arR',[],960,520,'cioè'),
  VN('7.954,05 €',1360,520,'settemilanovecentocinquantaquattro',{fs:84,sub:'ALL\'ANNO',fill:GF_,minw:560}),
  VT('ANNO 2026',960,740,'del duemilaventisei',DF_,34)]},
]);
// ---------- BLOCCO 5 (685 f = 22,8 s) ----------
const ZL=(s,v,at,fill)=>I('tag',[s,fill,fill===AMB?'#5A3300':'#fff',30],960+RX(v),620,at);
const BP=(s,v,at)=>I('tag',[s,DF_,'#fff',30],960+RX(v),710,at);
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA SOGLIA DELLA PENSIONE',cap:'FINO A 7.954,05 € INTERO, FINO A 8.108,99 € UNA PARTE, SOPRA NIENTE',items:[
  VT('PENSIONE DI UN ANNO',960,260,'in un anno',DF_,36),
  I('rul',[],960,540,'non supera questa cifra'),
  ZL('INTERO',7827,'può essere intero','url(#g_badge)'),BP('7.954,05 €',7954.05,['può essere intero',0.3]),
  ZL('UNA PARTE',8031.5,'se ne prende una parte',AMB),BP('8.108,99 €',8108.99,'fino a ottomilacentootto'),
  ZL('NIENTE',8204,['se ne prende una parte',0.5],RF_),
  VT('IL BONUS SCENDE PIANO PIANO FINO A ZERO',960,380,['se ne prende una parte',0.9],AMB,32)]},
 {at:'Franco, in un anno',top:'FRANCO E LA SOGLIA',cap:'PER DIECI EURO AL MESE IN PIÙ, IL BONUS SPARISCE',items:[
  I('rul',[],960,540,'Franco, in un anno'),
  ZL('INTERO',7827,['Franco, in un anno',0.1],'url(#g_badge)'),ZL('UNA PARTE',8031.5,['Franco, in un anno',0.2],AMB),ZL('NIENTE',8204,['Franco, in un anno',0.3],RF_),
  I('mk',['FRANCO: 8.190 €',RED_,270],960+RX(8190),540,'ottomilacentonovanta'),
  I('mk',['620 € AL MESE = 8.060 €',AMB,130],960+RX(8060),540,'Con seicentoventi'),
  VN('48,99 €',470,300,'quarantotto euro',{fs:72,sub:'AVREBBE PRESO',fill:GF_,minw:420}),
  BP('7.954,05 €',7954.05,['Per dieci euro',-0.2]),BP('8.108,99 €',8108.99,['Per dieci euro',0])]},
]);
// ---------- BLOCCO 6 (613 f = 20,4 s) - richiesta di iscrizione dopo il primo conto ----------
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PRIMA DI ANDARE AVANTI',cap:'CONTI FATTI CON I LIMITI VERI DELL\'INPS: ORE DI LAVORO PER OGNI VIDEO',items:[
  I('per',['F','FRANCO',null,110],380,350,'Franco resta senza bonus'),
  VT('SENZA BONUS PER 10 €',380,640,'per dieci euro al mese',RF_,32),
  I('clock',[115],1060,400,'ci prendono ore'),VT('ORE PER OGNI VIDEO',1060,640,['ci prendono ore',0.2],AMB,36),
  I('doc',['LIMITI UFFICIALI INPS',420,300,GRN,30],1560,450,'i limiti veri')]},
 {at:'Se ti sono serviti',top:'ISCRIVITI: È GRATIS',cap:'VOGLIAMO ARRIVARE A 1.000 ISCRITTI: CI SERVE IL TUO AIUTO',items:[
  I('btn',['ISCRIVITI'],560,270,'iscriviti adesso'),
  VT('GRATIS, BASTA UN TOCCO',560,420,'è gratis',GF_,36),
  I('per',['A','ANNA',null,72],1260,270,'prima di vedere Anna'),I('per',['L','LUCIA',null,72],1560,270,['prima di vedere Anna',0.2]),
  VT('I PROSSIMI CONTI NELLA PAGINA INIZIALE',960,530,'pagina iniziale',AMB,30),
  I('goal',[1300,0.25],960,730,'Vogliamo arrivare a mille')]},
]);
// ---------- BLOCCO 7 (732 f = 24,4 s) ----------
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ANNA',cap:'ANNA PRENDE IL MINIMO: LA SUA PENSIONE VA BENE',items:[
  I('per',['A','ANNA','611,85 € AL MESE',130],430,370,'Anna prende il minimo'),
  VN('611,85 €',1050,290,'seicentoundici euro',{fs:84,sub:'IL MINIMO',minw:440}),
  I('rw',['Condizione 1: la pensione',true,36,true],790,520,'la sua pensione va bene'),
  I('circ',['2'],830,690,'la seconda condizione'),VT('CONDIZIONE 2: IL REDDITO',1340,690,'il reddito',AMB,38)]},
 {at:'Se sei solo',top:'CONDIZIONE 2: IL REDDITO',cap:'SE SEI SPOSATO, OLTRE AL LIMITE DI COPPIA RESTA ANCHE QUELLO PERSONALE',items:[
  I('lim',['SE SEI SOLO',false,'11.931,08 €','REDDITO IRPEF, PENSIONE COMPRESA'],560,450,'Se sei solo'),
  I('lim',['SE SEI SPOSATO',true,'23.862,15 €','LIMITE DI COPPIA'],1360,450,'Se sei sposato'),
  VT('+ RESTA IL LIMITE PERSONALE',1360,770,'resta anche il limite personale',AMB,34)]},
]);
// ---------- BLOCCO 8 (721 f = 24,0 s) ----------
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ANNA E IL MARITO',cap:'INSIEME SONO SOTTO IL LIMITE: ANNA PRENDE IL BONUS INTERO',items:[
  I('per',['A','ANNA',null,85],250,290,'Il marito di Anna'),I('per',['M','MARITO',null,85],470,290,['Il marito di Anna',0.2]),
  VN('1.200 €',1060,280,'milleduecento euro',{fs:76,sub:'AL MESE = 15.600 € L\'ANNO',minw:520}),
  I('sbar',[7954.05,15600,true,'ANNA 7.954 €','MARITO 15.600 €'],960,620,'Insieme fanno'),
  I('stamp',['BONUS INTERO',GRN,36],1680,280,'prende il bonus intero')]},
 {at:'Se il marito prendesse',top:'E SE IL MARITO PRENDESSE 50 € IN PIÙ?',cap:'CINQUANTA EURO DEL MARITO, E IL BONUS SPARIREBBE',items:[
  VT('+ 50 € AL MESE',320,280,'Se il marito prendesse',AMB,38),
  VN('1.250 €',1000,280,'milleduecentocinquanta',{fs:76,sub:'AL MESE = 16.250 € L\'ANNO',minw:520}),
  I('sbar',[7954.05,16250,false,'ANNA 7.954 €','MARITO 16.250 €'],960,620,'la coppia arriverebbe'),
  I('stamp',['BONUS: 0 €',RED_,40],1660,280,'bonus zero')]},
]);
// ---------- BLOCCO 9 (631 f = 21,0 s) ----------
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ANNA NON DEVE FARE NIENTE',cap:'L\'INPS LO PAGA DA SOLO, IN VIA PROVVISORIA, E POI VERIFICA I REDDITI',items:[
  I('per',['A','ANNA','NESSUNA DOMANDA',110],300,380,'Anna non deve fare niente'),
  I('stp',['1','PAGATO DA SOLO','RATA DI DICEMBRE',360],700,460,'lo paga da solo'),
  I('arR',[],935,460,['in via provvisoria',-0.4],0.6),
  I('stp',['2','PROVVISORIO','PAGATO D\'UFFICIO',360],1170,460,'in via provvisoria'),
  I('arR',[],1405,460,['lo verifica',-0.4],0.6),
  I('stp',['3','VERIFICA','SUI REDDITI',360],1640,460,'redditi dichiarati')]},
 {at:'Non lo prende mai',top:'CHI NON LO PRENDE MAI',cap:'CHI HA SOLO TRATTAMENTI ASSISTENZIALI. E ORA, LUCIA',items:[
  VT('SOLO TRATTAMENTI ASSISTENZIALI',620,230,'trattamenti assistenziali',RF_,36),
  I('rw',['Assegno sociale',false,38,true],300,360,'assegno sociale'),
  I('rw',['Pensione sociale',false,38,true],300,480,'pensione sociale'),
  I('rw',['Prestazioni di invalidità civile',false,38,true],300,600,'invalidità civile'),
  I('per',['L','LUCIA',null,120],1480,380,'E ora Lucia'),
  VT('LEI TROVA TRE PAGAMENTI',1480,730,'trova tre soldi',AMB,36)]},
]);
// ---------- BLOCCO 10 (733 f = 24,4 s) ----------
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LUCIA',cap:'COME ANNA PRENDE IL BONUS. E PER LEI ARRIVA ANCHE LA QUATTORDICESIMA',items:[
  I('per',['L','LUCIA',null,130],380,420,'Lucia prende'),
  I('rw',['Prende il minimo',true,38,true],680,300,'anche lei il minimo'),
  I('rw',['È sola',true,38,true],680,420,'è sola'),
  I('rw',['64 anni a settembre',true,38,true],680,540,'sessantaquattro anni a settembre'),
  I('coin',['BONUS',95,GRN,34],1420,360,'Quindi il bonus'),
  I('coin',['14ª',95,RED_,56],1680,360,'la quattordicesima'),
  VT('TERZO PAGAMENTO: LA 14ª',1540,620,['la quattordicesima',0.2],AMB,32)]},
 {at:'Di solito si paga',top:'LA QUATTORDICESIMA DI DICEMBRE',cap:'L\'ANNO SCORSO, A DICEMBRE, L\'HANNO PRESA QUASI 150.000 PENSIONATI',items:[
  I('mon',[[[6,6,GRN,'DI SOLITO: LUGLIO']]],960,330,'Di solito si paga a luglio'),
  I('mon',[[[7,11,AMB,'64 ANNI DOPO LUGLIO: PAGATA A DICEMBRE']]],960,560,'dopo luglio'),
  VT('O PENSIONE INIZIATA NEL 2026',520,720,'va in pensione durante l\'anno',GF_,34),
  VN('QUASI 150.000',1380,730,'quasi centocinquantamila',{fs:56,sub:'DICEMBRE SCORSO',fill:GF_,minw:500})]},
]);
// ---------- BLOCCO 11 (780 f = 26,0 s) ----------
const QX=[960-750+440+(1500-440)/4,960-750+440+(1500-440)*3/4];const QY=r=>440-184+92*(r+1)+46;
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO VALE LA QUATTORDICESIMA',cap:'IMPORTI ANNUI, LAVORATORI DIPENDENTI (AUTONOMI: FINO A 18, 18-28, OLTRE 28 ANNI)',items:[
  I('qtab',[],960,440,'Dipende dagli anni'),
  GN('437 €',QX[0],QY(0),'quattrocentotrentasette'),GN('546 €',QX[0],QY(1),'cinquecentoquarantasei'),GN('655 €',QX[0],QY(2),'seicentocinquantacinque'),
  GN('336 €',QX[1],QY(0),'trecentotrentasei','#2B6F77'),GN('420 €',QX[1],QY(1),'quattrocentoventi','#2B6F77'),GN('504 €',QX[1],QY(2),'cinquecentoquattro','#2B6F77'),
  I('mon',[[[8,11,AMB,'LUCIA: SOLO DA SETTEMBRE = UNA PARTE']],900,28],960,780,'Ma Lucia')]},
]);
// ---------- BLOCCO 12 (701 f = 23,4 s) ----------
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUATTORDICESIMA: COSA CAMBIA',cap:'LA 14ª NON È TASSATA E ARRIVA IN AUTOMATICO',items:[
  I('per',['L',null,null,85],330,320,'conta solo il tuo'),I('per',['M',null,null,85],600,320,'il reddito del coniuge'),
  I('cross',[70,70],600,320,'non conta'),
  VT('REDDITO DEL CONIUGE: NON CONTA',465,520,['non conta',0.2],GF_,32),
  VT('NON È TASSATA',1360,250,'non è tassata',GF_,42),
  I('rw',['Assegno sociale o invalidità civile: no',false,30,true],900,400,'non spetta'),
  I('rw',['Arriva in automatico',true,36,true],930,520,'arriva in automatico')]},
 {at:'Ecco il dicembre',top:'IL DICEMBRE DEI TRE VICINI',cap:'FRANCO: 13ª · ANNA: 13ª E BONUS · LUCIA: 13ª, BONUS E PARTE DI 14ª',items:[
  I('ghead',[],960,240,'Ecco il dicembre'),
  I('grow',['F','FRANCO',['si','no','no']],960,370,'Franco:'),
  I('grow',['A','ANNA',['si','si','no']],960,510,'Anna:'),
  I('grow',['L','LUCIA',['si','si','UNA PARTE']],960,650,'Lucia:')]},
]);
// ---------- BLOCCO 13 (531 f = 17,7 s) ----------
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SE NON VEDI NIENTE',cap:'CONTROLLA IL CEDOLINO DI DICEMBRE SU MY INPS, APPENA È ONLINE',items:[
  I('per',['A','ANNA',null,80],330,300,'come Anna'),I('per',['L','LUCIA',null,80],330,620,'o Lucia'),
  I('phone',[['Tredicesima','Importo aggiuntivo','Quattordicesima']],960,480,'controlla il cedolino'),
  VT('OGNI VOCE HA LA SUA RIGA',1530,480,'ogni voce ha la sua riga',AMB,32)]},
 {at:'Se il bonus o',top:'SE MANCA QUALCOSA',cap:'DOMANDA DI RICOSTITUZIONE DELLA PENSIONE: ONLINE O CON UN PATRONATO',items:[
  VT('BONUS O 14ª MANCANO?',560,230,'Se il bonus o',RF_,40),
  I('doc',['RICOSTITUZIONE',460,330,GRN,34],560,540,'ricostituzione della pensione'),
  I('arR',[],1000,540,['online',-0.3]),
  I('br',['inps.it',520,200],1400,360,'online'),
  I('ico',['comune','PATRONATO',300,250],1400,660,'con un patronato')]},
]);
// ---------- BLOCCO 14 (780 f = 26,0 s) - ULTIMO: contenuti in alto, zona bassa libera per la schermata finale (N.22) ----------
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E TU CHI SEI?',cap:'',items:[
  I('per',['F','FRANCO',null,70],660,230,'Franco'),I('per',['A','ANNA',null,70],960,230,'Anna'),I('per',['L','LUCIA',null,70],1260,230,'Lucia'),
  VT('SCRIVI NEI COMMENTI: QUANTO PRENDI, SOLO O SPOSATO',960,440,'Scrivilo nei commenti',AMB,34),
  I('dbg',[1600,250],960,635,'I limiti del'),
  I('dline',['LIMITI 2026 SULL\'AUMENTO PROVVISORIO DELL\'1,4%: POSSONO CAMBIARE','#fff',32],960,632,'possono cambiare'),
  I('dline',['VERIFICA SEMPRE SU INPS.IT O CON UN PATRONATO','#fff',32],960,682,'Controlla sempre'),
  I('dline',['SOLO INFORMATIVO, NON AFFILIATO ALL\'INPS','#7FF0D2',32],960,730,'non è affiliato')]},
]);
