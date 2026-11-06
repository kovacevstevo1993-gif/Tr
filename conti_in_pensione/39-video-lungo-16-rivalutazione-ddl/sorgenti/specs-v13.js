// ===== VIDEO 13 (pensione di reversibilita') - elementi nuovi + 22 blocchi =====
// Un po' diverso dai video 8-12 (N.37, N.47), stessi colori: titoletto con i QUATTRO PASSAGGI del video (chi / quanto / riduzione / domanda),
// didascalia a pannello con barra gialla e "i", sfondo con linee di soglia e scalinata che sale; pittogrammi di famiglia, anelli di percentuale,
// scala del reddito con le tre soglie, grafico del gradino, schermata del sito, schede a due colonne.
const NB13=22;
const PASSI13=['CHI','QUANTO','RIDUZIONE','DOMANDA'];
function passo13(n){if(n<=2)return -1;if(n<=6)return 0;if(n<=9)return 1;if(n<=16)return 2;if(n<=18)return 3;if(n==19)return 2;return 4;}
function topLabel(g,s){const t=el('g',{transform:'translate(-840 0)'},g);
 const b=el('g',{},t);
 el('rect',{x:-56,y:-42,width:112,height:84,rx:22,fill:'#06303A',stroke:'#7FF0D2','stroke-width':3,filter:'url(#g_sh3)'},b);
 txt(b,(N<10?'0':'')+N,0,15,42,AMB,'900');
 const x=txt(t,s,86,12,36,'#7FF0D2','bold','start');x.setAttribute('letter-spacing','6');
 let w=tw(s,36)+s.length*6;try{w=x.getBBox().width;}catch(e){}
 el('rect',{x:86,y:30,width:Math.min(w,150),height:5,rx:2.5,fill:AMB},t);
 // stepper dei quattro passaggi (a destra)
 const a=passo13(N);const CW=196,CG=8,X0=1730-(4*CW+3*CG);
 PASSI13.forEach((p,i)=>{const on=(i===a),done=(i<a)||a===4;const cx=X0+i*(CW+CG);
  el('rect',{x:cx,y:-23,width:CW,height:46,rx:23,fill:on?AMB:(done?'#1B9F81':'#06303A'),stroke:on?'#fff':'#7FF0D2','stroke-width':on?3:2,opacity:on?1:(done?0.95:0.5)},t);
  txt(t,(i+1)+' '+p,cx+CW/2,8,21,on?'#5A3300':'#fff','900');});
 return t;}
function cap(g,s,size){size=size||44;const c=el('g',{},g);if(!s)return c;
 const t=txt(c,s,0,0,size,'#FFFFFF','bold');let tl=mw(t,s,size);
 const maxT=1540;if(tl>maxT){size=size*maxT/tl;t.setAttribute('font-size',size.toFixed(1));tl=mw(t,s,size);}
 const padL=130,padR=60;const w=tl+padL+padR;
 t.setAttribute('x',(-w/2+padL+tl/2).toFixed(1));t.setAttribute('y',(size*0.36).toFixed(1));
 const ins=e=>{c.insertBefore(e,t);return e;};
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:20,fill:'#06303A',filter:'url(#g_sh2)'}));
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:20,fill:'none',stroke:'#7FF0D2','stroke-width':2.5,opacity:.4}));
 ins(el('rect',{x:-w/2,y:-56,width:98,height:112,rx:20,fill:AMB}));
 ins(el('rect',{x:-w/2+60,y:-56,width:38,height:112,fill:'#06303A'}));
 ins(el('rect',{x:-w/2+90,y:-56,width:8,height:112,fill:AMB}));
 const ib=el('g',{transform:'translate('+(-w/2+46)+' 0)'},c);el('circle',{r:30,fill:'#06303A'},ib);
 el('rect',{x:-4.5,y:-4,width:9,height:22,rx:4,fill:AMB},ib);el('circle',{cx:0,cy:-14,r:5.5,fill:AMB},ib);
 return c;}
