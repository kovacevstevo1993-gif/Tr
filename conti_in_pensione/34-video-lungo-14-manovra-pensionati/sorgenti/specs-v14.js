// ===== VIDEO 14 (manovra 2027 e pensionati) - stile nuovo (N.37, N.47): titoletto SENZA numero, con tre misure (FONDO / IRPEF / BUONO) di cui si accende quella in corso;
// didascalia a pannello con barra di segno "§"; sfondo con bande diagonali, simboli, quadrante. Stessi colori del canale.
const MIS14=['FONDO','IRPEF','BUONO'];
function mis14(n){if(n===3||n===9||n===10)return [0];if(n===4||n===11||n===12)return [1];if(n>=6&&n<=8)return [2];if(n===15)return [0,1,2];return [];}
function topLabel(g,s){const t=el('g',{transform:'translate(-840 0)'},g);
 el('rect',{x:0,y:-34,width:10,height:68,rx:5,fill:AMB},t);
 const x=fitT(t,s,34,0,36,'#7FF0D2','bold',900,'start');x.setAttribute('letter-spacing','5');
 const on=mis14(N);const CW=170,CG=10,X0=1680-(3*CW+2*CG);
 MIS14.forEach((p,i)=>{const a=on.indexOf(i)>=0;const cx=X0+i*(CW+CG);
  el('rect',{x:cx,y:-24,width:CW,height:48,rx:12,fill:a?AMB:'#06303A',stroke:a?'#fff':'#7FF0D2','stroke-width':a?3:2,opacity:a?1:0.55},t);
  txt(t,p,cx+CW/2,8,24,a?'#5A3300':'#fff','900');});
 return t;}
function cap(g,s,size){size=size||44;const c=el('g',{},g);if(!s)return c;
 const t=txt(c,s,0,0,size,'#FFFFFF','bold');let tl=mw(t,s,size);
 const maxT=1540;if(tl>maxT){size=size*maxT/tl;t.setAttribute('font-size',size.toFixed(1));tl=mw(t,s,size);}
 const padL=110,padR=60;const w=tl+padL+padR;
 t.setAttribute('x',(-w/2+padL+tl/2).toFixed(1));t.setAttribute('y',(size*0.36).toFixed(1));
 const ins=e=>{c.insertBefore(e,t);return e;};
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:16,fill:'#06303A',filter:'url(#g_sh2)'}));
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:16,fill:'none',stroke:AMB,'stroke-width':3,opacity:.55}));
 ins(el('rect',{x:-w/2,y:-56,width:84,height:112,rx:16,fill:AMB}));
 ins(el('rect',{x:-w/2+40,y:-56,width:44,height:112,fill:AMB}));
 txt(c,'§',-w/2+42,22,70,'#5A3300','900');
 return c;}
