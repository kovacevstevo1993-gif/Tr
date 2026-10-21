// ===== SHORT 11 - se vivessi all'estero (teaser video 8) (1080x1920, 30 fps) =====
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
const DUR=[436,436,404,376,453].map(x=>x/30);
const TX=["Se vivessi all'estero con la tua pensione, quanti soldi in più ti resterebbero ogni anno? Con duemila euro lordi, in Italia lasci circa cinquemilacento euro di Irpef. In un paese, secondo le guide fiscali, oggi li terresti tutti.", "Il motivo: per le pensioni private dell'Inps, con diversi paesi, le tasse si pagano soltanto dove vivi davvero. Ma il paese nuovo ti tassa con le sue regole. C'è dove paghi poco, dove oggi non paghi niente, e dove il paradiso non c'è più.", "Prima di sognare, però, ci sono tre trappole. Una riguarda chi ha lavorato per lo Stato. Una riguarda chi prende poco: c'è chi parte per risparmiare e si ritrova con meno di prima. E la terza può bloccarti la pensione.", "E occhio alle promesse. Il paese dove oggi non paghi niente sta discutendo di cambiare la regola. E la tassa al sette per cento per chi va a vivere nei piccoli comuni del Sud? Con la pensione Inps non vale.", "Quale paese conviene con mille, millecinquecento o duemila euro lo trovi nel video correlato qui sotto: toccalo adesso. Se ti piacciono questi conti, metti mi piace e iscriviti a Conti in Pensione. E scrivi nei commenti: tu dove andresti?"];
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
