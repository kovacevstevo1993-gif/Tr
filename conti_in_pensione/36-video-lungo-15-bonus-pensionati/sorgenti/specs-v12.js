// ===== VIDEO 12 (coefficienti di trasformazione 2027) - elementi nuovi + 15 blocchi =====
// Un po' diverso dai video 8-11 (N.37, N.47), stessi colori: titoletto con numero del blocco e striscia di avanzamento a 15 tacche,
// didascalia con filo giallo in alto, decreto con sigillo, scalinata, grafico a barre per età, scala dei mesi con bandierine.
const NB12=15;
const TABD12=[-1.21,-1.25,-1.31,-1.34,-1.39,-1.46,-1.48,-1.55,-1.60,-1.64,-1.68,-1.74,-1.83,-1.90,-1.97];
function topLabel(g,s){const t=el('g',{transform:'translate(-840 0)'},g);
 const b=el('g',{transform:'translate(0 0)'},t);
 el('rect',{x:-56,y:-42,width:112,height:84,rx:22,fill:'#06303A',stroke:'#7FF0D2','stroke-width':3,filter:'url(#g_sh3)'},b);
 txt(b,(N<10?'0':'')+N,0,15,42,AMB,'900');
 const x=txt(t,s,86,12,36,'#7FF0D2','bold','start');x.setAttribute('letter-spacing','6');
 let w=tw(s,36)+s.length*6;try{w=x.getBBox().width;}catch(e){}
 el('rect',{x:86,y:30,width:Math.min(w,150),height:5,rx:2.5,fill:AMB},t);
 const X0=1320,DX=28;
 for(let i=0;i<NB12;i++){const on=(i+1)===N;el('rect',{x:X0+i*DX,y:on?-16:-9,width:22,height:on?32:18,rx:5,fill:on?AMB:'#7FF0D2',opacity:on?1:((i+1)<N?.8:.26)},t);}
 return t;}
function cap(g,s,size){size=size||44;const c=el('g',{},g);if(!s)return c;
 const t=txt(c,s,0,0,size,'#FFFFFF','bold');let tl=mw(t,s,size);
 const maxT=1540;if(tl>maxT){size=size*maxT/tl;t.setAttribute('font-size',size.toFixed(1));tl=mw(t,s,size);}
 const padL=120,padR=60;const w=tl+padL+padR;
 t.setAttribute('x',(-w/2+padL+tl/2).toFixed(1));t.setAttribute('y',(size*0.36).toFixed(1));
 const ins=e=>{c.insertBefore(e,t);return e;};
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:22,fill:'#06303A',filter:'url(#g_sh2)'}));
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:22,fill:'none',stroke:'#7FF0D2','stroke-width':2.5,opacity:.45}));
 ins(el('rect',{x:-w/2+34,y:-56,width:w-68,height:7,rx:3.5,fill:AMB}));
 const ib=el('g',{transform:'translate('+(-w/2+62)+' 4)'},c);el('circle',{r:30,fill:'#0D5158',stroke:'#7FF0D2','stroke-width':3},ib);
 el('path',{d:'M-10 -14 L16 0 L-10 14 Z',fill:AMB,'stroke-linejoin':'round',stroke:AMB,'stroke-width':4},ib);
 return c;}
// ---------- decreto: foglio con testata scura, righe e sigillo ----------
function decreeB(g,w,h,head,sub){
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:84,rx:26,fill:'#0B4A50'},g);el('rect',{x:-w/2,y:-h/2+50,width:w,height:34,fill:'#0B4A50'},g);
 el('rect',{x:-w/2,y:-h/2+80,width:w,height:5,fill:AMB},g);
 fitT(g,head,0,-h/2+42,34,'#fff','900',w-50);
 if(sub)fitT(g,sub,0,-h/2+132,34,GRN,'900',w-50);
 [0,1,2].forEach(i=>el('rect',{x:-w/2+44,y:-h/2+176+i*40,width:i==2?w*0.5:w-88,height:14,rx:7,fill:'#C3D3D7'},g));
 const sg=el('g',{transform:'translate('+(w/2-96)+' '+(h/2-84)+')'},g);
 el('circle',{r:56,fill:AMB,stroke:'#fff','stroke-width':5},sg);el('circle',{r:42,fill:'none',stroke:'#5A3300','stroke-width':3,'stroke-dasharray':'4 6'},sg);ico(sg,'stato',0.8,'#5A3300');
 return g;}
