const S=[];
// ---------- SCENE 1 : hook ----------
S[0]={D:5.0,build(g){
 const o={};
 // calendar
 o.calP=el('g',{},g);
 const b=el('g',{},o.calP);
 el('rect',{x:-232,y:6,width:464,height:566,rx:34,fill:'#C9D6D8'},b); // sheet under
 el('rect',{x:-230,y:0,width:460,height:560,rx:34,fill:'url(#g_paper)',filter:'url(#g_sh)'},b);
 const clip=el('clipPath',{id:'c1clip'},b);el('rect',{x:-230,y:0,width:460,height:560,rx:34},clip);
 const hg=el('g',{'clip-path':'url(#c1clip)'},b);
 el('rect',{x:-230,y:0,width:460,height:130,fill:'url(#g_head)'},hg);
 el('rect',{x:-230,y:0,width:460,height:10,fill:'#fff',opacity:.35},hg);
 el('rect',{x:-230,y:128,width:460,height:8,fill:'#0B4A50',opacity:.15},hg);
 txt(b,'OTTOBRE 2026',0,86,46,'#FFFFFF');
 txt(b,'1',0,400,320,'#0B4A50');
 txt(b,'GIOVEDÌ',0,478,42,'#1B9F81');
 for(let i=0;i<14;i++)el('rect',{x:-200+i*30,y:512,width:16,height:4,rx:2,fill:'#B7C7CA'},b);
 metalRing(b,-120,-44,36,92);metalRing(b,120,-44,36,92);
 o.glow=el('circle',{cx:0,cy:270,r:150,fill:'none',stroke:'#2FBF9B','stroke-width':6,opacity:0},b);
 // envelope
 o.env=el('g',{},g);
 const e=o.env;
 el('rect',{x:-320,y:-140,width:640,height:400,rx:24,fill:'#CDBF9C',filter:'url(#g_sh)'},e);
 el('polygon',{points:'-320,-140 320,-140 0,-330',fill:'#B7A882'},e);
 o.sheet=el('g',{},e);
 el('rect',{x:-270,y:0,width:540,height:340,rx:18,fill:'#FFFFFF',filter:'url(#g_sh3)'},o.sheet);
 txt(o.sheet,'CEDOLINO · OTTOBRE',0,46,30,'#1B9F81');
 el('rect',{x:-230,y:64,width:460,height:3,fill:'#C9D6D8'},o.sheet);
 txt(o.sheet,'IMPORTO NETTO',0,110,26,'#6F878C','bold');
 txt(o.sheet,'€ •••,••',0,200,84,'#0B4A50');
 el('polygon',{points:'-320,-140 -320,260 0,40',fill:'#E4D9BC'},e);
 el('polygon',{points:'320,-140 320,260 0,40',fill:'#E9DFC4'},e);
 el('polygon',{points:'-320,260 320,260 0,40',fill:'#F1E9D2'},e);
 el('path',{d:'M-320 260 L0 40 L320 260',fill:'none',stroke:'#fff','stroke-opacity':.5,'stroke-width':3},e);
 // magnifier
 o.mag=el('g',{},g);
 const m=o.mag;
 el('line',{x1:78,y1:78,x2:190,y2:190,stroke:'#0A3F45','stroke-width':34,'stroke-linecap':'round'},m);
 el('line',{x1:78,y1:78,x2:190,y2:190,stroke:'url(#g_metal)','stroke-width':22,'stroke-linecap':'round'},m);
 const lc=el('clipPath',{id:'lens1'},m);el('circle',{cx:0,cy:0,r:104},lc);
 el('circle',{cx:0,cy:0,r:104,fill:'#E9FBF6'},m);
 o.lensG=el('g',{'clip-path':'url(#lens1)'},m);
 o.lensT=txt(o.lensG,'€ •••,••',0,0,104,'#0B4A50');
 o.lensQ=el('circle',{cx:0,cy:0,r:104,fill:'#fff',opacity:.1},m);
 el('circle',{cx:0,cy:0,r:104,fill:'none',stroke:'url(#g_metal)','stroke-width':22},m);
 el('circle',{cx:0,cy:0,r:114,fill:'none',stroke:'#0A3F45','stroke-width':4,opacity:.7},m);
 el('path',{d:'M-70 -30 A76 76 0 0 1 -10 -76',fill:'none',stroke:'#fff','stroke-width':12,'stroke-linecap':'round',opacity:.7},m);
 o.q=el('g',{},g);
 el('circle',{cx:0,cy:0,r:62,fill:'url(#g_badge)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},o.q);
 txt(o.q,'!',0,26,84,'#fff');
 this.o=o;},
 update(t){const o=this.o;
 // calendar drop + swing
 const p=eob(seg(t,0.1,1.0));const y=lerp(-700,250,p);
 const tt=Math.max(0,t-0.9);const ang=(t>0.9)?9*Math.exp(-2.6*tt)*Math.sin(8*tt):0;
 T(o.calP,540,y,ang,1);
 op(o.glow,0.5+0.5*Math.sin(t*5)*(t>1.2?1:0)*0.5);
 // envelope
 const pe=eob(seg(t,1.5,2.3));T(o.env,540,lerp(2000,1400,pe),0,1);
 const ps=eo3(seg(t,2.4,3.2));T(o.sheet,0,lerp(40,-215,ps),0,1);
 // magnifier
 const pm=eo3(seg(t,3.5,4.3));
 const hx=lerp(1250,600,pm)+10*Math.sin(t*3)*pm, hy=lerp(1150,1290,pm)+8*Math.cos(t*3)*pm;
 T(o.mag,hx,hy,0,1);
 // lens content: magnify amount text at world (540, envY + sheetY + 200)
 const ey=lerp(2000,1400,pe), sy=lerp(40,-215,ps);
 const wx=540, wy=ey+sy+200-30;
 o.lensT.setAttribute('x',(wx-hx)*1.7);o.lensT.setAttribute('y',(wy-hy)*1.7+34);
 op(o.mag,pm>0?1:0);
 const pq=eob(seg(t,4.2,4.8));T(o.q,870,1130,0,pq);
 },
};
// ---------- SCENE 2 : totale ----------
S[1]={D:3.433,build(g){
 const o={};
 o.spot=el('polygon',{points:'440,900 640,900 960,1400 120,1400',fill:'url(#g_spot)'},g);
 o.up=el('g',{},g);
 const pp=paper(o.up,840,560);
 txt(o.up,'CEDOLINO DI PENSIONE',0,74,40,'#0B4A50');
 txt(o.up,'OTTOBRE 2026',0,118,28,'#1B9F81');
 rows(o.up,['IMPORTO LORDO','TRATTENUTE','RIMBORSO 730','ARRETRATI'],840,110,92);
 o.q=[];for(let i=0;i<3;i++){const q=el('g',{},g);el('circle',{r:34,fill:'url(#g_badge)',stroke:'#fff','stroke-width':5},q);txt(q,'?',0,14,44,'#fff');o.q.push(q);}
 o.low=el('g',{},g);
 el('rect',{x:-450,y:-190,width:900,height:380,rx:40,fill:'#2FBF9B',opacity:.35,filter:'url(#g_glow)'},o.low);
 el('rect',{x:-440,y:-180,width:880,height:360,rx:36,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.low);
 el('rect',{x:-440,y:-180,width:880,height:70,rx:36,fill:'url(#g_head)'},o.low);
 el('rect',{x:-440,y:-140,width:880,height:30,fill:'url(#g_head)'},o.low);
 txt(o.low,'TOTALE NETTO',0,-124,40,'#fff');
 txt(o.low,'€ •••,••',0,70,150,'#0B4A50');
 this.o=o;},
 update(t){const o=this.o;
 const pl=eob(seg(t,0.05,0.8));T(o.low,540,lerp(2100,1320,pl),0,1+0.02*Math.sin(t*4));
 const dim=seg(t,0.7,1.3);op(o.spot,dim);
 let a=1-0.5*dim;const lose=seg(t,1.9,3.2);
 T(o.up,540,lerp(280,150,eio(lose)),-5*eio(lose),1-0.1*lose);
 op(o.up,a*(1-eio(lose)));o.up.style.filter=`blur(${lose*14}px)`;
 o.q.forEach((q,i)=>{const s=eob(seg(t,1.9+i*0.2,2.5+i*0.2));const dx=[-300,0,300][i];
  T(q,540+dx+18*Math.sin(t*3+i),lerp(560,520,eio(lose))-14*Math.sin(t*2.4+i),0,s*(1-0.4*lose));op(q,1-lose*0.8);});
 },
};
// ---------- SCENE 3 : arretrati / 730 / trattenute ----------
S[2]={D:6.4,build(g){
 const o={};
 o.up=el('g',{},g);
 paper(o.up,840,560);
 txt(o.up,'CEDOLINO DI PENSIONE',0,74,40,'#0B4A50');
 txt(o.up,'OTTOBRE 2026',0,118,28,'#1B9F81');
 rows(o.up,['IMPORTO LORDO','ARRETRATI','RIMBORSO 730','TRATTENUTE'],840,110,92);
 o.hl=[];
 for(let i=0;i<3;i++){const r=el('rect',{x:-410,y:214+i*92,width:820,height:62,rx:14,fill:i==2?'#E5533D':'#2FBF9B',opacity:0},o.up);o.hl.push(r);}
 // medallions
 const specs=[{x:180,c:'g_badge',l:'ARRETRATI'},{x:540,c:'g_badge',l:'RIMBORSO 730'},{x:860,c:'g_red',l:'TRATTENUTE'}];
 o.med=specs.map((s,i)=>{const m=el('g',{},g);
  el('circle',{r:112,fill:'url(#'+s.c+')',stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},m);
  el('circle',{r:92,fill:'#FBF6EA'},m);
  txt(m,s.l,0,168,32,'#F0FBF8');
  return m;});
 // icon A: coin stack + up arrow
 const A=el('g',{},o.med[0]);
 for(let i=0;i<4;i++)goldCoin(A,0,26-i*18,58,17,12);
 el('path',{d:'M0 -58 L-30 -22 L-12 -22 L-12 -2 L12 -2 L12 -22 L30 -22 Z',fill:'#1B9F81'},A);
 // icon B: form 730 + return arrow
 const B=el('g',{},o.med[1]);
 el('rect',{x:-50,y:-62,width:100,height:124,rx:10,fill:'#fff',stroke:'#0B4A50','stroke-width':5},B);
 txt(B,'730',0,-22,38,'#0B4A50');
 for(let i=0;i<3;i++)el('rect',{x:-32,y:-4+i*20,width:64,height:6,rx:3,fill:'#9DB4B8'},B);
 el('path',{d:'M-78 30 A70 70 0 0 0 40 74',fill:'none',stroke:'#1B9F81','stroke-width':12,'stroke-linecap':'round'},B);
 el('polygon',{points:'36,52 68,80 30,96',fill:'#1B9F81'},B);
 // icon C: coin cut
 const C=el('g',{},o.med[2]);
 coin(C,0,-6,58);
 el('polygon',{points:'-12,-70 62,-70 62,20 20,-6',fill:'#FBF6EA'},C);
 el('path',{d:'M-12 -70 L20 -6 L62 20',fill:'none',stroke:'#E5533D','stroke-width':6,'stroke-dasharray':'8 8'},C);
 el('rect',{x:-40,y:38,width:80,height:20,rx:10,fill:'#E5533D'},C);
 this.o=o;},
 update(t){const o=this.o;
 const pu=eob(seg(t,0.1,0.9));T(o.up,540,lerp(-700,250,pu),0,1);
 const times=[3.0,4.05,5.35];
 o.med.forEach((m,i)=>{const p=eob(seg(t,times[i],times[i]+0.55));T(m,[180,540,860][i],1290+8*Math.sin(t*2.5+i)*(p>0?1:0),(1-p)*-20,Math.max(0,p));});
 o.hl.forEach((r,i)=>{const on=seg(t,times[i],times[i]+0.4)*(1-0.0);r.setAttribute('opacity',0.28*on*(0.6+0.4*Math.sin(t*4)));});
 },
};
// ---------- SCENE 4 : bilancia ----------
S[3]={D:3.833,build(g){
 const o={};
 o.sc=el('g',{},g);
 const s=o.sc;
 el('polygon',{points:'-150,300 150,300 100,250 -100,250',fill:'url(#g_metal)',filter:'url(#g_sh)'},s);
 el('rect',{x:-160,y:296,width:320,height:36,rx:14,fill:'#0A3F45',filter:'url(#g_sh)'},s);
 el('rect',{x:-16,y:-40,width:32,height:300,rx:12,fill:'url(#g_metal)'},s);
 o.beam=el('g',{},s);
 el('rect',{x:-360,y:-14,width:720,height:28,rx:14,fill:'url(#g_metal)',filter:'url(#g_sh3)'},o.beam);
 el('circle',{cx:-360,cy:0,r:16,fill:'#0A3F45'},o.beam);el('circle',{cx:360,cy:0,r:16,fill:'#0A3F45'},o.beam);
 el('circle',{cx:0,cy:-50,r:30,fill:'url(#g_rim)',stroke:'#fff','stroke-width':4},s);
 el('circle',{cx:0,cy:0,r:26,fill:'url(#g_metal)',stroke:'#0A3F45','stroke-width':6},s);
 o.chL=el('g',{},s);o.chR=el('g',{},s);
 o.panL=el('g',{},s);o.panR=el('g',{},s);
 [o.panL,o.panR].forEach((pn,i)=>{
  if(i==0){for(let k=0;k<4;k++)goldCoin(pn,0,-8-k*17,58,17,12);}
  else{for(let k=0;k<1;k++)goldCoin(pn,0,-8,58,17,12);}
  el('path',{d:'M-140 0 Q0 90 140 0 Z',fill:'url(#g_metal)',filter:'url(#g_sh3)'},pn);
  el('ellipse',{cx:0,cy:0,rx:140,ry:16,fill:'#DCE7EA'},pn);
  const bd=el('g',{},pn);});
 // draw coins above pan rim
 o.badL=el('g',{},g);el('circle',{r:100,fill:'url(#g_badge)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},o.badL);
 txt(o.badL,'+',0,34,120,'#fff');txt(o.badL,'PIÙ',0,148,44,'#7FF0D2');
 o.badR=el('g',{},g);el('circle',{r:100,fill:'url(#g_red)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},o.badR);
 txt(o.badR,'−',0,34,120,'#fff');txt(o.badR,'MENO',0,148,44,'#FFB4A8');
 this.o=o;},
 update(t){const o=this.o;
 const ps=eob(seg(t,0.05,0.9));T(o.sc,540,lerp(-500,470,ps),0,1);
 let ang;
 if(t<1.0)ang=0; else if(t<2.5)ang=9*Math.sin((t-1.0)*4.2)*Math.min(1,(t-1.0)*2);
 else if(t<3.2)ang=lerp(9*Math.sin(1.5*4.2),-13,eio(seg(t,2.5,3.0)));
 else ang=lerp(-13,13,eio(seg(t,3.2,3.7)));
 o.beam.setAttribute('transform',`rotate(${ang})`);
 const r=ang*Math.PI/180, len=360;
 const lx=-len*Math.cos(r), ly=-len*Math.sin(r), rx=len*Math.cos(r), ry=len*Math.sin(r);
 const drop=250;
 T(o.panL,lx,ly+drop,0,1);T(o.panR,rx,ry+drop,0,1);
 // chains
 [[o.chL,lx,ly],[o.chR,rx,ry]].forEach(([c,x,y])=>{c.innerHTML='';
  [-120,0,120].forEach(dx=>el('line',{x1:x,y1:y,x2:x+dx,y2:y+drop-4,stroke:'#0A3F45','stroke-width':4,'stroke-dasharray':'10 6'},c));});
 const act=t>2.5?(ang<0?0:1):-1;
 const pl=eob(seg(t,1.6,2.3));
 T(o.badL,300,1290,0,pl*(act==0?1.12:1));T(o.badR,780,1290,0,pl*(act==1?1.12:1));
 op(o.badL,act==1?0.55:1);op(o.badR,act==0?0.55:1);
 },
};
// ---------- SCENE 5 : My INPS ----------
S[4]={D:5.4,build(g){
 const o={};
 o.ph=el('g',{},g);const P=o.ph;
 el('rect',{x:-400,y:-660,width:800,height:1320,rx:88,fill:'#061E22',filter:'url(#g_sh)'},P);
 el('rect',{x:-400,y:-660,width:800,height:1320,rx:88,fill:'none',stroke:'url(#g_metal)','stroke-width':8},P);
 const cl=el('clipPath',{id:'scr5'},P);el('rect',{x:-376,y:-636,width:752,height:1272,rx:66},cl);
 const sc=el('g',{'clip-path':'url(#scr5)'},P);
 el('rect',{x:-376,y:-636,width:752,height:1272,fill:'#EAF3F4'},sc);
 el('rect',{x:-376,y:-636,width:752,height:210,fill:'url(#g_head)'},sc);
 el('rect',{x:-90,y:-632,width:180,height:34,rx:17,fill:'#061E22'},sc);
 // header logo (generic)
 el('circle',{cx:-250,cy:-500,r:44,fill:'#fff'},sc);txt(sc,'M',-250,-484,52,'#1B9F81');
 txt(sc,'My INPS',-40,-482,58,'#fff','bold','start');
 // search bar
 o.bar=el('g',{},sc);
 el('rect',{x:-330,y:-380,width:660,height:96,rx:48,fill:'#fff',filter:'url(#g_sh3)'},o.bar);
 el('circle',{cx:-278,cy:-334,r:16,fill:'none',stroke:'#1B9F81','stroke-width':6},o.bar);
 el('line',{x1:-266,y1:-322,x2:-250,y2:-306,stroke:'#1B9F81','stroke-width':6,'stroke-linecap':'round'},o.bar);
 o.typed=txt(o.bar,'',-225,-320,36,'#0B4A50','bold','start');
 o.cur=el('rect',{x:-225,y:-354,width:4,height:44,fill:'#1B9F81'},o.bar);
 // tiles
 o.tiles=el('g',{},sc);
 const names=['Pensione','Cedolino','Certificati','Domande'];
 o.tl=names.map((n,i)=>{const gx=(i%2)*340-170,gy=Math.floor(i/2)*300-190;const tg=el('g',{},o.tiles);
  el('rect',{x:-150,y:-120,width:300,height:250,rx:36,fill:'#fff',filter:'url(#g_sh3)'},tg);
  el('circle',{cx:0,cy:-40,r:52,fill:i==1?'url(#g_badge)':'#CFE3E5'},tg);
  el('rect',{x:-24,y:-64,width:48,height:60,rx:8,fill:'#fff'},tg);
  el('rect',{x:-14,y:-52,width:28,height:5,rx:2,fill:i==1?'#1B9F81':'#9DB4B8'},tg);el('rect',{x:-14,y:-40,width:28,height:5,rx:2,fill:i==1?'#1B9F81':'#9DB4B8'},tg);el('rect',{x:-14,y:-28,width:18,height:5,rx:2,fill:i==1?'#1B9F81':'#9DB4B8'},tg);
  txt(tg,n,0,88,32,'#0B4A50');tg._p=[gx,gy];return tg;});
 // results
 o.res=el('g',{},sc);
 el('rect',{x:-340,y:-250,width:680,height:640,rx:36,fill:'#fff',filter:'url(#g_sh)'},o.res);
 txt(o.res,'CEDOLINO · OTTOBRE 2026',0,-190,30,'#1B9F81');
 o.rowY=[];const lab=['Importo lordo','Arretrati','Rimborso 730','Trattenute'];
 o.hlr=el('rect',{x:-316,y:-160,width:632,height:100,rx:20,fill:'#2FBF9B',opacity:0},o.res);
 o.ck=[];
 lab.forEach((l,i)=>{const y=-110+i*120;o.rowY.push(y);
  txt(o.res,l,-290,y+12,38,'#0B4A50','bold','start');
  el('rect',{x:110,y:y-12,width:160,height:28,rx:14,fill:'#BFD0D3'},o.res);
  const c=el('path',{d:`M-320 ${y+130-70} l0 0`,fill:'none'},o.res);c.remove();
  const k=el('path',{d:`M292 ${y+4} l14 16 l30 -34`,fill:'none',stroke:'#1B9F81','stroke-width':10,'stroke-linecap':'round','stroke-linejoin':'round','stroke-dasharray':70,'stroke-dashoffset':70},o.res);o.ck.push(k);
  if(i<3)el('rect',{x:-300,y:y+52,width:600,height:3,fill:'#E1EAEC'},o.res);});
 // finger touch
 o.tap=el('g',{},g);
 o.rip=el('circle',{r:40,fill:'none',stroke:'#fff','stroke-width':8},o.tap);
 el('circle',{r:34,fill:'#0B4A50',opacity:.35},o.tap);el('circle',{r:26,fill:'#fff',opacity:.9,filter:'url(#g_sh3)'},o.tap);
 this.o=o;},
 update(t){const o=this.o;
 const pp=eob(seg(t,0,0.7));T(o.ph,540,lerp(2200,860,pp),-3.5+ (1-pp)*6,1);
 // tiles pop
 o.tl.forEach((tg,i)=>{const s=eob(seg(t,0.5+i*0.18,1.1+i*0.18));const out=seg(t,3.2,3.5);
  T(tg,tg._p[0],tg._p[1]+30,0,Math.max(0,s)*(1-out*0.9));op(tg,1-out);});
 // pulse on cedolino tile before typing
 // typing
 const full='Cedolino della pensione';const n=Math.floor(clamp((t-1.5)/1.8)*full.length+0.0001);
 o.typed.textContent=full.slice(0,n);
 const w=n*20.4;o.cur.setAttribute('x',-222+w);op(o.cur,(t>1.4&&t<3.5&&Math.floor(t*3)%2==0)?1:0);
 // tap ripple on search bar at 1.3 and result at 3.4
 const tp=(t>1.1&&t<1.6)?seg(t,1.1,1.6):(t>3.3&&t<3.85?seg(t,3.3,3.85):-1);
 if(tp>=0){const cx=(t<2?540-130:540+40),cy=(t<2?860-350:860-180);T(o.tap,cx,cy+ (t<2?0:0),0,1);op(o.tap,1-Math.abs(tp-0.5)*0.6);
  o.rip.setAttribute('r',40+tp*90);o.rip.setAttribute('opacity',1-tp);}else op(o.tap,0);
 // results
 const pr=eob(seg(t,3.5,4.1));T(o.res,0,lerp(700,0,eo3(seg(t,3.5,4.1))),0,1);op(o.res,seg(t,3.5,3.8));
 // highlighter
 const idx=(t-3.7)/0.45;const ii=clamp(Math.floor(idx),0,3);
 const hy=o.rowY[ii]-52;
 o.hlr.setAttribute('y',hy);o.hlr.setAttribute('opacity',t>3.7&&t<5.35?0.3:0);
 o.ck.forEach((k,i)=>{const a=seg(t,3.85+i*0.45,4.1+i*0.45);k.setAttribute('stroke-dashoffset',70*(1-a));});
 },
};
// ---------- SCENE 6 : chiedi ----------
S[5]={D:5.833,build(g){
 const o={};
 o.up=el('g',{},g);
 paper(o.up,840,520);
 txt(o.up,'CEDOLINO DI PENSIONE',0,74,40,'#0B4A50');
 txt(o.up,'OTTOBRE 2026',0,118,28,'#1B9F81');
 rows(o.up,['IMPORTO LORDO','ARRETRATI','RIMBORSO 730','TRATTENUTE'],840,110,92);
 o.pen=el('ellipse',{cx:0,cy:0,rx:415,ry:56,fill:'none',stroke:'#E5533D','stroke-width':10,'stroke-linecap':'round','stroke-dasharray':2400,'stroke-dashoffset':2400,transform:'translate(0 288) rotate(-1.5)'},o.up);
 o.qb=el('g',{},g);
 el('circle',{r:56,fill:'url(#g_red)',stroke:'#fff','stroke-width':7,filter:'url(#g_sh2)'},o.qb);txt(o.qb,'?',0,22,72,'#fff');
 // plaques
 function plaque(label,icon,x){const p=el('g',{},g);
  el('rect',{x:-215,y:-190,width:430,height:380,rx:44,fill:'#2FBF9B',opacity:.35,filter:'url(#g_glow)'},p).setAttribute('class','pg');
  el('rect',{x:-200,y:-175,width:400,height:350,rx:40,fill:'url(#g_paper)',filter:'url(#g_sh)'},p);
  el('rect',{x:-200,y:-175,width:400,height:96,rx:40,fill:'url(#g_head)'},p);el('rect',{x:-200,y:-125,width:400,height:46,fill:'url(#g_head)'},p);
  txt(p,label,0,-104,52,'#fff');
  icon(p);p._x=x;return p;}
 o.pl=[plaque('INPS',p=>{ // building
  el('polygon',{points:'-90,-30 0,-84 90,-30',fill:'#0B4A50'},p);
  el('rect',{x:-96,y:-30,width:192,height:14,fill:'#0B4A50'},p);
  [-66,-22,22,66].forEach(x=>el('rect',{x:x-9,y:-12,width:18,height:84,rx:4,fill:'#1B9F81'},p));
  el('rect',{x:-104,y:80,width:208,height:18,rx:6,fill:'#0B4A50'},p);
 },300),plaque('PATRONATO',p=>{ // two people + shield
  el('circle',{cx:-46,cy:-38,r:26,fill:'#0B4A50'},p);el('path',{d:'M-100 62 A54 54 0 0 1 8 62 Z',fill:'#0B4A50'},p);
  el('circle',{cx:46,cy:-38,r:26,fill:'#1B9F81'},p);el('path',{d:'M-8 62 A54 54 0 0 1 100 62 Z',fill:'#1B9F81'},p);
  el('rect',{x:-104,y:74,width:208,height:16,rx:8,fill:'#0B4A50'},p);
 },780)];
 o.pl[1].querySelector('text').setAttribute('font-size',44);
 // thought bubble
 o.tb=el('g',{},g);
 el('circle',{cx:-70,cy:130,r:14,fill:'#fff',filter:'url(#g_sh3)'},o.tb);el('circle',{cx:-100,cy:170,r:8,fill:'#fff'},o.tb);
 el('rect',{x:-260,y:-70,width:520,height:180,rx:90,fill:'#fff',filter:'url(#g_sh)'},o.tb);
 txt(o.tb,'€ sbagliato?',0,26,60,'#B8331F');
 this.o=o;},
 update(t){const o=this.o;
 const pu=eob(seg(t,0.05,0.8));T(o.up,540,lerp(-700,150,pu),0,1);
 o.pen.setAttribute('stroke-dashoffset',2400*(1-eio(seg(t,0.8,1.7))));
 const qb=eob(seg(t,1.7,2.2));T(o.qb,930,lerp(0,470,1)+ -5*Math.sin(t*4),0,qb*(1-seg(t,2.4,2.8)*0.0));
 const up2=seg(t,2.3,2.8);op(o.up,1);
 const tm=[2.4,3.3];
 o.pl.forEach((p,i)=>{const s=eob(seg(t,tm[i],tm[i]+0.6));const glow=t>5.1?0.6+0.4*Math.sin((t-5.1)*8):0;
  T(p,p._x,1370,(1-s)*(i?8:-8),Math.max(0,s)*(1+0.03*glow));
  p.querySelector('.pg').setAttribute('opacity',t>5.1?0.35+0.5*glow:0.35);});
 // bubble grows then deflates
 const g1=eob(seg(t,4.4,5.0));const d=seg(t,5.05,5.35);
 const sc=Math.max(0,g1)*(1-eio(d))*(1+0.08*Math.sin(d*40)*(d>0?1:0));
 T(o.tb,540,1010-30*d,0,sc);op(o.tb,1-d);
 },
};
// ---------- SCENE 7 : iscriviti ----------
S[6]={D:5.4,build(g){
 const o={};
 o.hero=el('g',{},g);o.heroIn=el('g',{transform:'translate(-395 -425)'},o.hero);o.heroIn.innerHTML=LOGO_ART;
 o.pill=el('g',{},g);
 o.pillBg=el('rect',{x:-260,y:-70,width:520,height:140,rx:70,fill:'url(#g_red)',filter:'url(#g_sh)'},o.pill);
 o.pillT=txt(o.pill,'ISCRIVITI',0,24,64,'#fff');
 o.tick=el('path',{d:'M-190 0 l24 26 l44 -50',fill:'none',stroke:'#fff','stroke-width':14,'stroke-linecap':'round','stroke-linejoin':'round',opacity:0},o.pill);
 o.bell=el('g',{},g);const bl=el('g',{filter:'url(#g_sh2)'},o.bell);
 el('path',{d:'M-46 34 C-46 -10 -30 -50 0 -50 C30 -50 46 -10 46 34 L62 52 L-62 52 Z',fill:'#F4C542'},bl);
 el('circle',{cx:0,cy:-58,r:10,fill:'#F4C542'},bl);el('circle',{cx:0,cy:66,r:13,fill:'#C99A1E'},bl);
 el('path',{d:'M-26 -8 C-26 -30 -14 -40 -4 -42',fill:'none',stroke:'#fff',opacity:.6,'stroke-width':6,'stroke-linecap':'round'},bl);
 o.tap=el('g',{},g);o.rip=el('circle',{r:40,fill:'none',stroke:'#fff','stroke-width':8},o.tap);el('circle',{r:26,fill:'#fff',opacity:.9,filter:'url(#g_sh3)'},o.tap);
 // news card
 o.nc=el('g',{},g);
 el('rect',{x:-400,y:-170,width:800,height:340,rx:40,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.nc);
 el('rect',{x:-400,y:-170,width:800,height:84,rx:40,fill:'url(#g_red)'},o.nc);el('rect',{x:-400,y:-130,width:800,height:44,fill:'url(#g_red)'},o.nc);
 txt(o.nc,'NOVITÀ PENSIONI',0,-108,44,'#fff');
 [-30,40,110].forEach((y,i)=>el('rect',{x:-350,y:y,width:i==2?420:700,height:22,rx:11,fill:i==0?'#0B4A50':'#BFD0D3'},o.nc));
 // seals
 o.seal=['INPS','LAVORO','MEF'].map((s,i)=>{const sg=el('g',{},g);
  el('circle',{r:104,fill:'url(#g_rim)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},sg);
  el('circle',{r:80,fill:'none',stroke:'#fff','stroke-width':4,'stroke-dasharray':'4 8'},sg);
  el('circle',{r:66,fill:'#FBF6EA'},sg);
  txt(sg,s,0,i==1?11:14,i==1?32:40,'#0B4A50');
  return sg;});
 o.fu=txt(g,'FONTI UFFICIALI',540,1470,50,'#7FF0D2');
 this.o=o;},
 update(t){const o=this.o;
 const ph=eob(seg(t,0.05,0.9));const heroY=lerp(-500,470,ph);
 const shrink=eio(seg(t,1.0,1.6));
 T(o.hero,540,lerp(heroY,400,shrink),0,lerp(1.05,0.72,shrink));
 // pill
 const pp=eob(seg(t,1.2,1.8));const tap=seg(t,1.95,2.2);const sq=1-0.12*Math.sin(tap*Math.PI);
 const done=t>2.15;
 T(o.pill,540,800,0,Math.max(0,pp)*sq*(done?1+0.05*Math.sin((t-2.15)*10)*Math.exp(-(t-2.15)*3):1));
 o.pillBg.setAttribute('fill',done?'url(#g_badge)':'url(#g_red)');
 o.pillT.textContent=done?'ISCRITTO':'ISCRIVITI';o.pillT.setAttribute('x',done?30:0);op(o.tick,done?1:0);
 // bell
 const pb=eob(seg(t,2.2,2.7));const swing=t>2.2?26*Math.exp(-1.2*(t-2.2))*Math.sin((t-2.2)*13):0;
 T(o.bell,860,690,swing,Math.max(0,pb)*1.2);
 // tap
 if(t>1.8&&t<2.5){const s=seg(t,1.8,2.5);T(o.tap,lerp(760,600,eo3(seg(t,1.8,2.1))),lerp(900,820,eo3(seg(t,1.8,2.1))),0,1);op(o.tap,1);
  o.rip.setAttribute('r',lerp(30,110,seg(t,2.05,2.5)));o.rip.setAttribute('opacity',t>2.05?1-seg(t,2.05,2.5):0);}else op(o.tap,0);
 // news card
 const nin=eo3(seg(t,2.6,3.2)),nout=eio(seg(t,3.9,4.3));
 T(o.nc,540+lerp(1000,0,nin)-nout*1000,1130,(1-nin)*6-nout*6,1);
 // seals
 [0,1,2].forEach((i,k)=>{const s0=4.15+i*0.3;const p=seg(t,s0,s0+0.25);const st=eo3(p);
  const sc=lerp(2.6,1,st)+(t>s0+0.25?0.08*Math.exp(-(t-s0-0.25)*9)*Math.sin((t-s0)*30):0);
  T(o.seal[i],[230,540,850][i],1200,lerp(-25,-6+i*6,st),p>0?sc:0);op(o.seal[i],p>0?clamp(p*3):0);});
 const fu=eob(seg(t,5.0,5.4));T(o.fu,0,0,0,1);op(o.fu,seg(t,5.0,5.3));
 },
};
