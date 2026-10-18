// ===== SHORT 10 - iscrizione al canale (1080x1920, 30 fps) =====
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
const DUR=[436,412,436,357,417].map(x=>x/30);
const TX=["Pensione: quanti soldi ti mancano nel cedolino senza che nessuno te lo spieghi? Tredicesima, acconti, addizionali, rivalutazione tagliata. Sono regole scritte, non errori. Ma se non le conosci, te ne accorgi quando i soldi sono già andati.", "Su questo canale le spieghiamo con il conto vero, in euro. Ogni numero lo controlliamo sulle fonti ufficiali prima di dirtelo. Per pochi minuti di video servono ore di ricerche. Lo facciamo perché tu lo sappia prima, non dopo.", "Un esempio: sulla tredicesima da mille euro lordi, a molti ne arrivano circa settecentosettanta. E se ci scrivi nei commenti quanto prendi, ti rispondiamo con il tuo conto: lo facciamo con tutti. Gratis, senza venderti niente.", "Adesso però ci serve una mano da te. Siamo ancora pochi, e vogliamo arrivare a mille iscritti per continuare a fare questi conti. Iscriverti non ti costa niente, basta un tocco. Per noi vuol dire poter andare avanti.", "Iscriviti a Conti in Pensione e metti mi piace. Poi tocca il video correlato: c'è un test in tre domande per scoprire se con la rivalutazione tagliata hai perso niente, poco o tanto. E se sei con noi, scrivi: ci sono!"];
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
S.forEach(s=>{s.sb=[{s:0,e:s.D}];});
document.querySelector('defs').insertAdjacentHTML('beforeend','<linearGradient id="g_amber" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC93B"/><stop offset="1" stop-color="#C98500"/></linearGradient>');