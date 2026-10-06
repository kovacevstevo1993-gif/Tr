// override con autoadattamento del testo
function chip(p,label,w){w=w||300;const fs=Math.min(54,(w-70)/(label.length*0.76));const g=el('g',{},p);
 el('rect',{x:-w/2,y:-46,width:w,height:92,rx:46,fill:AMB,filter:'url(#g_sh2)'},g);
 el('rect',{x:-w/2,y:-46,width:w,height:92,rx:46,fill:'none',stroke:'#fff','stroke-width':5,'stroke-opacity':.85},g);
 const t=txt(g,label,0,fs*0.36,fs,'#5A3300');return {g,t};}
function pill(p,label,w,fs,fill){fs=Math.min(fs,(w-80)/(label.length*0.76));const g=el('g',{},p);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:fs*1.8,rx:fs*0.9,fill:fill||AMB,filter:'url(#g_sh2)'},g);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:fs*1.8,rx:fs*0.9,fill:'none',stroke:'#fff','stroke-width':4,'stroke-opacity':.85},g);
 txt(g,label,0,fs*0.36,fs,fill?'#fff':'#5A3300');return g;}
// ===== oggetti nuovi =====
function coinA(p,r){const g=el('g',{},p);
 el('circle',{r:r,fill:AMB,stroke:'#fff','stroke-width':r*0.1,filter:'url(#g_sh3)'},g);
 el('circle',{r:r*0.72,fill:'none',stroke:'#C98A1A','stroke-width':r*0.06},g);
 txt(g,'€',0,r*0.34,r*1.05,'#7A4A00','900');return g;}
function scissors(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 const mk=(sgn)=>{const h=el('g',{},g);const k=el('g',{transform:'scale(1 '+sgn+')'},h);
  el('path',{d:'M0 0 L-210 -6 L-210 10 L0 18 Z',fill:'url(#g_metal)',stroke:'#6F878C','stroke-width':3},k);
  el('line',{x1:0,y1:9,x2:90,y2:24,stroke:'#C9D6D8','stroke-width':16,'stroke-linecap':'round'},k);
  el('circle',{cx:110,cy:44,r:36,fill:'none',stroke:'#E4412C','stroke-width':16},k);return h;};
 const a=mk(1),b=mk(-1);el('circle',{r:12,fill:'#0B4A50'},g);return {g,a,b};}
function slipCard(p,label,amount){const c=el('g',{},p);
 el('rect',{x:-260,y:-160,width:520,height:320,rx:30,fill:'url(#g_paper)',filter:'url(#g_sh)'},c);
 el('rect',{x:-260,y:-160,width:520,height:76,rx:30,fill:'url(#g_head)'},c);el('rect',{x:-260,y:-120,width:520,height:36,fill:'url(#g_head)'},c);
 txt(c,label,0,-106,38,'#fff');
 const amt=txt(c,amount,0,64,112,INK,'900');
 el('rect',{x:-200,y:96,width:400,height:10,rx:5,fill:'#C9D6D8'},c);
 return {g:c,amt};}
function semaforo(p){const o=el('g',{},p);
 el('rect',{x:-26,y:230,width:52,height:300,fill:'#0A2B30'},o);
 el('rect',{x:-125,y:-300,width:250,height:600,rx:62,fill:'#0A2B30',stroke:'#7FA9AE','stroke-width':8,filter:'url(#g_sh)'},o);
 const L=[];[['#E4412C',-190],['#FFB838',0],['#2FBF9B',190]].forEach(([c,y])=>{
  el('circle',{cx:0,cy:y,r:72,fill:'#17383D'},o);
  const glow=el('circle',{cx:0,cy:y,r:118,fill:c,opacity:0,filter:'url(#g_glow)'},o);
  const on=el('circle',{cx:0,cy:y,r:72,fill:c,opacity:0.08},o);
  L.push({on,glow});});
 return {g:o,L};}