// ---------- pittogramma di famiglia ----------
function famB(g,kind,r,fill,label,o){o=o||{};
 const c=el('g',{filter:'url(#g_sh2)'},g);
 el('circle',{r:r,fill:fill||'url(#g_badge)',stroke:'#fff','stroke-width':Math.max(5,r*0.07)},c);
 const s=r/100;const W='#fff';
 const man=(x,y,k,col,hair)=>{const m=el('g',{transform:'translate('+(x*s)+' '+(y*s)+') scale('+(k*s)+')'},c);
  el('circle',{cx:0,cy:-30,r:17,fill:col||W},m);
  el('path',{d:'M-30 34 Q-30 -4 0 -4 Q30 -4 30 34 Z',fill:col||W},m);
  if(hair)el('path',{d:'M-17 -34 Q0 -58 17 -34',fill:'none',stroke:hair,'stroke-width':6,'stroke-linecap':'round'},m);return m;};
 if(kind=='spouse'){man(-24,8,0.9);man(24,8,0.9);el('circle',{cx:0*s,cy:44*s,r:9*s,fill:'none',stroke:AMB,'stroke-width':5*s},c);}
 else if(kind=='unit'){man(-26,8,0.88);man(26,8,0.88);el('path',{d:'M0 52 C-22 36 -12 22 0 32 C12 22 22 36 0 52 Z',fill:AMB,transform:'translate(0 '+(-2*s)+') scale('+s+')'},c);}
 else if(kind=='sep'){man(-34,8,0.9);man(34,8,0.9);el('line',{x1:0,y1:-34*s,x2:0,y2:52*s,stroke:AMB,'stroke-width':6*s,'stroke-dasharray':(8*s)+' '+(8*s),'stroke-linecap':'round'},c);}
 else if(kind=='div'){man(-34,8,0.9);man(34,8,0.9);el('path',{d:'M-14 40 L14 -2',stroke:'#FF8E7A','stroke-width':8*s,'stroke-linecap':'round',transform:'scale('+s+')'},c);}
 else if(kind=='child'){man(0,18,0.62);}
 else if(kind=='stud'){man(0,14,0.82);el('path',{d:'M-34 -50 L0 -66 L34 -50 L0 -34 Z',fill:AMB,stroke:'#5A3300','stroke-width':2,transform:'translate(0 '+(-2*s)+') scale('+s+')'},c);el('line',{x1:30*s,y1:-52*s,x2:30*s,y2:-26*s,stroke:AMB,'stroke-width':4*s},c);}
 else if(kind=='inab'){man(0,6,0.85);el('circle',{cx:44*s,cy:36*s,r:17*s,fill:AMB},c);el('path',{d:'M44 28 V44 M36 36 H52',stroke:'#5A3300','stroke-width':5,'stroke-linecap':'round',transform:'translate('+(44*s)+' '+(36*s)+') scale('+s+') translate(-44 -36)'},c);}
 else if(kind=='par'){man(-26,8,0.9,W,'#7A9AA0');man(26,8,0.9,W,'#7A9AA0');}
 else if(kind=='sib'){man(-26,12,0.82);man(26,2,0.98);}
 else if(kind=='one'){man(0,8,1);}
 if(label){const lg=el('g',{transform:'translate(0 '+(r+40)+')'},g);pillB(lg,label,o.fs||30,o.lfill||'#06303A','#fff',null,{minw:o.minw});}
 return g;}
// ---------- anello di percentuale ----------
function pctB(g,r,frac,main,label,fill,o){o=o||{};const sw=r*0.26;
 el('circle',{r:r,fill:'#06303A',filter:'url(#g_sh)'},g);
 el('circle',{r:r,fill:'none',stroke:'#0F5560','stroke-width':sw},g);
 const a=Math.min(0.9999,frac)*Math.PI*2;
 el('path',{d:`M0 ${-r} A${r} ${r} 0 ${frac>.5?1:0} 1 ${r*Math.sin(a)} ${-r*Math.cos(a)}`,fill:'none',stroke:fill||'#2FD0A8','stroke-width':sw,'stroke-linecap':'butt'},g);
 el('circle',{r:r+sw/2,fill:'none',stroke:'#fff','stroke-width':3,opacity:.5},g);
 fitT(g,main,0,0,o.fs||r*0.58,'#fff','900',r*1.5);
 if(label){const lg=el('g',{transform:'translate(0 '+(r+sw/2+46)+')'},g);pillB(lg,label,o.lfs||28,o.lfill||'#0B4A50','#fff');}
 return g;}
// ---------- grafico del gradino: scalino (rosso, tratteggiato, sbarrato) contro rampa vera (verde) ----------
function stepchartB(g,W,H){const x0=-W/2,y0=H/2;
 el('rect',{x:x0-20,y:-H/2-20,width:W+40,height:H+40,rx:26,fill:'#06303A',filter:'url(#g_sh)'},g);
 el('line',{x1:x0,y1:y0,x2:x0+W,y2:y0,stroke:'#7FF0D2','stroke-width':4},g);el('line',{x1:x0,y1:-H/2,x2:x0,y2:y0,stroke:'#7FF0D2','stroke-width':4},g);
 const tx=x0+W*0.34;
 el('line',{x1:tx,y1:-H/2+10,x2:tx,y2:y0,stroke:AMB,'stroke-width':3,'stroke-dasharray':'8 8'},g);
 txt(g,'SOGLIA',tx,y0+44,26,AMB,'900');
 // scalino che NON c'e'
 el('path',{d:`M${x0} ${-H/2+70} H${tx} V${-H/2+70+H*0.5} H${x0+W}`,fill:'none',stroke:'#FF8E7A','stroke-width':7,'stroke-dasharray':'14 10','stroke-linejoin':'round'},g);
 // rampa vera
 el('path',{d:`M${x0} ${-H/2+70} H${tx} L${tx+W*0.07} ${-H/2+70+H*0.07} L${x0+W} ${-H/2+70+H*0.07+10}`,fill:'none',stroke:'#2FD0A8','stroke-width':11,'stroke-linecap':'round','stroke-linejoin':'round'},g);
 txt(g,'COSÌ NON È',x0+W*0.62,-H/2+70+H*0.5-18,28,'#FF8E7A','900');
 txt(g,'COSÌ È DAVVERO',x0+W*0.64,-H/2+70-30,28,'#2FD0A8','900');
 txt(g,'REDDITO →',x0+W-10,y0+44,24,'#7FF0D2','bold','end');txt(g,'RIDUZIONE ↓',x0+8,-H/2-0,22,'#7FF0D2','bold','start');
 return g;}
