// ===== oggetti extra =====
function sealO(p,r){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('circle',{r:r,fill:'#0B4A50',stroke:AMB,'stroke-width':r*0.1},g);
 el('circle',{r:r*0.82,fill:'none',stroke:'#fff','stroke-width':3,'stroke-dasharray':'6 8'},g);
 const a=[];for(let i=0;i<5;i++){const an=-Math.PI/2+i*2*Math.PI/5,bn=an+Math.PI/5;a.push([Math.cos(an)*r*0.34,Math.sin(an)*r*0.34-r*0.18],[Math.cos(bn)*r*0.15,Math.sin(bn)*r*0.15-r*0.18]);}
 el('polygon',{points:a.map(q=>q.join(',')).join(' '),fill:AMB},g);
 txt(g,'UFFICIALE',0,r*0.62,r*0.2,'#fff','900');return g;}
function docO(p,w,h,l1,l2,l3){const g=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:90,rx:26,fill:'url(#g_head)'},g);el('rect',{x:-w/2,y:-h/2+50,width:w,height:40,fill:'url(#g_head)'},g);
 txt(g,l1,0,-h/2+62,46,'#fff','900');
 txt(g,l2,0,-h/2+170,78,INK,'900');txt(g,l3,0,-h/2+240,44,GRN,'900');
 for(let i=0;i<6;i++)el('rect',{x:-w/2+50,y:-h/2+290+i*50,width:w-100-(i%3)*70,height:14,rx:7,fill:'#C9D6D8'},g);
 return g;}
function briefcase(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:'M-60 -90 L-60 -130 Q-60 -150 -40 -150 L40 -150 Q60 -150 60 -130 L60 -90',fill:'none',stroke:'#6F878C','stroke-width':22},g);
 el('rect',{x:-170,y:-100,width:340,height:230,rx:30,fill:'#0B4A50',stroke:'#2FBF9B','stroke-width':8},g);
 el('rect',{x:-170,y:-10,width:340,height:20,fill:'#2FBF9B',opacity:.5},g);
 el('rect',{x:-26,y:-24,width:52,height:48,rx:10,fill:AMB},g);return g;}
function stopSign(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 const pts=[];for(let i=0;i<8;i++){const a=Math.PI/8+i*Math.PI/4;pts.push((Math.cos(a)*140).toFixed(1)+','+(Math.sin(a)*140).toFixed(1));}
 el('polygon',{points:pts.join(' '),fill:'#E4412C',stroke:'#fff','stroke-width':10},g);
 txt(g,'STOP',0,26,76,'#fff','900');return g;}
function sticky(p,l1,l2){const g=el('g',{filter:'url(#g_sh)'},p);
 el('rect',{x:-330,y:-200,width:660,height:400,rx:14,fill:'#FFE680'},g);
 txt(g,l1,0,-40,86,'#5A3300','900');txt(g,l2,0,70,50,'#7A4A00','900');
 el('circle',{cx:0,cy:-200,r:30,fill:'#E4412C',stroke:'#fff','stroke-width':6},g);return g;}
function magnifier(p){const g=el('g',{},p);
 el('line',{x1:100,y1:100,x2:230,y2:230,stroke:'#0A3F45','stroke-width':44,'stroke-linecap':'round'},g);
 el('line',{x1:100,y1:100,x2:230,y2:230,stroke:'url(#g_metal)','stroke-width':30,'stroke-linecap':'round'},g);
 el('circle',{r:140,fill:'#E9FBF6',opacity:.9},g);el('circle',{r:140,fill:'none',stroke:'url(#g_metal)','stroke-width':26},g);return g;}
