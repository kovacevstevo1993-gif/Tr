// ===== SHORT 19 - teaser video lungo 16 + iscrizione (rivalutazione 2027, art. 55) (1080x1920, 30 fps) =====
// Regole N.15/N.18: comparsa 0.9 s, elementi che restano fino a fine scena, distanza >= 0,45 s, ultimo completo entro l'80 %, poi tutto FERMO.
// Look NUOVO rispetto a S18 (N.47): titoletto a PANNELLO SCURO con icona scalini e barra a 5 gradini che si riempie (niente numeri, N.50), schede a FOGLIO con angolo piegato,
// didascalia a PANNELLO SCURO con barra gialla e scalini, sfondo con SCALE traslucide che salgono piano e simboli %.
const eob2=x=>{const c1=1.0,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const pop=(t,a,d)=>Math.max(0,eob2(seg(t,a,a+(d||.9))));
const sl=(t,a,d)=>eo3(seg(t,a,a+(d||.9)));
const GRN='#13805F',DK='#0B4A50',ORG='#E8832A',AMB='#FFB020',NAVY='#06303A',SKIN='#F3C9A5';
function fade(t,n,x,y,a,dy){T(n,x,y+(1-sl(t,a,.9))*(dy===undefined?60:dy),0,1);op(n,seg(t,a,a+.55));}
function slideX(t,n,x,y,a,dx,r){T(n,x+(1-sl(t,a,.9))*dx,y,r||0,1);op(n,seg(t,a,a+.55));}
function rise(t,a,d,n,y,dy){const k=sl(t,a,d||.9);T(n,n._x,y+(1-k)*(dy||140),0,1);op(n,seg(t,a,a+(d||.9)*.6));}
function fit(p,s,x,y,fs,fill,maxW,anchor){const t=txt(p,s,x,y,fs,fill,'bold',anchor||'middle');const L=t.getComputedTextLength();if(L>maxW)t.setAttribute('font-size',fs*maxW/L);return t;}
function personI(p,s,col){const g=el('g',{},p);col=col||'#0B4A50';el('circle',{cx:0,cy:-30*s,r:20*s,fill:col},g);el('path',{d:`M${-34*s} ${40*s} Q${-34*s} ${-4*s} 0 ${-4*s} Q${34*s} ${-4*s} ${34*s} ${40*s}Z`,fill:col},g);return g;}
// scalini: n gradini che salgono da sinistra a destra, base a y=0, centrati in x; hi = gradino evidenziato
function stairsI(p,n,w,h,hi,col){const g=el('g',{},p);const sw=w/n;
 for(let k=0;k<n;k++){const sh=h*(k+1)/n;const x=-w/2+k*sw;
  el('rect',{x:x,y:-sh,width:sw-6,height:sh,rx:10,fill:(hi===k?ORG:(col||'url(#g_head)')),stroke:'#fff','stroke-width':4,filter:'url(#g_sh3)'},g);
  el('rect',{x:x+6,y:-sh+6,width:sw-18,height:12,rx:6,fill:'#fff','fill-opacity':.45},g);}
 return g;}
// foglio con angolo piegato in alto a destra
function sheet(p,w,h,fill,stroke){const g=el('g',{},p);const f=44;
 el('path',{d:`M${-w/2} ${-h/2} H${w/2-f} L${w/2} ${-h/2+f} V${h/2} H${-w/2}Z`,fill:fill||'url(#g_paper)',stroke:stroke||'#fff','stroke-width':5,'stroke-linejoin':'round',filter:'url(#g_sh)'},g);
 el('path',{d:`M${w/2-f} ${-h/2} V${-h/2+f} H${w/2}Z`,fill:'#B9CDD1',stroke:stroke||'#fff','stroke-width':4,'stroke-linejoin':'round'},g);return g;}
function scissorsI(p,s,col){const g=el('g',{filter:'url(#g_sh2)'},p);const st={fill:'none',stroke:col||'#fff','stroke-linecap':'round'};
 el('line',Object.assign({x1:-52*s,y1:-30*s,x2:76*s,y2:36*s,'stroke-width':14*s},st),g);el('line',Object.assign({x1:-52*s,y1:30*s,x2:76*s,y2:-36*s,'stroke-width':14*s},st),g);
 el('circle',Object.assign({cx:-74*s,cy:-34*s,r:22*s,'stroke-width':10*s},st),g);el('circle',Object.assign({cx:-74*s,cy:34*s,r:22*s,'stroke-width':10*s},st),g);return g;}
function buildingI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-110*s} ${-40*s} L0 ${-110*s} L${110*s} ${-40*s}Z`,fill:'#fff',stroke:'#9FB4B9','stroke-width':4*s,'stroke-linejoin':'round'},g);
 el('rect',{x:-100*s,y:-40*s,width:200*s,height:20*s,fill:'#DCE7EA'},g);
 [-70,-24,24,70].forEach(x=>el('rect',{x:(x-12)*s,y:-20*s,width:24*s,height:84*s,fill:'#fff',stroke:'#9FB4B9','stroke-width':3*s},g));
 el('rect',{x:-116*s,y:64*s,width:232*s,height:20*s,rx:6*s,fill:'#DCE7EA',stroke:'#9FB4B9','stroke-width':3*s},g);return g;}
function thumbI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-96*s,y:-8*s,width:44*s,height:96*s,rx:10*s,fill:'#0B4A50',stroke:'#fff','stroke-width':6*s},g);
 el('path',{d:`M${-40*s} ${-4*s} L${-6*s} ${-78*s} Q${20*s} ${-96*s} ${32*s} ${-64*s} L${24*s} ${-26*s} H${86*s} Q${112*s} ${-24*s} ${104*s} ${8*s} L${92*s} ${62*s} Q${86*s} ${88*s} ${60*s} ${88*s} H${-40*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);return g;}
