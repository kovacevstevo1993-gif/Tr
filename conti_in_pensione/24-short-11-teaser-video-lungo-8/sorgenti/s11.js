// ===== SHORT 11: se vivessi all'estero (teaser video lungo 8). Composizioni NUOVE in ogni blocco =====
// varianti rispetto agli short 8-10 (anti-ripetizione, N.47 "un po' diverso, non stravolto"): avanzamento con aereo su rotta tratteggiata,
// didascalia a carta d'imbarco (talloncino con aereo), bandiere disegnate come nel video 8, bandiere coperte "?" per tenere la curiosita'.
let UID=0;const AMB='#C98500',GRN='#13805F';
function star5(p,cx,cy,r,fill){let d='';for(let i=0;i<10;i++){const a=-Math.PI/2+i*Math.PI/5,rr=i%2?r*0.42:r;d+=(i?'L':'M')+(cx+rr*Math.cos(a)).toFixed(1)+' '+(cy+rr*Math.sin(a)).toFixed(1)+' ';}
 return el('path',{d:d+'Z',fill:fill},p);}
function flag(p,code,w,h){const g=el('g',{},p);const id='fc'+(++UID);const cp=el('clipPath',{id:id},g);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:12},cp);
 const f=el('g',{'clip-path':'url(#'+id+')'},g);const R=(x,y,ww,hh,c)=>el('rect',{x:x,y:y,width:ww,height:hh,fill:c},f);const x0=-w/2,y0=-h/2;
 if(code=='IT'){R(x0,y0,w/3+1,h,'#1F9A4B');R(x0+w/3,y0,w/3+1,h,'#F7F7F2');R(x0+2*w/3,y0,w/3+1,h,'#D7322B');}
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:12,fill:'none',stroke:'#fff','stroke-width':6},g);g.setAttribute('filter','url(#g_sh2)');return g;}
// bandiera coperta: il paese non si dice nello short (cerchio aperto verso il video lungo)
function mflag(p,w){const h=w*2/3;const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:12,fill:'#2C6E73',stroke:'#fff','stroke-width':6},g);
 el('rect',{x:-w/2+6,y:-h/2+6,width:w-12,height:h*0.22,rx:8,fill:'#fff','fill-opacity':.12},g);
 txt(g,'?',0,h*0.27,h*0.78,'#FFD43B','bold');return g;}
function planeIco(p,s,col){const g=el('g',{transform:'scale('+s+')',filter:'url(#g_sh2)'},p);
 el('path',{d:'M-110 0 Q-110 -16 -90 -16 L90 -16 Q130 -16 140 0 Q130 16 90 16 L-90 16 Q-110 16 -110 0 Z',fill:'#fff'},g);
 el('path',{d:'M-10 -14 L-60 -110 L-30 -110 L40 -14 Z M-10 14 L-60 110 L-30 110 L40 14 Z',fill:col||AMB},g);
 el('path',{d:'M-95 -12 L-120 -55 L-102 -55 L-75 -12 Z M-95 12 L-120 55 L-102 55 L-75 12 Z',fill:col||AMB},g);return g;}
// avanzamento: rotta tratteggiata con 5 tappe e aereo sulla tappa del blocco
function prog(p,i){const g=el('g',{},p);el('line',{x1:-220,y1:0,x2:220,y2:0,stroke:'#fff','stroke-opacity':.45,'stroke-width':5,'stroke-dasharray':'14 12','stroke-linecap':'round'},g);
 for(let k=0;k<5;k++)el('circle',{cx:-220+k*110,cy:0,r:11,fill:k<i?'#FFB020':'#2C6E73',stroke:'#fff','stroke-width':3},g);
 const pl=el('g',{transform:'translate('+(-220+i*110)+' 0)'},g);planeIco(pl,.3,'#FFB020');return g;}
// didascalia a carta d'imbarco: talloncino a sinistra con aereo, linea tratteggiata
function capV(p,lines,fs){fs=fs||58;const mx=Math.max(...lines.map(l=>l.length));fs=Math.min(fs,(1000-230)/(mx*0.76));const w=Math.min(1000,mx*fs*0.76+230);const h=lines.length*(fs*1.42)+54;const c=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:'#06303A',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:'none',stroke:'#FFB020','stroke-width':5},c);
 el('line',{x1:-w/2+120,y1:-h/2+14,x2:-w/2+120,y2:h/2-14,stroke:'#FFB020','stroke-width':4,'stroke-dasharray':'10 9'},c);
 const pl=el('g',{transform:'translate('+(-w/2+60)+' 0) rotate(-35)'},c);planeIco(pl,.26,'#FFB020');
 lines.forEach((l,i)=>txt(c,l,60,-h/2+27+fs*1.08+i*fs*1.42,fs,'#FFFFFF','bold'));return c;}
