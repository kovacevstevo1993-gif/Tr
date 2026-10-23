// ===== VIDEO 10 (pensione alle casalinghe / assegno sociale) - elementi nuovi =====
// Un po' diverso dai video 8-9 (N.37, N.47 alla lettera), stessi colori e stessa impostazione del canale:
// titoletto con casetta e tacche dei 16 blocchi, didascalia con filo giallo in alto e casetta,
// ritratti in cornice quadrata (lei, il marito), "casa del reddito" (il tetto = il limite), schede con testata scura
// e filo giallo, timbri inclinati, pillole con icona, sfondo con casa in trasparenza e luci che scorrono piano.
const NB10=16;
// larghezza vera del testo (misurata nel browser); se non si puo', stima
function mw(t,s,fs){let w=0;try{w=t.getComputedTextLength();}catch(e){}return w||tw(s,fs);}
// testo centrato su yc, rimpicciolito se supera maxW
function fitT(p,s,x,yc,fs,fill,weight,maxW,anchor){const t=txt(p,s,x,yc+fs*0.36,fs,fill,weight||'bold',anchor);
 if(maxW){const w=mw(t,s,fs);if(w>maxW){const f2=fs*maxW/w;t.setAttribute('font-size',f2.toFixed(1));t.setAttribute('y',(yc+f2*0.36).toFixed(1));}}return t;}
