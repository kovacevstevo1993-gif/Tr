// ===== SHORT 9 - teaser video lungo 7 (1080x1920, 30 fps) =====
// Regola n.5: movimenti LENTI (>=0.7 s), tutto completo almeno 0.5 s prima della fine, poi FERMO. Fascia y 330-680 libera per le didascalie di CapCut.
const eob2=x=>{const c1=1.0,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const pop=(t,a,d)=>Math.max(0,eob2(seg(t,a,a+(d||.9))));
const sl=(t,a,d)=>eo3(seg(t,a,a+(d||.9)));
function ttl(p,s,size,fill){const t=txt(p,s,0,0,size,fill||'#fff','bold');t.setAttribute('stroke','#06282C');t.setAttribute('stroke-width',size*0.16);t.setAttribute('stroke-linejoin','round');t.setAttribute('paint-order','stroke');return t;}
function person(p,shirt,hair){const g=el('g',{},p);
 el('path',{d:'M-135 232 Q-135 92 0 92 Q135 92 135 232 Z',fill:shirt,stroke:'#fff','stroke-width':7,'stroke-linejoin':'round',filter:'url(#g_sh2)'},g);
 el('path',{d:'M-38 98 L0 158 L38 98 Z',fill:'#fff'},g);el('path',{d:'M-11 158 L0 226 L11 158 Z',fill:'#0B3A3F'},g);
 el('rect',{x:-26,y:48,width:52,height:56,rx:16,fill:'#EDBE92'},g);
 el('circle',{cx:0,cy:0,r:80,fill:'#F7D3B0',stroke:'#fff','stroke-width':6},g);
 el('path',{d:'M-82 -8 Q-84 -96 0 -96 Q84 -96 82 -8 Q44 -52 -8 -50 Q-52 -48 -82 -8Z',fill:hair},g);
 el('circle',{cx:-27,cy:10,r:9,fill:'#0B3A3F'},g);el('circle',{cx:27,cy:10,r:9,fill:'#0B3A3F'},g);
 el('path',{d:'M-28 40 Q0 66 28 40',fill:'none',stroke:'#B5523B','stroke-width':8,'stroke-linecap':'round'},g);return g;}
function eye(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:'M-120 0 Q0 -105 120 0 Q0 105 -120 0Z',fill:'#fff',stroke:'#0B4A50','stroke-width':8,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:0,r:44,fill:'#1B9F81'},g);el('circle',{cx:0,cy:0,r:20,fill:'#0A1C1F'},g);
 el('line',{x1:-100,y1:-80,x2:100,y2:80,stroke:RED,'stroke-width':20,'stroke-linecap':'round'},g);return g;}
function check(p,r,col){const g=el('g',{},p);el('circle',{r:r,fill:col||'#1B9F81',stroke:'#fff','stroke-width':r*.16},g);
 el('path',{d:`M${-r*.45} ${r*.02} l${r*.3} ${r*.32} l${r*.6} ${-r*.66}`,fill:'none',stroke:'#fff','stroke-width':r*.26,'stroke-linecap':'round','stroke-linejoin':'round'},g);return g;}
function crossC(p,r){const g=el('g',{},p);el('circle',{r:r,fill:RED,stroke:'#fff','stroke-width':r*.16},g);
 el('path',{d:`M${-r*.4} ${-r*.4} L${r*.4} ${r*.4} M${r*.4} ${-r*.4} L${-r*.4} ${r*.4}`,stroke:'#fff','stroke-width':r*.26,'stroke-linecap':'round'},g);return g;}