function playI(p){const g=el('g',{filter:'url(#g_sh2)'},p);el('rect',{x:-70,y:-50,width:140,height:100,rx:26,fill:RED,stroke:'#fff','stroke-width':6},g);el('path',{d:'M-16 -24 L26 0 L-16 24Z',fill:'#fff'},g);return g;}
function avatar(p,col){const g=el('g',{},p);el('circle',{r:46,fill:col,stroke:'#fff','stroke-width':6},g);el('circle',{cy:-10,r:16,fill:'#fff'},g);el('path',{d:'M-26 30 Q0 -4 26 30Z',fill:'#fff'},g);return g;}
function bubble(p,w,h,fill){const g=el('g',{filter:'url(#g_sh)'},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:40,fill:fill,stroke:'#fff','stroke-width':4},g);
 el('path',{d:`M${-w/2+30} ${h/2-4} l40 0 l-60 34 Z`,fill:fill},g);return g;}
function building(p){const g=el('g',{filter:'url(#g_sh2)'},p);el('path',{d:'M-62 -24 L0 -64 L62 -24Z',fill:'#0B4A50',stroke:'#fff','stroke-width':5,'stroke-linejoin':'round'},g);
 [-44,-15,15,44].forEach(x=>el('rect',{x:x-8,y:-20,width:16,height:58,rx:3,fill:'#fff'},g));el('rect',{x:-66,y:40,width:132,height:16,rx:4,fill:'#0B4A50',stroke:'#fff','stroke-width':4},g);return g;}
function coinsDown(p){const g=el('g',{filter:'url(#g_sh2)'},p);[22,0,-22].forEach((y,k)=>{el('ellipse',{cx:-18,cy:y+12,rx:40,ry:14,fill:'#B7860B'},g);el('ellipse',{cx:-18,cy:y,rx:40,ry:14,fill:'#FFC93B',stroke:'#fff','stroke-width':3},g);});
 el('path',{d:'M40 -40 H62 V14 H80 L51 50 L22 14 H40Z',fill:RED,stroke:'#fff','stroke-width':4,'stroke-linejoin':'round'},g);return g;}
function lockR(p){const g=el('g',{filter:'url(#g_sh2)'},p);el('path',{d:'M-30 -6 V-34 a30 30 0 0 1 60 0 V-6',fill:'none',stroke:'#0B4A50','stroke-width':13,'stroke-linecap':'round'},g);
 el('rect',{x:-46,y:-8,width:92,height:72,rx:16,fill:RED,stroke:'#fff','stroke-width':6},g);el('circle',{cx:0,cy:24,r:10,fill:'#fff'},g);return g;}
function docSeal(p){const g=el('g',{filter:'url(#g_sh2)'},p);el('rect',{x:-50,y:-66,width:100,height:132,rx:10,fill:'#fff',stroke:'#9FB4B9','stroke-width':4},g);
 [-44,-22,0].forEach(y=>el('rect',{x:-34,y:y,width:68,height:9,rx:4,fill:'#C9D6D8'},g));el('circle',{cx:16,cy:36,r:22,fill:AMB,stroke:'#fff','stroke-width':4},g);el('path',{d:'M6 36 l7 8 l14 -15',fill:'none',stroke:'#fff','stroke-width':6,'stroke-linecap':'round','stroke-linejoin':'round'},g);return g;}
function eyeO(p){const g=el('g',{filter:'url(#g_sh2)'},p);el('path',{d:'M-70 0 Q0 -60 70 0 Q0 60 -70 0Z',fill:'#fff',stroke:'#0B4A50','stroke-width':6,'stroke-linejoin':'round'},g);
 el('circle',{r:26,fill:'#1B9F81'},g);el('circle',{r:12,fill:'#0A1C1F'},g);return g;}
