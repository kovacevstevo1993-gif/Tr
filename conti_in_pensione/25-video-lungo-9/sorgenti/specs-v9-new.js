// ===== VIDEO 9 (pensioni di dicembre: tredicesima, bonus 154,94, quattordicesima) =====
// Un po' diverso dai video 7-8 (N.37, N.47): titoletto a sinistra con calendarietto DIC e filetto, didascalia con bordo sottile,
// barra gialla e moneta €, personaggi disegnati (Franco, Anna, Lucia), cedolino di dicembre, righello della soglia,
// barra di coppia, striscia dei mesi, tabella della quattordicesima, griglia finale, telefono My Inps, sfondo di dicembre.
function topLabel(g,s){const t=el('g',{transform:'translate(-840 0)'},g);
 el('rect',{x:-34,y:-38,width:68,height:74,rx:12,fill:'url(#g_paper)',filter:'url(#g_sh3)'},t);
 el('rect',{x:-34,y:-38,width:68,height:26,rx:10,fill:RED_},t);el('rect',{x:-34,y:-22,width:68,height:10,fill:RED_},t);
 txt(t,'DIC',0,-18,17,'#fff','bold');txt(t,'1',0,28,34,INK,'900');
 const x=txt(t,s,62,12,36,'#7FF0D2','bold','start');x.setAttribute('letter-spacing','6');
 const w=tw(s,36)+s.length*6;el('line',{x1:62+w+30,y1:0,x2:1680,y2:0,stroke:'#7FF0D2','stroke-width':3,opacity:.35},t);
 el('circle',{cx:1680,cy:0,r:7,fill:'#7FF0D2',opacity:.6},t);return t;}
function cap(g,s,size){size=size||44;size=Math.min(size,1540/Math.max(1,tw(s,1)));const w=Math.min(1820,tw(s,size)+230);const c=el('g',{},g);
 el('rect',{x:-w/2,y:-56,width:w,height:112,rx:26,fill:'#06303A',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:-56,width:w,height:112,rx:26,fill:'none',stroke:'#7FF0D2','stroke-width':3,opacity:.55},c);
 el('rect',{x:-w/2,y:-56,width:18,height:112,rx:9,fill:AMB},c);
 el('circle',{cx:-w/2+78,cy:0,r:32,fill:AMB,stroke:'#fff','stroke-width':4},c);txt(c,'€',-w/2+78,13,38,'#5A3300','900');
 txt(c,s,(-w/2+125+w/2-30)/2,size*0.36,size,'#FFFFFF','bold');return c;}
