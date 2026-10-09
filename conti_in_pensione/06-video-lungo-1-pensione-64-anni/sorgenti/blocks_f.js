// =================== BLOCCO 26 ===================
function calcO(p,label,col){const g=el('g',{},p);
 el('rect',{x:-190,y:-260,width:380,height:520,rx:44,fill:'#0A2B30',stroke:'#7FA9AE','stroke-width':8,filter:'url(#g_sh)'},g);
 el('rect',{x:-155,y:-225,width:310,height:110,rx:18,fill:'#BFEFE3'},g);
 for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('rect',{x:-155+c*105,y:-90+r*105,width:95,height:90,rx:18,fill:'#17383D'},g);
 const pl=el('g',{transform:'translate(0 330)'},g);pill(pl,label,520,48,col);return g;}
BLK[26]={D:16.27,S:[
{s:0,e:5.5,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'SECONDA PROPOSTA');
 o.door=el('g',{},g);door(o.door);
 o.sg=el('g',{},g);el('rect',{x:-260,y:-100,width:520,height:200,rx:36,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.sg);txt(o.sg,'64 ANNI',0,34,100,'#fff','900');
 o.tl=el('g',{},g);el('rect',{x:-380,y:-6,width:760,height:12,rx:6,fill:'#fff',opacity:.85},o.tl);el('rect',{x:-380,y:-60,width:290,height:120,rx:16,fill:'#E4412C',opacity:.3},o.tl);el('rect',{x:-90,y:-60,width:470,height:120,rx:16,fill:'#2FBF9B',opacity:.3},o.tl);
 el('rect',{x:-94,y:-90,width:8,height:180,rx:4,fill:AMB},o.tl);txt(o.tl,'1996',-90,-110,40,AMB,'900');
 o.c=el('g',{},g);coinA(o.c,46);
 o.ck=el('g',{},g);checkBadge(o.ck,80);
 o.cap=el('g',{},g);cap(o.cap,"SECONDA PROPOSTA: L'USCITA A 64 ANNI ANCHE PER CHI HA CONTRIBUTI PRIMA DEL 1996",44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.door,480,520,0,0.9*Math.max(0,eob(seg(t,0.1,0.8))));T(o.sg,480,230,0,Math.max(0,eob(seg(t,0.4,1.1))));
 T(o.tl,1330,520,0,Math.max(0,eob(seg(t,1.4,2.1))));T(o.c,1330-230,520,0,Math.max(0,eob(seg(t,2.4,3.0))));
 T(o.ck,1700,300,0,Math.max(0,eob(seg(t,3.6,4.2))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:5.5,e:9.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'BELLA NOTIZIA?');
 o.m=el('g',{},g);medal(o.m,false);o.q=el('g',{},g);qBubble(o.q,120);
 o.a=el('g',{},g);card3(o.a,'BELLA NOTIZIA?','#2FBF9B',620,160);o.b=el('g',{},g);card3(o.b,'DIPENDE...','#E09A1A',620,160);
 o.cap=el('g',{},g);cap(o.cap,'BELLA NOTIZIA? DIPENDE...',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.m,460,470,0,1.1*Math.max(0,eob(seg(t,0.1,0.8))));T(o.q,760,260,10*Math.sin(t*4),Math.max(0,eob(seg(t,0.5,1.1))));
 T(o.a,1380,360,-3,Math.max(0,eob(seg(t,0.8,1.4))));T(o.b,1380,600,3,Math.max(0,eob(seg(t,1.8,2.4))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:9.0,e:16.27,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL RICALCOLO');
 o.c1=el('g',{},g);calcO(o.c1,'METODO MISTO','#6F878C');o.c2=el('g',{},g);calcO(o.c2,'TUTTO CONTRIBUTIVO','#E4412C');
 o.ar=el('g',{},g);el('path',{d:'M-90 0 L90 0 M50 -45 L90 0 L50 45',fill:'none',stroke:'#fff','stroke-width':18,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.s1=el('g',{},g);const a=slipCard(o.s1,'ASSEGNO','€ 1.800');a.amt.setAttribute('font-size',70);
 o.s2=el('g',{},g);const b=slipCard(o.s2,'ASSEGNO','€ 1.600');b.amt.setAttribute('font-size',70);
 o.dn=el('g',{},g);el('path',{d:'M0 -60 L0 60 M-50 10 L0 66 L50 10',fill:'none',stroke:'#E4412C','stroke-width':26,'stroke-linecap':'round','stroke-linejoin':'round'},o.dn);
 o.lo=el('g',{},g);pill(o.lo,'PENSIONE PIÙ BASSA',720,60,'#E4412C');
 o.cap=el('g',{},g);cap(o.cap,'RICALCOLO TUTTO CONTRIBUTIVO: IN GENERE UNA PENSIONE PIÙ BASSA',46);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.c1,330,500,-2,0.7*Math.max(0,eob(seg(t,0.2,0.9))));T(o.c2,1000,500,2,0.7*Math.max(0,eob(seg(t,2.0,2.7))));
 T(o.ar,660,420,0,Math.max(0,eob(seg(t,1.6,2.2))));
 T(o.s1,330,200,-3,0.55*Math.max(0,eob(seg(t,1.0,1.7))));T(o.s2,1000,240+seg(t,3.6,4.6)*80,3,0.55*Math.max(0,eob(seg(t,3.0,3.7))));
 T(o.dn,1620,430,0,Math.max(0,eob(seg(t,4.2,4.9))));T(o.lo,1480,720,-3,Math.max(0,eob(seg(t,4.8,5.5))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 27 ===================
function cgilBadge(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-330,y:-110,width:660,height:220,rx:34,fill:'#E4412C',stroke:'#fff','stroke-width':10},g);txt(g,'CGIL',-130,26,100,'#fff','900');txt(g,'OSSERVATORIO',130,-10,34,'#fff','900');txt(g,'PREVIDENZA',130,40,34,'#fff','900');return g;}
function donut(p,pct,col,label){const g=el('g',{},p);const r=150,c=2*Math.PI*r;
 el('circle',{r:r,fill:'none',stroke:'#0A3F45','stroke-width':44},g);
 const a=el('circle',{r:r,fill:'none',stroke:col,'stroke-width':44,'stroke-dasharray':c+' '+c,'stroke-dashoffset':c,transform:'rotate(-90)','stroke-linecap':'round'},g);
 const t=txt(g,'',0,26,92,'#fff','900');txt(g,label,0,96,34,LT,'900');return {g,a,t,c};}
BLK[27]={D:11.9,S:[
{s:0,e:3.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'QUANTO PIÙ BASSA?');
 o.q=el('g',{},g);qBubble(o.q,150);o.c=el('g',{},g);cgilBadge(o.c);
 o.cap=el('g',{},g);cap(o.cap,"QUANTO PIÙ BASSA? SECONDO L'OSSERVATORIO PREVIDENZA DELLA CGIL",48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.q,560,470,10*Math.sin(t*4),Math.max(0,eob(seg(t,0.1,0.8))));T(o.c,1280,470,-2,Math.max(0,eob(seg(t,0.9,1.6))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:3.6,e:11.9,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'STIPENDIO DI 35 MILA EURO');
 o.pay=el('g',{},g);
 el('rect',{x:-250,y:-290,width:500,height:580,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.pay);el('rect',{x:-250,y:-290,width:500,height:84,rx:26,fill:'url(#g_head)'},o.pay);el('rect',{x:-250,y:-250,width:500,height:44,fill:'url(#g_head)'},o.pay);
 txt(o.pay,'STIPENDIO',0,-230,46,'#fff');txt(o.pay,'€ 35.000',0,-90,86,INK,'900');txt(o.pay,'L’ANNO',0,-30,40,GRN,'900');
 for(let i=0;i<4;i++)el('rect',{x:-190,y:30+i*58,width:380-(i%2)*80,height:16,rx:8,fill:'#C9D6D8'},o.pay);
 o.big=el('g',{},g);o.num=txt(o.big,'',0,0,190,'#FF6A55','900');o.un=txt(o.big,'AL MESE IN MENO',0,100,60,'#fff','900');
 o.d=donut(g,10.6,'#E4412C','DEL 100%');
 o.cap=el('g',{},g);cap(o.cap,'35 MILA EURO DI STIPENDIO: CIRCA 182 EURO IN MENO, IL 10,6%',48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.pay,480,470,-3,Math.max(0,eob(seg(t,0.1,0.8))));
 const v=Math.round(eio(seg(t,1.0,3.0))*182);o.num.textContent=t>1.0?('− '+v+' €'):'';
 T(o.big,1330,330,0,Math.max(0,eob(seg(t,0.8,1.5))));
 T(o.d.g,1330,720,0,0.8*Math.max(0,eob(seg(t,3.0,3.7))));
 const k=eio(seg(t,3.4,5.4));o.d.a.setAttribute('stroke-dashoffset',o.d.c*(1-0.106*k*4));
 o.d.t.textContent=Math.round(k*106)/10+'%'.replace('.',',');o.d.t.textContent=(Math.round(k*106)/10).toString().replace('.',',')+'%';
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 28 ===================
BLK[28]={D:11.14,S:[
{s:0,e:3.9,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'STIPENDIO DI 50 MILA EURO');
 o.pay=el('g',{},g);docO(o.pay,480,600,'BUSTA PAGA','€ 50.000','L’ANNO');
 o.big=el('g',{},g);o.num=txt(o.big,'',0,0,190,'#FF6A55','900');txt(o.big,'AL MESE IN MENO',0,100,56,'#fff','900');
 o.cap=el('g',{},g);cap(o.cap,'CON 50 MILA EURO: CIRCA 261 EURO',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.pay,500,470,-3,Math.max(0,eob(seg(t,0.1,0.8))));
 o.num.textContent=t>0.8?('− '+Math.round(eio(seg(t,0.8,2.6))*261)+' €'):'';T(o.big,1330,450,0,Math.max(0,eob(seg(t,0.6,1.3))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:3.9,e:7.5,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'STIPENDIO DI 70 MILA EURO');
 o.pay=el('g',{},g);docO(o.pay,480,600,'BUSTA PAGA','€ 70.000','L’ANNO');
 o.big=el('g',{},g);o.num=txt(o.big,'',0,0,170,'#FF6A55','900');txt(o.big,'AL MESE IN MENO',0,100,56,'#fff','900');
 o.cap=el('g',{},g);cap(o.cap,'CON 70 MILA: OLTRE 365 EURO AL MESE!',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.pay,500,470,-3,Math.max(0,eob(seg(t,0.1,0.8))));
 o.num.textContent=t>0.8?('− '+Math.round(eio(seg(t,0.8,2.4))*365)+'+ €'):'';T(o.big,1330,450,0,Math.max(0,eob(seg(t,0.6,1.3))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:7.5,e:11.14,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ATTENZIONE');
 o.c=el('g',{},g);cgilBadge(o.c);
 o.st=el('g',{},g);el('rect',{x:-390,y:-80,width:780,height:160,rx:20,fill:'none',stroke:'#E09A1A','stroke-width':14},o.st);txt(o.st,'PROPOSTA NON DEFINITA',0,22,54,'#E09A1A','900');
 o.q=el('g',{},g);qBubble(o.q,90);
 o.cap=el('g',{},g);cap(o.cap,'SONO STIME DI UN SINDACATO, SU UNA PROPOSTA ANCORA NON DEFINITA',48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.c,960,350,-2,Math.max(0,eob(seg(t,0.1,0.8))));T(o.st,960,640,-3,Math.max(0,eob(seg(t,1.0,1.7)))*(t>1.7?1+0.03*Math.sin((t-1.7)*7):1));
 T(o.q,1560,330,10*Math.sin(t*4),Math.max(0,eob(seg(t,1.8,2.4))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 29 ===================
BLK[29]={D:19.27,S:[
{s:0,e:6.5,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TERZA PROPOSTA');
 o.p=el('g',{},g);o.pl=plate(o.p,'41','ANNI DI CONTRIBUTI');o.pl.s.setAttribute('font-size',28);
 o.ages=el('g',{},g);o.ag=[55,58,61,64,67].map((a,i)=>{const c=el('g',{},o.ages);el('rect',{x:-90,y:-60,width:180,height:120,rx:24,fill:'url(#g_paper)',filter:'url(#g_sh2)'},c);txt(c,'ETÀ',0,-14,28,GRN,'900');txt(c,'?',0,44,64,INK,'900');return c;});
 o.pr=el('g',{},g);pill(o.pr,'QUOTA 41 PER TUTTI',760,60,'#E09A1A');
 o.cap=el('g',{},g);cap(o.cap,'TERZA PROPOSTA: LA QUOTA 41 PER TUTTI, A QUALSIASI ETÀ',48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.p,700,380,0,1.3*Math.max(0,eob(seg(t,0.1,0.8))));
 o.ag.forEach((c,i)=>T(c,420+i*270,720,(i-2)*3,Math.max(0,eob(seg(t,1.8+i*0.4,2.4+i*0.4)))));
 T(o.ages,0,0,0,1);T(o.pr,1480,560,3,Math.max(0,eob(seg(t,1.2,1.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:6.5,e:12.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'MA MANCA QUALCOSA');
 o.bp=el('g',{},g);docO(o.bp,500,640,'PROGETTO','TECNICO','NON ANCORA');
 o.x1=el('g',{},g);el('line',{x1:-220,y1:-260,x2:220,y2:260,stroke:'#E4412C','stroke-width':26,'stroke-linecap':'round'},o.x1);el('line',{x1:-220,y1:260,x2:220,y2:-260,stroke:'#E4412C','stroke-width':26,'stroke-linecap':'round'},o.x1);
 o.pg=el('g',{},g);piggy(o.pg);o.q=el('g',{},g);txt(o.q,'0',0,30,140,'#fff','900');
 o.l1=el('g',{},g);pill(o.l1,'NESSUN PROGETTO TECNICO',700,48,'#E4412C');o.l2=el('g',{},g);pill(o.l2,'NESSUN SOLDO',560,48,'#E4412C');
 o.cap=el('g',{},g);cap(o.cap,"NON C'È ANCORA UN PROGETTO TECNICO NÉ I SOLDI PER FINANZIARLA",48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.bp,480,450,-3,Math.max(0,eob(seg(t,0.1,0.8))));T(o.x1,480,450,0,Math.max(0,eob(seg(t,1.2,1.8))));op(o.x1,seg(t,1.2,1.6));
 T(o.l1,480,780,-2,Math.max(0,eob(seg(t,1.8,2.4))));
 T(o.pg,1380,450,2,1.0*Math.max(0,eob(seg(t,2.6,3.3))));T(o.q,1380,450,0,Math.max(0,eob(seg(t,3.4,3.9))));
 T(o.l2,1380,780,2,Math.max(0,eob(seg(t,3.8,4.4))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:12.0,e:19.27,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA PENSIONE MINIMA');
 o.s=el('g',{},g);const sc=slipCard(o.s,'MINIMA 2026','€ 611,85');sc.amt.setAttribute('font-size',84);
 o.ar=el('g',{},g);el('path',{d:'M0 60 L0 -60 M-40 -20 L0 -64 L40 -20',fill:'none',stroke:AMB,'stroke-width':22,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.t1=el('g',{},g);card3(o.t1,'€ 700','#E09A1A',380,150);o.t2=el('g',{},g);card3(o.t2,'€ 800','#E09A1A',380,150);
 o.q=el('g',{},g);qBubble(o.q,110);
 o.st=el('g',{},g);pill(o.st,'NULLA È DECISO',640,64,'#06303A');
 o.cap=el('g',{},g);cap(o.cap,'LA MINIMA: 611,85 NEL 2026. SI PARLA DI 700 O 800 EURO, MA NULLA È DECISO',44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.s,520,520,-2,Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.ar,960,520,0,Math.max(0,eob(seg(t,1.8,2.4))));
 T(o.t1,1400,360,-3,Math.max(0,eob(seg(t,2.6,3.2))));T(o.t2,1400,610,3,Math.max(0,eob(seg(t,3.4,4.0))));
 T(o.q,1750,480,10*Math.sin(t*4),Math.max(0,eob(seg(t,4.6,5.2))));
 T(o.st,960,790,-1,Math.max(0,eob(seg(t,5.2,5.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 30 ===================
BLK[30]={D:13.49,S:[
{s:0,e:4.7,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'QUANDO SI DECIDE?');
 o.c1=calendarPage(g,'OTTOBRE','20',320,'ENTRO IL');o.c2=calendarPage(g,'DICEMBRE','31',320,'ENTRO FINE');
 o.ar=el('g',{},g);el('path',{d:'M-80 0 L80 0 M40 -45 L80 0 L40 45',fill:'none',stroke:'#fff','stroke-width':20,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.pr=el('g',{},g);pill(o.pr,'LEGGE DI BILANCIO',720,56,'#2FBF9B');
 o.cap=el('g',{},g);cap(o.cap,'LA LEGGE DI BILANCIO: PRESENTATA ENTRO IL 20 OTTOBRE, APPROVATA ENTRO DICEMBRE',44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.c1.g,420,170,0,1.0*Math.max(0,eob(seg(t,0.1,0.8))));T(o.c2.g,1500,170,0,1.0*Math.max(0,eob(seg(t,1.6,2.3))));
 T(o.ar,960,480,0,Math.max(0,eob(seg(t,1.2,1.8))));T(o.pr,960,800,-1,Math.max(0,eob(seg(t,2.6,3.2))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:4.7,e:8.3,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'POCHE SETTIMANE');
 o.h=el('g',{},g);hourglass(o.h);
 o.cs=[0,1,2,3,4,5].map(i=>{const c=el('g',{},g);el('rect',{x:-70,y:-70,width:140,height:140,rx:22,fill:'url(#g_paper)',filter:'url(#g_sh3)'},c);el('rect',{x:-70,y:-70,width:140,height:40,rx:22,fill:'url(#g_head)'},c);el('rect',{x:-70,y:-46,width:140,height:16,fill:'url(#g_head)'},c);txt(c,'SETT.',0,-40,24,'#fff','900');txt(c,''+(i+1),0,52,60,INK,'900');return c;});
 o.cap=el('g',{},g);cap(o.cap,'LA RISPOSTA ARRIVA TRA POCHE SETTIMANE',56);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.h,480,470,0,1.3*Math.max(0,eob(seg(t,0.1,0.8)))*(1+0.02*Math.sin(t*5)));
 o.cs.forEach((c,i)=>T(c,860+(i%3)*220,360+Math.floor(i/3)*220,(i-2.5)*2,Math.max(0,eob(seg(t,0.8+i*0.3,1.3+i*0.3)))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:8.3,e:13.49,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'L’ERRORE PIÙ PERICOLOSO');
 o.w=el('g',{},g);warn(o.w);
 o.d=el('g',{},g);docO(o.d,420,520,'PROPOSTA','NON LEGGE','');
 o.dec=el('g',{},g);card3(o.dec,'DECISIONE IMPORTANTE','#E4412C',760,160);
 o.ar=el('g',{},g);el('path',{d:'M0 -60 L0 60 M-40 20 L0 64 L40 20',fill:'none',stroke:'#fff','stroke-width':20,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.cap=el('g',{},g);cap(o.cap,"L'ERRORE PIÙ PERICOLOSO: DECIDERE BASANDOSI SU UNA PROPOSTA",48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.w,430,430,0,1.4*Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.d,1050,370,-4,0.8*Math.max(0,eob(seg(t,1.0,1.7))));T(o.ar,1450,560,0,Math.max(0,eob(seg(t,1.8,2.4))));
 T(o.dec,1400,780,2,Math.max(0,eob(seg(t,2.4,3.0))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
