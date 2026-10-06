// =================== helper blocchi 21-25 ===================
function meter(p,max,thr,val,label){const g=el('g',{},p);const W=900;
 el('rect',{x:-W/2,y:-30,width:W,height:60,rx:30,fill:'#0A3F45',stroke:LT,'stroke-width':3},g);
 const f=el('rect',{x:-W/2,y:-30,width:10,height:60,rx:30,fill:'url(#g_badge)'},g);
 const tx=-W/2+W*thr/max;
 el('rect',{x:tx-4,y:-80,width:8,height:160,rx:4,fill:AMB},g);txt(g,'SOGLIA '+label,tx,-96,38,AMB,'900');
 const v=txt(g,'',0,100,60,'#fff','900');
 return {g,f,W,max,thr,tx,v};}
function setMeter(m,val,k,col){m.f.setAttribute('width',Math.max(10,m.W*val/m.max*k));m.f.setAttribute('fill',col||'url(#g_badge)');}
// =================== BLOCCO 21 ===================
BLK[21]={D:18.94,S:[
{s:0,e:7.8,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LAVORI USURANTI');
 o.h=el('g',{},g);hardhat(o.h);
 o.p1=el('g',{},g);o.pl1=plate(o.p1,'61','ANNI E 7 MESI');o.pl1.s.setAttribute('font-size',28);
 o.p2=el('g',{},g);o.pl2=plate(o.p2,'35','ANNI DI CONTRIBUTI');o.pl2.s.setAttribute('font-size',28);
 o.sh=el('g',{},g);shield(o.sh);o.chip=el('g',{},g);chip(o.chip,'+1 MESE',320);
 o.no=el('g',{},g);pill(o.no,'PER LORO NON VALE',760,60,'#2FBF9B');
 o.cap=el('g',{},g);cap(o.cap,'USURANTI: ANCHE A 61 ANNI E 7 MESI, CON 35 ANNI DI CONTRIBUTI',46);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.h,960,330,0,1.2*Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.p1,500,600,0,1.2*Math.max(0,eob(seg(t,1.2,1.9))));T(o.p2,1420,600,0,1.2*Math.max(0,eob(seg(t,2.4,3.1))));
 T(o.sh,960,640,0,0.7*Math.max(0,eob(seg(t,4.6,5.3))));
 const cx=t<5.3?lerp(1800,1100,eo3(seg(t,4.0,5.3))):lerp(1100,1750,eo3(seg(t,5.4,6.4)));
 T(o.chip,cx,lerp(300,500,seg(t,4.0,5.3)),t>5.3?-10:6,t<4.0||t>6.6?0:1);
 T(o.no,960,790,-2,Math.max(0,eob(seg(t,6.2,6.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:7.8,e:13.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'UN PO’ DI ROSSO');
 o.sem=semaforo(g);setL(o.sem.L,0,1);
 o.a=el('g',{},g);card3(o.a,'QUOTA 103','#E4412C',560,170);o.b=el('g',{},g);card3(o.b,'OPZIONE DONNA','#E4412C',680,170);
 o.xa=el('g',{},g);o.xb=el('g',{},g);[o.xa,o.xb].forEach(x=>{el('line',{x1:-80,y1:-80,x2:80,y2:80,stroke:'#fff','stroke-width':22,'stroke-linecap':'round'},x);el('line',{x1:-80,y1:80,x2:80,y2:-80,stroke:'#fff','stroke-width':22,'stroke-linecap':'round'},x);});
 o.pr=el('g',{},g);pill(o.pr,'NON PROROGATE',700,64,'#06303A');
 o.cap=el('g',{},g);cap(o.cap,'QUOTA 103 E OPZIONE DONNA NON SONO STATE PROROGATE',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sem.g,420,470,0,0.85*Math.max(0,eob(seg(t,0.1,0.8))));setL(o.sem.L,0,seg(t,0.4,0.9));
 T(o.a,1240,330,-3,Math.max(0,eob(seg(t,0.8,1.5))));T(o.b,1240,560,3,Math.max(0,eob(seg(t,1.6,2.3))));
 T(o.xa,1620,330,0,Math.max(0,eob(seg(t,2.4,2.9))));T(o.xb,1660,560,0,Math.max(0,eob(seg(t,2.9,3.4))));
 T(o.pr,1240,780,-2,Math.max(0,eob(seg(t,3.4,4.0))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:13.2,e:18.94,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'MA ATTENZIONE');
 o.doc=el('g',{},g);docO(o.doc,520,640,'REQUISITI','MATURATI','ENTRO LA DATA');
 o.seal=el('g',{},g);sealO(o.seal,95);
 o.ar=el('g',{},g);el('path',{d:'M-130 0 L130 0 M70 -55 L130 0 L70 55',fill:'none',stroke:'#fff','stroke-width':20,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.k=el('g',{},g);card3(o.k,'DIRITTO CONSERVATO','#2FBF9B',760,170);o.ck=el('g',{},g);checkBadge(o.ck,90);
 o.cap=el('g',{},g);cap(o.cap,'CHI AVEVA GIÀ I REQUISITI NON PERDE IL DIRITTO!',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.doc,420,470,-3,Math.max(0,eob(seg(t,0.1,0.8))));T(o.seal,560,720,-12,Math.max(0,eob(seg(t,0.9,1.5))));
 T(o.ar,820,470,0,Math.max(0,eob(seg(t,1.4,2.0))));T(o.k,1400,450,2,Math.max(0,eob(seg(t,1.8,2.5))));T(o.ck,1760,330,0,Math.max(0,eob(seg(t,2.5,3.1))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 22 ===================
BLK[22]={D:19.25,S:[
{s:0,e:4.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'UN ESEMPIO: MARCO');
 o.m=el('g',{},g);medal(o.m,false);
 o.cal=calendarPage(g,'GENNAIO','1',320,'1985');
 o.nb=el('g',{},g);pill(o.nb,'SENZA BUCHI',560,60,'#2FBF9B');
 o.cap=el('g',{},g);cap(o.cap,'MARCO HA INIZIATO A LAVORARE A GENNAIO DEL 1985, SENZA BUCHI',46);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.m,520,440,0,1.1*Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.cal.g,1300,lerp(-700,170,eob(seg(t,0.6,1.4))),t>1.4?5*Math.exp(-2.4*(t-1.4))*Math.sin(8*(t-1.4)):0,1.15);
 T(o.nb,1300,820,-2,Math.max(0,eob(seg(t,2.2,2.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:4.0,e:8.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'42 ANNI E 11 MESI');
 o.bar=el('g',{},g);el('rect',{x:-800,y:-24,width:1600,height:48,rx:24,fill:'#0A3F45',stroke:LT,'stroke-width':3},o.bar);o.fill=el('rect',{x:-800,y:-24,width:10,height:48,rx:24,fill:'url(#g_badge)'},o.bar);
 txt(o.bar,'1985',-800,80,44,'#fff','900','middle');txt(o.bar,'DICEMBRE 2027',700,80,40,'#fff','900','middle');
 o.m=el('g',{},g);medal(o.m,false);
 o.b=el('g',{},g);el('rect',{x:-380,y:-110,width:760,height:220,rx:40,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.b);txt(o.b,'42 ANNI E 11 MESI',0,26,84,'#fff','900');
 o.ck=el('g',{},g);checkBadge(o.ck,90);
 o.cap=el('g',{},g);cap(o.cap,'A DICEMBRE 2027 AVRÀ 42 ANNI E 11 MESI DI CONTRIBUTI',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.bar,960,700,0,1);o.fill.setAttribute('width',10+1590*eio(seg(t,0.4,3.0)));
 T(o.m,-800+960+1590*eio(seg(t,0.4,3.0)),590,0,0.28);
 T(o.b,960,350,0,Math.max(0,eob(seg(t,2.6,3.3))));T(o.ck,1480,260,0,Math.max(0,eob(seg(t,3.2,3.8))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:8.4,e:13.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA PENSIONE PARTE DOPO');
 o.c1=calendarPage(g,'DICEMBRE','2027',150,'');o.c2=calendarPage(g,'MARZO','2028',150,'');
 o.mm=[0,1,2].map(i=>{const c=el('g',{},g);el('rect',{x:-85,y:-85,width:170,height:170,rx:24,fill:'url(#g_paper)',filter:'url(#g_sh2)'},c);el('rect',{x:-85,y:-85,width:170,height:50,rx:24,fill:'#E09A1A'},c);el('rect',{x:-85,y:-60,width:170,height:25,fill:'#E09A1A'},c);txt(c,'MESE',0,-48,30,'#fff','900');txt(c,''+(i+1),0,50,84,INK,'900');return c;});
 o.ar=el('g',{},g);el('path',{d:'M-40 0 L40 0 M10 -30 L40 0 L10 30',fill:'none',stroke:'#fff','stroke-width':12,'stroke-linecap':'round'},o.ar);
 o.coin=el('g',{},g);coinA(o.coin,90);
 o.cap=el('g',{},g);cap(o.cap,'MA LA PENSIONE PARTE TRE MESI DOPO, A MARZO 2028',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.c1.g,300,150,0,0.85*Math.max(0,eob(seg(t,0.1,0.8))));T(o.c2.g,1620,150,0,0.85*Math.max(0,eob(seg(t,3.2,3.9))));
 [0,1,2].forEach(i=>T(o.mm[i],700+i*260,520,(i-1)*3,Math.max(0,eob(seg(t,1.2+i*0.6,1.8+i*0.6)))));
 T(o.ar,540,520,0,Math.max(0,eob(seg(t,1.0,1.6))));
 T(o.coin,1620,700,10*Math.sin(t*4),Math.max(0,eob(seg(t,4.0,4.6))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:13.6,e:19.25,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'SE SI DIMETTE PRIMA');
 o.b=el('g',{},g);briefcase(o.b);o.s=el('g',{},g);stopSign(o.s);
 o.w=el('g',{},g);
 el('path',{d:'M-170 -90 L170 -90 L170 130 L-170 130 Z',fill:'#6F4A2A',stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},o.w);
 el('rect',{x:-170,y:-90,width:340,height:60,fill:'#8A5B33'},o.w);txt(o.w,'0',0,98,100,'#fff','900');
 o.l1=el('g',{},g);pill(o.l1,'NESSUNO STIPENDIO',700,52,'#E4412C');o.l2=el('g',{},g);pill(o.l2,'NESSUNA PENSIONE',700,52,'#E4412C');
 o.q=el('g',{},g);o.qq=[0,1,2].map(i=>{const c=el('g',{},g);el('rect',{x:-85,y:-85,width:170,height:170,rx:24,fill:'#E4412C',opacity:.9},c);txt(c,''+(i+1),0,28,70,'#fff','900');return c;});
 o.cap=el('g',{},g);cap(o.cap,'SE SI DIMETTE PRIMA: TRE MESI SENZA STIPENDIO E SENZA PENSIONE!',48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.b,400,400,-4,1.1*Math.max(0,eob(seg(t,0.1,0.8))));T(o.s,400,400,0,0);
 T(o.w,1320,400,3,1.1*Math.max(0,eob(seg(t,1.2,1.9))));
 [0,1,2].forEach(i=>T(o.qq[i],760+i*200,620,(i-1)*3,0.8*Math.max(0,eob(seg(t,2.0+i*0.5,2.5+i*0.5)))));
 T(o.l1,600,800,-2,Math.max(0,eob(seg(t,3.2,3.9))));T(o.l2,1360,800,2,Math.max(0,eob(seg(t,3.8,4.5))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 23 ===================
BLK[23]={D:12.69,S:[
{s:0,e:4.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'UN ESEMPIO: GIULIA');
 o.m=el('g',{},g);medal(o.m,true);
 o.k1=el('g',{},g);kid(o.k1,1.4);o.k2=el('g',{},g);kid(o.k2,1.4);
 o.p=el('g',{},g);o.pl=plate(o.p,'64','ANNI');
 o.cal=el('g',{},g);pill(o.cal,'HA INIZIATO NEL 1997',720,56,'#2FBF9B');
 o.cap=el('g',{},g);cap(o.cap,'GIULIA HA 64 ANNI, HA INIZIATO NEL 1997 E HA DUE FIGLI',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.m,440,420,0,1.1*Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.k1,720,560,0,Math.max(0,eob(seg(t,1.2,1.8))));T(o.k2,860,560,0,Math.max(0,eob(seg(t,1.6,2.2))));
 T(o.p,1380,430,0,1.4*Math.max(0,eob(seg(t,0.8,1.5))));
 T(o.cal,1300,770,-2,Math.max(0,eob(seg(t,2.4,3.1))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:4.6,e:8.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA SUA SOGLIA');
 o.m=meter(g,2000,1420,0,'€ 1.420');o.mm=o.m.g;
 o.big=el('g',{},g);el('rect',{x:-380,y:-100,width:760,height:200,rx:40,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.big);txt(o.big,'SOGLIA',0,-30,40,GRN,'900');txt(o.big,'€ 1.420',0,60,100,INK,'900');
 o.d=el('g',{},g);medal(o.d,true);
 o.cap=el('g',{},g);cap(o.cap,'CON DUE FIGLI LA SUA SOGLIA È CIRCA 1.420 EURO',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.mm,960,720,0,Math.max(0,eob(seg(t,0.1,0.8))));setMeter(o.m,1420,eio(seg(t,0.8,2.6)),'#E09A1A');
 T(o.big,960,350,0,Math.max(0,eob(seg(t,0.4,1.1))));T(o.d,260,360,0,0.5*Math.max(0,eob(seg(t,0.4,1.0))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:8.6,e:12.69,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PENSIONE STIMATA');
 o.m=meter(g,2000,1420,0,'€ 1.420');o.mm=o.m.g;
 o.est=el('g',{},g);el('rect',{x:-380,y:-100,width:760,height:200,rx:40,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.est);txt(o.est,'STIMATA',0,-30,40,'#fff','900');txt(o.est,'€ 1.500',0,60,100,'#fff','900');
 o.ok=el('g',{},g);pill(o.ok,'PUÒ USCIRE!',560,80,'#2FBF9B');o.ck=el('g',{},g);checkBadge(o.ck,90);
 o.cap=el('g',{},g);cap(o.cap,'PENSIONE STIMATA 1.500 EURO: PUÒ USCIRE!',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.mm,960,720,0,1);setMeter(o.m,1500,eio(seg(t,0.4,2.0)),'url(#g_badge)');
 T(o.est,960,350,0,Math.max(0,eob(seg(t,0.1,0.8))));T(o.ok,960,520,-2,Math.max(0,eob(seg(t,2.0,2.7))));T(o.ck,1500,330,0,Math.max(0,eob(seg(t,2.4,3.0))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 24 ===================
BLK[24]={D:9.36,S:[
{s:0,e:3.7,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'E SE FOSSE MILLE E TRECENTO?');
 o.m=meter(g,2000,1420,0,'€ 1.420');o.mm=o.m.g;
 o.est=el('g',{},g);el('rect',{x:-380,y:-100,width:760,height:200,rx:40,fill:'#E4412C',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.est);txt(o.est,'STIMATA',0,-30,40,'#fff','900');txt(o.est,'€ 1.300',0,60,100,'#fff','900');
 o.hg=el('g',{},g);hourglass(o.hg);
 o.cap=el('g',{},g);cap(o.cap,'SE È 1.300, DEVE ASPETTARE!',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.mm,960,720,0,1);setMeter(o.m,1300,eio(seg(t,0.4,1.8)),'#E4412C');
 T(o.est,700,350,0,Math.max(0,eob(seg(t,0.1,0.8))));T(o.hg,1500,380,0,0.9*Math.max(0,eob(seg(t,1.8,2.5)))*(1+0.02*Math.sin(t*5)));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:3.7,e:9.36,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'UN ALTRO ESEMPIO: LUCA');
 o.m=el('g',{},g);medal(o.m,false);
 o.tl=el('g',{},g);el('rect',{x:-700,y:-6,width:1400,height:12,rx:6,fill:'#fff',opacity:.85},o.tl);
 el('rect',{x:-700,y:-90,width:500,height:180,rx:20,fill:'#E4412C',opacity:.25},o.tl);el('rect',{x:-200,y:-90,width:900,height:180,rx:20,fill:'#2FBF9B',opacity:.25},o.tl);
 el('rect',{x:-205,y:-130,width:10,height:260,rx:5,fill:AMB},o.tl);txt(o.tl,'1996',-200,-150,56,AMB,'900');txt(o.tl,'1988',-460,80,44,'#FFB3A8','900');
 o.c=el('g',{},g);coinA(o.c,56);
 o.sg=el('g',{},g);el('rect',{x:-260,y:-100,width:520,height:200,rx:36,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.sg);txt(o.sg,'64 ANNI',0,34,100,'#fff','900');
 o.x=el('g',{},g);el('line',{x1:-300,y1:-130,x2:300,y2:130,stroke:'#E4412C','stroke-width':30,'stroke-linecap':'round'},o.x);el('line',{x1:-300,y1:130,x2:300,y2:-130,stroke:'#E4412C','stroke-width':30,'stroke-linecap':'round'},o.x);
 o.cap=el('g',{},g);cap(o.cap,'LUCA HA CONTRIBUTI PRIMA DEL 1996: I 64 ANNI, OGGI, NON ESISTONO',46);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.m,360,370,0,0.85*Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.tl,1160,730,0,Math.max(0,eob(seg(t,0.4,1.1))));
 T(o.c,1160-460,730,0,Math.max(0,eob(seg(t,1.2,1.8))));
 T(o.sg,1260,360,0,Math.max(0,eob(seg(t,2.6,3.3))));T(o.x,1260,360,0,Math.max(0,eob(seg(t,3.4,3.9))));op(o.x,seg(t,3.4,3.7));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 25 ===================
function ministry(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:'M-220 -40 L0 -170 L220 -40 Z',fill:'#6F878C',stroke:'#fff','stroke-width':6},g);
 el('rect',{x:-220,y:-40,width:440,height:30,fill:'#C9D6D8'},g);
 for(let i=-2;i<=2;i++)el('rect',{x:i*80-22,y:-10,width:44,height:170,rx:8,fill:'#EAF7F4'},g);
 el('rect',{x:-240,y:160,width:480,height:36,rx:8,fill:'#6F878C'},g);txt(g,'MEF',0,-70,56,'#fff','900');return g;}
BLK[25]={D:16.85,S:[
{s:0,e:5.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL SEMAFORO GIALLO');
 o.sem=semaforo(g);
 o.pr=el('g',{},g);card3(o.pr,'LE PROPOSTE','#E09A1A',620,170);
 o.st=el('g',{},g);el('rect',{x:-420,y:-80,width:840,height:160,rx:20,fill:'none',stroke:'#E4412C','stroke-width':14},o.st);txt(o.st,'NIENTE È LEGGE!',0,34,88,'#E4412C','900');
 o.cap=el('g',{},g);cap(o.cap,'SEMAFORO GIALLO: LE PROPOSTE. NIENTE DI QUELLO CHE DICO È LEGGE!',48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sem.g,420,470,0,0.85*Math.max(0,eob(seg(t,0.1,0.8))));setL(o.sem.L,1,seg(t,0.5,1.0));
 T(o.pr,1240,350,-3,Math.max(0,eob(seg(t,0.8,1.5))));T(o.st,1240,600,-8,Math.max(0,eob(seg(t,2.2,2.9)))*(t>2.9?1+0.03*Math.sin((t-2.9)*7):1));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:5.0,e:10.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PRIMA PROPOSTA');
 o.cal=calendarPage(g,'ANNO','2027',150,'');
 o.st=el('g',{},g);stopSign(o.st);
 o.ch=el('g',{},g);chip(o.ch,'+1 MESE',320);
 o.lg=el('g',{},g);pill(o.lg,'LO CHIEDE LA LEGA',740,60,'#06303A');
 o.rq=el('g',{},g);pill(o.rq,'SOLO UNA RICHIESTA',740,60,'#E09A1A');
 o.cap=el('g',{},g);cap(o.cap,"PRIMA PROPOSTA: STOP ALL'AUMENTO DELL'ETÀ DEL 2027",50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.cal.g,500,150,0,1.1*Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.ch,500,700,-3,Math.max(0,eob(seg(t,0.8,1.5))));T(o.st,1330,430,0,1.3*Math.max(0,eob(seg(t,1.8,2.5))));
 T(o.lg,1330,720,-2,Math.max(0,eob(seg(t,3.0,3.7))));T(o.rq,1330,830,2,Math.max(0,eob(seg(t,4.0,4.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:10.6,e:16.85,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'DIPENDE DA...');
 o.mi=el('g',{},g);ministry(o.mi);
 o.c=[0,1,2,3].map(i=>{const c=el('g',{},g);coinA(c,54);return c;});
 o.q=el('g',{},g);qBubble(o.q,100);
 o.k=el('g',{},g);pill(o.k,'I COSTI',460,64,'#E09A1A');o.d=el('g',{},g);pill(o.d,'IL MINISTERO DELL’ECONOMIA',900,56,'#06303A');
 o.cap=el('g',{},g);cap(o.cap,"DIPENDE DAI COSTI E DAL MINISTERO DELL'ECONOMIA",52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.mi,1360,430,0,1.2*Math.max(0,eob(seg(t,0.1,0.8))));
 o.c.forEach((c,i)=>{const k=eob(seg(t,0.8+i*0.4,1.4+i*0.4));T(c,300+i*150,lerp(200,560,k)+Math.sin(t*3+i)*6,i*20,Math.max(0,k));});
 T(o.k,520,760,-3,Math.max(0,eob(seg(t,2.2,2.9))));T(o.d,1360,760,2,Math.max(0,eob(seg(t,3.2,3.9))));
 T(o.q,1000,300,10*Math.sin(t*4),Math.max(0,eob(seg(t,4.0,4.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
