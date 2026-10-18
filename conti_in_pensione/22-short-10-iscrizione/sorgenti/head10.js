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