function lockG(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-38*s} ${-10*s} V${-50*s} a${38*s} ${38*s} 0 0 1 ${76*s} 0 V${-10*s}`,fill:'none',stroke:'#fff','stroke-width':16*s,'stroke-linecap':'round'},g);
 el('rect',{x:-58*s,y:-12*s,width:116*s,height:90*s,rx:20*s,fill:YEL,stroke:'#fff','stroke-width':7*s},g);el('circle',{cx:0,cy:30*s,r:12*s,fill:'#7A2A00'},g);return g;}
function bigArrow(p){return el('path',{d:'M-60 -90 H60 V0 H110 L0 110 L-110 0 H-60Z',fill:YEL,stroke:'#fff','stroke-width':8,'stroke-linejoin':'round',filter:'url(#g_sh2)'},p);}

function topLabelV(p,s){const fs=58,sp=8;const w=s.length*(fs*0.72+sp)+80;const t=el('g',{},p);
 el('polygon',{points:'-16,-16 0,-32 16,-16 0,0',fill:'#7FF0D2',transform:'translate('+(-w/2+18)+' 0)'},t);
 const x=txt(t,s,-w/2+64,fs*0.36,fs,'#7FF0D2','bold','start');x.setAttribute('letter-spacing',sp);return t;}
function capV(p,lines,fs){fs=fs||58;const mx=Math.max(...lines.map(l=>l.length));fs=Math.min(fs,(1000-130)/(mx*0.76));const w=Math.min(1000,mx*fs*0.76+130);const h=lines.length*(fs*1.42)+54;const c=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:Math.min(60,h/2),fill:'#06303A',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:Math.min(60,h/2),fill:'none',stroke:'#FFB020','stroke-width':6},c);
 lines.forEach((l,i)=>txt(c,l,0,-h/2+27+fs*1.08+i*fs*1.42,fs,'#FFFFFF','bold'));return c;}
const CAPY=1560;
// entrata dal basso con dissolvenza (lenta): nessun elemento entra da fuori quadro
function rise(t,a,d,n,y,dy,sc){const k=sl(t,a,d||.9);T(n,n._x,y+(1-k)*(dy||140),0,(sc||1));op(n,seg(t,a,a+(d||.9)*.6));}

function thumb(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-96*s,y:-8*s,width:44*s,height:96*s,rx:10*s,fill:'#0B4A50',stroke:'#fff','stroke-width':6*s},g);
 el('path',{d:`M${-40*s} ${-4*s} L${-6*s} ${-78*s} Q${20*s} ${-96*s} ${32*s} ${-64*s} L${24*s} ${-26*s} H${86*s} Q${112*s} ${-24*s} ${104*s} ${8*s} L${92*s} ${62*s} Q${86*s} ${88*s} ${60*s} ${88*s} H${-40*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);return g;}