Object.assign(BUILD,{
 ladder:(g,h)=>{h=h||90;[[-700,-180,'0 %','url(#g_badge)'],[-170,120,'− 25 %','#E39A1C'],[130,420,'− 40 %','#D9692B'],[430,700,'− 50 %','url(#g_red)']].forEach(([a,b,l,f])=>{
   const w=b-a;el('rect',{x:a,y:-h/2,width:w,height:h,rx:20,fill:f,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);fitT(g,l,(a+b)/2,0,44,'#fff','900',w-30);});},
 fam:(g,kind,r,fill,label,o)=>famB(g,kind,r,fill,label,o),
 pct:(g,r,frac,main,label,fill,o)=>pctB(g,r,frac,main,label,fill,o),
 stepc:(g,W,H)=>stepchartB(g,W,H),
 okx:(g,ok,r)=>{r=r||44;el('circle',{r:r,fill:ok?'url(#g_badge)':'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh3)'},g);
  el('path',{d:ok?`M${-r*.42} ${r*.02} L${-r*.1} ${r*.34} L${r*.46} ${-r*.3}`:`M${-r*.34} ${-r*.34} L${r*.34} ${r*.34} M${r*.34} ${-r*.34} L${-r*.34} ${r*.34}`,fill:'none',stroke:'#fff','stroke-width':r*.2,'stroke-linecap':'round','stroke-linejoin':'round'},g);},
});
const IC=(w,h,icon,lines,x,y,at,o)=>I('icard',[w,h,icon,lines,Object.assign({lh:44},o||{})],x,y,at);
const BN=(top,val,sub,o,x,y,at)=>I('bign',[top,val,sub,o],x,y,at);
const GRNB={fill:GF_,col:'#fff',subcol:'#fff'},REDB={fill:RF_,col:'#fff',subcol:'#fff'},AMBB={fill:AMB,col:'#5A3300',subcol:'#5A3300'};
const DKB={fill:'#06303A',col:'#fff',subcol:'#7FF0D2'};
// scala del reddito: quattro segmenti con le tre soglie (x da 260 a 1660)
const SEGX=[[260,780,'0 %','NESSUNA RIDUZIONE',GF_],[790,1080,'− 25 %',null,'#E39A1C'],[1090,1380,'− 40 %',null,'#D9692B'],[1390,1660,'− 50 %',null,RF_]];
function ladder(y,at,h){h=h||96;return SEGX.map((s,i)=>I('seg',[s[1]-s[0],h,s[4],s[2],null],(s[0]+s[1])/2,y,at[i]));}
function thr(y,at,fs){return [[780,'23.862,15 €'],[1080,'31.816,20 €'],[1380,'39.770,25 €']].map((s,i)=>P(s[1],s[0],y,at[i],DK,fs||28));}
// ======================= BLOCCHI =======================
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONE DI REVERSIBILITÀ',cap:'QUANTO TI RESTA DAVVERO QUANDO IL CONIUGE VIENE A MANCARE?',items:[
  I('fam',['spouse',92,null,'IL TUO CONIUGE'],250,330,'il tuo coniuge'),
  BN('PENSIONE LORDA AL MESE','2.000 €',null,Object.assign({fs:104,minw:420},DKB),700,325,'duemila euro lordi'),
  I('arR',[],1075,330,'viene a mancare'),
  BN('LA TUA REVERSIBILITÀ','? €',null,Object.assign({fs:104,minw:420},GRNB),1420,325,'Quanto ti resta davvero'),
  I('q',[70],1810,330,'Quanto ti resta davvero'),
  BN('IN CERTI CASI IL TAGLIO ARRIVA A','− 7.800 €','ALL\'ANNO',Object.assign({fs:112,minw:560,tfs:30,sfs:30},REDB),560,640,'fino a settemilaottocento'),
  P('QUANDO SUCCEDE?',1300,590,'Quando succede',AMB,38,'q'),
  P('UN MECCANISMO CHE CAMBIA I CONTI',1360,720,'un meccanismo che cambia i conti',DF_,32,'lock')]},
]);
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COME È ORGANIZZATO IL VIDEO',cap:'QUATTRO PASSAGGI, DALLE SCHEDE E DALLE CIRCOLARI DELL\'INPS',items:[
  P('DOPO UN LUTTO I SOLDI SONO L\'ULTIMO PENSIERO',960,225,'Facciamo ordine',DF_,34,'cal'),
  P('MA LE PRATICHE ARRIVANO LO STESSO',960,300,'ma le pratiche arrivano lo stesso',AMB,34,'doc'),
  IC(420,200,'people',[['1 · CHI',40],['HA DIRITTO',32,GRN]],270,465,'chi ha diritto'),
  IC(420,200,'coin',[['2 · QUANTO',40],['SPETTA',32,GRN]],720,465,'quanto spetta'),
  IC(420,200,'cut',[['3 · QUANDO',40],['SCATTA IL TAGLIO',30,GRN]],1170,465,'quando scatta la riduzione'),
  IC(420,200,'web',[['4 · LA DOMANDA',36],['COME SI FA',32,GRN]],1620,465,'come si presenta la domanda'),
  IC(640,150,'doc',[['SCHEDE E CIRCOLARI',34],['DELL\'INPS',30,GRN]],480,690,'schede e delle circolari'),
  P('LIMITI DI REDDITO: 2026',1160,690,'con i limiti del duemilaventisei',AMB,34,'cal'),
  P('QUELLI DEL 2027 CAMBIANO A GENNAIO',1400,800,'Quelli del duemilaventisette',DF_,30,'calback')]},
]);
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE DUE PENSIONI AI SUPERSTITI',cap:'REVERSIBILITÀ SE MUORE UN PENSIONATO, INDIRETTA SE MUORE UN ASSICURATO',items:[
  I('card',['REVERSIBILITÀ',720,420,{hc:GRN,lines:[['MUORE CHI ERA GIÀ',36,-8,INK],['PENSIONATO',36,36,INK],['È UNA QUOTA',32,110,GRN],['DELLA SUA PENSIONE',32,154,GRN]]}],480,450,'La reversibilità spetta ai familiari'),
  I('card',['PENSIONE INDIRETTA',720,420,{hc:'#2B6F8F',lines:[['MUORE UN ASSICURATO',36,-8,INK],['NON ANCORA PENSIONATO',34,36,INK],['E AVEVA ALMENO:',30,110,GRN]]}],1440,450,'La pensione indiretta spetta'),
  P('15 ANNI DI CONTRIBUTI',1440,715,'quindici anni di contributi',AMB,32,'ok'),
  P('OPPURE 5 ANNI, DI CUI 3 NEGLI ULTIMI 5',1440,785,'oppure cinque anni',DF_,28,'clock'),
  P('LE REGOLE CHE SEGUONO VALGONO PER ENTRAMBE',960,850,'Le regole che seguono',DK,32,'ok',{icol:GRN})]},
]);
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CHI HA DIRITTO: IL CONIUGE',cap:'CONIUGE, UNITO CIVILMENTE, SEPARATO E DIVORZIATO A TRE CONDIZIONI',items:[
  I('fam',['spouse',92,null,'CONIUGE'],290,320,'il coniuge'),
  I('fam',['unit',92,null,'UNITO CIVILMENTE'],740,320,'chi è unito civilmente'),
  I('fam',['sep',92,null,'SEPARATO'],1190,320,'il coniuge separato'),
  I('fam',['div',92,'url(#g_red)','DIVORZIATO'],1640,320,'Il coniuge divorziato'),
  IC(500,160,'doc',[['1 · ASSEGNO',32],['DI DIVORZIO',32,GRN]],290,640,'deve ricevere l\'assegno di divorzio'),
  IC(500,160,'x',[['2 · NON',32],['RISPOSATO',32,GRN]],900,640,'non deve essersi risposato'),
  IC(620,160,'cal',[['3 · RAPPORTO ASSICURATIVO',26],['PRIMA DELLA SENTENZA',28,GRN]],1560,640,'il rapporto assicurativo'),
  P('LE QUOTE TRA CONIUGE ED EX CONIUGE: PIÙ AVANTI',960,820,'Le quote tra coniuge',DK,30,'next')]},
]);
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CHI HA DIRITTO: I FIGLI',cap:'MINORENNI, INABILI A CARICO E STUDENTI FINO A 21 O 26 ANNI',items:[
  I('fam',['child',96,null,'MINORENNI'],330,330,'i figli minorenni'),
  I('fam',['inab',96,null,'INABILI AL LAVORO','A CARICO',{minw:300}],960,330,'i figli inabili al lavoro'),
  I('fam',['stud',96,null,'STUDENTI MAGGIORENNI'],1590,330,'i maggiorenni a carico che studiano'),
  P('A CARICO AL MOMENTO DEL DECESSO',960,545,'a carico al momento del decesso',DK,28,'ok',{icol:GRN}),
  P('A QUALSIASI ETÀ',960,615,'a qualsiasi età',AMB,30,'clock'),
  IC(800,170,'book',[['SCUOLE E CORSI PROFESSIONALI',30],['FINO A 21 ANNI',46,GRN]],480,750,'fino a ventuno anni'),
  IC(800,170,'land',[['UNIVERSITÀ, NEI LIMITI DELLA DURATA LEGALE',26],['FINO A 26 ANNI',46,GRN]],1440,750,'fino a ventisei')]},
]);
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'GENITORI, FRATELLI, SORELLE',cap:'SOLO SE MANCANO CONIUGE E FIGLI E SE ERANO A CARICO DEL DEFUNTO',items:[
  P('SE MANCANO CONIUGE E FIGLI, O NON HANNO DIRITTO',960,230,'entrano in gioco',AMB,34,'next'),
  I('fam',['par',92,null,'GENITORI'],430,400,'Genitori, fratelli e sorelle'),
  I('fam',['sib',92,null,'FRATELLI E SORELLE'],1490,400,'fratelli e sorelle'),
  IC(560,130,'people',[['A CARICO DEL DEFUNTO',30]],960,370,'a carico del defunto'),
  IC(560,130,'x',[['NESSUNA PENSIONE PROPRIA',28]],960,520,'una pensione propria'),
  IC(640,150,'cake',[['GENITORI: ALMENO',30],['65 ANNI',44,GRN]],450,700,'I genitori devono'),
  IC(660,150,'ok',[['FRATELLI E SORELLE:',30],['CELIBI O NUBILI E INABILI',30,GRN]],1470,700,'Fratelli e sorelle devono'),
  P('LA PERCENTUALE PARTE DAL 15 %',960,850,'Per loro la percentuale',DF_,34,'up')]},
]);
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO SPETTA: PERCENTUALI',cap:'LA REVERSIBILITÀ È UNA PERCENTUALE DELLA PENSIONE DEL DEFUNTO',items:[
  P('UNA PERCENTUALE DELLA PENSIONE DEL DEFUNTO',960,225,'La reversibilità è una percentuale',AMB,34,'coin'),
  I('pct',[118,0.6,'60 %','CONIUGE DA SOLO','#2FD0A8'],400,400,'Il coniuge da solo'),
  I('pct',[118,0.8,'80 %','CONIUGE + 1 FIGLIO','#E39A1C',{lfs:26}],960,400,'Con un figlio'),
  I('pct',[118,1,'100 %','CONIUGE + 2 O PIÙ FIGLI','#D9692B',{lfs:24}],1520,400,'Con almeno due figli'),
  P('SE HANNO DIRITTO SOLTANTO I FIGLI',960,650,'Se hanno diritto soltanto i figli',DK,30,'people'),
  IC(480,140,'people',[['UN FIGLIO',30],['70 %',50,GRN]],300,770,'il settanta per cento'),
  IC(480,140,'people',[['DUE FIGLI',30],['80 %',50,GRN]],960,770,'l\'ottanta se sono due'),
  IC(480,140,'people',[['TRE O PIÙ',30],['100 %',50,GRN]],1620,770,'il cento se sono tre')]},
]);
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO CON DUEMILA EURO',cap:'MILLEDUECENTO AL MESE: QUINDICIMILASEICENTO EURO ALL\'ANNO',items:[
  BN('PENSIONE LORDA DEL DEFUNTO','2.000 €',null,Object.assign({fs:80,minw:280,tfs:22},DKB),400,300,'pensione lorda di duemila euro'),
  I('op',['×'],735,300,'spettano milleduecento'),
  BN('CONIUGE DA SOLO','60 %',null,Object.assign({fs:80,minw:260,tfs:22},AMBB),1020,300,'al coniuge senza altri aventi diritto'),
  I('op',['='],1285,300,'spettano milleduecento'),
  BN('REVERSIBILITÀ AL MESE','1.200 €',null,Object.assign({fs:80,minw:280,tfs:22},GRNB),1600,300,'spettano milleduecento'),
  IC(560,130,'people',[['CONIUGE + 1 FIGLIO',28],['1.600 € IN TUTTO',40,GRN]],360,520,'Se c\'è anche un figlio'),
  IC(560,130,'people',[['CONIUGE + 2 O PIÙ FIGLI',26],['2.000 € IN TUTTO',40,GRN]],1000,520,'Se i figli sono due o più'),
  P('LORDI, 13 MENSILITÀ',1600,520,'Sono importi lordi',DK,28,'cal'),
  BN('1.200 € × 13 MENSILITÀ','15.600 €','ALL\'ANNO',Object.assign({fs:96,minw:620,tfs:30,sfs:30},AMBB),560,740,'fanno quindicimilaseicento'),
  P('IL TAGLIO PARTE DA QUESTA CIFRA',1330,740,'Il taglio parte da questa cifra',RF_,32,'cut')]},
]);
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'UNA PAUSA BREVE',cap:'SE TI STA SERVENDO: ISCRIVITI E ATTIVA LA CAMPANELLA',items:[
  P('SIAMO ANCORA UN CANALE PICCOLO',960,230,'Siamo ancora un canale piccolo',DK,34,'people'),
  I('btn',['ISCRIVITI'],440,430,'iscriviti'),
  I('bell',[],900,430,'Attiva anche la campanella'),
  I('goalbar',[700,0.26],1500,420,'ci avvicini ai mille iscritti'),
  P('VERSO 1.000 ISCRITTI',1500,500,'ci avvicini ai mille iscritti',AMB,30,'up'),
  IC(700,150,'book',[['ORE DI LETTURA',34],['CIRCOLARI E SENTENZE',28,GRN]],420,680,'Leggere circolari e sentenze richiede ore'),
  IC(760,150,'cal',[['A NOVEMBRE: DECRETO',32],['SULL\'AUMENTO DI GENNAIO',28,GRN]],1410,680,'a novembre arriva il decreto'),
  P('DA QUEL DECRETO DIPENDONO LE SOGLIE',960,830,'da quello dipendono le soglie',DF_,32,'next')]},
]);
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA RIDUZIONE: CHI RIGUARDA',cap:'DIPENDE DAL REDDITO DI CHI RICEVE LA PENSIONE, NON DA QUELLO DEL DEFUNTO',items:[
  P('IL PUNTO CHE PREOCCUPA DI PIÙ: IL TAGLIO',960,230,'Adesso il punto che preoccupa',RF_,34,'cut'),
  I('fam',['one',76,null,'CONIUGE'],300,400,'Riguarda il coniuge'),
  I('fam',['par',76,null,'GENITORI'],640,400,'i genitori'),
  I('fam',['sib',76,null,'FRATELLI E SORELLE'],1000,400,'i fratelli e le sorelle'),
  I('fam',['child',76,'url(#g_red)','I FIGLI NO'],1500,400,'ma non i figli'),
  IC(1060,130,'people',[['CONTA IL REDDITO DI CHI RICEVE LA PENSIONE,',28],['NON QUELLO DEL DEFUNTO',34,GRN]],590,690,'Conta il reddito di chi riceve'),
  IC(640,130,'ruler',[['3 · 4 · 5 VOLTE IL MINIMO',30],['13 MENSILITÀ',34,GRN]],1500,690,'tre, quattro e cinque volte'),
  P('PRIMA IL REDDITO CHE CONTA, POI LE CIFRE',960,830,'Prima il reddito che conta',AMB,32,'next')]},
]);
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUALE REDDITO CONTA',cap:'REDDITO SOGGETTO A IRPEF, AL NETTO DEI CONTRIBUTI (CIRCOLARE 185/2015)',items:[
  P('CONTA',480,235,'Quale reddito conta',GF_,40,'ok'),
  P('NON CONTA',1440,235,'Restano fuori',RF_,40,'x'),
  IC(800,140,'doc',[['REDDITO SOGGETTO A IRPEF',32]],480,380,'quello soggetto a Irpef'),
  IC(800,170,'calc',[['AL NETTO DEI CONTRIBUTI',32],['PREVIDENZIALI E ASSISTENZIALI',26,GRN]],480,570,'al netto dei contributi'),
  IC(800,120,'brief',[['TRATTAMENTO DI FINE RAPPORTO',30]],1440,340,'il trattamento di fine rapporto'),
  IC(800,120,'house',[['REDDITO DELLA CASA DI ABITAZIONE',30]],1440,480,'il reddito della casa di abitazione'),
  IC(800,120,'env',[['ARRETRATI TASSATI A PARTE',30]],1440,620,'le somme arretrate tassate a parte'),
  IC(800,120,'coin',[['LA REVERSIBILITÀ STESSA',30]],1440,760,'Non conta nemmeno la reversibilità'),
  P('CIRCOLARE INPS 185 DEL 2015',480,790,'La regola è nella circolare',DK,30,'doc')]},
]);
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE SOGLIE DEL 2026',cap:'FINO A 23.862,15 € NESSUNA RIDUZIONE; POI −25 %, −40 %, −50 %',items:[
  P('IL TRIPLO',780,300,'il triplo',DK,28,null),
  P('IL QUADRUPLO',1080,300,'il quadruplo',DK,28,null),
  P('IL QUINTUPLO',1380,300,'il quintuplo',DK,28,null),
  P('DEL MINIMO, 13 MENSILITÀ',960,225,'Per il duemilaventisei',AMB,30,'ruler'),
  I('seg',[520,110,GF_,'0 %',null],520,450,'nessuna riduzione'),
  I('seg',[290,110,'#E39A1C','− 25 %',null],935,450,'la reversibilità scende del venticinque'),
  I('seg',[290,110,'#D9692B','− 40 %',null],1235,450,'del quaranta'),
  I('seg',[270,110,RF_,'− 50 %',null],1525,450,'oltre, del cinquanta'),
  P('23.862,15 €',780,560,'ventitremilaottocentosessantadue',DK,28,'up'),
  P('31.816,20 €',1080,560,'trentunomilaottocentosedici',DK,28,'up'),
  P('39.770,25 €',1380,560,'trentanovemilasettecentosettanta',DK,28,'up'),
  IC(840,150,'ok',[['FINO ALLA PRIMA SOGLIA:',30],['NESSUNA RIDUZIONE',40,GRN]],480,760,['nessuna riduzione',1.2]),
  IC(840,150,'cut',[['OLTRE LA TERZA SOGLIA:',30],['LA REVERSIBILITÀ SCENDE DEL 50 %',28,'#C0392B']],1400,760,['oltre, del cinquanta',1.2])]},
]);
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ESEMPIO 1: REDDITO 28.000 €',cap:'−25 %: PERDI 3.900 € ALL\'ANNO, INCASSI 900 € AL MESE',items:[
  BN('LA TUA REVERSIBILITÀ AL MESE','1.200 €','= 15.600 € ALL\'ANNO',Object.assign({fs:96,minw:560,tfs:28,sfs:28},DKB),520,285,'Ricevi milleduecento'),
  BN('IL TUO REDDITO ANNUO','28.000 €','(REVERSIBILITÀ ESCLUSA)',Object.assign({fs:96,minw:560,tfs:28,sfs:26},AMBB),1400,285,'è di ventottomila euro'),
  I('ladder',[90],960,480,'è di ventottomila euro'),
  I('mark',['',AMB],830,570,'sei nella prima fascia'),
  BN('PERDI UN QUARTO','− 3.900 €','ALL\'ANNO · 300 AL MESE',Object.assign({fs:92,minw:560,tfs:28,sfs:28},REDB),520,760,'Perdi un quarto'),
  I('arR',[],960,760,'trecento al mese'),
  BN('INCASSI','900 €','AL MESE',Object.assign({fs:96,minw:480,tfs:28,sfs:30},GRNB),1380,760,'Quindi incassi')]},
]);
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ESEMPIO 2: REDDITO 45.000 €',cap:'−50 %: PERDI 7.800 € ALL\'ANNO, INCASSI 600 € AL MESE',items:[
  BN('STESSA REVERSIBILITÀ','1.200 €','AL MESE · 15.600 € ALL\'ANNO',Object.assign({fs:96,minw:600,tfs:28,sfs:26},DKB),520,285,'Stessa reversibilità'),
  BN('IL TUO REDDITO ANNUO','45.000 €','OLTRE L\'ULTIMA SOGLIA',Object.assign({fs:96,minw:600,tfs:28,sfs:26},AMBB),1400,285,'quarantacinquemila euro'),
  I('ladder',[90],960,480,'quarantacinquemila euro'),
  I('mark',['',AMB],1560,570,'oltre l\'ultima soglia'),
  BN('PERDI LA METÀ','− 7.800 €','ALL\'ANNO',Object.assign({fs:92,minw:520,tfs:28,sfs:30},REDB),440,760,'Perdi la metà'),
  BN('INCASSI','600 €','PER CIASCUNA DELLE 13 MENSILITÀ',Object.assign({fs:92,minw:560,tfs:28,sfs:26},GRNB),1090,760,'e incassi seicento euro'),
  I('stamp',[['I 7.800 € DELL\'INIZIO','DEL VIDEO'],RED_,30,-4],1650,700,'Sono i settemilaottocento euro')]},
]);
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CASO IN CUI NON SCATTA',cap:'CON FIGLI MINORENNI, STUDENTI O INABILI NEL NUCLEO I LIMITI NON SI APPLICANO',items:[
  P('C\'È UN CASO IN CUI LA RIDUZIONE NON SCATTA',960,230,'C\'è un caso in cui la riduzione non scatta',GF_,34,'ok'),
  I('fam',['spouse',82,null,'BENEFICIARIO'],250,420,'Se il beneficiario vive'),
  I('fam',['child',82,null,'FIGLI MINORENNI'],640,420,'figli minorenni'),
  I('fam',['stud',82,null,'STUDENTI'],1010,420,'studenti'),
  I('fam',['inab',82,null,'INABILI'],1320,420,'o inabili'),
  I('stamp',[['LIMITI DI REDDITO','NON SI APPLICANO'],'#1B9F81',32,-4],1655,430,'i limiti di reddito non si applicano'),
  IC(860,160,'ok',[['I LIMITI VALGONO PER LA PENSIONE',28],['AL SOLO CONIUGE, GENITORI, FRATELLI E SORELLE',24,GRN]],500,680,'valgono per la pensione che spetta'),
  IC(860,160,'x',[['NON VALGONO SE A RICEVERLA',28],['SONO I FIGLI, DA SOLI O CON IL CONIUGE',26,'#C0392B']],1420,680,'Non valgono se a riceverla'),
  P('CIRCOLARE INPS DEL 2015',960,840,'Lo scrive l\'Inps',DK,30,'doc')]},
]);
SPECS[16]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA SENTENZA DEL 2022',cap:'CORTE COSTITUZIONALE 162/2022: IL TAGLIO NON PUÒ SUPERARE I REDDITI',items:[
  I('decree',[560,330,'CORTE COSTITUZIONALE','SENTENZA N. 162 · 2022'],360,430,'la sentenza centosessantadue'),
  BN('IL TAGLIO NON PUÒ SUPERARE','I REDDITI',"CHE LO HANNO CAUSATO",Object.assign({fs:80,minw:620,tfs:28,sfs:30},AMBB),1080,320,'il taglio non può superare'),
  IC(760,150,'doc',[['CIRCOLARE INPS 108',34],['RIESAME D\'UFFICIO',32,GRN]],1200,520,'con la circolare centootto'),
  IC(560,130,'coin',[['ARRETRATI E INTERESSI',28],['ENTRO 5 ANNI',36,GRN]],420,730,'riconosce arretrati e interessi'),
  P('TAGLIO TROPPO ALTO? CHIEDI UN CONTROLLO',1330,700,'Se il tuo taglio ti sembra troppo alto',RF_,30,'q'),
  P('ALL\'INPS O A UN PATRONATO',1330,790,'a un patronato',DK,30,'phone')]},
]);
SPECS[17]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA DOMANDA',cap:'ONLINE, CONTACT CENTER O PATRONATO: LA PENSIONE PARTE DAL MESE DOPO',items:[
  I('br',['inps.it',760,330],440,400,'online all\'Inps'),
  OV(I('row',['DOMANDA SUPERSTITI',560,true],440,420,'con il servizio dedicato')),
  P('CONTACT CENTER',1130,290,'puoi chiamare il contact center',DK,32,'phone'),
  P('PATRONATO',1580,290,'andare da un patronato',DK,32,'people'),
  IC(740,150,'cal',[['DECORRENZA: 1° GIORNO',30],['DEL MESE DOPO IL DECESSO',30,GRN]],1380,470,'La pensione decorre'),
  IC(740,150,'clock',[['RISPOSTA ORDINARIA: 30 GIORNI',28],['ALCUNE PRATICHE: PIÙ A LUNGO',26,GRN]],1380,660,'Il termine ordinario di risposta'),
  IC(1100,130,'warn',[['ARRETRATI: PRESCRIZIONE A 5 ANNI',34],['MEGLIO NON ASPETTARE',30,'#C0392B']],700,810,'Gli arretrati si prescrivono')]},
]);
SPECS[18]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TRE SITUAZIONI DELICATE',cap:'NUOVE NOZZE, DEFUNTO RISPOSATO DOPO IL DIVORZIO, CONVIVENTE NON SPOSATO',items:[
  I('card',['1 · NUOVE NOZZE',560,460,{hc:'#2B6F8F',lines:[['PERDI LA PENSIONE',34,-70,INK],['MA RICEVI UN ASSEGNO',30,-10,GRN],['UNA VOLTA SOLA:',30,34,GRN],['2 ANNUALITÀ',46,100,INK],['TREDICESIMA COMPRESA',26,150,GRN]]}],330,470,'chi si risposa perde la pensione'),
  I('card',['2 · EX CONIUGE',560,460,{hc:GRN,lines:[['IL DEFUNTO SI ERA',32,-70,INK],['RISPOSATO DOPO',32,-26,INK],['IL DIVORZIO',32,18,INK],['QUOTA DECISA',34,90,GRN],['DAL TRIBUNALE',40,140,GRN]]}],960,470,'se il defunto si era risposato'),
  I('card',['3 · CONVIVENTE',560,460,{hc:'#C0392B',lines:[['NON SPOSATO',38,-70,INK],['NON COMPARE',34,10,INK],['NELL\'ELENCO',34,54,INK],['DEI BENEFICIARI',34,98,INK],['DELL\'INPS',34,142,GRN]]}],1590,470,'il convivente non sposato'),
  P('TRE SITUAZIONI DELICATE',960,780,'Tre situazioni delicate',AMB,34,'warn')]},
]);
SPECS[19]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA CHICCA: IL GRADINO',cap:'REDDITO E REVERSIBILITÀ RIDOTTA NON SCENDONO SOTTO IL TOTALE DELLA FASCIA PRECEDENTE',items:[
  P('LA CHICCA',330,235,'La chicca',AMB,38,'bulb'),
  P('UN EURO SOPRA LA SOGLIA NON COSTA L\'INTERA RIDUZIONE',1180,235,'Un euro sopra la soglia',DK,30,'up'),
  I('stepc',[840,400],520,545,'il gradino che non c\'è'),
  I('stamp',[['C\'È UNA','SALVAGUARDIA'],'#1B9F81',34,-4],1180,385,'c\'è una salvaguardia'),
  IC(740,170,'doc',[['REDDITO + REVERSIBILITÀ RIDOTTA',26],['NON SCENDONO SOTTO IL TOTALE',26,GRN],['CON IL REDDITO AL LIMITE PRECEDENTE',24,GRN]],1470,560,'Il totale tra reddito',{lh:40}),
  BN('CON 24.000 € DI REDDITO, APPENA SOPRA','≈ − 138 €','ALL\'ANNO, NON 3.900',Object.assign({fs:84,minw:700,tfs:26,sfs:30},GRNB),1450,765,'perdi circa centotrentotto'),
  P('IL CONTO ESATTO LO FA L\'INPS',520,850,'Il conto esatto',DK,30,'calc')]},
]);
SPECS[20]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E DAL PROSSIMO ANNO?',cap:'LE SOGLIE SI RICALCOLANO OGNI GENNAIO: STIMA INTORNO A 24.500 €',items:[
  P('OGNI GENNAIO LE SOGLIE SI RICALCOLANO',960,230,'Ogni gennaio le soglie',AMB,34,'calback'),
  IC(500,150,'up',[['AUMENTO DELLE PENSIONI',28],['SALE IL MINIMO',32,GRN]],320,400,'che segue l\'aumento delle pensioni'),
  I('arR',[],680,400,'che segue l\'aumento delle pensioni'),
  IC(500,150,'ruler',[['SOGLIE RICALCOLATE',30],['SUL TRATTAMENTO MINIMO',26,GRN]],1030,400,'sul trattamento minimo'),
  IC(500,150,'doc',[['DECRETO DI NOVEMBRE',30],['PERCENTUALE UFFICIALE',26,GRN]],1600,400,'La percentuale ufficiale'),
  BN('NOSTRE STIME: AUMENTO DAL 2,6 AL 3,1 %','≈ 24.500 €','LA SOGLIA PIÙ BASSA SALIREBBE',Object.assign({fs:100,minw:760,tfs:28,sfs:28},AMBB),620,680,'la soglia più bassa salirebbe'),
  I('stamp',[['È UNA STIMA'],RED_,40,-4],1500,650,'È una stima'),
  P('QUANDO ESCE IL DECRETO CONTROLLIAMO LE SOGLIE VERE',1260,830,'quando esce il decreto',DK,30,'lens')]},
]);
SPECS[21]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CINQUE CONTROLLI',cap:'LA LISTA DA TENERE SOTT\'OCCHIO PRIMA DI FARE I CONTI',items:[
  IC(1500,110,'people',[['1 · IN QUALE CATEGORIA RIENTRI TRA I BENEFICIARI',34]],960,260,'in quale categoria rientri'),
  IC(1500,110,'coin',[['2 · QUALE PERCENTUALE SPETTA AL TUO CASO',34]],960,395,'quale percentuale spetta'),
  IC(1500,110,'ruler',[['3 · REDDITO: SOTTO IL PRIMO LIMITE, TRA I LIMITI O SOPRA L\'ULTIMO',30]],960,530,'se il reddito sta sotto'),
  IC(1500,110,'house',[['4 · NEL NUCLEO CI SONO FIGLI CON DIRITTO? ALLORA IL TAGLIO SPARISCE',30]],960,665,'se nel nucleo familiare ci sono figli'),
  IC(1500,110,'cal',[['5 · IL MESE DEL DECESSO: DA LÌ PARTE LA PENSIONE',32]],960,800,'il mese del decesso')]},
]);
SPECS[22]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COMMENTA E VERIFICA',cap:'',items:[
  I('dbox',[1500,280,[['CANALE INFORMATIVO, NON CONSULENZA, NON AFFILIATO ALL\'INPS',32,'#fff'],['REGOLE E IMPORTI CAMBIANO OGNI ANNO: VERIFICA SU INPS.IT',30,'#fff'],['O CON UN PATRONATO · CIRCOLARI E SCHEDE NELLA DESCRIZIONE',28,'#7FF0D2']]],960,320,'Canale informativo'),
  P('SCRIVI NEL COMMENTO IL NUMERO CHE NON CONOSCEVI',960,525,'Scrivi nei commenti',AMB,34,'chat'),
  I('circ',['1'],560,622,'uno, due'),I('circ',['2'],760,622,'uno, due'),I('circ',['3'],960,622,'tre'),I('circ',['4'],1160,622,'quattro'),I('circ',['5'],1360,622,'cinque')]},
]);