function medalS(p,f,s){const g=el('g',{transform:'scale('+s+')'},p);medal(g,f);return g;}
// =================== BLOCCO 6 ===================
BLK[6]={D:10.13,S:[
{s:0,e:4.3,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'DAL 2028');
 o.cal=calendarPage(g,'GENNAIO','1',320,'2028');
 o.p=el('g',{},g);o.pl=plate(o.p,'67','ANNI');o.dr=dotsRow(o.p,12,225);
 o.chip=el('g',{},g);chip(o.chip,'+3 MESI',340);
 o.sq=el('g',{},g);o.sqs=[];for(let i=0;i<20;i++)o.sqs.push(el('rect',{x:-380+i*38,y:0,width:32,height:44,rx:8,fill:'#0A3F45',opacity:.6,stroke:LT,'stroke-width':2},o.sq));
 o.lab=el('g',{},g);pill(o.lab,'CONTRIBUTI: RESTANO 20 ANNI',900,52,'#2FBF9B');
 o.c1=el('g',{},g);cap(o.c1,'DAL 2028: 67 ANNI E 3 MESI',56);o.c2=el('g',{},g);cap(o.c2,'I CONTRIBUTI RESTANO 20 ANNI',56);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 const p=eob(seg(t,0.1,0.8));T(o.cal.g,480,lerp(-700,170,p),t>0.9?5*Math.exp(-2.4*(t-0.9))*Math.sin(8*(t-0.9)):0,0.95);
 T(o.p,1340,350,0,1.35*Math.max(0,eob(seg(t,0.5,1.2))));op(o.dr.g,seg(t,0.9,1.4));
 o.pl.s.textContent='ANNI E 3 MESI';o.pl.s.setAttribute('font-size',34);
 [0,1,2].forEach(i=>lightDot(o.dr.a[i],t>1.2+i*0.35,seg(t,1.2+i*0.35,1.7+i*0.35)));
 T(o.chip,1640,150,8,Math.max(0,eob(seg(t,1.1,1.8))));
 T(o.sq,960,850,0,Math.max(0,eob(seg(t,2.7,3.2))));
 o.sqs.forEach((q,i)=>{const on=t>3.0+i*0.04;q.setAttribute('fill',on?'#2FBF9B':'#0A3F45');q.setAttribute('opacity',on?1:.6);});
 T(o.lab,960,775,0,Math.max(0,eob(seg(t,2.9,3.5))));
 op(o.c1,t<2.7?1:0);op(o.c2,t>=2.7?1:0);T(o.c1,960,950,0,1);T(o.c2,960,950,0,1);}},
{s:4.3,e:10.13,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LO DICE LA CIRCOLARE');
 o.doc=el('g',{},g);docO(o.doc,560,720,'CIRCOLARE','N. 28','16 MARZO 2026');
 o.seal=el('g',{},g);sealO(o.seal,95);
 o.bub=el('g',{},g);const bb=el('g',{},o.bub);el('rect',{x:-200,y:-90,width:400,height:180,rx:60,fill:'#fff',filter:'url(#g_sh2)'},bb);txt(bb,'VOCI?',0,34,100,INK,'900');
 o.x=el('g',{},g);el('line',{x1:-230,y1:-110,x2:230,y2:110,stroke:'#E4412C','stroke-width':22,'stroke-linecap':'round'},o.x);el('line',{x1:-230,y1:110,x2:230,y2:-110,stroke:'#E4412C','stroke-width':22,'stroke-linecap':'round'},o.x);
 o.ok=el('g',{},g);pill(o.ok,'UFFICIALI!',620,92,'#2FBF9B');
 o.ck=el('g',{},g);checkBadge(o.ck,90);
 o.cap=el('g',{},g);cap(o.cap,'CIRCOLARE INPS N. 28 DEL 16 MARZO 2026',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.doc,520,520,-2,Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.seal,720,760,-12,Math.max(0,eob(seg(t,1.6,2.3))));
 T(o.bub,1380,330,-3,Math.max(0,eob(seg(t,3.4,4.0))));T(o.x,1380,330,0,Math.max(0,eob(seg(t,4.1,4.5))));op(o.x,seg(t,4.1,4.4));
 T(o.ok,1380,640,-4,Math.max(0,eob(seg(t,4.8,5.4))));
 T(o.ck,1700,640,0,Math.max(0,eob(seg(t,5.0,5.6))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.4,1.0))));}}
]};
// =================== BLOCCO 7 ===================
BLK[7]={D:15.5,S:[
{s:0,e:5.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PERCHÉ SALE?');
 o.q=el('g',{},g);qBubble(o.q,160);
 o.gr=el('g',{},g);
 el('rect',{x:-380,y:-290,width:760,height:580,rx:36,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.gr);
 txt(o.gr,'SPERANZA DI VITA',0,-215,50,INK,'900');
 el('line',{x1:-310,y1:210,x2:310,y2:210,stroke:'#6F878C','stroke-width':6},o.gr);el('line',{x1:-310,y1:210,x2:-310,y2:-150,stroke:'#6F878C','stroke-width':6},o.gr);
 o.line=el('path',{d:'M-300 170 L-190 130 L-70 90 L50 30 L170 -30 L290 -110',fill:'none',stroke:'#2FBF9B','stroke-width':16,'stroke-linecap':'round','stroke-linejoin':'round','stroke-dasharray':'800','stroke-dashoffset':'800'},o.gr);
 o.pts=[[-300,170],[-190,130],[-70,90],[50,30],[170,-30],[290,-110]].map(q=>el('circle',{cx:q[0],cy:q[1],r:14,fill:AMB,stroke:'#fff','stroke-width':4,opacity:0},o.gr));
 o.loop=el('g',{},g);el('circle',{r:130,fill:'#06303A',stroke:AMB,'stroke-width':14,filter:'url(#g_sh2)'},o.loop);txt(o.loop,'2',0,28,110,'#fff','900');txt(o.loop,'ANNI',0,82,36,LT,'900');
 o.arc=el('path',{d:'M0 -156 A156 156 0 1 1 -110 110',fill:'none',stroke:LT,'stroke-width':12,'stroke-linecap':'round'},o.loop);
 o.ev=el('g',{},g);pill(o.ev,'OGNI 2 ANNI',560,60);
 o.up=el('g',{},g);pill(o.up,'ETÀ PENSIONABILE ▲',720,60,'#E4412C');
 o.cap=el('g',{},g);cap(o.cap,"OGNI 2 ANNI L'ETÀ SI ADEGUA ALLA SPERANZA DI VITA",50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 const qs=eob(seg(t,0.1,0.7));T(o.q,lerp(960,1650,eio(seg(t,0.8,1.5))),lerp(430,170,eio(seg(t,0.8,1.5))),8*Math.sin(t*4),Math.max(0,qs)*lerp(1,0.5,eio(seg(t,0.8,1.5))));
 T(o.gr,520,500,-2,Math.max(0,eob(seg(t,0.9,1.6))));
 o.line.setAttribute('stroke-dashoffset',800-800*eio(seg(t,1.6,3.6)));
 o.pts.forEach((c,i)=>{op(c,t>1.8+i*0.35?1:0);});
 T(o.loop,1400,370,0,Math.max(0,eob(seg(t,2.6,3.3))));o.arc.setAttribute('transform','rotate('+(t*90)+')');
 T(o.ev,1400,590,-3,Math.max(0,eob(seg(t,3.0,3.6))));
 T(o.up,1400,740,2,Math.max(0,eob(seg(t,4.2,4.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.8,1.4))));}},
{s:5.6,e:10.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LEGGE DI BILANCIO 2026');
 o.doc=el('g',{},g);docO(o.doc,560,720,'LEGGE DI BILANCIO','2026','NOVITÀ PENSIONI');
 o.st=el('g',{},g);pill(o.st,'GRADUALMENTE',640,70,'#2FBF9B');
 o.stairs=el('g',{},g);o.steps=[0,1,2].map(i=>{const h=120+i*110;return {r:el('rect',{x:i*190-285,y:230-h,width:170,height:h,rx:18,fill:i==2?'url(#g_badge)':'#CFE9E3',stroke:'#fff','stroke-width':4},o.stairs),h};});
 o.cap=el('g',{},g);cap(o.cap,'LA LEGGE DI BILANCIO 2026: AUMENTO GRADUALE',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.doc,520,520,-2,Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.st,520,540,-10,Math.max(0,eob(seg(t,1.8,2.5))));
 T(o.stairs,1400,500,0,1);
 o.steps.forEach((s,i)=>{const k=eob(seg(t,2.4+i*0.55,2.9+i*0.55));s.r.setAttribute('transform','translate(0,230) scale(1,'+Math.max(0,k)+') translate(0,-230)');});
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.4,1.0))));}},
{s:10.4,e:15.5,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'COSA CAMBIA');
 o.c1=calendarPage(g,'ANNO','2027',150,'');o.c2=calendarPage(g,'ANNO','2028',150,'');
 o.k1=el('g',{},g);chip(o.k1,'+1 MESE',320);o.k2=el('g',{},g);chip(o.k2,'+2 MESI',320);
 o.ar=el('g',{},g);el('path',{d:'M-60 0 L60 0 M30 -30 L60 0 L30 30',fill:'none',stroke:'#fff','stroke-width':14,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.tot=el('g',{},g);el('circle',{r:170,fill:'url(#g_badge)',stroke:'#fff','stroke-width':12,filter:'url(#g_sh)'},o.tot);txt(o.tot,'3',0,30,150,'#fff','900');txt(o.tot,'IN TUTTO',0,98,36,'#fff','900');
 o.dr=dotsRow(g,12,0);
 o.cap=el('g',{},g);cap(o.cap,'1 MESE NEL 2027, 2 MESI NEL 2028: IN TUTTO 3 MESI',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.c1.g,420,170,0,0.9*Math.max(0,eob(seg(t,0.2,0.9))));T(o.c2.g,980,170,0,0.9*Math.max(0,eob(seg(t,2.4,3.1))));
 T(o.ar,700,430,0,Math.max(0,eob(seg(t,2.2,2.8))));
 T(o.k1,420,690,-3,Math.max(0,eob(seg(t,1.0,1.7))));T(o.k2,980,690,3,Math.max(0,eob(seg(t,3.2,3.9))));
 T(o.tot,1590,420,0,Math.max(0,eob(seg(t,3.9,4.6))));
 o.dr.g.setAttribute('transform','translate(960 850)');
 lightDot(o.dr.a[0],t>1.4,seg(t,1.4,1.9));lightDot(o.dr.a[1],t>3.5,seg(t,3.5,4.0));lightDot(o.dr.a[2],t>3.8,seg(t,3.8,4.3));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 8 ===================
BLK[8]={D:20.23,S:[
{s:0,e:3.9,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PENSIONE ANTICIPATA');
 o.a=el('g',{},g);
 el('rect',{x:-290,y:-300,width:580,height:600,rx:36,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.a);txt(o.a,'ETÀ',0,-170,100,INK,'900');
 const cal=el('g',{transform:'translate(0 20)'},o.a);el('rect',{x:-100,y:-100,width:200,height:200,rx:24,fill:'#EAF7F4',stroke:'#C9D6D8','stroke-width':6},cal);txt(cal,'67',0,30,100,'#6F878C','900');
 o.x=el('g',{},g);el('line',{x1:-250,y1:-250,x2:250,y2:250,stroke:'#E4412C','stroke-width':34,'stroke-linecap':'round'},o.x);el('line',{x1:-250,y1:250,x2:250,y2:-250,stroke:'#E4412C','stroke-width':34,'stroke-linecap':'round'},o.x);
 o.b=el('g',{},g);
 el('rect',{x:-290,y:-300,width:580,height:600,rx:36,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.b);txt(o.b,'CONTRIBUTI',0,-190,54,INK,'900');
 for(let i=0;i<4;i++){const c=el('g',{transform:'translate('+(-120+i*80)+' '+(120-i*45)+')'},o.b);el('rect',{x:-34,y:-110,width:68,height:230,rx:12,fill:'#2FBF9B'},c);}
 o.ck=el('g',{},g);checkBadge(o.ck,90);
 o.cap=el('g',{},g);cap(o.cap,'CONTA SOLO IL NUMERO DI ANNI DI CONTRIBUTI',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.a,520,500,-3,Math.max(0,eob(seg(t,0.1,0.8))));T(o.x,520,500,0,Math.max(0,eob(seg(t,0.9,1.5))));op(o.x,seg(t,0.9,1.3));
 T(o.b,1400,500,3,Math.max(0,eob(seg(t,1.5,2.2))));T(o.ck,1700,260,0,Math.max(0,eob(seg(t,2.4,3.0))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:3.9,e:20.23,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ANNI DI CONTRIBUTI NECESSARI');
 o.tb=el('g',{},g);el('rect',{x:-880,y:-330,width:1760,height:640,rx:40,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.tb);
 o.mm=el('g',{},o.tb);const m1=el('g',{transform:'translate(0 -255)'},o.mm);medalS(m1,false,0.3);txt(o.mm,'UOMINI',0,-175,44,INK,'900');
 const m2=el('g',{transform:'translate(560 -255)'},o.mm);medalS(m2,true,0.3);txt(o.mm,'DONNE',560,-175,44,INK,'900');
 el('rect',{x:-820,y:-140,width:1640,height:6,rx:3,fill:'#C9D6D8'},o.tb);
 o.rows=[['OGGI','42 anni e 10 mesi','41 anni e 10 mesi','#2FBF9B',-60],['DAL 2027','42 anni e 11 mesi','41 anni e 11 mesi','#E09A1A',80],['DAL 2028','43 anni e 1 mese','42 anni e 1 mese','#E4412C',220]].map(r=>{
  const w=el('g',{},o.tb);el('rect',{x:-840,y:r[4]-55,width:1680,height:120,rx:26,fill:r[3],opacity:0.14},w);
  const lb=el('g',{transform:'translate(-640 '+r[4]+')'},w);pill(lb,r[0],300,44,r[3]);
  txt(w,r[1],0,r[4]+16,46,INK,'900');txt(w,r[2],560,r[4]+16,46,INK,'900');return w;});
 o.cs=[cap(g,'OGGI: 42 ANNI E 10 MESI / 41 ANNI E 10 MESI',54),cap(g,'DAL 2027: 42 ANNI E 11 MESI / 41 ANNI E 11 MESI',54),cap(g,'DAL 2028: 43 ANNI E 1 MESE / 42 ANNI E 1 MESE',54)];
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.tb,960,490,0,Math.max(0,eob(seg(t,0.1,0.8)))*0.95);
 const tm=[0.4,5.6,10.7];
 o.rows.forEach((r,i)=>{op(r,seg(t,tm[i],tm[i]+0.5));});
 const idx=t<tm[1]?0:(t<tm[2]?1:2);
 o.cs.forEach((c,i)=>{op(c,i===idx?1:0);T(c,960,950,0,1);});}}
]};
// =================== BLOCCO 9 ===================
BLK[9]={D:16.27,S:[
{s:0,e:2.9,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ATTENZIONE');
 o.w=el('g',{},g);warn(o.w);
 o.m=el('g',{},g);magnifier(o.m);txt(o.m,'!',0,44,130,'#E4412C','900');
 o.cap=el('g',{},g);cap(o.cap,'ATTENZIONE A UN DETTAGLIO CHE MOLTI DIMENTICANO',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.w,640,500,0,1.5*Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.m,1300,430,0,Math.max(0,eob(seg(t,0.7,1.4)))*(1+0.03*Math.sin(t*5)));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:2.9,e:8.5,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA FINESTRA DI TRE MESI');
 o.fl=el('g',{},g);o.line=el('rect',{x:-700,y:-8,width:1400,height:16,rx:8,fill:'#0A3F45',stroke:LT,'stroke-width':3},g);
 o.flag=el('g',{},g);el('line',{x1:0,y1:0,x2:0,y2:-190,stroke:'#fff','stroke-width':10,'stroke-linecap':'round'},o.flag);el('path',{d:'M0 -190 L130 -150 L0 -110 Z',fill:'#2FBF9B'},o.flag);
 o.fl2=txt(g,'CONTRIBUTI MATURATI',0,0,36,'#fff','900');
 o.cals=[0,1,2].map(i=>{const c=el('g',{},g);el('rect',{x:-95,y:-95,width:190,height:190,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh2)'},c);el('rect',{x:-95,y:-95,width:190,height:56,rx:26,fill:'url(#g_head)'},c);el('rect',{x:-95,y:-60,width:190,height:21,fill:'url(#g_head)'},c);txt(c,'MESE',0,-52,34,'#fff','900');txt(c,''+(i+1),0,60,90,INK,'900');return c;});
 o.coin=el('g',{},g);coinA(o.coin,100);o.pp=el('g',{},g);pill(o.pp,'LA PENSIONE PARTE',640,54,'#2FBF9B');
 o.cap=el('g',{},g);cap(o.cap,'DOPO I CONTRIBUTI: UNA FINESTRA DI TRE MESI',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.line,960,540,0,1);
 T(o.flag,300,540,0,Math.max(0,eob(seg(t,0.1,0.7))));o.fl2.setAttribute('transform','translate(300 620)');op(o.fl2,seg(t,0.4,0.9));
 o.cals.forEach((c,i)=>{T(c,640+i*270,420,(i-1)*3,Math.max(0,eob(seg(t,0.8+i*1.0,1.4+i*1.0))));});
 T(o.coin,1640,430,0,Math.max(0,eob(seg(t,3.9,4.6)))*(1+0.04*Math.sin(t*6)));
 T(o.pp,1500,690,-3,Math.max(0,eob(seg(t,4.2,4.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:8.5,e:13.3,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LAVORATORE DIPENDENTE');
 o.b=el('g',{},g);briefcase(o.b);
 o.bl=el('g',{},g);pill(o.bl,'LAVORO DIPENDENTE',620,54);
 o.ar=el('g',{},g);el('path',{d:'M-90 0 L90 0 M50 -45 L90 0 L50 45',fill:'none',stroke:'#fff','stroke-width':18,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.s=el('g',{},g);stopSign(o.s);
 o.coin=el('g',{},g);coinA(o.coin,90);
 o.sl=el('g',{},g);pill(o.sl,'SMETTI DI LAVORARE',700,54,'#E4412C');
 o.cap=el('g',{},g);cap(o.cap,'PER INCASSARLA DEVI AVER SMESSO DI LAVORARE',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.b,460,430,-4,1.3*Math.max(0,eob(seg(t,0.1,0.8))));T(o.bl,460,690,-2,Math.max(0,eob(seg(t,0.6,1.3))));
 T(o.ar,960,440,0,Math.max(0,eob(seg(t,1.2,1.8))));
 T(o.s,1380,420,0,1.2*Math.max(0,eob(seg(t,1.8,2.5))));T(o.sl,1380,690,3,Math.max(0,eob(seg(t,2.4,3.1))));
 T(o.coin,1700,250,0,Math.max(0,eob(seg(t,3.3,3.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:13.3,e:16.27,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TIENILO A MENTE');
 o.n=el('g',{},g);sticky(o.n,'RICORDA!','3 MESI DI FINESTRA');txt(o.n,'+ SMETTERE DI LAVORARE',0,150,40,'#7A4A00','900');
 o.q=el('g',{},g);qBubble(o.q,90);
 o.cap=el('g',{},g);cap(o.cap,'TIENILO A MENTE... TRA POCO TI SERVIRÀ!',56);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.n,960,470,-4+2*Math.sin(t*3),1.2*Math.max(0,eob(seg(t,0.1,0.9))));
 T(o.q,1560,250,10*Math.sin(t*4),Math.max(0,eob(seg(t,1.4,2.0))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 10 ===================
BLK[10]={D:9.97,S:[
{s:0,e:5.3,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA DOMANDA');
 o.sg=el('g',{},g);el('rect',{x:-260,y:-120,width:520,height:240,rx:36,fill:'url(#g_badge)',stroke:'#fff','stroke-width':12,filter:'url(#g_sh)'},o.sg);txt(o.sg,'64',-80,46,150,'#fff','900');txt(o.sg,'ANNI',120,36,56,'#fff','900');
 o.q=el('g',{},g);qBubble(o.q,150);
 o.m=el('g',{},g);medal(o.m,false);
 o.yes=el('g',{},g);pill(o.yes,'ESISTE',420,60,'#2FBF9B');o.no=el('g',{},g);pill(o.no,'NON ESISTE',560,60,'#E4412C');
 o.cap=el('g',{},g);cap(o.cap,'QUESTA PENSIONE A 64 ANNI ESISTE O NO?',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.m,360,420,0,0.85*Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.sg,960,360,0,Math.max(0,eob(seg(t,0.5,1.2))));
 T(o.q,1560,350,10*Math.sin(t*4),Math.max(0,eob(seg(t,1.2,1.9))));
 T(o.yes,780,690,-3,Math.max(0,eob(seg(t,2.2,2.9))));T(o.no,1260,690,3,Math.max(0,eob(seg(t,2.8,3.5))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:5.3,e:6.8,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA RISPOSTA');
 o.ck=el('g',{},g);checkBadge(o.ck,200);
 o.st=el('g',{},g);pill(o.st,'SÌ! È LEGGE!',900,110,'#2FBF9B');
 o.sp=ring(g,200);
 o.cap=el('g',{},g);cap(o.cap,'SÌ, ESISTE! È LEGGE!',60);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.ck,960,380,0,Math.max(0,eob(seg(t,0.05,0.5))));
 T(o.st,960,700,-3,Math.max(0,eob(seg(t,0.3,0.8))));
 const rr=seg(t,0.1,0.8);o.sp.setAttribute('r',lerp(100,420,rr));o.sp.setAttribute('opacity',(1-rr)*0.8);T(o.sp,960,380,0,1);
 T(o.cap,960,950,0,1);}},
{s:6.8,e:9.97,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL TRUCCO');
 o.k=[0,1,2].map(i=>{const c=el('g',{},g);el('circle',{r:150,fill:'url(#g_paper)',filter:'url(#g_sh)'},c);el('circle',{r:150,fill:'none',stroke:['#2FBF9B','#E09A1A','#E4412C'][i],'stroke-width':14},c);txt(c,''+(i+1),0,60,170,INK,'900');const lk=el('g',{transform:'translate(100 100) scale(0.5)'},c);lockO(lk);return c;});
 o.cap=el('g',{},g);cap(o.cap,"C'È UN TRUCCO: TRE CONDIZIONI",58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 [440,960,1480].forEach((x,i)=>{T(o.k[i],x,480,(i-1)*4,Math.max(0,eob(seg(t,0.5+i*0.6,1.1+i*0.6)))*1.2);});
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.2,0.8))));}}
]};
