// ===== VIDEO 10 - blocchi (motore b-sync-80: tempi da testo + durata, scene >= 5 s, tutto completo entro l'80 %) =====
const OV=it=>{it.ov=1;return it;};   // sovrapposizione voluta (controllo sovrapposizioni in render.py)
const P=(s,x,y,at,fill,fs,icon,o)=>I('pill',[s,fs||34,fill||DF_,(fill===AMB)?'#5A3300':'#fff',icon,o],x,y,at);
const LIGHT='#D6F5EC';
Object.assign(BUILD,{
 pill:(g,s,fs,fill,col,icon,o)=>pillB(g,s,fs,fill,col,icon,o),
 bign:(g,top,val,sub,o)=>bigN(g,top,val,sub,o),
 card:(g,title,w,h,o)=>cardB(g,title,w,h,o),
 stamp:(g,lines,col,fs,rot)=>stampB(g,lines,col,fs,rot),
 icoc:(g,k,r,fill,icol)=>icoC(g,k,r,fill,icol),
 ava:(g,kind,r,label,lfill)=>{ava(g,kind,r);if(label){const lg=el('g',{transform:'translate(0 '+(r*1.09+36)+')'},g);pillB(lg,label,30,lfill||DF_,'#fff');}},
 cpl:(g,r,label,lfill,dx)=>{dx=dx||r*1.25;const a=el('g',{transform:'translate('+(-dx)+' 0)'},g);ava(a,'C',r);const b=el('g',{transform:'translate('+dx+' 0)'},g);ava(b,'H',r);
  if(label){const lg=el('g',{transform:'translate(0 '+(r*1.09+36)+')'},g);pillB(lg,label,30,lfill||DF_,'#fff');}},
 // scheda con icona a sinistra e righe a destra
 icard:(g,w,h,icon,lines,o)=>{o=o||{};el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:o.fill||'url(#g_paper)',filter:'url(#g_sh)'},g);
  if(o.stroke)el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'none',stroke:o.stroke,'stroke-width':6},g);
  const ir=o.ir||Math.min(70,h*0.36);const ix=-w/2+ir+34;const ig=el('g',{transform:'translate('+ix+' 0)'},g);el('circle',{r:ir,fill:o.ibg||LIGHT},ig);ico(ig,icon,ir/54,o.icol||INK);
  if(o.xbadge){const xb=el('g',{transform:'translate('+(ix+ir*0.72)+' '+(-ir*0.72)+')'},g);el('circle',{r:ir*0.34,fill:o.xbadge=='x'?RED_:GRN,stroke:'#fff','stroke-width':4},xb);ico(xb,o.xbadge,ir*0.34/42,'#fff');}
  const x0=ix+ir+26,x1=w/2-34,cx=(x0+x1)/2;const n=lines.length;const lh=o.lh||(lines[0][1]*1.32);
  lines.forEach((L,i)=>fitT(g,L[0],cx,(i-(n-1)/2)*lh+(o.dy||0),L[1],L[2]||INK,L[3]||'900',x1-x0));},
 // ----- blocco 1 -----
 b1house:(g)=>{houseB(g,440,330,150);win10(g,-150,-262,0.9);win10(g,150,-262,0.9);},
 seal67:(g)=>{el('circle',{r:128,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);el('circle',{r:128,fill:'none',stroke:AMB,'stroke-width':12},g);
  el('circle',{r:108,fill:'none',stroke:'#0B4A50','stroke-width':3,'stroke-dasharray':'6 8',opacity:.5},g);txt(g,'67',0,22,118,INK,'900');txt(g,'ANNI',0,74,36,GRN,'bold');},
 cheque:(g)=>{const w=980,h=250;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  const c=el('g',{transform:'translate(-300 0) rotate(-4)'},g);el('rect',{x:-160,y:-90,width:320,height:180,rx:16,fill:'#E9FBF5',stroke:GRN,'stroke-width':5},c);
  el('rect',{x:-160,y:-90,width:320,height:40,rx:14,fill:GRN},c);el('rect',{x:-160,y:-62,width:320,height:12,fill:GRN},c);
  [-14,16,46].forEach((y,i)=>el('rect',{x:-130,y:y,width:i==2?110:190,height:10,rx:5,fill:'#9FC9C0'},c));
  const cn=el('g',{transform:'translate(100 30)'},c);el('circle',{r:44,fill:AMB,stroke:'#fff','stroke-width':5},cn);euro(cn,0,0,0.5,'#5A3300',16);
  fitT(g,'PUÒ CHIEDERE',170,-30,46,INK,'900',500);fitT(g,"UN ASSEGNO ALL'INPS",170,36,46,GRN,'900',500);},
 cifra:(g)=>{const w=540,h=250;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'none',stroke:AMB,'stroke-width':6},g);
  const lg=el('g',{transform:'translate(-160 0)'},g);el('circle',{r:74,fill:AMB},lg);ico(lg,'lock',1.25,'#5A3300');
  txt(g,'? €',90,30,104,INK,'900');fitT(g,'UNA CIFRA',90,-82,28,GRN,'bold',280);fitT(g,'DECIDE TUTTO',90,82,30,GRN,'bold',300);},
 pens:(g)=>{cardB(g,'PENSIONE DEL MARITO',470,250,{hfs:28});const a=el('g',{transform:'translate(-140 40)'},g);ava(a,'H',52);
  [0,1,2].forEach(i=>el('rect',{x:-40,y:i*34+2,width:i==1?150:210,height:16,rx:8,fill:'#C3D3D7'},g));
  const cn=el('g',{transform:'translate(150 108)'},g);el('circle',{r:24,fill:AMB,stroke:'#fff','stroke-width':4},cn);euro(cn,0,0,0.26,'#5A3300',16);
  arrB(g,-250,-10,-325,-10,AMB,9,'14 10');},
 ex:(g,n,k)=>{cardB(g,'ESEMPIO '+n,330,170,{hfs:30,hh:58});for(let i=0;i<k;i++)goldCoin(g,-80,60-i*16,46,15,10);
  txt(g,'? €',70,64,52,AMB,'900');},
 // ----- blocco 2 -----
 plate:(g,s)=>{const t=txt(g,s,60,0,78,INK,'900');const tl=mw(t,s,78);const w=tl+300,h=160;t.setAttribute('x',(-w/2+210+tl/2).toFixed(1));t.setAttribute('y',(78*0.36).toFixed(1));
  const ins=e=>{g.insertBefore(e,t);return e;};ins(el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:'url(#g_paper)',filter:'url(#g_sh)'}));
  ins(el('rect',{x:-w/2+10,y:-h/2+10,width:w-20,height:h-20,rx:22,fill:'none',stroke:GRN,'stroke-width':4}));
  const r=el('g',{transform:'translate('+(-w/2+110)+' -6)'},g);[[-22,1],[22,-1]].forEach(([x,s])=>el('path',{d:`M${x*0.4} 30 L${x} 78 L${x*0.4+s*-8} 66 L${x*0.2} 80 Z`,fill:RED_},r));
  for(let i=0;i<16;i++){const a=i*Math.PI/8;el('circle',{cx:52*Math.cos(a),cy:52*Math.sin(a),r:12,fill:AMB},r);}el('circle',{r:50,fill:AMB,stroke:'#fff','stroke-width':5},r);ico(r,'stato',0.62,'#5A3300');},
 nocard:(g)=>{cardB(g,'NON È',640,400,{hc:RED_,hicon:'x',hicol:RED_,hfs:34});const ig=el('g',{transform:'translate(0 -40)'},g);el('circle',{r:66,fill:'#FFE3DE'},ig);ico(ig,'brief',1.05,RED_);
  fitT(g,'UNA PENSIONE',0,70,42,INK,'900',560);fitT(g,'DA CONTRIBUTI',0,124,42,INK,'900',560);},
 sicard:(g)=>{cardB(g,'È',640,400,{hc:GRN,hicon:'ok',hicol:GRN,hfs:34});const ig=el('g',{transform:'translate(-150 -70)'},g);el('circle',{r:52,fill:LIGHT},ig);ico(ig,'stato',0.9,INK);
  fitT(g,'UN AIUTO',60,-98,40,INK,'900',380);fitT(g,'DELLO STATO',60,-44,40,INK,'900',380);},
 cal26:(g)=>{const w=240,h=240;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:28,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  el('path',{d:`M${-w/2} ${-h/2+64} V${-h/2+28} Q${-w/2} ${-h/2} ${-w/2+28} ${-h/2} H${w/2-28} Q${w/2} ${-h/2} ${w/2} ${-h/2+28} V${-h/2+64} Z`,fill:'url(#g_head)'},g);
  [-60,60].forEach(x=>metalRing(g,x,-h/2-26,26,64));txt(g,'2026',0,58,74,INK,'900');},
 c13:(g)=>{const L=[];for(let i=1;i<=13;i++)L.push(String(i));coinsRow(g,13,42,100,L,[12]);const lg=el('g',{transform:'translate(0 86)'},g);pillB(lg,'13 MENSILITÀ',30,DF_,'#fff');},
 form:(g)=>{cardB(g,'DOMANDA',340,170,{hfs:30,hh:56});const p=el('g',{transform:'translate(110 46) rotate(8)'},g);ico(p,'pen',0.85,INK);
  [0,1,2].forEach(i=>el('rect',{x:-130,y:-8+i*28,width:i==2?110:170,height:12,rx:6,fill:'#C3D3D7'},g));},
 flow:(g)=>{const w=700,h=170;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:24,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  const a=el('g',{transform:'translate(-280 -6)'},g);el('circle',{r:46,fill:LIGHT},a);ico(a,'cal',0.85,INK);
  fitT(g,'DATA DELLA',-110,-22,28,INK,'900',190);fitT(g,'DOMANDA',-110,18,28,INK,'900',190);
  arrB(g,10,0,74,0,AMB,10);const b=el('g',{transform:'translate(132 -6)'},g);el('circle',{r:44,fill:AMB,stroke:'#fff','stroke-width':4},b);euro(b,0,0,0.5,'#5A3300',16);
  fitT(g,'PRIMO',262,-22,28,GRN,'900',170);fitT(g,'PAGAMENTO',262,18,28,GRN,'900',170);},
 // ----- blocco 3 -----
 req:(g,n,icon,lines,big)=>{const w=400,h=460;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:28,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  const nb=el('g',{transform:'translate(-148 -180)'},g);el('circle',{r:34,fill:AMB,stroke:'#fff','stroke-width':4},nb);txt(nb,String(n),0,15,40,'#5A3300','900');
  const ig=el('g',{transform:'translate(0 -118)'},g);el('circle',{r:64,fill:LIGHT},ig);ico(ig,icon,1.08,INK);
  lines.forEach((L,i)=>fitT(g,L,0,-16+i*43,(big&&i==0)?52:32,INK,'900',w-70));},
 rsub:(g,lines)=>{const w=344,h=114;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:18,fill:LIGHT,stroke:GRN,'stroke-width':4},g);
  lines.forEach((L,i)=>fitT(g,L,0,(i-1)*33,i==0?26:24,i==0?GRN:INK,'bold',w-40));},
 hl4:(g)=>{el('rect',{x:-216,y:-246,width:432,height:492,rx:34,fill:'none',stroke:AMB,'stroke-width':9},g);
  const m=el('g',{transform:'translate(176 -206)'},g);el('circle',{r:48,fill:AMB,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},m);ico(m,'lens',0.95,'#5A3300');
  const lg=el('g',{transform:'translate(-50 270)'},g);pillB(lg,'LA PARTE DA CAPIRE BENE',28,AMB,'#5A3300','lens');},
 // ----- blocco 4 -----
 b4axis:(g)=>{el('line',{x1:0,y1:0,x2:0,y2:-512,stroke:'#BFFBEA','stroke-width':6,'stroke-linecap':'round'},g);el('path',{d:'M-16 -506 L0 -536 L16 -506 Z',fill:'#BFFBEA'},g);
  [-250,-500].forEach(y=>el('line',{x1:-14,y1:y,x2:14,y2:y,stroke:'#BFFBEA','stroke-width':5},g));el('line',{x1:-30,y1:0,x2:1060,y2:0,stroke:'#BFFBEA','stroke-width':5,opacity:.6},g);
  const lg=el('g',{transform:'translate(0 -566)'},g);pillB(lg,"REDDITO ALL'ANNO",26,DF_,'#fff');},
 b4hs:(g)=>{houseB(g,360,250,100,{chim:false});const a=el('g',{transform:'translate(0 -62)'},g);ava(a,'C',46);const lg=el('g',{transform:'translate(0 38)'},g);pillB(lg,'NON SPOSATA',28,DF_,'#fff');},
 b4hd:(g)=>{houseB(g,400,500,100);el('line',{x1:-192,y1:-250,x2:192,y2:-250,stroke:'#9FB4B9','stroke-width':4,'stroke-dasharray':'12 9'},g);
  const a=el('g',{transform:'translate(-62 -62)'},g);ava(a,'C',46);const b=el('g',{transform:'translate(62 -62)'},g);ava(b,'H',46);const lg=el('g',{transform:'translate(0 38)'},g);pillB(lg,'SPOSATA',28,DF_,'#fff');},
 b4v:(g,l1,l2,w)=>{w=w||310;el('rect',{x:-w/2,y:-49,width:w,height:98,rx:18,fill:LIGHT,stroke:GRN,'stroke-width':4},g);fitT(g,l1,0,-24,24,GRN,'bold',w-40);fitT(g,l2,0,18,44,INK,'900',w-40);},
 b4mar:(g)=>{const w=300,h=92;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:18,fill:AMB,stroke:'#fff','stroke-width':4},g);fitT(g,'+ REDDITO',0,-20,30,'#5A3300','900',w-40);fitT(g,'DEL MARITO',0,20,30,'#5A3300','900',w-40);},
 b4x2:(g)=>{const c=el('g',{transform:'translate(0 -72)'},g);el('circle',{r:80,fill:AMB,stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},c);txt(c,'× 2',0,24,66,'#5A3300','900');
  const lg=el('g',{transform:'translate(0 70)'},g);pillB(lg,'IL TETTO RADDOPPIA',27,DF_,'#fff');},
 b4r1:(g)=>{const a=el('g',{transform:'translate(-820 0)'},g);ava(a,'H',54);const lg=el('g',{transform:'translate(-525 0)'},g);pillB(lg,'LA SUA PENSIONE',30,DF_,'#fff');
  el('rect',{x:-320,y:-48,width:1160,height:96,rx:24,fill:'url(#g_badge)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  for(let i=0;i<10;i++){const c=el('g',{transform:'translate('+(-260+i*116)+' 0)'},g);el('circle',{r:22,fill:'#fff',opacity:.22},c);euro(c,0,0,0.22,'#fff',16).setAttribute('opacity','.5');}},
 b4r2:(g)=>{const lg=el('g',{transform:'translate(-525 0)'},g);pillB(lg,'AL NETTO',30,GRN,'#fff');
  el('rect',{x:-320,y:-48,width:540,height:96,rx:24,fill:GRN,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  const ck=el('g',{transform:'translate(-250 0)'},g);el('circle',{r:26,fill:'#fff'},ck);ico(ck,'ok',0.6,GRN);fitT(g,'SI CONTA QUESTA',-30,0,30,'#fff','900',360);
  el('line',{x1:222,y1:-60,x2:222,y2:-142,stroke:'#fff','stroke-width':4,'stroke-dasharray':'10 8',opacity:.8},g);},
 b4cut:(g,s,col,w,tc)=>{el('rect',{x:-w/2,y:-48,width:w,height:96,rx:24,fill:col,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);fitT(g,s,0,0,32,tc||'#fff','900',w-44);
  el('line',{x1:w/2+4,y1:-60,x2:w/2+4,y2:-142,stroke:'#fff','stroke-width':4,'stroke-dasharray':'10 8',opacity:.8},g);},
 // ----- blocco 5 -----
 b5red:(g)=>{el('rect',{x:-262,y:-96,width:524,height:190,rx:20,fill:'url(#g_red)',opacity:.55},g);el('rect',{x:-262,y:-96,width:524,height:190,rx:20,fill:'none',stroke:'#FF8A75','stroke-width':4,'stroke-dasharray':'14 10'},g);},
 b5house:(g)=>{houseB(g,440,460,95,{over:26});el('line',{x1:-214,y1:-230,x2:214,y2:-230,stroke:'#9FB4B9','stroke-width':4,'stroke-dasharray':'12 9'},g);
  [[-120,-115],[120,-115],[-120,-345],[120,-345]].forEach(([x,y])=>win10(g,x,y,0.8));},
 b5fl:(g,i,lines,fill,tc)=>{el('rect',{x:-216,y:-112,width:432,height:224,rx:i?6:10,fill:fill,opacity:.94},g);const n=lines.length;
  lines.forEach((L,k)=>fitT(g,L,0,(i?-52:0)+(k-(n-1)/2)*44,36,tc||'#fff','900',390));},
 b5gap:(g)=>{el('line',{x1:-214,y1:62,x2:214,y2:62,stroke:'#0B4A50','stroke-width':5,'stroke-dasharray':'12 8'},g);
  const lg=el('g',{transform:'translate(-120 62)'},g);pillB(lg,'LA COPPIA',22,DF_,'#fff');arrB(g,165,58,165,-106,'#0B4A50',9);},
 b5card:(g,l1,l2,fill,tc,w)=>{w=w||600;const h=128;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:24,fill:fill,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  fitT(g,l1,0,-24,34,tc,'900',w-70);fitT(g,l2,0,26,28,tc,'bold',w-70);},
 // ----- blocco 6 -----
 pcard:(g,kind,head,val,sub,w)=>{w=w||640;const h=360;cardB(g,head,w,h,{hfs:34});const a=el('g',{transform:'translate('+(-w/2+125)+' 34)'},g);ava(a,kind,78);
  fitT(g,val,95,6,84,INK,'900',w-330);fitT(g,sub,95,92,28,GRN,'bold',w-310);},
 b6house:(g)=>{houseB(g,380,500,95,{over:18});el('line',{x1:-182,y1:-250,x2:182,y2:-250,stroke:'#9FB4B9','stroke-width':4,'stroke-dasharray':'12 9'},g);
  [[-250,'7.101 €'],[-500,'14.202 €']].forEach(([y,s])=>{el('line',{x1:-214,y1:y,x2:-192,y2:y,stroke:'#BFFBEA','stroke-width':5},g);const lg=el('g',{transform:'translate(-318 '+y+')'},g);pillB(lg,s,26,DF_,'#fff');});},
 b6fill:(g)=>{const hh=320;el('rect',{x:-184,y:-hh,width:368,height:hh-6,rx:8,fill:'url(#g_badge)',opacity:.95},g);el('line',{x1:-184,y1:-hh,x2:184,y2:-hh,stroke:'#fff','stroke-width':5},g);
  fitT(g,'LA COPPIA',0,-200,30,'#fff','bold',330);fitT(g,'9.100 €',0,-140,58,'#fff','900',330);},
 b6gap:(g)=>{el('rect',{x:-184,y:-494,width:368,height:170,rx:6,fill:AMB,opacity:.9},g);
  el('path',{d:'M200 -496 H220 V-324 H200',fill:'none',stroke:AMB,'stroke-width':7},g);
  const c=el('g',{transform:'translate(440 -410)'},g);const w=320,h=110;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:20,fill:'url(#g_paper)',filter:'url(#g_sh2)'},c);
  el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:20,fill:'none',stroke:AMB,'stroke-width':5},c);fitT(c,'MANCANO',0,-26,26,GRN,'bold',w-40);fitT(c,'5.102,24 €',0,18,46,INK,'900',w-40);
  arrB(g,226,-410,272,-410,AMB,7);},
 b6res:(g)=>{cardB(g,'DIVISO IN 13 RATE',540,380,{hfs:30});fitT(g,'5.102,24 € ÷ 13',0,-72,40,INK,'900',470);},
 b6val:(g)=>{const w=460,h=170;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:22,fill:'url(#g_badge)',stroke:'#fff','stroke-width':5},g);fitT(g,'392,48 €',0,-16,78,'#fff','900',w-50);fitT(g,'AL MESE',0,52,30,'#fff','bold',w-50);},
 // ----- blocco 7 -----
 lui7:(g,val,sub)=>{cardB(g,'LUI',440,260,{hfs:32});const a=el('g',{transform:'translate(-130 34)'},g);ava(a,'H',58);fitT(g,val,72,22,56,INK,'900',250);fitT(g,sub,72,78,24,GRN,'bold',250);},
 bar7:(g,v)=>{const W=1140,x0=-W/2;const xl=x0+W*v/14202.24;
  el('rect',{x:x0,y:-45,width:W,height:90,rx:22,fill:'#06303A',stroke:'#7FF0D2','stroke-width':3,opacity:.9},g);
  el('rect',{x:x0+6,y:-39,width:xl-x0-8,height:78,rx:18,fill:'url(#g_badge)'},g);fitT(g,'LUI '+v.toLocaleString('it-IT')+' €',(x0+xl)/2,0,34,'#fff','900',xl-x0-60);
  el('line',{x1:W/2,y1:-70,x2:W/2,y2:70,stroke:'#fff','stroke-width':6},g);el('path',{d:`M${W/2-34} -70 L${W/2} -100 L${W/2+34} -70 Z`,fill:'url(#g_red)',stroke:'#fff','stroke-width':4},g);
  const lg=el('g',{transform:'translate('+(W/2-210)+' -112)'},g);pillB(lg,'TETTO 14.202,24 €',26,DF_,'#fff');},
 gap7:(g,v,lei)=>{const W=1140,x0=-W/2;const xl=x0+W*v/14202.24;el('rect',{x:xl+2,y:-39,width:W/2-xl-8,height:78,rx:12,fill:AMB},g);
  el('line',{x1:(xl+W/2)/2,y1:44,x2:(xl+W/2)/2,y2:86,stroke:AMB,'stroke-width':5},g);const lg=el('g',{transform:'translate('+(W/2-204)+' 116)'},g);pillB(lg,'A LEI: '+lei,30,AMB,'#5A3300');},
 // ----- blocco 8 -----
 b8lock:(g)=>{cardB(g,'LA CIFRA CHE DECIDE TUTTO',640,440,{hfs:30});const lg=el('g',{transform:'translate(0 -66)'},g);el('circle',{r:72,fill:AMB},lg);ico(lg,'unlock',1.2,'#5A3300');},
 b8val:(g)=>{const w=560,h=150;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:22,fill:LIGHT,stroke:GRN,'stroke-width':5},g);fitT(g,'14.202,24 €',0,-14,72,INK,'900',w-50);fitT(g,"TETTO DI COPPIA, ALL'ANNO",0,48,26,GRN,'bold',w-50);},
 b8bar:(g)=>{const a=el('g',{transform:'translate(-800 0)'},g);ava(a,'H',52);
  el('rect',{x:-700,y:-46,width:1220,height:92,rx:22,fill:'url(#g_badge)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);fitT(g,'PENSIONE NETTA DI TUO MARITO',-90,0,32,'#fff','900',1100);
  el('line',{x1:520,y1:-72,x2:520,y2:72,stroke:'#fff','stroke-width':6},g);el('path',{d:'M486 -72 L520 -102 L554 -72 Z',fill:'url(#g_red)',stroke:'#fff','stroke-width':4},g);
  const c=el('g',{transform:'translate(690 0)'},g);const w=270,h=96;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:18,fill:'url(#g_paper)',filter:'url(#g_sh3)'},c);fitT(c,'TETTO',0,-22,24,GRN,'bold',w-40);fitT(c,'14.202,24 €',0,18,36,INK,'900',w-40);},
 b8tu:(g)=>{const a=el('g',{transform:'translate(-440 0)'},g);ava(a,'C',52);const lg=el('g',{transform:'translate(-70 0)'},g);pillB(lg,'TU: NESSUN ALTRO REDDITO',30,DF_,'#fff');},
 pm8:(g,s,icon,fill,w)=>{w=w||480;const h=120;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  const ig=el('g',{transform:'translate('+(-w/2+64)+' 0)'},g);el('circle',{r:42,fill:fill},ig);ico(ig,icon,0.78,'#fff');fitT(g,s,38,0,42,INK,'900',w-160);},
 eq8:(g)=>{el('circle',{r:30,fill:AMB,stroke:'#fff','stroke-width':5},g);el('rect',{x:-15,y:-10,width:30,height:6,rx:3,fill:'#5A3300'},g);el('rect',{x:-15,y:4,width:30,height:6,rx:3,fill:'#5A3300'},g);},
 // ----- blocco 9 -----
 btn10:(g,s)=>{const w=470,h=132;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:66,fill:'url(#g_red)',stroke:'#fff','stroke-width':7,filter:'url(#g_sh)'},g);
  const pg=el('g',{transform:'translate('+(-w/2+78)+' 0)'},g);el('circle',{r:40,fill:'#fff'},pg);el('path',{d:'M-12 -20 L22 0 L-12 20 Z',fill:RED_},pg);fitT(g,s,50,0,58,'#fff','900',w-190);},
 // ----- blocco 10 -----
 b10lim:(g)=>{cardB(g,'IL TUO LIMITE',420,260,{hfs:30});const h=el('g',{transform:'translate(-120 40)'},g);el('circle',{r:56,fill:LIGHT},h);ico(h,'house',1.0,INK);
  fitT(g,'7.101,12 €',70,30,50,INK,'900',230);fitT(g,"ALL'ANNO",70,84,26,GRN,'bold',230);},
 sheet:(g)=>{cardB(g,'IL CONTO',900,520,{hfs:32,hicon:'calc'});
  el('line',{x1:-410,y1:-62,x2:410,y2:-62,stroke:'#C3D3D7','stroke-width':3,'stroke-dasharray':'8 8'},g);
  txt(g,'IL TUO LIMITE',-400,-110,38,INK,'bold','start');txt(g,'7.101,12 €',400,-110,44,INK,'900','end');},
 srow:(g,l,v,col)=>{txt(g,l,-400,-6,38,col||INK,'bold','start');txt(g,v,400,-6,44,col||INK,'900','end');
  el('line',{x1:-410,y1:40,x2:410,y2:40,stroke:'#0B4A50','stroke-width':4},g);el('line',{x1:-410,y1:50,x2:410,y2:50,stroke:'#0B4A50','stroke-width':4},g);},
 stot:(g,l,v)=>{el('rect',{x:-420,y:-48,width:840,height:96,rx:18,fill:LIGHT,stroke:GRN,'stroke-width':4},g);txt(g,l,-396,15,40,GRN,'900','start');txt(g,v,396,17,50,GRN,'900','end');},
 // ----- blocco 11 -----
 ncard:(g,icon,lines,ok)=>{const w=480,h=380;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:28,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:28,fill:'none',stroke:ok?GRN:RED_,'stroke-width':5,opacity:.8},g);
  const ig=el('g',{transform:'translate(0 -66)'},g);el('circle',{r:72,fill:ok?LIGHT:'#FFE3DE'},ig);ico(ig,icon,1.15,INK);
  const xb=el('g',{transform:'translate(168 -140)'},g);el('circle',{r:30,fill:ok?GRN:RED_,stroke:'#fff','stroke-width':4},xb);ico(xb,ok?'ok':'x',0.62,'#fff');
  lines.forEach((L,i)=>fitT(g,L,0,64+i*46,34,INK,'900',w-70));},
 ytile:(g,icon,lines)=>{const w=400,h=232;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'none',stroke:GRN,'stroke-width':4,opacity:.8},g);
  const ig=el('g',{transform:'translate(0 -52)'},g);el('circle',{r:48,fill:LIGHT},ig);ico(ig,icon,0.82,INK);
  const xb=el('g',{transform:'translate(158 -82)'},g);el('circle',{r:22,fill:GRN,stroke:'#fff','stroke-width':3},xb);ico(xb,'ok',0.45,'#fff');
  lines.forEach((L,i)=>fitT(g,L,0,i==0?36:80,i==0?32:22,i==0?INK:GRN,'900',w-60));},
 b11pair:(g)=>{[[-60,'ok',GRN],[60,'x',RED_]].forEach(([x,k,c])=>{const b=el('g',{transform:'translate('+x+' 0)'},g);el('circle',{r:40,fill:c,stroke:'#fff','stroke-width':5,filter:'url(#g_sh3)'},b);ico(b,k,0.8,'#fff');});},
 // ----- blocco 12 -----
 b12axis:(g)=>{el('line',{x1:-740,y1:0,x2:740,y2:0,stroke:'#BFFBEA','stroke-width':6,'stroke-linecap':'round',opacity:.85},g);
  for(let a=16;a<=67;a+=1){const x=-600+(a-16)*1200/49;if(a%5==0)el('line',{x1:x,y1:-10,x2:x,y2:10,stroke:'#BFFBEA','stroke-width':3,opacity:.6},g);}
  const m=el('g',{transform:'translate(600 0)'},g);el('circle',{r:40,fill:AMB,stroke:'#fff','stroke-width':5,filter:'url(#g_sh3)'},m);txt(m,'65',0,12,32,'#5A3300','900');
  const lg=el('g',{transform:'translate(600 76)'},g);pillB(lg,'FINO AI 65 ANNI',28,DF_,'#fff');},
 b12range:(g)=>{el('rect',{x:-600,y:-14,width:1200,height:28,rx:14,fill:'url(#g_badge)',stroke:'#fff','stroke-width':4},g);
  const m=el('g',{transform:'translate(-600 0)'},g);el('circle',{r:40,fill:AMB,stroke:'#fff','stroke-width':5,filter:'url(#g_sh3)'},m);txt(m,'16',0,12,32,'#5A3300','900');
  const lg=el('g',{transform:'translate(-600 76)'},g);pillB(lg,'DAI 16 ANNI',28,DF_,'#fff');const l2=el('g',{transform:'translate(0 76)'},g);pillB(l2,'PUOI ISCRIVERTI',28,GRN,'#fff','ok');},
 b12card:(g)=>{cardB(g,'FONDO CASALINGHE INPS',640,310,{hfs:30});const a=el('g',{transform:'translate(-80 10)'},g);ava(a,'C',62);},
 b12men:(g)=>{const a=el('g',{transform:'translate(80 10)'},g);ava(a,'H',62);const lg=el('g',{transform:'translate(0 108)'},g);pillB(lg,'APERTO ANCHE AGLI UOMINI',26,GRN,'#fff');},
 // ----- blocco 13 -----
 b13five:(g)=>{const L=['1','2','3','4','5'];const c=el('g',{transform:'translate(-300 0)'},g);coinsRow(c,5,34,84,L);const lg=el('g',{transform:'translate(200 0)'},g);pillB(lg,'ALMENO 5 ANNI DI CONTRIBUTI',30,DF_,'#fff');},
 b13p:(g,head,fill)=>{cardB(g,head,680,390,{hfs:40,hh:76,hc:fill});},
 b13cond:(g)=>{fitT(g,'SE È ALMENO IL 20% PIÙ ALTA',0,-20,32,INK,'900',600);fitT(g,"DELL'ASSEGNO SOCIALE",0,24,32,INK,'900',600);},
 b13any:(g)=>{const ig=el('g',{transform:'translate(-200 0)'},g);el('circle',{r:58,fill:LIGHT},ig);ico(ig,'ok',1.1,GRN);fitT(g,'QUALUNQUE SIA',60,-28,40,INK,'900',380);fitT(g,"L'IMPORTO",60,28,40,INK,'900',380);},
 b13calc:(g)=>{const c=el('g',{transform:'translate(-360 40)'},g);for(let i=0;i<3;i++)goldCoin(c,0,-i*22,70,22,14);
  const lg=el('g',{transform:'translate(-360 -80)'},g);pillB(lg,'QUELLO CHE VERSI',28,DF_,'#fff');arrB(g,-180,0,-30,0,AMB,12);
  const b=el('g',{transform:'translate(260 0)'},g);el('rect',{x:-200,y:-40,width:400,height:80,rx:20,fill:'#06303A',stroke:'#7FF0D2','stroke-width':3},b);
  el('rect',{x:-194,y:-34,width:96,height:68,rx:16,fill:'url(#g_badge)'},b);const l3=el('g',{transform:'translate(0 -80)'},b);pillB(l3,'LA PENSIONE DEL FONDO',28,GRN,'#fff');},
 // ----- blocco 14 -----
 ch:(g,head,hicon,icon,lines)=>{cardB(g,head,700,440,{hfs:34,hicon:hicon});if(icon){const ig=el('g',{transform:'translate(0 -40)'},g);el('circle',{r:76,fill:LIGHT},ig);ico(ig,icon,1.25,INK);}
  (lines||[]).forEach((L,i)=>fitT(g,L,0,76+i*46,36,INK,'900',620));},
 telrow:(g,num,sub)=>{fitT(g,num,0,-14,66,INK,'900',600);fitT(g,sub,0,40,26,GRN,'bold',600);},
 b14time:(g)=>{const mk=(x,head,icon,l1,l2,hc)=>{const c=el('g',{transform:'translate('+x+' 0)'},g);cardB(c,head,330,290,{hfs:26,hc:hc});
   const ig=el('g',{transform:'translate(0 -6)'},c);el('circle',{r:52,fill:LIGHT},ig);ico(ig,icon,0.95,INK);fitT(c,l1,0,82,28,INK,'900',280);if(l2)fitT(c,l2,0,116,22,GRN,'bold',280);};
  mk(-260,'MESE DELLA DOMANDA','pen','DOMANDA',null);arrB(g,-80,0,80,0,AMB,12);mk(260,'MESE DOPO','coin','DAL 1° GIORNO',null,GRN);},
 // ----- blocco 15 -----
 wrow:(g,n,icon,s,sub)=>{const w=1640,h=170;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:28,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2,y:-h/2,width:16,height:h,rx:8,fill:AMB},g);
  const nb=el('g',{transform:'translate(-752 0)'},g);el('circle',{r:38,fill:AMB,stroke:'#fff','stroke-width':4},nb);txt(nb,String(n),0,16,44,'#5A3300','900');
  const ig=el('g',{transform:'translate(-640 0)'},g);el('circle',{r:52,fill:LIGHT},ig);ico(ig,icon,0.92,INK);
  txt(g,s,-560,sub?-14:14,36,INK,'900','start');if(sub)txt(g,sub,-560,40,28,GRN,'bold','start');},
 wsub:(g,s,fill,tc)=>{pillB(g,s,28,fill,tc||'#fff');},
 // ----- blocco 16 -----
 dbox:(g)=>{const w=1640,h=150;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'#06303A',stroke:'#7FF0D2','stroke-width':3,filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2+30,y:-h/2,width:w-60,height:6,rx:3,fill:AMB},g);
  fitT(g,'PER IL TUO CASO VERIFICA SU INPS.IT O CHIEDI A UN PATRONATO',0,-24,32,'#fff','bold',w-80);fitT(g,"CANALE SOLO INFORMATIVO, NON AFFILIATO ALL'INPS",0,28,30,'#7FF0D2','bold',w-80);},
});
// ======================= BLOCCHI =======================
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONE ALLE CASALINGHE',cap:'ANCHE CHI NON HA MAI LAVORATO PUÒ CHIEDERE UN ASSEGNO',items:[
  I('b1house',[],480,825,'Pensione alle casalinghe'),
  OV(I('ava',['C',100,'CASALINGA',DF_],480,628,'casalinghe')),
  I('seal67',[],1000,330,'sessantasette'),
  I('icard',[620,210,'brief',[['ANCHE CHI NON HA',38],['MAI LAVORATO',38,GRN]],{xbadge:'x',ibg:'#FFE3DE'}],1490,330,'anche chi non ha mai'),
  I('cheque',[],1240,650,'può chiedere')]},
 {at:'Ma per chi è sposata',top:'LA CIFRA CHE DECIDE TUTTO',cap:'SOPRA QUELLA CIFRA, A LEI NON ARRIVA NIENTE',items:[
  I('cpl',[78,'SPOSATA',DF_],330,300,'per chi è sposata'),
  I('cifra',[],960,320,'una cifra'),
  I('pens',[],1585,320,'pensione del marito'),
  I('pill',['SOPRA QUELLA CIFRA, A LEI: 0 €',36,RF_,'#fff','up',{rx:24,h:84,icol:RED_}],1340,575,'Sopra quella cifra'),
  P('TE LA DICIAMO TRA POCO',400,575,'Te la diciamo',AMB,32,'clock'),
  I('ex',[1,3],560,772,'tre esempi'),I('ex',[2,4],930,772,['tre esempi',0.5]),I('ex',[3,5],1300,772,['con pensioni diverse',0]),
  I('stamp',[['CALCOLATI','AL CENTESIMO'],GRN,38,-6],1665,772,'calcolati al centesimo')]},
]);
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SI CHIAMA ASSEGNO SOCIALE',cap:'NON È UNA PENSIONE DA CONTRIBUTI: È UN AIUTO DELLO STATO',items:[
  I('plate',['ASSEGNO SOCIALE'],960,250,'Si chiama assegno sociale'),
  I('nocard',[],520,610,'Non è una pensione'),
  I('sicard',[],1400,610,'è un aiuto dello Stato'),
  OV(P('PER CHI HA REDDITI BASSI',1400,680,'per chi ha redditi bassi',GF_,32,'down',{icol:GRN})),
  OV(P("LO PAGA L'INPS",1400,762,"lo paga l'Inps",DF_,32,'office'))]},
 {at:'Nel duemilaventisei',top:'QUANTO VALE NEL 2026',cap:'FINO A 546,24 € AL MESE PER 13 MENSILITÀ, SENZA TASSE',items:[
  I('cal26',[],250,310,'Nel duemilaventisei'),
  I('bign',['FINO A','546,24 €','AL MESE',{fs:108,minw:640}],800,305,'vale fino a'),
  I('stamp',[['NIENTE TASSE','DA PAGARE'],GRN,42,-5],1545,305,'non ci sono tasse'),
  I('c13',[],960,518,'per tredici mensilità'),
  P('NON ARRIVA DA SOLO',330,772,'Ma non arriva da solo',RF_,34,'warn',{icol:RED_}),
  I('form',[],860,772,'bisogna fare domanda'),
  I('flow',[],1450,772,'da quella data')]},
]);
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CHI PUÒ AVERLO: REGOLE 2026',cap:'SERVONO QUATTRO COSE. IL LIMITE È LA PARTE DA CAPIRE BENE',items:[
  P('CHI PUÒ AVERLO?',640,210,'Chi può averlo',AMB,36,'q'),
  P('SERVONO 4 COSE',1260,210,'servono quattro cose',DF_,36,'ok',{icol:GRN}),
  I('req',[1,'cal',['67 ANNI','COMPIUTI'],true],330,532,'Sessantasette anni'),
  I('req',[2,'it',['VIVERE DAVVERO','IN ITALIA']],750,532,'Vivere davvero'),
  OV(I('rsub',[['ALMENO 10 ANNI','SOGGIORNO LEGALE','E CONTINUATIVO']],750,690,'almeno dieci anni')),
  I('req',[3,'id',['CITTADINANZA','ITALIANA O','EQUIPARATA']],1170,532,'La cittadinanza'),
  OV(I('rsub',[['ES. PERMESSO DI','SOGGIORNO DI','LUNGO PERIODO']],1170,690,'come il permesso')),
  I('req',[4,'ruler',['REDDITI SOTTO','UN LIMITE','PRECISO']],1590,532,'E redditi sotto'),
  OV(I('hl4',[],1590,532,'È proprio il limite'))]},
]);
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'I LIMITI SONO DUE',cap:'IL TETTO RADDOPPIA: DA 7.101,12 € A 14.202,24 € ALL\'ANNO',items:[
  P('DUE LIMITI',640,205,'I limiti sono due',AMB,36),
  I('b4hs',[],620,790,'Se non sei sposata'),
  OV(I('b4v',['MENO DI','7.101,12 €'],620,600,'meno di settemila')),
  OV(I('b4axis',[],250,790,"di reddito all'anno")),
  I('b4hd',[],1110,790,'Se sei sposata'),
  OV(I('b4mar',[],1110,478,'si aggiunge anche')),
  I('b4x2',[],1605,420,'il tetto raddoppia'),
  OV(I('b4v',['TETTO DI COPPIA','14.202,24 €',330],1110,352,'quattordicimila'))]},
 {at:'Attenzione',top:'LA SUA PENSIONE SI CONTA AL NETTO',cap:'AL NETTO DELLE TASSE: TOGLIENDO IRPEF E ADDIZIONALI',items:[
  P('ATTENZIONE',960,225,'Attenzione',RF_,38,'warn',{icol:RED_}),
  I('b4r1',[],960,400,'la sua pensione'),
  I('b4r2',[],960,600,'al netto delle tasse'),
  I('b4cut',['− IRPEF',RED_,260],1320,600,'togliendo Irpef'),
  I('b4cut',['− ADDIZIONALI','#E39A1C',340,'#4A2600'],1630,600,'e addizionali')]},
]);
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PER UNA COPPIA FUNZIONA COSÌ',cap:'SE SIETE NEL MEZZO, SPETTA QUELLO CHE MANCA PER ARRIVARE AL TETTO',items:[
  OV(I('b5red',[],870,247,'Se lo superate')),
  I('b5house',[],870,800,'Per una coppia'),
  I('cpl',[60,'COPPIA',DF_,74],300,540,['Per una coppia',0.45]),
  OV(I('b5fl',[0,['SOTTO 7.101 €'],'url(#g_badge)'],870,685,'non arrivate a')),
  I('pill',['ASSEGNO INTERO',38,GF_,'#fff','ok',{icol:GRN}],1460,685,"l'assegno è intero"),
  OV(I('b5fl',[1,['TRA 7.101 €','E 14.202 €'],AMB,'#5A3300'],870,455,'tra settemilacentouno')),
  I('b5card',['NE SPETTA UNA PARTE:','QUELLO CHE MANCA AL TETTO',AMB,'#5A3300'],1460,455,'ne spetta una parte'),
  OV(I('b5gap',[],870,455,'quello che manca')),
  P('SOPRA 14.202 €',400,247,'Se lo superate',RF_,32),
  I('pill',['NON SPETTA',40,RF_,'#fff','x',{icol:RED_}],1460,247,"l'assegno non spetta"),
  P('ADESSO I NUMERI VERI',330,800,'Adesso passiamo',DF_,30,'calc')]},
]);
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PRIMO ESEMPIO',cap:'LEI NON HA REDDITI. LUI: 9.100 € DI PENSIONE NETTA IN UN ANNO',items:[
  P('ESEMPIO 1',960,215,'Primo esempio',AMB,36),
  I('pcard',['C','LEI','0 €','NESSUN REDDITO'],540,500,'Lei non ha redditi'),
  I('pcard',['H','LUI','9.100 €','NETTI IN UN ANNO'],1380,500,'La pensione di lui'),
  P('CIRCA 700 € AL MESE, SU 13 RATE',1380,772,'circa settecento',DF_,32,'coin')]},
 {at:'La coppia sta',top:'QUANTO SPETTA A LEI',cap:'MANCANO 5.102,24 € PER ARRIVARE AL TETTO: È L\'ASSEGNO DI LEI',items:[
  I('b6house',[],520,830,'La coppia sta'),
  OV(I('b6fill',[],520,830,'tra le due soglie')),
  OV(I('b6gap',[],520,830,'mancano cinquemila')),
  P("= L'ASSEGNO DI LEI",980,530,"è l'assegno di lei",AMB,32),
  I('b6res',[],1525,560,'Diviso in tredici rate'),
  OV(I('b6val',[],1525,620,'trecentonovantadue'))]},
]);
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SECONDO ESEMPIO',cap:'LUI: 11.700 € NETTI L\'ANNO. A LEI: 192,48 € A RATA',items:[
  I('lui7',['11.700 €',"NETTI L'ANNO"],330,330,'lui prende'),
  I('bar7',[11700],1210,360,'euro netti'),
  P('CIRCA 900 € AL MESE',330,525,'circa novecento',DF_,30,'coin'),
  OV(I('gap7',[11700,'2.502,24 €'],1210,360,'spettano duemila')),
  I('bign',['2.502,24 € ÷ 13','192,48 €','A RATA',{fs:92,fill:GF_,minw:520,tfs:28,sfs:30}],1100,700,'centonovantadue')]},
 {at:'Terzo esempio',top:'TERZO ESEMPIO',cap:'LUI: 13.000 € NETTI L\'ANNO. A LEI: 92,48 € A RATA',items:[
  I('lui7',['13.000 €',"NETTI L'ANNO"],330,330,'lui arriva a'),
  I('bar7',[13000],1210,360,'tredicimila'),
  P('CIRCA 1.000 € AL MESE',330,525,'circa mille al mese',DF_,30,'coin'),
  OV(I('gap7',[13000,'1.202,24 €'],1210,360,'spettano milleduecento')),
  I('bign',['1.202,24 € ÷ 13','92,48 €','A RATA',{fs:92,fill:GF_,minw:520,tfs:28,sfs:30}],1100,700,'ventiquattro: novantadue')]},
]);
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ECCO LA CIFRA PROMESSA',cap:'14.202,24 € L\'ANNO: SU 13 MENSILITÀ, CIRCA 1.092 € AL MESE',items:[
  I('b8lock',[],520,480,'Ed ecco la cifra'),
  OV(I('b8val',[],520,590,'Il tetto della coppia')),
  P('÷ 13 MENSILITÀ',1340,300,'su tredici mensilità',DF_,38),
  I('bign',['CIRCA','1.092 €','OGNI MESE',{fs:116,fill:GF_,minw:580}],1340,560,'circa mille e novantadue')]},
 {at:'Se la pensione netta',top:'SE LUI ARRIVA AL TETTO',cap:'OGNI EURO IN PIÙ CHE PRENDE LUI È UN EURO IN MENO PER TE',items:[
  I('b8bar',[],960,300,'Se la pensione netta'),
  I('b8tu',[],600,470,'e tu non hai altri'),
  I('stamp',[['IL TUO ASSEGNO','È ZERO'],RED_,44,-5],1265,470,'il tuo assegno è zero'),
  P('NELLA FASCIA DI MEZZO: UNA REGOLA SEMPLICE',960,636,'Nella fascia di mezzo',AMB,30,'bulb'),
  I('pm8',['+1 € A LUI','up',GRN],680,790,'ogni euro in più'),
  I('pm8',['−1 € A TE','down',RED_],1240,790,'un euro in meno'),
  OV(I('eq8',[],960,790,['un euro in meno',-0.3]))]},
]);
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SE IL CONTO TI HA CHIARITO LE IDEE',cap:'ISCRIVITI AL CANALE: È GRATIS, E PER NOI OGNI NUOVO ISCRITTO CONTA',items:[
  I('icoc',['bulb',72,AMB,'#5A3300'],290,330,'chiarito le idee'),
  I('btn10',['ISCRIVITI'],720,330,'iscriviti al canale'),
  P('È GRATIS',720,488,'è gratis',GF_,38,'ok',{icol:GRN}),
  I('icard',[660,236,'calc',[['CI AIUTA A FARE CALCOLI',32],['COME QUESTI, CON I',32],['DATI UFFICIALI',32,GRN]],{lh:44}],1400,330,'ci aiuta a continuare'),
  I('icard',[660,170,'people',[['PER NOI OGNI NUOVO ISCRITTO',30],['CONTA DAVVERO',40,GRN]],{lh:50,ir:56}],1400,600,'Per noi ogni nuovo'),
  P('E RESTA: ADESSO IL CASO DELLE VEDOVE',960,792,'adesso arriva il caso',DF_,34,'next')]},
]);
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SE SEI VEDOVA',cap:'PER L\'INPS NON SEI CONIUGATA: CONTA SOLO IL TUO REDDITO',items:[
  I('ava',['V',110,'VEDOVA',DF_],330,400,'Se sei vedova'),
  I('stamp',[["PER L'INPS:",'NON CONIUGATA'],INK,44,-4],900,300,'non sei coniugata'),
  P('CONTA SOLO IL TUO REDDITO',900,470,'conta solo il tuo reddito',GF_,34,'ok',{icol:GRN}),
  I('b10lim',[],1520,400,'il tuo limite'),
  I('icard',[1120,140,'warn',[['MA LA REVERSIBILITÀ È UN REDDITO: SI CONTA',36]],{ibg:'#FFE3DE',icol:RED_,ir:48,stroke:RED_}],980,700,'Ma la reversibilità')]},
 {at:'Esempio:',top:'ESEMPIO: CON LA REVERSIBILITÀ',cap:'L\'ASSEGNO È LA DIFFERENZA: 1.901,12 € L\'ANNO, 146,24 € A RATA',items:[
  I('sheet',[],680,520,'Esempio:'),
  OV(I('srow',['− REVERSIBILITÀ NETTA','5.200,00 €',RED_],680,520,'la reversibilità vale')),
  P('CIRCA 400 € AL MESE',1500,440,'circa quattrocento',DF_,30,'coin'),
  OV(I('stot',['= ASSEGNO','1.901,12 €'],680,650,'è la differenza')),
  I('bign',['1.901,12 € ÷ 13','146,24 €','PER CIASCUNA DELLE 13 RATE',{fs:88,fill:GF_,minw:560,tfs:28,sfs:26}],1500,680,'centoquarantasei')]},
]);
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COSA ENTRA NEL CONTO E COSA NO',cap:'NON CONTANO: CASA DOVE ABITI, LIQUIDAZIONE, ARRETRATI TASSATI A PARTE',items:[
  I('b11pair',[],960,215,'Cosa entra nel conto'),
  P('NON CONTANO',960,330,'Non contano',RF_,38,'x',{icol:RED_}),
  I('ncard',['house',['LA CASA','DOVE ABITI']],420,610,'la casa dove abiti'),
  I('ncard',['env',['LA LIQUIDAZIONE','DI FINE LAVORO']],960,610,'la liquidazione'),
  I('ncard',['calback',['GLI ARRETRATI','TASSATI A PARTE']],1500,610,'gli arretrati')]},
 {at:'Contano invece',top:'COSA CONTA',cap:'SI CONTANO GLI INTERESSI, NON I RISPARMI CHE LI PRODUCONO',items:[
  P('CONTANO',960,215,'Contano invece',GF_,38,'ok',{icol:GRN}),
  I('ytile',['globe',['LE PENSIONI','ANCHE DA ALTRI STATI']],280,410,'le pensioni'),
  I('ytile',['house',['LE ALTRE CASE']],720,410,'le altre case'),
  I('ytile',['land',['I TERRENI']],1160,410,'i terreni'),
  I('ytile',['coin',['GLI INTERESSI']],1600,410,'gli interessi'),
  P('BUONI POSTALI',1600,592,'buoni postali',DF_,28,'mail'),
  P('LIBRETTI',1600,666,'dei libretti',DF_,28,'book'),
  P('CONTI IN BANCA',1600,740,'conti in banca',DF_,28,'stato'),
  I('icard',[1180,210,'piggy',[['ATTENZIONE:',30,RED_],['CONTANO GLI INTERESSI,',34],['NON I RISPARMI CHE LI PRODUCONO',34]],{lh:46,ir:62,stroke:AMB}],790,680,'Attenzione')]},
]);
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'UN\'ALTRA STRADA: IL FONDO CASALINGHE',cap:'ISCRIZIONE DAI 16 ANNI, APERTA ANCHE AGLI UOMINI',items:[
  I('b12axis',[],960,240,'Fino ai sessantacinque'),
  P('UN\'ALTRA STRADA',520,410,'un\'altra strada',AMB,34,'signs'),
  I('b12card',[],520,640,'il Fondo casalinghe'),
  OV(I('b12men',[],520,640,'aperto pure agli uomini')),
  OV(I('b12range',[],960,240,'Puoi iscriverti')),
  P('SE NON LAVORI',1400,470,'se non lavori',GF_,30,'ok',{icol:GRN}),
  P('E NON HAI GIÀ UNA PENSIONE TUA',1400,560,'e non hai già',GF_,30,'ok',{icol:GRN}),
  P('CON LA REVERSIBILITÀ PUOI',1400,650,'con la reversibilità',AMB,30,'ok',{icol:'#5A3300'}),
  I('stamp',[["L'ISCRIZIONE RESTA VALIDA",'ANCHE SE NON VERSI NIENTE'],GRN,34,-4],1400,790,"L'iscrizione resta")]},
]);
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANDO PAGA LA PENSIONE',cap:'CON ALMENO 5 ANNI DI CONTRIBUTI: DAI 57 ANNI OPPURE A 65 ANNI',items:[
  I('b13five',[],960,215,'Con almeno cinque'),
  I('b13p',['DAI 57 ANNI',GRN],560,545,'dai cinquantasette'),
  OV(I('b13cond',[],560,520,'se è almeno il venti')),
  OV(P('CIRCA 655 € AL MESE',560,640,'cioè circa',AMB,40)),
  I('b13p',['OPPURE A 65 ANNI','#0B4A50'],1360,545,'Oppure a sessantacinque'),
  OV(I('b13any',[],1360,590,'qualunque sia'))]},
 {at:'Però si calcola',top:'PERÒ: SI CALCOLA SU QUELLO CHE VERSI',cap:'CON POCHI VERSAMENTI LA PENSIONE DEL FONDO È PICCOLA',items:[
  I('b13calc',[],960,330,'si calcola su quello'),
  P('CON POCHI VERSAMENTI È PICCOLA',960,520,'con pochi versamenti',AMB,32,'down',{icol:'#5A3300'}),
  I('icard',[640,150,'x',[['NON VIENE INTEGRATA',32],['AL MINIMO',32]],{ibg:'#FFE3DE',icol:RED_,ir:46}],600,722,'non viene integrata'),
  I('icard',[680,150,'x',[['NON PASSA AI FAMILIARI',32],['SUPERSTITI',32]],{ibg:'#FFE3DE',icol:RED_,ir:46}],1330,722,'non passa ai familiari')]},
]);
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COME SI CHIEDE L\'ASSEGNO SOCIALE',cap:'ONLINE SUL SITO INPS CON LO SPID, OPPURE AL CONTACT CENTER',items:[
  P('DOMANDA DI ASSEGNO SOCIALE',960,215,'Ecco come si chiede',DF_,34,'doc'),
  I('ch',['ONLINE','web','web',["SUL SITO DELL'INPS"]],540,560,'Online sul sito'),
  OV(P('CON LO SPID',540,712,'con lo Spid',GF_,32,'key',{icol:GRN})),
  I('ch',['CONTACT CENTER','phone',null,null],1380,560,'al contact center'),
  OV(I('telrow',['803 164','GRATUITO DA TELEFONO FISSO'],1380,500,'ottocentotre')),
  OV(I('telrow',['06 164 164','DAL CELLULARE'],1380,668,'o zero sei'))]},
 {at:'oppure con un patronato',top:'OPPURE CON UN PATRONATO',cap:'SI INCASSA DAL PRIMO GIORNO DEL MESE DOPO LA DOMANDA',items:[
  I('ch',['PATRONATO','office','office',['UN PATRONATO']],440,480,'con un patronato'),
  I('b14time',[],1270,460,'Si incassa dal primo'),
  I('icard',[960,130,'calback',[['OGNI MESE DI ATTESA È UN MESE PERSO',34,RED_]],{ibg:'#FFE3DE',ir:46,stroke:RED_}],1270,762,'ogni mese di attesa')]},
]);
SPECS[15]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TRE AVVERTENZE',cap:'CONTROLLI OGNI ANNO, ESTERO OLTRE 29 GIORNI, NUOVI IMPORTI A GENNAIO',items:[
  I('wrow',[1,'lens',"OGNI ANNO L'INPS RICONTROLLA REDDITI E RESIDENZA",null],960,300,'Prima'),
  OV(I('wsub',["SE QUALCOSA CAMBIA, L'IMPORTO SI AGGIORNA",AMB,'#5A3300'],830,330,'e se qualcosa cambia')),
  I('wrow',[2,'plane',"ALL'ESTERO PIÙ DI 29 GIORNI DI FILA: ASSEGNO SOSPESO",null],960,500,'Seconda'),
  OV(I('wsub',['DOPO UN ANNO DI SOSPENSIONE SI PERDE',RF_],790,530,'e dopo un anno')),
  I('wrow',[3,'cal','ASSEGNO E LIMITI CAMBIANO OGNI GENNAIO','CON LA RIVALUTAZIONE DELLE PENSIONI'],960,700,'Terza')]},
]);
SPECS[16]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONE ALLE CASALINGHE',cap:'',items:[
  P('DAI 67 ANNI, ANCHE SENZA CONTRIBUTI',960,200,'Dai sessantasette',GF_,32,'ok',{icol:GRN}),
  P('COPPIE SPOSATE: DECIDE IL REDDITO DEI DUE',960,285,'ma per le coppie',AMB,32,'people',{icol:'#5A3300'}),
  I('icard',[740,180,'share',[["CONOSCI QUALCUNO DI QUELL'ETÀ",28],['CHE NON L\'HA ANCORA CHIESTO?',28],['MANDAGLI QUESTO VIDEO',32,GRN]],{lh:42,ir:54}],540,430,'Conosci qualcuno'),
  I('icard',[760,180,'chat',[['SCRIVI NEI COMMENTI:',28],['È GIUSTO CONTARE',32,GRN],['IL REDDITO DEL MARITO?',32,GRN]],{lh:42,ir:54}],1380,430,'E scrivi nei commenti'),
  I('dbox',[],960,612,'Per il tuo caso')]},
]);
