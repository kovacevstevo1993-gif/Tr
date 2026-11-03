// ===== SHORT 16: composizioni NUOVE in ogni blocco (palazzo+tre schede, buono+documento, fondo/uscita+righello eta', schede dei tre temi+commento+video) =====
function personI(p,s,col){const g=el('g',{},p);col=col||'#0B4A50';el('circle',{cx:0,cy:-30*s,r:20*s,fill:col},g);el('path',{d:`M${-34*s} ${40*s} Q${-34*s} ${-4*s} 0 ${-4*s} Q${34*s} ${-4*s} ${34*s} ${40*s}Z`,fill:col},g);return g;}
function calcI(p,s){const g=el('g',{},p);el('rect',{x:-40*s,y:-52*s,width:80*s,height:104*s,rx:12*s,fill:'#0B4A50',stroke:'#fff','stroke-width':4},g);el('rect',{x:-30*s,y:-42*s,width:60*s,height:26*s,rx:5*s,fill:'#D6F5EC'},g);
 for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('circle',{cx:(-20+c*20)*s,cy:(0+r*18)*s,r:6*s,fill:(r==2&&c==2)?AMB:'#7FF0D2'},g);return g;}
function thumbI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-96*s,y:-8*s,width:44*s,height:96*s,rx:10*s,fill:'#0B4A50',stroke:'#fff','stroke-width':6*s},g);
 el('path',{d:`M${-40*s} ${-4*s} L${-6*s} ${-78*s} Q${20*s} ${-96*s} ${32*s} ${-64*s} L${24*s} ${-26*s} H${86*s} Q${112*s} ${-24*s} ${104*s} ${8*s} L${92*s} ${62*s} Q${86*s} ${88*s} ${60*s} ${88*s} H${-40*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);return g;}
function bellI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
function palazzoI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-270*s} ${-60*s} L0 ${-190*s} L${270*s} ${-60*s}Z`,fill:'#F3F8F9',stroke:'#fff','stroke-width':4,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:-100*s,r:28*s,fill:AMB},g);
 el('rect',{x:-270*s,y:-60*s,width:540*s,height:30*s,fill:'#DCE7EA'},g);
 for(let k=0;k<5;k++)el('rect',{x:(-220+k*110)*s-20*s,y:-30*s,width:40*s,height:150*s,rx:6*s,fill:'#fff',stroke:'#C9D6D8','stroke-width':2},g);
 el('rect',{x:-290*s,y:120*s,width:580*s,height:26*s,fill:'#C9D6D8'},g);el('rect',{x:-320*s,y:146*s,width:640*s,height:26*s,fill:'#9FB4B9'},g);
 el('line',{x1:0,y1:-190*s,x2:0,y2:-262*s,stroke:'#fff','stroke-width':6},g);el('path',{d:`M0 ${-262*s} H${70*s} L${50*s} ${-240*s} L${70*s} ${-218*s} H0Z`,fill:RED},g);return g;}
function safeI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-130*s,y:-120*s,width:260*s,height:240*s,rx:26*s,fill:'#2A7A82',stroke:'#fff','stroke-width':6},g);
 el('rect',{x:-104*s,y:-94*s,width:208*s,height:188*s,rx:16*s,fill:'#0B4A50'},g);
 el('circle',{cx:-18*s,cy:-40*s,r:36*s,fill:'none',stroke:AMB,'stroke-width':9},g);el('circle',{cx:-18*s,cy:-40*s,r:7*s,fill:AMB},g);
 el('rect',{x:48*s,y:-62*s,width:26*s,height:44*s,rx:10*s,fill:'#9FB4B9'},g);
 el('rect',{x:-110*s,y:120*s,width:40*s,height:22*s,fill:'#06303A'},g);el('rect',{x:70*s,y:120*s,width:40*s,height:22*s,fill:'#06303A'},g);return g;}
function doorI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-80*s,y:-120*s,width:160*s,height:240*s,rx:12*s,fill:'#0B3A3F',stroke:'#fff','stroke-width':6},g);el('rect',{x:-60*s,y:-100*s,width:120*s,height:200*s,rx:8*s,fill:'#25C48A'},g);
 el('circle',{cx:38*s,cy:6*s,r:9*s,fill:YEL},g);
 el('rect',{x:-70*s,y:-168*s,width:140*s,height:40*s,rx:10*s,fill:'#25C48A',stroke:'#fff','stroke-width':4},g);txt(g,'USCITA',0,-138*s,26*s,'#fff','bold');return g;}