// ---------- icone (disegnate intorno a 0,0, circa 80 x 80) ----------
function ico(p,k,s,col){s=s||1;col=col||INK;const g=el('g',{transform:'scale('+s+')'},p);const W='#fff';
 const E=(t,a)=>el(t,a,g);
 if(k=='house'){E('path',{d:'M-42 -2 L0 -40 L42 -2 Z',fill:col,'stroke-linejoin':'round'});E('rect',{x:-31,y:-6,width:62,height:42,rx:4,fill:col});E('rect',{x:-9,y:12,width:18,height:24,rx:3,fill:W});}
 else if(k=='brief'){E('path',{d:'M-15 -20 V-32 H15 V-20',fill:'none',stroke:col,'stroke-width':7,'stroke-linejoin':'round'});E('rect',{x:-40,y:-22,width:80,height:56,rx:9,fill:col});E('rect',{x:-40,y:-2,width:80,height:5,fill:W,opacity:.6});E('rect',{x:-7,y:-6,width:14,height:12,rx:3,fill:AMB});}
 else if(k=='x'){E('path',{d:'M-24 -24 L24 24 M24 -24 L-24 24',stroke:col,'stroke-width':12,'stroke-linecap':'round'});}
 else if(k=='ok'){E('path',{d:'M-26 2 L-8 20 L28 -20',fill:'none',stroke:col,'stroke-width':12,'stroke-linecap':'round','stroke-linejoin':'round'});}
 else if(k=='q'){E('path',{d:'M-18 -14 Q-18 -36 0 -36 Q20 -36 20 -16 Q20 -2 4 6 Q0 9 0 16',fill:'none',stroke:col,'stroke-width':11,'stroke-linecap':'round'});E('circle',{cx:0,cy:32,r:7,fill:col});}
 else if(k=='warn'){E('path',{d:'M0 -38 L41 32 H-41 Z',fill:col,stroke:col,'stroke-width':6,'stroke-linejoin':'round'});E('rect',{x:-4.5,y:-14,width:9,height:28,rx:4.5,fill:W});E('circle',{cx:0,cy:23,r:5.5,fill:W});}
 else if(k=='clock'){E('circle',{r:36,fill:'none',stroke:col,'stroke-width':8});E('path',{d:'M0 -22 V0 L16 12',fill:'none',stroke:col,'stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'});}
 else if(k=='lock'||k=='unlock'){if(k=='lock')E('path',{d:'M-22 -6 V-20 Q-22 -42 0 -42 Q22 -42 22 -20 V-6',fill:'none',stroke:col,'stroke-width':9});
  else E('path',{d:'M-22 -6 V-20 Q-22 -42 0 -42 Q22 -42 22 -20 V-28',fill:'none',stroke:col,'stroke-width':9,transform:'translate(30 -6)'});
  E('rect',{x:-32,y:-8,width:64,height:48,rx:9,fill:col});E('circle',{cx:0,cy:11,r:7,fill:W});E('rect',{x:-3,y:12,width:6,height:15,rx:3,fill:W});}
 else if(k=='cal'){E('rect',{x:-36,y:-30,width:72,height:66,rx:9,fill:W,stroke:col,'stroke-width':6});E('rect',{x:-36,y:-30,width:72,height:20,rx:7,fill:col});
  [-16,16].forEach(x=>E('rect',{x:x-4,y:-40,width:8,height:18,rx:4,fill:col}));for(let r=0;r<2;r++)for(let c=0;c<3;c++)E('rect',{x:-24+c*18,y:-2+r*16,width:12,height:10,rx:2,fill:col,opacity:.75});}
 else if(k=='calback'){ico(g,'cal',1,col);E('path',{d:'M30 26 A22 22 0 1 1 30 -2',fill:'none',stroke:AMB,'stroke-width':8,transform:'translate(14 10)'});E('path',{d:'M38 -14 L46 6 L26 4 Z',fill:AMB});}
 else if(k=='coin'){E('circle',{r:36,fill:AMB,stroke:'#fff','stroke-width':5});euro(g,0,0,0.4,'#5A3300',16);}
 else if(k=='stato'){E('path',{d:'M-40 -16 L0 -40 L40 -16 Z',fill:col});[-28,-10,10,28].forEach(x=>E('rect',{x:x-5,y:-12,width:10,height:38,fill:col}));E('rect',{x:-44,y:28,width:88,height:10,rx:2,fill:col});}
 else if(k=='office'){E('rect',{x:-30,y:-38,width:60,height:76,rx:5,fill:col});for(let r=0;r<4;r++)for(let c=0;c<3;c++)E('rect',{x:-21+c*16,y:-30+r*15,width:10,height:9,rx:1.5,fill:W,opacity:.9});E('rect',{x:-7,y:24,width:14,height:14,fill:W});}
 else if(k=='phone'){E('path',{d:'M-26 -34 Q-36 -30 -34 -14 Q-28 14 2 30 Q20 38 30 30 L36 22 Q38 16 32 12 L18 4 Q12 2 8 8 L4 13 Q-12 4 -16 -10 L-10 -14 Q-4 -18 -6 -24 L-14 -36 Q-18 -40 -26 -34 Z',fill:col});}
 else if(k=='web'){E('rect',{x:-40,y:-30,width:80,height:56,rx:7,fill:W,stroke:col,'stroke-width':6});E('rect',{x:-40,y:-30,width:80,height:14,rx:6,fill:col});E('rect',{x:-50,y:28,width:100,height:9,rx:4,fill:col});E('rect',{x:-26,y:-6,width:40,height:6,rx:3,fill:col,opacity:.5});E('rect',{x:-26,y:6,width:28,height:6,rx:3,fill:col,opacity:.5});}
 else if(k=='key'){E('circle',{cx:-18,cy:0,r:18,fill:'none',stroke:col,'stroke-width':9});E('path',{d:'M0 0 H40 M28 0 V14 M38 0 V10',fill:'none',stroke:col,'stroke-width':9,'stroke-linecap':'round'});}
 else if(k=='people'){[[-18,col],[18,col]].forEach(([x,c],i)=>{E('circle',{cx:x,cy:-16,r:12,fill:c,opacity:i?1:.75});E('path',{d:`M${x-20} 30 Q${x-20} 0 ${x} 0 Q${x+20} 0 ${x+20} 30 Z`,fill:c,opacity:i?1:.75});});}
 else if(k=='globe'){E('circle',{r:36,fill:'none',stroke:col,'stroke-width':6});E('ellipse',{rx:15,ry:36,fill:'none',stroke:col,'stroke-width':5});E('line',{x1:-36,y1:0,x2:36,y2:0,stroke:col,'stroke-width':5});E('path',{d:'M-31 -18 H31 M-31 18 H31',stroke:col,'stroke-width':4});}
 else if(k=='land'){E('path',{d:'M-42 30 L-20 -6 L42 -6 L42 30 Z',fill:col,opacity:.9});[0,1,2].forEach(i=>E('path',{d:`M${-30+i*10} 30 L${-8+i*16} -6`,stroke:W,'stroke-width':4,opacity:.8}));E('circle',{cx:22,cy:-26,r:12,fill:AMB});}
 else if(k=='piggy'){E('ellipse',{cx:0,cy:4,rx:38,ry:28,fill:col});E('path',{d:'M-14 -20 L-6 -36 L4 -22 Z',fill:col});E('circle',{cx:22,cy:-2,r:4,fill:W});E('rect',{x:-10,y:-24,width:20,height:6,rx:3,fill:W});[-22,16].forEach(x=>E('rect',{x:x-6,y:26,width:12,height:12,rx:3,fill:col}));E('circle',{cx:0,cy:-40,r:9,fill:AMB,stroke:W,'stroke-width':3});}
 else if(k=='book'){E('path',{d:'M0 -26 Q-22 -38 -42 -30 V30 Q-22 22 0 34 Q22 22 42 30 V-30 Q22 -38 0 -26 Z',fill:col});E('line',{x1:0,y1:-26,x2:0,y2:34,stroke:W,'stroke-width':4});}
 else if(k=='mail'){E('rect',{x:-40,y:-26,width:80,height:54,rx:7,fill:col});E('path',{d:'M-40 -22 L0 8 L40 -22',fill:'none',stroke:W,'stroke-width':5,'stroke-linejoin':'round'});}
 else if(k=='env'){E('rect',{x:-40,y:-26,width:80,height:54,rx:7,fill:col});E('path',{d:'M-40 -22 L0 8 L40 -22',fill:'none',stroke:W,'stroke-width':5});E('circle',{cx:24,cy:16,r:15,fill:AMB,stroke:W,'stroke-width':3});euro(g,24,16,0.17,'#5A3300',16);}
 else if(k=='doc'){E('path',{d:'M-28 -38 H14 L30 -22 V38 H-28 Z',fill:W,stroke:col,'stroke-width':6,'stroke-linejoin':'round'});E('path',{d:'M14 -38 V-22 H30',fill:'none',stroke:col,'stroke-width':5});[-10,4,18].forEach((y,i)=>E('rect',{x:-18,y:y,width:i==2?24:36,height:6,rx:3,fill:col,opacity:.7}));}
 else if(k=='pen'){E('path',{d:'M-30 30 L-24 12 L18 -30 L30 -18 L-12 24 Z',fill:col});E('path',{d:'M-30 30 L-24 12 L-12 24 Z',fill:AMB});}
 else if(k=='calc'){E('rect',{x:-30,y:-38,width:60,height:76,rx:9,fill:col});E('rect',{x:-21,y:-30,width:42,height:16,rx:3,fill:'#D6F5EC'});for(let r=0;r<3;r++)for(let c=0;c<3;c++)E('rect',{x:-21+c*15,y:-8+r*14,width:11,height:10,rx:2,fill:c==2&&r==2?AMB:'#7FF0D2'});}
 else if(k=='share'){E('path',{d:'M-34 26 Q-30 -12 10 -12 V-30 L40 0 L10 30 V12 Q-18 10 -34 26 Z',fill:col,'stroke-linejoin':'round'});}
 else if(k=='chat'){E('path',{d:'M-38 -30 H38 Q44 -30 44 -24 V14 Q44 20 38 20 H-6 L-24 36 L-20 20 H-38 Q-44 20 -44 14 V-24 Q-44 -30 -38 -30 Z',fill:col});[-18,0,18].forEach(x=>E('circle',{cx:x,cy:-5,r:5,fill:W}));}
 else if(k=='lens'){E('circle',{cx:-8,cy:-8,r:24,fill:'none',stroke:col,'stroke-width':9});E('line',{x1:10,y1:10,x2:32,y2:32,stroke:col,'stroke-width':11,'stroke-linecap':'round'});}
 else if(k=='plane'){E('path',{d:'M-40 4 L-30 -4 L-6 0 L10 -34 L20 -34 L14 0 L32 2 L38 -12 L44 -12 L42 6 L44 22 L38 22 L32 10 L14 12 L20 44 L10 44 L-6 12 L-30 14 Z',fill:col,transform:'rotate(-90) translate(-4 0)'});}
 else if(k=='next'){E('path',{d:'M-34 -12 H6 V-30 L38 0 L6 30 V12 H-34 Z',fill:col,'stroke-linejoin':'round'});}
 else if(k=='up'||k=='down'){const d=k=='up'?'M0 -38 L30 -6 H12 V36 H-12 V-6 H-30 Z':'M0 38 L30 6 H12 V-36 H-12 V6 H-30 Z';E('path',{d:d,fill:col,'stroke-linejoin':'round'});}
 else if(k=='bulb'){E('path',{d:'M-24 -8 Q-24 -36 0 -36 Q24 -36 24 -8 Q24 6 12 16 V24 H-12 V16 Q-24 6 -24 -8 Z',fill:col});E('rect',{x:-11,y:28,width:22,height:8,rx:4,fill:col});[-42,42].forEach(x=>E('line',{x1:x*0.8,y1:-10,x2:x,y2:-14,stroke:AMB,'stroke-width':6,'stroke-linecap':'round'}));E('line',{x1:0,y1:-46,x2:0,y2:-54,stroke:AMB,'stroke-width':6,'stroke-linecap':'round'});}
 else if(k=='id'){E('rect',{x:-42,y:-28,width:84,height:56,rx:8,fill:W,stroke:col,'stroke-width':6});E('circle',{cx:-20,cy:-6,r:9,fill:col});E('path',{d:'M-34 18 Q-34 4 -20 4 Q-6 4 -6 18 Z',fill:col});[-10,4].forEach(y=>E('rect',{x:4,y:y,width:26,height:6,rx:3,fill:col,opacity:.7}));}
 else if(k=='it'){const fw=72,fh=48;[['#1F9A4B',-fw/2],['#F7F7F2',-fw/6],['#D7322B',fw/6]].forEach(([c,x])=>E('rect',{x:x,y:-fh/2,width:fw/3+0.5,height:fh,fill:c}));E('rect',{x:-fw/2,y:-fh/2,width:fw,height:fh,rx:4,fill:'none',stroke:col,'stroke-width':4});}
 else if(k=='ruler'){E('rect',{x:-42,y:-14,width:84,height:28,rx:5,fill:col});for(let i=0;i<7;i++)E('rect',{x:-34+i*11,y:-14,width:4,height:i%2?10:16,fill:W});E('rect',{x:16,y:-28,width:6,height:56,rx:3,fill:RED_});}
 else if(k=='cut'){E('circle',{cx:-22,cy:20,r:12,fill:'none',stroke:col,'stroke-width':7});E('circle',{cx:22,cy:20,r:12,fill:'none',stroke:col,'stroke-width':7});E('path',{d:'M-14 12 L20 -36 M14 12 L-20 -36',stroke:col,'stroke-width':8,'stroke-linecap':'round'});}
 else if(k=='signs'){E('rect',{x:-5,y:-40,width:10,height:80,rx:4,fill:col});E('path',{d:'M-2 -34 H34 L44 -24 L34 -14 H-2 Z',fill:AMB});E('path',{d:'M2 -6 H-34 L-44 4 L-34 14 H2 Z',fill:'#7FF0D2'});}
 else if(k=='cake'){E('rect',{x:-32,y:0,width:64,height:34,rx:6,fill:col});E('rect',{x:-32,y:8,width:64,height:6,fill:W,opacity:.6});[-16,0,16].forEach(x=>{E('rect',{x:x-3,y:-20,width:6,height:20,fill:AMB});E('path',{d:`M${x} -34 Q${x+6} -26 ${x} -22 Q${x-6} -26 ${x} -34 Z`,fill:RED_});});}
 return g;}
