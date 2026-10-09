// =================== helper 31-42 ===================
function idCard(p,label,col){const g=el('g',{},p);
 el('rect',{x:-150,y:-95,width:300,height:190,rx:22,fill:'url(#g_paper)',filter:'url(#g_sh2)'},g);
 el('rect',{x:-150,y:-95,width:300,height:54,rx:22,fill:col},g);el('rect',{x:-150,y:-66,width:300,height:25,fill:col},g);
 txt(g,label,0,-52,34,'#fff','900');el('circle',{cx:-80,cy:20,r:34,fill:'#C9D6D8'},g);
 el('rect',{x:-30,y:0,width:150,height:14,rx:7,fill:'#C9D6D8'},g);el('rect',{x:-30,y:28,width:110,height:14,rx:7,fill:'#C9D6D8'},g);return g;}
function menuBtn(p,label,w,col){const g=el('g',{},p);
 el('rect',{x:-w/2,y:-48,width:w,height:96,rx:28,fill:col||'#fff',stroke:'#2FBF9B','stroke-width':6,filter:'url(#g_sh2)'},g);
 txt(g,label,0,12,Math.min(40,(w-60)/(label.length*0.62)),col?'#fff':INK,'900');return g;}
function finger(p){const g=el('g',{},p);
 el('circle',{r:44,fill:'#fff',opacity:.55},g);el('circle',{r:22,fill:'#fff',opacity:.9},g);return g;}
function scrn(p,title){const g=el('g',{},p);
 el('rect',{x:-420,y:-250,width:840,height:500,rx:36,fill:'#0A2B30',stroke:'#7FA9AE','stroke-width':8,filter:'url(#g_sh)'},g);
 el('rect',{x:-390,y:-220,width:780,height:440,rx:20,fill:'#EAF7F4'},g);
 el('rect',{x:-390,y:-220,width:780,height:76,rx:20,fill:'url(#g_head)'},g);el('rect',{x:-390,y:-190,width:780,height:46,fill:'url(#g_head)'},g);
 txt(g,title,0,-168,40,'#fff','900');return g;}
