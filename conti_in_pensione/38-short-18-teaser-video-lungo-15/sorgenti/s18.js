// ===== SHORT 18: composizioni NUOVE (carta grande + calendario/cestino/timbro, scalinata di fasce + ticket + Comune, due carte a confronto, biforcazione di dicembre + conto, commento + pulsanti + telefono) =====
function elderI(p,s,col){const g=personI(p,s,col);el('path',{d:`M${46*s} ${30*s} V${-6*s} q0 ${-14*s} ${-14*s} ${-14*s}`,fill:'none',stroke:col||'#0B4A50','stroke-width':7*s,'stroke-linecap':'round'},g);return g;}
function thumbI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-96*s,y:-8*s,width:44*s,height:96*s,rx:10*s,fill:'#0B4A50',stroke:'#fff','stroke-width':6*s},g);
 el('path',{d:`M${-40*s} ${-4*s} L${-6*s} ${-78*s} Q${20*s} ${-96*s} ${32*s} ${-64*s} L${24*s} ${-26*s} H${86*s} Q${112*s} ${-24*s} ${104*s} ${8*s} L${92*s} ${62*s} Q${86*s} ${88*s} ${60*s} ${88*s} H${-40*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);return g;}
function bellI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
function handI(p){const g=el('g',{filter:'url(#g_sh2)'},p);const st={fill:SKIN,stroke:'#C9946B','stroke-width':4};
 el('rect',Object.assign({x:-50,y:30,width:100,height:100,rx:30},st),g);
 el('rect',Object.assign({x:24,y:20,width:26,height:64,rx:13},st),g);el('rect',Object.assign({x:-50,y:24,width:26,height:56,rx:13},st),g);el('rect',Object.assign({x:-10,y:14,width:26,height:70,rx:13},st),g);
 el('rect',Object.assign({x:-26,y:-62,width:34,height:140,rx:17},st),g);return g;}
// calendario: testata rossa con il mese, griglia di giorni, un giorno cerchiato con "?"
function calI(p,w,h,label,hi){const g=el('g',{},p);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:22,fill:'url(#g_paper)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh)'},g);
 el('path',{d:`M${-w/2} ${-h/2+64} V${-h/2+22} Q${-w/2} ${-h/2} ${-w/2+22} ${-h/2} H${w/2-22} Q${w/2} ${-h/2} ${w/2} ${-h/2+22} V${-h/2+64}Z`,fill:RED},g);fit(g,label,0,-h/2+46,38,'#fff',w-50);
 const cw=(w-60)/7,ch=(h-100)/4;for(let r=0;r<4;r++)for(let c=0;c<7;c++){const x=-w/2+30+c*cw+cw/2,y=-h/2+82+r*ch+ch/2;
  if(r*7+c===hi){el('circle',{cx:x,cy:y,r:Math.min(cw,ch)*.58,fill:ORG,stroke:'#fff','stroke-width':4},g);fit(g,'?',x,y+13,34,'#fff',cw);}
  else el('rect',{x:x-cw*.32,y:y-ch*.22,width:cw*.64,height:ch*.44,rx:6,fill:'#DCE7EA'},g);}
 return g;}
function basketI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-60*s} ${-10*s} Q0 ${-70*s} ${60*s} ${-10*s}`,fill:'none',stroke:'#fff','stroke-width':9*s,'stroke-linecap':'round'},g);
 el('circle',{cx:-22*s,cy:-22*s,r:20*s,fill:RED,stroke:'#fff','stroke-width':4*s},g);el('rect',{x:6*s,y:-52*s,width:30*s,height:48*s,rx:10*s,fill:'#fff',stroke:'#9FB4B9','stroke-width':3*s},g);
 el('path',{d:`M${-76*s} ${-10*s} H${76*s} L${58*s} ${56*s} H${-58*s}Z`,fill:AMB,stroke:'#fff','stroke-width':6*s,'stroke-linejoin':'round'},g);
 [-30,0,30].forEach(x=>el('line',{x1:x*s,y1:-4*s,x2:x*s*.9,y2:50*s,stroke:'#C98300','stroke-width':4*s},g));return g;}