// icona dentro un cerchio
function icoC(p,k,r,fill,icol){const g=el('g',{},p);el('circle',{r:r,fill:fill||'#fff',stroke:'#fff','stroke-width':Math.max(3,r*0.08),filter:'url(#g_sh3)'},g);ico(g,k,r/52,icol||INK);return g;}
// casetta piccola per titoletto e didascalia
function hico(p,s,col,door){const g=el('g',{transform:'scale('+s+')'},p);
 el('path',{d:'M-33 -2 L0 -31 L33 -2 Z',fill:col,'stroke-linejoin':'round'},g);
 el('rect',{x:-24,y:-6,width:48,height:32,rx:4,fill:col},g);
 el('rect',{x:-7,y:8,width:14,height:18,rx:2,fill:door||'#fff'},g);return g;}
// ---------- titoletto (a sinistra, con casetta e 16 tacche dei blocchi) ----------
function topLabel(g,s){const t=el('g',{transform:'translate(-840 0)'},g);
 el('rect',{x:-36,y:-36,width:72,height:72,rx:18,fill:'url(#g_paper)',filter:'url(#g_sh3)'},t);
 hico(t,0.95,INK);
 const x=txt(t,s,64,12,36,'#7FF0D2','bold','start');x.setAttribute('letter-spacing','6');
 let w=tw(s,36)+s.length*6;try{w=x.getBBox().width;}catch(e){}
 el('rect',{x:64,y:30,width:Math.min(w,150),height:5,rx:2.5,fill:AMB},t);
 const X0=1452,DX=14;const l0=64+w+28,l1=X0-26;if(l1>l0+20)el('line',{x1:l0,y1:0,x2:l1,y2:0,stroke:'#7FF0D2','stroke-width':3,opacity:.32},t);
 for(let i=0;i<NB10;i++){const on=(i+1)===N;const h=on?30:16;el('rect',{x:X0+i*DX-3,y:-h/2,width:6,height:h,rx:3,fill:on?AMB:'#7FF0D2',opacity:on?1:((i+1)<N?.75:.28)},t);}
 return t;}