function bellI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
function calcI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);el('rect',{x:-60*s,y:-80*s,width:120*s,height:160*s,rx:16*s,fill:NAVY,stroke:'#fff','stroke-width':5*s},g);
 el('rect',{x:-46*s,y:-66*s,width:92*s,height:36*s,rx:8*s,fill:'#9BF0DB'},g);
 for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('rect',{x:(-46+c*33)*s,y:(-16+r*30)*s,width:26*s,height:22*s,rx:6*s,fill:c==2&&r==2?ORG:'#fff'},g);return g;}
function checkI(p,r,col){const g=el('g',{},p);el('circle',{r:r,fill:col||'#1E9C6E',stroke:'#fff','stroke-width':r*.12},g);el('path',{d:`M${-r*.45} ${r*.02} l${r*.28} ${r*.34} l${r*.6} ${-r*.66}`,fill:'none',stroke:'#fff','stroke-width':r*.2,'stroke-linecap':'round','stroke-linejoin':'round'},g);return g;}
// titoletto: pannello scuro con icona scalini, titolo fisso e barra a 5 gradini che si riempie secondo il blocco (niente numeri)
function head(p,o,k){o.lab=el('g',{},p);
 el('rect',{x:-490,y:-48,width:980,height:96,rx:26,fill:NAVY,stroke:AMB,'stroke-width':5,filter:'url(#g_sh2)'},o.lab);
 const ic=el('g',{transform:'translate(-432 8)'},o.lab);stairsI(ic,4,64,52,3,'#9BF0DB');
 fit(o.lab,'RIVALUTAZIONE 2027',-380,14,40,'#fff',400,'start');
 const bs=el('g',{transform:'translate(246 18)'},o.lab);
 for(let i=0;i<5;i++){const h=14+i*9;el('rect',{x:i*44,y:-h,width:36,height:h,rx:6,fill:(i<=k?AMB:'#1E4F57'),stroke:i<=k?'#fff':'none','stroke-width':2},bs);}}
function headU(t,o){T(o.lab,540,190,0,1);op(o.lab,seg(t,0,.9));}
// didascalia: pannello scuro con barra gialla a sinistra e due righe
function strip(p,lines,fs){fs=fs||46;const c=el('g',{},p);const w=900,h=lines.length*fs*1.3+60;
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:NAVY,stroke:'#9BF0DB','stroke-opacity':.5,'stroke-width':4,filter:'url(#g_sh)'},c);
 el('rect',{x:-w/2,y:-h/2,width:26,height:h,rx:13,fill:AMB},c);
 const ic=el('g',{transform:'translate('+(-w/2+110)+' '+(h/2-28)+')'},c);stairsI(ic,3,84,66,2,'#2E8C96');
 lines.forEach((l,i)=>fit(c,l,-w/2+190+(w-230)/2-30,-h/2+30+fs*0.98+i*fs*1.3,fs,'#fff',w-250));
 c._x=540;return c;}
// sfondo: scale traslucide che salgono piano + simboli %
let BGX=null;
function bgx(t){if(!BGX){const b=document.getElementById('bok');BGX={r:[]};
 for(let k=0;k<8;k++){const g=el('g',{},b);const s=.9+(k%3)*.4;
  [0,1,2,3].forEach(j=>el('rect',{x:(j*60-120)*s,y:(-j*46)*s,width:54*s,height:(46*(j+1)+10)*s,rx:8*s,fill:'#9BF0DB','fill-opacity':.08+(k%3)*.02},g));
  if(k%2==0){const q=el('g',{transform:'translate('+(170*s)+' '+(-70*s)+') scale('+s+')','fill-opacity':.1,opacity:.1},g);el('circle',{cx:-26,cy:-26,r:20,fill:'none',stroke:'#fff','stroke-width':12},q);el('circle',{cx:26,cy:26,r:20,fill:'none',stroke:'#fff','stroke-width':12},q);el('line',{x1:34,y1:-40,x2:-34,y2:40,stroke:'#fff','stroke-width':12,'stroke-linecap':'round'},q);}
  BGX.r.push([g,(k*217)%950,(k*283)%2200,9+(k*3)%8,0]);}}
 BGX.r.forEach(([g,x,y,sp,rot])=>{g.setAttribute('transform','translate('+(x+30*Math.sin(t*.15+x))+' '+((((y-t*sp)%2300)+2300)%2300-150)+') rotate('+rot+')');});}
/*DUR*/
/*TX*/
function vt(i,frag){const s=TX[i];const k=s.indexOf(frag);if(k<0)throw new Error('frag '+frag);
 const wt=c=>/[,:;]/.test(c)?7:/[.?!]/.test(c)?12:1;let tot=0,acc=0;for(let j=0;j<s.length;j++){const w=wt(s[j]);tot+=w;if(j<k)acc+=w;}
 return (DUR[i]-0.6)*acc/tot;}
const GAP=0.7;
function plan(i,frags){const n=frags.length+1,lim=0.8*DUR[i]-0.9;let t=frags.map(f=>vt(i,f)).concat([99]);
 t[0]=Math.max(t[0],1.0);for(let k=1;k<n;k++)t[k]=Math.max(t[k],t[k-1]+GAP);
 for(let k=n-1;k>=0;k--){const m=lim-(n-1-k)*GAP;if(t[k]>m)t[k]=m;}
 return t;}
const PL=[];
