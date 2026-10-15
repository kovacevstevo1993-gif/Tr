// ===== VIDEO 7 (rivalutazione persa 2023-2026) - motore b-sync-80: tempi calcolati su testo + durata del blocco =====
// Regole: scene >= 5 s, comparsa 0,9 s, nessun elemento sparisce nella scena, tutto completo entro l'80 %, poi fermo.
// Novita' del video 7 (N.37, non in serie): SCONTRINO della pensione (carta con bordo a zig-zag) + sfondo in movimento.
const SPECS={};
const GF_='url(#g_badge)',RF_='url(#g_red)',PF_='url(#g_paper)',DF_='#0B4A50';
const VT=(s,x,y,at,fill,fs)=>I('tag',[s,fill||AMB,(fill&&fill!==AMB)?'#fff':'#5A3300',fs||44],x,y,at);
const VN=(s,x,y,at,o)=>{o=o||{};return I('num',[s,o.fs||76,o.fill||PF_,o.sub,o.subfill,o.minw],x,y,at);};
BUILD.calS=(g,h,b,bs,sub,sc)=>{const w=el('g',{transform:'translate(0 '+(-250*sc)+') scale('+sc+')'},g);calendarPage(w,h,b,bs,sub);};
// scontrino: centro in (0,0); w x h; testata, righe [etichetta, importo, colore], totale
BUILD.rcpt=(g,w,h,head,lines,total,tsub)=>{const zz=22;let d=`M${-w/2} ${-h/2+20} Q${-w/2} ${-h/2} ${-w/2+20} ${-h/2} H${w/2-20} Q${w/2} ${-h/2} ${w/2} ${-h/2+20} V${h/2}`;
 const n=Math.round(w/zz);for(let i=0;i<n;i++){const x1=w/2-(i+0.5)*w/n,x2=w/2-(i+1)*w/n;d+=` L${x1} ${h/2-14} L${x2} ${h/2}`;}d+=' Z';
 el('path',{d:d,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:84,rx:20,fill:GRN},g);el('rect',{x:-w/2,y:-h/2+50,width:w,height:34,fill:GRN},g);
 txt(g,head,0,-h/2+56,Math.min(38,(w-60)/(head.length*0.74)),'#fff','bold');
 let y=-h/2+140;(lines||[]).forEach(l=>{txt(g,l[0],-w/2+40,y,34,INK,'bold','start');txt(g,l[1],w/2-40,y,36,l[2]||INK,'900','end');
  el('line',{x1:-w/2+36,y1:y+22,x2:w/2-36,y2:y+22,stroke:'#B7C7CA','stroke-width':3,'stroke-dasharray':'10 8'},g);y+=72;});
 el('line',{x1:-w/2+30,y1:y-10,x2:w/2-30,y2:y-10,stroke:INK,'stroke-width':5},g);
 txt(g,total,0,y+88,Math.min(110,(w-60)/(total.length*0.62)),RED_,'900');
 if(tsub)txt(g,tsub,0,y+146,34,GRN,'bold');};