// ---------- grafico a barre per età (altezza = variazione, da zero) ----------
function agebarsB(g,W,H){const n=TABD12.length,gap=W/n,bw=gap*0.66;const base=H/2;
 el('rect',{x:-W/2-10,y:base,width:W+20,height:8,rx:4,fill:'#06303A',stroke:'#7FF0D2','stroke-width':2},g);
 TABD12.forEach((v,i)=>{const h=H*Math.abs(v)/2.2;const x=-W/2+i*gap+gap/2;const f=i/(n-1);
  const col=f<0.34?'#2B6F77':(f<0.67?'#E39A1C':'#D23A25');
  el('rect',{x:x-bw/2,y:base-h,width:bw,height:h,rx:10,fill:col,stroke:'#fff','stroke-width':3,filter:'url(#g_sh3)'},g);
  txt(g,String(57+i),x,base+46,30,'#E9FBF6','bold');});
 txt(g,'ETÀ DI USCITA  →',0,base+98,30,'#7FF0D2','bold');
 return g;}
// ---------- barra con cifra sopra e età sotto (origine = base) ----------
function vbarB(g,w,h,fill,top,bottom){
 el('rect',{x:-w/2,y:-h,width:w,height:h,rx:16,fill:fill,stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},g);
 fitT(g,top,0,-h-38,44,'#fff','900',w+120);fitT(g,bottom,0,50,34,'#E9FBF6','bold',w+120);return g;}
// ---------- scala dei mesi ----------
function maxisB(g,W,months){el('rect',{x:-W/2-10,y:-6,width:W+20,height:12,rx:6,fill:'#06303A',stroke:'#7FF0D2','stroke-width':2},g);
 for(let m=0;m<=months;m++){const x=-W/2+m*W/months;const big=(m%6===0);el('rect',{x:x-2,y:big?-24:-14,width:4,height:big?48:28,rx:2,fill:big?AMB:'#7FF0D2',opacity:big?1:.7},g);
  if(big)txt(g,String(m),x,76,38,'#fff','900');}
 txt(g,'MESI',W/2-20,76,30,'#7FF0D2','bold','end');return g;}
function flagB(g,label,fill,ph,col,dx){el('line',{x1:0,y1:0,x2:0,y2:-ph,stroke:'#fff','stroke-width':6,'stroke-linecap':'round'},g);
 el('circle',{r:16,fill:fill,stroke:'#fff','stroke-width':5},g);
 const pg=el('g',{transform:'translate('+(dx||0)+' '+(-ph-34)+')'},g);pillB(pg,label,30,fill,col||'#fff');return g;}