// ---------- didascalia (riquadro scuro, filo giallo in alto, casetta a sinistra) ----------
function cap(g,s,size){size=size||44;const c=el('g',{},g);if(!s)return c;
 const t=txt(c,s,0,0,size,'#FFFFFF','bold');let tl=mw(t,s,size);
 const maxT=1540;if(tl>maxT){size=size*maxT/tl;t.setAttribute('font-size',size.toFixed(1));tl=mw(t,s,size);}
 const padL=124,padR=60;const w=tl+padL+padR;
 t.setAttribute('x',(-w/2+padL+tl/2).toFixed(1));t.setAttribute('y',(size*0.36).toFixed(1));
 const ins=e=>{c.insertBefore(e,t);return e;};
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:22,fill:'#06303A',filter:'url(#g_sh2)'}));
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:22,fill:'none',stroke:'#7FF0D2','stroke-width':2.5,opacity:.45}));
 ins(el('rect',{x:-w/2+34,y:-56,width:w-68,height:6,rx:3,fill:AMB}));
 const hb=el('g',{transform:'translate('+(-w/2+64)+' 2)'},c);el('circle',{r:31,fill:'#0B4A50',stroke:'#7FF0D2','stroke-width':3},hb);hico(hb,0.6,'#7FF0D2','#0B4A50');
 return c;}