function flagI(p,s){const g=el('g',{},p);el('line',{x1:0,y1:60*s,x2:0,y2:-70*s,stroke:'#fff','stroke-width':8*s,'stroke-linecap':'round'},g);el('path',{d:`M0 ${-70*s} H${80*s} L${58*s} ${-42*s} L${80*s} ${-14*s} H0Z`,fill:AMB,stroke:'#fff','stroke-width':4},g);return g;}
function voucher(p,w,h){const g=el('g',{},p);
 el('path',{d:`M${-w/2+24} ${-h/2} H${w/2-24} A24 24 0 0 0 ${w/2} ${-h/2+24} V${-30} A32 32 0 0 0 ${w/2} 30 V${h/2-24} A24 24 0 0 0 ${w/2-24} ${h/2} H${-w/2+24} A24 24 0 0 0 ${-w/2} ${h/2-24} V30 A32 32 0 0 0 ${-w/2} ${-30} V${-h/2+24} A24 24 0 0 0 ${-w/2+24} ${-h/2}Z`,fill:'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh)'},g);
 el('line',{x1:-w/2+230,y1:-h/2+22,x2:-w/2+230,y2:h/2-22,stroke:'#9FB4B9','stroke-width':4,'stroke-dasharray':'10 10'},g);
 el('circle',{cx:-w/2+115,cy:0,r:70,fill:'#25C48A',stroke:'#fff','stroke-width':6},g);el('rect',{x:-w/2+115-14,y:-44,width:28,height:88,rx:6,fill:'#fff'},g);el('rect',{x:-w/2+115-44,y:-14,width:88,height:28,rx:6,fill:'#fff'},g);
 return g;}
