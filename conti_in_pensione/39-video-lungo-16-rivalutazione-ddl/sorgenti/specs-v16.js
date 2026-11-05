// ===== VIDEO 16 (rivalutazione 2027, articolo 55) - look nuovo (N.37, N.47, N.50) =====
// Diverso dai video 13-15, stessi colori del canale: titoletto con scalino dorato + indicatore a sei scalini (nessun numero di blocco),
// didascalia a pannello con angoli tagliati e linguetta dorata, schede a "foglio" con fascia colorata e angolo piegato,
// documento parlamentare di carta, cedolino con bordo seghettato, biglietti con tacche, scalinata in prospettiva, calcolatrice, calendario.
const GOLD16='#F2B33D',RED16='#C8372A',INK16='#10343B',MUTE16='#5C7479',GRN16='#1B9F81',SER16='DejaVu Serif, Liberation Serif, Georgia, serif';
(function(){const d=document.querySelector('defs');
 const mk=(id,stops)=>{const lg=el('linearGradient',{id:id,x1:0,y1:0,x2:0,y2:1},d);stops.forEach(([o,c,op])=>el('stop',{offset:o,'stop-color':c,'stop-opacity':op===undefined?1:op},lg));};
 mk('g16_paper',[[0,'#FFFEF8'],[1,'#E9E4D3']]);mk('g16_front',[[0,'#fff',0.30],[1,'#000',0.20]]);
 mk('g16_amb',[[0,'#FFD36B'],[1,'#E0A02A']]);mk('g16_grn',[[0,'#3FD1AB'],[1,'#17846C']]);
 mk('g16_dk',[[0,'#1F5B68'],[1,'#0A2E36']]);mk('g16_red',[[0,'#E8604C'],[1,'#B72B1E']]);})();
const IO=(...a)=>Object.assign(I(...a),{ov:true});
function sub16(g){return el('g',{},g);}
function fitS(p,s,x,yc,fs,fill,weight,maxW,anchor){const t=txt(p,s,x,yc+fs*0.36,fs,fill,weight||'bold',anchor);t.setAttribute('font-family',SER16);
 if(maxW){const w=mw(t,s,fs);if(w>maxW){const f2=fs*maxW/w;t.setAttribute('font-size',f2.toFixed(1));t.setAttribute('y',(yc+f2*0.36).toFixed(1));}}return t;}
// ---------- titoletto e didascalia ----------
const HI16={7:6,8:6,9:5,10:4,11:3,12:2,13:2,14:1,15:99};
function miniSt(g,hi){const w=26,h=11;for(let i=0;i<6;i++){const on=(hi===i+1)||hi===99;
 el('rect',{x:i*(w+5),y:-(i+1)*h,width:w,height:(i+1)*h,rx:3,fill:on?GOLD16:'#0A3F45',stroke:on?'#fff':'#7FF0D2','stroke-width':on?3:2,'stroke-opacity':on?1:.6},g);}}
function topLabel(g,s){const t=el('g',{},g);
 el('rect',{x:100,y:62,width:64,height:64,rx:14,fill:'url(#g16_amb)',stroke:'#fff','stroke-width':3},t);
 el('polygon',{points:'110,116 110,102 124,102 124,90 138,90 138,78 152,78 152,116',fill:INK16},t);
 const x=fitT(t,s,190,94,38,'#BFFBEA','bold',1150,'start');x.setAttribute('letter-spacing','6');
 el('rect',{x:100,y:146,width:1720,height:2,fill:'#7FF0D2',opacity:.25},t);el('rect',{x:100,y:145,width:200,height:4,fill:GOLD16},t);
 const ind=el('g',{transform:'translate(1639 134)'},t);miniSt(ind,HI16[N]||-1);return t;}
function cap(g,s,size){size=size||40;const c=el('g',{},g);if(!s)return c;
 const t=txt(c,s,0,0,size,'#FFFFFF','bold');let tl=mw(t,s,size);
 const maxT=1500;if(tl>maxT){size=size*maxT/tl;t.setAttribute('font-size',size.toFixed(1));tl=mw(t,s,size);}
 const padL=150,padR=60+tl*0.03;const w=tl+padL+padR,h=108,k=24;
 t.setAttribute('x',(-w/2+padL+tl/2).toFixed(1));t.setAttribute('y',(size*0.36).toFixed(1));
 const ins=e=>{c.insertBefore(e,t);return e;};
 ins(el('path',{d:`M${-w/2+k} ${-h/2} H${w/2} V${h/2-k} L${w/2-k} ${h/2} H${-w/2} V${-h/2+k} Z`,fill:'#062830',filter:'url(#g_sh2)'}));
 ins(el('path',{d:`M${-w/2+k} ${-h/2+2} H${w/2-2}`,fill:'none',stroke:GOLD16,'stroke-width':4}));
 const tab=el('g',{},c);c.insertBefore(tab,t);
 el('path',{d:`M${-w/2+k} ${-h/2} H${-w/2+118} V${h/2} H${-w/2} V${-h/2+k} Z`,fill:'url(#g16_amb)'},tab);
 const ig=el('g',{transform:'translate('+(-w/2+62)+' 0)'},tab);ico(ig,'doc',1.15,INK16);
 return c;}
// ---------- elementi ----------
function card16(g,w,h,icon,lines,o){o=o||{};const k=26,bw=o.bw||Math.min(120,h*0.85);
 el('path',{d:`M${-w/2} ${-h/2} H${w/2-k} L${w/2} ${-h/2+k} V${h/2} H${-w/2} Z`,fill:'url(#g16_paper)',filter:'url(#g_sh2)'},g);
 const dec=sub16(g);el('path',{d:`M${w/2-k} ${-h/2} V${-h/2+k} H${w/2} Z`,fill:'#BDB6A0'},dec);
 el('rect',{x:-w/2,y:-h/2,width:bw,height:h,fill:o.band||GRN16},dec);
 el('rect',{x:-w/2+bw-6,y:-h/2,width:6,height:h,fill:'#000',opacity:.12},dec);
 const ig=el('g',{transform:'translate('+(-w/2+bw/2)+' 0)'},dec);el('circle',{r:bw*0.34,fill:'#fff'},ig);ico(ig,icon,bw*0.34/50,o.band||GRN16);
 const x0=-w/2+bw+28,x1=w/2-Math.max(44,0.045*w);const n=lines.length;const lh=o.lh||(lines[0][1]*1.35);
 lines.forEach((L,i)=>fitT(g,L[0],x0,(i-(n-1)/2)*lh,L[1],L[2]||INK16,L[3]||'900',x1-x0,'start'));return g;}