// =================== BLOCCO 31 ===================
BLK[31]={D:18.77,S:[
{s:0,e:7.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PASSO UNO');
 o.m=el('g',{},g);medal(o.m,false);o.tu=el('g',{},g);pill(o.tu,'TU, OGGI',460,64,'#2FBF9B');
 o.sc=el('g',{},g);scrn(o.sc,'MAI INPS');
 o.i=[idCard(g,'SPID','#2FBF9B'),idCard(g,'CARTA IDENTITÀ','#E09A1A'),idCard(g,'CARTA SERVIZI','#6F878C')];
 o.pa=el('g',{},g);pill(o.pa,'OPPURE: UN PATRONATO',760,52,'#06303A');
 o.cap=el('g',{},g);cap(o.cap,'ENTRA NEL TUO MAI INPS CON SPID, CARTA D’IDENTITÀ O CARTA DEI SERVIZI',44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.m,260,430,0,0.85*Math.max(0,eob(seg(t,0.1,0.8))));T(o.tu,260,680,-3,Math.max(0,eob(seg(t,0.6,1.2))));
 T(o.sc,960,430,0,0.78*Math.max(0,eob(seg(t,0.8,1.5))));
 o.i.forEach((c,i)=>T(c,1500,230+i*220,(i-1)*3,0.72*Math.max(0,eob(seg(t,2.0+i*0.7,2.6+i*0.7)))));
 T(o.pa,1000,790,-1,Math.max(0,eob(seg(t,5.0,5.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:7.0,e:18.77,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'FASCICOLO PREVIDENZIALE');
 o.m1=el('g',{},g);menuBtn(o.m1,'FASCICOLO PREVIDENZIALE',760);o.m2=el('g',{},g);menuBtn(o.m2,'ESTRATTO CONTO CONTRIBUTIVO',860,'#2FBF9B');
 o.f=el('g',{},g);finger(o.f);
 o.sc=el('g',{},g);scrn(o.sc,'ESTRATTO CONTO');
 o.rw=[];for(let i=0;i<5;i++){const r=el('g',{},o.sc);txt(r,''+(2022+i),-330,-100+i*70,36,INK,'900','start');el('rect',{x:-190,y:-124+i*70,width:420,height:34,rx:17,fill:'#C9D6D8'},r);const f=el('rect',{x:-190,y:-124+i*70,width:10,height:34,rx:17,fill:'url(#g_badge)'},r);o.rw.push({r,f});}
 o.cap=el('g',{},g);cap(o.cap,'LI TROVI TUTTI I CONTRIBUTI VERSATI A TUO NOME, ANNO PER ANNO',48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.m1,960,360,0,Math.max(0,eob(seg(t,0.1,0.8)))*(t<2.4?1:Math.max(0,1-seg(t,2.4,2.8))));
 T(o.m2,960,540,0,Math.max(0,eob(seg(t,0.8,1.5)))*(t<5.0?1:Math.max(0,1-seg(t,5.0,5.4))));
 const fx=t<2.0?lerp(1500,960,eo3(seg(t,1.0,2.0))):lerp(960,960,0),fy=t<2.0?lerp(800,360,eo3(seg(t,1.0,2.0))):lerp(360,540,eio(seg(t,3.2,4.2)));
 T(o.f,fx,fy,0,t<1.0||t>4.8?0:1);
 T(o.sc,960,460,0,Math.max(0,eob(seg(t,5.2,5.9))));o.sc.setAttribute('transform','translate(960 460) scale('+Math.max(0,eob(seg(t,5.2,5.9)))+')');
 o.rw.forEach((x,i)=>x.f.setAttribute('width',Math.max(10,420*eo3(seg(t,6.0+i*0.7,6.8+i*0.7)))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 32 ===================
BLK[32]={D:19.27,S:[
{s:0,e:9.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'CERCA TRE COSE');
 o.c=[['ANNI CHE MANCANO','#E09A1A',0],['PERIODI NON RISULTANO','#E4412C',1],['DATA DEL 1° CONTRIBUTO','#2FBF9B',2]].map(([s,c,i])=>{const w=el('g',{},g);
  el('rect',{x:-260,y:-250,width:520,height:500,rx:36,fill:'url(#g_paper)',filter:'url(#g_sh)'},w);el('rect',{x:-260,y:-250,width:520,height:120,rx:36,fill:c},w);el('rect',{x:-260,y:-190,width:520,height:60,fill:c},w);
  txt(w,s,0,-168,s.length>18?32:38,'#fff','900');
  const ic=el('g',{transform:'translate(0 40)'},w);
  if(i==0){for(let k=0;k<5;k++)el('rect',{x:-190+k*80,y:-60,width:66,height:110,rx:12,fill:k==3?'none':'#2FBF9B',stroke:k==3?'#E09A1A':'none','stroke-width':6,'stroke-dasharray':'12 8'},ic);txt(ic,'?',74,40,110,'#E09A1A','900');}
  if(i==1){const m=el('g',{transform:'translate(-20 -10) scale(0.75)'},ic);magnifier(m);}
  if(i==2){el('line',{x1:-190,y1:30,x2:190,y2:30,stroke:'#C9D6D8','stroke-width':10},ic);const f=el('g',{transform:'translate(-120 30)'},ic);el('line',{x1:0,y1:0,x2:0,y2:-110,stroke:INK,'stroke-width':8},f);el('path',{d:'M0 -110 L90 -85 L0 -60 Z',fill:'#2FBF9B'},f);}
  return w;});
 o.cap=el('g',{},g);cap(o.cap,'CERCA: GLI ANNI CHE MANCANO, I PERIODI NON RISULTANO, LA DATA DEL PRIMO CONTRIBUTO',42);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 [380,960,1540].forEach((x,i)=>T(o.c[i],x,500,(i-1)*3,0.88*Math.max(0,eob(seg(t,0.3+i*2.4,0.9+i*2.4)))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:9.2,e:14.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IN QUALE SISTEMA SEI?');
 o.b=[['RETRIBUTIVO','#6F878C'],['MISTO','#E09A1A'],['CONTRIBUTIVO','#2FBF9B']].map(([s,c])=>{const w=el('g',{},g);card3(w,s,c,560,200);return w;});
 o.fl=el('g',{},g);el('line',{x1:0,y1:0,x2:0,y2:-170,stroke:'#fff','stroke-width':10,'stroke-linecap':'round'},o.fl);el('path',{d:'M0 -170 L180 -130 L0 -90 Z',fill:'#2FBF9B'},o.fl);txt(o.fl,'1° CONTRIBUTO',90,-120,28,'#fff','900');
 o.cap=el('g',{},g);cap(o.cap,'LA DATA DEL PRIMO CONTRIBUTO DECIDE IL TUO SISTEMA',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 [380,960,1540].forEach((x,i)=>T(o.b[i],x,560,(i-1)*3,Math.max(0,eob(seg(t,0.4+i*0.6,1.0+i*0.6)))));
 T(o.fl,960,400,0,Math.max(0,eob(seg(t,0.2,0.8))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:14.4,e:19.27,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TROVI UN BUCO?');
 o.bar=el('g',{},g);for(let i=0;i<12;i++)el('rect',{x:-720+i*125,y:-50,width:112,height:100,rx:16,fill:(i==5||i==6)?'none':'#2FBF9B',stroke:(i==5||i==6)?'#E4412C':'none','stroke-width':8,'stroke-dasharray':'14 10'},o.bar);
 o.q=el('g',{},g);txt(o.q,'BUCO!',0,0,90,'#E4412C','900');
 o.bt=el('g',{},g);menuBtn(o.bt,'SEGNALA L’ANOMALIA',760,'#E4412C');o.f=el('g',{},g);finger(o.f);
 o.cap=el('g',{},g);cap(o.cap,'SE TROVI UN BUCO, SEGNALALO DAL TUO MAI INPS: PIÙ ASPETTI, PIÙ È DIFFICILE',44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.bar,960,380,0,Math.max(0,eob(seg(t,0.1,0.8))));T(o.q,960,250,-3,Math.max(0,eob(seg(t,0.9,1.5)))*(1+0.04*Math.sin(t*6)));
 T(o.bt,960,640,0,Math.max(0,eob(seg(t,1.6,2.3))));
 T(o.f,lerp(1500,1000,eo3(seg(t,2.4,3.4))),lerp(850,650,eo3(seg(t,2.4,3.4))),0,t>2.4&&t<4.2?1:0);
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 33 ===================
BLK[33]={D:15.86,S:[
{s:0,e:7.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PASSO DUE: PENSAMI');
 o.sc=el('g',{},g);scrn(o.sc,'PENSAMI');
 o.sl=[0,1,2].map(i=>{const r=el('g',{},o.sc);txt(r,['ETÀ','STIPENDIO','CONTRIBUTI'][i],-340,-90+i*70,30,INK,'900','start');el('rect',{x:-100,y:-112+i*70,width:400,height:14,rx:7,fill:'#C9D6D8'},r);const k=el('circle',{cx:-100,cy:-105+i*70,r:20,fill:AMB,stroke:'#fff','stroke-width':4},r);return {r,k};});
 o.res=el('g',{},g);el('rect',{x:-290,y:-130,width:580,height:260,rx:36,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.res);txt(o.res,'QUANDO',0,-30,56,'#fff','900');txt(o.res,'E QUANTO',0,60,56,'#fff','900');
 o.sg=el('g',{},g);pill(o.sg,'IL SIMULATORE DELL’INPS',760,50,'#06303A');
 o.cap=el('g',{},g);cap(o.cap,'PROVA PENSAMI, IL SIMULATORE DELL’INPS: QUANDO E CON QUALE IMPORTO',44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sc,620,430,0,0.85*Math.max(0,eob(seg(t,0.1,0.8))));
 o.sl.forEach((s,i)=>s.k.setAttribute('cx',lerp(-100,300,eio(seg(t,1.0+i*0.7,2.4+i*0.7)))));
 T(o.res,1560,420,3,Math.max(0,eob(seg(t,3.6,4.3))));T(o.sg,1100,820,-1,Math.max(0,eob(seg(t,4.6,5.3))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:7.4,e:15.86,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'SIMULAZIONE, NON PROMESSA');
 o.st=el('g',{},g);el('rect',{x:-380,y:-90,width:760,height:180,rx:20,fill:'none',stroke:'#E09A1A','stroke-width':14},o.st);txt(o.st,'NON UNA PROMESSA',0,28,66,'#E09A1A','900');
 o.nw=el('g',{},g);o.nd=docO(o.nw,420,560,'GIORNALE','TITOLO','');
 o.vs=el('g',{},g);txt(o.vs,'MEGLIO',0,30,80,'#fff','900');
 o.sim=el('g',{},g);scrn(o.sim,'SIMULAZIONE');o.ck=el('g',{},g);checkBadge(o.ck,90);
 o.cap=el('g',{},g);cap(o.cap,'È UNA SIMULAZIONE, NON UNA PROMESSA: MEGLIO DI UN TITOLO DI GIORNALE',44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.st,960,300,-4,Math.max(0,eob(seg(t,0.2,0.9)))*(t>0.9?1+0.03*Math.sin((t-0.9)*7):1));
 T(o.nw,420,640,-4,0.8*Math.max(0,eob(seg(t,1.6,2.3))));T(o.vs,960,640,0,Math.max(0,eob(seg(t,3.0,3.6))));
 T(o.sim,1480,640,3,0.6*Math.max(0,eob(seg(t,3.6,4.3))));T(o.ck,1760,470,0,Math.max(0,eob(seg(t,4.6,5.2))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 34 ===================
BLK[34]={D:17.09,S:[
{s:0,e:7.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PASSO TRE: TRE DATE');
 o.n=el('g',{},g);const pad=el('g',{},o.n);el('rect',{x:-260,y:-250,width:520,height:500,rx:20,fill:'#FFE680',filter:'url(#g_sh)'},pad);
 o.d=[['ANTICIPATA','#E09A1A'],['VECCHIAIA','#2FBF9B'],['FINESTRA 3 MESI','#E4412C']].map(([s,c],i)=>{const w=el('g',{},g);el('rect',{x:-250,y:-110,width:500,height:220,rx:28,fill:'url(#g_paper)',stroke:c,'stroke-width':10,filter:'url(#g_sh2)'},w);txt(w,s,0,-30,s.length>12?40:50,c,'900');txt(w,'DATA: __ / __ / ____',0,60,44,INK,'900');return w;});
 o.cap=el('g',{},g);cap(o.cap,'SCRIVI TRE DATE: ANTICIPATA, VECCHIAIA E FINESTRA DI TRE MESI',46);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.n,960,470,0,1.35*Math.max(0,eob(seg(t,0.1,0.8))));op(o.n,0.35);
 o.d.forEach((w,i)=>T(w,960,260+i*230,(i-1)*2,Math.max(0,eob(seg(t,0.8+i*1.8,1.4+i*1.8)))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:7.4,e:12.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PASSO QUATTRO');
 o.p=el('g',{},g);o.pc=docO(o.p,520,640,'PORTA TUTTO','PATRONATO','');
 o.pa=el('g',{},g);card3(o.pa,'PATRONATO','#2FBF9B',560,170);o.m=el('g',{},g);medal(o.m,true);
 o.ar=el('g',{},g);el('path',{d:'M-90 0 L90 0 M50 -45 L90 0 L50 45',fill:'none',stroke:'#fff','stroke-width':18,'stroke-linecap':'round','stroke-linejoin':'round'},o.ar);
 o.fr=el('g',{},g);pill(o.fr,'DI SOLITO GRATUITO',640,52,'#E09A1A');
 o.cap=el('g',{},g);cap(o.cap,'PORTA TUTTO A UN PATRONATO',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.p,430,470,-3,Math.max(0,eob(seg(t,0.1,0.8))));T(o.ar,820,470,0,Math.max(0,eob(seg(t,1.0,1.6))));
 T(o.m,1160,400,0,0.8*Math.max(0,eob(seg(t,1.4,2.1))));T(o.pa,1500,640,3,Math.max(0,eob(seg(t,2.0,2.7))));T(o.fr,1360,820,-2,Math.max(0,eob(seg(t,3.0,3.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:12.4,e:17.09,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PASSO CINQUE');
 o.b=el('g',{},g);briefcase(o.b);o.s=el('g',{},g);stopSign(o.s);
 o.cal=calendarPage(g,'MANOVRA','OK',200,'');
 o.nx=el('g',{},g);pill(o.nx,'NIENTE SCELTE IRREVERSIBILI',900,52,'#E4412C');
 o.cap=el('g',{},g);cap(o.cap,'NIENTE DIMISSIONI PRIMA CHE LA MANOVRA SIA APPROVATA!',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.b,430,430,-3,1.2*Math.max(0,eob(seg(t,0.1,0.8))));T(o.s,430,430,0,1.2*Math.max(0,eob(seg(t,1.0,1.7))));
 T(o.cal.g,1420,170,0,1.0*Math.max(0,eob(seg(t,1.8,2.5))));T(o.nx,960,790,-1,Math.max(0,eob(seg(t,2.6,3.3))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 35 ===================
BLK[35]={D:11.54,S:[
{s:0,e:3.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'I TRE ERRORI PIÙ COSTOSI');
 o.e=[0,1,2].map(i=>{const c=el('g',{},g);el('circle',{r:150,fill:'url(#g_red)',stroke:'#fff','stroke-width':12,filter:'url(#g_sh)'},c);txt(c,''+(3-i),0,60,170,'#fff','900');return c;});
 o.cap=el('g',{},g);cap(o.cap,'ECCO I TRE ERRORI PIÙ COSTOSI',58);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 o.e.forEach((c,i)=>T(c,420+i*540,480,(i-1)*5,Math.max(0,eob(seg(t,0.2+i*0.4,0.8+i*0.4)))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:3.6,e:11.54,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ERRORE NUMERO TRE');
 o.n=el('g',{},g);el('circle',{r:100,fill:'url(#g_red)',stroke:'#fff','stroke-width':10},o.n);txt(o.n,'3',0,40,120,'#fff','900');
 o.b=el('g',{},g);briefcase(o.b);o.ar=el('g',{},g);el('path',{d:'M-90 0 L90 0 M50 -45 L90 0 L50 45',fill:'none',stroke:'#fff','stroke-width':18,'stroke-linecap':'round'},o.ar);
 o.w=el('g',{},g);el('rect',{x:-170,y:-90,width:340,height:220,rx:20,fill:'#6F4A2A',stroke:'#fff','stroke-width':8},o.w);txt(o.w,'0',0,70,100,'#fff','900');
 o.mm=[0,1,2].map(i=>{const c=el('g',{},g);el('rect',{x:-70,y:-70,width:140,height:140,rx:22,fill:'#E4412C'},c);txt(c,'MESE '+(i+1),0,14,36,'#fff','900');return c;});
 o.cap=el('g',{},g);cap(o.cap,'DIMETTERSI PRIMA: CON LA FINESTRA DI TRE MESI RISCHI DI RESTARE SENZA NULLA',44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.n,200,260,0,Math.max(0,eob(seg(t,0.1,0.7))));T(o.b,420,400,-3,1.1*Math.max(0,eob(seg(t,0.2,0.9))));T(o.ar,820,400,0,Math.max(0,eob(seg(t,1.0,1.6))));
 T(o.w,1300,400,3,Math.max(0,eob(seg(t,1.4,2.1))));
 o.mm.forEach((c,i)=>T(c,660+i*200,720,(i-1)*3,Math.max(0,eob(seg(t,2.2+i*0.6,2.8+i*0.6)))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 36 ===================
BLK[36]={D:15.67,S:[
{s:0,e:7.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ERRORE NUMERO DUE');
 o.n=el('g',{},g);el('circle',{r:100,fill:'url(#g_red)',stroke:'#fff','stroke-width':10},o.n);txt(o.n,'2',0,40,120,'#fff','900');
 o.h=el('g',{},g);o.hd=headline(o.h,'PENSIONE A 64 ANNI PER TUTTI!',1000,40);
 o.x=el('g',{},g);el('line',{x1:-440,y1:-120,x2:440,y2:120,stroke:'#E4412C','stroke-width':26,'stroke-linecap':'round'},o.x);el('line',{x1:-440,y1:120,x2:440,y2:-120,stroke:'#E4412C','stroke-width':26,'stroke-linecap':'round'},o.x);
 o.no=el('g',{},g);pill(o.no,'NON ESISTE!',560,76,'#E4412C');
 o.cap=el('g',{},g);cap(o.cap,'ERRORE NUMERO DUE: FIDARSI DI UN TITOLO',54);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.n,200,260,0,Math.max(0,eob(seg(t,0.1,0.7))));T(o.h,960,420,-2,1.15*Math.max(0,eob(seg(t,0.4,1.1))));
 T(o.x,960,420,0,Math.max(0,eob(seg(t,2.6,3.2))));op(o.x,seg(t,2.6,3.0));T(o.no,960,700,-3,Math.max(0,eob(seg(t,3.2,3.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:7.4,e:11.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'UNA REGOLA PRECISA');
 o.r=el('g',{},g);docO(o.r,480,600,'REGOLA','SOGLIE','PRECISE');o.q=el('g',{},g);qBubble(o.q,100);o.ok=el('g',{},g);checkBadge(o.ok,80);
 o.w=el('g',{},g);pill(o.w,'CHI LA PROPONE? È APPROVATA?',1000,52,'#06303A');
 o.cap=el('g',{},g);cap(o.cap,'CONTROLLA SEMPRE CHI LA PROPONE, E SE È GIÀ STATA APPROVATA',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.r,520,430,-3,Math.max(0,eob(seg(t,0.1,0.8))));T(o.q,1100,300,10*Math.sin(t*4),Math.max(0,eob(seg(t,0.8,1.4))));T(o.ok,1500,300,0,Math.max(0,eob(seg(t,1.6,2.2))));
 T(o.w,1250,640,-2,Math.max(0,eob(seg(t,1.2,1.9))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:11.2,e:15.67,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ADESSO...');
 o.chest=el('g',{},g);
 el('rect',{x:-230,y:-60,width:460,height:260,rx:26,fill:'#0B4A50',stroke:'#2FBF9B','stroke-width':10,filter:'url(#g_sh)'},o.chest);
 el('path',{d:'M-230 -60 A230 150 0 0 1 230 -60 Z',fill:'#0F6068',stroke:'#2FBF9B','stroke-width':10},o.chest);
 for(let i=-1;i<=1;i+=2)el('rect',{x:i*130-18,y:-190,width:36,height:390,rx:10,fill:AMB,opacity:.9},o.chest);
 o.lk=el('g',{},o.chest);const L=lockO(o.lk);L.setAttribute('transform','translate(0 20) scale(0.8)');
 o.pl=el('g',{},g);pill(o.pl,'ERRORE NUMERO UNO',820,60,'#E4412C');
 o.cap=el('g',{},g);cap(o.cap,'E ADESSO, L’ERRORE NUMERO UNO: QUELLO CHE TI AVEVO PROMESSO!',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.chest,960,420,2*Math.sin(t*3),1.3*Math.max(0,eob(seg(t,0.2,1.0))));T(o.pl,960,780,0,Math.max(0,eob(seg(t,1.0,1.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 37 ===================
BLK[37]={D:14.12,S:[
{s:0,e:6.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'CONTROLLARE TROPPO TARDI');
 o.bar=el('g',{},g);for(let i=0;i<12;i++)el('rect',{x:-720+i*125,y:-50,width:112,height:100,rx:16,fill:(i==5||i==6)?'none':'#2FBF9B',stroke:(i==5||i==6)?'#E4412C':'none','stroke-width':8,'stroke-dasharray':'14 10'},o.bar);
 o.last=el('g',{},g);pill(o.last,'ULTIMO ANNO',460,56,'#E09A1A');
 o.cal=calendarPage(g,'ULTIMO','1',320,'ANNO');
 o.bu=el('g',{},g);txt(o.bu,'BUCO!',0,0,90,'#E4412C','900');
 o.cap=el('g',{},g);cap(o.cap,"ASPETTARE L'ULTIMO ANNO E SCOPRIRE UN PERIODO CHE NON RISULTA VERSATO",44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.bar,960,300,0,Math.max(0,eob(seg(t,0.1,0.8))));
 T(o.cal.g,420,420,-2,0.8*Math.max(0,eob(seg(t,1.0,1.7))));T(o.last,420,820,-3,Math.max(0,eob(seg(t,1.6,2.3))));
 T(o.bu,1260,590,-4,1.2*Math.max(0,eob(seg(t,3.0,3.7)))*(1+0.04*Math.sin(t*6)));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:6.2,e:14.12,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'RECUPERARE UN CONTRIBUTO');
 o.d=[0,1,2].map(i=>docO(g,300,380,'BUSTA PAGA',''+(2010+i*6),''));
 o.m=el('g',{},g);magnifier(o.m);o.h=el('g',{},g);hourglass(o.h);
 o.mm=[0,1,2,3].map(i=>{const c=el('g',{},g);el('rect',{x:-70,y:-70,width:140,height:140,rx:22,fill:'#E09A1A'},c);txt(c,'+1',0,16,56,'#fff','900');txt(c,'MESE',0,56,26,'#fff','900');return c;});
 o.cap=el('g',{},g);cap(o.cap,'RECUPERARE UN CONTRIBUTO PUÒ RICHIEDERE MESI: OGNI MESE IN PIÙ DI LAVORO',44);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 o.d.forEach((d,i)=>T(d,360+i*300,470,(i-1)*4,0.8*Math.max(0,eob(seg(t,0.2+i*0.5,0.8+i*0.5)))));
 const mx=lerp(300,1000,eio(seg(t,1.4,4.0)));T(o.m,mx,lerp(700,500,eio(seg(t,1.4,4.0))),0,Math.max(0,eob(seg(t,1.2,1.8))));
 T(o.h,1600,430,0,Math.max(0,eob(seg(t,3.6,4.3)))*0.9*(1+0.02*Math.sin(t*5)));
 o.mm.forEach((c,i)=>T(c,1260+i*0,0,0,0));
 o.mm.forEach((c,i)=>T(c,560+i*220,780,(i-1.5)*3,Math.max(0,eob(seg(t,4.4+i*0.7,5.0+i*0.7)))*0.85));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 38 ===================
BLK[38]={D:12.28,S:[
{s:0,e:12.28,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'RIEPILOGO: VERDE');
 o.sem=semaforo(g);setL(o.sem.L,2,1);
 o.p1=el('g',{},g);o.pl1=plate(o.p1,'67','ANNI E 1 MESE');o.pl1.s.setAttribute('font-size',28);
 o.k1=el('g',{},g);pill(o.k1,'VECCHIAIA DAL 2027',520,44,'#2FBF9B');
 o.mu=el('g',{},g);o.pm=plate(o.mu,'42','ANNI E 11 MESI');o.pm.s.setAttribute('font-size',28);
 o.md=el('g',{},g);o.pd=plate(o.md,'41','ANNI E 11 MESI');o.pd.s.setAttribute('font-size',28);
 o.m1=el('g',{},g);medal(o.m1,false);o.m2=el('g',{},g);medal(o.m2,true);
 o.k2=el('g',{},g);pill(o.k2,'ANTICIPATA DAL 2027',560,44,'#E09A1A');
 o.cap=el('g',{},g);cap(o.cap,'VERDE: DAL 2027 VECCHIAIA A 67 ANNI E 1 MESE, ANTICIPATA 42 ANNI E 11 MESI / 41 ANNI E 11 MESI',38);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sem.g,260,470,0,0.7*Math.max(0,eob(seg(t,0.1,0.8))));setL(o.sem.L,2,1);
 T(o.p1,780,380,0,1.1*Math.max(0,eob(seg(t,0.8,1.5))));T(o.k1,780,590,-2,Math.max(0,eob(seg(t,1.4,2.0))));
 T(o.mu,1240,380,0,0.9*Math.max(0,eob(seg(t,4.4,5.1))));T(o.md,1680,380,0,0.9*Math.max(0,eob(seg(t,6.4,7.1))));
 T(o.m1,1240,640,0,0.34*Math.max(0,eob(seg(t,4.8,5.4))));T(o.m2,1680,640,0,0.34*Math.max(0,eob(seg(t,6.8,7.4))));
 T(o.k2,1460,810,2,Math.max(0,eob(seg(t,7.6,8.2))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 39 ===================
BLK[39]={D:9.36,S:[
{s:0,e:9.36,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'VERDE: ANCHE A 64 ANNI');
 o.sem=semaforo(g);setL(o.sem.L,2,1);
 o.a=el('g',{},g);o.pa=plate(o.a,'64','ANNI');o.b=el('g',{},g);o.pb=plate(o.b,'20','ANNI DI CONTRIBUTI');o.pb.s.setAttribute('font-size',26);
 o.c=el('g',{},g);card3(o.c,'3 \u00d7 ASSEGNO SOCIALE','#2FBF9B',720,150);
 o.k=el('g',{},g);pill(o.k,'SOLO CONTRIBUTIVI PURI',720,50,'#E09A1A');
 o.cap=el('g',{},g);cap(o.cap,'VERDE ANCHE A 64 ANNI: PER I CONTRIBUTIVI PURI, 20 ANNI E 3 VOLTE L\u2019ASSEGNO SOCIALE',40);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sem.g,260,470,0,0.7*Math.max(0,eob(seg(t,0.1,0.8))));setL(o.sem.L,2,1);
 T(o.a,780,350,0,1.1*Math.max(0,eob(seg(t,0.6,1.3))));T(o.b,1260,350,0,1.1*Math.max(0,eob(seg(t,2.2,2.9))));
 T(o.c,1020,640,-2,Math.max(0,eob(seg(t,4.0,4.7))));T(o.k,1020,800,2,Math.max(0,eob(seg(t,6.0,6.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 40 ===================
BLK[40]={D:16.68,S:[
{s:0,e:10.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'GIALLO: SONO SOLO PROPOSTE');
 o.sem=semaforo(g);setL(o.sem.L,1,1);
 o.l=['STOP ALL\u2019AUMENTO','USCITA A 64 ANNI CON RICALCOLO','QUOTA 41','MINIME PI\u00d9 ALTE'].map((s,i)=>{const w=el('g',{},g);card3(w,s,'#E09A1A',1000,130);return w;});
 o.cap=el('g',{},g);cap(o.cap,'GIALLO: STOP ALL\u2019AUMENTO, USCITA A 64 ANNI CON RICALCOLO, QUOTA 41, MINIME PI\u00d9 ALTE',40);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.sem.g,300,470,0,0.7*Math.max(0,eob(seg(t,0.1,0.8))));setL(o.sem.L,1,1);
 o.l.forEach((w,i)=>T(w,1130,220+i*180,(i%2?2:-2),Math.max(0,eob(seg(t,0.6+i*1.8,1.2+i*1.8)))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:10.2,e:16.68,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA RISPOSTA');
 o.ma=el('g',{},g);docO(o.ma,420,560,'MANOVRA','2027','LA RISPOSTA');
 o.sem=semaforo(g);setL(o.sem.L,0,1);
 o.a=el('g',{},g);card3(o.a,'QUOTA 103','#E4412C',520,140);o.b=el('g',{},g);card3(o.b,'OPZIONE DONNA','#E4412C',620,140);
 o.cl=el('g',{},g);pill(o.cl,'CHIUSE PER CHI NON AVEVA I REQUISITI',1100,48,'#06303A');
 o.cap=el('g',{},g);cap(o.cap,'ROSSO: QUOTA 103 E OPZIONE DONNA SONO CHIUSE PER CHI NON AVEVA GI\u00c0 I REQUISITI',40);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.ma,420,430,-3,0.85*Math.max(0,eob(seg(t,0.1,0.8))));T(o.sem.g,860,430,0,0.7*Math.max(0,eob(seg(t,1.8,2.5))));setL(o.sem.L,0,seg(t,2.2,2.8));
 T(o.a,1430,330,-2,Math.max(0,eob(seg(t,2.6,3.2))));T(o.b,1470,520,2,Math.max(0,eob(seg(t,3.2,3.8))));
 T(o.cl,1250,790,-1,Math.max(0,eob(seg(t,4.0,4.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 41 ===================
BLK[41]={D:13.52,S:[
{s:0,e:6.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TOCCA A TE');
 o.q=el('g',{},g);qBubble(o.q,170);
 o.c=el('g',{},g);[0,1,2].forEach(i=>{const b=el('g',{transform:'translate(0 '+(i*130)+')'},o.c);el('rect',{x:-420,y:-52,width:840,height:104,rx:52,fill:'url(#g_paper)',filter:'url(#g_sh2)'},b);el('circle',{cx:-360,cy:0,r:34,fill:['#2FBF9B','#E09A1A','#E4412C'][i]},b);el('rect',{x:-300,y:-14,width:[620,520,420][i],height:28,rx:14,fill:'#C9D6D8'},b);});
 o.t=el('g',{},g);pill(o.t,'IN CHE ANNO PENSI DI ANDARE IN PENSIONE?',1300,56,'#2FBF9B');
 o.cap=el('g',{},g);cap(o.cap,'IN CHE ANNO PENSI DI ANDARE IN PENSIONE? SCRIVILO NEI COMMENTI!',48);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.q,360,400,10*Math.sin(t*4),Math.max(0,eob(seg(t,0.1,0.8))));T(o.t,1200,250,-1,Math.max(0,eob(seg(t,0.6,1.3))));
 [0,1,2].forEach(i=>{});T(o.c,1200,500,0,1);o.c.children[0]&&0;
 [...o.c.children].forEach((b,i)=>op(b,seg(t,1.8+i*1.0,2.4+i*1.0)));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}},
{s:6.0,e:13.52,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ISCRIVITI');
 o.hero=el('g',{},g);el('circle',{r:170,fill:'url(#g_badge)',stroke:'#fff','stroke-width':12,filter:'url(#g_sh)'},o.hero);txt(o.hero,'CP',0,50,150,'#fff','900');
 o.pill=el('g',{},g);o.pb=pill(o.pill,'ISCRIVITI',560,90,'#E4412C');
 o.bell=el('g',{},g);el('path',{d:'M-70 50 Q-70 -80 0 -80 Q70 -80 70 50 L90 80 L-90 80 Z',fill:AMB,stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},o.bell);el('circle',{cx:0,cy:100,r:22,fill:AMB},o.bell);
 o.f=el('g',{},g);finger(o.f);o.ck=el('g',{},g);checkBadge(o.ck,80);
 o.mn=el('g',{},g);pill(o.mn,'QUANDO LA MANOVRA SAR\u00c0 APPROVATA',1100,50,'#06303A');
 o.cap=el('g',{},g);cap(o.cap,'ISCRIVITI A CONTI IN PENSIONE E ATTIVA LA CAMPANELLA!',50);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.hero,540,400,0,0.9*Math.max(0,eob(seg(t,0.1,0.8))));T(o.pill,1300,420,0,Math.max(0,eob(seg(t,0.8,1.5)))*(1-0.1*Math.sin(clamp(seg(t,2.6,3.0))*Math.PI)));
 T(o.f,lerp(1700,1300,eo3(seg(t,1.8,2.6))),lerp(700,440,eo3(seg(t,1.8,2.6))),0,t>1.8&&t<3.2?1:0);
 o.ck.setAttribute('transform','translate(1660 420) scale('+Math.max(0,eob(seg(t,3.0,3.6)))+')');
 const sw=t>3.2?20*Math.exp(-1.2*(t-3.2))*Math.sin((t-3.2)*13):0;T(o.bell,1300,640,sw,Math.max(0,eob(seg(t,3.2,3.8))));
 T(o.mn,960,820,-1,Math.max(0,eob(seg(t,4.6,5.3))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));}}
]};
// =================== BLOCCO 42 ===================
BLK[42]={D:15.48,S:[
{s:0,e:15.48,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IMPORTANTE');
 o.card=el('g',{},g);el('rect',{x:-820,y:-300,width:1640,height:600,rx:50,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.card);
 el('rect',{x:-820,y:-300,width:1640,height:110,rx:50,fill:'url(#g_head)'},o.card);el('rect',{x:-820,y:-230,width:1640,height:40,fill:'url(#g_head)'},o.card);
 txt(o.card,'INFORMAZIONI A SCOPO DIVULGATIVO',0,-215,56,'#fff','900');
 o.l=['NON SOSTITUISCONO LA CONSULENZA','DI UN PATRONATO O DELL\u2019INPS','VERIFICA SEMPRE SUI CANALI UFFICIALI'].map((s,i)=>txt(o.card,s,0,-70+i*85,i==2?58:52,i==2?GRN:INK,'900'));
 txt(o.card,'INPS.IT',0,255,80,'#E09A1A','900');
 o.sh=el('g',{},g);shield(o.sh);
 o.cap=el('g',{},g);cap(o.cap,'GRAZIE PER AVER GUARDATO FINO ALLA FINE... E ALLA PROSSIMA!',52);
 this.o=o;},
 update(t){const o=this.o;T(o.top,960,100,0,1);
 T(o.card,960,470,0,Math.max(0,eob(seg(t,0.1,0.9))));
 o.l.forEach((x,i)=>op(x,seg(t,0.8+i*0.9,1.4+i*0.9)));
 T(o.sh,1780,120,0,0.3*Math.max(0,eob(seg(t,2.0,2.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,6.0,6.8))));}}
]};