// ---------- BLOCCO 1 (841 fotogrammi = 28,0 s) ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONI: QUANTO HAI PERSO?',cap:'4 ANNI DI RIVALUTAZIONE TAGLIATA: È SCRITTO NELLE LEGGI',items:[
  I('rcpt',[560,600,'SCONTRINO DELLA PENSIONE',[['Pensione 2022','3.000 €'],['Periodo','2023-2026'],['Rivalutazione','TAGLIATA',RED_]],'-9.400 €','LORDI IN 4 ANNI'],520,530,'novemilaquattrocento'),
  VN('3.000 €',1350,330,'chi a fine duemilaventidue',{fs:90,sub:'PENSIONE LORDA FINE 2022',minw:640}),
  VT('NÉ MULTA, NÉ ERRORE',1350,560,'Non per una multa',RF_,40),
  I('stamp',['LEGGE DI BILANCIO',GRN,52],1350,690,'per una regola scritta'),
  VT('IL BUCO NON SI RICHIUDE',1350,815,'E quel buco',AMB,40)]},
 {at:'Oggi facciamo un test',top:'IL TEST',cap:'IN POCHI MINUTI CAPISCI IN QUALE GRUPPO SEI',items:[
  VT('TU QUANTO HAI PERSO?',960,250,'Oggi facciamo un test',GF_,46),
  VN('NIENTE',420,480,'perso niente',{fs:84,fill:GF_,sub:'GRUPPO 1',minw:470}),
  VN('POCO',960,480,'poco',{fs:84,fill:AMB,sub:'GRUPPO 2',minw:470}),
  VN('TANTO',1500,480,'o tanto',{fs:84,fill:RF_,sub:'GRUPPO 3',minw:470}),
  VT('E POI: COSA SI DECIDE PER IL 2027?',960,760,'cosa si sta decidendo adesso',DF_,42)]},
]);
// ---------- BLOCCO 2 (607 f = 20,2 s) ----------
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PERCHÉ SE NE PARLA ORA',cap:'UN\'INCHIESTA MOLTO VISTA HA APERTO LA DISCUSSIONE',items:[
  VT('PERCHÉ PROPRIO ORA?',960,250,'Perché se ne parla',GF_,46),
  I('hl',['SBERLA AI PENSIONATI'],620,520,"un'inchiesta giornalistica"),
  VT('MOLTO VISTA',620,690,'molto vista',AMB,40),
  I('bubble',[460,250],1420,470,'su YouTube'),
  VT('LA DISCUSSIONE',1420,690,'è partita la discussione',DF_,40)]},
 {at:'Io non ti porto opinioni',top:'NIENTE OPINIONI: IL CONTO',cap:'PRIMA SERVE UNA PAROLA SOLA: RIVALUTAZIONE',items:[
  VT('NIENTE OPINIONI',480,260,'Io non ti porto opinioni',RF_,44),
  I('calc',[],480,520,'ti porto il conto'),
  VT('PERCENTUALI UFFICIALI',480,760,'le percentuali ufficiali',GF_,38),
  VN('RIVALUTAZIONE',1340,430,'rivalutazione',{fs:84,fill:GF_,sub:'LA PAROLA CHIAVE',minw:760}),
  VT('IL TRUCCO STA QUI',1340,690,'tutto il trucco',AMB,42)]},
]);
// ---------- BLOCCO 3 (690 f = 23,0 s) ----------
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COS\'È LA RIVALUTAZIONE',cap:'OGNI GENNAIO LA PENSIONE SEGUE IL COSTO DELLA VITA',items:[
  I('calS',['GENNAIO','+ %',150,'OGNI ANNO',0.72],330,590,'Ogni gennaio'),
  I('basket',[],800,560,'il costo della vita'),
  VN('PREZZI +5 %',1470,330,'Se i prezzi salgono',{fs:72,fill:RF_,minw:560}),
  I('arD',[],1470,500,'la pensione dovrebbe salire'),
  VN('PENSIONE +5 %',1470,670,['la pensione dovrebbe salire',0.6],{fs:72,fill:GF_,minw:560}),
  VT('DOVREBBE...',800,800,'Dovrebbe.',AMB,44)]},
 {at:'Perché la legge',top:'MA NON PER TUTTI',cap:'LA PARTE NON DATA NON TORNA PIÙ INDIETRO',items:[
  I('trow',[1300,'Pensioni più basse','100 %',GF_],960,300,'solo alle pensioni più basse'),
  I('trow',[1300,'Tutte le altre','MENO',AMB],960,450,'Le altre ne ricevono'),
  I('stamp',['NON TORNA PIÙ INDIETRO',RED_,56],960,680,'non ti torna più indietro')]},
]);
// ---------- BLOCCO 4 (571 f = 19,0 s) ----------
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL METRO: IL MINIMO INPS',cap:'SOPRA I 2.100 € LORDI SI COMINCIA A PERDERE',items:[
  VT('IL METRO PER CAPIRE A CHI TOCCA',960,240,'si usa un metro',GF_,42),
  ...EQ(440,[['num','525 €','Nel duemilaventidue valeva',{sub:'MINIMO INPS 2022'}],['op','×','Quattro volte'],['num','4','Quattro volte il minimo',{sub:'VOLTE'}],['op','=','faceva circa'],['num','2.100 €','duemilacento euro lordi',{fill:AMB,sub:'LORDI AL MESE'}]],80,300),
  I('seg',[700,110,GF_,'SOTTO 2.100 €','NESSUNA PERDITA'],560,700,'chi non ha perso niente'),
  I('seg',[700,110,RF_,'SOPRA 2.100 €','INIZIA LA PERDITA'],1360,700,'cominciato a perdere')]},
]);
// ---------- BLOCCO 5 (871 f = 29,0 s) ----------
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'2023: L\'ANNO CHIAVE',cap:'RIVALUTAZIONE 8,1 %: LA PIÙ ALTA DEGLI ULTIMI ANNI',items:[
  I('calS',['ANNO','2023',125,'L\'ANNO CHIAVE',0.8],420,560,'Il duemilaventitré'),
  I('mbars',[],1320,500,'I prezzi corrono'),
  VN('+8,1 %',1320,720,'otto virgola uno',{fs:96,fill:GF_,sub:'RIVALUTAZIONE 2023',minw:560})]},
 {at:'Ma la legge di bilancio',top:'LE FASCE DEL 2023',cap:'SOPRA 4 VOLTE IL MINIMO: UNA PERCENTUALE SU TUTTO L\'ASSEGNO',items:[
  I('trow',[1400,'Fino a 4 volte il minimo','100 %',GF_],960,260,'aumento pieno'),
  I('trow',[1400,'Da 4 a 5 volte','85 %',AMB],960,390,"l'ottantacinque per cento"),
  I('trow',[1400,'Da 5 a 6 volte','53 %',RED_],960,520,'il cinquantatré'),
  I('trow',[1400,'Oltre 10 volte','32 %',RED_],960,650,'fino al trentadue'),
  VT('PERCENTUALE SU TUTTO L\'ASSEGNO',960,790,'una percentuale sola su tutto',DF_,40)]},
]);