function tag16(g,s,fs,fill,col,icon,o){o=o||{};fs=fs||32;const t=txt(g,s,0,fs*0.36,fs,col||'#fff','bold');const tl=mw(t,s,fs);
 const h=o.h||fs*1.9;const padL=icon?(h*1.0+fs*0.45):fs*1.1;const padR=fs*0.9+(tl+padL)*0.04;const w=Math.max(o.minw||0,tl+padL+padR);const k=h*0.26;
 t.setAttribute('x',(-w/2+padL+(w-padL-padR)/2).toFixed(1));
 const r=el('path',{d:`M${-w/2+k} ${-h/2} H${w/2-10} Q${w/2} ${-h/2} ${w/2} ${-h/2+10} V${h/2-10} Q${w/2} ${h/2} ${w/2-10} ${h/2} H${-w/2+k} L${-w/2} 0 Z`,fill:fill,stroke:o.stroke||'#fff','stroke-width':3,'stroke-linejoin':'round',filter:'url(#g_sh3)'});g.insertBefore(r,t);
 if(icon){const ig=el('g',{transform:'translate('+(-w/2+h*0.62)+' 0)'},g);el('circle',{r:h*0.36,fill:o.ibg||'#fff'},ig);ico(ig,icon,h*0.36/50,o.icol||INK16);}
 g.__w=w;return g;}
function ticket16(g,o){const w=o.w||380,h=o.h||240,r=16,nr=15,ny=-h/2+h*0.30;const col=o.col||GRN16;
 el('path',{d:`M${-w/2+r} ${-h/2} H${w/2-r} A${r} ${r} 0 0 1 ${w/2} ${-h/2+r} V${ny-nr} A${nr} ${nr} 0 0 0 ${w/2} ${ny+nr} V${h/2-r} A${r} ${r} 0 0 1 ${w/2-r} ${h/2} H${-w/2+r} A${r} ${r} 0 0 1 ${-w/2} ${h/2-r} V${ny+nr} A${nr} ${nr} 0 0 0 ${-w/2} ${ny-nr} V${-h/2+r} A${r} ${r} 0 0 1 ${-w/2+r} ${-h/2} Z`,fill:'url(#g16_paper)',filter:'url(#g_sh2)'},g);
 const dec=sub16(g);el('path',{d:`M${-w/2+nr+6} ${ny} H${w/2-nr-6}`,stroke:'#B9B29C','stroke-width':3,'stroke-dasharray':'8 7',fill:'none'},dec);
 el('rect',{x:-w/2+6,y:-h/2+6,width:8,height:ny-nr-10,rx:4,fill:col},dec);
 fitT(g,o.title,10,(-h/2+ny)/2-2,o.tfs||26,col,'900',w-90);
 const fsv=o.fs||72;fitT(g,o.val,0,ny+(h/2-ny)*0.36,fsv,INK16,'900',w-70);
 if(o.sub)fitT(g,o.sub,0,h/2-28,o.sfs||26,MUTE16,'bold',w-70);return g;}
function stamp16(g,s,w,h,col){col=col||RED16;
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:10,fill:'rgba(255,255,255,0.88)',stroke:col,'stroke-width':8,filter:'url(#g_sh2)'},g);
 const dec=sub16(g);el('rect',{x:-w/2+10,y:-h/2+10,width:w-20,height:h-20,rx:5,fill:'none',stroke:col,'stroke-width':2.5},dec);
 fitT(g,s,0,0,34,col,'900',w*0.84);return g;}
function cover16(g,w){const h=w*1.34,x0=-w/2,y0=-h/2;
 const pile=sub16(g);[[9,10,2.2],[-6,5,-1.8]].forEach(([dx,dy,r])=>el('rect',{x:x0+dx,y:y0+dy,width:w,height:h,rx:8,fill:'#D6D0BC',transform:`rotate(${r})`,filter:'url(#g_sh3)'},pile));
 el('rect',{x:x0,y:y0,width:w,height:h,rx:8,fill:'url(#g16_paper)',filter:'url(#g_sh)'},g);
 const dec=sub16(g);el('path',{d:`M${x0} ${y0+70} V${y0+8} Q${x0} ${y0} ${x0+8} ${y0} H${-x0-8} Q${-x0} ${y0} ${-x0} ${y0+8} V${y0+70} Z`,fill:'url(#g16_dk)'},dec);
 el('rect',{x:x0,y:y0+66,width:w,height:5,fill:GOLD16},dec);
 el('circle',{cx:0,cy:y0+140,r:38,fill:'none',stroke:INK16,'stroke-width':4},dec);el('circle',{cx:0,cy:y0+140,r:28,fill:INK16},dec);
 for(let i=0;i<5;i++){const a=-Math.PI/2+i*2*Math.PI/5;el('circle',{cx:20*Math.cos(a),cy:y0+140+20*Math.sin(a),r:4.5,fill:GOLD16},dec);}
 el('rect',{x:x0+34,y:y0+250,width:w-68,height:3,fill:INK16},dec);el('rect',{x:x0+34,y:y0+257,width:w-68,height:1.5,fill:INK16},dec);
 el('rect',{x:x0,y:-y0-26,width:w,height:26,rx:0,fill:'url(#g16_dk)'},dec);
 const t1=fitT(g,'ATTI PARLAMENTARI',0,y0+36,28,'#fff','bold',w*0.82);t1.setAttribute('letter-spacing','4');
 fitS(g,'CAMERA DEI DEPUTATI',0,y0+216,29,INK16,'bold',w*0.84);
 fitS(g,'N. 3174',0,y0+322,92,INK16,'bold',w*0.7);
 const t2=fitT(g,'DISEGNO DI LEGGE',0,y0+385,26,'#8A6A1E','bold',w*0.8);t2.setAttribute('letter-spacing','3');
 ['Bilancio di previsione','dello Stato per l\'anno','finanziario 2027'].forEach((l,i)=>fitS(g,l,0,y0+436+i*40,27,INK16,'bold',w*0.84));
 return g;}
function art55(g,w){const h=w*1.18,x0=-w/2,y0=-h/2;
 const pile=sub16(g);el('rect',{x:x0+8,y:y0+9,width:w,height:h,rx:8,fill:'#D6D0BC',transform:'rotate(1.6)',filter:'url(#g_sh3)'},pile);
 el('rect',{x:x0,y:y0,width:w,height:h,rx:8,fill:'url(#g16_paper)',filter:'url(#g_sh)'},g);
 const dec=sub16(g);el('rect',{x:x0+22,y:y0,width:3,height:h,fill:RED16,opacity:.55},dec);
 fitS(g,'Art. 55.',x0+46,y0+64,48,INK16,'bold',w*0.5,'start');
 ['(Modifiche alla disciplina in materia di','rivalutazione automatica dei trattamenti','pensionistici)'].forEach((l,i)=>{const t=fitS(g,l,x0+46,y0+118+i*28,19,MUTE16,'normal',w-90,'start');t.setAttribute('font-style','italic');});
 el('rect',{x:x0+40,y:y0+236,width:w-80,height:58,rx:6,fill:GOLD16,opacity:.35},dec);
 const L=[0.95,0.9,0.97,0.86,0.93,0.55,0.95,0.9,0.96,0.8,0.92,0.4];
 L.forEach((f,i)=>{if(i>=Math.floor((h-226)/42))return;el('rect',{x:x0+46,y:y0+196+i*42,width:(w-92)*f,height:12,rx:6,fill:'#B5B9B0'},dec);});
 return g;}
