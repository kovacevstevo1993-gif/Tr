// ===== SHORT 15 - teaser video lungo 12 (coefficienti di trasformazione 2027) (1080x1920, 30 fps) =====
// Regole N.15/N.18: comparsa 0.9 s, elementi che restano fino a fine scena, distanza >= 1.0 s, ultimo completo entro l'80 %, poi tutto FERMO.
// Look NUOVO rispetto agli short 12-14 (N.47 "un po' piu diverse, piu professionali, piu elementi"): titoletto a LINGUETTA DI TABELLA con griglia e 5 celle di avanzamento,
// schede a BLOCCO NOTE CON SPIRALE (anelli in alto), didascalia a PANNELLO SCURO con righello, sfondo con ETA' (57...71) che salgono piano.
const eob2=x=>{const c1=1.0,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const pop=(t,a,d)=>Math.max(0,eob2(seg(t,a,a+(d||.9))));
const sl=(t,a,d)=>eo3(seg(t,a,a+(d||.9)));
const GRN='#13805F',DK='#0B4A50',ORG='#E8832A',AMB='#FFB020',NAVY='#06303A';
function fade(t,n,x,y,a){T(n,x,y+(1-sl(t,a,.9))*60,0,1);op(n,seg(t,a,a+.55));}
function rise(t,a,d,n,y,dy){const k=sl(t,a,d||.9);T(n,n._x,y+(1-k)*(dy||140),0,1);op(n,seg(t,a,a+(d||.9)*.6));}
function stampIn(t,o,a,x,y,r,s0){const s=seg(t,a,a+.9);T(o,x,y,r||-4,s>0?lerp(s0||1.4,1,eo3(s)):0);op(o,clamp(s*2.5));}
// scheda a blocco note con spirale (centrata in 0,0)
function scard(p,w,h,fill,r){r=r||36;const g=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:r,fill:fill||'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh)'},g);
 const n=Math.max(4,Math.floor((w-120)/70));for(let k=0;k<n;k++){const x=-w/2+60+k*((w-120)/(n-1));
  el('rect',{x:x-9,y:-h/2-20,width:18,height:44,rx:9,fill:'#0B4A50',stroke:'#fff','stroke-width':3},g);el('rect',{x:x-5,y:-h/2-10,width:10,height:20,rx:5,fill:'#9BF0DB'},g);}
 return g;}
// titoletto: linguetta di tabella (griglia 3x2 + testo) + 5 celle di avanzamento
function head(p,o,s,i){o.lab=el('g',{},p);
 el('rect',{x:-400,y:-52,width:800,height:104,rx:20,fill:NAVY,stroke:AMB,'stroke-width':5,filter:'url(#g_sh2)'},o.lab);
 const gi=el('g',{transform:'translate(-350 0)'},o.lab);el('rect',{x:-30,y:-30,width:60,height:60,rx:8,fill:'#fff'},gi);
 [-10,10].forEach(y=>el('line',{x1:-30,y1:y,x2:30,y2:y,stroke:'#0B4A50','stroke-width':3},gi));[-10,10].forEach(x=>el('line',{x1:x,y1:-30,x2:x,y2:30,stroke:'#0B4A50','stroke-width':3},gi));el('rect',{x:-30,y:-30,width:60,height:20,rx:8,fill:AMB},gi);
 const x=txt(o.lab,s,30,14,40,'#7FF0D2','bold','middle');x.setAttribute('letter-spacing',3);
 o.pr=el('g',{},p);for(let k=0;k<5;k++){el('rect',{x:-190+k*80,y:-22,width:68,height:44,rx:8,fill:k<=i?AMB:'#FFFFFF','fill-opacity':k<=i?1:.28,stroke:'#fff','stroke-width':3,'stroke-opacity':.7},o.pr);}}
function headU(t,o){T(o.lab,540,130,0,1);op(o.lab,seg(t,0,.9));T(o.pr,540,250,0,1);op(o.pr,seg(t,0,.9));}
// didascalia: pannello scuro con righello giallo in basso
function capN(p,lines,fs){fs=fs||56;const mx=Math.max(...lines.map(l=>l.length));fs=Math.min(fs,(980-120)/(mx*0.76));const w=Math.min(1000,mx*fs*0.76+120);const h=lines.length*(fs*1.42)+86;const c=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:NAVY,stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2+30,y:h/2-34,width:w-60,height:10,rx:5,fill:AMB},c);
 for(let k=0;k<=12;k++)el('rect',{x:-w/2+30+k*((w-66)/12),y:h/2-52,width:6,height:(k%3==0)?18:10,fill:'#7FF0D2'},c);
 lines.forEach((l,i)=>txt(c,l,0,-h/2+30+fs*1.0+i*fs*1.42,fs,'#fff','bold'));c._x=540;return c;}
// sfondo: eta' (57...71) che salgono piano
let BGX=null;
function bgx(t){if(!BGX){const b=document.getElementById('bok');BGX=[];for(let k=0;k<12;k++){const e=el('text',{'font-size':96+(k*29)%80,fill:'#9BF0DB',opacity:.07+(k%3)*.02,'font-family':FONT,'font-weight':'bold','text-anchor':'middle'},b);e.textContent=String(57+(k*5)%15);BGX.push([e,(k*131+60)%1000+40,(k*257)%1920,10+(k*5)%14]);}}
 BGX.forEach(([e,x,y,sp],k)=>{e.setAttribute('x',x+22*Math.sin(t*.3+k));e.setAttribute('y',(((y-t*sp)%2000)+2000)%2000-40);});}
/*DUR*/
/*TX*/
function vt(i,frag){const s=TX[i];const k=s.indexOf(frag);if(k<0)throw new Error('frag '+frag);return 0.15+(DUR[i]-0.6)*k/s.length-0.15;}
const GAP=1.0;
function plan(i,frags){const n=frags.length+1,lim=0.8*DUR[i]-0.9;let t=frags.map(f=>vt(i,f)).concat([99]);
 t[0]=Math.max(t[0],GAP);for(let k=1;k<n;k++)t[k]=Math.max(t[k],t[k-1]+GAP);
 for(let k=n-1;k>=0;k--){const m=lim-(n-1-k)*GAP;if(t[k]>m)t[k]=m;}
 return t;}
const PL=[];