// personaggio disegnato (stilizzato, nessuna persona reale)
function person(p,kind,col,r){r=r||110;const g=el('g',{filter:'url(#g_sh)'},p);
 const id='pc'+(++UID);const cp=el('clipPath',{id:id},g);el('circle',{r:r},cp);
 el('circle',{r:r,fill:'#0E5A60'},g);const f=el('g',{'clip-path':'url(#'+id+')'},g);
 const SK='#F1D9C4';
 el('path',{d:`M${-r*0.9} ${r} Q${-r*0.85} ${r*0.3} 0 ${r*0.26} Q${r*0.85} ${r*0.3} ${r*0.9} ${r} Z`,fill:col},f);
 el('rect',{x:-r*0.12,y:r*0.02,width:r*0.24,height:r*0.28,fill:SK},f);
 if(kind=='A')el('circle',{cx:0,cy:-r*0.6,r:r*0.19,fill:'#6B4A3A'},f);
 el('ellipse',{cx:0,cy:-r*0.18,rx:r*0.3,ry:r*0.35,fill:SK},f);
 if(kind=='A')el('path',{d:`M${-r*0.33} ${-r*0.1} Q${-r*0.38} ${-r*0.58} 0 ${-r*0.58} Q${r*0.38} ${-r*0.58} ${r*0.33} ${-r*0.1} Q${r*0.22} ${-r*0.42} 0 ${-r*0.42} Q${-r*0.22} ${-r*0.42} ${-r*0.33} ${-r*0.1} Z`,fill:'#6B4A3A'},f);
 if(kind=='L')el('path',{d:`M${-r*0.38} ${r*0.06} Q${-r*0.44} ${-r*0.62} 0 ${-r*0.58} Q${r*0.44} ${-r*0.62} ${r*0.38} ${r*0.06} L${r*0.27} ${r*0.06} Q${r*0.27} ${-r*0.38} 0 ${-r*0.38} Q${-r*0.27} ${-r*0.38} ${-r*0.27} ${r*0.06} Z`,fill:'#D5DBDE'},f);
 if(kind=='F'||kind=='M'){const hc=kind=='F'?'#C9D3D6':'#5B4A42';
  [-1,1].forEach(s=>el('path',{d:`M${s*r*0.31} ${-r*0.16} Q${s*r*0.34} ${-r*0.46} ${s*r*0.16} ${-r*0.5}`,fill:'none',stroke:hc,'stroke-width':r*0.1,'stroke-linecap':'round'},f));
  if(kind=='M')el('path',{d:`M${-r*0.28} ${-r*0.36} Q0 ${-r*0.66} ${r*0.28} ${-r*0.36} Q0 ${-r*0.5} ${-r*0.28} ${-r*0.36} Z`,fill:hc},f);}
 if(kind=='F'){[-1,1].forEach(s=>el('circle',{cx:s*r*0.13,cy:-r*0.2,r:r*0.09,fill:'none',stroke:INK,'stroke-width':r*0.035},f));el('line',{x1:-r*0.04,y1:-r*0.2,x2:r*0.04,y2:-r*0.2,stroke:INK,'stroke-width':r*0.035},f);}
 [-1,1].forEach(s=>el('circle',{cx:s*r*0.12,cy:-r*0.2,r:r*0.032,fill:INK},f));
 el('path',{d:`M${-r*0.1} ${-r*0.01} Q0 ${r*0.07} ${r*0.1} ${-r*0.01}`,fill:'none',stroke:INK,'stroke-width':r*0.032,'stroke-linecap':'round'},f);
 el('circle',{r:r,fill:'none',stroke:'#fff','stroke-width':r*0.07},g);el('circle',{r:r*1.08,fill:'none',stroke:col,'stroke-width':r*0.06},g);return g;}