const S=[
// ---- 1: palazzo del governo + tre schede coperte "?" + una rivela "circa 500 euro l'anno" + quattro pensionati (due si' / due no) + "chi ci guadagna?" + timbro disegno di legge ----
{D:DUR[0],build(p){const o={};head(p,o);
 o.pa=el('g',{},p);palazzoI(o.pa,.62);fit(o.pa,'GOVERNO',0,150,46,'#fff',360);
 o.cs=[0,1,2].map(k=>{const c=taped(p,290,300);c.q=el('g',{},c);fit(c.q,'NOVITÀ',0,-92,40,GRN,240);txt(c.q,'?',0,70,170,ORG,'bold');return c;});
 o.rv=el('g',{},o.cs[2]);fit(o.rv,'CIRCA',0,-86,40,GRN,240);fit(o.rv,'500 €',0,18,92,ORG,250);fit(o.rv,"ALL'ANNO",0,88,46,INK,250);op(o.rv,0);
 o.pn=el('g',{},p);[0,1,2,3].forEach(k=>{const g=el('g',{},o.pn);T(g,-300+k*200,0,0,1);el('circle',{r:62,fill:'#fff',stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},g);personI(g,1.35,'#0B4A50');
  const ok=k<2;el('circle',{cx:46,cy:46,r:26,fill:ok?'#25C48A':RED,stroke:'#fff','stroke-width':5},g);
  el('path',{d:ok?'M34 46 L43 56 L60 36':'M36 36 L58 58 M58 36 L36 58',fill:'none',stroke:'#fff','stroke-width':7,'stroke-linecap':'round','stroke-linejoin':'round'},g);});
 {const pp=pillS(o.pn,'NON PER OGNI PENSIONATO',860,36,'#0B4A50');T(pp,0,118,0,1);}
 o.cq=pillS(p,'CHI CI GUADAGNA?',700,52,ORG);
 o.st=el('g',{},p);el('rect',{x:-330,y:-62,width:660,height:124,rx:20,fill:'rgba(255,255,255,0.93)',stroke:RED,'stroke-width':10},o.st);fit(o.st,'DISEGNO DI LEGGE',0,-12,50,RED,600);fit(o.st,'PUÒ CAMBIARE',0,48,34,RED,600);
 o.cap=balloon(p,['TRE NOVITÀ NELLA MANOVRA','UNA FINO A CIRCA 500 €']);return o;},
 update(t,o){const i=0;const a=plan(i,['governo','tre novità','Una può arrivare','non per ogni pensionato','Chi ci guadagna','disegno di legge']);PL[i]=a;headU(t,o,0);bgx(t);
  fade(t,o.pa,540,430,a[0]);
  [-330,0,330].forEach((dx,k)=>T(o.cs[k],540+dx,800,(k-1)*3,pop(t,a[1]+k*.12)));
  op(o.cs[2].q,1-seg(t,a[2],a[2]+.3));op(o.rv,seg(t,a[2]+.4,a[2]+.9));
  fade(t,o.pn,540,1060,a[3]);T(o.cq,540,1285,0,pop(t,a[4]));stampIn(t,o.st,a[5],540,1432,-4,1.08);rise(t,a[6],.9,o.cap,1620,100);}},
// ---- 2: buono con croce (spese sanitarie) + due domande (per chi? quanto vale?) + comunicato letto riga per riga + foglio vuoto "non ancora scritto" ----
{D:DUR[1],build(p){const o={};head(p,o);
 o.vo=el('g',{},p);voucher(o.vo,860,270);fit(o.vo,'BUONO',150,-14,100,INK,420);fit(o.vo,'SPESE SANITARIE',150,64,44,GRN,420);
 o.q=el('g',{},p);{const a1=pillS(o.q,'PER CHI?',380,44,GRN);T(a1,-250,0,0,1);const a2=pillS(o.q,'QUANTO VALE?',470,44,ORG);T(a2,250,0,0,1);}
 o.d1=taped(p,440,480);el('rect',{x:-190,y:-186,width:380,height:60,rx:10,fill:NAVY},o.d1);fit(o.d1,'COMUNICATO',0,-146,34,'#fff',340);
 for(let k=0;k<7;k++){const y=-96+k*52;if(k<3)el('rect',{x:-200,y:y-14,width:400,height:36,rx:8,fill:AMB,'fill-opacity':.55},o.d1);el('rect',{x:-180,y:y,width:360-(k%3)*50,height:12,rx:6,fill:'#9FB4B9'},o.d1);}
 o.rr=pillS(p,'RIGA PER RIGA',420,36,GRN);
 o.d2=el('g',{},p);el('rect',{x:-220,y:-240,width:440,height:480,rx:20,fill:'#fff','fill-opacity':.14,stroke:AMB,'stroke-width':8,'stroke-dasharray':'20 14'},o.d2);
 for(let k=0;k<5;k++)el('rect',{x:-170,y:-170+k*52,width:340-(k%2)*70,height:12,rx:6,fill:'#fff','fill-opacity':.35},o.d2);
 fit(o.d2,'?',0,150,200,AMB,200);{const sp=pillS(o.d2,'NON ANCORA SCRITTO',420,26,'#0B4A50');T(sp,0,-200,0,1);}
 o.cap=balloon(p,['BUONO PER LE','SPESE SANITARIE']);return o;},
 update(t,o){const i=1;const a=plan(i,['un buono per le spese sanitarie','Per chi è','comunicato ufficiale','non ha ancora scritto']);PL[i]=a;headU(t,o,1);bgx(t);
  fade(t,o.vo,540,520,a[0]);T(o.q,540,810,0,pop(t,a[1]));
  fade(t,o.d1,300,1150,a[2]);T(o.rr,300,1450,0,pop(t,a[2]+.3));fade(t,o.d2,780,1150,a[3]);rise(t,a[4],.9,o.cap,1625,100);}},
// ---- 3: cassaforte "fondo" + porta d'uscita con persona + sistema contributivo + righello dell'eta' con "?" + timbro "non scritta" + bandiera "regola gia' fissata" + scheda Irpef con calcolatrice ----
{D:DUR[2],build(p){const o={};head(p,o);
 o.fd=el('g',{},p);{const sf=safeI(o.fd,1.0);T(sf,-260,0,0,1);const dr=doorI(o.fd,1.0);T(dr,240,0,0,1);const pe=personI(o.fd,1.3,'#fff');T(pe,60,50,0,1);
  el('path',{d:'M-110 30 H-30 V10 L20 50 L-30 90 V70 H-110Z',fill:AMB,stroke:'#fff','stroke-width':5,'stroke-linejoin':'round'},o.fd);fit(o.fd,'FONDO',-260,72,46,'#fff',170);}
 o.sc=pillS(p,'SISTEMA CONTRIBUTIVO',820,40,'#0B4A50');
 o.et=taped(p,920,240);fit(o.et,'DA CHE ETÀ?',0,-52,76,INK,780);
 el('rect',{x:-400,y:20,width:800,height:16,rx:8,fill:'#9FB4B9'},o.et);for(let k=0;k<=10;k++)el('rect',{x:-404+k*80,y:6,width:8,height:(k%5==0)?44:30,rx:3,fill:NAVY},o.et);
 el('circle',{cx:-404+3*80+4,cy:84,r:30,fill:ORG,stroke:'#fff','stroke-width':5},o.et);txt(o.et,'?',-404+3*80+4,99,42,'#fff','bold');
 o.ns=el('g',{},p);el('rect',{x:-250,y:-46,width:500,height:92,rx:18,fill:'rgba(255,255,255,0.94)',stroke:RED,'stroke-width':9},o.ns);fit(o.ns,'NON SCRITTA',0,14,56,RED,460);
 o.rg=el('g',{},p);{const rp=pillS(o.rg,'REGOLA GIÀ FISSATA',760,42,GRN);T(rp,60,-30,0,1);const fl=flagI(o.rg,1.0);T(fl,-380,-10,0,1);const dp=pillS(o.rg,'DA QUI SI PARTE',520,34,'#0B4A50');T(dp,60,50,0,1);}
 o.ir=taped(p,920,230);{const ci=calcI(o.ir,1.5);T(ci,-340,0,0,1);fit(o.ir,"TAGLIO DELL'IRPEF",100,-26,62,INK,640);const pc=pillS(o.ir,'IL CONTO',300,40,ORG);T(pc,100,58,0,1);}
 o.cap=balloon(p,['IL FONDO: DA CHE ETÀ?','IL TAGLIO IRPEF: IL CONTO']);return o;},
 update(t,o){const i=2;const a=plan(i,['un fondo per chi esce','sistema contributivo','Da che età','non lo scrive','regola già fissata','La terza']);PL[i]=a;headU(t,o,tt=>tt<a[5]?2:3);bgx(t);
  fade(t,o.fd,575,500,a[0]);T(o.sc,540,730,0,pop(t,a[1]));fade(t,o.et,540,925,a[2]);stampIn(t,o.ns,a[3],740,985,-6,1.5);
  T(o.rg,540,1140,0,pop(t,a[4]));fade(t,o.ir,540,1380,a[5]);rise(t,a[6],.9,o.cap,1625,100);}},
// ---- 4: le tre schede (buono, fondo, Irpef) + commento + video correlato con freccia + tocca + mi piace + iscriviti ----
{D:DUR[3],build(p){const o={};head(p,o);
 o.tr=el('g',{},p);[['BUONO','#25C48A'],['FONDO',AMB],['IRPEF',ORG]].forEach((d,k)=>{const c=taped(o.tr,290,210);T(c,-330+k*330,0,(k-1)*3,1);el('rect',{x:-130,y:50,width:260,height:16,rx:8,fill:d[1]},c);fit(c,d[0],-18,24,62,INK,190);
  el('circle',{cx:106,cy:-66,r:30,fill:d[1],stroke:'#fff','stroke-width':5},c);txt(c,'?',106,-50,44,'#fff','bold');});
 o.cm=el('g',{},p);el('rect',{x:-470,y:-90,width:940,height:180,rx:34,fill:NAVY,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},o.cm);
 el('circle',{cx:-400,cy:-22,r:34,fill:'#7FF0D2'},o.cm);el('rect',{x:-340,y:-34,width:240,height:20,rx:10,fill:'#fff','fill-opacity':.5},o.cm);
 el('rect',{x:-420,y:22,width:840,height:52,rx:26,fill:'#fff'},o.cm);fit(o.cm,'Scrivilo nei commenti…',-380,58,34,'#5B7378',620,'start');el('rect',{x:300,y:32,width:5,height:32,fill:ORG},o.cm);
 o.vi=el('g',{},p);{const c=taped(o.vi,640,310);el('rect',{x:-290,y:-125,width:580,height:200,rx:16,fill:'url(#g_red)'},c);el('path',{d:'M-40 -85 L60 -25 L-40 35Z',fill:'#fff'},c);fit(c,'VIDEO CORRELATO ▼',0,128,40,INK,560);}
 o.tp=el('g',{},p);el('rect',{x:-260,y:-52,width:520,height:104,rx:52,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.tp);fit(o.tp,'APRILO ADESSO',0,16,50,'#fff',460);
 o.li=el('g',{},p);el('circle',{r:58,fill:NAVY,stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.li);{const th=thumbI(o.li,.55);th.setAttribute('transform','translate(-6 -2)');}
 o.is=el('g',{},p);el('rect',{x:-250,y:-54,width:500,height:108,rx:54,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.is);txt(o.is,'ISCRIVITI',-20,19,52,'#fff','bold');{const be=bellI(o.is,.55);T(be,196,0,0,1);}
 o.cap=balloon(p,['APRI IL VIDEO CORRELATO','METTI MI PIACE E ISCRIVITI']);return o;},
 update(t,o){const i=3;const a=plan(i,['Quale delle tre','Scrivilo nei commenti','video correlato','aprilo adesso','mi piace','iscriviti']);PL[i]=a;headU(t,o,3);bgx(t);
  fade(t,o.tr,540,470,a[0]);fade(t,o.cm,540,720,a[1]);fade(t,o.vi,540,1040,a[2]);T(o.tp,540,1290,0,pop(t,a[3]));T(o.li,250,1425,0,pop(t,a[4]));T(o.is,700,1425,0,pop(t,a[5]));rise(t,a[6],.9,o.cap,1625,100);}},
];
