// ===== SHORT 8 - teaser video lungo 6 (1080x1920, 30 fps) =====
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
const DUR=[311,317,274,322,282,274].map(x=>x/30);
const TX=[
"Cedolino di novembre: quattrocentottanta euro in meno, in una volta sola! Non è un errore dell'Inps e non è una multa. Ma se non sai cos'è, ti prendi un bello spavento...",
"Prima la data. Il primo novembre è domenica, ed è anche Ognissanti. Quindi la pensione arriva lunedì due novembre, in banca e alle Poste. Nessun ritardo.",
"E i titoli su aumenti e arretrati a novembre? Guarda bene a chi sono rivolti. Se la pensione te la paga l'Inps, a novembre non scatta nessun aumento generale.",
"Nel cedolino di novembre invece ci sono due voci che contano. Una arriva, e può toglierti centinaia di euro. L'altra finisce, e a dicembre ti lascia più soldi in banca.",
"Nel video completo: a chi tocca quella trattenuta, il conto passo passo con i numeri, quando non si paga proprio e dove trovare le tre voci nel tuo cedolino.",
"Tocca il video correlato e guardalo adesso! Poi iscriviti a Conti in Pensione e metti mi piace. E scrivimi quanto prendi: ti rispondo con il conto!"];
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
const S=[
// ---- 1: CEDOLINO DI NOVEMBRE -480 ----
{D:DUR[0],build(p){const o={};head(p,o,'PENSIONI NOVEMBRE',0);
 o.c1=bigCard(p,'CEDOLINO DI NOVEMBRE','− 480 €',null,RED,880,270);
 o.pl=pillS(p,'IN UNA VOLTA SOLA',720,58,'#0B4A50');o.pl._x=540;
 o.s1=stamp(p,'NON È UN ERRORE',760,54,RED);
 o.s2=stamp(p,'NON È UNA MULTA',760,54,RED);
 o.cap=capV(p,['COS\'È','QUESTA VOCE?']);return o;},
 update(t,o){const i=0;const a=plan(i,['quattrocentottanta','in una volta','Non è un errore','non è una multa']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.c1,470,120);rise(t,a[1],.9,o.pl,720,100);
  stampIn(t,o.s1,a[2],540,950,-3);stampIn(t,o.s2,a[3],540,1170,3);
  T(o.cap,540,CAPY,0,pop(t,a[a.length-1]));}},
// ---- 2: LA DATA ----
{D:DUR[1],build(p){const o={};head(p,o,'LA DATA',1);
 o.c1=calCard(p,'DOMENICA','1','È ANCHE OGNISSANTI',RED);
 o.ar=bigArrow(p);
 o.c2=calCard(p,'LUNEDÌ 2 NOVEMBRE','2','ARRIVA LA PENSIONE','#13805F');
 o.pl=pillS(p,'BANCA E POSTE',640,58,'#0B4A50');o.pl._x=540;
 o.cap=capV(p,['NESSUN','RITARDO']);return o;},
 update(t,o){const i=1;const a=plan(i,['Il primo novembre','Quindi la pensione','lunedì due','in banca']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.c1,450,120);T(o.ar,540,700,0,.8*pop(t,a[1]));
  rise(t,a[2],.9,o.c2,950,120);rise(t,a[3],.9,o.pl,1210,100);
  T(o.cap,540,CAPY,0,pop(t,a[a.length-1]));}},
// ---- 3: AUMENTI E ARRETRATI? ----
{D:DUR[2],build(p){const o={};head(p,o,'AUMENTI E ARRETRATI?',2);
 o.c1=card(p,0,0,940,250,46);txt(o.c1,'I TITOLI DICONO',0,-44,40,'#1B9F81','bold');txt(o.c1,'«AUMENTI E ARRETRATI',0,26,56,INK,'bold');txt(o.c1,'A NOVEMBRE»',0,92,56,INK,'bold');o.c1._x=540;
 o.pl=pillS(p,'A CHI SONO RIVOLTI?',800,56,'#0B4A50');o.pl._x=540;
 o.c2=card(p,0,0,940,250,46);txt(o.c2,'PENSIONE PAGATA DALL\'INPS',0,-40,44,'#1B9F81','bold');txt(o.c2,'NESSUN AUMENTO',0,40,66,RED,'bold');txt(o.c2,'GENERALE A NOVEMBRE',0,100,40,INK,'bold');o.c2._x=540;
 o.cap=capV(p,['LEGGI BENE','I TITOLI']);return o;},
 update(t,o){const i=2;const a=plan(i,['E i titoli','Guarda bene','nessun aumento']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.c1,460,120);rise(t,a[1],.9,o.pl,720,100);rise(t,a[2],.9,o.c2,990,120);
  T(o.cap,540,CAPY,0,pop(t,a[a.length-1]));}},
// ---- 4: DUE VOCI ----
{D:DUR[3],build(p){const o={};head(p,o,'NEL CEDOLINO',3);
 o.c1=card(p,0,0,940,200,46);txt(o.c1,'NOVEMBRE',0,-20,40,'#1B9F81','bold');txt(o.c1,'DUE VOCI CHE CONTANO',0,48,58,INK,'bold');o.c1._x=540;
 o.r1=voceRow(p,false,'UNA ARRIVA','− CENTINAIA DI EURO');
 o.r2=voceRow(p,true,'UNA FINISCE','+ SOLDI A DICEMBRE');
 o.cap=capV(p,['QUALI SONO?']);return o;},
 update(t,o){const i=3;const a=plan(i,['due voci','Una arriva','L\'altra finisce']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.c1,440,120);rise(t,a[1],.9,o.r1,720,120);rise(t,a[2],.9,o.r2,1010,120);
  T(o.cap,540,CAPY,0,pop(t,a[a.length-1]));}},
// ---- 5: NEL VIDEO COMPLETO ----
{D:DUR[4],build(p){const o={};head(p,o,'NEL VIDEO COMPLETO',4);
 o.r=['A CHI TOCCA LA TRATTENUTA','IL CONTO PASSO PASSO','QUANDO NON SI PAGA','LE 3 VOCI DEL CEDOLINO'].map((s,k)=>{const g=card(p,0,0,940,170,44);
  const c=el('g',{transform:'translate(-370 0)'},g);circleN(c,50,String(k+1),'url(#g_badge)');txt(g,s,-290,16,44,INK,'bold','start');g._x=540;return g;});
 o.cap=capV(p,['GUARDALO FINO','ALLA FINE']);return o;},
 update(t,o){const i=4;const a=plan(i,['a chi tocca','il conto passo','quando non','dove trovare']);PL[i]=a;headU(t,o);
  [0,1,2,3].forEach(k=>rise(t,a[k],.9,o.r[k],[430,640,850,1060][k],110));
  T(o.cap,540,CAPY,0,pop(t,a[a.length-1]));}},
// ---- 6: GUARDA, ISCRIVITI, MI PIACE ----
{D:DUR[5],build(p){const o={};head(p,o,'GUARDALO ORA',5);
 o.pb=playBtn(p);o.pill=pillS(p,'VIDEO CORRELATO',900,70,'#0B4A50');o.pill._x=540;
 o.sub=pillS(p,'ISCRIVITI',440,72,'url(#g_red)');o.bl=bell(p,.7);o.lk=thumb(p,1.0);
 o.nov=pillS(p,'SCRIVIMI QUANTO PRENDI',960,52,'#0B4A50');o.nov._x=540;
 o.cap=capV(p,['GUARDA, ISCRIVITI','E METTI MI PIACE']);return o;},
 update(t,o){const i=5;const a=plan(i,['video correlato','iscriviti','mi piace','scrivimi']);PL[i]=a;headU(t,o);
  T(o.pb,540,560,0,.95*pop(t,.15));
  rise(t,a[0],.9,o.pill,880,90);
  T(o.sub,290,1100,0,pop(t,a[1]));T(o.bl,590,1100,0,pop(t,a[1]+GAP*.5));
  T(o.lk,830,1100,0,pop(t,a[2]));
  rise(t,a[3],.9,o.nov,1330,90);
  T(o.cap,540,CAPY,0,pop(t,a[a.length-1]));}},
];
S.forEach(s=>{s.sb=[{s:0,e:s.D}];});
function playBtn(p){const g=el('g',{filter:'url(#g_sh)'},p);el('rect',{x:-330,y:-205,width:660,height:410,rx:90,fill:'url(#g_red)',stroke:'#fff','stroke-width':10},g);el('path',{d:'M-70 -110 L130 0 L-70 110Z',fill:'#fff','stroke-linejoin':'round',stroke:'#fff','stroke-width':26},g);return g;}
document.querySelector('defs').insertAdjacentHTML('beforeend','<linearGradient id="g_amber" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC93B"/><stop offset="1" stop-color="#C98500"/></linearGradient>');
