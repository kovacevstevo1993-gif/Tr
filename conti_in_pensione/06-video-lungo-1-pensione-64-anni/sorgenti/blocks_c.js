// =================== BLOCCO 11 ===================
function yx(y){return -800+(y-1980)*32;}
BLK[11]={D:13.9,S:[
{s:0,e:13.9,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'CONDIZIONE NUMERO UNO');
 o.n=el('g',{},g);el('circle',{r:80,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh2)'},o.n);txt(o.n,'1',0,36,110,'#fff','900');
 o.tl=el('g',{},g);
 el('rect',{x:-800,y:-150,width:yx(1996)+800,height:300,rx:20,fill:'#E4412C',opacity:.22},o.tl);
 el('rect',{x:yx(1996),y:-150,width:800-yx(1996),height:300,rx:20,fill:'#2FBF9B',opacity:.25},o.tl);
 el('rect',{x:-800,y:-6,width:1600,height:12,rx:6,fill:'#fff',opacity:.85},o.tl);
 [1980,1990,2000,2010,2020,2030].forEach(y=>{el('rect',{x:yx(y)-3,y:-22,width:6,height:44,fill:'#fff'},o.tl);txt(o.tl,''+y,yx(y),84,34,'#E9FBF6','900');});
 el('rect',{x:yx(1996)-5,y:-190,width:10,height:380,rx:5,fill:AMB},o.tl);
 txt(o.tl,'1996',yx(1996),-215,70,AMB,'900');
 txt(o.tl,'PRIMA DEL 1996',(yx(1996)-800)/2,138,40,'#FFB3A8','900');txt(o.tl,'DAL 1996 IN POI',(800+yx(1996))/2,138,40,'#9FF5DC','900');
 o.fl=el('g',{},g);el('line',{x1:0,y1:0,x2:0,y2:-170,stroke:'#fff','stroke-width':10,'stroke-linecap':'round'},o.fl);el('path',{d:'M0 -170 L180 -130 L0 -90 Z',fill:'#2FBF9B'},o.fl);txt(o.fl,'1° CONTRIBUTO',90,-120,28,'#fff','900');
 o.pure=el('g',{},g);pill(o.pure,'SISTEMA CONTRIBUTIVO PURO',960,54,'#2FBF9B');
 o.red=el('g',{},g);coinA(o.red,70);
 o.x=el('g',{},g);el('line',{x1:-90,y1:-90,x2:90,y2:90,stroke:'#E4412C','stroke-width':22,'stroke-linecap':'round'},o.x);el('line',{x1:-90,y1:90,x2:90,y2:-90,stroke:'#E4412C','stroke-width':22,'stroke-linecap':'round'},o.x);
 o.no=el('g',{},g);pill(o.no,'UN SOLO CONTRIBUTO PRIMA: NON FA PER TE',1300,50,'#E4412C');
 o.c1=el('g',{},g);cap(o.c1,'IL PRIMO CONTRIBUTO DAL 1° GENNAIO 1996 IN POI',50);
 o.c2=el('g',{},g);cap(o.c2,'CON UN SOLO CONTRIBUTO PRIMA DEL 1996 NON FA PER TE',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.n,200,260,0,Math.max(0,eob(seg(t,0.1,0.7))));
 T(o.tl,960,520,0,Math.max(0,eob(seg(t,0.2,0.9))));
 const fp=eob(seg(t,2.2,2.9));T(o.fl,960+yx(2006),lerp(150,520,fp)-0,0,Math.max(0,fp));o.fl.setAttribute('transform','translate('+(960+yx(2006))+' '+lerp(180,540,fp)+') scale('+Math.max(0,fp)+')');
 T(o.pure,960,780,0,Math.max(0,eob(seg(t,5.4,6.0))));
 const rd=eob(seg(t,8.4,9.1));T(o.red,960+yx(1988),lerp(150,520,rd),0,Math.max(0,rd));
 T(o.x,960+yx(1988),520,0,Math.max(0,eob(seg(t,9.4,9.9))));
 T(o.no,960,780,-2,Math.max(0,eob(seg(t,9.9,10.5))));
 op(o.pure,t<8.2?1:Math.max(0,1-seg(t,8.2,8.6)));
 op(o.c1,t<8.2?1:0);op(o.c2,t>=8.2?1:0);T(o.c1,960,950,0,1);T(o.c2,960,950,0,1);}}
]};
// =================== BLOCCO 12 ===================
BLK[12]={D:16.13,S:[
{s:0,e:5.1,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'CONDIZIONE NUMERO DUE');
 o.n=el('g',{},g);el('circle',{r:80,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh2)'},o.n);txt(o.n,'2',0,36,110,'#fff','900');
 o.p=el('g',{},g);o.pl=plate(o.p,'20','ANNI DI CONTRIBUTI');o.pl.s.setAttribute('font-size',30);
 o.sq=el('g',{},g);o.sqs=[];for(let i=0;i<20;i++)o.sqs.push(el('rect',{x:-380+i*38,y:0,width:32,height:44,rx:8,fill:'#0A3F45',opacity:.6,stroke:LT,'stroke-width':2},o.sq));
 o.slip=el('g',{},g);const sc=slipCard(o.slip,'BUSTA PAGA','CONTRIBUTI');sc.amt.setAttribute('font-size',66);
 o.st=el('g',{},g);pill(o.st,'VERSATI DAVVERO',560,60,'#2FBF9B');o.ck=el('g',{},g);checkBadge(o.ck,70);
 o.cap=el('g',{},g);cap(o.cap,'ALMENO 20 ANNI DI CONTRIBUTI EFFETTIVI: VERSATI DAVVERO',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.n,200,260,0,Math.max(0,eob(seg(t,0.1,0.7))));
 T(o.p,640,420,0,1.45*Math.max(0,eob(seg(t,0.4,1.1))));
 T(o.sq,960,810,0,Math.max(0,eob(seg(t,1.0,1.6))));
 o.sqs.forEach((q,i)=>{const on=t>1.5+i*0.06;q.setAttribute('fill',on?'#2FBF9B':'#0A3F45');q.setAttribute('opacity',on?1:.6);});
 T(o.slip,1480,400,3,0.85*Math.max(0,eob(seg(t,2.4,3.1))));
 T(o.st,1480,640,-4,Math.max(0,eob(seg(t,3.4,4.0))));T(o.ck,1760,300,0,Math.max(0,eob(seg(t,3.6,4.2))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.4,1.0))));}},
{s:5.1,e:16.13,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'COSA CAMBIA');
 o.cal=calendarPage(g,'ANNO','2027',150,'');
 o.pa=el('g',{},g);o.pla=plate(o.pa,'20','ANNI E 1 MESE');o.pla.s.setAttribute('font-size',34);
 o.pb=el('g',{},g);o.plb=plate(o.pb,'64','ANNI E 1 MESE');o.plb.s.setAttribute('font-size',34);
 o.lb1=el('g',{},g);pill(o.lb1,'CONTRIBUTI',420,46,'#2FBF9B');o.lb2=el('g',{},g);pill(o.lb2,'ETÀ',300,46,'#E09A1A');
 o.k1=el('g',{},g);o.kt1=chip(o.k1,'+1 MESE',300);o.k2=el('g',{},g);o.kt2=chip(o.k2,'+1 MESE',300);
 o.c1=el('g',{},g);cap(o.c1,'DAL 2027: 20 ANNI E 1 MESE, ETÀ 64 ANNI E 1 MESE',50);
 o.c2=el('g',{},g);cap(o.c2,'DAL 2028: 20 ANNI E 3 MESI, ETÀ 64 ANNI E 3 MESI',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 const f=seg(t,5.8,6.6);const sc=f<0.5?1-f*2:(f-0.5)*2;
 o.cal.big.textContent=f<0.5?'2027':'2028';
 o.cal.g.setAttribute('transform','translate(300 '+(140+280)+') scale('+(0.95)+' '+(0.95*Math.max(0.03,Math.abs(sc)))+') translate(0 -280)');
 T(o.pa,960,420,0,1.2*Math.max(0,eob(seg(t,0.3,1.0))));T(o.pb,1500,420,0,1.2*Math.max(0,eob(seg(t,0.8,1.5))));
 T(o.lb1,960,210,0,Math.max(0,eob(seg(t,0.5,1.1))));T(o.lb2,1500,210,0,Math.max(0,eob(seg(t,1.0,1.6))));
 const three=t>6.6;
 o.pla.s.textContent=three?'ANNI E 3 MESI':'ANNI E 1 MESE';o.plb.s.textContent=three?'ANNI E 3 MESI':'ANNI E 1 MESE';
 o.kt1.t.textContent=three?'+3 MESI':'+1 MESE';o.kt2.t.textContent=three?'+3 MESI':'+1 MESE';
 T(o.k1,960,700,-3,Math.max(0,eob(seg(t,1.6,2.3))));T(o.k2,1500,700,3,Math.max(0,eob(seg(t,2.0,2.7))));
 op(o.c1,t<5.8?1:0);op(o.c2,t>=5.8?1:0);T(o.c1,960,950,0,1);T(o.c2,960,950,0,1);}}
]};
// =================== BLOCCO 13 ===================
function kettle(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:'M-80 -150 Q-80 -240 0 -240 Q80 -240 80 -150',fill:'none',stroke:'#0B4A50','stroke-width':34,'stroke-linecap':'round'},g);
 el('path',{d:'M-190 140 Q-210 -140 0 -140 Q210 -140 190 140 Z',fill:'#0B4A50',stroke:'#2FBF9B','stroke-width':10},g);
 el('rect',{x:-170,y:130,width:340,height:34,rx:14,fill:'#06303A'},g);txt(g,'3×',0,70,130,'#fff','900');return g;}
