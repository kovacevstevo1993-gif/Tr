// ===== VIDEO 15 (Carta Dedicata a te e aiuti per i pensionati) - stile nuovo (N.37, N.47, N.50) =====
// Diverso dai video 7-14, stessi colori del canale: titoletto con carta prepagata e binario a 4 stazioni (LA CARTA / L'ELENCO / LE DATE / GLI AIUTI),
// didascalia a "carta" con filo giallo sotto, elementi nuovi (carta prepagata, frecce a pentagono, misuratore Isee, fasce, elenco del Comune,
// alimenti disegnati, asse dei mesi con bandierine, codici esenzione, riquadri bollette, tv, monete) e sfondo con carte che scorrono, fasci di luce e anelli.
(function(){const d=document.querySelector('defs');
 const lg=el('linearGradient',{id:'g_pk',x1:0,y1:0,x2:1,y2:1},d);
 [['0','#14A6A2'],['0.55','#0B5E6B'],['1','#06303A']].forEach(([o,c])=>el('stop',{offset:o,'stop-color':c},lg));})();
// ---------- icone nuove ----------
const _ico15=ico;
const NI15={
 bolt:(g,col)=>el('path',{d:'M10 -42 L-24 6 H-3 L-12 42 L26 -10 H5 Z',fill:col,'stroke-linejoin':'round'},g),
 flame:(g,col)=>{el('path',{d:'M0 -42 Q26 -14 24 8 Q22 34 0 40 Q-22 34 -24 8 Q-24 -4 -10 -18 Q-6 -2 4 -8 Q8 -26 0 -42 Z',fill:col},g);el('path',{d:'M0 6 Q12 16 8 28 Q0 34 -8 28 Q-10 16 0 6 Z',fill:'#fff',opacity:.9},g);},
 drop:(g,col)=>{el('path',{d:'M0 -42 Q32 -4 32 14 Q32 40 0 40 Q-32 40 -32 14 Q-32 -4 0 -42 Z',fill:col},g);el('path',{d:'M-14 12 Q-12 26 2 30',fill:'none',stroke:'#fff','stroke-width':6,'stroke-linecap':'round',opacity:.9},g);},
 bin:(g,col)=>{el('rect',{x:-30,y:-30,width:60,height:9,rx:4,fill:col},g);el('rect',{x:-9,y:-40,width:18,height:12,rx:4,fill:col},g);el('path',{d:'M-24 -18 H24 L19 40 H-19 Z',fill:col},g);[-9,0,9].forEach(x=>el('line',{x1:x,y1:-8,x2:x*0.8,y2:30,stroke:'#fff','stroke-width':4,'stroke-linecap':'round'},g));},
 tv:(g,col)=>{el('rect',{x:-42,y:-28,width:84,height:56,rx:9,fill:col},g);el('rect',{x:-34,y:-20,width:68,height:40,rx:5,fill:'#D6F5EC'},g);el('path',{d:'M-14 -38 L0 -28 L14 -38',fill:'none',stroke:col,'stroke-width':5,'stroke-linecap':'round'},g);el('rect',{x:-18,y:30,width:36,height:6,rx:3,fill:col},g);},
 hcard:(g,col)=>{el('rect',{x:-42,y:-28,width:84,height:56,rx:9,fill:col},g);el('path',{d:'M-30 -6 H-18 V-18 H-10 V-6 H2 V2 H-10 V14 H-18 V2 H-30 Z',fill:'#fff'},g);[-10,4,18].forEach((y,i)=>el('rect',{x:10,y:y-4,width:i==2?16:26,height:7,rx:3,fill:'#fff',opacity:.9},g));},
 cart:(g,col)=>{el('path',{d:'M-42 -30 H-26 L-14 14 H26 L36 -16 H-22',fill:'none',stroke:col,'stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'},g);el('circle',{cx:-6,cy:30,r:7,fill:col},g);el('circle',{cx:22,cy:30,r:7,fill:col},g);},
};
ico=function(p,k,s,col){if(NI15[k]){s=s||1;col=col||INK;const g=el('g',{transform:'scale('+s+')'},p);NI15[k](g,col);return g;}return _ico15(p,k,s,col);};
// ---------- carta piccola (titoletto e didascalia) ----------
function miniCard(p,w){const g=el('g',{},p);const h=w*0.63;
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:w*0.1,fill:'url(#g_pk)',stroke:'#7FF0D2','stroke-width':2.5},g);
 el('rect',{x:-w*0.36,y:-h*0.22,width:w*0.2,height:h*0.26,rx:w*0.03,fill:AMB},g);
 el('rect',{x:-w*0.36,y:h*0.14,width:w*0.6,height:h*0.1,rx:h*0.05,fill:'#fff',opacity:.55},g);
 return g;}
// ---------- titoletto: carta + titolo a sinistra, binario a 4 stazioni a destra (senza numero del blocco, N.50) ----------
const ST15=['LA CARTA','L\'ELENCO','LE DATE','GLI AIUTI'];
const stn15=n=>n<=4?0:(n<=11?1:(n===12?2:3));
function topLabel(g,s){const t=el('g',{transform:'translate(-840 0)'},g);
 const mc=el('g',{transform:'translate(46 0)'},t);miniCard(mc,76);
 const x=fitT(t,s,110,0,34,'#7FF0D2','bold',700,'start');x.setAttribute('letter-spacing','5');
 const cur=stn15(N);const X0=1230,DX=150;
 el('line',{x1:X0,y1:0,x2:X0+3*DX,y2:0,stroke:'#7FF0D2','stroke-width':3,opacity:.35},t);
 el('line',{x1:X0,y1:0,x2:X0+cur*DX,y2:0,stroke:AMB,'stroke-width':5},t);
 ST15.forEach((p,i)=>{const cx=X0+i*DX;const a=i===cur;
  el('circle',{cx:cx,cy:0,r:a?13:8,fill:a?AMB:(i<cur?'#7FF0D2':'#06303A'),stroke:a?'#fff':'#7FF0D2','stroke-width':a?4:2.5},t);
  fitT(t,p,cx,34,20,a?'#FFE7B0':'#CFEDE7','bold',DX-14);});
 return t;}
// ---------- didascalia a carta: riquadro scuro, carta inclinata a sinistra, filo giallo sotto ----------
function cap(g,s,size){size=size||42;const c=el('g',{},g);if(!s)return c;
 const t=txt(c,s,0,0,size,'#FFFFFF','bold');let tl=mw(t,s,size);
 const maxT=1480;if(tl>maxT){size=size*maxT/tl;t.setAttribute('font-size',size.toFixed(1));tl=mw(t,s,size);}
 const padL=170,padR=56;const w=tl+padL+padR;
 t.setAttribute('x',(-w/2+padL+tl/2).toFixed(1));t.setAttribute('y',(size*0.36).toFixed(1));
 const ins=e=>{c.insertBefore(e,t);return e;};
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:20,fill:'#06303A',filter:'url(#g_sh2)'}));
 ins(el('rect',{x:-w/2+4,y:-52,width:w-8,height:104,rx:17,fill:'none',stroke:'#7FF0D2','stroke-width':2,opacity:.35}));
 ins(el('rect',{x:-w/2+34,y:46,width:w-68,height:7,rx:3.5,fill:AMB}));
 const mc=el('g',{transform:'translate('+(-w/2+92)+' -2) rotate(-8)'},c);miniCard(mc,104);
 return c;}