Object.assign(BUILD,{
 decree:(g,w,h,head,sub)=>decreeB(g,w,h,head,sub),
 agebars:(g,W,H)=>agebarsB(g,W,H),
 vbar:(g,w,h,fill,top,bottom)=>vbarB(g,w,h,fill,top,bottom),
 maxis:(g,W,m)=>maxisB(g,W,m),
 flag:(g,label,fill,ph,col,dx)=>flagB(g,label,fill,ph,col,dx),
});
const AM_='#5A3300';
// ======================= BLOCCHI =======================
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONE DAL 1° GENNAIO 2027',cap:'A PARITÀ DI CONTRIBUTI E DI ETÀ: 836 EURO ALL\'ANNO IN MENO RISPETTO AL 2023',items:[
  P('PENSIONE DAL PRIMO GENNAIO',960,225,'Pensione dal primo gennaio',AMB,38,'cal'),
  I('bign',['ASSEGNO PIÙ BASSO DI','− 836 €','ALL\'ANNO, RISPETTO A CHI È USCITO NEL 2023',{fs:132,fill:RF_,col:'#fff',subcol:'#fff',minw:760,tfs:32,sfs:28}],520,520,'più basso di ottocentotrentasei'),
  I('icard',[700,150,'coin',[['400.000 € DI CONTRIBUTI',34],['STESSI CONTRIBUTI DI PRIMA',26,GRN]],{lh:44}],1430,370,'quattrocentomila euro di contributi'),
  I('icard',[700,150,'clock',[['USCITA A 67 ANNI',38],['STESSA ETÀ DI USCITA',26,GRN]],{lh:44}],1430,550,'un\'uscita a sessantasette anni'),
  I('stamp',[['È UN DECRETO','DI OTTOBRE'],GRN,38,-4],1430,745,'è un decreto di ottobre'),
  P('PER RECUPERARE: IL CONTO, ALLA FINE',520,790,'c\'è un conto per recuperare',AMB,34,'lock')]},
]);
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL DECRETO DEL 16 OTTOBRE',cap:'CAMBIA UNA TABELLA DI 15 RIGHE: I COEFFICIENTI DI TRASFORMAZIONE',items:[
  I('decree',[600,340,'DECRETO · 16 OTTOBRE','MINISTERO DEL LAVORO'],480,380,'Il decreto è datato sedici ottobre'),
  I('icard',[760,120,'stato',[['MINISTERO DEL LAVORO',36],['HA EMANATO IL DECRETO',26,GRN]],{lh:44,ir:46}],1430,260,'Lo ha emanato il Ministero del Lavoro'),
  I('icard',[760,120,'stato',[['DI CONCERTO CON L\'ECONOMIA',34],['MINISTERO DELL\'ECONOMIA',26,GRN]],{lh:44,ir:46}],1430,400,'di concerto con quello dell\'Economia'),
  P('RESO NOTO IL 20 OTTOBRE',1430,520,'lo ha reso noto il venti',AMB,36,'cal'),
  I('bign',['UNA TABELLA DI','15 RIGHE','I COEFFICIENTI DI TRASFORMAZIONE',{fs:100,fill:GF_,col:'#fff',subcol:'#fff',minw:600,tfs:28,sfs:26}],480,690,'Cambia una tabella di quindici righe'),
  I('icard',[760,120,'cal',[['IN VIGORE DAL 1° GENNAIO 2027',32],['CON IL NUOVO ANNO',26,GRN]],{lh:44,ir:46}],1430,640,'primo gennaio duemilaventisette'),
  P('NON TOCCA TUTTI: CHI È DENTRO?',1430,790,'Ma non toccano tutti',DF_,32,'q')]},
]);
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL COEFFICIENTE A 67 ANNI',cap:'DA 5,723 A 5,608 A 5,514: IN TOTALE MENO 3,65 PER CENTO',items:[
  P('PRENDI 67 ANNI',960,222,'Prendi sessantasette anni',AMB,40,'clock'),
  I('bign',['2023 E 2024','5,723 %',null,{fs:84,minw:420,tfs:30,padh:60}],340,430,'cinque virgola settecentoventitré'),
  I('arR',[],650,430,'Poi cinque virgola seicentotto',0.45),
  I('bign',['2025 E 2026','5,608 %',null,{fs:84,minw:420,tfs:30,padh:60}],960,430,'cinque virgola seicentotto'),
  I('arR',[],1270,430,'Da gennaio',0.45),
  I('bign',['DA GENNAIO 2027','5,514 %',null,{fs:84,fill:AMB,col:AM_,subcol:AM_,minw:420,tfs:30,padh:60}],1580,430,'cinque virgola cinquecentoquattordici'),
  I('pill',['PRIMO TAGLIO: − 2,01 %',32,RF_,'#fff','down'],650,600,'meno due virgola zero uno'),
  I('pill',['SECONDO TAGLIO: − 1,68 %',32,RF_,'#fff','down'],1270,600,'poi meno uno virgola sessantotto'),
  I('bign',['TOTALE','− 3,65 %',null,{fs:90,fill:RF_,col:'#fff',subcol:'#fff',minw:560,tfs:32}],960,775,'Totale')]},
]);
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DA 57 A 71 ANNI: TUTTE LE RIGHE',cap:'OGNI RIGA DELLA TABELLA È PIÙ BASSA: DA −1,21% A −1,97%',items:[
  P('IL TAGLIO NON RIGUARDA UN\'ETÀ SOLA',960,222,'ha toccato ogni riga',AMB,38,'down'),
  I('agebars',[1560,250],960,425,'dai cinquantasette ai settantuno anni'),
  I('bign',['USCITA A 57 ANNI','− 1,21 %',null,{fs:76,fill:'#2B6F77',col:'#fff',subcol:'#fff',minw:440,tfs:26,padh:60}],400,780,'parte da uno virgola ventuno'),
  I('bign',['USCITA A 71 ANNI','− 1,97 %',null,{fs:76,fill:RF_,col:'#fff',subcol:'#fff',minw:440,tfs:26,padh:60}],1520,780,'arriva a uno virgola novantasette'),
  P('IL PERCHÉ, PIÙ AVANTI',960,745,'spiegano anche il perché',DF_,28,'q'),
  P('PRIMA: IL NUMERO IN EURO',960,830,'il numero in euro',GF_,28,'coin')]},
]);
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ISCRIVITI AL CANALE',cap:'COSTA UN TOCCO E CI AIUTA AD ARRIVARE A MILLE ISCRITTI',items:[
  P('UN ATTIMO, PRIMA DI CONTINUARE',960,215,'Un attimo',AMB,36,'bulb'),
  I('icard',[780,160,'doc',[['I DECRETI LI LEGGIAMO PER TE',34],['AL POSTO TUO',30,GRN]],{lh:46}],480,380,'i decreti li legge al posto tuo'),
  I('btn',['ISCRIVITI'],1440,380,'iscriviti al canale'),
  P('BASTA UN TOCCO',1440,500,'basta un tocco',GF_,34,'ok'),
  I('icard',[780,160,'people',[['VERSO I 1.000 ISCRITTI',34],['CI AIUTI AD ARRIVARCI',30,GRN]],{lh:46}],480,580,'ai mille iscritti'),
  I('goalbar',[640,0.28],480,700,['ai mille iscritti',0.5]),
  I('icard',[780,150,'calc',[['CONTI VERI',34],['SUI TESTI UFFICIALI',30,GRN]],{lh:46}],1440,640,'conti veri sui testi ufficiali'),
  I('bell',[],900,800,'Attiva anche la campanella',0.5),
  I('icard',[800,150,'next',[['QUANDO ESCE IL DECRETO SULL\'AUMENTO:',26],['TABELLA RIFATTA CON LA % VERA',30,GRN]],{lh:44}],1430,810,'quando esce il decreto sull\'aumento')]},
]);
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COME SI USA LA TABELLA',cap:'MONTANTE × COEFFICIENTE = PENSIONE ANNUA: DA 5.608 A 5.514 EURO',items:[
  P('MONTANTE = CONTRIBUTI VERSATI, RIVALUTATI',960,215,'si chiama montante',AMB,36,'coin'),
  ...EQ(340,[['num','MONTANTE','Lo moltiplichi',{fs:38}],['op','×','Lo moltiplichi'],['num','COEFFICIENTE','per il coefficiente della tua età',{fs:38}],['op','=','ottieni'],['num','PENSIONE ANNUA','la pensione annua',{fs:38}]],34,240),
  ...EQ(520,[['num','100.000 €','Oggi',{fs:52,sub:'OGGI'}],['op','×','all\'età di sessantasette'],['num','5,608 %','all\'età di sessantasette',{fs:52,sub:'A 67 ANNI'}],['op','=','ogni centomila euro di montante valgono'],['num','5.608 €','cinquemilaseicentotto',{fs:52,sub:'EURO L\'ANNO'}]],52,240),
  ...EQ(700,[['num','100.000 €','Da gennaio',{fs:52,sub:'DA GENNAIO'}],['op','×','Da gennaio'],['num','5,514 %','Da gennaio',{fs:52,sub:'A 67 ANNI'}],['op','=','cinquemilacinquecentoquattordici'],['num','5.514 €','cinquemilacinquecentoquattordici',{fs:52,sub:'EURO L\'ANNO',fill:AMB}]],52,240),
  P('DIFFERENZA: 94 € L\'ANNO',960,840,'Differenza',RF_,36,'down')]},
]);
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TRE ESEMPI A 67 ANNI',cap:'CIFRE LORDE, TREDICI MENSILITÀ: CONFRONTO CON CHI ESCE QUEST\'ANNO',items:[
  P('STESSA ETÀ: 67 ANNI',960,215,'Tre esempi',AMB,38,'clock'),
  I('trow2',[1500,[['MONTANTE',DK,LT,0.34],['PERDI ALL\'ANNO',DK,LT,0.36],['AL MESE',DK,LT,0.30]],{h:62,fs:26}],960,310,'confrontati con chi esce quest\'anno'),
  I('trow2',[1500,[['150.000 €','#2B6F77','#fff',0.34],['− 141 €','url(#g_red)','#fff',0.36],['≈ 11 €',AMB,AM_,0.30]],{h:96,fs:46}],960,420,'Montante da centocinquantamila euro'),
  I('trow2',[1500,[['250.000 €',GRN,'#fff',0.34],['− 235 €','url(#g_red)','#fff',0.36],['≈ 18 €',AMB,AM_,0.30]],{h:96,fs:46,hl:1}],960,540,'Da duecentocinquantamila'),
  I('trow2',[1500,[['400.000 €','#2B6F77','#fff',0.34],['− 376 €','url(#g_red)','#fff',0.36],['≈ 29 €',AMB,AM_,0.30]],{h:96,fs:46}],960,660,'Da quattrocentomila'),
  P('CIFRE LORDE · 13 MENSILITÀ',520,775,'Cifre lorde, tredici mensilità',DF_,30,'doc'),
  I('icard',[800,140,'chat',[['SCRIVICI NEI COMMENTI',32],['MONTANTE ED ETÀ',34,GRN]],{lh:44}],1380,805,'Scrivici nei commenti'),
  P('TI RISPONDIAMO CON IL CONTO',520,845,'ti rispondiamo con il conto',GF_,30,'ok')]},
]);
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA PERDITA CRESCE CON L\'ETÀ',cap:'SU 100.000 EURO DI MONTANTE: DA 70 A 119 EURO ALL\'ANNO',items:[
  P('MONTANTE DI 100.000 € · PERDITA ALL\'ANNO',860,215,'Con un montante di centomila',AMB,36,'coin'),
  I('vbar',[170,150,'#2B6F77','70 €','62 ANNI'],270,640,'sessantadue anni'),
  I('vbar',[170,175,'#2B6F77','79 €','64 ANNI'],520,640,'settantanove'),
  I('vbar',[170,210,'#E39A1C','94 €','67 ANNI'],770,640,'novantaquattro'),
  I('vbar',[170,265,'#D23A25','119 €','70 ANNI'],1020,640,'centodiciannove'),
  I('icard',[640,150,'up',[['1 · PIÙ TARDI ESCI',34],['PIÙ ALTO È IL COEFFICIENTE',28,GRN]],{lh:44}],1560,330,'più tardi esci, più alto'),
  I('icard',[640,150,'down',[['2 · PIÙ GRANDE',34],['LA PERCENTUALE DI TAGLIO',28,GRN]],{lh:44}],1560,510,'più grande è la percentuale'),
  P('IL MOTIVO È DOPPIO',1560,690,'Il motivo è doppio',DF_,32,'q'),
  I('icard',[1100,110,'ok',[['CHI ESCE PRIMA PERDE MENO,',32],['MA PARTE DA UN ASSEGNO PIÙ BASSO',30,GRN]],{lh:42,ir:42}],960,820,'Chi esce prima perde meno')]},
]);
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DOVE TROVI IL TUO MONTANTE',cap:'L\'ESTRATTO CONTO SI APRE SU MY INPS, NEL FASCICOLO PREVIDENZIALE',items:[
  P('IL TUO MONTANTE: DOVE LO TROVI?',960,215,'Il tuo montante, dove lo trovi',AMB,38,'q'),
  I('br',['inps.it · My Inps',860,380],520,450,'L\'estratto conto lo apri su'),
  OV(I('row',['ESTRATTO CONTO',760,true],520,440,'L\'estratto conto lo apri su')),
  OV(I('row',['FASCICOLO PREVIDENZIALE',760,true],520,540,'nel fascicolo previdenziale')),
  I('icard',[800,130,'doc',[['OGNI ANNO L\'INPS DEVE MANDARTI',30],['L\'ESTRATTO CONTO DEL MONTANTE',32,GRN]],{lh:42}],520,740,'La legge dice che ogni anno'),
  P('ACCESSO CON SPID',1400,300,'con Spid',DF_,34,'lock'),
  P('CARTA D\'IDENTITÀ ELETTRONICA',1400,395,'carta d\'identità elettronica',DF_,34,'lock'),
  P('CARTA NAZIONALE DEI SERVIZI',1400,490,'carta nazionale dei servizi',DF_,34,'lock'),
  P('SE NON C\'È: SEDE INPS O PATRONATO',1400,630,'Se non c\'è',AMB,32,'stato',{icol:AM_}),
  P('SENZA QUEL NUMERO, OGNI CONTO È UNA STIMA',1180,852,'Senza quel numero',RF_,34,'warn')]},
]);
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CHI RIENTRA NEI NUOVI COEFFICIENTI',cap:'SOLO LA PARTE DI PENSIONE CALCOLATA CON IL SISTEMA CONTRIBUTIVO',items:[
  P('CHI RIENTRA?',960,215,'Chi rientra',AMB,40,'q'),
  I('icard',[1500,120,'calc',[['SOLO LE PENSIONI, O LE QUOTE, CALCOLATE CON IL CONTRIBUTIVO',32]],{lh:44,ir:48}],960,340,'riguardano solo le pensioni'),
  I('bign',['HA INIZIATO A VERSARE DA','GENNAIO 1996','RIENTRA PER INTERO',{fs:68,fill:GF_,col:'#fff',subcol:'#fff',minw:640,tfs:28,sfs:30}],480,610,'Rientra per intero chi ha iniziato'),
  P('VERSAVA GIÀ PRIMA: QUOTA CONTRIBUTIVA',1370,470,'Chi versava già prima',DF_,28,'cal'),
  I('trow2',[880,[['ALMENO 18 ANNI A FINE 1995',DK,'#fff',0.58,28],['PERIODI DAL 2012',AMB,AM_,0.42,32]],{h:84,fs:30}],1370,580,'se a fine novantacinque aveva almeno diciotto anni'),
  I('trow2',[880,[['ALTRI CASI',DK,'#fff',0.58,28],['PERIODI DAL 1996','#2B6F77','#fff',0.42,32]],{h:84,fs:30}],1370,690,'dal novantasei, negli altri casi')]},
]);
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DENTRO E FUORI DAL TAGLIO',cap:'IL COEFFICIENTE DIPENDE DALL\'ETÀ NEL MOMENTO IN CUI PARTE LA PENSIONE',items:[
  I('stamp',[['RIENTRA'],GRN,60,-3],490,262,'Rientra anche'),
  I('icard',[760,130,'ok',[['OPZIONE DONNA',38]],{lh:44,ir:48,ibg:'#D6F5EC'}],490,425,'chi sceglie l\'opzione donna'),
  I('icard',[760,150,'ok',[['PENSIONE IN CUMULO',34],['CALCOLATA COL CONTRIBUTIVO',28,GRN]],{lh:44,ir:48,ibg:'#D6F5EC'}],490,575,'una pensione in cumulo'),
  I('stamp',[['RESTA FUORI'],RED_,60,3],1430,262,'Resta fuori'),
  I('icard',[760,130,'x',[['LA PARTE RETRIBUTIVA',36],['DA QUESTO DECRETO NON CAMBIA',26,GRN]],{lh:44,ir:48,ibg:'#FFE3DE',icol:RED_}],1430,425,'Resta fuori la parte calcolata'),
  I('icard',[760,150,'x',[['CHI È GIÀ PENSIONATO',36]],{lh:44,ir:48,ibg:'#FFE3DE',icol:RED_}],1430,575,'Fuori anche chi è già pensionato'),
  I('icard',[1500,110,'clock',[['IL COEFFICIENTE DIPENDE DALL\'ETÀ QUANDO PARTE LA PENSIONE',30]],{lh:44,ir:46}],960,725,'il coefficiente dipende dall\'età'),
  P('PER CHI È GIÀ IN PENSIONE, QUEL MOMENTO È PASSATO',960,835,'quel momento è passato',AMB,34,'cal',{icol:AM_})]},
]);
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO PROMESSO: I MESI DI ATTESA',cap:'PER TORNARE AL COEFFICIENTE DI QUEST\'ANNO: CIRCA SEI MESI',items:[
  P('ED ECCO IL CONTO PROMESSO',960,215,'Ed ecco il conto promesso',AMB,38,'bulb'),
  I('icard',[1500,120,'up',[['OGNI MESE IN PIÙ: IL COEFFICIENTE CRESCE DI UN DODICESIMO',30],['DELLA DIFFERENZA CON QUELLO DELL\'ETÀ SUCCESSIVA',28,GRN]],{lh:42,ir:48}],960,350,'Per ogni mese in più'),
  P('RIFATTO PER OGNI ETÀ, 57–70 ANNI',520,470,'Lo abbiamo rifatto',DF_,32,'calc'),
  OV(I('maxis',[1500,14],960,740,'servono circa')),
  OV(I('flag',['≈ 6 MESI · TABELLA 2025-26',GF_,110],842,740,'circa sei mesi')),
  OV(I('flag',['POCO PIÙ DI 1 ANNO · TABELLA 2023-24',AMB,220,AM_,-170],1538,740,'poco più di un anno')),
  P('I CONTRIBUTI RESTANO QUELLI DI PRIMA',960,848,'I contributi, in questo conto',RF_,30,'lock')]},
]);
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ATTENZIONE: NON È UN CONSIGLIO',cap:'DAL 2027 LA VECCHIAIA ARRIVA A 67 ANNI E 1 MESE: COEFFICIENTE −1,39%',items:[
  P('ATTENZIONE, NON È UN CONSIGLIO',960,215,'Attenzione, non è un consiglio',RF_,38,'warn'),
  I('icard',[760,130,'clock',[['RIMANDARE = ANCHE',32],['MESI DI ASSEGNO IN MENO',34,GRN]],{lh:44,ir:48}],480,350,'rimandare vuol dire'),
  I('icard',[760,130,'calc',[['IL CONTO COMPLETO',32],['VA FATTO SUL TUO CASO',34,GRN]],{lh:44,ir:48}],1440,350,'il conto completo va fatto'),
  I('bign',['VECCHIAIA DAL 2027','67 ANNI + 1 MESE',null,{fs:44,minw:500,tfs:26,padh:50}],370,590,'dal duemilaventisette, per la vecchiaia'),
  I('bign',['COEFFICIENTE CON QUEL MESE','≈ 5,530 %',null,{fs:60,fill:AMB,col:AM_,subcol:AM_,minw:440,tfs:24,padh:50}],990,590,'circa cinque virgola cinquecentotrenta'),
  I('bign',['OGGI, A 67 ANNI','5,608 %',null,{fs:60,minw:400,tfs:24,padh:50}],1600,590,'il valore di oggi per quell\'età'),
  I('bign',['PERDITA','− 1,39 %',null,{fs:84,fill:RF_,col:'#fff',subcol:'#fff',minw:520,tfs:30}],960,790,'una perdita dell\'uno virgola trentanove')]},
]);
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL PERCHÉ DEL TAGLIO',cap:'IL TASSO DI SCONTO È LO STESSO: CAMBIANO I DATI DEMOGRAFICI',items:[
  P('IL PERCHÉ',960,215,'Il perché',AMB,40,'q'),
  I('icard',[760,140,'coin',[['TASSO DI SCONTO: 1,5 %',36],['RESTA QUELLO DI PRIMA',28,GRN]],{lh:44,ir:50}],480,350,'il tasso di sconto, uno virgola cinque'),
  I('icard',[760,140,'people',[['CAMBIANO I DATI DELL\'ISTAT',34],['PROBABILITÀ DI MORTE',28,GRN]],{lh:44,ir:50}],1440,350,'Cambiano i dati demografici'),
  ...EQ(530,[['num','COEFFICIENTE','dividendo uno',{fs:44}],['op','=','dividendo uno'],['num','1','dividendo uno',{fs:60}],['op','÷','per un divisore'],['num','DIVISORE','per un divisore',{fs:44}]],44,260),
  I('bign',['DIVISORE A 67 ANNI · PRIMA','17,831',null,{fs:92,minw:560,tfs:26}],520,705,'sale da diciassette virgola ottocentotrentuno'),
  I('arR',[],960,705,'a diciotto virgola centotrentasei',0.7),
  I('bign',['DA GENNAIO','18,136',null,{fs:92,fill:AMB,col:AM_,subcol:AM_,minw:560,tfs:26}],1400,705,'a diciotto virgola centotrentasei'),
  P('COME SE LA PENSIONE DURASSE DI PIÙ',960,848,'Come se la pensione durasse di più',DF_,34,'clock')]},
]);
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RIEPILOGO IN TRE PUNTI',cap:'',items:[
  I('dbox',[1300,150,[["CANALE INFORMATIVO, NON CONSULENZA, NON AFFILIATO ALL'INPS",26,AMB],['VERIFICA SU INPS.IT O CON UN PATRONATO',28,'#fff']]],960,255,'Canale informativo'),
  I('circ',['1'],250,400,'Uno',0.72),
  I('icard',[1250,100,'down',[['DA GENNAIO LA TABELLA È PIÙ BASSA A OGNI ETÀ',32]],{lh:40,ir:42}],1060,400,'da gennaio la tabella è più bassa'),
  I('circ',['2'],250,520,'Due',0.72),
  I('icard',[1250,100,'calc',[['LA PERDITA DIPENDE DAL TUO MONTANTE E DALL\'ETÀ',32]],{lh:40,ir:42}],1060,520,'la perdita in euro dipende'),
  I('circ',['3'],250,640,'Tre',0.72),
  I('icard',[1250,100,'stato',[['RIGUARDA LA PARTE CONTRIBUTIVA DAL 2027',32]],{lh:40,ir:42}],1060,640,'riguarda la parte contributiva')]},
]);