const Q8=(title,l1,l2,x,y,w,h,at,hc)=>I('card',[title,w,h,{hc:hc||'#0B4A50',lines:[[l1,34,-6,INK],[l2,28,46,GRN]],hfs:30}],x,y,at);
// ======================= BLOCCHI =======================
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'MANOVRA E PENSIONATI',cap:'TRE MISURE ANNUNCIATE: SOLO UNA VALE FINO A 500 € ALL\'ANNO',items:[
  IC(540,190,'env',[['BUONO SANITARIO',34],['PER GLI ANZIANI',30,GRN]],330,320,'Un buono sanitario'),
  IC(540,190,'signs',[['FONDO PER L\'USCITA',34],['DAL LAVORO',30,GRN]],960,320,'un fondo per l\'uscita dal lavoro'),
  IC(540,190,'cut',[['MENO IRPEF',38]],1590,320,'meno Irpef'),
  P('UNA VALE FINO A 500 € ALL\'ANNO',960,485,'Una vale fino a cinquecento',AMB,38,'coin'),
  P('MA NON PER OGNI PENSIONATO',960,570,'ma non per ogni pensionato',RF_,34,'warn'),
  P('QUALI PENSIONATI CI GUADAGNANO?',360,665,'Quali pensionati ci guadagnano?',DF_,26,'q'),
  P('A CHI SPETTA IL BUONO?',960,665,'A chi spetta il buono?',DF_,26,'q'),
  P('DA CHE ETÀ SI POTRÀ USCIRE?',1560,665,'E da che età si potrà uscire?',DF_,26,'q'),
  I('stamp',[['DISEGNO DI LEGGE','PUÒ CAMBIARE'],RED_,38,-4],640,790,'Per ora è un disegno di legge'),
  P('DOCUMENTI UFFICIALI',1360,790,'Lo vediamo con i documenti ufficiali',AMB,36,'doc')]},
]);
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE FONTI UFFICIALI',cap:'DUE FONTI UFFICIALI SUL SITO DEL GOVERNO',items:[
  P('SITO DEL GOVERNO',960,225,'sul sito del governo',AMB,38,'web'),
  IC(640,210,'doc',[['COMUNICATO DEL CONSIGLIO',30],['DEI MINISTRI N. 195',34],['DEL 28 OTTOBRE',30,GRN]],480,410,'il comunicato del Consiglio dei ministri numero'),
  IC(640,210,'chat',[['INTERVENTO DELLA PRESIDENTE',30],['DEL CONSIGLIO MELONI',34],['ALLA CONFERENZA STAMPA',28,GRN]],1440,410,'l\'intervento della presidente'),
  P('SOLO QUESTI DUE DOCUMENTI UFFICIALI',960,600,'Ci basiamo solo su questi due',GF_,34,'ok'),
  P('NON BOZZE, NON CIFRE DEI GIORNALI',960,695,'non su bozze',RF_,34,'x'),
  P('ORDINE: FONDO → IRPEF → BUONO',960,790,'Li vediamo in quest\'ordine',AMB,40,'next')]},
]);
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL FONDO',cap:'FONDO DA 850 MILIONI: I DETTAGLI SI DECIDONO IN PARLAMENTO',items:[
  P('DAL COMUNICATO',480,225,'il comunicato scrive',DF_,32,'doc'),
  BN('FONDO ISTITUITO','850 MILIONI','DI EURO',Object.assign({fs:84,minw:640,tfs:28,sfs:30},AMBB),480,430,'ottocentocinquanta milioni'),
  IC(800,140,'signs',[['FLESSIBILITÀ IN USCITA DAL LAVORO',30]],1400,285,'flessibilità in uscita'),
  IC(800,140,'calc',[['PER CHI ACCEDE ALLA PENSIONE',28],['CON IL SISTEMA CONTRIBUTIVO',30,GRN]],1400,445,'sistema contributivo'),
  IC(1100,125,'chat',[['LA PRESIDENTE: «BISOGNERÀ LAVORARE»',34]],960,640,'bisognerà lavorare'),
  IC(1100,125,'stato',[['SI LAVORERÀ NEL DIBATTITO PARLAMENTARE',32]],960,790,'dibattito parlamentare')]},
]);
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'L\'IRPEF',cap:'IRPEF: IL 33 % VALE FINO A 55.000 €, BENEFICIO MASSIMO 500 €',items:[
  P('LA PRESIDENTE: ALZIAMO LA SOGLIA',960,225,'La presidente dice',DF_,32,'chat'),
  I('seg',[760,96,'#0B4A50','SCAGLIONE DEL 33 %',null],600,335,'secondo scaglione'),
  I('seg',[640,96,AMB,'FINO A 55.000 €',null],1340,335,'fino a cinquantacinquemila'),
  BN('BENEFICIO MASSIMO','≈ 500 €','ALL\'ANNO',Object.assign({fs:100,minw:560,tfs:28,sfs:30},GRNB),500,570,'beneficio massimo'),
  IC(820,160,'doc',[['IL COMUNICATO CONFERMA',30],['33 % ESTESO FINO A 55.000 €',28,GRN]],1380,545,'Il comunicato conferma'),
  I('stamp',[['MASSIMO'],RED_,56,-4],760,790,'la parola massimo'),
  P('TRA POCO: PER CHI VALE',1400,790,'per chi vale',AMB,36,'lens')]},
]);
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PRIMA DI CONTINUARE',cap:'ISCRIVITI SE TI STIAMO FACENDO RISPARMIARE TEMPO',items:[
  IC(880,170,'doc',[['QUESTO VIDEO PARTE',30],['DALLE FONTI UFFICIALI',34,GRN]],500,300,'parte dalle fonti ufficiali'),
  IC(880,140,'clock',[['LEGGERLE RICHIEDE ORE',36]],500,490,'richiede ore'),
  I('btn',['ISCRIVITI'],1340,330,'iscriviti'),
  I('bell',[],1760,350,'iscriviti',0.8),
  P('PER TE: UN TOCCO',1330,520,'per te è un tocco',DF_,36,'ok'),
  P('PER NOI: UN AIUTO CONCRETO',1330,620,'per noi è un aiuto concreto',DF_,36,'ok'),
  P('ADESSO IL BUONO: CINQUE PUNTI SENZA RISPOSTA',960,790,'Adesso il buono',AMB,38,'q')]},
]);
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL BUONO',cap:'BUONO DA 300 €: OLTRE 75 ANNI, PENSIONE FINO A 28.000 € ANNUI',items:[
  P('DAL COMUNICATO',450,225,'Il comunicato dice',DF_,32,'doc'),
  BN('BUONO','300 €','PER LE SPESE SANITARIE',Object.assign({fs:120,minw:500,tfs:26,sfs:26},AMBB),410,440,'un buono di trecento euro'),
  IC(960,125,'people',[['PIÙ DI 75 ANNI',38]],1330,270,'età superiore ai settantacinque'),
  IC(960,125,'coin',[['PENSIONE FINO A 28.000 € ANNUI',34]],1330,415,'pensione fino a ventottomila'),
  IC(960,125,'house',[['SPESE SANITARIE NON COPERTE',32],['DAL SERVIZIO SANITARIO NAZIONALE',26,GRN]],1330,560,'spese sanitarie che'),
  P('MELONI AGGIUNGE:',360,760,'La presidente Meloni aggiunge',DF_,32,'chat'),
  P('FARMACI',830,760,'per i farmaci',AMB,38,'ok'),
  P('VISITE SPECIALISTICHE',1360,760,'visite specialistiche',AMB,38,'ok')]},
]);
const EQ14=(y,parts)=>EQ(y,parts,66,260);
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTROLLO SUI NUMERI',cap:'5,5 MILIONI × 300 € = 1,65 MILIARDI: L\'ORDINE DI GRANDEZZA TORNA',items:[
  P('LA PRESIDENTE: 5,5 MILIONI DI PERSONE',560,240,'La presidente parla',DF_,30,'people'),
  P('COSTO: 1,6 MILIARDI',1440,240,'di un costo di un miliardo',DF_,30,'coin'),
  ...EQ14(420,[['num','5,5 MLN','Cinque milioni e mezzo per',{sub:'PERSONE'}],['op','×','per trecento'],['num','300 €','trecento euro fanno',{sub:'A TESTA'}],['op','=','fanno un miliardo'],['num','1,65 MLD','un miliardo e seicentocinquanta',{sub:'DI EURO',fill:AMB}]]),
  P('L\'ORDINE DI GRANDEZZA TORNA',960,590,'l\'ordine di grandezza',GF_,36,'ok'),
  IC(640,140,'ok',[['300 € IN TOTALE',36],['PER OGNI PERSONA',28,GRN]],560,750,'trecento euro in totale'),
  IC(640,140,'x',[['NON UNA CIFRA MENSILE',34]],1360,750,'non con una cifra mensile',{stroke:RED_})]},
]);
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CINQUE COSE NON DETTE',cap:'DEL BUONO MANCANO ANCORA CINQUE RISPOSTE',items:[
  Q8('UNO','COME SI OTTIENE?','AUTOMATICO O SERVE UNA DOMANDA',330,320,560,240,'Uno: come si ottiene'),
  Q8('DUE','QUANDO ARRIVA?','LA DATA NON C\'È',960,320,560,240,'Due: quando arriva'),
  Q8('TRE','QUANTE VOLTE?','UNA VOLTA SOLA O OGNI ANNO',1590,320,560,240,'Tre: se vale'),
  Q8('QUATTRO','28.000 €: LORDI O NETTI?','SOLO PENSIONE O TUTTO IL REDDITO',520,610,840,240,'Quattro: se i ventottomila'),
  Q8('CINQUE','CHI SUPERA IL LIMITE?','DI POCO: COSA SUCCEDE',1360,610,720,240,'Cinque: cosa succede'),
  I('stamp',[['DOMANDE APERTE'],RED_,40,-4],960,810,'domande aperte')]},
]);
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TORNIAMO AL FONDO',cap:'DEL FONDO NON SONO SCRITTI ETÀ, CONTRIBUTI E IMPORTO',items:[
  I('card',['ETÀ DI USCITA',500,290,{hc:'#C0392B',lines:[['?',120,-2,INK],['NON SCRITTA',34,100,RED_]]}],330,330,'l\'età di uscita'),
  I('card',['CONTRIBUTI RICHIESTI',500,290,{hc:'#C0392B',lines:[['?',120,-2,INK],['NON SCRITTI',34,100,RED_]]}],960,330,'i contributi richiesti'),
  I('card',['IMPORTO DELL\'ASSEGNO',500,290,{hc:'#C0392B',lines:[['?',120,-2,INK],['NON SCRITTO',34,100,RED_]]}],1590,330,'l\'importo dell\'assegno'),
  IC(1500,130,'q',[['IL FONDO CAMBIA LA REGOLA GIÀ ESISTENTE?',36],['PER I CONTRIBUTIVI PURI: IL COMUNICATO NON LO DICE',28,GRN]],960,590,'Il comunicato non dice nemmeno'),
  P('LA REGOLA ESISTENTE: SUBITO',560,790,'Quella regola la vediamo subito',DF_,34,'next'),
  P('COSÌ SAI DA DOVE SI PARTE',1370,790,'così sai da dove si parte',AMB,36,'ruler')]},
]);
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA REGOLA DEL 2027',cap:'LA REGOLA GIÀ FISSATA PER IL 2027',items:[
  P('REGOLA GIÀ FISSATA PER IL 2027',960,225,'La regola già fissata',DF_,36,'lock'),
  I('card',['ETÀ',520,300,{hc:'#2B6F8F',lines:[['64 ANNI',72,0,INK],['E 1 MESE',40,80,GRN]]}],330,440,'sessantaquattro anni'),
  I('card',['CONTRIBUTI EFFETTIVI',520,300,{hc:'#1B9F81',lines:[['20 ANNI',72,0,INK],['E 1 MESE',40,80,GRN]]}],960,440,'venti anni e un mese'),
  I('card',['ASSEGNO MINIMO',520,300,{hc:'#E39A1C',lines:[['3 ×',72,0,INK],['ASSEGNO SOCIALE',34,80,GRN]]}],1590,440,'almeno tre volte'),
  BN('CON I VALORI DI QUEST\'ANNO','1.638,72 €','ASSEGNO MINIMO RICHIESTO',Object.assign({fs:82,minw:700,tfs:26,sfs:26},AMBB),700,745,'milleseicentotrentotto'),
  P('MADRI: SOGLIA PIÙ BASSA',1500,745,'Per le madri',GF_,36,'down')]},
]);
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO DELL\'IRPEF',cap:'LA FETTA TRA 50.000 E 55.000 € PAGA 10 PUNTI IN MENO',items:[
  P('OGGI',360,215,'Oggi il reddito',DF_,34,'cal'),
  I('seg',[760,96,'#0B4A50','33 %','DA 28.000 A 50.000 €'],640,305,'tra ventottomila e cinquantamila'),
  I('seg',[640,96,RED_,'43 %','OLTRE 50.000 €'],1350,305,'quello oltre il quarantatré'),
  P('CON LA MANOVRA',450,450,'Con la manovra',AMB,34,'up'),
  I('seg',[760,96,'#0B4A50','33 %',null],640,540,'il trentatré vale fino ai'),
  I('seg',[340,96,AMB,'33 %','DA 50.000 A 55.000 €'],1260,540,'La fetta tra cinquantamila'),
  P('− 10 PUNTI',1690,540,'dieci punti in meno',GF_,38,'down'),
  P('IL 10 % DI 5.000 € = 500 €',960,740,'il dieci per cento di cinquemila',AMB,44,'calc'),
  P('SOTTO I 50.000 €: NIENTE CAMBIA',960,830,'Sotto i cinquantamila',DF_,34,'ok')]},
]);
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CHI CI GUADAGNA',cap:'FINO A 500 € ALL\'ANNO: SOLO DA 55.000 € IN SU',items:[
  P('≈ 3.850 € AL MESE · 13 MENSILITÀ',960,225,'circa tremilaottocentocinquanta',DF_,32,'cal'),
  I('vbar',[200,26,'#5C7C86','0 €','50.000 €'],400,720,'Un pensionato con cinquantamila'),
  I('vbar',[200,132,'#2B8FA0','200 €','52.000 €'],780,720,'Con cinquantaduemila'),
  I('vbar',[200,264,'#1B9F81','400 €','54.000 €'],1160,720,'Con cinquantaquattromila'),
  I('vbar',[200,330,AMB,'500 € · MASSIMO','55.000 € E OLTRE'],1540,720,'Da cinquantacinquemila'),
  P('IRPEF NAZIONALE, SENZA ADDIZIONALI',560,850,'Sono importi di Irpef nazionale',DF_,28),
  P('SE LA PENSIONE È L\'UNICO REDDITO',1400,850,'se la pensione è l\'unico',DF_,28)]},
]);
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COSA NON C\'È',cap:'NEI DOCUMENTI UFFICIALI NON COMPAIONO RIVALUTAZIONE E AUMENTI',items:[
  IC(580,150,'x',[['RIVALUTAZIONE',36],['NON COMPARE',26,RED_]],330,270,'la rivalutazione',{stroke:RED_}),
  IC(580,150,'x',[['AUMENTO DELLE PENSIONI',32],['NON COMPARE',26,RED_]],930,270,'l\'aumento delle pensioni',{stroke:RED_}),
  IC(580,150,'x',[['PENSIONI MINIME',36],['NON COMPARE',26,RED_]],330,450,'le pensioni minime',{stroke:RED_}),
  IC(580,150,'x',[['REQUISITI PER LA PENSIONE',30],['NON COMPARE',26,RED_]],930,450,'i requisiti per andare',{stroke:RED_}),
  I('card',['DECRETO DEI MINISTERI',560,290,{hc:'#2B6F8F',lines:[['FISSA L\'AUMENTO',34,-6,INK],['DI GENNAIO',34,40,INK],['ANNO SCORSO: 19 NOVEMBRE',26,110,GRN]]}],1570,360,'L\'aumento di gennaio lo fissa'),
  P('QUELLO DELL\'ANNO SCORSO: 19 NOVEMBRE',960,650,'quello dell\'anno scorso',DF_,34,'cal'),
  P('QUANDO ESCE, RIFACCIAMO IL CONTO',960,780,'Quando esce, rifacciamo',AMB,38,'calc')]},
]);
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DATI NON UFFICIALI',cap:'IPOTESI E BOZZE DI STAMPA: NON SONO DATI CERTI',items:[
  P('I NUMERI CHE CIRCOLANO',960,225,'sui numeri che circolano',DF_,36,'chat'),
  I('card',['IPOTESI DELLA STAMPA',700,230,{hc:'#C0392B',lines:[['64 ANNI CON 36 DI CONTRIBUTI',34,10,INK]]}],520,400,'sessantaquattro anni con trentasei'),
  I('card',['IPOTESI DELLA STAMPA',700,230,{hc:'#C0392B',lines:[['TAGLI ALLA RIVALUTAZIONE',34,-6,INK],['PER FASCE',34,40,INK]]}],1400,400,'i tagli alla rivalutazione'),
  IC(1500,120,'book',[['VENGONO DA IPOTESI E BOZZE RIPORTATE DALLA STAMPA',32]],960,590,'vengono da ipotesi e bozze'),
  P('NEI DOCUMENTI UFFICIALI: NON CI SONO',960,730,'Nei documenti ufficiali',RF_,36,'x'),
  I('stamp',[['NON SONO DATI CERTI'],RED_,36,-3],960,830,'non sono dati certi')]},
]);
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TRE PUNTI',cap:'',items:[
  I('card',['UNO · IL BUONO',560,230,{hc:'#2B8FA0',lines:[['È ANNUNCIATO',34,-10,INK],['MANCANO MODALITÀ,',28,38,GRN],['DATE E LIMITI',28,72,GRN]]}],330,290,'Uno: il buono'),
  I('card',['DUE · IL FONDO',560,230,{hc:'#1B9F81',lines:[['MANCANO ANCORA',34,-10,INK],['LE REGOLE',34,40,GRN]]}],960,290,'Due: sul fondo'),
  I('card',['TRE · L\'IRPEF',560,230,{hc:'#E39A1C',lines:[['AL MASSIMO 500 €',34,-10,INK],['PER CHI SUPERA',28,38,GRN],['I 50.000 € DI REDDITO',28,72,GRN]]}],1590,290,'Tre: l\'Irpef'),
  P('UN PARENTE OLTRE I 75 ANNI? MANDAGLI IL VIDEO',960,450,'Hai un parente',AMB,36,'share'),
  I('dbox',[1500,190,[['CANALE INFORMATIVO, NON CONSULENZA, NON AFFILIATO ALL\'INPS',30,'#fff'],['VERIFICA SU INPS.IT O CON UN PATRONATO',30,'#7FF0D2']]],960,590,'Canale informativo')]},
]);
