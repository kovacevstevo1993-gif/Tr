// ===== SHORT 9: una composizione NUOVA per ogni blocco (ordine utente 17/10: tutte diverse, piu' professionali, non stravolgere) =====
const fmt=n=>String(n).replace(/\B(?=(\d{3})+(?!\d))/g,'.');
function inC(k,n,x,y,a){ // elemento dentro una scheda: entra dal basso con dissolvenza (0,9 s)
 const s=sl(k,a,.9);T(n,x,y+(1-s)*60,0,1);op(n,seg(k,a,a+.55));}
function pillL(p,label,w,fs,fill){const g=el('g',{},p);el('rect',{x:-w/2,y:-fs*0.95,width:w,height:fs*1.9,rx:fs*0.95,fill:fill,stroke:'#fff','stroke-width':5},g);txt(g,label,0,fs*0.36,fs,'#fff','bold');return g;}
const S=[
// ---- 1: GANCIO - pensione 3.000, contatore -9.400, niente multa/errore, regola di legge ----
{D:DUR[0],build(p){const o={};head(p,o,'RIVALUTAZIONE',0);
 o.c0=card(p,0,0,940,180,46);coin(o.c0,-350,0,62);txt(o.c0,'PENSIONE DA',-262,-16,40,'#1B9F81','bold','start');txt(o.c0,'3.000 € LORDI',-262,52,62,INK,'bold','start');o.c0._x=540;
 o.c1=card(p,0,0,940,330,48);txt(o.c1,'PERSI IN 4 ANNI',0,-102,44,'#1B9F81','bold');o.num=txt(o.c1,'−9.400 €',0,40,150,RED,'bold');
 ['2023','2024','2025','2026'].forEach((y,k)=>{const g=el('g',{transform:'translate('+(-255+k*170)+' 115)'},o.c1);el('rect',{x:-72,y:-26,width:144,height:52,rx:26,fill:'#0B4A50'},g);txt(g,y,0,12,32,'#fff','bold');});o.c1._x=540;
 o.m=['MULTA','ERRORE'].map((s,k)=>{const g=card(p,0,0,440,170,44);const c=el('g',{transform:'translate(-130 0)'},g);crossC(c,46);txt(g,s,-62,19,52,INK,'bold','start');g._x=[300,780][k];return g;});
 o.c3=card(p,0,0,940,180,46);const bk=el('g',{transform:'translate(-350 0)',filter:'url(#g_sh3)'},o.c3);el('rect',{x:-58,y:-70,width:116,height:140,rx:14,fill:'#0B4A50',stroke:'#fff','stroke-width':6},bk);el('rect',{x:-40,y:-70,width:8,height:140,fill:'#1B9F81'},bk);txt(bk,'§',8,30,86,YEL,'bold');
 txt(o.c3,'UNA REGOLA SCRITTA',-262,-14,52,INK,'bold','start');txt(o.c3,'NELLA LEGGE',-262,50,42,'#1B9F81','bold','start');o.c3._x=540;
 o.cap=capV(p,['QUEI SOLDI','NON TORNANO PIÙ']);return o;},
 update(t,o){const i=0;const a=plan(i,['con una pensione','novemilaquattrocento','Non per una multa','non per un errore','Per una regola']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.c0,400,120);rise(t,a[1],.9,o.c1,690,120);
  o.num.textContent='−'+fmt(Math.round(9400*eo3(seg(t,a[1],a[1]+.9))/100)*100)+' €';
  rise(t,a[2],.9,o.m[0],1000,100);rise(t,a[3],.9,o.m[1],1000,100);
  rise(t,a[4],.9,o.c3,1230,120);
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 2: PREZZI CONTRO PENSIONE - grafico a due barre, la parte persa ----
{D:DUR[1],build(p){const o={};head(p,o,'PREZZI E PENSIONE',1);
 o.pg=pillS(p,'OGNI GENNAIO',560,54,'#0B4A50');o.pg._x=540;
 o.ch=card(p,0,0,940,600,48);el('rect',{x:-390,y:197,width:780,height:6,rx:3,fill:'#9FB4B9'},o.ch);
 el('rect',{x:80,y:-200,width:220,height:400,rx:14,fill:'none',stroke:'#0B4A50','stroke-width':4,'stroke-dasharray':'14 10',opacity:.55},o.ch);
 o.bp=el('rect',{x:-300,y:200,width:220,height:0,rx:14,fill:'url(#g_amber)'},o.ch);o.bn=el('rect',{x:80,y:200,width:220,height:0,rx:14,fill:'url(#g_badge)'},o.ch);
 txt(o.ch,'PREZZI',-190,258,44,INK,'bold');txt(o.ch,'PENSIONE',190,258,44,INK,'bold');
 o.gap=el('g',{},o.ch);el('rect',{x:80,y:-200,width:220,height:160,rx:14,fill:RED,'fill-opacity':.22,stroke:RED,'stroke-width':5,'stroke-dasharray':'12 8'},o.gap);txt(o.gap,'PERSA',190,-106,44,RED,'bold');o.ch._x=540;
 o.dal=pillS(p,'DAL 2023',420,54,'url(#g_red)');
 o.st=stamp(p,'NON SI RECUPERA',800,56,RED);
 o.cap=capV(p,['LA PARTE PERSA','NON TORNA']);return o;},
 update(t,o){const i=1;const a=plan(i,['Ogni gennaio','dovrebbe salire','dal duemilaventitré','solo una parte','non si recupera']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.pg,360,90);rise(t,a[1],.9,o.ch,760,120);
  const g=eo3(seg(t,a[1]+.2,a[1]+.9)),s=eo3(seg(t,a[3],a[3]+.9));
  const hp=400*g,hn=400*g-160*s;o.bp.setAttribute('y',200-hp);o.bp.setAttribute('height',hp);o.bn.setAttribute('y',200-hn);o.bn.setAttribute('height',Math.max(0,hn));
  op(o.gap,seg(t,a[3]+.3,a[3]+.9));
  T(o.dal,540,1140,0,pop(t,a[2]));stampIn(t,o.st,a[4],540,1305,-3);
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 3: LA SOGLIA - sotto niente, sopra la perdita cresce (cifra nascosta) ----
{D:DUR[2],build(p){const o={};head(p,o,'CHI HA PERSO?',2);
 o.ch=card(p,0,0,960,860,50);const c=o.ch;
 el('rect',{x:-410,y:297,width:820,height:6,rx:3,fill:'#9FB4B9'},c);txt(c,'PENSIONE LORDA →',0,372,38,'#5A6E73','bold');
 o.g=el('g',{},c);el('rect',{x:-410,y:222,width:280,height:75,rx:10,fill:'#1B9F81','fill-opacity':.28},o.g);txt(o.g,'NIENTE',-268,40,46,'#13805F','bold');txt(o.g,'PERSO',-268,96,46,'#13805F','bold');const ck=el('g',{transform:'translate(-268 168)'},o.g);check(ck,34,'#13805F');
 o.rp=el('g',{},c);el('path',{d:'M-130 300 L410 300 L410 -190 Z',fill:'url(#g_red)',opacity:.9},o.rp);txt(o.rp,'PERDITA',290,230,40,'#fff','bold');
 o.q=el('g',{},c);el('path',{d:'M-130 -185 V300',fill:'none',stroke:'#0B4A50','stroke-width':6,'stroke-dasharray':'16 12'},o.q);const qb=el('g',{transform:'translate(-130 -255)'},o.q);el('circle',{r:66,fill:YEL,stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},qb);txt(qb,'?',0,34,96,'#7A2A00','bold');
 o.ch1=el('g',{},c);const p1=el('g',{transform:'translate(40 70)'},o.ch1);pillL(p1,'POCO',230,46,'#C98500');const p2=el('g',{transform:'translate(195 -300)'},o.ch1);pillL(p2,'OLTRE 12.000 €',450,44,'url(#g_red)');
 o.ch._x=540;o.cap=capV(p,['NON TUTTI','HANNO PERSO']);return o;},
 update(t,o){const i=2;const a=plan(i,['Ma non tutti','C\'è una cifra','non hai perso niente','la perdita cresce','chi ha perso poco']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.ch,800,120);
  inC(t,o.q,0,0,a[1]);inC(t,o.g,0,0,a[2]);
  const r=eo3(seg(t,a[3],a[3]+.9));o.rp.setAttribute('transform','translate(-130 300) scale('+Math.max(.001,r)+') translate(130 -300)');op(o.rp,seg(t,a[3],a[3]+.3));
  inC(t,o.ch1,0,0,a[4]);
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 4: IL 2027 - giornale con l'ipotesi, timbro, il buco che si allarga ----
{D:DUR[3],build(p){const o={};head(p,o,'E IL 2027?',3);
 o.c0=card(p,0,0,940,190,46);const cl=el('g',{transform:'translate(-340 0)'},o.c0);
 el('rect',{x:-70,y:-74,width:140,height:148,rx:20,fill:'#fff',stroke:RED,'stroke-width':7},cl);el('rect',{x:-70,y:-74,width:140,height:44,rx:18,fill:RED},cl);el('rect',{x:-70,y:-48,width:140,height:18,fill:RED},cl);txt(cl,'GEN',0,-40,28,'#fff','bold');txt(cl,'1',0,52,66,INK,'bold');
 txt(o.c0,'GENNAIO 2027',-236,-12,56,INK,'bold','start');txt(o.c0,'COSA PUÒ SUCCEDERE',-236,50,38,'#1B9F81','bold','start');o.c0._x=540;
 o.np=card(p,0,0,940,420,40);const n=o.np;txt(n,'ULTIME NOTIZIE',-400,-150,34,'#5A6E73','bold','start');el('rect',{x:-410,y:-130,width:820,height:5,fill:'#0B4A50'},n);
 txt(n,'NUOVO TAGLIO',0,-50,84,RED,'bold');txt(n,'ALLA RIVALUTAZIONE?',0,22,56,INK,'bold');
 const pm=el('g',{transform:'translate(0 102)'},n);pillL(pm,'PENSIONI MEDIO ALTE',600,38,'#0B4A50');
 [160,186].forEach((y,k)=>el('rect',{x:-380,y:y,width:k?520:760,height:12,rx:6,fill:'#C9D6D8'},n));o.np._x=540;
 o.st=stamp(p,'NIENTE DI DECISO',720,56,RED);
 o.h=card(p,0,0,940,200,46);o.hole=el('ellipse',{cx:-270,cy:0,rx:50,ry:42,fill:'#0A1C1F',stroke:RED,'stroke-width':7},o.h);
 txt(o.h,'IL BUCO',-150,-12,58,INK,'bold','start');txt(o.h,'SI ALLARGA',-150,50,44,RED,'bold','start');o.h._x=540;
 o.cap=capV(p,['PER ORA','SOLO UN\'IPOTESI']);return o;},
 update(t,o){const i=3;const a=plan(i,['E il duemila','Sui giornali','niente di deciso','il buco si allarga']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.c0,395,120);rise(t,a[1],.9,o.np,745,120);
  stampIn(t,o.st,a[2],540,1062,-4);
  rise(t,a[3],.9,o.h,1285,110);const k=eo3(seg(t,a[3]+.2,a[3]+.9));o.hole.setAttribute('rx',50+50*k);o.hole.setAttribute('ry',42+22*k);o.hole.setAttribute('cx',-270-10*k);
  T(o.cap,540,CAPY,0,pop(t,a[4]));}},
// ---- 5: NEL VIDEO COMPLETO - scontrino, cifra confine, test, tre risposte ----
{D:DUR[4],build(p){const o={};head(p,o,'NEL VIDEO COMPLETO',4);
 o.r=card(p,0,0,940,230,46);const rc=el('g',{transform:'translate(-340 0)',filter:'url(#g_sh3)'},o.r);
 el('path',{d:'M-62 -92 H62 V82 l-15.5 14 l-15.5 -14 l-15.5 14 l-15.5 -14 l-15.5 14 l-15.5 -14 l-15.5 14 l-15.5 -14 Z',fill:'#fff',stroke:'#9FB4B9','stroke-width':4},rc);
 [-58,-24,10,44].forEach((y,k)=>{el('rect',{x:-44,y:y,width:50,height:10,rx:5,fill:'#9FB4B9'},rc);el('rect',{x:14,y:y,width:30,height:10,rx:5,fill:RED},rc);});
 txt(o.r,'LO SCONTRINO',-236,-14,56,INK,'bold','start');txt(o.r,'ANNO PER ANNO',-236,50,42,'#1B9F81','bold','start');o.r._x=540;
 o.f=card(p,0,0,940,210,46);const fi=el('g',{transform:'translate(-340 0)'},o.f);el('circle',{r:64,fill:YEL,stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},fi);txt(fi,'€ ?',0,22,52,'#7A2A00','bold');
 txt(o.f,'LA CIFRA ESATTA',-236,-12,54,INK,'bold','start');txt(o.f,'CHE FA DA CONFINE',-236,48,40,'#1B9F81','bold','start');o.f._x=540;
 o.ts=card(p,0,0,940,240,46);txt(o.ts,'TEST IN 3 DOMANDE',0,-46,54,INK,'bold');[-200,0,200].forEach((x,k)=>{const g=el('g',{transform:'translate('+x+' 50)'},o.ts);circleN(g,44,String(k+1),'url(#g_badge)');});o.ts._x=540;
 o.res=el('g',{},p);[['NIENTE','#13805F',230],['POCO','#C98500',540],['TANTO','url(#g_red)',850]].forEach(d=>{const g=el('g',{transform:'translate('+d[2]+' 0)'},o.res);pillS(g,d[0],270,48,d[1]);});
 o.cap=capV(p,['E TU, QUANTO','HAI PERSO?']);return o;},
 update(t,o){const i=4;const a=plan(i,['lo scontrino','la cifra esatta','un test','niente, poco']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.r,460,120);rise(t,a[1],.9,o.f,750,120);rise(t,a[2],.9,o.ts,1030,120);
  T(o.res,0,1290,0,1);op(o.res,seg(t,a[3],a[3]+.55));o.res.setAttribute('transform','translate(0 '+(1290+(1-sl(t,a[3],.9))*60)+')');
  T(o.cap,540,CAPY,0,pop(t,a[4]));}},
// ---- 6: TELEFONO - tocca il video correlato, iscriviti, mi piace, scrivimi ----
{D:DUR[5],build(p){const o={};head(p,o,'GUARDALO ORA',5);
 o.ph=el('g',{filter:'url(#g_sh)'},p);el('rect',{x:-230,y:-400,width:460,height:800,rx:62,fill:'#0A1C1F',stroke:'#fff','stroke-width':8},o.ph);
 el('rect',{x:-205,y:-365,width:410,height:730,rx:40,fill:'url(#g_bg)'},o.ph);
 const th=el('g',{},o.ph);el('rect',{x:-180,y:-330,width:360,height:330,rx:24,fill:'#1E9096',stroke:'#9BF0DB','stroke-width':4},th);
 txt(th,'PENSIONI',0,-245,56,'#fff','bold');const nn=txt(th,'−9.400 €',0,-140,60,YEL,'bold');nn.setAttribute('stroke','#06282C');nn.setAttribute('stroke-width',10);nn.setAttribute('paint-order','stroke');txt(th,'IN 4 ANNI',0,-60,40,'#fff','bold');
 const rb=el('g',{},o.ph);el('rect',{x:-185,y:170,width:370,height:92,rx:46,fill:YEL,stroke:'#fff','stroke-width':5},rb);el('path',{d:'M-158 192 L-120 216 L-158 240 Z',fill:'#06282C'},rb);txt(rb,'VIDEO CORRELATO',-104,224,24,'#06282C','bold','start');
 o.tap=el('g',{},o.ph);el('circle',{cx:-139,cy:216,r:32,fill:'none',stroke:'#fff','stroke-width':5,opacity:.9},o.tap);
 o.sub=pillS(p,'ISCRIVITI',420,66,'url(#g_red)');o.bl=bell(p,.7);o.lk=thumb(p,1.0);
 o.cap=capV(p,['SCRIVIMI QUANTO PRENDI']);return o;},
 update(t,o){const i=5;const a=plan(i,['Tocca il video','iscriviti','mi piace']);PL[i]=a;headU(t,o);
  T(o.ph,540,725,0,pop(t,a[0]));op(o.tap,seg(t,a[0]+.5,a[0]+.9));
  T(o.sub,330,1300,0,pop(t,a[1]));T(o.bl,645,1300,0,pop(t,a[1]+.45));
  T(o.lk,860,1300,0,pop(t,a[2]));
  T(o.cap,540,CAPY,0,pop(t,a[3]));}},
];
S.forEach(s=>{s.sb=[{s:0,e:s.D}];});
document.querySelector('defs').insertAdjacentHTML('beforeend','<linearGradient id="g_amber" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC93B"/><stop offset="1" stop-color="#C98500"/></linearGradient>');