function setL(L,i,v){L.forEach((l,k)=>{const x=(k===i)?v:0;l.on.setAttribute('opacity',0.08+0.92*x);l.glow.setAttribute('opacity',0.75*x);});}
function lockO(p){const o=el('g',{},p);
 el('path',{d:'M-62 -20 L-62 -78 A62 62 0 0 1 62 -78 L62 -20',fill:'none',stroke:'#C9D6D8','stroke-width':26,'stroke-linecap':'round'},o);
 el('rect',{x:-98,y:-30,width:196,height:150,rx:26,fill:AMB,stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},o);
 el('circle',{cx:0,cy:38,r:20,fill:'#5A3300'},o);el('rect',{x:-8,y:38,width:16,height:46,rx:6,fill:'#5A3300'},o);return o;}
function hourglass(p){const o=el('g',{},p);
 el('rect',{x:-110,y:-176,width:220,height:26,rx:13,fill:AMB},o);el('rect',{x:-110,y:150,width:220,height:26,rx:13,fill:AMB},o);
 el('path',{d:'M-90 -150 L90 -150 L12 0 L90 150 L-90 150 L-12 0 Z',fill:'#EAF7F4',stroke:'#fff','stroke-width':6},o);
 el('path',{d:'M-70 -136 L70 -136 L10 -10 L-10 -10 Z',fill:AMB},o);
 el('path',{d:'M-70 136 L70 136 L40 66 L-40 66 Z',fill:AMB},o);return o;}
function phoneO(p){const o=el('g',{},p);
 el('rect',{x:-210,y:0,width:420,height:700,rx:56,fill:'#0A2B30',filter:'url(#g_sh)'},o);
 el('rect',{x:-210,y:0,width:420,height:700,rx:56,fill:'none',stroke:'#7FA9AE','stroke-width':5},o);
 el('rect',{x:-186,y:26,width:372,height:648,rx:36,fill:'#EAF7F4'},o);
 return o;}
function card3(p,label,col,w,h){w=w||440;h=h||170;const g=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:col,stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},g);
 txt(g,label,0,h*0.16,Math.min(72,w/label.length*1.35),'#fff','900');return g;}