// ---------- pillola con testo misurato e icona facoltativa ----------
function pillB(g,s,fs,fill,col,icon,o){o=o||{};fs=fs||34;const t=txt(g,s,0,fs*0.36,fs,col||'#fff','bold');const tl=mw(t,s,fs);
 const h=o.h||fs*1.8;const ir=icon?h*0.37:0;const padL=icon?(h*0.14+2*ir+fs*0.45):fs*0.95;const padR=fs*0.95;
 const w=Math.max(o.minw||0,tl+padL+padR);const tx=-w/2+padL+(w-padL-padR)/2;t.setAttribute('x',tx.toFixed(1));
 const r=el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:o.rx!==undefined?o.rx:h/2,fill:fill,stroke:o.stroke||'#fff','stroke-width':o.sw||4,filter:'url(#g_sh3)'});g.insertBefore(r,t);
 if(icon){const ig=el('g',{transform:'translate('+(-w/2+h*0.14+ir)+' 0)'},g);el('circle',{r:ir,fill:o.ibg||'#fff'},ig);ico(ig,icon,ir/48,o.icol||INK);}
 g.__w=w;return w;}
// ---------- numero grande con riga sopra e sotto ----------
function bigN(g,top,val,sub,o){o=o||{};const fs=o.fs||96;const fill=o.fill||'url(#g_paper)';const dark=!(fill==='url(#g_paper)'||fill==='#fff');
 const col=o.col||(dark?'#fff':INK);const sc=o.subcol||(dark?'#fff':GRN);const tH=o.tfs||30,sH=o.sfs||30;const pv=o.padv||36;
 const H=(top?tH*1.55:0)+fs*1.02+(sub?sH*1.55:0)+pv;
 const r=el('rect',{x:0,y:-H/2,width:10,height:H,rx:o.rx||28,fill:fill,filter:'url(#g_sh)'},g);
 const rs=el('rect',{x:0,y:-H/2,width:10,height:H,rx:o.rx||28,fill:'none',stroke:o.stroke||'#fff','stroke-opacity':o.stroke?1:.85,'stroke-width':o.stroke?6:4},g);
 let yy=-H/2+pv/2;const T=[];
 if(top){T.push(txt(g,top,0,yy+tH*1.05,tH,sc,'bold'));yy+=tH*1.55;}
 T.push(txt(g,val,0,yy+fs*0.84,fs,col,'900'));yy+=fs*1.02;
 if(sub){T.push(txt(g,sub,0,yy+sH*1.1,sH,sc,'bold'));}
 const w=Math.max(o.minw||0,...T.map(t=>mw(t,t.textContent,+t.getAttribute('font-size'))))+(o.padh||90);
 [r,rs].forEach(e=>{e.setAttribute('x',-w/2);e.setAttribute('width',w);});g.__w=w;g.__h=H;return w;}