// ---------- carta prepagata grande ----------
function pcardB(g,w,o){o=o||{};const h=w*0.63;const R=w*0.055;
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:R,fill:'url(#g_pk)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh)'},g);
 const id='pq'+(++UID);const cp=el('clipPath',{id:id},g);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:R},cp);
 const d=el('g',{'clip-path':'url(#'+id+')'},g);
 el('polygon',{points:`${-w/2},${h*0.1} ${-w/2+w*0.5},${-h/2} ${-w/2+w*0.72},${-h/2} ${-w/2},${h*0.45}`,fill:'#fff',opacity:.07},d);
 el('circle',{cx:w*0.26,cy:h*0.02,r:h*0.34,fill:'none',stroke:'#7FF0D2','stroke-width':3,opacity:.2},d);
 el('circle',{cx:w*0.26,cy:h*0.02,r:h*0.25,fill:'none',stroke:'#7FF0D2','stroke-width':3,opacity:.16},d);
 const cx=-w/2+w*0.12,cy=-h*0.02;
 el('rect',{x:cx-w*0.07,y:cy-w*0.05,width:w*0.14,height:w*0.1,rx:w*0.015,fill:'#F2C96B',stroke:'#B88A1F','stroke-width':2},g);
 [-1,0,1].forEach(k=>el('line',{x1:cx-w*0.07,y1:cy+k*w*0.026,x2:cx+w*0.07,y2:cy+k*w*0.026,stroke:'#B88A1F','stroke-width':2},g));
 el('line',{x1:cx,y1:cy-w*0.05,x2:cx,y2:cy+w*0.05,stroke:'#B88A1F','stroke-width':2},g);
 [0.5,0.8,1.1].forEach(k=>el('path',{d:`M${cx+w*0.13} ${cy-w*0.04*k} Q${cx+w*0.13+w*0.03*k} ${cy} ${cx+w*0.13} ${cy+w*0.04*k}`,fill:'none',stroke:'#fff','stroke-width':3,'stroke-linecap':'round',opacity:.8},g));
 fitT(g,o.title||'DEDICATA A TE',-w/2+w*0.06,-h/2+h*0.17,w*0.07,'#fff','900',w*0.7,'start');
 fitT(g,o.kicker||'CARTA PREPAGATA',-w/2+w*0.06,-h/2+h*0.3,w*0.034,'#7FF0D2','bold',w*0.7,'start');
 if(o.amt)fitT(g,o.amt,-w/2+w*0.06,h*0.3,w*0.17,'#fff','900',w*0.62,'start');
 el('circle',{cx:w*0.32,cy:h*0.36,r:h*0.13,fill:'#E4412C',opacity:.9},g);el('circle',{cx:w*0.39,cy:h*0.36,r:h*0.13,fill:AMB,opacity:.9},g);
 return g;}
// ---------- freccia a pentagono (passaggi) ----------
function chevB(g,w,h,fill,label,sub,first,o){o=o||{};const k=h*0.42;const L=-w/2,R=w/2;
 const d=first?`M${L} ${-h/2} H${R-k} L${R} 0 L${R-k} ${h/2} H${L} Z`:`M${L} ${-h/2} H${R-k} L${R} 0 L${R-k} ${h/2} H${L} L${L+k} 0 Z`;
 el('path',{d:d,fill:fill,stroke:'#fff','stroke-width':5,'stroke-linejoin':'round',filter:'url(#g_sh2)'},g);
 const col=(fill===AMB)?'#5A3300':'#fff';const cx=first?-k/2:0;const maxw=first?w-k-50:w-2*k-30;
 fitT(g,label,cx,sub?-h*0.14:0,o.fs||40,col,'900',maxw);
 if(sub)fitT(g,sub,cx,h*0.22,o.sfs||26,(col==='#fff')?'#CFF7EC':'#5A3300','bold',maxw);
 return g;}
// ---------- misuratore con soglia (Isee) ----------
const fmtN=v=>String(v).replace(/\B(?=(\d{3})+(?!\d))/g,'.');
function gaugeB(g,W,max,val,label,ticks){const H=70;const X=v=>-W/2+v/max*W;
 el('rect',{x:-W/2-6,y:-H/2-6,width:W+12,height:H+12,rx:H/2+6,fill:'#06303A',filter:'url(#g_sh2)'},g);
 const id='gz'+(++UID);const cp=el('clipPath',{id:id},g);el('rect',{x:-W/2,y:-H/2,width:W,height:H,rx:H/2},cp);
 const bg=el('g',{'clip-path':'url(#'+id+')'},g);
 el('rect',{x:-W/2,y:-H/2,width:X(val)+W/2,height:H,fill:'url(#g_badge)'},bg);
 el('rect',{x:X(val),y:-H/2,width:W/2-X(val),height:H,fill:'#0A3F45'},bg);
 el('rect',{x:-W/2,y:-H/2,width:W,height:H,rx:H/2,fill:'none',stroke:'#fff','stroke-width':4,opacity:.85},g);
 el('line',{x1:X(val),y1:-H/2-26,x2:X(val),y2:H/2+14,stroke:AMB,'stroke-width':6},g);
 el('path',{d:`M${X(val)-16} ${-H/2-42} h32 l-16 18 z`,fill:AMB},g);
 fitT(g,label,X(val),-H/2-74,34,'#FFE7B0','900',W*0.7);
 (ticks||[]).forEach(v=>{el('line',{x1:X(v),y1:H/2+4,x2:X(v),y2:H/2+20,stroke:'#fff','stroke-width':3,opacity:.7},g);fitT(g,fmtN(v),X(v),H/2+46,26,'#CFEDE7','bold',160);});
 return g;}
// ---------- persone stilizzate ----------
function pplB(g,n,col,s){s=s||1;const G=el('g',{transform:'scale('+s+')'},g);
 for(let i=0;i<n;i++){const x=(i-(n-1)/2)*46;el('circle',{cx:x,cy:-18,r:13,fill:col},G);el('path',{d:`M${x-19} 30 Q${x-19} 0 ${x} 0 Q${x+19} 0 ${x+19} 30 Z`,fill:col},G);}return G;}
// ---------- fascia di priorita ----------
function tierB(g,w,h,rank,title,sub,fill){
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:22,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h/2,width:150,height:h,rx:22,fill:fill},g);el('rect',{x:-w/2+110,y:-h/2,width:40,height:h,fill:fill},g);
 fitT(g,String(rank),-w/2+75,0,68,'#fff','900',110);
 fitT(g,title,-w/2+185,-18,38,INK,'900',w-185-330,'start');
 fitT(g,sub,-w/2+185,28,28,GRN,'bold',w-185-330,'start');
 const pg=el('g',{transform:'translate('+(w/2-165)+' 4)'},g);pplB(pg,3,fill,1.15);
 return g;}
// ---------- elenco del Comune ----------
function listB(g,w,h,title,n,hl){
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:24,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('path',{d:`M${-w/2} ${-h/2+84} V${-h/2+24} Q${-w/2} ${-h/2} ${-w/2+24} ${-h/2} H${w/2-24} Q${w/2} ${-h/2} ${w/2} ${-h/2+24} V${-h/2+84} Z`,fill:GRN},g);
 el('rect',{x:-w/2,y:-h/2+79,width:w,height:5,fill:AMB},g);
 fitT(g,title,0,-h/2+42,30,'#fff','900',w-60);
 const rh=(h-84-34)/n;
 for(let i=0;i<n;i++){const y=-h/2+84+17+rh*(i+0.5);const on=(i===hl);
  if(on)el('rect',{x:-w/2+18,y:y-rh/2+4,width:w-36,height:rh-8,rx:16,fill:'#FFF1CC',stroke:AMB,'stroke-width':4},g);
  el('circle',{cx:-w/2+62,cy:y,r:rh*0.28,fill:on?AMB:'#B7C7CA'},g);
  el('rect',{x:-w/2+110,y:y-9,width:(w-260)*(on?0.8:(0.5+0.1*((i*3)%4))),height:18,rx:9,fill:on?INK:'#C3D3D7'},g);
  if(on)el('path',{d:`M${w/2-86} ${y} l18 20 l36 -40`,fill:'none',stroke:'#1B9F81','stroke-width':12,'stroke-linecap':'round','stroke-linejoin':'round'},g);}
 return g;}