function stairs16(g,o){const n=o.n||6,W=o.W||620,H=o.H||380,dx=o.dx||46,dy=o.dy||-34,sw=W/n,hs=H/n;const hi=o.hi||[];const lab=o.labels||[];
 const ox=-(W+dx)/2,by=(H+Math.abs(dy))/2;
 el('ellipse',{cx:0,cy:by+6,rx:(W+dx)/2+16,ry:16,fill:'#021A1F',opacity:.4},sub16(g));
 for(let i=0;i<n;i++){const on=hi.includes(i+1);const x0=ox+i*sw,y0=by-(i+1)*hs;
  const c=on?['#F0B63C','#FFE08A','#B9801A']:(o.dim?['#2A7C86','#4DA7B0','#17535B']:['#2FB594','#76E3C5','#1B7F69']);
  el('polygon',{points:`${x0+sw},${y0} ${x0+sw+dx},${y0+dy} ${x0+sw+dx},${by+dy} ${x0+sw},${by}`,fill:c[2]},g);
  el('rect',{x:x0,y:y0,width:sw,height:by-y0,fill:c[0]},g);el('rect',{x:x0,y:y0,width:sw,height:by-y0,fill:'url(#g16_front)'},g);
  el('polygon',{points:`${x0},${y0} ${x0+sw},${y0} ${x0+sw+dx},${y0+dy} ${x0+dx},${y0+dy}`,fill:c[1]},g);
  el('path',{d:`M${x0} ${y0} H${x0+sw} L${x0+sw+dx} ${y0+dy}`,fill:'none',stroke:'#fff','stroke-width':2.5,'stroke-opacity':.7},g);
  if(lab[i])fitT(g,lab[i],x0+sw/2,y0+Math.min(hs*0.5,48),Math.min(34,sw*0.34),on?'#4A2E00':'#fff','900',sw-16);}
 return g;}
function cal16(g){const w=400,h=470,x0=-w/2,y0=-h/2;
 el('rect',{x:x0,y:y0,width:w,height:h,rx:22,fill:'url(#g16_paper)',filter:'url(#g_sh)'},g);
 const dec=sub16(g);el('path',{d:`M${x0} ${y0+110} V${y0+22} Q${x0} ${y0} ${x0+22} ${y0} H${-x0-22} Q${-x0} ${y0} ${-x0} ${y0+22} V${y0+110} Z`,fill:'url(#g16_grn)'},dec);
 metalRing(dec,-110,y0-30,34,62);metalRing(dec,110,y0-30,34,62);
 fitT(g,'GENNAIO',0,y0+66,50,'#fff','900',w*0.7);
 'LMMGVSD'.split('').forEach((c,i)=>fitT(g,c,x0+40+i*53,y0+150,24,MUTE16,'bold',30));
 for(let d=1;d<=31;d++){const idx=d-1+4;const c=idx%7,r=Math.floor(idx/7);const cx=x0+40+c*53,cy=y0+206+r*52;
  if(d===1)el('circle',{cx:cx,cy:cy,r:23,fill:GOLD16,stroke:'#fff','stroke-width':3},g);
  fitT(g,String(d),cx,cy,24,d===1?INK16:(c===6?RED16:INK16),'bold',34);}
 return g;}
function cedolino16(g,o){const w=o.w||520,h=o.h||300,x0=-w/2,y0=-h/2,k=14,hdr=o.hdr||60;const rows=o.rows||[];
 let d=`M${x0} ${y0+12} Q${x0} ${y0} ${x0+12} ${y0} H${-x0-12} Q${-x0} ${y0} ${-x0} ${y0+12} V${-y0-k}`;const n=Math.round(w/26),st=w/n;
 for(let i=0;i<n;i++){const xa=-x0-i*st;d+=` L${xa-st/2} ${-y0} L${xa-st} ${-y0-k}`;}d+=' Z';
 el('path',{d:d,fill:'url(#g16_paper)',filter:'url(#g_sh2)'},g);
 const dec=sub16(g);el('path',{d:`M${x0} ${y0+hdr} V${y0+12} Q${x0} ${y0} ${x0+12} ${y0} H${-x0-12} Q${-x0} ${y0} ${-x0} ${y0+12} V${y0+hdr} Z`,fill:'url(#g16_dk)'},dec);
 el('circle',{cx:-x0-38,cy:y0+hdr/2,r:15,fill:GOLD16},dec);
 const tt=fitT(g,o.title||'CEDOLINO DI PENSIONE',x0+28,y0+hdr/2,o.tfs||27,'#fff','bold',w-130,'start');tt.setAttribute('letter-spacing','2');
 const avail=h-hdr-k-(o.bar?40:14);const rh=o.rh||avail/rows.length;
 rows.forEach((r,i)=>{const yc=y0+hdr+8+(i+0.5)*rh-2;
  if(r[2])el('rect',{x:x0+14,y:yc-rh/2+3,width:w-28,height:rh-6,rx:10,fill:'#FFEEBF',stroke:GOLD16,'stroke-width':3},g);
  else el('rect',{x:x0+28,y:yc+rh/2-2,width:w-56,height:2,fill:'#CFC9B4'},dec);
  fitT(g,r[0],x0+36,yc,o.lfs||25,MUTE16,'bold',w*0.5,'start');fitT(g,r[1],-x0-36,yc,o.vfs||33,INK16,'900',w*0.4,'end');});
 if(o.bar){for(let i=0;i<46;i++)el('rect',{x:x0+34+i*((w-68)/46),y:-y0-k-30,width:(i%3?2:4),height:18,fill:'#6B7C80'},dec);}
 return g;}