function thumb(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-96*s,y:-8*s,width:44*s,height:96*s,rx:10*s,fill:'#0B4A50',stroke:'#fff','stroke-width':6*s},g);
 el('path',{d:`M${-40*s} ${-4*s} L${-6*s} ${-78*s} Q${20*s} ${-96*s} ${32*s} ${-64*s} L${24*s} ${-26*s} H${86*s} Q${112*s} ${-24*s} ${104*s} ${8*s} L${92*s} ${62*s} Q${86*s} ${88*s} ${60*s} ${88*s} H${-40*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);return g;}
function tri2(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);el('path',{d:`M0 ${-s} L${s*1.05} ${s*.8} L${-s*1.05} ${s*.8}Z`,fill:YEL,stroke:'#fff','stroke-width':6,'stroke-linejoin':'round'},g);txt(g,'!',0,s*0.55,s*1.2,'#7A2A00','bold');return g;}
function fade(t,n,x,y,a){T(n,x,y+(1-sl(t,a,.9))*60,0,1);op(n,seg(t,a,a+.55));}
const S=[
// ---- 1: Italia contro un paese coperto ----
{D:DUR[0],build(p){const o={};head(p,o,'ALL\'ESTERO',0);
 o.q=card(p,0,0,940,200,46);const pq=el('g',{transform:'translate(-345 0) rotate(-20)'},o.q);planeIco(pq,.5);
 txt(o.q,'LA TUA PENSIONE',-235,-10,54,INK,'bold','start');txt(o.q,'ALL\'ESTERO?',-235,54,44,'#1B9F81','bold','start');o.q._x=540;
 o.it=card(p,0,0,940,250,46);const fi=el('g',{transform:'translate(-335 0)'},o.it);flag(fi,'IT',150,100);
 txt(o.it,'IN ITALIA',-220,-56,38,'#1B9F81','bold','start');txt(o.it,'2.000 € LORDI',-220,12,60,INK,'bold','start');
 o.ir=el('g',{},o.it);o.irn=txt(o.ir,'IRPEF −5.100 € L\'ANNO',-220,78,42,RED,'bold','start');o.it._x=540;
 o.pl=el('g',{},p);const pp=el('g',{transform:'rotate(90)'},o.pl);planeIco(pp,.42,'#FFB020');
 o.ex=card(p,0,0,940,250,46);const fe=el('g',{transform:'translate(-335 0)'},o.ex);mflag(fe,150);
 txt(o.ex,'IN UN PAESE ESTERO',-220,-56,38,'#1B9F81','bold','start');
 o.gf=el('g',{},o.ex);txt(o.gf,'SECONDO LE GUIDE FISCALI',-220,78,30,'#5A6E73','bold','start');
 o.tn=el('g',{},o.ex);o.tnn=txt(o.tn,'+5.100 € L\'ANNO',-220,12,60,GRN,'bold','start');o.ex._x=540;
 o.cap=capV(p,['QUANTO TI RESTEREBBE','IN PIÙ OGNI ANNO?']);return o;},
 update(t,o){const i=0;const a=plan(i,['Se vivessi','Con duemila','cinquemilacento','In un paese','secondo le guide','li terresti tutti']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.q,420,120);rise(t,a[1],.9,o.it,730,120);
  inC(t,o.ir,0,0,a[2]);o.irn.textContent='IRPEF −'+fmt(Math.round(5100*eo3(seg(t,a[2],a[2]+.9))/100)*100)+' € L\'ANNO';
  T(o.pl,540,930+(1-sl(t,a[3],.9))*-50,0,1);op(o.pl,seg(t,a[3],a[3]+.55));rise(t,a[3]+.2,.9,o.ex,1130,120);
  inC(t,o.gf,0,0,a[4]);inC(t,o.tn,0,0,a[5]);o.tnn.textContent='+'+fmt(Math.round(5100*eo3(seg(t,a[5],a[5]+.9))/100)*100)+' € L\'ANNO';
  T(o.cap,540,CAPY,0,pop(t,a[6]));}},
// ---- 2: la regola (rotta Italia -> ?) e tre paesi coperti ----
{D:DUR[1],build(p){const o={};head(p,o,'LA REGOLA',1);
 o.r=card(p,0,0,940,300,46);txt(o.r,'PENSIONE PRIVATA INPS',0,-92,40,'#1B9F81','bold');
 const f1=el('g',{transform:'translate(-320 8)'},o.r);flag(f1,'IT',120,80);const f2=el('g',{transform:'translate(320 8)'},o.r);mflag(f2,120);
 el('path',{d:'M-245 8 Q0 -70 245 8',fill:'none',stroke:'#1B9F81','stroke-width':6,'stroke-dasharray':'16 12','stroke-linecap':'round'},o.r);
 o.rp=el('g',{},o.r);planeIco(o.rp,.32,AMB);
 o.rt=el('g',{},o.r);txt(o.rt,'TASSE SOLO DOVE VIVI DAVVERO',0,112,40,INK,'bold');o.r._x=540;
 o.n=card(p,0,0,940,190,46);const dn=el('g',{transform:'translate(-370 0) scale(.95)'},o.n);docSeal(dn);
 txt(o.n,'IL PAESE NUOVO TI TASSA',-285,-8,42,INK,'bold','start');txt(o.n,'CON LE SUE REGOLE',-285,52,38,'#1B9F81','bold','start');o.n._x=540;
 o.c=[['PAGHI','POCO',AMB],['OGGI PAGHI','0 €',GRN],['IL PARADISO','FINITO',RED]].map((d,k)=>{const g=card(p,0,0,290,330,40);
  const fg=el('g',{transform:'translate(5 -82)'},g);mflag(fg,120);txt(g,d[0],5,40,32,'#5A6E73','bold');txt(g,d[1],5,112,58,d[2],'bold');g._x=215+k*325;return g;});
 o.cap=capV(p,['STESSA PENSIONE,','CONTI DIVERSI']);return o;},
 update(t,o){const i=1;const a=plan(i,['pensioni private','soltanto dove vivi','Ma il paese nuovo','dove paghi poco','dove oggi non paghi','il paradiso']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.r,440,120);const u=eo3(seg(t,a[0]+.6,a[1]+.9));const x=-245+430*u,y=8-78*(1-Math.pow(2*u-1,2))*(u>0?1:0);T(o.rp,x,y,u>0?-12+24*u:0,1);op(o.rp,seg(t,a[0]+.3,a[0]+.9));
  inC(t,o.rt,0,0,a[1]);rise(t,a[2],.9,o.n,775,120);
  o.c.forEach((c,k)=>rise(t,a[3+k],.9,c,1100,110));
  T(o.cap,540,CAPY,0,pop(t,a[6]));}},
// ---- 3: tre trappole ----
{D:DUR[2],build(p){const o={};head(p,o,'PRIMA DI SOGNARE',2);
 o.h=card(p,0,0,940,190,46);const th=el('g',{transform:'translate(-350 6)'},o.h);tri2(th,58);
 txt(o.h,'CI SONO',-250,-12,40,'#5A6E73','bold','start');txt(o.h,'3 TRAPPOLE',-250,56,66,RED,'bold','start');o.h._x=540;
 const row=(n,t1,t2,ico)=>{const g=card(p,0,0,940,200,46);const c=el('g',{transform:'translate(-365 0)'},g);circleN(c,56,n,'url(#g_red)');
  txt(g,t1,-275,-10,46,INK,'bold','start');const s=el('g',{},g);txt(s,t2,-275,52,34,RED,'bold','start');const ic=el('g',{transform:'translate(385 0)'},g);ico(ic);g._x=540;g._s=s;return g;};
 o.r1=row('1','CHI HA LAVORATO','PER LO STATO',building);
 o.r2=row('2','CHI PRENDE POCO','PUÒ AVERE MENO DI PRIMA',coinsDown);
 o.r3=row('3','PUÒ BLOCCARTI','LA PENSIONE',lockR);
 o.cap=capV(p,['DA CONOSCERE','PRIMA DI PARTIRE']);return o;},
 update(t,o){const i=2;const a=plan(i,['tre trappole','per lo Stato','chi prende poco','con meno di prima','bloccarti']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.h,410,120);rise(t,a[1],.9,o.r1,670,120);
  rise(t,a[2],.9,o.r2,905,120);T(o.r2._s,0,0,0,1);op(o.r2._s,seg(t,a[3],a[3]+.55));
  rise(t,a[4],.9,o.r3,1140,120);
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 4: due promesse da controllare ----
{D:DUR[3],build(p){const o={};head(p,o,'OCCHIO',3);
 o.h=card(p,0,0,940,170,46);const eh=el('g',{transform:'translate(-345 0) scale(.9)'},o.h);eyeO(eh);txt(o.h,'ALLE PROMESSE',-245,20,58,INK,'bold','start');o.h._x=540;
 o.a=card(p,0,0,940,300,46);const fa=el('g',{transform:'translate(-335 -30)'},o.a);mflag(fa,140);
 txt(o.a,'IL PAESE DOVE OGGI',-225,-62,36,'#5A6E73','bold','start');txt(o.a,'0 € DI TASSE',-225,10,62,GRN,'bold','start');
 o.as=el('g',{},o.a);const sa=el('g',{transform:'translate(40 92) rotate(-2)'},o.as);stamp(sa,'LA REGOLA PUÒ CAMBIARE',720,38,AMB);o.a._x=540;
 o.b=card(p,0,0,940,260,46);txt(o.b,'7%',-300,40,120,INK,'bold');
 txt(o.b,'TASSA PER CHI VA',-150,-46,36,'#5A6E73','bold','start');txt(o.b,'A VIVERE AL SUD',-150,16,50,INK,'bold','start');
 o.bs=el('g',{},o.b);txt(o.bs,'PICCOLI COMUNI',-150,76,36,'#1B9F81','bold','start');o.b._x=540;
 o.nv=el('g',{},p);stamp(o.nv,'CON LA PENSIONE INPS NON VALE',900,40,RED);
 o.cap=capV(p,['QUELLO CHE SENTI','NON SEMPRE VALE']);return o;},
 update(t,o){const i=3;const a=plan(i,['occhio alle promesse','Il paese dove oggi','cambiare la regola','tassa al sette','piccoli comuni','non vale']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.h,390,120);rise(t,a[1],.9,o.a,660,120);
  const s=seg(t,a[2],a[2]+.9);T(o.as,0,0,0,s>0?lerp(1.3,1,eo3(s)):0);op(o.as,clamp(s*2.5));
  rise(t,a[3],.9,o.b,995,120);inC(t,o.bs,0,0,a[4]);
  stampIn(t,o.nv,a[5],540,1240,-3);
  T(o.cap,540,CAPY,0,pop(t,a[6]));}},
// ---- 5: quale paese conviene, video correlato, mi piace, iscriviti, commento ----
{D:DUR[4],build(p){const o={};head(p,o,'IL CONTO VERO',4);
 o.q=card(p,0,0,940,330,46);txt(o.q,'QUALE PAESE CONVIENE?',0,-104,48,INK,'bold');
 [-270,0,270].forEach(x=>{const f=el('g',{transform:'translate('+x+' -12)'},o.q);mflag(f,110);});
 o.ch=el('g',{},o.q);['1.000 €','1.500 €','2.000 €'].forEach((s,k)=>{const c=el('g',{transform:'translate('+(-270+k*270)+' 98)'},o.ch);pillL(c,s,240,38,'#0B4A50');});o.q._x=540;
 o.vc=card(p,0,0,940,200,46);const pv=el('g',{transform:'translate(-350 0)'},o.vc);playI(pv);
 txt(o.vc,'VIDEO CORRELATO',-250,-10,54,INK,'bold','start');txt(o.vc,'QUI SOTTO: TOCCALO ADESSO',-250,52,36,'#1B9F81','bold','start');o.vc._x=540;
 o.lk=thumb(p,.8);
 o.sub=el('g',{},p);pillS(o.sub,'ISCRIVITI',520,64,'url(#g_red)');const bb=el('g',{transform:'translate(300 -4)'},o.sub);bell(bb,.5);
 o.cm=el('g',{},p);const av=el('g',{transform:'translate(-380 0)'},o.cm);avatar(av,'#5A6E73');const cb=el('g',{transform:'translate(70 0)'},o.cm);bubble(cb,700,160,'#FFFFFF');
 txt(cb,'SCRIVILO NEI COMMENTI',-310,-28,32,'#5A6E73','bold','start');txt(cb,'TU DOVE ANDRESTI?',-310,42,50,GRN,'bold','start');
 o.cap=capV(p,['TOCCA IL','VIDEO CORRELATO']);return o;},
 update(t,o){const i=4;const a=plan(i,['Quale paese','mille','video correlato','metti mi piace','iscriviti','tu dove andresti']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.q,445,120);inC(t,o.ch,0,0,a[1]);rise(t,a[2],.9,o.vc,775,120);
  T(o.lk,175,1010,0,pop(t,a[3]));T(o.sub,590,1010,0,pop(t,a[4]));
  fade(t,o.cm,540,1240,a[5]);
  T(o.cap,540,CAPY,0,pop(t,a[6]));}},
];
S.forEach(s=>{s.sb=[{s:0,e:s.D}];});