// ---------- alimenti disegnati ----------
const FD={
 meat:f=>{el('path',{d:'M-38 -6 Q-34 -34 -2 -32 Q32 -30 34 -4 Q36 22 8 30 Q-28 36 -38 -6 Z',fill:'#D9534F'},f);el('path',{d:'M-32 -2 Q-28 -24 -4 -26',fill:'none',stroke:'#F6B1A8','stroke-width':5,'stroke-linecap':'round'},f);el('rect',{x:30,y:-4,width:20,height:10,rx:5,fill:'#F4EAD5'},f);el('circle',{cx:52,cy:-3,r:7,fill:'#F4EAD5'},f);el('circle',{cx:52,cy:9,r:7,fill:'#F4EAD5'},f);},
 fish:f=>{el('ellipse',{cx:-6,cy:0,rx:32,ry:18,fill:'#4FA3D1'},f);el('polygon',{points:'22,0 46,-18 46,18',fill:'#3B86B0'},f);el('polygon',{points:'-6,-16 6,-30 14,-14',fill:'#3B86B0'},f);el('circle',{cx:-24,cy:-4,r:5,fill:'#fff'},f);el('circle',{cx:-25,cy:-4,r:2.4,fill:INK},f);[-6,6].forEach(x=>el('path',{d:`M${x} -10 Q${x+6} 0 ${x} 10`,fill:'none',stroke:'#fff','stroke-width':3,opacity:.7},f));},
 milk:f=>{el('path',{d:'M-17 -8 L-10 -30 H10 L17 -8 Z',fill:'#E8F4FB',stroke:'#3B7DA8','stroke-width':4,'stroke-linejoin':'round'},f);el('rect',{x:-17,y:-8,width:34,height:44,rx:3,fill:'#fff',stroke:'#3B7DA8','stroke-width':4},f);el('rect',{x:-17,y:8,width:34,height:16,fill:'#3B7DA8'},f);el('path',{d:'M0 10 Q5 17 0 22 Q-5 17 0 10 Z',fill:'#fff'},f);},
 egg:f=>{el('ellipse',{cx:-12,cy:6,rx:20,ry:26,fill:'#F6E7C8',stroke:'#D9B26B','stroke-width':4},f);el('ellipse',{cx:14,cy:10,rx:18,ry:24,fill:'#FBF3DE',stroke:'#D9B26B','stroke-width':4},f);el('path',{d:'M-22 -6 Q-20 -14 -12 -16',fill:'none',stroke:'#fff','stroke-width':4,'stroke-linecap':'round'},f);},
 oil:f=>{el('path',{d:'M-16 -10 Q-16 -22 -6 -26 V-38 H6 V-26 Q16 -22 16 -10 V34 Q16 40 10 40 H-10 Q-16 40 -16 34 Z',fill:'#8DBB2F'},f);el('rect',{x:-8,y:-46,width:16,height:9,rx:3,fill:'#2B6F77'},f);el('rect',{x:-12,y:4,width:24,height:22,rx:4,fill:'#fff'},f);el('circle',{cx:0,cy:15,r:6,fill:'#5E8F1F'},f);},
 pasta:f=>{el('polygon',{points:'-42,-22 -4,0 -42,22',fill:'#F2C94C'},f);el('polygon',{points:'42,-22 4,0 42,22',fill:'#F2C94C'},f);el('rect',{x:-8,y:-10,width:16,height:20,rx:5,fill:'#E0A82E'},f);[-30,-20].forEach(x=>el('line',{x1:x,y1:-12,x2:x,y2:12,stroke:'#E0A82E','stroke-width':3},f));[30,20].forEach(x=>el('line',{x1:x,y1:-12,x2:x,y2:12,stroke:'#E0A82E','stroke-width':3},f));},
 rice:f=>{el('path',{d:'M-32 -4 Q-30 -34 0 -34 Q30 -34 32 -4 Z',fill:'#fff',stroke:'#D6DEE0','stroke-width':3},f);el('path',{d:'M-38 -4 H38 Q36 34 0 38 Q-36 34 -38 -4 Z',fill:'#E4412C'},f);[[-14,-18],[0,-24],[14,-16],[-4,-10],[10,-6]].forEach(([x,y])=>el('ellipse',{cx:x,cy:y,rx:5,ry:2.4,fill:'#E8EEF0'},f));},
 fruit:f=>{el('circle',{cx:0,cy:8,r:28,fill:'#D23A25'},f);el('path',{d:'M-10 -18 Q0 -10 10 -18',fill:'none',stroke:'#9F2A1A','stroke-width':4,'stroke-linecap':'round'},f);el('rect',{x:-2,y:-30,width:4,height:14,rx:2,fill:'#6B4A3A'},f);el('ellipse',{cx:12,cy:-26,rx:12,ry:6,fill:'#2FBF9B',transform:'rotate(-25 12 -26)'},f);el('path',{d:'M-18 -2 Q-18 -12 -8 -14',fill:'none',stroke:'#fff','stroke-width':4,'stroke-linecap':'round',opacity:.6},f);},
 veg:f=>{const c=el('g',{transform:'rotate(-35)'},f);el('polygon',{points:'-30,-14 36,0 -30,14',fill:'#F08A28'},c);[-6,8,20].forEach(x=>el('line',{x1:x,y1:-6,x2:x+4,y2:6,stroke:'#C96A12','stroke-width':3,opacity:.8},c));[-12,0,12].forEach(a=>el('ellipse',{cx:-40,cy:a*0.6,rx:12,ry:5,fill:'#2FBF9B',transform:`rotate(${a} -40 ${a*0.6})`},c));},
 coffee:f=>{el('path',{d:'M-30 -12 H26 V10 Q26 34 -2 34 Q-30 34 -30 10 Z',fill:'#fff',stroke:'#8B5A2B','stroke-width':5},f);el('path',{d:'M26 -4 Q44 -4 44 10 Q44 22 24 22',fill:'none',stroke:'#8B5A2B','stroke-width':5},f);el('ellipse',{cx:-2,cy:40,rx:40,ry:7,fill:'#C8D5DA'},f);el('path',{d:'M-14 -18 Q-20 -28 -12 -34 M2 -18 Q-4 -28 4 -34 M16 -18 Q10 -28 18 -34',fill:'none',stroke:'#8FA8AD','stroke-width':4,'stroke-linecap':'round'},f);}
};
function foodB(g,k,label){const r=64;el('circle',{r:r,fill:'url(#g_paper)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
 const f=el('g',{transform:'scale(0.95)'},g);FD[k](f);fitT(g,label,0,r+32,28,'#fff','900',230);return g;}
// ---------- asse dei mesi con bandierine ----------
const AXW=1640,AXM=12;const axX=m=>-AXW/2+m*AXW/AXM;
function axisB(g){const H=24;
 el('rect',{x:-AXW/2,y:-H/2,width:AXW,height:H,rx:H/2,fill:'#06303A',stroke:'#7FF0D2','stroke-width':3,filter:'url(#g_sh2)'},g);
 const MS=['NOV','DIC','GEN','FEB','MAR','APR','MAG','GIU','LUG','AGO','SET','OTT'];
 for(let i=0;i<=AXM;i++)el('line',{x1:axX(i),y1:-H/2-8,x2:axX(i),y2:H/2+8,stroke:'#fff','stroke-width':3,opacity:.6},g);
 for(let i=0;i<AXM;i++)fitT(g,MS[i],axX(i+0.5),56,26,i<2?'#FFE7B0':'#CFEDE7','bold',110);
 fitT(g,'2026',axX(1),106,32,'#7FF0D2','900',200);fitT(g,'2027',axX(7),106,32,'#7FF0D2','900',200);
 el('line',{x1:axX(0)+6,y1:90,x2:axX(2)-6,y2:90,stroke:'#7FF0D2','stroke-width':3,opacity:.5},g);el('line',{x1:axX(2)+6,y1:90,x2:axX(12)-6,y2:90,stroke:'#7FF0D2','stroke-width':3,opacity:.5},g);
 return g;}
function pinB(g,l1,l2,fill,h){h=h||170;const col=(fill===AMB)?'#5A3300':'#fff';
 el('line',{x1:0,y1:-8,x2:0,y2:-h+56,stroke:'#fff','stroke-width':5},g);
 el('circle',{r:16,fill:fill,stroke:'#fff','stroke-width':5,filter:'url(#g_sh3)'},g);
 const w=Math.max(l1.length*34*0.72,l2.length*26*0.66)+70;
 el('rect',{x:-w/2,y:-h-54,width:w,height:110,rx:18,fill:fill,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
 fitT(g,l1,0,-h-14,34,col,'900',w-40);fitT(g,l2,0,-h+28,26,(col==='#fff')?'#E9FBF6':'#5A3300','bold',w-40);return g;}
// ---------- confronto Carta acquisti / Dedicata a te ----------
function vsB(g){const S=1.5;
 const rows=[[-48,'CARTA ACQUISTI',480,AMB,'#5A3300'],[48,'DEDICATA A TE',500,'url(#g_badge)','#fff']];
 rows.forEach(([y,lab,v,fill,col])=>{fitT(g,lab,-255,y,32,'#fff','900',245,'end');
  const w=v*S;el('rect',{x:-235,y:y-34,width:w,height:68,rx:20,fill:fill,stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},g);
  fitT(g,v+' €',-235+w/2,y,40,col,'900',w-30);});
 el('path',{d:'M 530 -48 H 548 V 48 H 530',fill:'none',stroke:AMB,'stroke-width':5,'stroke-linecap':'round'},g);
 return g;}
// ---------- codice di esenzione ----------
function codeB(g,w,h,code,lines,fill){
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h/2,width:190,height:h,rx:26,fill:fill},g);el('rect',{x:-w/2+150,y:-h/2,width:40,height:h,fill:fill},g);
 fitT(g,code,-w/2+95,-8,68,'#fff','900',170);fitT(g,'CODICE',-w/2+95,h*0.26,22,'#E9FBF6','bold',170);
 const n=lines.length;const x0=-w/2+222,x1=w/2-24;const lh=Math.min(54,(h-40)/n);
 lines.forEach((L,i)=>fitT(g,L[0],x0,(i-(n-1)/2)*lh,L[1]||32,L[2]||INK,L[3]||'900',x1-x0,'start'));return g;}
// ---------- riquadro bolletta ----------
function tileB(g,icon,big,sub,fill){const w=400,h=300;
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('path',{d:`M${-w/2} -50 V${-h/2+30} Q${-w/2} ${-h/2} ${-w/2+30} ${-h/2} H${w/2-30} Q${w/2} ${-h/2} ${w/2} ${-h/2+30} V-50 Z`,fill:fill},g);
 const c=el('g',{transform:'translate(0 -100)'},g);el('circle',{r:46,fill:'#fff',stroke:'#fff','stroke-width':4},c);ico(c,icon,0.85,fill);
 fitT(g,big,0,34,78,INK,'900',w-50);fitT(g,sub,0,108,28,GRN,'bold',w-40);return g;}
// ---------- televisore ----------
function tvB(g,w){const h=w*0.66;
 el('path',{d:`M${-w*0.1} ${-h/2} L${-w*0.26} ${-h/2-w*0.17} M${w*0.1} ${-h/2} L${w*0.26} ${-h/2-w*0.17}`,fill:'none',stroke:'#fff','stroke-width':8,'stroke-linecap':'round'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:w*0.07,fill:'#0B4A50',stroke:'#fff','stroke-width':6,filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2+w*0.06,y:-h/2+w*0.06,width:w*0.88,height:h-w*0.12,rx:w*0.04,fill:'url(#g_badge)'},g);
 el('path',{d:`M${-w*0.08} ${-h*0.18} L${w*0.1} 0 L${-w*0.08} ${h*0.18} Z`,fill:'#fff'},g);
 el('rect',{x:-w*0.2,y:h/2,width:w*0.4,height:w*0.04,rx:4,fill:'#fff'},g);
 const b=el('g',{transform:`translate(${w/2} ${h/2})`},g);el('circle',{r:w*0.15,fill:'#2FD0A8',stroke:'#fff','stroke-width':6},b);
 el('path',{d:`M${-w*0.07} 0 l${w*0.05} ${w*0.06} l${w*0.1} ${-w*0.12}`,fill:'none',stroke:'#fff','stroke-width':9,'stroke-linecap':'round','stroke-linejoin':'round'},b);return g;}
// ---------- sei monete da 80 euro ----------
function coins6B(g){fitT(g,'OGNI DUE MESI ARRIVANO 80 €',0,-92,32,'#FFE7B0','900',700);
 for(let i=0;i<6;i++){const x=(i-2.5)*118;const c=el('g',{transform:`translate(${x} 0)`},g);el('circle',{r:50,fill:AMB,stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},c);el('circle',{r:38,fill:'none',stroke:'#fff','stroke-width':2.5,opacity:.6},c);fitT(c,'80',0,0,42,'#5A3300','900',70);}
 return g;}
// ---------- meta' e meta' ----------
function pie2B(g,r){const id='pe'+(++UID);
 el('circle',{r:r+6,fill:'#06303A',filter:'url(#g_sh2)'},g);
 el('path',{d:`M0 ${-r} A${r} ${r} 0 0 0 0 ${r} Z`,fill:'url(#g_badge)'},g);el('path',{d:`M0 ${-r} A${r} ${r} 0 0 1 0 ${r} Z`,fill:AMB},g);
 el('line',{x1:0,y1:-r,x2:0,y2:r,stroke:'#fff','stroke-width':5},g);el('circle',{r:r,fill:'none',stroke:'#fff','stroke-width':5},g);
 const a=el('g',{transform:`translate(${-r*0.5} -8)`},g);ico(a,'people',r/90,'#fff');const b=el('g',{transform:`translate(${r*0.5} -8)`},g);ico(b,'coin',r/90,'#5A3300');
 fitT(g,'METÀ',-r*0.5,r*0.55,r*0.17,'#fff','900',r*0.62);fitT(g,'METÀ',r*0.5,r*0.55,r*0.17,'#5A3300','900',r*0.62);return g;}
Object.assign(BUILD,{
 pcard:(g,w,o)=>pcardB(g,w,o),
 chev:(g,w,h,fill,label,sub,first,o)=>chevB(g,w,h,fill,label,sub,first,o),
 gauge:(g,W,max,val,label,ticks)=>gaugeB(g,W,max,val,label,ticks),
 tier:(g,w,h,rank,title,sub,fill)=>tierB(g,w,h,rank,title,sub,fill),
 list:(g,w,h,title,n,hl)=>listB(g,w,h,title,n,hl),
 food:(g,k,label)=>foodB(g,k,label),
 axis:(g)=>axisB(g),
 pin:(g,l1,l2,fill,h)=>pinB(g,l1,l2,fill,h),
 band:(g,w)=>{el('rect',{x:-w/2,y:-17,width:w,height:34,rx:17,fill:AMB,stroke:'#fff','stroke-width':4,filter:'url(#g_sh3)'},g);},
 vs:(g)=>vsB(g),
 code:(g,w,h,code,lines,fill)=>codeB(g,w,h,code,lines,fill),
 tile:(g,icon,big,sub,fill)=>tileB(g,icon,big,sub,fill),
 tvb:(g,w)=>tvB(g,w),
 coins6:(g)=>coins6B(g),
 pie2:(g,r)=>pie2B(g,r),
});
// ---------- pillola e scheda con icona: margine destro proporzionale (i riquadri larghi hanno margine del 3 %) ----------
function pillB(g,s,fs,fill,col,icon,o){o=o||{};fs=fs||34;const t=txt(g,s,0,fs*0.36,fs,col||'#fff','bold');const tl=mw(t,s,fs);
 const h=o.h||fs*1.8;const ir=icon?h*0.37:0;const padL=icon?(h*0.14+2*ir+fs*0.45):fs*1.15;const padR=fs*1.15+(tl+padL)*0.036;
 const w=Math.max(o.minw||0,tl+padL+padR);const tx=-w/2+padL+(w-padL-padR)/2;t.setAttribute('x',tx.toFixed(1));
 const r=el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:o.rx!==undefined?o.rx:h/2,fill:fill,stroke:o.stroke||'#fff','stroke-width':o.sw||4,filter:'url(#g_sh3)'});g.insertBefore(r,t);
 if(icon){const ig=el('g',{transform:'translate('+(-w/2+h*0.14+ir)+' 0)'},g);el('circle',{r:ir,fill:o.ibg||'#fff'},ig);ico(ig,icon,ir/48,o.icol||INK);}
 g.__w=w;return w;}
