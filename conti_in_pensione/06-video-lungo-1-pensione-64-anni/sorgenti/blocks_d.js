// =================== BLOCCO 16 ===================
function bag(p,s){const g=el('g',{transform:'scale('+s+')'},p);
 el('path',{d:'M-120 140 Q-170 -20 -80 -100 L80 -100 Q170 -20 120 140 Z',fill:'#0B4A50',stroke:'#2FBF9B','stroke-width':10,filter:'url(#g_sh2)'},g);
 el('rect',{x:-90,y:-130,width:180,height:44,rx:18,fill:'#0A3F45',stroke:'#2FBF9B','stroke-width':8},g);
 txt(g,'€',0,70,170,AMB,'900');return g;}
BLK[16]={D:12.93,S:[
{s:0,e:3.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL COEFFICIENTE A 64 ANNI');
 o.b=el('g',{},g);o.bb=card3(o.b,'64 ANNI','#2FBF9B',460,170);
 o.pc=el('g',{},g);el('circle',{r:210,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.pc);el('circle',{r:210,fill:'none',stroke:AMB,'stroke-width':16},o.pc);txt(o.pc,'5,088%',0,34,92,INK,'900');txt(o.pc,'COEFFICIENTE',0,100,32,GRN,'900');
 o.cap=el('g',{},g);cap(o.cap,'CON IL COEFFICIENTE DI OGGI A 64 ANNI: 5,088%',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.b,560,470,-3,Math.max(0,eob(seg(t,0.1,0.8))));T(o.pc,1320,470,0,Math.max(0,eob(seg(t,0.7,1.5)))*(1+0.02*Math.sin(t*5)));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:3.4,e:8.5,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL MONTANTE');
 o.bags=[0,1,2].map(i=>{const c=el('g',{},g);bag(c,1.1);return c;});
 o.big=el('g',{},g);
 el('rect',{x:-420,y:-130,width:840,height:260,rx:40,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.big);
 txt(o.big,'MONTANTE',0,-62,46,'#fff','900');o.num=txt(o.big,'',0,64,100,'#fff','900');
 o.cap=el('g',{},g);cap(o.cap,'SERVE UN MONTANTE DI CIRCA 419 MILA EURO!',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 [380,640,900].forEach((x,i)=>T(o.bags[i],x,430+(i%2)*40,(i-1)*6,Math.max(0,eob(seg(t,0.2+i*0.35,0.8+i*0.35)))));
 T(o.big,1360,480,2,Math.max(0,eob(seg(t,1.5,2.2))));
 o.num.textContent='€ '+Math.round(eio(seg(t,2.0,4.0))*419).toLocaleString('it-IT')+'.000'.replace('.000','.000');
 o.num.textContent='€ '+Math.round(eio(seg(t,2.0,4.0))*419)+' MILA';
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:8.5,e:12.93,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PER TANTI');
 o.doc=el('g',{},g);docO(o.doc,560,700,'PENSIONE','64 ANNI','CONDIZIONE IMPORTO');
 o.st=el('g',{},g);el('rect',{x:-330,y:-70,width:660,height:140,rx:16,fill:'none',stroke:'#E09A1A','stroke-width':14},o.st);txt(o.st,'SULLA CARTA',0,34,88,'#E09A1A','900');
 o.q=el('g',{},g);qBubble(o.q,100);
 o.man=el('g',{},g);medal(o.man,false);
 o.cap=el('g',{},g);cap(o.cap,'PER TANTI LA PENSIONE A 64 ANNI RESTA SULLA CARTA',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.doc,520,490,-3,Math.max(0,eob(seg(t,0.1,0.8))));T(o.st,520,540,-12,Math.max(0,eob(seg(t,1.4,2.0))));
 T(o.man,1280,430,0,0.9*Math.max(0,eob(seg(t,0.8,1.5))));T(o.q,1550,230,10*Math.sin(t*4),Math.max(0,eob(seg(t,2.2,2.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 17 ===================
BLK[17]={D:19.41,S:[
{s:0,e:3.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'USCIRE PRIMA');
 o.door=el('g',{},g);door(o.door);
 o.tag=el('g',{},g);el('rect',{x:-220,y:-90,width:440,height:180,rx:24,fill:AMB,stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},o.tag);el('circle',{cx:-180,cy:0,r:16,fill:'#fff'},o.tag);txt(o.tag,'HA UN',20,-10,50,'#5A3300','900');txt(o.tag,'PREZZO',20,48,64,'#5A3300','900');
 o.cap=el('g',{},g);cap(o.cap,'E USCIRE PRIMA HA UN PREZZO',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.door,620,500,0,Math.max(0,eob(seg(t,0.1,0.8)))*0.95);T(o.tag,1180,480,lerp(-30,6,eob(seg(t,0.6,1.5))),Math.max(0,eob(seg(t,0.6,1.3))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:3.2,e:10.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'COEFFICIENTE E ET\u00c0');
 o.ax=el('g',{},g);el('line',{x1:-800,y1:0,x2:800,y2:0,stroke:'#fff','stroke-width':6,opacity:.7},o.ax);
 o.b1=el('g',{},g);o.b2=el('g',{},g);
 o.r1=el('rect',{x:-130,y:-10,width:260,height:10,rx:14,fill:'#E09A1A'},o.b1);o.r2=el('rect',{x:-130,y:-10,width:260,height:10,rx:14,fill:'#2FBF9B'},o.b2);
 o.l1=txt(g,'64 ANNI',0,0,60,'#fff','900');o.l2=txt(g,'67 ANNI',0,0,60,'#fff','900');
 o.v1=txt(g,'5,088%',0,0,70,'#FFD27F','900');o.v2=txt(g,'5,608%',0,0,70,'#9FF5DC','900');
 o.cap=el('g',{},g);cap(o.cap,'A 64 ANNI 5,088%, A 67 ANNI 5,608%',56);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.ax,960,780,0,1);
 const h1=eio(seg(t,0.4,2.0))*(5.088/5.608)*470,h2=eio(seg(t,1.8,3.6))*470;
 o.r1.setAttribute('y',-h1);o.r1.setAttribute('height',Math.max(4,h1));o.r2.setAttribute('y',-h2);o.r2.setAttribute('height',Math.max(4,h2));
 T(o.b1,600,780,0,1);T(o.b2,1320,780,0,1);
 o.l1.setAttribute('transform','translate(600 850)');o.l2.setAttribute('transform','translate(1320 850)');
 o.v1.setAttribute('transform','translate(600 '+(760-h1-30)+')');o.v2.setAttribute('transform','translate(1320 '+(760-h2-30)+')');op(o.v1,seg(t,1.8,2.4));op(o.v2,seg(t,3.5,4.0));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:10.2,e:17.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LO STESSO MONTANTE');
 o.m=el('g',{},g);bag(o.m,1.2);
 o.s1=el('g',{},g);const a=slipCard(o.s1,'USCITA A 64 ANNI','€ 21.300');a.amt.setAttribute('font-size',84);
 o.s2=el('g',{},g);const b=slipCard(o.s2,'ATTESA FINO A 67 ANNI','€ 23.500');b.amt.setAttribute('font-size',84);
 o.pl=el('g',{},g);pill(o.pl,'+10% L’ANNO',560,76,'#2FBF9B');
 o.ar=el('g',{},g);el('path',{d:'M0 80 L0 -80 M-50 -30 L0 -90 L50 -30',fill:'none',stroke:'#2FBF9B','stroke-width':26,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.cap=el('g',{},g);cap(o.cap,'CON LO STESSO MONTANTE: ASPETTARE DA CIRCA IL 10% IN PIÙ',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.m,960,330,0,Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.s1,520,620,-3,0.95*Math.max(0,eob(seg(t,1.2,2.0))));T(o.s2,1400,620,3,0.95*Math.max(0,eob(seg(t,3.2,4.0))));
 T(o.ar,1740,520,0,Math.max(0,eob(seg(t,4.6,5.2))));T(o.pl,1400,330,-3,Math.max(0,eob(seg(t,5.0,5.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:17.0,e:19.41,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'STESSO LAVORO');
 o.k=el('g',{},g);card3(o.k,'ASSEGNO PIÙ ALTO','#2FBF9B',900,200);
 o.ck=el('g',{},g);checkBadge(o.ck,110);
 o.cap=el('g',{},g);cap(o.cap,'STESSO LAVORO, ASSEGNO PIÙ ALTO!',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.k,960,470,-2,Math.max(0,eob(seg(t,0.1,0.8))));T(o.ck,1480,360,0,Math.max(0,eob(seg(t,0.6,1.2))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.2,0.8))));}}
]};
// =================== BLOCCO 18 ===================
function piggy(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('ellipse',{cx:0,cy:0,rx:170,ry:130,fill:'#F4A5B8',stroke:'#fff','stroke-width':8},g);
 el('circle',{cx:120,cy:-20,r:42,fill:'#F29AAF',stroke:'#fff','stroke-width':6},g);el('circle',{cx:135,cy:-20,r:7,fill:'#7A3A4A'},g);el('circle',{cx:112,cy:-20,r:7,fill:'#7A3A4A'},g);
 el('circle',{cx:70,cy:-60,r:12,fill:'#7A3A4A'},g);
 el('path',{d:'M-60 -120 L-30 -165 L0 -120',fill:'#F29AAF',stroke:'#fff','stroke-width':6},g);
 el('rect',{x:-130,y:110,width:36,height:60,rx:12,fill:'#F29AAF'},g);el('rect',{x:70,y:110,width:36,height:60,rx:12,fill:'#F29AAF'},g);
 el('rect',{x:-60,y:-132,width:80,height:12,rx:6,fill:'#7A3A4A'},g);return g;}
BLK[18]={D:15.89,S:[
{s:0,e:3.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'DUE PALETTI');
 o.a=el('g',{},g);card3(o.a,'PALETTO 1','#E09A1A',520,170);o.b=el('g',{},g);card3(o.b,'PALETTO 2','#E4412C',520,170);
 o.w=el('g',{},g);warn(o.w);
 o.cap=el('g',{},g);cap(o.cap,'CI SONO ALTRI DUE PALETTI',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.a,500,480,-4,Math.max(0,eob(seg(t,0.4,1.1))));T(o.b,1420,480,4,Math.max(0,eob(seg(t,0.9,1.6))));T(o.w,960,470,0,1.1*Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:3.0,e:10.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PALETTO 1');
 o.pg=el('g',{},g);piggy(o.pg);txt(o.pg,'FONDO PENSIONE',0,240,48,'#fff','900');
 o.x=el('g',{},g);el('line',{x1:-230,y1:-170,x2:230,y2:190,stroke:'#E4412C','stroke-width':30,'stroke-linecap':'round'},o.x);el('line',{x1:-230,y1:190,x2:230,y2:-170,stroke:'#E4412C','stroke-width':30,'stroke-linecap':'round'},o.x);
 o.ar=el('g',{},g);el('path',{d:'M-130 0 L130 0 M70 -55 L130 0 L70 55',fill:'none',stroke:'#fff','stroke-width':20,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.th=el('g',{},g);const sc=slipCard(o.th,'SOGLIA','≥ 3×');sc.amt.setAttribute('font-size',100);
 o.on=el('g',{},g);pill(o.on,'CONTA SOLO L’ASSEGNO DELL’INPS',1000,56,'#2FBF9B');
 o.cap=el('g',{},g);cap(o.cap,'LE RENDITE DEI FONDI PENSIONE NON SI CONTANO PIÙ',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.pg,460,450,-2,Math.max(0,eob(seg(t,0.1,0.8))));T(o.x,460,450,0,Math.max(0,eob(seg(t,1.8,2.4))));op(o.x,seg(t,1.8,2.2));
 T(o.ar,960,450,0,Math.max(0,eob(seg(t,2.4,3.0))));T(o.th,1440,450,2,Math.max(0,eob(seg(t,2.6,3.3))));
 T(o.on,960,790,-1,Math.max(0,eob(seg(t,4.4,5.1))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:10.0,e:15.89,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PALETTO 2');
 o.roof=el('g',{},g);el('rect',{x:-420,y:-14,width:840,height:28,rx:12,fill:'#E4412C'},o.roof);for(let i=0;i<9;i++)el('rect',{x:-420+i*100,y:14,width:36,height:20,fill:'#E4412C',opacity:.6},o.roof);
 o.rt=el('g',{},g);pill(o.rt,'TETTO: 5 VOLTE LA MINIMA',820,50,'#E4412C');
 o.min=el('g',{},g);o.mins=[0,1,2,3,4].map(i=>{const c=el('g',{},o.min);el('rect',{x:-70,y:-90,width:140,height:180,rx:20,fill:'url(#g_paper)',filter:'url(#g_sh2)'},c);txt(c,'MINIMA',0,0,28,GRN,'900');const cc=el('g',{transform:'translate(0 48) scale(0.5)'},c);coinA(cc,52);return c;});
 o.mm=el('g',{},g);pill(o.mm,'FINO ALL’ETÀ DELLA VECCHIAIA',900,50,'#06303A');
 o.cap=el('g',{},g);cap(o.cap,"FINO ALLA VECCHIAIA L'ASSEGNO NON PUÒ SUPERARE 5 VOLTE IL MINIMO",44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.roof,960,330,0,Math.max(0,eob(seg(t,0.2,0.9))));T(o.rt,960,250,0,Math.max(0,eob(seg(t,0.8,1.5))));
 o.mins.forEach((c,i)=>T(c,520+i*220,lerp(100,640-i*55,eob(seg(t,1.2+i*0.5,1.8+i*0.5))),(i-2)*2,Math.max(0,eob(seg(t,1.2+i*0.5,1.8+i*0.5)))));
 T(o.mm,960,790,0,Math.max(0,eob(seg(t,4.2,4.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 19 ===================
function jobs(p){return {cal:null};}
BLK[19]={D:19.85,S:[
{s:0,e:3.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ALTRE STRADE VERDI');
 o.sem=semaforo(g);setL(o.sem.L,2,1);
 o.ar=el('g',{},g);for(let i=0;i<3;i++)el('path',{d:'M'+(i*90)+' -60 L'+(i*90+60)+' 0 L'+(i*90)+' 60',fill:'none',stroke:'#2FBF9B','stroke-width':26,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.cap=el('g',{},g);cap(o.cap,'MA CI SONO ALTRE STRADE VERDI!',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sem.g,640,470,0,0.95*Math.max(0,eob(seg(t,0.1,0.8))));setL(o.sem.L,2,1);
 T(o.ar,960,470,0,Math.max(0,eob(seg(t,0.8,1.5))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:3.6,e:9.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'APE SOCIALE');
 o.sign=el('g',{},g);el('rect',{x:-300,y:-110,width:600,height:220,rx:36,fill:'url(#g_badge)',stroke:'#fff','stroke-width':12,filter:'url(#g_sh)'},o.sign);txt(o.sign,'APE SOCIALE',0,24,70,'#fff','900');
 o.a=el('g',{},g);o.pa=plate(o.a,'63','ANNI E 5 MESI');o.pa.s.setAttribute('font-size',30);
 o.b=el('g',{},g);o.pb=plate(o.b,'30','ANNI DI CONTRIBUTI');o.pb.s.setAttribute('font-size',28);
 o.sq=el('g',{},g);o.sqs=[];for(let i=0;i<30;i++)o.sqs.push(el('rect',{x:-390+i*26,y:0,width:22,height:40,rx:6,fill:'#0A3F45',opacity:.6,stroke:LT,'stroke-width':2},o.sq));
 o.cap=el('g',{},g);cap(o.cap,"L'APE SOCIALE: UN ANTICIPO DAI 63 ANNI E 5 MESI CON 30 ANNI DI CONTRIBUTI",44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sign,960,260,-2,Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.a,520,540,0,1.35*Math.max(0,eob(seg(t,1.0,1.7))));T(o.b,1400,540,0,1.35*Math.max(0,eob(seg(t,2.4,3.1))));
 T(o.sq,960,810,0,Math.max(0,eob(seg(t,3.0,3.6))));o.sqs.forEach((q,i)=>{const on=t>3.4+i*0.06;q.setAttribute('fill',on?'#2FBF9B':'#0A3F45');q.setAttribute('opacity',on?1:.6);});
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:9.4,e:17.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PER CHI?');
 const mk=(label,build)=>{const c=el('g',{},g);el('rect',{x:-210,y:-240,width:420,height:480,rx:34,fill:'url(#g_paper)',filter:'url(#g_sh)'},c);const ic=el('g',{transform:'translate(0 -60)'},c);build(ic);const w=label.length>14?27:40;txt(c,label,0,160,w,INK,'900');return c;};
 o.c1=mk('DISOCCUPATI',ic=>{const b=el('g',{transform:'scale(1.0)'},ic);briefcase(b);el('line',{x1:-120,y1:-100,x2:120,y2:110,stroke:'#E4412C','stroke-width':20,'stroke-linecap':'round'},ic);});
 o.c2=mk('CHI ASSISTE UN FAMILIARE',ic=>{const m=el('g',{transform:'translate(-70 0)'},ic);medalS(m,true,0.3);const n=el('g',{transform:'translate(70 20)'},ic);medalS(n,false,0.24);el('path',{d:'M-130 100 Q0 140 130 100',fill:'none',stroke:'#E4412C','stroke-width':14,'stroke-linecap':'round'},ic);});
 o.c3=mk('INVALIDITÀ DEL 74%',ic=>{el('circle',{r:100,fill:'#EAF7F4',stroke:'#2FBF9B','stroke-width':14},ic);txt(ic,'74%',0,26,76,INK,'900');});
 o.c4=mk('LAVORI GRAVOSI',ic=>{const h=el('g',{transform:'translate(0 20)'},ic);hardhat(h);});
 o.cap=el('g',{},g);cap(o.cap,'DISOCCUPATI, CAREGIVER, INVALIDITÀ DEL 74%, LAVORI GRAVOSI',46);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 [o.c1,o.c2,o.c3,o.c4].forEach((c,i)=>{T(c,330+i*420,500,(i-1.5)*2,0.95*Math.max(0,eob(seg(t,0.4+i*1.5,1.0+i*1.5))));});
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:17.2,e:19.85,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'FINO A');
 o.r=el('g',{},g);el('rect',{x:-480,y:-170,width:960,height:340,rx:46,fill:'url(#g_badge)',stroke:'#fff','stroke-width':12,filter:'url(#g_sh)'},o.r);txt(o.r,'FINO A',0,-60,56,'#fff','900');txt(o.r,'€ 1.500',-130,70,130,'#fff','900');txt(o.r,'AL MESE',290,70,48,'#fff','900');
 o.c=el('g',{},g);coinA(o.c,100);
 o.cap=el('g',{},g);cap(o.cap,'FINO A 1.500 EURO AL MESE',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.r,960,470,-2,Math.max(0,eob(seg(t,0.1,0.8))));T(o.c,1560,260,12*Math.sin(t*4),Math.max(0,eob(seg(t,0.6,1.3))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.2,0.8))));}}
]};
// =================== BLOCCO 20 ===================
BLK[20]={D:18.67,S:[
{s:0,e:4.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ATTENZIONE ALLE DATE');
 o.cal=calendarPage(g,'DICEMBRE','31',320,'2026');
 o.w=el('g',{},g);warn(o.w);
 o.pl=el('g',{},g);pill(o.pl,'APE SOCIALE FINO AL 2026',900,56,'#E09A1A');
 o.cap=el('g',{},g);cap(o.cap,"L'APE SOCIALE È PREVISTA FINO AL 31 DICEMBRE 2026",52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 const p=eob(seg(t,0.1,0.8));T(o.cal.g,520,lerp(-700,180,p),t>0.9?5*Math.exp(-2.4*(t-0.9))*Math.sin(8*(t-0.9)):0,1.15);
 T(o.w,1400,430,0,1.2*Math.max(0,eob(seg(t,0.9,1.6))));T(o.pl,1400,730,-3,Math.max(0,eob(seg(t,1.8,2.5))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:4.4,e:9.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LE DOMANDE');
 o.line=el('g',{},g);el('rect',{x:-760,y:-8,width:1520,height:16,rx:8,fill:'#fff',opacity:.85},o.line);
 const pts=[[-700,'LUGLIO','15'],[-100,'NOVEMBRE','30']];
 o.pts=pts.map((q,i)=>{const c=el('g',{},g);el('circle',{r:26,fill:i?'#E4412C':AMB,stroke:'#fff','stroke-width':6},c);return c;});
 o.l1=el('g',{},g);o.c1=calendarPage(o.l1,'LUGLIO','15',240,'');o.l2=el('g',{},g);o.c2=calendarPage(o.l2,'NOVEMBRE','30',240,'');
 o.n1=el('g',{},g);pill(o.n1,'DOPO: SOLO SE RESTANO FONDI',900,50,'#E09A1A');o.n2=el('g',{},g);pill(o.n2,'ULTIMO GIORNO PER LA DOMANDA',900,50,'#E4412C');
 o.coin=el('g',{},g);coinA(o.coin,70);
 o.cap=el('g',{},g);cap(o.cap,'DOMANDE ENTRO IL 30 NOVEMBRE: DOPO IL 15 LUGLIO SOLO SE RESTANO FONDI',44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.l1,520,160,0,0.78*Math.max(0,eob(seg(t,0.4,1.1))));T(o.l2,1400,160,0,0.78*Math.max(0,eob(seg(t,2.2,2.9))));
 T(o.n1,520,690,-2,Math.max(0,eob(seg(t,1.4,2.1))));T(o.n2,1400,690,2,Math.max(0,eob(seg(t,3.1,3.8))));
 T(o.coin,1000,420,0,Math.max(0,eob(seg(t,1.6,2.2)))*(t>2.2?1+0.06*Math.sin(t*6):1));
 o.line.setAttribute('transform','translate(960 560)');
 T(o.pts[0],520,560,0,1);T(o.pts[1],1400,560,0,1);
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:9.6,e:18.67,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'QUOTA 41 PER I PRECOCI');
 o.p=el('g',{},g);o.pl=plate(o.p,'41','ANNI DI CONTRIBUTI');o.pl.s.setAttribute('font-size',28);
 o.k=el('g',{},g);const kk=el('g',{transform:'scale(2)'},o.k);kid(kk,1.0);
 o.f=el('g',{},g);o.fl=plate(o.f,'12','MESI PRIMA DEI 19 ANNI');o.fl.s.setAttribute('font-size',28);
 o.t=el('g',{},g);o.ts=['DISOCCUPATO','CAREGIVER','INVALIDO','LAVORO GRAVOSO'].map((s,i)=>{const c=el('g',{},o.t);pill(c,s,330,40,['#2FBF9B','#E09A1A','#E4412C','#6F878C'][i]);return c;});
 o.sh=el('g',{},g);shield(o.sh);
 o.c1=el('g',{},g);cap(o.c1,'LA QUOTA 41 PER I PRECOCI: 41 ANNI DI CONTRIBUTI',52);
 o.c2=el('g',{},g);cap(o.c2,'ALMENO 12 MESI VERSATI PRIMA DEI 19 ANNI',52);
 o.c3=el('g',{},g);cap(o.c3,'E UNA CONDIZIONE DI TUTELA',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.p,500,430,0,1.3*Math.max(0,eob(seg(t,0.2,0.9))));
 T(o.k,1000,300,0,Math.max(0,eob(seg(t,3.2,3.9))));T(o.f,1450,430,0,1.3*Math.max(0,eob(seg(t,3.6,4.3))));
 T(o.sh,960,430,0,0.8*Math.max(0,eob(seg(t,6.2,6.9))));
 o.ts.forEach((c,i)=>{const a=eob(seg(t,6.8+i*0.5,7.3+i*0.5));T(c,i<2?600+i*720:600+(i-2)*720,i<2?780:870,(i%2?3:-3),Math.max(0,a));});
 const fade=seg(t,6.0,6.4);op(o.p,1-fade);op(o.f,1-fade);op(o.k,1-fade);
 op(o.c1,t<3.4?1:0);op(o.c2,(t>=3.4&&t<6.0)?1:0);op(o.c3,t>=6.0?1:0);[o.c1,o.c2,o.c3].forEach(c=>T(c,960,950,0,1));}}
]};