const PCOL={F:'#2B8FA0',A:'#1B9F81',L:'#E39A1C',M:'#5C7C86'};
const RX=v=>-700+(v-7700)/600*1400;
const MESI='GFMAMGLASOND';
Object.assign(BUILD,{
 per:(g,kind,name,sub,r,subfill)=>{r=r||110;person(g,kind,PCOL[kind],r);if(name)lab(g,name,0,r+48,Math.min(40,r*0.42),DF_,'#fff');
  if(sub)lab(g,sub,0,r+48+Math.min(40,r*0.42)*1.9,30,subfill||GF_,subfill===AMB?'#5A3300':'#fff');},
 coin:(g,big,r,col,fs)=>{r=r||95;col=col||AMB;const b=el('g',{filter:'url(#g_sh2)'},g);el('circle',{r:r,fill:col,stroke:'#fff','stroke-width':8},b);
  el('circle',{r:r*0.8,fill:'none',stroke:'#fff','stroke-width':3,opacity:.6},b);txt(g,big,0,(fs||44)*0.36,fs||44,col===AMB?'#5A3300':'#fff','900');},
 ced:(g,title,rows,w)=>{w=w||600;const rh=78,h=118+rows.length*rh+24;const b=el('g',{filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:24,fill:'url(#g_paper)'},b);
  el('rect',{x:-w/2,y:-h/2,width:w,height:86,rx:24,fill:GRN},b);el('rect',{x:-w/2,y:-h/2+52,width:w,height:34,fill:GRN},b);
  txt(g,title,0,-h/2+56,32,'#fff','bold');
  rows.forEach((r,i)=>{const y=-h/2+112+i*rh+rh/2;if(i)el('line',{x1:-w/2+30,y1:y-rh/2,x2:w/2-30,y2:y-rh/2,stroke:'#C3D3D7','stroke-width':3,'stroke-dasharray':'8 8'},g);
   txt(g,r[0],-w/2+36,y+11,32,INK,'bold','start');txt(g,r[1],w/2-36,y+12,36,r[2]||INK,'900','end');});},
 rul:(g)=>{const W=1400;const id='rc'+(++UID);const cp=el('clipPath',{id:id},g);el('rect',{x:-W/2,y:-26,width:W,height:52,rx:26},cp);
  const z=el('g',{'clip-path':'url(#'+id+')'},g);const Z=(a,b,c)=>el('rect',{x:RX(a),y:-26,width:RX(b)-RX(a),height:52,fill:c},z);
  Z(7700,7954.05,'#2FD0A8');Z(7954.05,8108.99,AMB);Z(8108.99,8300,RED_);
  el('rect',{x:-W/2,y:-26,width:W,height:52,rx:26,fill:'none',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  [7954.05,8108.99].forEach(v=>el('line',{x1:RX(v),y1:-40,x2:RX(v),y2:126,stroke:'#fff','stroke-width':5,'stroke-dasharray':'10 8'},g));},
 mk:(g,s,col,h,fs)=>{h=h||130;fs=fs||32;col=col||AMB;el('line',{x1:0,y1:-26,x2:0,y2:-h+28,stroke:'#fff','stroke-width':5},g);
  el('circle',{cx:0,cy:-26,r:14,fill:col,stroke:'#fff','stroke-width':5},g);lab(g,s,0,-h,fs,col,col===AMB?'#5A3300':'#fff');},
 sbar:(g,a,b,ok,la,lb)=>{const W=1400,M=26000;const X=v=>-W/2+v/M*W;const lim=23862.15;
  el('rect',{x:-W/2,y:-42,width:W,height:84,rx:22,fill:'#06303A',stroke:LT,'stroke-width':3},g);
  el('rect',{x:X(0)+8,y:-32,width:X(a)-X(0)-8,height:64,rx:16,fill:AMB},g);
  el('rect',{x:X(a)+4,y:-32,width:X(a+b)-X(a)-4,height:64,rx:16,fill:ok?'#2FD0A8':RED_},g);
  txt(g,la,(X(0)+X(a))/2,11,30,'#5A3300','900');txt(g,lb,(X(a)+X(a+b))/2,11,30,ok?'#06303A':'#fff','900');
  el('line',{x1:X(lim),y1:-74,x2:X(lim),y2:74,stroke:'#fff','stroke-width':6,'stroke-dasharray':'14 10'},g);
  lab(g,'LIMITE DI COPPIA 23.862,15 €',X(lim)-250,-112,30,DF_,'#fff');
  lab(g,'TOTALE '+(a+b).toLocaleString('it-IT',{minimumFractionDigits:0,maximumFractionDigits:0})+' €',X(lim)-250,112,32,ok?GF_:RF_,'#fff');},
 mon:(g,ranges,W,fs)=>{W=W||1320;fs=fs||38;const cw=W/12;
  for(let i=0;i<12;i++){const x=-W/2+i*cw;let col=null;ranges.forEach(r=>{if(i>=r[0]&&i<=r[1])col=r[2];});
   el('rect',{x:x+4,y:-40,width:cw-8,height:80,rx:14,fill:col||'#0A3F45',stroke:col?'#fff':'#2B6F77','stroke-width':3},g);
   txt(g,MESI[i],x+cw/2,fs*0.36,fs,col?(col===AMB?'#5A3300':'#fff'):'#7FA8AE','900');}
  ranges.forEach(r=>{if(r[3])lab(g,r[3],-W/2+(r[0]+r[1]+1)*cw/2,-92,30,r[2],r[2]===AMB?'#5A3300':'#fff');});},
 qtab:(g)=>{const W=1500,c0=440,c1=(W-c0)/2,rh=92,H=rh*4;el('rect',{x:-W/2,y:-H/2,width:W,height:H,rx:24,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  el('rect',{x:-W/2,y:-H/2,width:W,height:rh,rx:24,fill:GRN},g);el('rect',{x:-W/2,y:-H/2+rh-30,width:W,height:30,fill:GRN},g);
  const hx=[-W/2+c0/2,-W/2+c0+c1/2,-W/2+c0+c1*1.5];
  txt(g,'ANNI DI CONTRIBUTI',hx[0],-H/2+58,28,'#fff','bold');txt(g,'REDDITO FINO A 11.931 €',hx[1],-H/2+58,28,'#fff','bold');txt(g,'DA 11.931 A 15.908 €',hx[2],-H/2+58,28,'#fff','bold');
  el('line',{x1:-W/2+c0,y1:-H/2+rh,x2:-W/2+c0,y2:H/2-16,stroke:'#C3D3D7','stroke-width':3},g);el('line',{x1:-W/2+c0+c1,y1:-H/2+rh,x2:-W/2+c0+c1,y2:H/2-16,stroke:'#C3D3D7','stroke-width':3},g);
  ['FINO A 15','DA 15 A 25','OLTRE 25'].forEach((s,i)=>{const y=-H/2+rh*(i+1)+rh/2;if(i)el('line',{x1:-W/2+20,y1:y-rh/2,x2:W/2-20,y2:y-rh/2,stroke:'#C3D3D7','stroke-width':3},g);txt(g,s,hx[0],y+11,32,INK,'bold');});},
 tv:(g,s,col,fs)=>txt(g,s,0,(fs||46)*0.36,fs||46,col||GRN,'900'),
 ghead:(g)=>{const W=1500;el('rect',{x:-W/2,y:-44,width:W,height:88,rx:22,fill:GRN,filter:'url(#g_sh2)'},g);
  [['VICINO',-W/2+190],['TREDICESIMA',-W/2+560],['BONUS 154,94 €',-W/2+900],['QUATTORDICESIMA',-W/2+1260]].forEach(([s,x])=>txt(g,s,x,11,30,'#fff','bold'));},
 grow:(g,kind,name,cells)=>{const W=1500;el('rect',{x:-W/2,y:-56,width:W,height:112,rx:22,fill:'url(#g_paper)',filter:'url(#g_sh2)'},g);
  const pg=el('g',{transform:'translate('+(-W/2+90)+' 0)'},g);person(pg,kind,PCOL[kind],42);txt(g,name,-W/2+150,12,34,INK,'900','start');
  [-W/2+560,-W/2+900,-W/2+1260].forEach((x,i)=>{const c=cells[i];
   if(c=='si'){el('circle',{cx:x,cy:0,r:30,fill:'#1B9F81'},g);el('path',{d:`M${x-15} 1 l10 11 l20 -22`,fill:'none',stroke:'#fff','stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'},g);}
   else if(c=='no'){el('circle',{cx:x,cy:0,r:30,fill:RED_},g);el('path',{d:`M${x-12} -12 l24 24 M${x+12} -12 l-24 24`,stroke:'#fff','stroke-width':8,'stroke-linecap':'round'},g);}
   else lab(g,c,x,0,30,AMB,'#5A3300');});},
 phone:(g,rows)=>{const w=380,h=640;const b=el('g',{filter:'url(#g_sh)'},g);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:48,fill:'#06303A',stroke:'#fff','stroke-width':6},b);
  el('rect',{x:-w/2+18,y:-h/2+60,width:w-36,height:h-120,rx:18,fill:'url(#g_paper)'},b);el('rect',{x:-40,y:-h/2+24,width:80,height:12,rx:6,fill:'#2B6F77'},b);
  el('rect',{x:-w/2+18,y:-h/2+60,width:w-36,height:86,rx:18,fill:GRN},b);el('rect',{x:-w/2+18,y:-h/2+120,width:w-36,height:26,fill:GRN},b);
  txt(g,'MY INPS',0,-h/2+114,34,'#fff','900');txt(g,'CEDOLINO DI DICEMBRE',0,-h/2+190,24,INK,'bold');
  rows.forEach((r,i)=>{const y=-h/2+250+i*84;el('rect',{x:-w/2+38,y:y-30,width:w-76,height:62,rx:14,fill:'#D6F5EC',stroke:'#1B9F81','stroke-width':3},g);txt(g,r,-w/2+58,y+10,26,INK,'bold','start');});},
 stp:(g,n,s1,s2,w)=>{w=w||330;const h=250;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  circN(g,40,n,'url(#g_badge)').setAttribute('transform','translate(0 '+(-h/2)+')');
  txt(g,s1,0,10,32,INK,'900');if(s2)txt(g,s2,0,56,28,GRN,'bold');},
 lim:(g,title,two,val,sub)=>{const w=640,h=470;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:28,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2,y:-h/2,width:w,height:84,rx:28,fill:GRN},g);el('rect',{x:-w/2,y:-h/2+54,width:w,height:30,fill:GRN},g);txt(g,title,0,-h/2+56,34,'#fff','bold');
  if(two){const a=el('g',{transform:'translate(-70 -55)'},g);person(a,'A',PCOL.A,70);const m=el('g',{transform:'translate(70 -55)'},g);person(m,'M',PCOL.M,70);}
  else{const a=el('g',{transform:'translate(0 -55)'},g);person(a,'A',PCOL.A,70);}
  txt(g,val,0,100,64,INK,'900');txt(g,sub,0,158,28,GRN,'bold');},
 crowd:(g,cols,rowsN,col)=>{const b=el('g',{},g);for(let r=0;r<rowsN;r++)for(let c=0;c<cols;c++){const x=(c-(cols-1)/2)*58,y=(r-(rowsN-1)/2)*70;
   el('circle',{cx:x,cy:y-18,r:14,fill:col||LT,opacity:.9},b);el('path',{d:`M${x-22} ${y+24} Q${x-22} ${y-2} ${x} ${y-2} Q${x+22} ${y-2} ${x+22} ${y+24} Z`,fill:col||LT,opacity:.9},b);}},
 vid:(g,s1,s2)=>{const w=480,h=290;const b=el('g',{filter:'url(#g_sh)'},g);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:24,fill:'#06303A',stroke:'#fff','stroke-width':6},b);
  el('rect',{x:-w/2+20,y:h/2-34,width:w-40,height:10,rx:5,fill:'#2B6F77'},b);el('rect',{x:-w/2+20,y:h/2-34,width:(w-40)*0.62,height:10,rx:5,fill:RED_},b);
  el('circle',{cx:0,cy:-30,r:56,fill:RED_,stroke:'#fff','stroke-width':5},b);el('path',{d:'M-16 -58 L30 -30 L-16 -2 Z',fill:'#fff'},b);
  txt(g,s1,0,72,34,'#fff','900');if(s2)txt(g,s2,0,108,24,LT,'bold');},
 tax2:(g)=>{const base=0;el('rect',{x:-330,y:0,width:660,height:8,rx:4,fill:LT},g);
  el('rect',{x:-230,y:-150,width:170,height:150,rx:16,fill:'#2B6F77',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  el('rect',{x:60,y:-290,width:170,height:290,rx:16,fill:'url(#g_red)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  txt(g,'TASSE',-145,-170,28,LT,'bold');txt(g,'TASSE',145,-310,28,'#FFB4A6','bold');
  lab(g,'RATA NORMALE',-145,60,30,DF_,'#fff');lab(g,'TREDICESIMA',145,60,30,DF_,'#fff');},
 posta:(g,label)=>{const w=270,h=270;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  const ig=el('g',{transform:'translate(0 -32)'},g);el('rect',{x:-90,y:-60,width:180,height:120,rx:12,fill:AMB,stroke:INK,'stroke-width':6},ig);
  el('path',{d:'M-90 -56 L0 10 L90 -56',fill:'none',stroke:INK,'stroke-width':6},ig);lab(g,label,0,h/2-46,32,DF_,'#fff');},
});
const GN=(s,x,y,at,col,fs)=>I('tv',[s,col,fs],x,y,at);
