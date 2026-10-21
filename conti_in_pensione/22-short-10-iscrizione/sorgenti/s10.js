// ===== SHORT 10: iscrizione al canale. Composizioni NUOVE in ogni blocco (cedolino con voci nascoste, lavoro dietro il conto, chat commento-risposta, obiettivo mille, bottoni + scala del test) =====
// varianti rispetto agli short 8-9 (anti-ripetizione): avanzamento a 5 pallini collegati, didascalia con barra gialla a sinistra
function prog(p,i){const g=el('g',{},p);el('rect',{x:-200,y:-3,width:400,height:6,rx:3,fill:'#FFFFFF','fill-opacity':.28},g);
 el('rect',{x:-200,y:-3,width:100*i,height:6,rx:3,fill:'#FFB020'},g);
 for(let k=0;k<5;k++)el('circle',{cx:-200+k*100,cy:0,r:k===i?18:13,fill:k<=i?'#FFB020':'#2C6E73',stroke:'#fff','stroke-width':k===i?5:3},g);return g;}
function capV(p,lines,fs){fs=fs||58;const mx=Math.max(...lines.map(l=>l.length));fs=Math.min(fs,(1000-150)/(mx*0.76));const w=Math.min(1000,mx*fs*0.76+150);const h=lines.length*(fs*1.42)+54;const c=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:34,fill:'#06303A',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2+22,y:-h/2+20,width:12,height:h-40,rx:6,fill:'#FFB020'},c);
 lines.forEach((l,i)=>txt(c,l,10,-h/2+27+fs*1.08+i*fs*1.42,fs,'#FFFFFF','bold'));return c;}
function qCirc(p,r,col,s){const g=el('g',{},p);el('circle',{r:r,fill:col||YEL,stroke:'#fff','stroke-width':r*.13,filter:'url(#g_sh2)'},g);txt(g,s||'?',0,r*(s&&s.length>1?.28:.36),r*(s&&s.length>1?.78:1.05),col?'#fff':'#7A2A00','bold');return g;}
function calc(p){const g=el('g',{filter:'url(#g_sh3)'},p);el('rect',{x:-58,y:-76,width:116,height:152,rx:16,fill:'#0B4A50',stroke:'#fff','stroke-width':6},g);
 el('rect',{x:-42,y:-60,width:84,height:36,rx:6,fill:'#9BF0DB'},g);txt(g,'€',26,-32,30,'#06282C','bold');
 for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('rect',{x:-42+c*30,y:-12+r*28,width:22,height:20,rx:5,fill:r===2&&c===2?YEL:'#fff'},g);return g;}
function docLens(p){const g=el('g',{filter:'url(#g_sh3)'},p);el('rect',{x:-56,y:-74,width:104,height:140,rx:10,fill:'#fff',stroke:'#9FB4B9','stroke-width':4},g);
 [-48,-24,0,24].forEach(y=>el('rect',{x:-40,y:y,width:72,height:9,rx:4,fill:'#C9D6D8'},g));
 el('circle',{cx:22,cy:28,r:34,fill:'#9BF0DB','fill-opacity':.5,stroke:'#0B4A50','stroke-width':9},g);el('line',{x1:46,y1:52,x2:72,y2:78,stroke:'#0B4A50','stroke-width':14,'stroke-linecap':'round'},g);
 const c=el('g',{transform:'translate(22 28)'},g);el('path',{d:'M-14 0 l9 10 l18 -20',fill:'none',stroke:'#13805F','stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'},c);return g;}
function playI(p){const g=el('g',{filter:'url(#g_sh2)'},p);el('rect',{x:-70,y:-50,width:140,height:100,rx:26,fill:RED,stroke:'#fff','stroke-width':6},g);el('path',{d:'M-16 -24 L26 0 L-16 24Z',fill:'#fff'},g);return g;}
function hourglass(p){const g=el('g',{filter:'url(#g_sh2)'},p);el('rect',{x:-54,y:-76,width:108,height:16,rx:8,fill:'#0B4A50'},g);el('rect',{x:-54,y:60,width:108,height:16,rx:8,fill:'#0B4A50'},g);
 el('path',{d:'M-40 -60 H40 Q40 -14 6 0 Q40 14 40 60 H-40 Q-40 14 -6 0 Q-40 -14 -40 -60Z',fill:'#fff',stroke:'#0B4A50','stroke-width':6},g);
 el('path',{d:'M-26 -44 H26 Q20 -16 0 -6 Q-20 -16 -26 -44Z',fill:YEL},g);el('path',{d:'M-30 56 Q0 22 30 56Z',fill:YEL},g);return g;}
