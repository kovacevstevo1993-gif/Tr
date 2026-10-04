const MINT='#2FD0A8',AMB2='#FFB838',DIM='#2B6F77';
const RED_='#E4412C';

function tag(p,s,w,fill,col,fs){fs=fs||40;w=Math.max(w,s.length*fs*0.8+90);const g=el('g',{},p);
 el('rect',{x:-w/2,y:-38,width:w,height:76,rx:38,fill:fill,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
 txt(g,s,0,fs*0.36,fs,col||'#fff','bold');return g;}
function stamp(p,s,w,col,fs){w=Math.max(w,s.length*fs*0.8+90);const g=el('g',{},p);
 el('rect',{x:-w/2,y:-fs*0.85,width:w,height:fs*1.7,rx:16,fill:'#FFFFFF',stroke:col,'stroke-width':10,filter:'url(#g_sh2)'},g);
 txt(g,s,0,fs*0.34,fs,col,'900');return g;}
function docCard(p,title,w,h,hc,fs){hc=hc||GRN;fs=fs||36;const g=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:74,rx:26,fill:hc},g);el('rect',{x:-w/2,y:-h/2+44,width:w,height:30,fill:hc},g);
 txt(g,title,0,-h/2+48,fs,'#fff','bold');return g;}
function magnifier(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('circle',{r:74,fill:'rgba(255,255,255,0.22)',stroke:'#fff','stroke-width':14},g);
 el('line',{x1:54,y1:54,x2:128,y2:128,stroke:AMB,'stroke-width':24,'stroke-linecap':'round'},g);return g;}
function arrowDown(p,col){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:'M-40 -70 H40 V0 H80 L0 80 L-80 0 H-40Z',fill:col||AMB,stroke:'#fff','stroke-width':6,'stroke-linejoin':'round'},g);return g;}
function arrowRight(p,col){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:'M-70 -36 H0 V-76 L80 0 L0 76 V36 H-70Z',fill:col||AMB,stroke:'#fff','stroke-width':6,'stroke-linejoin':'round'},g);return g;}
function calc(p){const g=el('g',{filter:'url(#g_sh)'},p);
 el('rect',{x:-110,y:-150,width:220,height:300,rx:30,fill:'#0B4A50',stroke:'#fff','stroke-width':6},g);
 el('rect',{x:-86,y:-124,width:172,height:62,rx:12,fill:'#D6F5EC'},g);txt(g,'=',60,-76,48,INK,'900','end');
 for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('rect',{x:-86+c*62,y:-40+r*58,width:48,height:42,rx:10,fill:c==2&&r==2?AMB:'#2FBF9B'},g);
 return g;}
function circN(p,r,n,fill){const g=el('g',{},p);
 el('circle',{r:r,fill:fill,stroke:'#fff','stroke-width':9,filter:'url(#g_sh2)'},g);txt(g,n,0,r*0.38,r*1.1,'#fff','900');return g;}
function bars(p,n){const g=el('g',{},p);const r=[];const W=1100,gap=W/n,bw=gap*0.7;
 el('rect',{x:-W/2-20,y:0,width:W+40,height:10,rx:5,fill:'#0A3F45',stroke:LT,'stroke-width':2},g);
 for(let i=0;i<n;i++){const h=110+i*(300/(n-1));
  const b=el('rect',{x:-W/2+i*gap+(gap-bw)/2,y:-h,width:bw,height:h,rx:10,fill:'#2B6F77',stroke:'#fff','stroke-opacity':.3,'stroke-width':2},g);r.push({b,h,x:-W/2+i*gap+gap/2});}
 txt(g,'ANNI DI LAVORO  →',0,70,34,LT,'bold');return {g,r};}
function setBar(o,i,k,col){const e=o.r[i];e.b.setAttribute('y',-e.h*k);e.b.setAttribute('height',Math.max(0.1,e.h*k));if(col)e.b.setAttribute('fill',col);}
function browser(p,url,w,h){const g=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:80,rx:26,fill:'#0B4A50'},g);el('rect',{x:-w/2,y:-h/2+50,width:w,height:30,fill:'#0B4A50'},g);
 [0,1,2].forEach(i=>el('circle',{cx:-w/2+44+i*38,cy:-h/2+40,r:12,fill:['#E4412C',AMB,'#2FBF9B'][i]},g));
 el('rect',{x:-w/2+190,y:-h/2+14,width:w-260,height:52,rx:26,fill:'#D6F5EC'},g);txt(g,url,-w/2+190+(w-260)/2,-h/2+50,34,INK,'bold');
 return g;}
function row(p,label,x,y,w,ok){const g=el('g',{},p);
 el('rect',{x:x-w/2,y:y-34,width:w,height:68,rx:18,fill:'#D6F5EC',stroke:'#1B9F81','stroke-width':4},g);
 txt(g,label,x+30,y+12,34,INK,'bold');
 if(ok)el('path',{d:'M'+(x-w/2+26)+' '+(y+2)+' l16 18 l30 -36',fill:'none',stroke:'#1B9F81','stroke-width':11,'stroke-linecap':'round','stroke-linejoin':'round'},g);return g;}

const pop=(t,a,b)=>Math.max(0,eob(seg(t,a,b)));
function piggy(p){const g=el('g',{filter:'url(#g_sh)'},p);
 el('ellipse',{cx:0,cy:0,rx:190,ry:140,fill:'#FFB3A3',stroke:'#fff','stroke-width':8},g);
 el('path',{d:'M-80 -120 L-40 -190 L10 -125Z',fill:'#F08A78',stroke:'#fff','stroke-width':6,'stroke-linejoin':'round'},g);
 el('ellipse',{cx:170,cy:20,rx:50,ry:42,fill:'#F08A78',stroke:'#fff','stroke-width':6},g);
 el('circle',{cx:160,cy:15,r:7,fill:'#7A2A00'},g);el('circle',{cx:182,cy:15,r:7,fill:'#7A2A00'},g);
 el('circle',{cx:100,cy:-45,r:12,fill:'#7A2A00'},g);
 el('rect',{x:-70,y:-148,width:130,height:16,rx:8,fill:'#7A2A00'},g);
 [-110,-40,60,130].forEach(x=>el('rect',{x:x-22,y:112,width:44,height:60,rx:14,fill:'#F08A78',stroke:'#fff','stroke-width':6},g));
 return g;}
function coinS(p,r){const g=el('g',{filter:'url(#g_sh2)'},p);el('circle',{r:r,fill:AMB,stroke:'#fff','stroke-width':6},g);txt(g,'€',0,r*0.38,r*1.1,'#5A3300','900');return g;}
function doorN(p,n,fill){const g=el('g',{},p);const d=el('g',{},g);door(d);
 el('rect',{x:-110,y:-262,width:220,height:420,rx:12,fill:'#0B4A50'},g);
 el('circle',{cx:70,cy:20,r:14,fill:AMB},g);
 const b=el('g',{},g);b.setAttribute('transform','translate(0 -345)');circN(b,66,String(n),fill||'url(#g_badge)');return g;}
function avatar(p,r){const g=el('g',{},p);medal(g,r);return g;}
function bill(p,s){const g=el('g',{filter:'url(#g_sh)'},p);
 el('rect',{x:-190,y:-100,width:380,height:200,rx:22,fill:'#D6F5EC',stroke:'#1B9F81','stroke-width':8},g);
 el('circle',{r:64,fill:'#fff',stroke:'#1B9F81','stroke-width':6},g);txt(g,s,0,16,46,INK,'900');
 txt(g,'€',-150,-48,44,'#1B9F81','900');txt(g,'€',150,76,44,'#1B9F81','900');return g;}
