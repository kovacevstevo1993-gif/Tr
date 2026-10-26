// ===== SHORT 14: composizioni NUOVE in ogni blocco (calendario+percentuale, flusso tasse, linea del tempo extra, decreto, tabella+bottoni) =====
function thumbI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-96*s,y:-8*s,width:44*s,height:96*s,rx:10*s,fill:'#0B4A50',stroke:'#fff','stroke-width':6*s},g);
 el('path',{d:`M${-40*s} ${-4*s} L${-6*s} ${-78*s} Q${20*s} ${-96*s} ${32*s} ${-64*s} L${24*s} ${-26*s} H${86*s} Q${112*s} ${-24*s} ${104*s} ${8*s} L${92*s} ${62*s} Q${86*s} ${88*s} ${60*s} ${88*s} H${-40*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);return g;}
function bellI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
function arrowR(p,x,y){return el('path',{d:`M${x-34} ${y-22} H${x+6} V${y-44} L${x+44} ${y} L${x+6} ${y+44} V${y+22} H${x-34}Z`,fill:AMB,stroke:'#fff','stroke-width':5,'stroke-linejoin':'round'},p);}
const S=[
// ---- 1: calendario GENNAIO 2027 + percentuale "? %" + stima + 1.000 lordi + 29 euro + "non arrivano" ----
{D:DUR[0],build(p){const o={};head(p,o,'AUMENTO PENSIONI 2027',0);
 o.cal=dcard(p,860,230,50);const l=txt(o.cal,'AUMENTO PENSIONI',0,-36,42,'#1B9F81','bold');l.setAttribute('letter-spacing',3);txt(o.cal,'GENNAIO 2027',0,62,92,INK,'bold');
 o.pc=dcard(p,860,240,50);txt(o.pc,'? %',-285,38,112,ORG,'bold');
 el('rect',{x:-420+8,y:-100,width:844,height:200,rx:34,fill:'none',stroke:'#9FB4B9','stroke-width':4,'stroke-dasharray':'14 10'},o.pc);
 txt(o.pc,'PERCENTUALE',70,-52,40,DK,'bold');txt(o.pc,'UFFICIALE',70,-4,40,DK,'bold');txt(o.pc,'NON C\'È ANCORA',70,66,46,RED,'bold');
 o.st=pillS(p,'STIMA PIÙ CITATA',620,44,'#0B4A50');
 o.lo=dcard(p,860,190,46);txt(o.lo,'1.000 €',-390,34,100,INK,'bold','start');const pl=pillS(o.lo,'LORDI',250,40,'#0B4A50');T(pl,290,0,0,1);
 o.pl=dcard(p,860,200,50,'#E3F8EE');txt(o.pl,'+ 29 €',0,26,118,GRN,'bold');txt(o.pl,'IN PIÙ',0,80,42,DK,'bold');
 o.stp=stamp(p,'NON ARRIVANO SUL CONTO',900,50,RED);
 o.cap=capV(p,['29 € LORDI SU 1.000 €','NON ARRIVANO SUL CONTO']);return o;},
 update(t,o){const i=0;const a=plan(i,['Aumento pensioni','la percentuale ufficiale','stima più citata','mille euro lordi','ventinove euro in più','non arrivino']);PL[i]=a;headU(t,o);bgx(t);
  fade(t,o.cal,540,420,a[0]);fade(t,o.pc,540,665,a[1]);T(o.st,540,850,0,pop(t,a[2]));
  fade(t,o.lo,540,1000,a[3]);fade(t,o.pl,540,1215,a[4]);stampIn(t,o.stp,a[5],540,1395,-3);rise(t,a[6],.9,o.cap,1560,100);}},
// ---- 2: PERCHE? + flusso aumento -> tasse (imbuto) -> in tasca (portafoglio) + barre: la parte che ti resta / oltre una certa cifra ----
{D:DUR[1],build(p){const o={};head(p,o,'AUMENTO PENSIONI 2027',1);
 o.q=dcard(p,660,190,46);txt(o.q,'PERCHÉ?',0,40,110,INK,'bold');
 o.w=el('g',{},p);el('rect',{x:-125,y:-85,width:250,height:170,rx:34,fill:'#0B4A50',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.w);
 el('path',{d:'M-125 -40 H125',stroke:AMB,'stroke-width':8},o.w);el('rect',{x:55,y:-12,width:80,height:54,rx:16,fill:AMB,stroke:'#fff','stroke-width':5},o.w);el('circle',{cx:88,cy:15,r:9,fill:'#7A4A00'},o.w);
 txt(o.w,'IN TASCA',0,138,40,'#fff','bold');
 o.k=el('g',{},p);coin(o.k,0,0,88);txt(o.k,'AUMENTO',0,150,40,'#fff','bold');arrowR(o.k,172,0);
 o.f=el('g',{},p);el('path',{d:'M-130 -92 H130 L46 38 V112 H-46 V38 Z',fill:'url(#g_red)',stroke:'#fff','stroke-width':7,'stroke-linejoin':'round',filter:'url(#g_sh2)'},o.f);txt(o.f,'TASSE',0,-28,46,'#fff','bold');arrowR(o.f,172,0);
 o.b1=el('g',{},p);el('rect',{x:60,y:1418,width:960,height:8,rx:4,fill:'#fff','fill-opacity':.85},o.b1);
 [150,290,430].forEach(x=>{el('rect',{x:x-50,y:1250,width:100,height:168,rx:12,fill:'#25C48A',stroke:'#fff','stroke-width':4},o.b1);});
 txt(o.b1,'LA PARTE',290,1172,40,'#fff','bold');txt(o.b1,'CHE TI RESTA',290,1218,40,'#fff','bold');
 o.b2=el('g',{},p);el('line',{x1:540,y1:1100,x2:540,y2:1418,stroke:AMB,'stroke-width':6,'stroke-dasharray':'16 12'},o.b2);
 [650,790,930].forEach(x=>{el('rect',{x:x-50,y:1328,width:100,height:90,rx:12,fill:ORG,stroke:'#fff','stroke-width':4},o.b2);});
 const cp=pillS(o.b2,'CERTA CIFRA ? €',500,38,'#0B4A50');T(cp,540,1050,0,1);
 o.cap=capV(p,['OLTRE UNA CERTA CIFRA','NE TIENI MENO']);return o;},
 update(t,o){const i=1;const a=plan(i,['Perché?','arrivarti in tasca',"l'aumento passa",'per le tasse','non è uguale','oltre una certa cifra']);PL[i]=a;headU(t,o);bgx(t);
  fade(t,o.q,540,440,a[0]);T(o.w,890,760,0,pop(t,a[1]));T(o.k,190,760,0,pop(t,a[2]));T(o.f,540,760,0,pop(t,a[3]));
  fade(t,o.b1,0,0,a[4]);fade(t,o.b2,0,0,a[5]);rise(t,a[6],.9,o.cap,1560,100);}},
// ---- 3: pensioni minime + Irpef barrata + extra su linea del tempo fino al 2026 + 2027 dubbio + barre percentuale/aumento vero ----
{D:DUR[2],build(p){const o={};head(p,o,'AUMENTO PENSIONI 2027',2);
 o.m=dcard(p,860,200,46);txt(o.m,'PENSIONI MINIME',0,26,68,INK,'bold');
 o.ir=dcard(p,740,200,46);txt(o.ir,'IRPEF',-190,18,86,'#6F878C','bold');el('line',{x1:-340,y1:2,x2:-40,y2:-4,stroke:RED,'stroke-width':14,'stroke-linecap':'round'},o.ir);
 const gp=pillS(o.ir,'NON C\'È',250,42,GRN);T(gp,190,-14,0,1);txt(o.ir,'SEMBRA TUTTO PIÙ FACILE',0,72,36,GRN,'bold');
 o.tl=el('g',{},p);el('rect',{x:100,y:1006,width:880,height:8,rx:4,fill:'#fff','fill-opacity':.9},o.tl);
 el('rect',{x:120,y:930,width:480,height:68,rx:16,fill:AMB,stroke:'#fff','stroke-width':5},o.tl);txt(o.tl,'EXTRA',360,980,46,'#5A3A00','bold');
 o.e26=el('g',{},p);el('line',{x1:600,y1:910,x2:600,y2:1030,stroke:RED,'stroke-width':9,'stroke-linecap':'round'},o.e26);txt(o.e26,'FINO AL 2026',450,1085,40,'#fff','bold');
 o.e27=el('g',{},p);el('line',{x1:612,y1:964,x2:970,y2:964,stroke:AMB,'stroke-width':8,'stroke-dasharray':'16 12','stroke-linecap':'round'},o.e27);txt(o.e27,'2027 ?',860,1085,42,'#fff','bold');txt(o.e27,'SE NON PROROGATO',790,1140,36,AMB,'bold');
 o.br=el('g',{},p);el('rect',{x:60,y:1448,width:960,height:8,rx:4,fill:'#fff','fill-opacity':.85},o.br);
 el('rect',{x:190,y:1230,width:220,height:218,rx:14,fill:'none',stroke:'#fff','stroke-width':5,'stroke-dasharray':'14 10'},o.br);txt(o.br,'LA PERCENTUALE',300,1158,34,'#fff','bold');txt(o.br,'FA PENSARE',300,1200,34,'#fff','bold');
 el('rect',{x:670,y:1330,width:220,height:118,rx:14,fill:ORG,stroke:'#fff','stroke-width':5},o.br);txt(o.br,'AUMENTO VERO',780,1298,34,'#fff','bold');
 o.cap=capV(p,["SENZA PROROGA DELL'EXTRA",'AUMENTO VERO PIÙ PICCOLO']);return o;},
 update(t,o){const i=2;const a=plan(i,['pensioni minime',"Irpef non c'è",'un extra','fino al duemilaventisei','se non viene prorogato','più piccolo']);PL[i]=a;headU(t,o);bgx(t);
  fade(t,o.m,540,440,a[0]);fade(t,o.ir,540,670,a[1]);fade(t,o.tl,0,0,a[2]);fade(t,o.e26,0,0,a[3]);fade(t,o.e27,0,0,a[4]);fade(t,o.br,0,0,a[5]);rise(t,a[6],.9,o.cap,1560,100);}},
// ---- 4: decreto + due ministeri + striscia dei mesi con NOVEMBRE + calendario 19 + lente + calcolatrice ----
{D:DUR[3],build(p){const o={};head(p,o,'AUMENTO PENSIONI 2027',3);
 o.d=el('g',{},p);el('rect',{x:-210,y:-165,width:420,height:330,rx:20,fill:'url(#g_paper)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh)'},o.d);
 txt(o.d,'DECRETO',-20,-96,56,INK,'bold');[-40,10,60,110].forEach((y,k)=>el('rect',{x:-160,y:y,width:k==3?200:320,height:16,rx:8,fill:'#C3D3D7'},o.d));
 el('circle',{cx:140,cy:100,r:44,fill:AMB,stroke:'#fff','stroke-width':5},o.d);el('circle',{cx:140,cy:100,r:28,fill:'none',stroke:'#7A4A00','stroke-width':4},o.d);
 o.mi=el('g',{},p);const e1=pillS(o.mi,'ECONOMIA',420,44,'#0B4A50');T(e1,0,-62,0,1);const e2=pillS(o.mi,'LAVORO',420,44,GRN);T(e2,0,62,0,1);
 o.mo=el('g',{},p);const L='GFMAMGLASOND';for(let k=0;k<12;k++){const nv=k==10;el('rect',{x:100+k*80-36,y:-50,width:72,height:100,rx:14,fill:nv?AMB:'#F5FBFA',stroke:'#fff','stroke-width':4},o.mo);txt(o.mo,L[k],100+k*80,18,38,nv?'#5A3A00':'#6F878C','bold');}
 txt(o.mo,'NOVEMBRE',100+10*80,92,36,AMB,'bold');
 o.ca=el('g',{},p);el('rect',{x:-230,y:-150,width:460,height:300,rx:26,fill:'url(#g_paper)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh)'},o.ca);
 el('path',{d:'M-230 -74 V-124 a26 26 0 0 1 26 -26 H204 a26 26 0 0 1 26 26 V-74Z',fill:RED},o.ca);
 txt(o.ca,"L'ANNO SCORSO",0,-96,36,'#fff','bold');txt(o.ca,'19',-20,66,170,INK,'bold');txt(o.ca,'NOV',150,32,40,GRN,'bold');
 o.lu=el('g',{filter:'url(#g_sh2)'},p);el('circle',{cx:0,cy:0,r:62,fill:'#fff','fill-opacity':.18,stroke:AMB,'stroke-width':14},o.lu);el('line',{x1:44,y1:44,x2:104,y2:104,stroke:AMB,'stroke-width':18,'stroke-linecap':'round'},o.lu);
 o.cl=el('g',{},p);el('rect',{x:-160,y:-180,width:320,height:360,rx:40,fill:'#0B4A50',stroke:'#fff','stroke-width':6,filter:'url(#g_sh)'},o.cl);
 el('rect',{x:-124,y:-146,width:248,height:84,rx:16,fill:'#D6F5EC'},o.cl);txt(o.cl,'= ? €',100,-86,52,INK,'bold','end');
 for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('circle',{cx:-84+c*84,cy:-10+r*80,r:30,fill:(r==2&&c==2)?AMB:'#2A7A82',stroke:'#fff','stroke-width':3},o.cl);
 o.cap=capV(p,['IL DECRETO FISSA IL NUMERO','POI RIFACCIAMO IL CONTO']);return o;},
 update(t,o){const i=3;const a=plan(i,['un decreto','Economia e del Lavoro','di solito a novembre','diciannove novembre','leggiamo il testo','rifacciamo il conto']);PL[i]=a;headU(t,o);bgx(t);
  T(o.d,300,570,-3*(1-sl(t,a[0])),pop(t,a[0]));T(o.mi,790,560,0,pop(t,a[1]));fade(t,o.mo,0,860,a[2]);
  T(o.ca,330,1180,-2*(1-sl(t,a[3])),pop(t,a[3]));
  const lk=sl(t,a[4]);T(o.lu,lerp(560,380,lk),lerp(760,640,lk),0,pop(t,a[4]));T(o.cl,780,1180,0,pop(t,a[5]));rise(t,a[6],.9,o.cap,1560,100);}},
// ---- 5: tabella "?" + video correlato + tocco + mi piace + iscriviti + campana + commento ----
{D:DUR[4],build(p){const o={};head(p,o,'AUMENTO PENSIONI 2027',4);
 o.tb=dcard(p,860,340,46);txt(o.tb,'TABELLA NETTA',0,-98,50,GRN,'bold');
 [['600 €','? €',-24],['…','…',52],['3.000 €','? €',128]].forEach(r=>{txt(o.tb,r[0],-340,r[2]+20,58,INK,'bold','start');el('path',{d:`M-60 ${r[2]+4} H20 V${r[2]-12} L56 ${r[2]+12} L20 ${r[2]+36} V${r[2]+20} H-60Z`,fill:AMB},o.tb);txt(o.tb,r[1],340,r[2]+20,58,ORG,'bold','end');});
 o.v=el('g',{},p);const pb=playBtn(o.v);pb.setAttribute('transform','scale(.5)');const vp=pillS(o.v,'VIDEO CORRELATO',560,38,'#0B4A50');T(vp,0,182,0,1);
 o.tp=el('g',{},p);el('circle',{r:46,fill:'none',stroke:'#fff','stroke-width':8,'stroke-opacity':.9},o.tp);el('circle',{r:78,fill:'none',stroke:'#fff','stroke-width':6,'stroke-opacity':.5},o.tp);el('circle',{r:22,fill:'#fff'},o.tp);
 const tpl=pillS(o.tp,'TOCCA ADESSO',420,36,AMB,'#5A3A00');T(tpl,-100,240,0,1);
 o.li=el('g',{},p);el('circle',{r:78,fill:'#0B4A50',stroke:'#fff','stroke-width':7,filter:'url(#g_sh2)'},o.li);const tg=thumbI(o.li,.6);tg.setAttribute('transform','translate(-6 -2)');
 o.is=el('g',{},p);el('rect',{x:-260,y:-62,width:520,height:124,rx:62,fill:'url(#g_red)',stroke:'#fff','stroke-width':7,filter:'url(#g_sh2)'},o.is);txt(o.is,'ISCRIVITI',-20,20,56,'#fff','bold');
 o.be=bellI(p,.8);
 o.co=el('g',{},p);el('rect',{x:-450,y:-75,width:900,height:150,rx:44,fill:'url(#g_paper)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh)'},o.co);
 txt(o.co,'SCRIVI NEI COMMENTI',0,-10,44,GRN,'bold');txt(o.co,'LA TUA PENSIONE LORDA',0,44,42,INK,'bold');
 o.cap=capV(p,['TOCCA IL VIDEO CORRELATO','SCRIVI QUANTO PRENDI']);return o;},
 update(t,o){const i=4;const a=plan(i,['tabella netta','video correlato','toccalo adesso','mi piace','iscriviti a Conti','scrivi nei commenti']);PL[i]=a;headU(t,o);bgx(t);
  fade(t,o.tb,540,480,a[0]);T(o.v,540,800,0,pop(t,a[1]));
  const s=seg(t,a[2],a[2]+.9);T(o.tp,640,830,0,s>0?lerp(1.5,1,eo3(s)):0);op(o.tp,clamp(s*2.5));
  T(o.li,170,1195,0,pop(t,a[3]));T(o.is,590,1195,0,pop(t,a[4]));T(o.be,940,1195,0,pop(t,a[4]+.25));
  fade(t,o.co,540,1375,a[5]);rise(t,a[6],.9,o.cap,1560,100);}},
];