const BLK={};
// =================== BLOCCO 2 ===================
BLK[2]={D:17.47,S:[
{s:0,e:4.1,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA MANOVRA');
 o.doc=el('g',{},g);
 el('rect',{x:-250,y:-300,width:500,height:600,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.doc);
 txt(o.doc,'MANOVRA',0,-210,70,INK,'900');txt(o.doc,'2027',0,-130,70,GRN,'900');
 for(let i=0;i<6;i++)el('rect',{x:-190,y:-70+i*58,width:380-(i%3)*60,height:16,rx:8,fill:'#C9D6D8'},o.doc);
 o.stamp=el('g',{},o.doc);el('rect',{x:-210,y:-52,width:420,height:104,rx:14,fill:'none',stroke:AMB,'stroke-width':12},o.stamp);txt(o.stamp,'PROPOSTA',0,24,74,AMB,'900');
 o.card=slipCard(g,'ASSEGNO DI PENSIONE','€ 1.800');
 o.strip=el('g',{},g);el('rect',{x:-260,y:100,width:520,height:60,rx:6,fill:'url(#g_paper)'},o.strip);el('line',{x1:-260,y1:100,x2:260,y2:100,stroke:'#E4412C','stroke-width':6,'stroke-dasharray':'18 12'},o.strip);
 o.sc=scissors(g);
 o.mn=el('g',{},g);el('circle',{r:70,fill:'url(#g_red)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh2)'},o.mn);el('rect',{x:-36,y:-8,width:72,height:16,rx:8,fill:'#fff'},o.mn);
 o.cap=el('g',{},g);cap(o.cap,"UNA PROPOSTA IN MANOVRA POTREBBE TAGLIARE L'ASSEGNO",52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.doc,520,470,-3,Math.max(0,eob(seg(t,0.1,0.8))));
 const st=eob(seg(t,0.8,1.4));T(o.stamp,0,0,-12,Math.max(0,st));
 T(o.card.g,1380,430,0,Math.max(0,eob(seg(t,0.4,1.1))));
 // forbici
 const sx=lerp(1900,1230,eio(seg(t,1.3,2.5)));const open=Math.abs(Math.sin(t*16))*22;
 T(o.sc.g,sx,lerp(700,590,seg(t,1.3,1.8)),0,Math.max(0,eob(seg(t,1.2,1.7))));
 o.sc.a.setAttribute('transform','rotate('+(-open)+')');o.sc.b.setAttribute('transform','rotate('+(open)+')');
 const cut=t>2.5;
 const fall=cut?(t-2.5):0;
 T(o.strip,1380,430+fall*fall*900,cut?18*fall:0,1);op(o.strip,cut?Math.max(0,1-fall*1.2):1);
 o.strip.setAttribute('transform','translate(1380 '+(430+fall*fall*900)+') rotate('+(cut?18*fall:0)+')');
 if(!cut||true){op(o.strip,cut?Math.max(0,1-fall*1.1):(t>1.0?1:0));}
 op(o.sc.g,t<3.4?1:Math.max(0,1-seg(t,3.4,3.9)));
 T(o.mn,1720,300,0,Math.max(0,eob(seg(t,2.6,3.2))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.5,1.1))));}},
{s:4.1,e:10.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'SECONDO LA CGIL');
 o.pay=el('g',{},g);
 el('rect',{x:-250,y:-290,width:500,height:580,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.pay);
 el('rect',{x:-250,y:-290,width:500,height:84,rx:26,fill:'url(#g_head)'},o.pay);el('rect',{x:-250,y:-250,width:500,height:44,fill:'url(#g_head)'},o.pay);
 txt(o.pay,'BUSTA PAGA',0,-230,46,'#fff');
 txt(o.pay,'STIPENDIO ALTO',0,-130,52,INK,'900');
 for(let i=0;i<5;i++){el('rect',{x:-190,y:-80+i*66,width:260,height:18,rx:9,fill:'#C9D6D8'},o.pay);el('rect',{x:110,y:-80+i*66,width:80,height:18,rx:9,fill:'#9AD9C8'},o.pay);}
 o.up=el('g',{},o.pay);el('path',{d:'M-34 20 L0 -26 L34 20 L12 20 L12 70 L-12 70 L-12 20 Z',fill:AMB,stroke:'#fff','stroke-width':4,transform:'translate(190 -130) scale(0.9)'},o.up);
 o.coins=[];for(let i=0;i<7;i++){const c=el('g',{},g);coinA(c,38+(i%3)*8);o.coins.push(c);}
 o.num=txt(g,'',0,0,200,'#FF6A55','900');o.unit=txt(g,'AL MESE',0,0,84,'#fff','900');
 o.chip=el('g',{},g);chip(o.chip,'STIMA DELLA CGIL',640);
 o.cap=el('g',{},g);cap(o.cap,'OLTRE 365 EURO IN MENO AL MESE (STIPENDI ALTI)',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.pay,520,470,-3,Math.max(0,eob(seg(t,0.1,0.8))));
 o.coins.forEach((c,i)=>{const s0=2.4+i*0.35;const k=seg(t,s0,s0+1.6);T(c,lerp(760,1100+i*14,k),lerp(450,230-(i%3)*60,k)+Math.sin(k*3.14)*-80,k*360,k>0&&k<1?1:0);op(c,k>0&&k<1?1-k*0.6:0);});
 const v=Math.round(eio(seg(t,3.0,4.9))*365);
 o.num.textContent=t>3.0?('− '+v+' €'):'';o.num.setAttribute('transform','translate(1380 480)');
 o.unit.setAttribute('transform','translate(1380 590)');op(o.unit,seg(t,3.0,3.6));
 T(o.chip,1380,720,-2,Math.max(0,eob(seg(t,1.0,1.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.6,1.2))));}},
{s:10.0,e:17.47,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IN QUESTO VIDEO');
 o.sem=semaforo(g);
 o.l1=el('g',{},g);card3(o.l1,'GIÀ LEGGE','#2FBF9B',560,150);
 o.l2=el('g',{},g);card3(o.l2,'SOLO PROPOSTA','#E09A1A',680,150);
 o.ph=el('g',{},g);const ph=phoneO(o.ph);
 txt(ph,'I TUOI CONTRIBUTI',0,90,34,INK,'900');
 for(let i=0;i<5;i++){txt(ph,''+(2022+i),-150,170+i*80,28,INK,'bold','start');el('rect',{x:-50,y:148+i*80,width:200,height:28,rx:14,fill:'#C9D6D8'},ph);el('rect',{x:-50,y:148+i*80,width:200,height:28,rx:14,fill:'url(#g_badge)'},ph);}
 o.tm=el('g',{},g);el('circle',{r:100,fill:'#06303A',stroke:AMB,'stroke-width':12,filter:'url(#g_sh2)'},o.tm);txt(o.tm,'5',0,26,100,'#fff','900');txt(o.tm,'MINUTI',0,66,28,LT,'900');
 o.ring=el('circle',{r:112,fill:'none',stroke:LT,'stroke-width':8,'stroke-dasharray':'704','stroke-dashoffset':'704',transform:'rotate(-90)'},o.tm);
 o.c1=el('g',{},g);cap(o.c1,'COSA È GIÀ LEGGE',54);o.c2=el('g',{},g);cap(o.c2,'COSA È SOLO UNA PROPOSTA',54);o.c3=el('g',{},g);cap(o.c3,'COME CONTROLLARE SU MAI INPS IN 5 MINUTI',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sem.g,420,470,0,Math.max(0,eob(seg(t,0.1,0.8)))*0.85);
 setL(o.sem.L,2,t<2.4?seg(t,0.4,0.9):0);
 if(t>=2.4)setL(o.sem.L,1,seg(t,2.4,2.9));
 if(t>=4.6)setL(o.sem.L,-1,0);
 T(o.l1,1060,330,-3,Math.max(0,eob(seg(t,0.6,1.3))));
 T(o.l2,1180,560,3,Math.max(0,eob(seg(t,2.6,3.3))));
 op(o.l1,t<4.6?1:Math.max(0,1-seg(t,4.6,5.0)));op(o.l2,t<4.6?1:Math.max(0,1-seg(t,4.6,5.0)));
 T(o.ph,1170,150,-2,Math.max(0,eob(seg(t,4.7,5.4))));
 T(o.tm,1500,700,0,Math.max(0,eob(seg(t,5.2,5.8))));o.ring.setAttribute('stroke-dashoffset',704-704*seg(t,5.4,7.2));
 op(o.c1,t<2.4?1:0);op(o.c2,(t>=2.4&&t<4.6)?1:0);op(o.c3,t>=4.6?1:0);
 [o.c1,o.c2,o.c3].forEach(c=>T(c,960,950,0,1));}}
]};
// =================== BLOCCO 3 ===================
BLK[3]={D:18.67,S:[
{s:0,e:9.07,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'RESTA FINO ALLA FINE');
 o.chest=el('g',{},g);
 el('rect',{x:-230,y:-60,width:460,height:260,rx:26,fill:'#0B4A50',stroke:'#2FBF9B','stroke-width':10,filter:'url(#g_sh)'},o.chest);
 el('path',{d:'M-230 -60 A230 150 0 0 1 230 -60 Z',fill:'#0F6068',stroke:'#2FBF9B','stroke-width':10},o.chest);
 for(let i=-1;i<=1;i+=2)el('rect',{x:i*130-18,y:-190,width:36,height:390,rx:10,fill:AMB,opacity:.9},o.chest);
 txt(o.chest,'1',0,150,150,'#fff','900');
 o.lock=el('g',{},o.chest);const L=lockO(o.lock);L.setAttribute('transform','translate(0 20) scale(0.8)');
 o.q=el('g',{},g);qBubble(o.q,100);
 o.tag=el('g',{},g);pill(o.tag,"ERRORE NUMERO UNO",820,56,'#E4412C');
 o.bar=el('g',{},g);
 el('rect',{x:-700,y:0,width:1400,height:34,rx:17,fill:'#0A3F45',opacity:.85,stroke:LT,'stroke-width':3},o.bar);
 o.fill=el('rect',{x:-700,y:0,width:10,height:34,rx:17,fill:'url(#g_badge)'},o.bar);
 o.flag=el('g',{},o.bar);el('line',{x1:0,y1:-10,x2:0,y2:-110,stroke:'#fff','stroke-width':8,'stroke-linecap':'round'},o.flag);el('path',{d:'M0 -110 L90 -85 L0 -60 Z',fill:'#E4412C'},o.flag);
 txt(o.bar,'FINE DEL VIDEO',560,86,32,LT,'900');
 o.cap=el('g',{},g);cap(o.cap,"RESTA FINO ALLA FINE: L'ERRORE NUMERO UNO TI SORPRENDERÀ",50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.chest,960,400,t>2?2*Math.sin(t*3):0,1.3*Math.max(0,eob(seg(t,0.2,1.0))));
 const lk=t>0.9?1:0;
 T(o.tag,960,690,0,Math.max(0,eob(seg(t,1.4,2.1))));
 T(o.q,1420,240,10*Math.sin(t*4),Math.max(0,eob(seg(t,6.2,6.9)))*(1+0.05*Math.sin(t*6)));
 T(o.bar,960,790,0,1);o.fill.setAttribute('width',10+1390*eio(seg(t,0.5,8.8)));
 T(o.flag,700,0,0,Math.max(0,eob(seg(t,0.4,1.0))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.6,1.2))));}},
{s:9.07,e:15.8,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'OGNI GIORNO LEGGI');
 o.ph=el('g',{},g);const ph=phoneO(o.ph);
 o.feed=el('g',{},ph);o.cl=el('clipPath',{id:'feedclip'},ph);el('rect',{x:-186,y:26,width:372,height:648,rx:36},o.cl);o.feed.setAttribute('clip-path','url(#feedclip)');
 o.items=[];const texts=['PENSIONE A 64 ANNI!','QUOTA 41!','STOP ALL’AUMENTO!','NOVITÀ PENSIONI','ULTIM’ORA'];
 texts.forEach((s,i)=>{const it=el('g',{},o.feed);el('rect',{x:-166,y:50+i*150,width:332,height:128,rx:18,fill:'#fff',stroke:'#C9D6D8','stroke-width':3},it);el('rect',{x:-166,y:50+i*150,width:332,height:34,rx:18,fill:'#E4412C'},it);txt(it,s.length>14?s:s,0,128+i*150,s.length>14?27:36,INK,'900');o.items.push(it);});
 o.b1=el('g',{},g);card3(o.b1,'PENSIONE A 64 ANNI!','#E4412C',640,140);
 o.b2=el('g',{},g);card3(o.b2,'QUOTA 41!','#E09A1A',520,140);
 o.b3=el('g',{},g);card3(o.b3,'STOP ALL’AUMENTO!','#2FBF9B',640,140);
 o.cap=el('g',{},g);cap(o.cap,'OGNI GIORNO LEGGI TITOLI COME QUESTI',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.ph,520,150,-3,Math.max(0,eob(seg(t,0.1,0.8))));
 o.feed.setAttribute('transform','translate(0 '+(-t*55)+')');
 T(o.b1,1380,310,4,Math.max(0,eob(seg(t,1.0,1.7))));
 T(o.b2,1330,520,-3,Math.max(0,eob(seg(t,2.6,3.3))));
 T(o.b3,1400,730,3,Math.max(0,eob(seg(t,4.2,4.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.4,1.0))));}},
{s:15.8,e:18.67,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TRE COSE DIVERSE');
 o.k=[card3(g,'LEGGE','#2FBF9B',460,180),card3(g,'PROPOSTA','#E09A1A',520,180),card3(g,'CHIUSO','#E4412C',460,180)].map(x=>x);
 o.q=el('g',{},g);qBubble(o.q,110);
 o.cap=el('g',{},g);cap(o.cap,'MA QUEI TITOLI LE MESCOLANO TUTTE E TRE',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 const sp=[[400,420],[960,420],[1520,420]];
 o.k.forEach((k,i)=>{const a=eob(seg(t,0.1+i*0.25,0.7+i*0.25));const m=eio(seg(t,1.2,2.2));
  const x=lerp(sp[i][0],960+(i-1)*70,m),y=lerp(sp[i][1],520+(i-1)*40,m);T(k,x,y,lerp(0,(i-1)*14,m),Math.max(0,a));});
 T(o.q,960,330,10*Math.sin(t*5),Math.max(0,eob(seg(t,2.0,2.6))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 4 ===================
BLK[4]={D:19.43,S:[
{s:0,e:4.97,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TRE COSE, TRE COLORI');
 o.cards=[];[['GIÀ LEGGE','#2FBF9B'],['SOLO UNA PROPOSTA','#E09A1A'],['CHIUSO','#E4412C']].forEach(([s,c],i)=>{
  const w=el('g',{},g);el('rect',{x:-270,y:-280,width:540,height:560,rx:36,fill:'url(#g_paper)',filter:'url(#g_sh)'},w);
  el('rect',{x:-270,y:-280,width:540,height:150,rx:36,fill:c},w);el('rect',{x:-270,y:-190,width:540,height:60,fill:c},w);
  txt(w,s,0,-165,s.length>12?48:62,'#fff','900');
  const ic=el('g',{transform:'translate(0 70)'},w);
  if(i==0){const cb=el('g',{transform:'scale(1.6)'},ic);checkBadge(cb,70);}
  if(i==1){el('rect',{x:-90,y:-110,width:180,height:230,rx:14,fill:'#fff',stroke:c,'stroke-width':8},ic);for(let k=0;k<4;k++)el('rect',{x:-60,y:-70+k*40,width:120,height:12,rx:6,fill:'#C9D6D8'},ic);txt(ic,'?',70,90,150,c,'900');}
  if(i==2){const lk=el('g',{transform:'scale(1.15)'},ic);lockO(lk);}
  o.cards.push(w);});
 o.cap=el('g',{},g);cap(o.cap,'GIÀ LEGGE, SOLO UNA PROPOSTA, CHIUSO',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 [380,960,1540].forEach((x,i)=>{const a=eob(seg(t,0.3+i*1.2,0.9+i*1.2));T(o.cards[i],x,500,(i-1)*3,Math.max(0,a)*0.88);});
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:4.97,e:11.69,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PER QUESTO USO UN SEMAFORO');
 o.sem=semaforo(g);
 o.a=el('g',{},g);card3(o.a,'VERDE: È LEGGE','#2FBF9B',760,150);
 o.b=el('g',{},g);card3(o.b,'GIALLO: È UNA PROPOSTA','#E09A1A',900,150);
 o.c=el('g',{},g);card3(o.c,'ROSSO: È CHIUSO','#E4412C',760,150);
 o.cap=el('g',{},g);cap(o.cap,'PER QUESTO USO UN SEMAFORO!',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sem.g,520,470,0,Math.max(0,eob(seg(t,0.1,0.8))));
 const i=t<1.9?-1:(t<4.0?2:(t<5.9?1:0));
 setL(o.sem.L,t<1.9?-1:(t<4.0?2:(t<5.9?1:0)),t<1.9?0:1);
 T(o.a,1350,300,-2,Math.max(0,eob(seg(t,1.9,2.5))));
 T(o.b,1300,500,2,Math.max(0,eob(seg(t,4.0,4.6))));
 T(o.c,1350,700,-2,Math.max(0,eob(seg(t,5.9,6.5))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:11.69,e:18.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'DECIDERE IN BASE A UN TITOLO');
 o.m=el('g',{},g);medal(o.m,false);
 o.ql=el('g',{},g);qBubble(o.ql,70);
 o.l=el('g',{},g);
 el('rect',{x:-340,y:-130,width:680,height:260,rx:34,fill:'url(#g_paper)',stroke:'#E4412C','stroke-width':10,filter:'url(#g_sh)'},o.l);
 const dr=el('g',{transform:'translate(-230 0) scale(0.55)'},o.l);el('rect',{x:-90,y:-150,width:180,height:300,rx:16,fill:'#0B4A50'},dr);el('rect',{x:-70,y:-130,width:140,height:110,rx:10,fill:'none',stroke:'#2FBF9B','stroke-width':6},dr);
 txt(o.l,'LASCIARE IL LAVORO',60,-8,38,INK,'900');txt(o.l,'TROPPO PRESTO',60,50,48,'#E4412C','900');
 o.r=el('g',{},g);
 el('rect',{x:-340,y:-130,width:680,height:260,rx:34,fill:'url(#g_paper)',stroke:AMB,'stroke-width':10,filter:'url(#g_sh)'},o.r);
 const hg=el('g',{transform:'translate(-230 0) scale(0.55)'},o.r);hourglass(hg);
 txt(o.r,'ASPETTARE',70,-8,48,INK,'900');txt(o.r,'PER NIENTE',70,50,48,'#C98A1A','900');
 o.al=el('g',{},g);el('path',{d:'M0 0 L-150 60',stroke:'#E4412C','stroke-width':14,'stroke-linecap':'round',fill:'none'},o.al);
 o.ar=el('g',{},g);el('path',{d:'M0 0 L150 60',stroke:AMB,'stroke-width':14,'stroke-linecap':'round',fill:'none'},o.ar);
 o.cap=el('g',{},g);cap(o.cap,'SE DECIDI IN BASE A UN TITOLO, RISCHI...',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.m,960,330,0,0.85*Math.max(0,eob(seg(t,0.2,0.9))));
 T(o.ql,1130,200,10*Math.sin(t*4),Math.max(0,eob(seg(t,0.8,1.4))));
 T(o.al,820,520,0,1);T(o.ar,1100,520,0,1);op(o.al,seg(t,1.4,1.8));op(o.ar,seg(t,3.0,3.4));
 T(o.l,520,760,-2,Math.max(0,eob(seg(t,1.6,2.3))));
 T(o.r,1400,760,2,Math.max(0,eob(seg(t,3.2,3.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:18.2,e:19.43,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PARTIAMO DAL VERDE');
 o.sem=semaforo(g);setL(o.sem.L,2,1);
 o.go=el('g',{},g);card3(o.go,'VIA!','#2FBF9B',400,170);
 o.cap=el('g',{},g);cap(o.cap,'PARTIAMO DAL VERDE!',60);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sem.g,720,470,0,1.0);setL(o.sem.L,2,1);
 T(o.go,1250,480,-4,Math.max(0,eob(seg(t,0.15,0.7))));
 T(o.cap,960,950,0,1);}}
]};
// =================== BLOCCO 5 ===================
BLK[5]={D:10.17,S:[
{s:0,e:5.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'VERDE: PENSIONE DI VECCHIAIA');
 o.p1=el('g',{},g);o.pl1=plate(o.p1,'67','ANNI');
 o.p2=el('g',{},g);o.pl2=plate(o.p2,'20','ANNI DI CONTRIBUTI');o.pl2.s.setAttribute('font-size',30);
 o.sq=el('g',{},g);o.sqs=[];for(let i=0;i<20;i++){o.sqs.push(el('rect',{x:-380+i*38,y:0,width:32,height:44,rx:8,fill:'#0A3F45',opacity:.6,stroke:LT,'stroke-width':2},o.sq));}
 o.plus=txt(g,'+',0,0,150,'#fff','900');
 o.ok=el('g',{},g);checkBadge(o.ok,70);
 o.cap=el('g',{},g);cap(o.cap,'VECCHIAIA OGGI: 67 ANNI DI ETÀ + 20 DI CONTRIBUTI',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.p1,500,420,0,1.45*Math.max(0,eob(seg(t,0.2,0.9))));
 o.plus.setAttribute('transform','translate(960 470)');op(o.plus,seg(t,1.4,1.8));
 T(o.p2,1420,420,0,1.45*Math.max(0,eob(seg(t,2.0,2.7))));
 T(o.sq,960,790,0,Math.max(0,eob(seg(t,2.6,3.2))));
 o.sqs.forEach((q,i)=>{const on=t>3.2+i*0.07;q.setAttribute('fill',on?'#2FBF9B':'#0A3F45');q.setAttribute('opacity',on?1:.6);});
 T(o.ok,1000,230,0,1.2*Math.max(0,eob(seg(t,4.6,5.2))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.4,1.0))));}},
{s:5.6,e:10.17,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'DAL PRIMO GENNAIO 2027');
 o.cal=calendarPage(g,'GENNAIO','1',320,'2027');
 o.p=el('g',{},g);o.pl=plate(o.p,'67','ANNI');
 o.dr=dotsRow(o.p,12,225);
 o.chip=el('g',{},g);chip(o.chip,'+1 MESE',340);
 o.sp=ring(g,100);
 o.cap=el('g',{},g);cap(o.cap,'DAL 1° GENNAIO 2027: 67 ANNI E 1 MESE',56);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 const p=eob(seg(t,0.1,0.9));T(o.cal.g,500,lerp(-700,200,p),t>0.9?5*Math.exp(-2.4*(t-0.9))*Math.sin(8*(t-0.9)):0,1.1);
 T(o.p,1360,500,0,1.45*Math.max(0,eob(seg(t,0.8,1.5))));op(o.dr.g,seg(t,1.2,1.7));
 const pc=eob(seg(t,2.4,3.1));T(o.chip,lerp(1800,1660,eo3(seg(t,2.4,2.9))),lerp(100,265,pc),lerp(18,8,pc),Math.max(0,pc));
 if(t>2.9){lightDot(o.dr.a[0],true,seg(t,2.9,3.4));o.pl.s.textContent='ANNI E 1 MESE';o.pl.s.setAttribute('font-size',34);}
 const rr=seg(t,2.9,3.5);o.sp.setAttribute('r',lerp(30,200,rr));o.sp.setAttribute('opacity',t>2.9?(1-rr)*0.8:0);T(o.sp,1660,275,0,1);
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== regia ===================
const bok=document.getElementById('bok');
for(let i=0;i<16;i++){el('circle',{cx:(i*271)%1920,cy:(i*197)%1080,r:30+((i*37)%80),fill:'#8FF5DC',opacity:.06+((i*13)%7)*0.01},bok);}
const sceneG=document.getElementById('scene');const camG=document.getElementById('cam');
let curB=-1,curS=-1;
function draw(b,t){
 const B=BLK[b];let i=B.S.length-1;for(let k=0;k<B.S.length;k++){if(t<B.S[k].e){i=k;break;}}
 const S0=B.S[i];
 if(curB!==b||curS!==i){sceneG.innerHTML='';S0.build(sceneG);curB=b;curS=i;}
 const lt=t-S0.s;S0.update(lt);
 const fin=eo3(seg(lt,0,0.3)),fout=(i<B.S.length-1)?1-eio(seg(t,S0.e-0.3,S0.e)):1;
 sceneG.setAttribute('opacity',Math.min(fin,fout));
 const z=1+0.02*(t/B.D);camG.setAttribute('transform','translate(960 540) scale('+z+') translate(-960 -540)');
}