function calc16(g){const w=380,h=560,x0=-w/2,y0=-h/2;
 el('rect',{x:x0,y:y0,width:w,height:h,rx:34,fill:'url(#g16_dk)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh)'},g);
 const dec=sub16(g);el('rect',{x:x0+8,y:y0+8,width:w-16,height:h/2,rx:28,fill:'#fff',opacity:.05},dec);
 el('rect',{x:x0+26,y:y0+30,width:w-52,height:150,rx:14,fill:'#CFE9DC',stroke:'#0A2E36','stroke-width':4},g);
 fitT(g,'111 € × 13 RATE',x0+44,y0+75,29,MUTE16,'bold',w-90,'start');
 fitT(g,'≈ 1.448 €',x0+w-44,y0+135,58,INK16,'900',w-100,'end');
 const K=[['7','8','9','÷'],['4','5','6','×'],['1','2','3','−'],['0',',','=','+']];
 K.forEach((r,ri)=>r.forEach((c,ci)=>{const kx=x0+26+ci*86,ky=y0+215+ri*82;const am=(c==='=');
  el('rect',{x:kx,y:ky,width:76,height:68,rx:14,fill:am?'url(#g16_amb)':(ci===3?'#2B6F77':'#3E8C96'),stroke:'#fff','stroke-opacity':.5,'stroke-width':2},g);
  fitT(g,c,kx+38,ky+34,30,am?'#4A2E00':'#fff','900',40);}));
 return g;}
function btnSub16(g){const w=500,h=122;
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:h/2,fill:'url(#g16_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh)'},g);
 const b=el('g',{transform:'translate('+(-w/2+78)+' 0)'},g);
 el('path',{d:'M0 -34 Q-24 -34 -24 -8 V12 L-34 26 H34 L24 12 V-8 Q24 -34 0 -34 Z',fill:'#fff'},b);el('circle',{cx:0,cy:34,r:8,fill:'#fff'},b);el('circle',{cx:0,cy:-40,r:6,fill:'#fff'},b);
 fitT(g,'ISCRIVITI',50,0,58,'#fff','900',w-190);return g;}
function btnLike16(g){const w=440,h=122;
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:h/2,fill:'url(#g16_paper)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh)'},g);
 const b=el('g',{transform:'translate('+(-w/2+84)+' 0) scale(1.15)'},g);
 el('rect',{x:-40,y:-6,width:22,height:42,rx:4,fill:'#2B6F77'},b);
 el('path',{d:'M-12 -4 L6 -34 Q12 -42 20 -37 Q27 -32 22 -20 L18 -8 H36 Q44 -8 44 0 Q44 7 40 9 Q44 13 42 19 Q41 25 36 27 Q38 32 34 36 Q30 39 24 39 H-12 Z',fill:'#1B9F81'},b);
 fitT(g,'MI PIACE',56,0,54,INK16,'900',w-200);return g;}
function meter16(g){const W=760,H=54;
 fitT(g,'QUANTA PARTE DELL\'AUMENTO ARRIVA',0,-74,34,'#fff','900',W+40);
 const dec=el('g',{},g);el('rect',{x:-W/2,y:-H/2,width:W,height:H,rx:H/2,fill:'#062830',stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},dec);
 el('rect',{x:-W/2+4,y:-H/2+4,width:W*0.55,height:H-8,rx:(H-8)/2,fill:'url(#g16_amb)'},dec);
 for(let i=1;i<10;i++)el('rect',{x:-W/2+i*W/10-1,y:H/2-14,width:2,height:10,fill:'#fff',opacity:.5},dec);
 fitT(g,'A SECONDA DELL\'IMPORTO',0,74,30,'#BFFBEA','bold',W);return g;}
function ruler16(g){const W=820,H=96;
 const dec=sub16(g);el('rect',{x:-W/2,y:-H/2,width:W,height:H,rx:10,fill:'#F3E3A6',stroke:'#C9A94A','stroke-width':3,filter:'url(#g_sh2)'},dec);
 el('rect',{x:-W/2,y:-H/2,width:W/10,height:H,rx:10,fill:GOLD16,opacity:.8},dec);
 for(let i=0;i<=10;i++){const x=-W/2+i*W/10;el('rect',{x:x-1.5,y:-H/2,width:3,height:34,fill:'#6B5A22'},dec);for(let j=1;j<5&&i<10;j++)el('rect',{x:x+j*W/50-1,y:-H/2,width:2,height:j===2?22:14,fill:'#6B5A22'},dec);}
 for(let i=1;i<=10;i++)fitT(g,String(i),-W/2+(i-0.5)*W/10,22,28,'#4A3C10','900',50);
 fitT(g,'MULTIPLI DEL TRATTAMENTO MINIMO',0,-H/2-34,32,'#fff','900',W);return g;}
function bars16(g){const W=900,H=300;
 el('rect',{x:-W/2,y:H/2,width:W,height:8,rx:4,fill:'#fff'},sub16(g));
 const hs=[50,95,150,215,300];hs.forEach((v,i)=>{const x=-W/2+60+i*172,last=i===4;
  el('rect',{x:x,y:H/2-v,width:120,height:v,rx:12,fill:last?'url(#g16_amb)':'#2B8E99',stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},g);});
 fitT(g,'≈ 1.448 €',-W/2+60+4*172-70,H/2-300-36,38,GOLD16,'900',300);
 fitT(g,'PIÙ SALE LA PENSIONE  →',0,H/2+52,32,'#BFFBEA','bold',W);return g;}