function avatar(p,col){const g=el('g',{},p);el('circle',{r:46,fill:col,stroke:'#fff','stroke-width':6},g);el('circle',{cy:-10,r:16,fill:'#fff'},g);el('path',{d:'M-26 30 Q0 -4 26 30Z',fill:'#fff'},g);return g;}
function bubble(p,w,h,fill,right){const g=el('g',{filter:'url(#g_sh)'},p);const x=-w/2,y=-h/2;
 el('rect',{x:x,y:y,width:w,height:h,rx:40,fill:fill,stroke:'#fff','stroke-width':4},g);
 el('path',{d:right?`M${w/2-70} ${h/2-4} l40 0 l20 34 Z`:`M${-w/2+30} ${h/2-4} l40 0 l-60 34 Z`,fill:fill},g);return g;}
function tag0(p){const g=el('g',{filter:'url(#g_sh2)',transform:'rotate(-12)'},p);el('path',{d:'M-70 -48 H40 L76 0 L40 48 H-70Z',fill:YEL,stroke:'#fff','stroke-width':6,'stroke-linejoin':'round'},g);el('circle',{cx:50,cy:0,r:8,fill:'#7A2A00'},g);txt(g,'0 €',-12,16,44,'#7A2A00','bold');return g;}
const S=[
// ---- 1: il cedolino con quattro voci che "mancano" ----
{D:DUR[0],build(p){const o={};head(p,o,'PENSIONE',0);
 o.q=card(p,0,0,940,220,46);const qc=el('g',{transform:'translate(-340 0)'},o.q);qCirc(qc,66,RED,'?');
 txt(o.q,'QUANTO TI MANCA',-240,-10,64,INK,'bold','start');txt(o.q,'NEL CEDOLINO?',-240,58,48,'#1B9F81','bold','start');o.q._x=540;
 o.ced=card(p,0,0,940,560,40);const c=o.ced;el('rect',{x:-470,y:-280,width:940,height:96,rx:40,fill:'#0B4A50'},c);el('rect',{x:-470,y:-220,width:940,height:36,fill:'#0B4A50'},c);
 txt(c,'CEDOLINO DELLA PENSIONE',0,-216,40,'#fff','bold');
 o.rw=['TREDICESIMA','ACCONTI','ADDIZIONALI','RIVALUTAZIONE TAGLIATA'].map((s,k)=>{const g=el('g',{},c);const y=-110+k*106;
  if(k)el('rect',{x:-400,y:y-58,width:800,height:3,fill:'#DCE6E7'},g);txt(g,s,-400,y+15,38,INK,'bold','start');txt(g,'− ? €',400,y+16,48,RED,'bold','end');return g;});
 o.ced._x=540;
 o.st=stamp(p,'REGOLE, NON ERRORI',760,58,'#0B4A50');
 o.cap=capV(p,['SE NON LE CONOSCI,','I SOLDI SONO GIÀ ANDATI']);return o;},
 update(t,o){const i=0;const a=plan(i,['quanti soldi','Tredicesima','acconti','addizionali','rivalutazione tagliata','Sono regole']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.q,410,120);rise(t,a[1]-.25,.9,o.ced,840,120);
  o.rw.forEach((r,k)=>inC(t,r,0,0,a[1+k]));
  stampIn(t,o.st,a[5],540,1265,-3);
  T(o.cap,540,CAPY,0,pop(t,a[6]));}},
// ---- 2: il lavoro dietro ogni conto ----
{D:DUR[1],build(p){const o={};head(p,o,'COME LAVORIAMO',1);
 o.c1=card(p,0,0,940,210,46);const k1=el('g',{transform:'translate(-340 0)'},o.c1);calc(k1);txt(o.c1,'IL CONTO VERO',-240,-10,60,INK,'bold','start');txt(o.c1,'IN EURO',-240,54,44,'#1B9F81','bold','start');o.c1._x=540;
 o.c2=card(p,0,0,940,210,46);const k2=el('g',{transform:'translate(-345 -4)'},o.c2);docLens(k2);txt(o.c2,'FONTI UFFICIALI',-240,-10,60,INK,'bold','start');txt(o.c2,'CONTROLLATE PRIMA',-240,54,44,'#1B9F81','bold','start');o.c2._x=540;
 o.m=card(p,0,0,450,300,44);const pm=el('g',{transform:'translate(0 -52)'},o.m);playI(pm);txt(o.m,'POCHI MINUTI',0,62,44,INK,'bold');txt(o.m,'DI VIDEO',0,112,36,'#1B9F81','bold');o.m._x=300;
 o.h=card(p,0,0,450,300,44);const ph=el('g',{transform:'translate(0 -52) scale(.8)'},o.h);hourglass(ph);txt(o.h,'ORE DI',0,62,44,INK,'bold');txt(o.h,'RICERCHE',0,112,36,RED,'bold');o.h._x=780;
 o.pd=el('g',{},p);const pa=el('g',{transform:'translate(-230 0)'},o.pd);pillS(pa,'PRIMA ✓',400,54,'#13805F');const pb=el('g',{transform:'translate(230 0)'},o.pd);const nb=pillS(pb,'DOPO',400,54,'#7C8B8E');el('line',{x1:-90,y1:-2,x2:90,y2:-2,stroke:RED,'stroke-width':10,'stroke-linecap':'round'},pb);
 o.cap=capV(p,['TU LO SAI PRIMA,','NON DOPO']);return o;},
 update(t,o){const i=1;const a=plan(i,['con il conto vero','Ogni numero','pochi minuti','ore di ricerche','Lo facciamo']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.c1,420,120);rise(t,a[1],.9,o.c2,690,120);
  rise(t,a[2],.9,o.m,1010,100);rise(t,a[3],.9,o.h,1010,100);
  T(o.pd,540,1290+(1-sl(t,a[4],.9))*60,0,1);op(o.pd,seg(t,a[4],a[4]+.55));
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 3: esempio + chat commento / risposta ----
{D:DUR[2],build(p){const o={};head(p,o,'UN ESEMPIO',2);
 o.ex=card(p,0,0,940,320,46);txt(o.ex,'TREDICESIMA',0,-100,44,'#1B9F81','bold');
 txt(o.ex,'1.000 €',-250,30,80,INK,'bold');txt(o.ex,'LORDI',-250,92,36,'#5A6E73','bold');
 el('path',{d:'M-60 4 H40 V-22 L92 18 L40 58 V32 H-60Z',fill:YEL,stroke:'#fff','stroke-width':5,transform:'translate(-14 2) scale(.6)'},o.ex);
 o.r=el('g',{},o.ex);o.rn=txt(o.r,'≈ 770 €',250,30,80,'#13805F','bold');txt(o.r,'A MOLTI',250,92,36,'#5A6E73','bold');o.ex._x=540;
 o.b1=el('g',{},p);const a1=el('g',{transform:'translate(-390 0)'},o.b1);avatar(a1,'#5A6E73');const u=el('g',{transform:'translate(40 0)'},o.b1);bubble(u,680,170,'#FFFFFF',false);
 txt(u,'IL TUO COMMENTO',-300,-30,32,'#5A6E73','bold','start');txt(u,'IO PRENDO … €',-300,40,56,INK,'bold','start');
 o.b2=el('g',{},p);const a2=el('g',{transform:'translate(390 0)'},o.b2);avatar(a2,'#13805F');const r=el('g',{transform:'translate(-40 0)'},o.b2);bubble(r,680,170,'#0B4A50',true);
 txt(r,'LA NOSTRA RISPOSTA',-300,-30,32,'#9BF0DB','bold','start');txt(r,'ECCO IL TUO CONTO',-300,40,48,'#fff','bold','start');const ck=el('g',{transform:'translate(285 12)'},r);check(ck,30,'#1B9F81');
 o.pl=el('g',{},p);const g1=el('g',{transform:'translate(-285 0)'},o.pl);pillS(g1,'GRATIS',300,50,'#13805F');const g2=el('g',{transform:'translate(170 0)'},o.pl);pillS(g2,'NIENTE DA VENDERE',560,42,'#0B4A50');
 o.cap=capV(p,['RISPONDIAMO','A TUTTI']);return o;},
 update(t,o){const i=2;const a=plan(i,['Un esempio','settecentosettanta','se ci scrivi','ti rispondiamo','Gratis']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.ex,430,120);inC(t,o.r,0,0,a[1]);o.rn.textContent='≈ '+Math.round(1000-230*eo3(seg(t,a[1],a[1]+.9)))+' €';
  T(o.b1,540,790+(1-sl(t,a[2],.9))*60,0,1);op(o.b1,seg(t,a[2],a[2]+.55));
  T(o.b2,540,1030+(1-sl(t,a[3],.9))*60,0,1);op(o.b2,seg(t,a[3],a[3]+.55));
  T(o.pl,540,1280+(1-sl(t,a[4],.9))*60,0,1);op(o.pl,seg(t,a[4],a[4]+.55));
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 4: l'obiettivo mille iscritti ----
{D:DUR[3],build(p){const o={};head(p,o,'CI AIUTI?',3);
 o.h=card(p,0,0,940,200,46);const hc=el('g',{transform:'translate(-340 0)'},o.h);qCirc(hc,62,'#13805F','+1');txt(o.h,'CI SERVE',-240,-10,62,INK,'bold','start');txt(o.h,'UNA MANO DA TE',-240,52,44,'#1B9F81','bold','start');o.h._x=540;
 o.g=card(p,0,0,940,340,46);const g=o.g;txt(g,'OBIETTIVO ISCRITTI',-400,-100,38,'#5A6E73','bold','start');
 el('rect',{x:-400,y:-10,width:800,height:64,rx:32,fill:'#DCE6E7'},g);o.fill=el('rect',{x:-400,y:-10,width:0,height:64,rx:32,fill:'url(#g_amber)'},g);
 o.mk=el('g',{},g);const mp=el('g',{transform:'translate(-216 100)'},o.mk);el('path',{d:'M0 -42 l14 -20 h-28z',fill:'#0B4A50',transform:'translate(0 6)'},mp);pillL(mp,'SIAMO QUI',260,34,'#0B4A50');
 o.fl=el('g',{},g);const ff=el('g',{transform:'translate(330 -100)'},o.fl);el('rect',{x:-4,y:-30,width:8,height:120,fill:'#0B4A50'},ff);el('path',{d:'M4 -30 H84 L64 -6 L84 18 H4Z',fill:RED},ff);txt(o.fl,'1.000',300,120,58,RED,'bold');o.g._x=540;
 o.c=card(p,0,0,940,220,46);const tg=el('g',{transform:'translate(-330 0)'},o.c);tag0(tg);txt(o.c,'NON TI COSTA NIENTE',-215,-10,52,INK,'bold','start');
 o.tp=el('g',{},o.c);txt(o.tp,'BASTA UN TOCCO',-215,54,42,'#1B9F81','bold','start');el('circle',{cx:320,cy:40,r:26,fill:'#fff',stroke:'#1B9F81','stroke-width':6},o.tp);o.ring=el('circle',{cx:320,cy:40,r:26,fill:'none',stroke:'#1B9F81','stroke-width':4},o.tp);o.c._x=540;
 o.cap=capV(p,['PER NOI VUOL DIRE','ANDARE AVANTI']);return o;},
 update(t,o){const i=3;const a=plan(i,['ci serve una mano','Siamo ancora pochi','mille iscritti','non ti costa','basta un tocco']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.h,400,120);rise(t,a[1]-.3,.9,o.g,720,120);
  o.fill.setAttribute('width',184*eo3(seg(t,a[1],a[1]+.9)));op(o.mk,seg(t,a[1]+.3,a[1]+.9));
  inC(t,o.fl,0,0,a[2]);rise(t,a[3],.9,o.c,1060,110);inC(t,o.tp,0,0,a[4]);
  const r=seg(t,a[4]+.9,a[4]+1.8);o.ring.setAttribute('r',26+30*eo3(r));op(o.ring,1-r);
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 5: iscriviti, mi piace, video correlato con la scala del test, commento "ci sono" ----
{D:DUR[4],build(p){const o={};head(p,o,'SEI CON NOI?',4);
 o.sub=el('g',{},p);pillS(o.sub,'ISCRIVITI',520,72,'url(#g_red)');const bb=el('g',{transform:'translate(335 -4)'},o.sub);bell(bb,.55);
 o.lk=thumb(p,.95);
 o.vc=card(p,0,0,940,330,46);const pv=el('g',{transform:'translate(-340 -60) scale(.85)'},o.vc);playI(pv);
 txt(o.vc,'VIDEO CORRELATO',-240,-70,52,INK,'bold','start');txt(o.vc,'TEST IN 3 DOMANDE',-240,-14,40,'#1B9F81','bold','start');
 o.sc=el('g',{},o.vc);[['NIENTE','#13805F'],['POCO','#C98500'],['TANTO',RED]].forEach((d,k)=>{const x=-400+k*270;el('rect',{x:x,y:40,width:260,height:70,rx:k===0?35:(k===2?35:8),fill:d[1]},o.sc);txt(o.sc,d[0],x+130,88,38,'#fff','bold');});
o.vc._x=540;
 o.cm=el('g',{},p);const av=el('g',{transform:'translate(-370 0)'},o.cm);avatar(av,'#5A6E73');const cb=el('g',{transform:'translate(80 0)'},o.cm);bubble(cb,640,160,'#FFFFFF',false);
 txt(cb,'SCRIVILO NEI COMMENTI',-280,-28,32,'#5A6E73','bold','start');txt(cb,'CI SONO!',-280,42,64,'#13805F','bold','start');
 o.cap=capV(p,['ISCRIVITI E','METTI MI PIACE']);return o;},
 update(t,o){const i=4;const a=plan(i,['Iscriviti','mi piace','tocca il video','niente, poco','scrivi: ci sono']);PL[i]=a;headU(t,o);
  T(o.sub,400,410,0,pop(t,a[0]));T(o.lk,905,405,0,pop(t,a[1]));
  rise(t,a[2],.9,o.vc,760,120);inC(t,o.sc,0,0,a[3]);
  T(o.cm,540,1130+(1-sl(t,a[4],.9))*60,0,1);op(o.cm,seg(t,a[4],a[4]+.55));
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
];