// ---------- ritratto in cornice quadrata (lei = C, il marito = H) ----------
const PC10={C:'#1B9F81',H:'#2B6F8F',V:'#5C7C86'};
function ava(p,kind,r,col){r=r||90;col=col||PC10[kind]||'#2B8FA0';const g=el('g',{filter:'url(#g_sh)'},p);
 const id='av'+(++UID);const cp=el('clipPath',{id:id},g);el('rect',{x:-r,y:-r,width:2*r,height:2*r,rx:r*0.3},cp);
 el('rect',{x:-r,y:-r,width:2*r,height:2*r,rx:r*0.3,fill:'#0E5A60'},g);
 const f=el('g',{'clip-path':'url(#'+id+')'},g);const SK='#F1D9C4',HG='#DCE2E4';
 el('circle',{cx:0,cy:-r*0.12,r:r*0.92,fill:'#14727B'},f);
 el('path',{d:`M${-r*0.95} ${r*1.05} Q${-r*0.9} ${r*0.32} 0 ${r*0.28} Q${r*0.9} ${r*0.32} ${r*0.95} ${r*1.05} Z`,fill:col},f);
 el('rect',{x:-r*0.12,y:r*0.04,width:r*0.24,height:r*0.28,fill:SK},f);
 const lady=(kind=='C'||kind=='V');
 if(lady)el('circle',{cx:0,cy:-r*0.64,r:r*0.17,fill:HG},f);
 el('ellipse',{cx:0,cy:-r*0.16,rx:r*0.3,ry:r*0.35,fill:SK},f);
 if(lady){el('path',{d:`M${-r*0.34} ${-r*0.04} Q${-r*0.4} ${-r*0.6} 0 ${-r*0.57} Q${r*0.4} ${-r*0.6} ${r*0.34} ${-r*0.04} Q${r*0.27} ${-r*0.4} 0 ${-r*0.41} Q${-r*0.27} ${-r*0.4} ${-r*0.34} ${-r*0.04} Z`,fill:HG},f);
  [-1,1].forEach(s=>el('circle',{cx:s*r*0.31,cy:-r*0.02,r:r*0.04,fill:AMB},f));
  el('path',{d:`M${-r*0.22} ${r*0.32} Q0 ${r*0.5} ${r*0.22} ${r*0.32}`,fill:'none',stroke:'#fff','stroke-width':r*0.05,'stroke-linecap':'round'},f);}
 if(kind=='H'){[-1,1].forEach(s=>el('path',{d:`M${s*r*0.31} ${-r*0.1} Q${s*r*0.36} ${-r*0.42} ${s*r*0.17} ${-r*0.47}`,fill:'none',stroke:'#C9D3D6','stroke-width':r*0.11,'stroke-linecap':'round'},f));
  el('path',{d:`M${-r*0.15} ${r*0.0} Q0 ${-r*0.07} ${r*0.15} ${r*0.0} Q0 ${r*0.05} ${-r*0.15} ${r*0.0} Z`,fill:'#C9D3D6'},f);
  [-1,1].forEach(s=>el('rect',{x:s*r*0.13-r*0.09,y:-r*0.27,width:r*0.18,height:r*0.13,rx:r*0.04,fill:'none',stroke:INK,'stroke-width':r*0.03},f));
  el('line',{x1:-r*0.04,y1:-r*0.21,x2:r*0.04,y2:-r*0.21,stroke:INK,'stroke-width':r*0.03},f);
  el('path',{d:`M${-r*0.2} ${r*0.3} L0 ${r*0.5} L${r*0.2} ${r*0.3}`,fill:'#fff'},f);}
 [-1,1].forEach(s=>el('circle',{cx:s*r*0.12,cy:-r*0.2,r:r*0.032,fill:INK},f));
 el('path',{d:kind=='H'?`M${-r*0.08} ${r*0.07} Q0 ${r*0.12} ${r*0.08} ${r*0.07}`:`M${-r*0.1} ${r*0.0} Q0 ${r*0.08} ${r*0.1} ${r*0.0}`,fill:'none',stroke:INK,'stroke-width':r*0.032,'stroke-linecap':'round'},f);
 el('rect',{x:-r,y:-r,width:2*r,height:2*r,rx:r*0.3,fill:'none',stroke:'#fff','stroke-width':r*0.06},g);
 el('rect',{x:-r*1.09,y:-r*1.09,width:2*r*1.09,height:2*r*1.09,rx:r*0.36,fill:'none',stroke:col,'stroke-width':r*0.05},g);
 return g;}