function bell(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
function card(p,x,y,w,h,r){const g=el('g',{},p);plateRect(g,-w/2,-h/2,w,h,r||50);return g;}

// tempi sulla voce (stima a caratteri dal testo del blocco e dalla durata dello screenshot, regola N.16).
// Regole N.15/N.18: comparsa 0,9 s, ogni elemento resta fino a fine scena, distanza >= 1,0 s tra elementi, ultimo completo entro l'80 % del blocco.
const DUR=[400,322,322,298,304,257].map(x=>x/30);
const TX=[
"Rivalutazione tagliata: con una pensione da tremila euro lordi, novemilaquattrocento euro persi in quattro anni. Non per una multa, non per un errore. Per una regola scritta nella legge. E quei soldi non tornano più.",
"Ogni gennaio la pensione dovrebbe salire quanto salgono i prezzi. Ma dal duemilaventitré, per molti pensionati, è salita solo una parte. E la parte persa non si recupera, neanche negli anni dopo.",
"Ma non tutti hanno perso. C'è una cifra sotto la quale non hai perso niente. Appena la superi, la perdita cresce in fretta: c'è chi ha perso poco, e chi ha perso oltre dodicimila euro lordi.",
"E il duemilaventisette? Sui giornali gira l'ipotesi di un nuovo taglio per le pensioni medio alte. Per ora non c'è niente di deciso. Ma se passa, il buco si allarga ancora.",
"Nel video completo: lo scontrino anno per anno, la cifra esatta che fa da confine, e un test in tre domande per capire se tu hai perso niente, poco o tanto.",
"Tocca il video correlato e fai il test adesso! Poi iscriviti a Conti in Pensione e metti mi piace. E scrivimi quanto prendi: ti dico se hai perso anche tu!"];
function vt(i,frag){const s=TX[i];const k=s.indexOf(frag);if(k<0)throw new Error('frag '+frag);return 0.15+(DUR[i]-0.6)*k/s.length-0.15;}
const GAP=1.0;
// tempo di avvio di ogni elemento: sulla parola, poi distanza minima e ultimo entro l'80 %
function plan(i,frags){const n=frags.length+1,lim=0.8*DUR[i]-0.9;let t=frags.map(f=>vt(i,f)).concat([99]);
 t[0]=Math.max(t[0],GAP);for(let k=1;k<n;k++)t[k]=Math.max(t[k],t[k-1]+GAP);
 for(let k=n-1;k>=0;k--){const m=lim-(n-1-k)*GAP;if(t[k]>m)t[k]=m;}
 return t;}
const PL=[];
function stampIn(t,o,a,x,y,r){const s=seg(t,a,a+.9);T(o,x,y,r||-4,s>0?lerp(1.4,1,eo3(s)):0);op(o,clamp(s*2.5));}
function rowCard(p,n,title,sub,col){const g=card(p,0,0,940,190,46);
 const c=el('g',{transform:'translate(-370 0)'},g);circleN(c,62,n,col||'url(#g_badge)');
 txt(g,title,-270,sub?-4:22,50,INK,'bold','start');if(sub)txt(g,sub,-270,58,38,'#1B9F81','bold','start');g._x=540;return g;}
function bigCard(p,top,main,sub,mainFill,w,h){h=h||260;const g=card(p,0,0,w||900,h,48);txt(g,top,0,-h*0.2,42,'#1B9F81','bold');txt(g,main,0,h*0.22,100,mainFill||INK,'bold');if(sub)txt(g,sub,0,h*0.4,36,'#5A6E73','bold');g._x=540;return g;}

// ---- migliorie short 8 (poche, regola N.12): filetto verde sulle schede, barra di avanzamento 6 blocchi, titoletto con riga ----
function card(p,x,y,w,h,r){const g=el('g',{},p);plateRect(g,-w/2,-h/2,w,h,r||50);el('rect',{x:-w/2+16,y:-h/2+30,width:10,height:h-60,rx:5,fill:'#1B9F81'},g);return g;}
function prog(p,i){const g=el('g',{},p);for(let k=0;k<6;k++)el('rect',{x:-255+k*88,y:-6,width:74,height:12,rx:6,fill:k<=i?'#FFB020':'#FFFFFF','fill-opacity':k<=i?1:.28},g);return g;}
function head(p,o,s,i){o.lab=topLabelV(p,s);o.pr=prog(p,i);}
function headU(t,o){T(o.lab,540,130,0,pop(t,0));T(o.pr,540,215,0,1);op(o.pr,seg(t,0,.9));}
function calCard(p,day,num,sub,col){const g=card(p,0,0,940,240,46);
 const c=el('g',{transform:'translate(-330 0)'},g);
 el('rect',{x:-80,y:-90,width:160,height:180,rx:24,fill:'#fff',stroke:col,'stroke-width':8},c);
 el('rect',{x:-80,y:-90,width:160,height:52,rx:20,fill:col},c);el('rect',{x:-80,y:-60,width:160,height:22,fill:col},c);
 txt(c,'NOV',0,-52,32,'#fff','bold');txt(c,num,0,58,86,INK,'bold');
 txt(g,day,-200,-14,54,INK,'bold','start');txt(g,sub,-200,52,38,col,'bold','start');g._x=540;return g;}
function voceRow(p,up,title,sub){const g=card(p,0,0,940,230,46);const col=up?'#13805F':RED;
 const c=el('g',{transform:'translate(-360 0)'},g);el('circle',{r:64,fill:col,stroke:'#fff','stroke-width':9,filter:'url(#g_sh2)'},c);
 el('path',{d:up?'M0 -36 L32 4 H12 V36 H-12 V4 H-32Z':'M0 36 L32 -4 H12 V-36 H-12 V-4 H-32Z',fill:'#fff'},c);
 txt(g,title,-262,-14,54,INK,'bold','start');txt(g,sub,-262,52,40,col,'bold','start');g._x=540;return g;}
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
