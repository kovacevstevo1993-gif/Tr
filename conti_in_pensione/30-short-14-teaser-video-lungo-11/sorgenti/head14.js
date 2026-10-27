// ===== SHORT 14 - teaser video lungo 11 (aumento pensioni gennaio 2027) (1080x1920, 30 fps) =====
// Regole N.15/N.18: comparsa 0.9 s, elementi che restano fino a fine scena, distanza >= 1.0 s, ultimo completo entro l'80 %, poi tutto FERMO.
// Look NUOVO rispetto agli short 8-13 (N.47 "un po' piu diverse, piu professionali, piu elementi"): titoletto a pillola scura con disco % e BARRE CHE SALGONO,
// schede con ANGOLO PIEGATO, didascalia a SCONTRINO (bordo a denti, fascia scura con moneta), sfondo con simboli % e euro che salgono piano.
const eob2=x=>{const c1=1.0,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const pop=(t,a,d)=>Math.max(0,eob2(seg(t,a,a+(d||.9))));
const sl=(t,a,d)=>eo3(seg(t,a,a+(d||.9)));
const GRN='#13805F',DK='#0B4A50',ORG='#E8832A',AMB='#FFB020';
function fade(t,n,x,y,a){T(n,x,y+(1-sl(t,a,.9))*60,0,1);op(n,seg(t,a,a+.55));}
function rise(t,a,d,n,y,dy){const k=sl(t,a,d||.9);T(n,n._x,y+(1-k)*(dy||140),0,1);op(n,seg(t,a,a+(d||.9)*.6));}
function stampIn(t,o,a,x,y,r){const s=seg(t,a,a+.9);T(o,x,y,r||-4,s>0?lerp(1.4,1,eo3(s)):0);op(o,clamp(s*2.5));}
// scheda con angolo piegato in alto a destra
function dcard(p,w,h,r,fill){const g=el('g',{},p);const c=52;r=r||44;
 el('path',{d:`M${-w/2} ${-h/2+r} Q${-w/2} ${-h/2} ${-w/2+r} ${-h/2} H${w/2-c} L${w/2} ${-h/2+c} V${h/2-r} Q${w/2} ${h/2} ${w/2-r} ${h/2} H${-w/2+r} Q${-w/2} ${h/2} ${-w/2} ${h/2-r}Z`,fill:fill||'url(#g_paper)',stroke:'#fff','stroke-width':4,'stroke-linejoin':'round',filter:'url(#g_sh)'},g);
 el('path',{d:`M${w/2-c} ${-h/2} V${-h/2+c} H${w/2}Z`,fill:'#BFD0D3',stroke:'#fff','stroke-width':3,'stroke-linejoin':'round'},g);return g;}
// titoletto: pillola scura con disco % + barre che salgono (avanzamento su 5 blocchi)
function head(p,o,s,i){o.lab=el('g',{},p);
 el('rect',{x:-390,y:-48,width:780,height:96,rx:48,fill:'#06303A',stroke:AMB,'stroke-width':5,filter:'url(#g_sh2)'},o.lab);
 const d=el('g',{transform:'translate(-340 0)'},o.lab);el('circle',{r:36,fill:'url(#g_badge)',stroke:'#fff','stroke-width':5},d);txt(d,'%',0,13,38,'#fff','bold');
 const x=txt(o.lab,s,30,14,38,'#7FF0D2','bold','middle');x.setAttribute('letter-spacing',3);
 o.pr=el('g',{},p);for(let k=0;k<5;k++){const h=18+k*11;el('rect',{x:-150+k*64,y:-h,width:44,height:h,rx:8,fill:k<=i?AMB:'#FFFFFF','fill-opacity':k<=i?1:.3},o.pr);}}
function headU(t,o){T(o.lab,540,130,0,1);op(o.lab,seg(t,0,.9));T(o.pr,540,250,0,1);op(o.pr,seg(t,0,.9));}
// didascalia a scontrino
function capV(p,lines,fs){fs=fs||56;const mx=Math.max(...lines.map(l=>l.length));fs=Math.min(fs,(1000-270)/(mx*0.76));const w=Math.min(1010,mx*fs*0.76+270);const h=lines.length*(fs*1.42)+70;const c=el('g',{},p);
 const n=Math.round(w/34),st=w/n;let pts=[[-w/2,-h/2],[w/2,-h/2],[w/2,h/2-18]];for(let k=1;k<=n;k++){pts.push([w/2-k*st+st/2,h/2]);pts.push([w/2-k*st,h/2-18]);}
 el('polygon',{points:pts.map(q=>q.join(',')).join(' '),fill:'#F5FBFA',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:-h/2,width:130,height:h-18,fill:'#0B4A50'},c);
 el('line',{x1:-w/2+130,y1:-h/2+8,x2:-w/2+130,y2:h/2-26,stroke:'#9BB',  'stroke-width':3,'stroke-dasharray':'8 8'},c);
 coin(c,-w/2+65,-9,46);
 lines.forEach((l,i)=>txt(c,l,65,-h/2+34+fs*1.0+i*fs*1.42,fs,INK,'bold'));c._x=540;return c;}
// sfondo: simboli % e euro che salgono piano (si aggiungono alle bolle del motore)
let BGX=null;
function bgx(t){if(!BGX){const b=document.getElementById('bok');BGX=[];for(let k=0;k<10;k++){const e=el('text',{'font-size':90+(k*29)%90,fill:'#9BF0DB',opacity:.07+(k%3)*.02,'font-family':FONT,'font-weight':'bold','text-anchor':'middle'},b);e.textContent=(k%2?'%':'€');BGX.push([e,(k*131+60)%1000+40,(k*257)%1920,10+(k*5)%14]);}}
 BGX.forEach(([e,x,y,sp],k)=>{e.setAttribute('x',x+22*Math.sin(t*.3+k));e.setAttribute('y',(((y-t*sp)%2000)+2000)%2000-40);});}
const DUR=[341,369,381,382,436].map(x=>x/30);
const TX=["Aumento pensioni a gennaio: la percentuale ufficiale non c'è ancora, ma con la stima più citata su mille euro lordi sono ventinove euro in più. Peccato che sul conto non arrivino ventinove.",
"Perché? Prima di arrivarti in tasca, l'aumento passa per le tasse. E la parte che ti resta non è uguale per ogni pensione: oltre una certa cifra al mese ne tieni meno. Quale cifra? Non la diciamo qui.",
"E le pensioni minime? Lì l'Irpef non c'è, quindi sembra tutto più facile. Invece c'è un extra, previsto dalla legge fino al duemilaventisei: se non viene prorogato, l'aumento vero è più piccolo di quanto fa pensare la percentuale.",
"Il numero ufficiale lo fissa un decreto dei ministeri dell'Economia e del Lavoro, di solito a novembre: quello dell'anno scorso porta la data del diciannove novembre. Quando esce, leggiamo il testo e rifacciamo il conto.",
"La tabella netta, da seicento a tremila euro, la trovi nel video correlato qui sotto: toccalo adesso. Metti mi piace e iscriviti a Conti in Pensione. Poi scrivi nei commenti quanto prendi di pensione lorda: ti rispondiamo con il conto."];
function vt(i,frag){const s=TX[i];const k=s.indexOf(frag);if(k<0)throw new Error('frag '+frag);return 0.15+(DUR[i]-0.6)*k/s.length-0.15;}
const GAP=1.0;
function plan(i,frags){const n=frags.length+1,lim=0.8*DUR[i]-0.9;let t=frags.map(f=>vt(i,f)).concat([99]);
 t[0]=Math.max(t[0],GAP);for(let k=1;k<n;k++)t[k]=Math.max(t[k],t[k-1]+GAP);
 for(let k=n-1;k>=0;k--){const m=lim-(n-1-k)*GAP;if(t[k]>m)t[k]=m;}
 return t;}
const PL=[];