BLK[13]={D:18.47,S:[
{s:0,e:2.9,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'CONDIZIONE NUMERO TRE');
 o.n=el('g',{},g);el('circle',{r:80,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh2)'},o.n);txt(o.n,'3',0,36,110,'#fff','900');
 o.k=el('g',{},g);kettle(o.k);o.c=el('g',{},g);coinA(o.c,150);
 o.st=el('g',{},g);pill(o.st,'LA PIÙ DIFFICILE: L’IMPORTO',900,64,'#E4412C');
 o.cap=el('g',{},g);cap(o.cap,"TRE, LA CONDIZIONE PIÙ DIFFICILE: L'IMPORTO!",54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.n,200,260,0,Math.max(0,eob(seg(t,0.1,0.7))));
 T(o.k,640,470,-4,1.1*Math.max(0,eob(seg(t,0.2,0.9))));T(o.c,1330,460,10*Math.sin(t*3),Math.max(0,eob(seg(t,0.8,1.5))));
 T(o.st,960,760,-2,Math.max(0,eob(seg(t,1.4,2.1))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:2.9,e:7.7,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA PRIMA RATA DI PENSIONE');
 o.sl=slipCard(g,'PRIMA RATA','≥');o.slg=o.sl.g;
 o.eq=el('g',{},g);txt(o.eq,'≥',0,60,200,'#fff','900');
 o.as=[0,1,2].map(i=>{const c=el('g',{},g);el('rect',{x:-150,y:-100,width:300,height:200,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh2)'},c);txt(c,'ASSEGNO',0,-30,40,INK,'900');txt(c,'SOCIALE',0,20,40,GRN,'900');const cc=el('g',{transform:'translate(0 72) scale(0.5)'},c);coinA(cc,60);return c;});
 o.x3=el('g',{},g);txt(o.x3,'× 3',0,50,130,AMB,'900');
 o.cap=el('g',{},g);cap(o.cap,"LA PRIMA RATA: ALMENO TRE VOLTE L'ASSEGNO SOCIALE",52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.slg,420,470,-2,0.8*Math.max(0,eob(seg(t,0.2,0.9))));
 o.slg.querySelectorAll('text').forEach((x,i)=>{if(i==1)x.textContent='≥ 3×';});
 T(o.eq,820,470,0,Math.max(0,eob(seg(t,1.0,1.6))));
 [0,1,2].forEach(i=>{T(o.as[i],1020+i*270+0,470+(i-1)*0,(i-1)*3,0.78*Math.max(0,eob(seg(t,1.6+i*0.5,2.2+i*0.5))));});
 T(o.x3,1330,720,0,Math.max(0,eob(seg(t,3.3,3.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:7.7,e:18.47,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL CONTO');
 o.a=el('g',{},g);
 el('rect',{x:-290,y:-190,width:580,height:380,rx:36,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.a);
 txt(o.a,'ASSEGNO SOCIALE 2026',0,-110,36,GRN,'900');txt(o.a,'€ 546,24',0,50,96,INK,'900');
 const cc=el('g',{transform:'translate(210 -150)'},o.a);coinA(cc,60);
 o.m=el('g',{},g);txt(o.m,'× 3',0,50,150,AMB,'900');
 o.r=el('g',{},g);
 el('rect',{x:-330,y:-190,width:660,height:380,rx:36,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.r);
 txt(o.r,'AL MESE',0,-100,52,'#fff','900');txt(o.r,'€ 1.638,72',0,50,84,'#fff','900');
 o.ck=el('g',{},g);checkBadge(o.ck,80);
 o.c1=el('g',{},g);cap(o.c1,"L'ASSEGNO SOCIALE 2026: 546,24 EURO",56);
 o.c2=el('g',{},g);cap(o.c2,'SERVONO ALMENO 1.638,72 EURO AL MESE!',56);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.a,480,470,-2,Math.max(0,eob(seg(t,0.2,0.9))));
 T(o.m,940,470,0,Math.max(0,eob(seg(t,3.0,3.6))));
 T(o.r,1480,470,2,0.95*Math.max(0,eob(seg(t,6.2,6.9))));T(o.ck,1760,290,0,Math.max(0,eob(seg(t,7.0,7.6))));
 op(o.c1,t<6.2?1:0);op(o.c2,t>=6.2?1:0);T(o.c1,960,950,0,1);T(o.c2,960,950,0,1);}}
]};
// =================== BLOCCO 14 ===================
function kid(p,s){const g=el('g',{transform:'scale('+s+')'},p);el('circle',{r:46,fill:'#F7D5B5',stroke:'#fff','stroke-width':6},g);el('path',{d:'M-46 -6 Q-40 -56 0 -52 Q40 -56 46 -6 Q20 -30 0 -28 Q-20 -30 -46 -6 Z',fill:'#7A4A00'},g);el('circle',{cx:-16,cy:6,r:5,fill:INK},g);el('circle',{cx:16,cy:6,r:5,fill:INK},g);el('path',{d:'M-12 24 Q0 34 12 24',fill:'none',stroke:'#C0583F','stroke-width':5,'stroke-linecap':'round'},g);return g;}
BLK[14]={D:7.77,S:[
{s:0,e:7.77,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'DONNE CON FIGLI');
 o.rows=[['1 FIGLIO','2,8 VOLTE','€ 1.529',1],['2 O PIÙ FIGLI','2,6 VOLTE','€ 1.420',2]].map(r=>{
  const w=el('g',{},g);el('rect',{x:-840,y:-130,width:1680,height:260,rx:40,fill:'url(#g_paper)',filter:'url(#g_sh)'},w);
  const m=el('g',{transform:'translate(-680 0)'},w);medalS(m,true,0.5);
  for(let k=0;k<r[3];k++){const kk=el('g',{transform:'translate('+(-560+k*70)+' 70)'},w);kid(kk,0.9);}
  txt(w,r[0],-380,-10,46,INK,'900');txt(w,r[1],60,28,62,AMB,'900');txt(w,'= '+r[2],560,28,76,GRN,'900');return w;});
 o.ref=el('g',{},g);pill(o.ref,'PER GLI ALTRI: € 1.638,72 (3 VOLTE)',1100,50,'#06303A');
 o.dn=el('g',{},g);el('path',{d:'M0 -60 L-50 0 L-18 0 L-18 60 L18 60 L18 0 L50 0 Z',fill:'#2FBF9B',stroke:'#fff','stroke-width':6},o.dn);
 o.c1=el('g',{},g);cap(o.c1,'DONNE CON UN FIGLIO: SOGLIA A CIRCA 1.529 EURO',52);
 o.c2=el('g',{},g);cap(o.c2,'CON DUE O PIÙ FIGLI: CIRCA 1.420 EURO',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.rows[0],960,370,-1,Math.max(0,eob(seg(t,0.2,0.9))));T(o.rows[1],960,680,1,Math.max(0,eob(seg(t,4.8,5.5))));
 T(o.ref,960,845,0,Math.max(0,eob(seg(t,1.4,2.0))));
 op(o.c1,t<4.8?1:0);op(o.c2,t>=4.8?1:0);T(o.c1,960,950,0,1);T(o.c2,960,950,0,1);}}
]};
// =================== BLOCCO 15 ===================
BLK[15]={D:8.77,S:[
{s:0,e:8.77,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'FACCIAMO UN CONTO');
 o.calc=el('g',{},g);
 el('rect',{x:-290,y:-380,width:580,height:760,rx:50,fill:'#0A2B30',stroke:'#7FA9AE','stroke-width':8,filter:'url(#g_sh)'},o.calc);
 el('rect',{x:-250,y:-340,width:500,height:150,rx:22,fill:'#BFEFE3'},o.calc);
 o.disp=txt(o.calc,'',230,-225,70,INK,'900','end');
 for(let r=0;r<4;r++)for(let c=0;c<4;c++)el('rect',{x:-250+c*130,y:-150+r*130,width:110,height:110,rx:24,fill:c==3?AMB:'#17383D'},o.calc);
 o.m=el('g',{},g);for(let i=0;i<13;i++){const c=el('g',{},o.m);el('rect',{x:-70,y:-70,width:140,height:140,rx:22,fill:'url(#g_paper)',filter:'url(#g_sh3)'},c);el('rect',{x:-70,y:-70,width:140,height:40,rx:22,fill:'url(#g_head)'},c);el('rect',{x:-70,y:-46,width:140,height:16,fill:'url(#g_head)'},c);txt(c,''+(i+1),0,52,60,INK,'900');}
 o.mc=[...o.m.children];
 o.lab=el('g',{},g);pill(o.lab,'13 MENSILITÀ',500,56,'#E09A1A');
 o.res=el('g',{},g);
 el('rect',{x:-420,y:-130,width:840,height:260,rx:40,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.res);
 txt(o.res,'CIRCA',0,-62,46,'#fff','900');txt(o.res,'€ 21.300 L’ANNO',0,64,74,'#fff','900');
 o.cap=el('g',{},g);cap(o.cap,'1.638,72 EURO AL MESE × 13 MENSILITÀ = CIRCA 21.300 EURO',46);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.calc,460,500,-2,0.85*Math.max(0,eob(seg(t,0.1,0.8))));
 o.disp.textContent=t<1.4?'':(t<3.2?'1638,72':(t<5.0?'1638,72×13':'= 21303'));
 o.mc.forEach((c,i)=>{const col=i%7,row=Math.floor(i/7);T(c,1010+col*125,280+row*160,(i%3-1)*3,0.9*Math.max(0,eob(seg(t,2.2+i*0.18,2.7+i*0.18))));});
 T(o.lab,1330,565,-2,Math.max(0,eob(seg(t,3.2,3.8))));
 T(o.res,1330,775,2,Math.max(0,eob(seg(t,5.1,5.8))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