// ---------- scheda con testata scura e filo giallo ----------
function cardB(g,title,w,h,o){o=o||{};const hh=title?(o.hh||66):0;const R=o.rx||24;
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:R,fill:o.fill||'url(#g_paper)',filter:'url(#g_sh)'},g);
 if(o.stroke)el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:R,fill:'none',stroke:o.stroke,'stroke-width':o.sw||6},g);
 if(title){const hg=el('g',{},g);
  el('path',{d:`M${-w/2} ${-h/2+hh} V${-h/2+R} Q${-w/2} ${-h/2} ${-w/2+R} ${-h/2} H${w/2-R} Q${w/2} ${-h/2} ${w/2} ${-h/2+R} V${-h/2+hh} Z`,fill:o.hc||'#0B4A50'},hg);
  el('rect',{x:-w/2,y:-h/2+hh-5,width:w,height:5,fill:o.ac||AMB},g);
  const ic=o.hicon?44:0;fitT(hg,title,ic/2,-h/2+hh/2-2,o.hfs||30,'#fff','bold',w-70-ic);
  if(o.hicon){const tl=(()=>{const tt=hg.querySelector('text');return mw(tt,title,o.hfs||30);})();const ix=ic/2-tl/2-30;const ig=el('g',{transform:'translate('+ix+' '+(-h/2+hh/2-2)+')'},g);el('circle',{r:19,fill:'#fff'},ig);ico(ig,o.hicon,0.36,o.hicol||(o.hc||INK));}}
 (o.lines||[]).forEach(L=>fitT(g,L[0],L[4]||0,L[2],L[1],L[3]||INK,L[5]||'900',w-2*(o.pad||34)));
 if(o.icon){const I_=o.icon;const ig=el('g',{transform:'translate('+I_[1]+' '+I_[2]+')'},g);if(I_[4])el('circle',{r:I_[5]||54,fill:I_[4]},ig);ico(ig,I_[0],I_[3]||1,I_[6]||INK);}
 return g;}