BUILD.icard=(g,w,h,icon,lines,o)=>{o=o||{};el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:o.fill||'url(#g_paper)',filter:'url(#g_sh)'},g);
  if(o.stroke)el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'none',stroke:o.stroke,'stroke-width':6},g);
  const ir=o.ir||Math.min(70,h*0.36);const ix=-w/2+ir+34;const ig=el('g',{transform:'translate('+ix+' 0)'},g);el('circle',{r:ir,fill:o.ibg||LIGHT},ig);ico(ig,icon,ir/54,o.icol||INK);
  const x0=ix+ir+26,x1=w/2-Math.max(40,0.036*w+8),cx=(x0+x1)/2;const n=lines.length;const lh=o.lh||(lines[0][1]*1.32);
  lines.forEach((L,i)=>fitT(g,L[0],cx,(i-(n-1)/2)*lh+(o.dy||0),L[1],L[2]||INK,L[3]||'900',x1-x0));};
const CP15=['#2B6F8F','#1B9F81','#E39A1C'];
// ======================= BLOCCHI =======================
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA CARTA DEDICATA A TE',cap:'CARTA DEDICATA A TE: 500 € DAL 4 NOVEMBRE E 500 € DA APRILE',items:[
  P('HAI UNA PENSIONE?',960,205,'Hai una pensione',AMB,40,'q'),
  I('pcard',[540,{amt:'500 €'}],480,430,'cinquecento euro per la spesa'),
  I('arR',[],960,430,['altri cinquecento',-0.3]),
  I('pcard',[540,{amt:'+500 €'}],1440,430,'altri cinquecento'),
  P('DAL 4 NOVEMBRE',480,640,'dal quattro novembre',AMB,34,'cal'),
  P('DA APRILE',1440,640,'da aprile',AMB,34,'cal'),
  IC(820,130,'x',[['NESSUNA REGOLA PER I PENSIONATI',34],['CONTANO ALTRE COSE',28,GRN]],470,750,'Il decreto non ha una regola'),
  IC(820,130,'warn',[['FAMIGLIE PICCOLE: UNA REGOLA IN PIÙ',32],['CHE CAMBIA LA RISPOSTA',28,GRN]],1450,750,'per le famiglie piccole'),
  P('IN CHIUSURA: QUANTO VALE, IN UN ANNO, CIÒ CHE PUOI AVERE SENZA LA CARTA',960,850,'In chiusura',DF_,30,'piggy')]},
]);
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE FONTI UFFICIALI',cap:'DECRETO DEL 24 GIUGNO E MESSAGGIO 2906 DELL\'INPS, LETTI PER INTERO',items:[
  P('TUTTO LETTO PER INTERO',960,205,'Abbiamo letto per intero',DF_,36,'book'),
  IC(760,170,'doc',[['DECRETO INTERMINISTERIALE',34],['DEL 24 GIUGNO',32,GRN],['PUBBLICATO IN GAZZETTA UFFICIALE',24,GRN]],500,350,'il decreto interministeriale'),
  IC(760,170,'mail',[['MESSAGGIO DELL\'INPS',34],['NUMERO 2906',34,GRN]],1420,350,'il messaggio numero'),
  I('chev',[480,140,CP15[0],'CHI RICEVE LA CARTA','E COME VIENE SCELTO',true,{fs:34,sfs:28}],440,590,'Prima vediamo chi riceve'),
  I('chev',[480,140,CP15[2],'UNA CARTA','CHE FORSE HAI GIÀ',false,{fs:44,sfs:30}],960,590,'In mezzo'),
  I('chev',[480,140,CP15[1],'GLI ALTRI AIUTI','CHI PRENDE UNA PENSIONE',false,{fs:38,sfs:28}],1480,590,'Poi gli altri aiuti'),
  P('QUELLA CARTA PUÒ ESCLUDERTI DA QUESTA',960,745,'può escluderti da questa',RF_,34,'warn'),
  P('TI FACCIAMO IL CONFRONTO IN EURO',960,830,'il confronto in euro',AMB,36,'calc')]},
]);
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COS\'È LA CARTA',cap:'UN CONTRIBUTO PER NUCLEO FAMILIARE, DA SPENDERE IN ALIMENTARI DI PRIMA NECESSITÀ',items:[
  I('pcard',[500,{title:'CARTA PREPAGATA',kicker:'POSTE ITALIANE'}],330,345,'versato su una carta prepagata'),
  P('PER NUCLEO FAMILIARE',330,570,'Un contributo per nucleo',DF_,28,'people'),
  P('NON PER PERSONA',330,645,'non per persona',RF_,28,'x'),
  P('GENERI ALIMENTARI DI PRIMA NECESSITÀ',1210,215,'generi alimentari di prima necessità',AMB,32,'cart'),
  I('food',['meat','CARNE'],830,345,'carne'),I('food',['fish','PESCE FRESCO'],1020,345,'pesce fresco'),I('food',['milk','LATTE'],1210,345,'latte'),
  I('food',['egg','UOVA'],1400,345,'uova'),I('food',['oil','OLIO'],1590,345,'olio'),
  I('food',['pasta','PASTA'],830,545,'pasta'),I('food',['rice','RISO'],1020,545,'riso'),I('food',['fruit','FRUTTA'],1210,545,'frutta'),
  I('food',['veg','VERDURA'],1400,545,'verdura'),I('food',['coffee','CAFFÈ'],1590,545,'caffè'),
  P('ALCOLICI ESCLUSI',330,735,'Gli alcolici sono esclusi',RF_,32,'x'),
  P('NESSUNA DOMANDA',330,815,'Non devi presentare domanda',GF_,32,'ok'),
  BN('NEI NEGOZI CONVENZIONATI','−15 €','OGNI 100 € DI SPESA',{fs:70,fill:AMB,col:'#5A3300',subcol:'#5A3300',tfs:26,sfs:26},1330,775,'Nei negozi convenzionati')]},
]);
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'UNA PAUSA',cap:'QUESTO VIDEO SI BASA SU FONTI UFFICIALI, LETTE RIGA PER RIGA',items:[
  P('UNA PAUSA BREVE',960,205,'Una pausa breve',DF_,36,'clock'),
  BN('LETTI RIGA PER RIGA','13','ARTICOLI DI DECRETO',{fs:120,fill:GF_,col:'#fff',subcol:'#fff',minw:440,tfs:28,sfs:28},320,400,'tredici articoli di decreto'),
  BN(null,'1','MESSAGGIO DELL\'INPS',{fs:120,fill:GF_,col:'#fff',subcol:'#fff',minw:440,tfs:28,sfs:28},900,400,'un messaggio'),
  IC(520,200,'doc',[['DIVERSE SCHEDE',34],['UFFICIALI',34,GRN]],1500,400,'diverse schede ufficiali'),
  I('btn',['ISCRIVITI'],560,630,'iscriviti al canale'),
  I('bell',[],980,630,'iscriviti al canale',0.65),
  P('È GRATUITO',1400,630,'è gratuito',GF_,36,'ok'),
  P('AIUTA ALTRI PENSIONATI A TROVARCI',960,775,'aiuta altri pensionati',DF_,34,'people'),
  P('ADESSO: CHI ENTRA NELL\'ELENCO',960,850,'Adesso la parte più utile',AMB,36,'next')]},
]);
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COME ARRIVA LA CARTA',cap:'LISTE DELL\'INPS, ELENCO DEI COMUNI, CARTA DELLE POSTE',items:[
  P('COME ARRIVA LA CARTA: IN TRE PASSAGGI',960,205,'Come arriva la carta',DF_,36,'next'),
  I('chev',[520,140,CP15[0],'INPS','PREPARA LE LISTE',true,{fs:46}],380,360,'Primo'),
  I('chev',[520,140,CP15[1],'COMUNI','VERIFICANO E PUBBLICANO',false,{fs:46}],960,360,'Secondo'),
  I('chev',[520,140,AMB,'POSTE ITALIANE','CONSEGNANO O RICARICANO',false,{fs:40}],1540,360,'Terzo'),
  IC(540,190,'web',[['PARTE DAGLI ISEE',32],['GIÀ PRESENTATI',32],['E CONTROLLA I NUCLEI',26,GRN]],380,620,'parte dagli Isee'),
  IC(540,190,'stato',[['VERIFICANO LE LISTE',32],['E PUBBLICANO L\'ELENCO',28,GRN]],960,620,'le verificano'),
  IC(540,190,'mail',[['CONSEGNA LA CARTA',32],['O RICARICA QUELLA',28],['CHE AVEVI GIÀ',28,GRN]],1540,620,'consegna la carta'),
  P('RAPPORTI CON I CITTADINI: I COMUNI E, PER LA CARTA, LE POSTE',960,830,'I rapporti con i cittadini',DF_,32,'people')]},
]);
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'I REQUISITI',cap:'ISEE ORDINARIO FINO A 15.000 € E TUTTI ISCRITTI ALL\'ANAGRAFE',items:[
  P('I REQUISITI SONO DUE',960,205,'I requisiti sono due',DF_,36,'ok'),
  IC(760,190,'house',[['ISCRIZIONE ALL\'ANAGRAFE',34],['DEL COMUNE, DI OGNI PERSONA',28,GRN],['DEL NUCLEO',28,GRN]],500,360,'l\'iscrizione all\'anagrafe'),
  IC(760,190,'id',[['ISEE ORDINARIO',38],['IN CORSO DI VALIDITÀ',30,GRN]],1420,360,'un Isee ordinario'),
  I('gauge',[1300,20000,15000,'FINO A 15.000 €',[0,5000,10000,15000,20000]],960,610,'fino a quindicimila'),
  IC(760,140,'cal',[['AL 3 AGOSTO 2026',36],['DATA DI USCITA IN GAZZETTA',26,GRN]],500,795,'Contano i requisiti'),
  IC(760,160,'clock',[['ISEE: VALE FINO AL 31 DICEMBRE',30],['DELL\'ANNO IN CUI LO PRESENTI',26,GRN],['UNO DEL 2025 ERA GIÀ SCADUTO',24,RED_]],1420,800,'La dichiarazione per')]},
]);
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE ESCLUSIONI',cap:'NON SPETTA SE IN FAMIGLIA C\'È CHI PRENDE ALTRE MISURE',items:[
  P('NON SPETTA SE IN FAMIGLIA C\'È CHI PRENDE',960,205,'Il contributo non spetta',RF_,36,'x'),
  IC(800,150,'x',[['ASSEGNO DI INCLUSIONE',36]],520,330,'l\'assegno di inclusione',{stroke:RED_}),
  IC(800,150,'x',[['CARTA ACQUISTI',36]],1400,330,'la Carta acquisti',{stroke:RED_}),
  IC(800,170,'x',[['ALTRA MISURA CONTRO LA POVERTÀ',30],['CON SUSSIDIO NAZIONALE,',26,GRN],['REGIONALE O COMUNALE',26,GRN]],520,520,'un\'altra misura contro la povertà',{stroke:RED_}),
  IC(800,170,'x',[['NASPI, CASSA INTEGRAZIONE',32],['O SOSTEGNO SIMILE',28,GRN],['(UN COMPONENTE DEL NUCLEO)',24,GRN]],1400,520,'Non spetta nemmeno',{stroke:RED_}),
  P('SEGNATI LA CARTA ACQUISTI',470,725,'Segnati',AMB,36,'pen'),
  IC(900,130,'people',[['È PENSATA ANCHE PER GLI ANZIANI',34],['CON REDDITI BASSI',34,GRN]],1340,725,'è pensata anche per gli anziani'),
  P('CI TORNIAMO PIÙ AVANTI',960,850,'Ci torniamo',DF_,34,'next')]},
]);
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CARTE LIMITATE',cap:'1.177.597 CARTE IN TUTTA ITALIA: CONTA ANCHE DOVE ABITI',items:[
  P('RISPETTARE I REQUISITI NON BASTA: LE CARTE SONO LIMITATE',960,205,'le carte sono limitate',RF_,34,'warn'),
  BN('IN TUTTA ITALIA','1.177.597','CARTE',{fs:104,fill:GF_,col:'#fff',subcol:'#fff',minw:760,tfs:30,sfs:30},560,420,'un milione'),
  IC(720,150,'doc',[['UNA LISTA SOLA',36],['PER ENTRAMBI GLI ANNI',30,GRN]],1400,380,'una lista sola'),
  I('pie2',[95],960,650,'A ogni Comune'),
  IC(700,160,'people',[['METÀ IN BASE AGLI ABITANTI',34]],480,650,'metà in base agli abitanti'),
  IC(700,200,'coin',[['METÀ IN BASE AL REDDITO MEDIO',30],['DEL COMUNE: QUANTO È LONTANO',26,GRN],['DA QUELLO NAZIONALE',26,GRN]],1450,650,'metà in base a quanto'),
  P('QUINDI CONTA ANCHE DOVE ABITI',960,850,'Quindi conta anche dove abiti',AMB,40,'house')]},
]);
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE TRE FASCE',cap:'TRE FASCE DI PRIORITÀ, TUTTE CON ALMENO TRE PERSONE',items:[
  P('COME SCELGONO I NOMI?',960,205,'Come scelgono i nomi',DF_,36,'q'),
  I('tier',[1400,104,1,'PRIMA FASCIA','DATA DI NASCITA DI UN COMPONENTE',CP15[0]],800,340,'Le prime due guardano'),
  I('tier',[1400,104,2,'SECONDA FASCIA','DATA DI NASCITA DI UN COMPONENTE',CP15[1]],800,460,'alla data di nascita'),
  I('tier',[1400,104,3,'TERZA FASCIA','NESSUNA DATA DI NASCITA',CP15[2]],800,580,'la terza no'),
  I('card',['IN OGNI FASCIA',340,300,{hc:'#0B4A50',hfs:28,lines:[['ALMENO',46,-18,INK],['TRE PERSONE',40,36,GRN]],icon:['people',0,106,1.3,null,null,INK]}],1700,460,'almeno tre persone'),
  P('A PARITÀ DI FASCIA: PASSA AVANTI L\'ISEE PIÙ BASSO',960,700,'A parità di fascia',AMB,34,'down'),
  IC(1000,130,'x',[['PENSIONATI SOLI O IN COPPIA:',32],['NON RIENTRANO IN QUESTE FASCE',32,RED_]],600,810,'I pensionati che vivono soli',{stroke:RED_}),
  P('ALLORA SONO ESCLUSI?',1530,810,'Allora sono esclusi',RF_,40,'q')]},
]);
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA REGOLA IN PIÙ',cap:'ARTICOLO 6: LE CARTE AVANZATE ANCHE A NUCLEI DI UNA PERSONA',items:[
  P('NON DEL TUTTO',500,205,'Non del tutto',AMB,40,'q'),
  P('ARTICOLO 6 DEL DECRETO',1300,205,'Per l\'articolo sei',DF_,34,'book'),
  I('chev',[520,150,CP15[0],'CARTE AVANZATE','DOPO LE TRE FASCE',true,{fs:42}],380,370,'le carte avanzate'),
  I('chev',[520,150,CP15[1],'IL COMUNE SCEGLIE','NELL\'ELENCO PREDISPOSTO',false,{fs:42}],960,370,'scegliendo'),
  I('chev',[520,150,AMB,'STATO DI BISOGNO','NUCLEI ANCHE DI UNA PERSONA',false,{fs:42,sfs:26}],1540,370,'i nuclei in effettivo'),
  IC(1100,110,'ok',[['QUINDI ANCHE UNA FAMIGLIA PICCOLA PUÒ AVERE UNA CARTA',32]],960,520,'Quindi anche una famiglia piccola'),
  P('MA DIPENDE DA DUE COSE',960,625,'ma dipende da due cose',RF_,34,'warn'),
  IC(780,140,'house',[['NEL SUO COMUNE',34],['AVANZANO CARTE',30,GRN]],500,740,'che nel suo Comune avanzino carte'),
  IC(780,140,'stato',[['IL COMUNE SCEGLIE',34],['QUELLA FAMIGLIA',30,GRN]],1420,740,'che il Comune scelga quella famiglia'),
  P('NEL DECRETO NON È SCRITTO COME SI VALUTA IL BISOGNO',960,850,'Nel decreto non c\'è scritto',DF_,32,'x')]},
]);
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COME SCOPRIRE SE CI SEI',cap:'L\'ELENCO È SUL SITO DEL COMUNE: NON SERVE FARE DOMANDA',items:[
  P('COME SCOPRIRE SE CI SEI?',560,205,'Come scoprire se ci sei',DF_,36,'q'),
  P('NON DEVI FARE DOMANDA',1380,205,'Non devi fare domanda',GF_,36,'ok'),
  I('list',[720,440,'ELENCO DEI BENEFICIARI · COMUNE',6,2],480,520,'è pubblicato in evidenza'),
  IC(900,140,'web',[['ELENCO PUBBLICATO IN EVIDENZA',32],['SUL SITO DEL TUO COMUNE',30,GRN]],1330,360,'sul sito del tuo Comune'),
  IC(900,140,'mail',[['IL COMUNE SEGNALA AI RESIDENTI',32],['E SPIEGA COME RITIRARE LA CARTA',28,GRN]],1330,530,'il Comune segnala'),
  IC(900,140,'office',[['RITIRO AGLI UFFICI POSTALI ABILITATI',30],['SU PRENOTAZIONE E A SCAGLIONI',28,GRN]],1330,700,'Il ritiro'),
  P('SE AVEVI GIÀ UNA CARTA E RIENTRI: LA RICARICA ARRIVA SU QUELLA',960,850,'Se avevi già una carta',AMB,32,'coin')]},
]);
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE DATE DA SEGNARE',cap:'PRIMO PAGAMENTO ENTRO IL 16 DICEMBRE 2026',items:[
  P('LA DATA DA SEGNARE',960,205,'La data da segnare',AMB,40,'cal'),
  OV(I('axis',[],960,560,'La data da segnare')),
  OV(I('pin',['16 DICEMBRE','PRIMO PAGAMENTO CON LA CARTA',RF_,170],345,560,'il primo pagamento con la carta')),
  P('ALTRIMENTI PERDI IL CONTRIBUTO DEL 2026',520,775,'altrimenti perdi il contributo',RF_,30,'x'),
  OV(I('pin',['1 APRILE → 31 AGOSTO','ATTIVA LA CARTA CON UN PAGAMENTO',GF_,170],1165,560,'Per il duemilaventisette')),
  OV(I('band',[683],1165,560,'dal primo aprile al trentuno agosto')),
  P('IL SECONDO IMPORTO PUÒ ESSERE RICALCOLATO',1330,845,'Il secondo importo',DF_,30,'calc'),
  OV(I('pin',['10 OTT 2027','SOMME SPESE ENTRO',AMB,170],1684,560,'entro il dieci ottobre'))]},
]);
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA CARTA ACQUISTI',cap:'CARTA ACQUISTI: 80 € OGNI DUE MESI, 480 € L\'ANNO',items:[
  P('TORNIAMO ALLA CARTA ACQUISTI',960,205,'Torniamo alla Carta acquisti',DF_,36,'next'),
  IC(780,150,'people',[['DAI 65 ANNI COMPIUTI',36],['E REDDITI BASSI',30,GRN]],500,350,'Spetta a chi ha compiuto'),
  I('coins6',[],1380,360,'ogni due mesi arrivano ottanta euro'),
  BN('IN UN ANNO','480 €','6 × 80 €',{fs:96,fill:AMB,col:'#5A3300',subcol:'#5A3300',tfs:28,sfs:28,minw:420},500,570,'quattrocentoottanta euro l\'anno'),
  IC(900,170,'cart',[['DA USARE PER COMPRARE CIBO',32],['NEGLI ESERCIZI CONVENZIONATI',32],['E PAGARE LUCE E GAS ALLE POSTE',28,GRN]],1380,570,'da usare per comprare cibo'),
  I('vs',[],620,790,'Se ce l\'hai'),
  P('DIFFERENZA: 20 € L\'ANNO',1560,740,'la differenza è di venti euro',AMB,32,'down'),
  P('QUELLA CARTA DIPENDE DAL COMUNE',1560,830,'quella carta dipende',RF_,24,'house')]},
]);
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE SOGLIE DEL 2026',cap:'SOGLIE 2026 DELLA CARTA ACQUISTI: REDDITI E ISEE',items:[
  P('NEL 2026: REDDITI PERSONALI E TRATTAMENTI, ANCHE NON TASSATI',960,205,'Nel duemilaventisei i redditi',DF_,32,'coin'),
  I('trow2',[1500,[['DA 65 A 69 ANNI','#2B6F8F','#fff',0.4],['SOTTO 8.230,81 €',AMB,'#5A3300',0.6]],{h:96}],960,330,'sotto ottomiladuecentotrenta'),
  I('trow2',[1500,[['DAI 70 ANNI','#1B9F81','#fff',0.4],['SOTTO 10.974,42 €',AMB,'#5A3300',0.6]],{h:96}],960,450,'sotto diecimila'),
  I('trow2',[1500,[['ISEE IN CORSO DI VALIDITÀ','#0B4A50','#fff',0.55],['SOTTO 8.230,81 €',AMB,'#5A3300',0.45]],{h:96}],960,570,'Serve anche un Isee'),
  IC(740,150,'lock',[['ALTRE REGOLE RIGUARDANO',30],['PATRIMONIO, UTENZE E PROPRIETÀ',30,GRN]],500,745,'Altre regole riguardano'),
  IC(740,150,'mail',[['PER LA DOMANDA:',30],['SI CHIEDE ALLE POSTE',34,GRN]],1420,745,'Si chiede alle Poste')]},
]);
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL TICKET SANITARIO',cap:'ESENZIONI E01 ED E03 PER REDDITO (SISTEMA TESSERA SANITARIA)',items:[
  P('IL TICKET SANITARIO',960,205,'Il ticket sanitario',DF_,36,'doc'),
  IC(1500,130,'hcard',[['SISTEMA TESSERA SANITARIA: ELENCO DELLE ESENZIONI PER REDDITO',32]],960,330,'Il Sistema Tessera Sanitaria'),
  I('code',[800,250,'E01',[['OLTRE I 65 ANNI',36],['REDDITO FAMILIARE',30,GRN],['FINO A 36.151,98 €',38,INK]],'#2B6F8F'],500,560,'Codice E zero uno'),
  I('code',[800,250,'E03',[['TITOLARI DI ASSEGNO SOCIALE',32],['(LA VECCHIA PENSIONE SOCIALE)',26,GRN],['E FAMILIARI A CARICO',30,INK]],'#1B9F81'],1420,560,'Codice E zero tre'),
  P('LE REGIONI POSSONO AGGIUNGERE ALTRE CONDIZIONI',960,790,'Le Regioni possono',AMB,34,'land')]},
]);
SPECS[16]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA PENSIONE AL MINIMO',cap:'ESENZIONE E04: PENSIONE AL MINIMO E PIÙ DI 60 ANNI',items:[
  I('code',[780,240,'E04',[['PENSIONE AL MINIMO',36],['E PIÙ DI 60 ANNI',34,GRN]],'#E39A1C'],480,350,'La E zero quattro'),
  BN('REDDITO DI FAMIGLIA, SOTTO','8.263,31 €',null,{fs:84,fill:GF_,col:'#fff',subcol:'#fff',tfs:28,minw:640},1380,350,'reddito di famiglia sotto'),
  BN('CON IL CONIUGE, SALE A','11.362,05 €',null,{fs:84,fill:AMB,col:'#5A3300',subcol:'#5A3300',tfs:28,minw:640},1380,590,'che con il coniuge sale'),
  IC(780,200,'phone',[['PER VERIFICARE, CHIEDI',30],['ALL\'AZIENDA SANITARIA',34,GRN],['O AL MEDICO DI FAMIGLIA',34,GRN]],480,590,'Per verificare'),
  IC(1500,130,'pen',[['NON RISULTI NELL\'ELENCO ANNUALE?',34],['PUOI PRESENTARE UN\'AUTOCERTIFICAZIONE',34,GRN]],960,810,'Se non risulti')]},
]);
SPECS[17]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CANONE TV',cap:'CANONE TV: ESENZIONE DAI 75 ANNI, REDDITO FINO A 8.000 €',items:[
  P('DAI 75 ANNI',440,215,'Dai settantacinque anni',AMB,40,'cake'),
  I('tvb',[300],440,420,'l\'esenzione dal canone televisivo'),
  BN('CANONE TV','90 €','ALL\'ANNO · AGENZIA DELLE ENTRATE',{fs:96,fill:GF_,col:'#fff',subcol:'#fff',tfs:28,sfs:24,minw:560},440,690,'novanta euro l\'anno'),
  IC(900,150,'coin',[['REDDITO DELL\'ANNO PRIMA, TUO E DEL CONIUGE',28],['NON OLTRE 8.000 €',38,GRN]],1330,330,'Conta il reddito'),
  IC(900,130,'x',[['NON CONTANO: LA CASA DOVE ABITI',28],['E I REDDITI ESENTI DA IRPEF',28,GRN]],1330,490,'esclusi la casa'),
  IC(900,150,'people',[['IN CASA, OLTRE AL CONIUGE: NESSUNO',28],['CON UN REDDITO PROPRIO (TRANNE COLF E BADANTI)',24,GRN]],1330,650,'In casa, oltre al coniuge'),
  IC(900,110,'pen',[['LA DICHIARAZIONE SI FA UNA VOLTA',30]],1330,790,'La dichiarazione si fa')]},
]);
SPECS[18]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL BONUS BOLLETTE',cap:'BONUS SOCIALE: ISEE FINO A 9.796 €, AUTOMATICO',items:[
  P('PER LE BOLLETTE: BONUS SOCIALE',960,205,'Per le bollette',DF_,36,'bulb'),
  I('stamp',[['AUTOMATICO'],'#1B9F81',38,-4],1690,370,'automatico'),
  I('gauge',[1100,12000,9796,'ISEE FINO A 9.796 € · SOGLIA DI QUEST\'ANNO',[0,3000,6000,9000,12000]],740,380,'con un Isee fino a'),
  I('tile',['bolt','−30 %','DELLA SPESA MEDIA','#E39A1C'],290,640,'Sulla luce'),
  I('tile',['flame','−15 %','DELLA SPESA','#E4572E'],750,640,'sul gas'),
  I('tile',['drop','50 LITRI','AL GIORNO A PERSONA','#2B8FA0'],1210,640,'sull\'acqua'),
  I('tile',['bin','−25 %','DELLA TASSA','#1B9F81'],1670,640,'sui rifiuti'),
  P('IL CONTRATTO DEVE ESSERE INTESTATO A UN COMPONENTE DEL NUCLEO',960,850,'Il contratto deve essere',AMB,32,'id')]},
]);
SPECS[19]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO FINALE',cap:'',items:[
  P('IL CONTO FINALE',960,195,'Il conto finale',AMB,40,'calc'),
  P('75 ANNI ENTRO GENNAIO',430,265,'Con settantacinque anni',DF_,28,'cake'),
  P('REDDITI SOTTO 8.000 €',960,265,'redditi sotto ottomila',DF_,28,'coin'),
  P('ISEE E RESTO IN REGOLA',1490,265,'un Isee nei limiti',DF_,28,'ok'),
  ...EQ(385,[['num','90 €','novanta di canone',{sub:'CANONE TV'}],['op','+',['novanta di canone',0.9]],['num','480 €','quattrocentoottanta di Carta',{sub:'CARTA ACQUISTI'}],['op','=',['puoi arrivare a',0.5]],['num','570 €','puoi arrivare a',{sub:'L\'ANNO, NEL 2026',fill:AMB}]],66,260),
  P('PIÙ TICKET E BOLLETTE',960,500,'più ticket e bollette',DF_,34,'next'),
  I('dbox',[1500,140,[['CANALE INFORMATIVO, NON CONSULENZA, NON AFFILIATO ALL\'INPS',30,'#fff'],['VERIFICA SU INPS.IT O CON UN PATRONATO',30,'#7FF0D2']]],960,628,'Questo canale informa')]},
]);