function buildingI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-110*s} ${-40*s} L0 ${-110*s} L${110*s} ${-40*s}Z`,fill:'#fff',stroke:'#9FB4B9','stroke-width':4*s,'stroke-linejoin':'round'},g);
 el('rect',{x:-100*s,y:-40*s,width:200*s,height:20*s,fill:'#DCE7EA'},g);
 [-70,-24,24,70].forEach(x=>el('rect',{x:(x-12)*s,y:-20*s,width:24*s,height:84*s,fill:'#fff',stroke:'#9FB4B9','stroke-width':3*s},g));
 el('rect',{x:-116*s,y:64*s,width:232*s,height:20*s,rx:6*s,fill:'#DCE7EA',stroke:'#9FB4B9','stroke-width':3*s},g);
 el('line',{x1:0,y1:-110*s,x2:0,y2:-150*s,stroke:'#fff','stroke-width':5*s},g);el('path',{d:`M0 ${-150*s} h${44*s} l${-10*s} ${14*s} l${10*s} ${14*s} h${-44*s}Z`,fill:GRN},g);return g;}
function docI(p,w,h,band,l1,l2){const g=el('g',{},p);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:20,fill:'url(#g_paper)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh)'},g);
 el('path',{d:`M${-w/2} ${-h/2+54} V${-h/2+20} Q${-w/2} ${-h/2} ${-w/2+20} ${-h/2} H${w/2-20} Q${w/2} ${-h/2} ${w/2} ${-h/2+20} V${-h/2+54}Z`,fill:GRN},g);fit(g,band,0,-h/2+40,30,'#fff',w-50);
 fit(g,l1,0,-h/2+54+(h-54)*.42,40,INK,w-60);if(l2)fit(g,l2,0,-h/2+54+(h-54)*.82,40,INK,w-60);return g;}
function calcI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);el('rect',{x:-60*s,y:-80*s,width:120*s,height:160*s,rx:16*s,fill:NAVY,stroke:'#fff','stroke-width':5*s},g);
 el('rect',{x:-46*s,y:-66*s,width:92*s,height:36*s,rx:8*s,fill:'#9BF0DB'},g);
 for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('rect',{x:(-46+c*33)*s,y:(-16+r*30)*s,width:26*s,height:22*s,rx:6*s,fill:c==2&&r==2?ORG:'#fff'},g);return g;}
const hid=g=>g;
const S=[
// ---- 1: carta grande 500 + calendario 4 novembre + cestino spesa + timbro NON A TUTTI + pensionato con "?" + decreto senza regola ----
{D:DUR[0],build(p){const o={};head(p,o,'LA CARTA');
 o.cd=el('g',{},p);cardI(o.cd,800,470,'gcA','CARTA DEDICATA A TE','500 €','SPESA');
 o.bk=el('g',{},p);{const b=basketI(o.bk,.8);b.setAttribute('transform','translate(-190 0)');const pl=pillS(o.bk,'SPESA ALIMENTARE',390,28,GRN);T(pl,110,0,0,1);}
 o.cl=el('g',{},p);calI(o.cl,300,230,'4 NOVEMBRE',-1);
 o.st=el('g',{},p);el('rect',{x:-290,y:-52,width:580,height:104,rx:20,fill:'none',stroke:RED,'stroke-width':10,'stroke-dasharray':'22 12'},o.st);fit(o.st,'NON A TUTTI',0,22,68,RED,520);
 o.pq=el('g',{},p);{const av=el('g',{transform:'translate(-380 0)'},o.pq);el('circle',{r:78,fill:'#fff',stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},av);const q=elderI(av,1.5,NAVY);q.setAttribute('transform','translate(-10 14)');
  const qm=el('g',{transform:'translate(56 -56)'},av);el('circle',{r:30,fill:ORG,stroke:'#fff','stroke-width':4},qm);fit(qm,'?',0,13,40,'#fff',40);
  const pl=pillS(o.pq,'E SE PRENDI UNA PENSIONE?',600,34,NAVY);T(pl,100,0,0,1);}
 o.dc=el('g',{},p);docI(o.dc,760,190,'DECRETO','NESSUNA REGOLA','PER I PENSIONATI');{const x=el('g',{transform:'translate(310 40)'},o.dc);el('circle',{r:36,fill:RED,stroke:'#fff','stroke-width':5},x);el('path',{d:'M-13 -13 L13 13 M13 -13 L-13 13',stroke:'#fff','stroke-width':8,'stroke-linecap':'round'},x);}
 o.cap=strip(p,['LA CARTA DA 500 EURO PER LA SPESA','CI SEI ANCHE TU, SE PRENDI UNA PENSIONE?']);return o;},
 update(t,o){const a=plan(0,['La Carta Dedicata a te','per la spesa alimentare','dal quattro novembre','ma non a tutti','E se prendi una pensione','Il decreto non scrive']);PL[0]=a;headU(t,o);bgx(t);
  fade(t,o.cd,540,520,a[0]);fade(t,o.bk,720,880,a[1]);fade(t,o.cl,250,880,a[2]);
  T(o.st,540,1055,-4,pop(t,a[3]));fade(t,o.pq,540,1185,a[4]);fade(t,o.dc,540,1350,a[5]);rise(t,a[6],.9,o.cap,1560,100);}},
// ---- 2: scalinata di tre fasce + cerchi con il numero di persone + ticket "1 o 2 persone" + non fuori + articolo -> Comune + "quali?" ----
{D:DUR[1],build(p){const o={};head(p,o,'LE FASCE');
 o.fs=el('g',{},p);[0,1,2].forEach(k=>{const g=el('g',{transform:'translate(0 '+(-110+k*110)+')'},o.fs);const w=860-k*110;const tk=ticket(g,w,92,'#fff',[GRN,'#2A7A82',ORG][k]);
  const lb=el('rect',{x:-w/2+4,y:-41,width:230,height:82,rx:14,fill:[GRN,'#2A7A82',ORG][k]},g);fit(g,'FASCIA '+(k+1),-w/2+119,13,34,'#fff',200);
  for(let j=0;j<3;j++){const q=personI(g,.62,NAVY);q.setAttribute('transform','translate('+(w/2-250+j*70)+' 14)');}});
 el('rect',{x:-430,y:-165,width:860,height:20,fill:'none'},o.fs);
 o.nb=el('g',{},p);{const pl=pillS(o.nb,'IL NUMERO DI PERSONE',640,34,NAVY);T(pl,0,-70,0,1);
  [1,2,3,4].forEach((n,k)=>{const c=el('g',{transform:'translate('+(-300+k*200)+' 30)'},o.nb);el('circle',{r:46,fill:'#fff',stroke:GRN,'stroke-width':6,filter:'url(#g_sh2)'},c);
   for(let j=0;j<n;j++){const q=personI(c,.34,NAVY);q.setAttribute('transform','translate('+((j-(n-1)/2)*30)+' 10)');}});}
 o.tk=el('g',{},p);ticket(o.tk,860,150,'#fff',GRN);{[-1,1].forEach((d,k)=>0);const q1=personI(o.tk,1.1,NAVY);q1.setAttribute('transform','translate(-360 18)');
  [0,1].forEach(j=>{const q=personI(o.tk,.9,GRN);q.setAttribute('transform','translate('+(-250+j*70)+' 22)');});fit(o.tk,'FAMIGLIA DA 1 O 2 PERSONE',180,14,40,INK,380);}
 o.nf=pillS(p,'NON RESTI FUORI IN PARTENZA',760,32,GRN);
 o.ar=el('g',{},p);docI(o.ar,380,190,'UN ARTICOLO','CONDIZIONI',null);
 o.cm=el('g',{},p);{const b=buildingI(o.cm,.8);b.setAttribute('transform','translate(0 -10)');const pl=pillS(o.cm,'IL TUO COMUNE',330,28,NAVY);T(pl,0,112,0,1);}
 o.ro=el('path',{d:'M0 0 H70 M48 -22 L74 0 L48 22',fill:'none',stroke:ORG,'stroke-width':12,'stroke-linecap':'round','stroke-linejoin':'round'},p);
 o.qu=pillS(p,'QUALI?',250,40,ORG);
 o.cap=strip(p,['TRE FASCE DI PRIORITÀ','E SE LA FAMIGLIA È PICCOLA?']);return o;},
 update(t,o){const a=plan(1,['tre fasce di priorità','il numero di persone','una o due persone','non resti fuori','un articolo','dal tuo Comune','Quali?']);PL[1]=a;headU(t,o);bgx(t);
  fade(t,o.fs,540,425,a[0]);fade(t,o.nb,540,730,a[1]);fade(t,o.tk,540,905,a[2]);T(o.nf,540,1035,0,pop(t,a[3]));
  slideX(t,o.ar,290,1225,a[4],-80);T(o.ro,495,1225,0,pop(t,a[5]));slideX(t,o.cm,790,1225,a[5],80);T(o.qu,540,1405,0,pop(t,a[6]));rise(t,a[7],.9,o.cap,1560,100);}},
// ---- 3: altra carta + anziani con redditi bassi + "se ce l'hai" + due carte a confronto + "che cosa" + "? € di differenza" + calcolatrice ----
{D:DUR[2],build(p){const o={};head(p,o,'L\'ALTRA CARTA');
 o.c2=el('g',{},p);cardI(o.c2,780,410,'gcB','L\'ALTRA CARTA','','DELLO STATO');
 o.an=el('g',{},p);{const e=elderI(o.an,1.1,NAVY);e.setAttribute('transform','translate(-330 10)');const pl=pillS(o.an,'ANZIANI CON REDDITI BASSI',640,32,NAVY);T(pl,60,0,0,1);}
 o.sc=pillS(p,'SE CE L\'HAI',440,38,ORG);
 o.dv=el('g',{},p);{const a1=el('g',{transform:'translate(-250 0)'},o.dv);cardI(a1,360,200,'gcB','L\'ALTRA','','');const a2=el('g',{transform:'translate(250 0)'},o.dv);cardI(a2,360,200,'gcA','500 €','','');
  const ar=el('g',{},o.dv);el('path',{d:'M-50 -16 H50 M30 -34 L52 -16 L30 2 M50 22 H-50 M-30 4 L-52 22 L-30 40',fill:'none',stroke:'#fff','stroke-width':11,'stroke-linecap':'round','stroke-linejoin':'round'},ar);}
 o.ck=pillS(p,'CHE COSA CAMBIA?',470,34,NAVY);
 o.df=el('g',{},p);ticket(o.df,460,112,'#fff',AMB);fit(o.df,'? €',-140,24,70,INK,150);fit(o.df,'DI DIFFERENZA',80,12,30,INK,190);
 o.ca=el('g',{},p);{const c=calcI(o.ca,.62);c.setAttribute('transform','translate(-250 0)');const pl=pillS(o.ca,'LO CALCOLIAMO NEL VIDEO',520,30,GRN);T(pl,40,0,0,1);}
 o.cap=strip(p,['UN\'ALTRA CARTA DELLO STATO','COSA CAMBIA PER QUELLA DA 500 EURO?']);return o;},
 update(t,o){const a=plan(2,['un\'altra carta','anziani con redditi bassi','Se ce l\'hai','per quella dei cinquecento euro','Che cosa','quanti euro di differenza','Lo calcoliamo']);PL[2]=a;headU(t,o);bgx(t);
  fade(t,o.c2,540,500,a[0]);fade(t,o.an,540,790,a[1]);T(o.sc,540,925,0,pop(t,a[2]));fade(t,o.dv,540,1090,a[3]);
  T(o.ck,280,1280,0,pop(t,a[4]));fade(t,o.df,790,1280,a[5],40);fade(t,o.ca,540,1405,a[6],40);rise(t,a[7],.9,o.cap,1560,100);}},
// ---- 4: carta che arriva a te + calendario di dicembre con giorno "?" + due esiti (lo tieni / lo perdi) + alla fine del video + conto degli aiuti ----
{D:DUR[3],build(p){const o={};head(p,o,'LA DATA');
 o.ar=el('g',{},p);{const c=el('g',{transform:'translate(-250 0)'},o.ar);cardI(c,420,240,'gcA','500 €','','');const av=el('g',{transform:'translate(300 0)'},o.ar);el('circle',{r:80,fill:'#fff',stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},av);const q=personI(av,1.5,NAVY);q.setAttribute('transform','translate(0 14)');
  el('path',{d:'M-20 0 H70 M48 -22 L74 0 L48 22',fill:'none',stroke:ORG,'stroke-width':12,'stroke-linecap':'round','stroke-linejoin':'round',transform:'translate(-18 0)'},o.ar);}
 o.cl=el('g',{},p);calI(o.cl,420,330,'DICEMBRE',17);
 o.ti=pillS(p,'LO TIENI',360,44,'#1E9C6E');o.pe=pillS(p,'LO PERDI',360,44,RED);
 o.fi=pillS(p,'ALLA FINE DEL VIDEO',680,38,NAVY);
 o.ct=el('g',{},p);{const c=calcI(o.ct,.7);c.setAttribute('transform','translate(-300 0)');const pl=pillS(o.ct,'IL CONTO DEGLI AIUTI',500,32,GRN);T(pl,60,0,0,1);}
 o.an=pillS(p,'IN UN ANNO',380,34,AMB,NAVY);
 o.sq=el('g',{},p);{const c=el('g',{transform:'translate(-150 0)'},o.sq);cardI(c,150,92,'gcA','','','');el('line',{x1:-70,y1:44,x2:70,y2:-44,stroke:RED,'stroke-width':10,'stroke-linecap':'round',transform:'translate(-150 0)'},o.sq);
  const pl=pillS(o.sq,'SENZA LA CARTA',300,28,NAVY);T(pl,85,0,0,1);}
 o.cap=strip(p,['A DICEMBRE UNA DATA DECIDE','SE TIENI IL CONTRIBUTO O LO PERDI']);return o;},
 update(t,o){const a=plan(3,['arriva a te','a dicembre','tieni il contributo','lo perdi','alla fine del video','il conto degli aiuti','in un anno','senza quella carta']);PL[3]=a;headU(t,o);bgx(t);
  fade(t,o.ar,540,470,a[0]);fade(t,o.cl,290,880,a[1]);T(o.ti,790,800,0,pop(t,a[2]));T(o.pe,790,940,0,pop(t,a[3]));
  T(o.fi,540,1130,0,pop(t,a[4]));fade(t,o.ct,540,1235,a[5],40);T(o.an,300,1345,0,pop(t,a[6]));fade(t,o.sq,760,1345,a[7],40);rise(t,a[8],.9,o.cap,1560,100);}},
// ---- 5: Carta acquisti + "ce l'hai gia?" + commento SI/NO + mi piace + iscriviti + telefono video correlato con dito + 7 minuti + confronto + conto finale ----
{D:DUR[4],build(p){const o={};head(p,o,'TOCCA A TE');
 o.c2=el('g',{},p);cardI(o.c2,700,360,'gcB','CARTA ACQUISTI','','');
 o.qh=pillS(p,'CE L\'HAI GIÀ?',520,40,ORG);
 o.cm=el('g',{},p);el('rect',{x:-450,y:-65,width:900,height:130,rx:30,fill:NAVY,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},o.cm);
 el('rect',{x:-420,y:-40,width:500,height:80,rx:40,fill:'#fff'},o.cm);fit(o.cm,'Scrivi nei commenti…',-390,16,36,'#5B7378',420,'start');
 [['SÌ','#1E9C6E',150],['NO',RED,300]].forEach(([s,c,x])=>{const b=el('g',{transform:'translate('+(x+60)+' 0)'},o.cm);el('rect',{x:-60,y:-38,width:120,height:76,rx:38,fill:c,stroke:'#fff','stroke-width':4},b);fit(b,s,0,14,40,'#fff',90);});
 o.lk=el('g',{},p);el('rect',{x:-200,y:-62,width:400,height:124,rx:62,fill:NAVY,stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.lk);{const th=thumbI(o.lk,.5);th.setAttribute('transform','translate(-135 4)');}fit(o.lk,'MI PIACE',55,16,46,'#fff',230);
 o.is=el('g',{},p);el('rect',{x:-210,y:-72,width:420,height:144,rx:36,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.is);fit(o.is,'ISCRIVITI',-34,4,48,'#fff',250);fit(o.is,'A CONTI IN PENSIONE',-34,46,25,'#fff',290);{const be=bellI(o.is,.4);T(be,160,-4,0,1);}
 o.ph=el('g',{},p);{const s=.62;const pg=el('g',{transform:'scale('+s+')'},o.ph);el('rect',{x:-170,y:-260,width:340,height:520,rx:50,fill:'#0A1C1F',stroke:'#fff','stroke-width':6,filter:'url(#g_sh)'},pg);
  el('rect',{x:-146,y:-232,width:292,height:464,rx:30,fill:'#E9F6F4'},pg);el('rect',{x:-130,y:-222,width:260,height:62,rx:14,fill:'#fff'},pg);fit(pg,'VIDEO CORRELATO',0,-180,26,NAVY,208);
  el('rect',{x:-130,y:-140,width:260,height:160,rx:16,fill:'url(#g_red)'},pg);el('path',{d:'M-28 -98 L48 -60 L-28 -22Z',fill:'#fff','stroke-linejoin':'round',stroke:'#fff','stroke-width':12},pg);
  [[-130,50,200],[-130,82,150],[-130,114,220],[-130,146,120]].forEach(([x,y,w])=>el('rect',{x:x,y:y,width:w,height:12,rx:6,fill:'#B5C6C9'},pg));}
 o.fg=el('g',{},p);o.rip=[0,1].map(()=>el('circle',{r:20,fill:'none',stroke:'#fff','stroke-width':5},o.fg));o.hd=el('g',{},o.fg);{const h=handI(o.hd);o.hd.setAttribute('data-s','1');}
 o.mn=pillS(p,'POCO PIÙ DI 7 MINUTI',460,30,AMB,NAVY);
 o.cf=pillS(p,'IL CONFRONTO',460,32,GRN);o.cn=pillS(p,'IL CONTO FINALE',460,32,NAVY);
 o.cap=strip(p,['CE L\'HAI GIÀ, LA CARTA ACQUISTI?','SCRIVILO NEI COMMENTI']);return o;},
 update(t,o){const a=plan(4,['L\'altra carta, la Carta acquisti','ce l\'hai già','Scrivi sì o no nei commenti','Metti mi piace','iscriviti a Conti in Pensione','apri il video correlato','dura poco più di sette minuti','il confronto','il conto finale']);PL[4]=a;headU(t,o);bgx(t);
  fade(t,o.c2,540,460,a[0]);T(o.qh,540,715,0,pop(t,a[1]));fade(t,o.cm,540,865,a[2]);
  T(o.lk,290,1035,0,pop(t,a[3]));T(o.is,780,1035,0,pop(t,a[4]));
  fade(t,o.ph,260,1295,a[5]);
  const k6=a[5]+.7,e=seg(t,k6,k6+.9);T(o.fg,300,1290,0,1);op(o.fg,seg(t,k6,k6+.5));T(o.hd,10,lerp(200,30,eo3(e)),-25,.62);
  const tp=t-(k6+.9);o.rip.forEach((c,j)=>{const u=tp>0&&tp<3?((tp*0.9+j*.5)%1):0;c.setAttribute('r',20+u*50);c.setAttribute('opacity',tp>0&&tp<3?(1-u)*.9:0);});
  T(o.mn,760,1195,0,pop(t,a[6]));T(o.cf,760,1295,0,pop(t,a[7]));T(o.cn,760,1395,0,pop(t,a[8]));rise(t,a[9],.9,o.cap,1560,100);}},
];