function timeline16(g){const W=1400;
 const dec=sub16(g);el('rect',{x:-W/2,y:-7,width:W,height:14,rx:7,fill:'#062830',stroke:'#7FF0D2','stroke-width':3,filter:'url(#g_sh2)'},dec);
 [[-W/2+110,'2023'],[0,'2024'],[W/2-110,'2025']].forEach(([x,l],i)=>{el('circle',{cx:x,cy:0,r:22,fill:i===1?'url(#g16_amb)':'url(#g16_grn)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},g);fitT(g,l,x,-62,56,'#fff','900',200);});return g;}
function watch16(g){el('rect',{x:-350,y:-240,width:700,height:480,rx:24,fill:'rgba(2,26,31,0.22)',stroke:'#BFFBEA','stroke-width':5,'stroke-dasharray':'22 14'},g);
 const t=fitT(g,'WATCH NEXT',0,310,56,'#FFFFFF','900',640);t.setAttribute('letter-spacing','6');return g;}
function dbox16(g,w,h,lines){el('path',{d:`M${-w/2+24} ${-h/2} H${w/2} V${h/2-24} L${w/2-24} ${h/2} H${-w/2} V${-h/2+24} Z`,fill:'#062830',stroke:'#7FF0D2','stroke-width':3,filter:'url(#g_sh2)'},g);
 const n=lines.length;lines.forEach((L,i)=>fitT(g,L[0],0,(i-(n-1)/2)*(L[1]*1.5),L[1],L[2],'bold',w*0.9));return g;}
Object.assign(BUILD,{
 card16:(g,...a)=>card16(g,...a),tag16:(g,...a)=>tag16(g,...a),ticket16:(g,o)=>ticket16(g,o),stamp16:(g,...a)=>stamp16(g,...a),
 cover16:(g,w)=>cover16(g,w),art55:(g,w)=>art55(g,w),stairs16:(g,o)=>stairs16(g,o),cal16:(g)=>cal16(g),cedo16:(g,o)=>cedolino16(g,o),
 calc16:(g)=>calc16(g),sub16:(g)=>btnSub16(g),like16:(g)=>btnLike16(g),meter16:(g)=>meter16(g),ruler16:(g)=>ruler16(g),bars16:(g)=>bars16(g),
 tl16:(g)=>timeline16(g),watch16:(g)=>watch16(g),dbox16:(g,w,h,l)=>dbox16(g,w,h,l),mag16:(g)=>magnifier(g),
 op16:(g,s)=>{el('circle',{r:34,fill:'#fff',stroke:GOLD16,'stroke-width':6,filter:'url(#g_sh2)'},g);txt(g,s,0,14,44,INK16,'900');},
});
// ---------- mkBlk con movimento vivo degli elementi (lento, fermo solo alla fine) ----------
function mkBlk(text,dur,scenes){const sp=speech(text,dur);
 const st=scenes.map((sc,i)=>i==0?0:Math.max(0.8,sp(sc.at)-0.3+(sc.sh||0)));
 scenes.forEach((sc,i)=>{const s=st[i],e=(i<scenes.length-1)?st[i+1]:dur;const L=e-s;
  const D=0.9;sc._D=D;sc._L=L;
  if(L<5.0)throw new Error('REGOLA N.18: scena troppo corta ('+L.toFixed(1)+' s, minimo 5 s)');
  const A0=0.5;
  sc.items.forEach(it=>{it._raw=Math.max(A0,sp(it.at)-0.2-s);});
  const lim=Math.max(A0+0.05,Math.min(0.8*L-D,L-0.8-D));const amax=Math.max(...sc.items.map(it=>it._raw));
  const k=(amax>lim)?(lim-A0)/Math.max(0.01,amax-A0):1;
  sc.items.forEach(it=>{it._a=A0+(it._raw-A0)*k;});
  {const ord=[...sc.items].sort((x,y)=>x._a-y._a);const n=ord.length;const gap=n>1?Math.min(0.45,(lim-A0)/(n-1)):0;
   for(let q=1;q<n;q++){ord[q]._a=Math.max(ord[q]._a,ord[q-1]._a+gap);}
   const mx=Math.max(...ord.map(o=>o._a));if(mx>lim&&n>1){const kk=(lim-A0)/(mx-A0);ord.forEach(o=>{o._a=A0+(o._a-A0)*kk;});}}
  SB.push({s,e,build(g){const o={items:[]};
   o.top=el('g',{},g);topLabel(o.top,sc.top);
   o.cap=el('g',{},g);if(sc.cap)cap(o.cap,sc.cap,sc.capSize||40);
   sc.items.forEach(it=>{const n=el('g',{},g);BUILD[it.k](n,...it.a);o.items.push({n,it});});
   this.o=o;},
  update(t){const o=this.o;const G=OFF+s+t;
   T(o.top,0,0,0,1);T(o.cap,960,950,0,pop(t,0.15,Math.min(1.0,Math.max(0.45,L-0.8))));
   const damp=1-eio(seg(t,L-0.9,L-0.05));
   o.items.forEach(({n,it},ix)=>{const a=it._a;const ph=ix*1.7+it.x*0.013;
    T(n,it.x+2.6*Math.cos(0.5*G+ph)*damp,it.y+4.2*Math.sin(0.7*G+ph)*damp,(it.r||0)+0.35*Math.sin(0.45*G+ph)*damp,(it.s||1)*pop(t,a,a+D));});}});});
 window.__IT=scenes.map(sc=>sc.items.map(it=>it._a));window.__SC=scenes.map((sc,i)=>[st[i],(i<scenes.length-1)?st[i+1]:dur]);}
// ---------- scorciatoie di composizione ----------
const CD=(w,h,icon,lines,x,y,at,o)=>I('card16',[w,h,icon,lines,o],x,y,at);
const TG=(s,fs,fill,col,icon,x,y,at,o)=>I('tag16',[s,fs,fill,col,icon,o],x,y,at);
const TK=(o,x,y,at)=>I('ticket16',[o],x,y,at);
const GRN_='url(#g16_grn)',AMB_='url(#g16_amb)',DK_='url(#g16_dk)',RD_='url(#g16_red)';
const ST6=(hi,x,y,at,o)=>I('stairs16',[Object.assign({hi:hi,W:440,H:320},o||{})],x,y,at);
// blocchi 9-12: composizione per scalino (variante X o Y)
function scalino(c){const Y=c.v==='Y';const mx=(x)=>Y?1920-x:x;
 const sx=Y?1590:330, ccx=Y?390:1530, tx=Y?990:930;
 const tk=(a,b)=>Y?[900,1380][a]:[540,1020][a];
 const sy=c.sy||400,ty=c.ty||770;
 const it=[
  ST6([c.step],sx,sy,c.a1,{dim:true}),
  CD(600,140,'ruler',[['OLTRE '+c.thr+' €',44,INK16],['LORDI AL MESE',28,GRN16]],tx,265,c.a2,{band:'#2B6F8F'}),
  CD(600,150,'calc',[[c.pct+' % DELL\'INDICE',48,INK16],['SU TUTTO L\'IMPORTO',28,GRN16]],tx,430,c.a3,{band:'#C78416'}),
  I('cedo16',[{w:480,h:340,rows:[['Pensione lorda',c.pen+' €',true],['Indice (ipotesi)','3 %'],['Quota riconosciuta',c.pct+' %']],bar:true,vfs:30,lfs:24}],ccx,c.cy||410,c.a4),
  TK({w:440,h:190,title:c.t5,val:'≈ '+c.oggi+' €',sub:'AL MESE',col:GRN16,fs:68},tk(0),ty,c.a5),
  TK({w:440,h:190,title:c.t6,val:'≈ '+c.testo+' €',sub:'AL MESE',col:'#C78416',fs:68},tk(1),ty,c.a6),
  TK({w:480,h:190,title:c.t7,val:'≈ '+c.loss+' €',sub:c.s7,col:RED16,fs:64},ccx,ty-5,c.a7)];
 if(c.note)it.push(TG(c.note,30,AMB_,'#4A2E00','warn',Y?990:930,c.ny||600,c.a8));
 return it;}
// ======================= BLOCCHI =======================
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RIVALUTAZIONE 2027',cap:'RIVALUTAZIONE 2027: L\'ARTICOLO 55 LA TAGLIA A SEI SCALINI',items:[
  I('art55',[440],330,450,'Rivalutazione delle pensioni',0.92),
  ST6([],1100,430,'a sei scalini',{W:600,H:370}),
  TK({w:340,h:230,title:'IL TAGLIO',val:'OLTRE 1.000 €',sub:'IN UN ANNO',col:RED16,fs:40,tfs:28},1640,330,'supera mille euro'),
  TG('CHI PERDE?',34,DK_,'#fff','q',330,735,'Chi perde?'),
  TG('QUANTO?',34,DK_,'#fff','coin',700,735,'Quanto?'),
  TG('SU QUALE SCALINO SEI TU?',34,AMB_,'#4A2E00','up',1250,735,'E su quale scalino'),
  TG('UNO SCALINO ALLA VOLTA',32,GRN_,'#fff','calc',760,830,'Facciamo il conto insieme'),
  TG('ALLA FINE: IL TUO CONTO',32,RD_,'#fff','coin',1430,830,'alla fine sai'),
  ]},
]);
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA FONTE',cap:'ATTO DELLA CAMERA N. 3174: IL TESTO UFFICIALE DELLA MANOVRA',items:[
  I('cover16',[480],430,525,'Partiamo dalla fonte',0.97),
  CD(900,140,'cal',[['PRESENTATO IL 30 OTTOBRE',38,INK16],['DAL MINISTRO DELL\'ECONOMIA',30,GRN16]],1330,245,'presentato dal ministro',{band:'#2B6F8F'}),
  CD(900,120,'stato',[['IL TESTO UFFICIALE DELLA MANOVRA',32,INK16]],1330,385,'È il testo ufficiale',{band:GRN16}),
  IO('stamp16',['DA VOTARE IN PARLAMENTO',470,96],1330,715,'che il Parlamento deve ancora votare',1,-5),
  I('mag16',[],940,560,'L\'abbiamo letto direttamente',0.9),
  TG('NIENTE BOZZE',32,RD_,'#fff','x',1420,515,'a bozze'),
  TG('NIENTE CIFRE DEI GIORNALI',32,RD_,'#fff','x',1520,585,'a cifre dei giornali'),
  TG('I CONTI VALGONO PER QUESTO TESTO',34,GRN_,'#fff','ok',1230,840,'I conti che vedrai'),
  ]},
]);
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COS\'È LA RIVALUTAZIONE',cap:'LA RIVALUTAZIONE: L\'AUMENTO CHE OGNI GENNAIO ADEGUA LA PENSIONE AI PREZZI',items:[
  I('art55',[400],300,400,'In quel testo',0.82),
  I('cal16',[],690,410,'che ogni gennaio',0.8),
  I('cedo16',[{w:420,h:250,title:'PENSIONE',rows:[['Pensione','ogni mese'],['Aumento','a gennaio',true]],bar:true,vfs:27,lfs:25}],1160,400,'cioè l\'aumento'),
  I('arR',[],1430,400,'adegua la pensione',0.5),
  TG('PREZZI',38,AMB_,'#4A2E00','coin',1665,400,'ai prezzi'),
  I('meter16',[],560,775,'decide quanta parte'),
  CD(820,150,'ruler',[['UNA REGOLA PER CHI STA',32,INK16],['APPENA OLTRE UN LIMITE',32,INK16],['LA VEDIAMO PIÙ AVANTI',26,GRN16]],1380,745,'E c\'è una regola',{band:'#C78416',lh:40}),
  ]},
]);
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LE SOGLIE',cap:'SEI SCALINI, MISURATI IN MULTIPLI DEL TRATTAMENTO MINIMO',items:[
  ST6([],510,500,'Prima le soglie',{W:600,H:370}),
  I('ruler16',[],1400,270,'si misurano in multipli'),
  TK({w:700,h:220,title:'TRATTAMENTO MINIMO INPS',val:'611,85 €',sub:'AL MESE, QUEST\'ANNO',col:GRN16,fs:68,tfs:30},1400,465,'che quest\'anno è'),
  CD(840,120,'calback',[['DI SOLITO L\'INPS USA IL MINIMO',30,INK16],['DELL\'ANNO PRIMA',30,INK16]],1400,650,'Di solito l\'Imps usa',{band:'#2B6F8F'}),
  CD(840,120,'ok',[['SE FA COSÌ ANCHE STAVOLTA,',30,INK16],['VALE QUELLO DI QUEST\'ANNO',30,GRN16]],1400,785,'se anche stavolta fa così',{band:GRN16}),
  TG('SI SCENDE DALLA CIMA',32,DK_,'#fff','down',510,215,'Scendiamo dalla cima'),
  TG('DOVE ABBIAMO GIÀ VISTO QUESTA SCALA?',27,AMB_,'#4A2E00','q',520,830,'Alla fine scopriamo'),
  ]},
]);
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'UNA RICHIESTA BREVE',cap:'ISCRIVITI E METTI MI PIACE: ADESSO SI SCENDE',items:[
  TG('UNA RICHIESTA BREVE',34,DK_,'#fff','bulb',330,215,'una richiesta breve'),
  I('art55',[420],330,520,'Questo video nasce dalla lettura',0.75),
  IO('mag16',[],470,640,'parola per parola',0.8),
  TG('CI VUOLE TEMPO',32,AMB_,'#4A2E00','clock',330,800,'e ci vuole tempo'),
  I('sub16',[],1100,260,'iscriviti al canale'),
  I('like16',[],1600,260,'metti mi piace'),
  TG('PER TE: UN TOCCO',34,GRN_,'#fff','ok',1130,430,'per te è un tocco'),
  TG('PER NOI: ARRIVARE A PIÙ PENSIONATI',32,DK_,'#fff','people',1300,535,'per noi vuol dire'),
  CD(1000,130,'doc',[['CONTI FATTI SULLE FONTI UFFICIALI',34,INK16]],1230,680,'con conti fatti',{band:'#2B6F8F'}),
  TG('ADESSO SI SCENDE',40,AMB_,'#4A2E00','down',1230,825,'adesso si scende'),
  ]},
]);
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'I DUE METODI DI CALCOLO',cap:'DUE METODI: OGGI PER PEZZI, NEL TESTO UNA SOLA PERCENTUALE',items:[
  TG('OGGI: OGNI PEZZO HA LA SUA PERCENTUALE',34,DK_,'#fff','cut',710,225,'Oggi ogni pezzo'),
  I('seg16',[800,120,GRN_,'100 %','FINO A 4 VOLTE IL MINIMO'],560,355,'cento per cento'),
  I('seg16',[400,120,'#6AAE3C','90 %','TRA 4 E 5 VOLTE'],1168,355,'novanta tra quattro'),
  I('seg16',[400,120,'#D69A22','75 %','OLTRE'],1576,355,'settantacinque oltre'),
  TG('IL TESTO: UNA SOLA PERCENTUALE',34,AMB_,'#4A2E00','lock',560,560,'Il testo cambia'),
  I('seg16',[1616,120,DK_,'UNA SOLA % SU TUTTO L\'IMPORTO',null],968,690,'sceglie una sola percentuale'),
  TG('QUELLA DELLO SCALINO IN CUI CADE IL TOTALE',30,GRN_,'#fff','up',620,810,'quella dello scalino'),
  TG('NON A UN PEZZO',30,RD_,'#fff','x',1530,810,'non a un pezzo'),
  ]},
]);
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SCALINO PIÙ ALTO',cap:'SCALINO PIÙ ALTO: OLTRE 6.118,50 € LORDI AL MESE',items:[
  ST6([6],330,375,'Lo scalino più alto',{dim:true,H:270}),
  CD(600,150,'ruler',[['OLTRE 6.118,50 €',44,INK16],['LORDI AL MESE, 10 VOLTE IL MINIMO',24,GRN16]],940,270,'oltre seimilacentodiciotto',{band:'#2B6F8F'}),
  CD(520,150,'calc',[['32 % DELL\'INDICE',40,INK16],['RICONOSCIUTO DAL TESTO',24,GRN16]],1540,270,'il trentadue per cento',{band:'#C78416'}),
  CD(620,140,'cal',[['L\'INDICE: UN DECRETO',32,INK16],['ATTESO A FINE NOVEMBRE',28,GRN16]],900,440,'L\'indice lo fissa un decreto',{band:'#2B6F8F'}),
  TG('IPOTESI NOSTRA: 3 %',32,AMB_,'#4A2E00','up',1520,415,'noi ipotizziamo'),
  TG('ARROTONDATO ALL\'EURO',30,DK_,'#fff','coin',1520,520,'arrotondiamo all\'euro'),
  I('cedo16',[{w:640,h:250,rows:[['Pensione lorda','7.000,00 €',true],['Indice (ipotesi)','3 %'],['Quota riconosciuta','32 %']],vfs:30,lfs:24,tfs:25}],430,745,'Con settemila euro'),
  TK({w:430,h:210,title:'AUMENTO COL METODO DI OGGI',val:'≈ 179 €',sub:'AL MESE',col:GRN16,fs:68,tfs:22},1110,745,'il metodo di oggi'),
  TK({w:430,h:210,title:'AUMENTO COL TESTO',val:'≈ 67 €',sub:'AL MESE',col:'#C78416',fs:68,tfs:22},1580,745,'il testo, circa'),
  ]},
]);
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA DIFFERENZA',cap:'LA DIFFERENZA: CIRCA 111 € AL MESE, CIRCA 1.448 € SU 13 RATE',items:[
  I('calc16',[],340,525,'La differenza',0.95),
  TK({w:430,h:210,title:'DIFFERENZA',val:'≈ 111 €',sub:'OGNI MESE',col:RED16,fs:68},900,268,'centoundici euro'),
  TK({w:430,h:210,title:'SU 13 RATE',val:'≈ 1.448 €',sub:'IN UN ANNO',col:RED16,fs:62},1400,268,'su tredici rate'),
  CD(1000,130,'warn',[['IL TAGLIO DA PIÙ DI 1.000 €',34,INK16],['ANNUNCIATO ALL\'INIZIO',28,GRN16]],1180,440,'È il taglio da più di mille',{band:RED16}),
  I('bars16',[],1180,702,'Più la pensione sale',0.74),
  ]},
]);
SPECS[9]=()=>mkBlk(TXT,TOT,[{at:0,top:'SECONDO SCALINO',cap:'SECONDO SCALINO: OLTRE 4.894,80 €, 37 % SU TUTTO L\'IMPORTO',items:scalino({v:'X',step:5,thr:'4.894,80',pct:'37',pen:'5.100,00',oggi:'136',testo:'57',loss:'1.030',t5:'AUMENTO COL METODO DI OGGI',t6:'AUMENTO COL TESTO',t7:'PERDITA IN UN ANNO',s7:'SU 13 RATE',a1:'Scendiamo al secondo scalino',a2:'oltre quattromilaottocentonovantaquattro',a3:'il trentasette per cento',a4:'Passiamo a cinquemilacento',a5:'con le regole di oggi',a6:'con la nuova scala',a7:'Su base annua'})}]);
SPECS[10]=()=>mkBlk(TXT,TOT,[{at:0,top:'TERZO SCALINO',cap:'TERZO SCALINO: OLTRE 3.671,10 €, 47 % SU TUTTA LA PENSIONE',items:scalino({v:'Y',step:4,thr:'3.671,10',pct:'47',pen:'3.800,00',oggi:'107',testo:'54',loss:'689',t5:'AUMENTO COL METODO DI OGGI',t6:'AUMENTO COL TESTO',t7:'DI MENO NELL\'ANNO',s7:'SU 13 RATE',a1:'Un gradino più giù',a2:'oltre tremilaseicentosettantuno',a3:'quarantasette per cento',a4:'A tremilaottocento euro',a5:'l\'aumento attuale',a6:'quello del testo',a7:'Sono circa seicentoottantanove'})}]);
SPECS[11]=()=>mkBlk(TXT,TOT,[{at:0,top:'QUARTO SCALINO',cap:'QUARTO SCALINO: OLTRE 3.059,25 €, 53 % SU TUTTO L\'IMPORTO',items:scalino({v:'X',step:3,thr:'3.059,25',pct:'53',pen:'3.300,00',oggi:'95',testo:'52',loss:'558',t5:'OGGI ARRIVEREBBERO',t6:'CON LA MANOVRA',t7:'MANCANO NELL\'ANNO',s7:'SU 13 RATE',a1:'Ancora giù',a2:'oltre tremilacinquantanove',a3:'il cinquantatré per cento',a4:'Per tremilatrecento euro',a5:'oggi arriverebbero',a6:'con la manovra',a7:'Sull\'intero anno'})}]);
SPECS[12]=()=>mkBlk(TXT,TOT,[{at:0,top:'QUINTO SCALINO',cap:'QUINTO SCALINO: OLTRE 2.447,40 €, 85 % SU TUTTA LA PENSIONE',items:scalino({v:'Y',step:2,sy:380,cy:385,ty:770,ny:605,note:'LA PERCENTUALE SCENDE DI POCO, MA VALE PER TUTTO',thr:'2.447,40',pct:'85',pen:'2.700,00',oggi:'80',testo:'69',loss:'148',t5:'AUMENTO COL METODO DI OGGI',t6:'AUMENTO COL TESTO',t7:'MANCANO NELL\'ANNO',s7:'SU 13 RATE',a1:'Siamo al quinto scalino',a2:'oltre duemilaquattrocentoquarantasette',a3:'ottantacinque per cento',a4:'Con duemilasettecento euro',a5:'l\'aumento passa da circa ottanta',a6:'a circa sessantanove',a7:'per l\'anno intero mancano',a8:'La percentuale scende di poco'})}]);
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA REGOLA DEL LIMITE',cap:'REGOLA DEL LIMITE: SOGLIA PIÙ RIVALUTAZIONE PIENA',items:[
  CD(1500,130,'ruler',[['LA REGOLA PROMESSA: PER CHI SUPERA UN LIMITE DI POCO',36,INK16],['DOPO L\'AUMENTO LA PENSIONE NON PUÒ RESTARE SOTTO UNA CIFRA',28,GRN16]],960,245,'Qui scatta la regola promessa',{band:'#2B6F8F'}),
  TG('SOGLIA',44,DK_,'#fff','ruler',290,440,'sotto la soglia',{minw:380}),
  I('op16',['+'],545,440,'più la rivalutazione piena'),
  TG('RIVALUTAZIONE PIENA',36,GRN_,'#fff','up',925,440,'più la rivalutazione piena'),
  I('op16',['='],1300,440,'Con la soglia più bassa'),
  TK({w:380,h:200,title:'LIMITE',val:'2.520,82 €',sub:'CON L\'INDICE D\'ESEMPIO',col:'#C78416',fs:50,tfs:30,sfs:22},1620,440,'il limite è'),
  TK({w:420,h:200,title:'PENSIONE DI PARTENZA',val:'2.450 €',sub:'AL MESE',col:'#2B6F8F',fs:62,tfs:22},300,740,'Chi ha una pensione'),
  I('arR',[],660,740,'arriva a quella cifra',0.8),
  TK({w:440,h:200,title:'ARRIVA A',val:'2.520,82 €',sub:'IL LIMITE',col:GRN16,fs:52,tfs:28},1010,740,'arriva a quella cifra'),
  TK({w:420,h:200,title:'RISPETTO A OGGI',val:'− 3 €',sub:'AL MESE, CIRCA',col:RED16,fs:68,tfs:24},1500,740,'perde circa tre euro'),
  ]},
]);
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ULTIMO SCALINO',cap:'ULTIMO SCALINO: L\'AUMENTO RESTA INTERO, COME OGGI',items:[
  ST6([1],330,380,'Scendiamo all\'ultimo scalino',{dim:true}),
  TG('FINO ALLA SOGLIA DEL QUINTO SCALINO',34,DK_,'#fff','ruler',1180,235,'fino alla soglia'),
  CD(900,130,'ok',[['L\'AUMENTO RESTA INTERO,',36,INK16],['COME OGGI',32,GRN16]],1130,390,'Qui l\'aumento resta intero',{band:GRN16}),
  I('cedo16',[{w:440,h:160,title:'PENSIONE',hdr:46,tfs:22,rows:[['Lorda','1.500,00 €',true]],vfs:30,lfs:24}],880,600,'una pensione da millecinquecento'),
  TK({w:320,h:160,title:'A RATA',val:'+ 45 €',col:GRN16,fs:56,tfs:22},1260,600,'quarantacinque a rata'),
  TK({w:320,h:160,title:'NELL\'ANNO',val:'585 €',col:GRN16,fs:56,tfs:22},1640,600,'cinquecentoottantacinque'),
  I('cedo16',[{w:440,h:160,title:'PENSIONE',hdr:46,tfs:22,rows:[['Lorda','2.000,00 €',true]],vfs:30,lfs:24}],880,790,'una da duemila'),
  TK({w:320,h:160,title:'A RATA',val:'+ 60 €',col:GRN16,fs:56,tfs:22},1260,790,'sessanta a rata'),
  TK({w:320,h:160,title:'NELL\'ANNO',val:'780 €',col:GRN16,fs:56,tfs:22},1640,790,'settecentoottanta'),
  CD(520,230,'ok',[['SE SEI QUI,',32,INK16],['PER TE L\'ARTICOLO',28,INK16],['NON CAMBIA',28,INK16],['LA RIVALUTAZIONE',28,GRN16]],330,740,'Se sei qui',{band:GRN16}),
  ]},
]);
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA SCALA GIÀ VISTA',cap:'LA SCALA GIÀ VISTA: LE PERCENTUALI DEL 2023',items:[
  I('tl16',[],960,275,'E la scala promessa'),
  TG('LA SCALA DEL 2023',32,DK_,'#fff','cal',430,400,'del duemilaventitré'),
  I('stairs16',[{n:5,W:540,H:290,hi:[5],labels:['85 %','53 %','47 %','37 %','32 %']}],430,622,'ottantacinque, cinquantatré'),
  TG('APPLICATE ALL\'INTERO ASSEGNO',32,GRN_,'#fff','ok',1300,500,'applicate all\'intero'),
  CD(960,120,'doc',[['LEGGE DI FINE 2022: PER DUE ANNI',34,INK16]],1300,615,'Le fissò la legge',{band:'#2B6F8F'}),
  TG('2024: L\'ULTIMO SCALINO SCENDE A 22 %',32,AMB_,'#4A2E00','down',1300,715,'nel duemilaventiquattro'),
  TG('DAL 2025: DI NUOVO LE FASCE DI OGGI',32,DK_,'#fff','next',1300,810,'Dal duemilaventicinque'),
  TG('FONTE: SCHEDE DELLA CAMERA',30,DK_,'#fff','doc',430,855,'Fonte: schede'),
  ]},
]);
SPECS[16]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IN SINTESI',cap:'',items:[
  I('watch16',[],470,470,0),
  CD(940,130,'ruler',[['OLTRE IL LIMITE PIÙ BASSO: IL TAGLIO C\'È E CRESCE CON L\'IMPORTO',28,INK16],['SOTTO: L\'AUMENTO ARRIVA INTERO',30,GRN16]],1350,235,'In sintesi',{band:'#2B6F8F',lh:40}),
  TG('CIFRE LORDE E ARROTONDATE',30,DK_,'#fff','coin',1190,345,'Cifre lorde'),
  TG('VOTO DEL PARLAMENTO',28,AMB_,'#4A2E00','stato',1115,420,'voto del Parlamento'),
  TG('DECRETO DELL\'INDICE',28,AMB_,'#4A2E00','doc',1610,420,'decreto dell\'indice'),
  TG('E TU, A CHE SCALINO SEI? SCRIVILO NEI COMMENTI',25,GRN_,'#fff','chat',1350,490,'E tu, a che scalino'),
  TG('UN PARENTE CON UNA PENSIONE ALTA? MANDAGLI IL VIDEO',25,GRN_,'#fff','share',1350,548,'Hai un parente'),
  I('dbox16',[940,100,[['CANALE INFORMATIVO, NON CONSULENZA, NON AFFILIATO ALL\'INPS',24,'#fff'],['VERIFICA SU INPS.IT O CON UN PATRONATO',24,'#7FF0D2']]],1350,640,'Canale informativo'),
  ]},
]);
Object.assign(BUILD,{seg16:(g,w,h,fill,label,sub)=>{el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:18,fill:fill,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
 fitT(g,label,0,0,label.length>8?40:60,fill===AMB_?'#4A2E00':'#fff','900',w*0.9);if(sub)fitT(g,sub,0,h/2+36,28,'#BFFBEA','bold',w);}});