// ---------- timbro inclinato, doppio bordo ----------
function stampB(g,lines,col,fs,rot){fs=fs||40;const sg=el('g',{transform:'rotate('+(rot||-6)+')'},g);
 const T=lines.map((s,i)=>txt(sg,s,0,0,i==0?fs:fs*0.8,col,'900'));const ws=T.map(t=>mw(t,t.textContent,+t.getAttribute('font-size')));
 const w=Math.max(...ws)+fs*1.6;const lh=fs*1.12;const h=lines.length*lh+fs*0.9;
 T.forEach((t,i)=>t.setAttribute('y',(-h/2+fs*0.45+lh*i+lh*0.78).toFixed(1)));
 const r1=el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:14,fill:'#fff',stroke:col,'stroke-width':8,filter:'url(#g_sh2)'});sg.insertBefore(r1,T[0]);
 const r2=el('rect',{x:-w/2+10,y:-h/2+10,width:w-20,height:h-20,rx:9,fill:'none',stroke:col,'stroke-width':3,opacity:.7});sg.insertBefore(r2,T[0]);
 return w;}
// ---------- casa (base a terra in 0,0) ----------
function houseB(p,w,h,rh,o){o=o||{};const g=el('g',{},p);
 if(o.chim!==false)el('rect',{x:w*0.2,y:-h-rh*0.85,width:w*0.1,height:rh*0.75,rx:4,fill:o.roof||'#C9503C',stroke:'#fff','stroke-width':4},g);
 el('rect',{x:-w/2,y:-h,width:w,height:h,rx:10,fill:o.body||'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h,width:w,height:h,rx:10,fill:'none',stroke:'#fff','stroke-width':5},g);
 const ov_=o.over!==undefined?o.over:28;el('path',{d:`M${-w/2-ov_} ${-h+8} L0 ${-h-rh} L${w/2+ov_} ${-h+8} Z`,fill:o.roofFill||'url(#g_red)',stroke:'#fff','stroke-width':6,'stroke-linejoin':'round',filter:'url(#g_sh2)'},g);
 return g;}
// finestrella
function win10(p,x,y,s){const g=el('g',{transform:'translate('+x+' '+y+') scale('+(s||1)+')'},p);
 el('rect',{x:-30,y:-30,width:60,height:60,rx:8,fill:'#BFEFE3',stroke:'#0B4A50','stroke-width':5},g);
 el('line',{x1:0,y1:-30,x2:0,y2:30,stroke:'#0B4A50','stroke-width':4},g);el('line',{x1:-30,y1:0,x2:30,y2:0,stroke:'#0B4A50','stroke-width':4},g);return g;}
// freccia dritta (da x1,y1 a x2,y2, coordinate locali)
function arrB(p,x1,y1,x2,y2,col,sw,dash){const g=el('g',{},p);const a=Math.atan2(y2-y1,x2-x1);const L=Math.hypot(x2-x1,y2-y1);const hl=sw*2.6;
 el('line',{x1:x1,y1:y1,x2:x1+(L-hl*0.8)*Math.cos(a),y2:y1+(L-hl*0.8)*Math.sin(a),stroke:col,'stroke-width':sw,'stroke-linecap':'round','stroke-dasharray':dash||''},g);
 const p1=[x2,y2],p2=[x2-hl*Math.cos(a)+hl*0.62*Math.sin(a),y2-hl*Math.sin(a)-hl*0.62*Math.cos(a)],p3=[x2-hl*Math.cos(a)-hl*0.62*Math.sin(a),y2-hl*Math.sin(a)+hl*0.62*Math.cos(a)];
 el('path',{d:`M${p1} L${p2} L${p3} Z`,fill:col},g);return g;}
// riga di monete numerate
function coinsRow(p,n,r,gap,labels,hl){const g=el('g',{},p);const W=(n-1)*gap;
 for(let i=0;i<n;i++){const x=-W/2+i*gap;const c=el('g',{transform:'translate('+x+' 0)'},g);
  el('circle',{r:r,fill:(hl&&hl.includes(i))?AMB:'url(#g_rim)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh3)'},c);
  el('circle',{r:r*0.78,fill:'none',stroke:'#fff','stroke-width':2,opacity:.55},c);
  if(labels)txt(c,labels[i],0,r*0.36*1.0,r*0.8,(hl&&hl.includes(i))?'#5A3300':'#fff','900');}
 return g;}
