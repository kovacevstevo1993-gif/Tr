// ---------- helper short 2 ----------
let UID=0;
const AMB='#FFB838',INK='#0B4A50',GRN='#1B9F81',LT='#7FF0D2';
function calendarPage(p,headTxt,bigTxt,bigSize,subTxt){
 const g=el('g',{},p);const id='cc'+(++UID);
 el('rect',{x:-232,y:6,width:464,height:566,rx:34,fill:'#C9D6D8'},g);
 el('rect',{x:-230,y:0,width:460,height:560,rx:34,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 const cp=el('clipPath',{id:id},g);el('rect',{x:-230,y:0,width:460,height:560,rx:34},cp);
 const hg=el('g',{'clip-path':'url(#'+id+')'},g);
 el('rect',{x:-230,y:0,width:460,height:130,fill:'url(#g_head)'},hg);
 el('rect',{x:-230,y:0,width:460,height:10,fill:'#fff',opacity:.35},hg);
 el('rect',{x:-230,y:128,width:460,height:8,fill:INK,opacity:.15},hg);
 const head=txt(g,headTxt,0,86,46,'#FFFFFF');
 const big=txt(g,bigTxt,0,bigSize>200?400:376,bigSize,INK);
 const sub=txt(g,subTxt||'',0,478,46,GRN);
 for(let i=0;i<14;i++)el('rect',{x:-200+i*30,y:512,width:16,height:4,rx:2,fill:'#B7C7CA'},g);
 metalRing(g,-120,-44,36,92);metalRing(g,120,-44,36,92);
 return {g,head,big,sub};}
function plate(p,big,small){
 const g=el('g',{},p);
 el('rect',{x:-210,y:-150,width:420,height:300,rx:44,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-210,y:-150,width:420,height:300,rx:44,fill:'none',stroke:'#fff','stroke-opacity':.8,'stroke-width':4},g);
 const b=txt(g,big,0,48,230,INK);
 const s=txt(g,small,0,118,38,GRN);
 return {g,b,s};}
function dotsRow(p,n,y){const g=el('g',{},p);const a=[];
 for(let i=0;i<n;i++){const c=el('circle',{cx:(i-(n-1)/2)*42,cy:y,r:15,fill:'#0A3F45',opacity:.55,stroke:'#7FF0D2','stroke-width':2},g);a.push(c);}
 return {g,a};}
function lightDot(d,on,k){ // k = pop 0..1
 d.setAttribute('fill',on?AMB:'#0A3F45');d.setAttribute('opacity',on?1:.55);d.setAttribute('r',15+(on?9*Math.sin(clamp(k)*Math.PI):0));}
function chip(p,label,w){w=w||300;const g=el('g',{},p);
 el('rect',{x:-w/2,y:-46,width:w,height:92,rx:46,fill:AMB,filter:'url(#g_sh2)'},g);
 el('rect',{x:-w/2,y:-46,width:w,height:92,rx:46,fill:'none',stroke:'#fff','stroke-width':5,'stroke-opacity':.85},g);
 const t=txt(g,label,0,19,54,'#5A3300');return {g,t};}
function warn(p){const g=el('g',{},p);
 el('path',{d:'M0 -150 L170 130 Q182 152 158 152 L-158 152 Q-182 152 -170 130 Z',fill:'#fff',stroke:'#E4412C','stroke-width':28,'stroke-linejoin':'round',filter:'url(#g_sh)'},g);
 txt(g,'!',0,104,210,'#0B2E33');return g;}
function qBubble(p,r){const g=el('g',{},p);
 el('circle',{cx:0,cy:0,r:r,fill:'url(#g_badge)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},g);
 txt(g,'?',0,r*.38,r*1.25,'#fff');return g;}
function medal(p,female){const g=el('g',{},p);
 el('circle',{cx:0,cy:0,r:190,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('circle',{cx:0,cy:0,r:190,fill:'none',stroke:'#fff','stroke-width':6,'stroke-opacity':.8},g);
 const cp='mc'+(++UID);const c=el('clipPath',{id:cp},g);el('circle',{cx:0,cy:0,r:176},c);
 const ig=el('g',{'clip-path':'url(#'+cp+')'},g);
 el('circle',{cx:0,cy:0,r:176,fill:'#E4F5F1'},ig);
 if(female){
  el('circle',{cx:0,cy:-52,r:84,fill:'#0B4A50'},ig); // capelli
  el('path',{d:'M-84 -52 L-96 70 Q0 96 96 70 L84 -52 Z',fill:'#0B4A50'},ig);
  el('path',{d:'M-60 176 L-46 40 L46 40 L60 176 Z',fill:GRN},ig);
  el('path',{d:'M-150 176 L-60 60 L60 60 L150 176 Z',fill:GRN},ig);
  el('rect',{x:-22,y:20,width:44,height:34,fill:'#F2C9A5'},ig);
  el('circle',{cx:0,cy:-42,r:60,fill:'#F7D5B5'},ig);
  el('path',{d:'M-62 -52 Q-10 -120 62 -52 Q20 -80 -62 -52 Z',fill:'#0B4A50'},ig);
  el('circle',{cx:-20,cy:-38,r:5,fill:'#0B4A50'},ig);el('circle',{cx:20,cy:-38,r:5,fill:'#0B4A50'},ig);
  el('path',{d:'M-14 -14 Q0 -4 14 -14',fill:'none',stroke:'#C0583F','stroke-width':5,'stroke-linecap':'round'},ig);
 }else{
  el('path',{d:'M-140 176 Q-140 50 0 50 Q140 50 140 176 Z',fill:INK},ig);
  el('polygon',{points:'-34,50 34,50 0,110',fill:'#fff'},ig);
  el('polygon',{points:'-12,66 12,66 8,150 -8,150',fill:'#E4412C'},ig);
  el('rect',{x:-24,y:20,width:48,height:40,fill:'#F2C9A5'},ig);
  el('circle',{cx:0,cy:-30,r:62,fill:'#F7D5B5'},ig);
  el('path',{d:'M-62 -40 Q-50 -100 0 -96 Q50 -100 62 -40 Q40 -70 0 -66 Q-40 -70 -62 -40 Z',fill:'#6F878C'},ig);
  el('circle',{cx:-20,cy:-28,r:5,fill:INK},ig);el('circle',{cx:20,cy:-28,r:5,fill:INK},ig);
  el('path',{d:'M-16 -4 Q0 8 16 -4',fill:'none',stroke:'#C0583F','stroke-width':5,'stroke-linecap':'round'},ig);
 }
 return g;}
function hardhat(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:'M-135 40 A135 135 0 0 1 135 40 Z',fill:'#FFC21F'},g);
 el('rect',{x:-30,y:-100,width:60,height:140,rx:18,fill:'#FFD65A'},g);
 el('rect',{x:-170,y:34,width:340,height:40,rx:20,fill:'#F2A900'},g);
 el('path',{d:'M-100 20 A110 110 0 0 1 -50 -70',fill:'none',stroke:'#fff','stroke-width':12,'stroke-linecap':'round',opacity:.6},g);
 return g;}
function shield(p){const g=el('g',{filter:'url(#g_sh)'},p);
 el('path',{d:'M0 -200 L170 -135 L170 30 Q170 150 0 220 Q-170 150 -170 30 L-170 -135 Z',fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,'stroke-linejoin':'round'},g);
 el('path',{d:'M0 -170 L140 -118 L140 28 Q140 128 0 188 Q-140 128 -140 28 L-140 -118 Z',fill:'none',stroke:'#fff','stroke-width':3,opacity:.5},g);
 return g;}
function progress(p){const g=el('g',{},p);
 const W=760,S=W/45;
 el('rect',{x:-W/2,y:0,width:W,height:46,rx:23,fill:'#0A3F45',opacity:.7},g);
 el('rect',{x:-W/2,y:0,width:W,height:46,rx:23,fill:'none',stroke:LT,'stroke-width':3,opacity:.6},g);
 const fill=el('rect',{x:-W/2,y:0,width:10,height:46,rx:23,fill:'url(#g_badge)'},g);
 for(let k=0;k<=40;k+=10){el('rect',{x:-W/2+k*S-1.5,y:56,width:3,height:16,fill:'#fff',opacity:.7},g);txt(g,''+k,-W/2+k*S,112,34,'#E9FBF6','bold','middle');}
 const cnt=txt(g,'',0,-52,70,'#fff');
 const lab=txt(g,'ANNI DI CONTRIBUTI',0,176,36,LT);
 function set(v){fill.setAttribute('width',Math.max(0,v*S));const Y=Math.floor(v+1e-6),M=Math.round((v-Y)*12);cnt.textContent=Y+' anni e '+M+' mesi';}
 return {g,set};}
function pill(p,label,w,fs,fill){const g=el('g',{},p);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:fs*1.8,rx:fs*0.9,fill:fill||AMB,filter:'url(#g_sh2)'},g);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:fs*1.8,rx:fs*0.9,fill:'none',stroke:'#fff','stroke-width':4,'stroke-opacity':.85},g);
 txt(g,label,0,fs*0.36,fs,fill?'#fff':'#5A3300');return g;}
function checkBadge(p,r){const g=el('g',{},p);
 el('circle',{cx:0,cy:0,r:r,fill:'url(#g_badge)',stroke:'#fff','stroke-width':r*0.12,filter:'url(#g_sh2)'},g);
 el('path',{d:`M${-r*.42} ${r*.02} L${-r*.1} ${r*.34} L${r*.46} ${-r*.3}`,fill:'none',stroke:'#fff','stroke-width':r*.22,'stroke-linecap':'round','stroke-linejoin':'round'},g);return g;}
function ring(p,r){return el('circle',{cx:0,cy:0,r:r,fill:'none',stroke:LT,'stroke-width':6,opacity:0},p);}