// ---------- BLOCCO 6 (721 f = 24,0 s) ----------
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PRIMO SCONTRINO: 2023',cap:'SOLO NEL PRIMO ANNO: CIRCA 1.480 € LORDI IN MENO',items:[
  VN('3.000 €',480,300,'Pensione di tremila',{fs:80,sub:'LORDI A FINE 2022',minw:600}),
  VT('TRA 5 E 6 VOLTE IL MINIMO',480,500,'tra cinque e sei volte',AMB,38),
  VN('53 %',480,680,'prende il cinquantatré',{fs:80,fill:RF_,sub:'DELL\'AUMENTO',minw:420}),
  I('rcpt',[660,640,'SCONTRINO 2023',[['Senza taglio','3.243 €'],['Con il taglio','3.129 €',RED_],['Al mese','-114 €',RED_]],'-1.480 €','NEL PRIMO ANNO (X 13)'],1360,500,'Invece di salire')]},
]);
// ---------- BLOCCO 7 (787 f = 26,2 s) ----------
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SECONDO SCONTRINO: 2024',cap:'STESSE FASCE: LA NOSTRA PENSIONE È ANCORA AL 53 %',items:[
  I('calS',['ANNO','2024',125,'SECONDO',0.8],420,560,'Secondo scontrino'),
  VN('+5,4 %',1320,330,'cinque virgola quattro',{fs:76,fill:GF_,sub:'RIVALUTAZIONE 2024',minw:560}),
  VT('STESSE FASCE DEL 2023',1320,580,'le stesse fasce',DF_,40),
  VT('SOPRA 10 VOLTE: 22 %',1320,690,'ancora più forte',RF_,40),
  VT('LA NOSTRA: ANCORA 53 %',1320,800,'La nostra pensione',AMB,40)]},
 {at:'Ma attenzione: parte',top:'LA DISTANZA CRESCE',cap:'L\'AUMENTO PERSO NEL 2023 NON È MAI ARRIVATO',items:[
  VT('DISTANZA AL MESE: PARTE GIÀ PIÙ BASSA',960,250,'parte già più bassa',AMB,42),
  I('step',[320,210,RF_,'-114 €'],700,740,'non è mai arrivato'),
  I('step',[320,370,RF_,'-200 €'],1220,740,'sale a duecento'),
  VT('2023',700,800,['non è mai arrivato',0.5],DF_,36),
  VT('2024',1220,800,['sale a duecento',0.5],DF_,36)]},
]);
// ---------- BLOCCO 8 (810 f = 27,0 s) ----------
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DAL 2025: REGOLE NORMALI',cap:'LE PERCENTUALI SI APPLICANO A SCAGLIONI',items:[
  I('trow',[1400,'Fino a 4 volte il minimo','100 %',GF_],960,280,'aumento pieno'),
  I('trow',[1400,'Parte tra 4 e 5 volte','90 %',AMB],960,405,'novanta per cento'),
  I('trow',[1400,'Parte sopra 5 volte','75 %',AMB],960,530,'settantacinque per cento'),
  VT('SEMBRA UNA BUONA NOTIZIA',960,690,'Sembra una buona notizia',GF_,42)]},
 {at:'Ma la rivalutazione è bassa',top:'MA AUMENTI BASSI',cap:'LA DIFFERENZA ACCUMULATA NON SPARISCE',items:[
  VN('+0,8 %',480,320,'zero virgola otto',{fs:76,fill:AMB,sub:'RIVALUTAZIONE 2025',minw:520}),
  VN('+1,4 %',480,620,'uno virgola quattro',{fs:76,fill:AMB,sub:'RIVALUTAZIONE 2026',minw:520}),
  VN('-207 €',1340,400,'oggi sono circa',{fs:110,fill:RF_,sub:'AL MESE, OGGI',minw:560}),
  VT('LA DIFFERENZA RESTA',1340,690,'la differenza accumulata',AMB,42)]},
]);
// ---------- BLOCCO 9 (640 f = 21,3 s) ----------
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TOTALE',cap:'PARTENZA 3.000 € LORDI: IL BUCO NON SI RICHIUDE',items:[
  I('rcpt',[640,680,'SCONTRINO 2023-2026',[['2023','-1.482 €',RED_],['2024','-2.597 €',RED_],['2025','-2.630 €',RED_],['2026','-2.688 €',RED_]],'-9.400 €','CIRCA, LORDI'],560,495,'Ecco il totale'),
  VN('-2.700 €',1380,380,'duemilasettecento',{fs:90,fill:RF_,sub:'OGNI ANNO, DA ORA IN POI',minw:640}),
  I('stamp',['IL BUCO NON SI RICHIUDE',RED_,44],1380,700,'Questo è il buco')]},
]);
// ---------- BLOCCO 10 (595 f = 19,8 s) ----------
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TEST: DOMANDA 1',cap:'GRUPPO 1: NIENTE PERSO CON QUESTI TAGLI',items:[
  VT('DOMANDA 1',960,240,'Prima domanda',GF_,46),
  VN('SOTTO 2.440 €',1010,420,'sotto i duemilaquattrocentoquaranta',{fs:80,fill:GF_,sub:'PENSIONE LORDA DI OGGI',minw:760}),
  I('chk',[80],400,450,'non hai perso niente'),
  VT('RIVALUTAZIONE SEMPRE PIENA',960,680,'sempre la rivalutazione piena',GF_,40),
  VT('CONTA IL TOTALE: DUE PENSIONI SI SOMMANO',960,800,'conta il totale',AMB,38)]},
]);
// ---------- BLOCCO 11 (786 f = 26,2 s) ----------
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TEST: DOMANDA 2',cap:'GRUPPO 2: LA PERDITA C\'È, MA È CONTENUTA',items:[
  VT('DOMANDA 2',960,240,'Seconda domanda',GF_,46),
  VN('DA 2.440 A 3.000 €',960,430,'tra i duemilaquattrocentoquaranta',{fs:76,fill:AMB,sub:'PENSIONE LORDA DI OGGI',minw:900}),
  VT('PERDITA CONTENUTA',960,700,"Qui la perdita c'è",AMB,44)]},
 {at:'Esempio:',top:'ESEMPIO: 2.500 € NEL 2022',cap:'IN 4 ANNI CIRCA 2.500 € LORDI IN MENO',items:[
  I('rcpt',[640,600,'ESEMPIO: 2.500 € NEL 2022',[['Oggi','2.856 €'],['Senza tagli','2.911 €'],['Al mese','-55 €',RED_]],'-2.500 €','IN 4 ANNI, LORDI'],560,500,'Esempio'),
  VN('-700 €',1380,420,"settecento euro lordi l'anno",{fs:96,fill:RF_,sub:'OGNI ANNO, DA ORA',minw:560})]},
]);
// ---------- BLOCCO 12 (805 f = 26,8 s) ----------
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TEST: DOMANDA 3',cap:'GRUPPO 3: QUI LA PERDITA È GROSSA',items:[
  VT('DOMANDA 3',960,240,'Terza domanda',GF_,46),
  VN('SOPRA 3.000 €',960,430,'sopra i tremila',{fs:80,fill:RF_,sub:'PENSIONE LORDA DI OGGI',minw:760}),
  VT('2023 E 2024: FASCE DEL 53 % O MENO',960,700,'nelle fasce del cinquantatré',RF_,38)]},
 {at:'Il nostro esempio',top:'QUANTO HANNO PERSO',cap:'CIFRE LORDE: AL NETTO È MENO, MA LA PERDITA RESTA',items:[
  VN('-9.400 €',520,380,'ha perso circa novemila',{fs:96,fill:RF_,sub:'PARTENZA 3.000 €, OGGI 3.287 €',minw:700}),
  VN('> 12.000 €',1400,380,'oltre dodicimila',{fs:80,fill:RF_,sub:'PARTENZA 3.500 €',minw:640}),
  VT('AL NETTO DELLE TASSE È MENO, MA RESTA',960,700,'Sono cifre lorde',AMB,38)]},
]);
// ---------- BLOCCO 13 (686 f = 22,9 s) ----------
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'NON È LA PRIMA VOLTA',cap:'2012 E 2013: RIVALUTAZIONE BLOCCATA SOPRA 3 VOLTE IL MINIMO',items:[
  I('calS',['ANNI','2012-13',78,'BLOCCO',0.8],420,560,'Nel duemiladodici'),
  VT('SOPRA 3 VOLTE IL MINIMO',1300,280,'sopra tre volte il minimo',RF_,40),
  VN('0 %',1300,500,'bloccata del tutto',{fs:96,fill:RF_,sub:'RIVALUTAZIONE',minw:420})]},
 {at:'Nel duemilaquindici',top:'LA CORTE COSTITUZIONALE',cap:'CHI ERA GIÀ IN PENSIONE HA PERSO ANCHE LÌ',items:[
  VT('CORTE COSTITUZIONALE, 2015',520,280,'la Corte costituzionale',DF_,38),
  I('stamp',['ILLEGITTIMO',RED_,60],520,450,'era illegittimo'),
  VT('RIMBORSO SOLO PARZIALE',1460,280,'solo parziale',AMB,42),
  VN('PRIMA DEL 2012',1380,470,'prima del duemiladodici',{fs:64,fill:AMB,sub:'HA PERSO ANCHE LÌ',minw:640})]},
]);
// ---------- BLOCCO 14 (733 f = 24,4 s) ----------
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E ADESSO IL 2027',cap:'ISTAT, STIME PRELIMINARI DI FINE SETTEMBRE',items:[
  VT('ISTAT, STIME PRELIMINARI',960,240,'stime preliminari',DF_,40),
  VN('+4,2 %',520,460,'quattro virgola due',{fs:96,fill:RF_,sub:'PREZZI A SETTEMBRE, IN UN ANNO',minw:640}),
  VN('3,1 %',1400,460,'tre virgola uno',{fs:96,fill:AMB,sub:'MEDIA GIÀ ACQUISITA 2026',minw:640})]},
 {at:'Quindi a gennaio',top:'RIVALUTAZIONE 2027',cap:'PERCENTUALE UFFICIALE: DECRETO DEL MINISTERO DELL\'ECONOMIA',items:[
  I('calS',['GENNAIO','2027',125,'RIVALUTAZIONE',0.8],420,560,'Quindi a gennaio'),
  VN('CIRCA 3 %',1300,360,'intorno al tre per cento',{fs:90,fill:GF_,sub:'STIMA, NON UFFICIALE',minw:600}),
  VT('DECRETO: DI SOLITO A FINE NOVEMBRE',1300,640,'un decreto del Ministero',DF_,36)]},
]);
// ---------- BLOCCO 15 (793 f = 26,4 s) ----------
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SE ARRIVA IL 3 %',cap:'AUMENTI LORDI AL MESE, SE RESTANO LE REGOLE DI OGGI',items:[
  VT('SE LA RIVALUTAZIONE È DEL 3 %',960,240,'un tre per cento',GF_,40),
  I('trow',[1300,'Pensione 2.000 € lordi','+60 €',GF_],960,390,'circa sessanta'),
  I('trow',[1300,'Pensione 2.500 € lordi','+75 €',GF_],960,515,'circa settantacinque'),
  I('trow',[1300,'Pensione 3.000 € lordi','+88 €',GF_],960,640,'circa ottantotto')]},
 {at:'Ma attenzione: sui giornali',top:'L\'IPOTESI DEI GIORNALI',cap:'IL TESTO DELLA MANOVRA ARRIVA IN PARLAMENTO A GIORNI',items:[
  I('hl',['NUOVO TAGLIO ALLA RIVALUTAZIONE?'],960,320,'sui giornali gira'),
  VT('SOPRA CIRCA 3 VOLTE IL MINIMO',960,510,'sopra circa tre volte',RF_,40),
  I('stamp',['SOLO UN\'IPOTESI: NIENTE DI DECISO',RED_,44],960,680,"solo un'ipotesi")]},
]);
// ---------- BLOCCO 16 (542 f = 18,1 s) ----------
SPECS[16]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA DOMANDA VERA',cap:'NON QUANTO AUMENTA, MA SE LE FASCE SARANNO TAGLIATE',items:[
  VT('IL 2027 SARÀ...',960,240,'se il duemilaventisette',GF_,46),
  VN('PIENA',560,440,'rivalutazione piena',{fs:84,fill:GF_,sub:'RIVALUTAZIONE',minw:520}),
  I('op',['O'],960,470,'o un altro anno'),
  VN('TAGLIATA',1360,440,'fasce tagliate',{fs:84,fill:RF_,sub:'FASCE',minw:520}),
  VT('CONTO AGGIORNATO APPENA È UFFICIALE',960,660,'faccio il conto aggiornato',AMB,38),
  I('btn',['ISCRIVITI'],960,790,'iscriviti al canale')]},
]);
// ---------- BLOCCO 17 (781 f = 26,0 s) - ULTIMO: parte bassa libera per la schermata finale (N.22) ----------
SPECS[17]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IN QUALE FASCIA SEI?',cap:'',items:[
  VT('SCRIVILO NEI COMMENTI',960,225,'Scrivimi nei commenti',GF_,40),
  VT('SOTTO 2.440 €',430,330,'sotto i duemila',GF_,38),
  VT('IN MEZZO',960,330,'in mezzo',AMB,38),
  VT('SOPRA 3.000 €',1490,330,'o sopra i tremila',RF_,38),
  I('dbg',[1560,300],960,590,'sono conti di esempio'),
  I('dline',['CONTI DI ESEMPIO, LORDI E ARROTONDATI','#fff',38],960,582,'sono conti di esempio'),
  I('dline',['VERIFICA SUL SITO DELL\'INPS O CON UN PATRONATO','#fff',38],960,642,'controlla sempre sul sito'),
  I('dline',['CANALE INFORMATIVO, NON AFFILIATO ALL\'INPS','#7FF0D2',38],960,702,'non è affiliato')]},
]);
