// ===== SHORT 4 - teaser video lungo 2 (1080x1920, 30 fps) =====
// Regola n.5: movimenti LENTI (>=0.7 s), tutto completo almeno 0.5 s prima della fine, poi FERMO. Fascia y 330-680 libera per le didascalie di CapCut.
const eob2=x=>{const c1=1.0,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const pop=(t,a,d)=>Math.max(0,eob2(seg(t,a,a+(d||.8))));
const sl=(t,a,d)=>eo3(seg(t,a,a+(d||.8)));
function ttl(p,s,size,fill){const t=txt(p,s,0,0,size,fill||'#fff','bold');t.setAttribute('stroke','#06282C');t.setAttribute('stroke-width',size*0.16);t.setAttribute('stroke-linejoin','round');t.setAttribute('paint-order','stroke');return t;}
function person(p,shirt,hair){const g=el('g',{},p);
 el('path',{d:'M-135 232 Q-135 92 0 92 Q135 92 135 232 Z',fill:shirt,stroke:'#fff','stroke-width':7,'stroke-linejoin':'round',filter:'url(#g_sh2)'},g);
 el('path',{d:'M-38 98 L0 158 L38 98 Z',fill:'#fff'},g);el('path',{d:'M-11 158 L0 226 L11 158 Z',fill:'#0B3A3F'},g);
 el('rect',{x:-26,y:48,width:52,height:56,rx:16,fill:'#EDBE92'},g);
 el('circle',{cx:0,cy:0,r:80,fill:'#F7D3B0',stroke:'#fff','stroke-width':6},g);
 el('path',{d:'M-82 -8 Q-84 -96 0 -96 Q84 -96 82 -8 Q44 -52 -8 -50 Q-52 -48 -82 -8Z',fill:hair},g);
 el('circle',{cx:-27,cy:10,r:9,fill:'#0B3A3F'},g);el('circle',{cx:27,cy:10,r:9,fill:'#0B3A3F'},g);
 el('path',{d:'M-28 40 Q0 66 28 40',fill:'none',stroke:'#B5523B','stroke-width':8,'stroke-linecap':'round'},g);return g;}
function eye(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:'M-120 0 Q0 -105 120 0 Q0 105 -120 0Z',fill:'#fff',stroke:'#0B4A50','stroke-width':8,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:0,r:44,fill:'#1B9F81'},g);el('circle',{cx:0,cy:0,r:20,fill:'#0A1C1F'},g);
 el('line',{x1:-100,y1:-80,x2:100,y2:80,stroke:RED,'stroke-width':20,'stroke-linecap':'round'},g);return g;}
function check(p,r,col){const g=el('g',{},p);el('circle',{r:r,fill:col||'#1B9F81',stroke:'#fff','stroke-width':r*.16},g);
 el('path',{d:`M${-r*.45} ${r*.02} l${r*.3} ${r*.32} l${r*.6} ${-r*.66}`,fill:'none',stroke:'#fff','stroke-width':r*.26,'stroke-linecap':'round','stroke-linejoin':'round'},g);return g;}
function crossC(p,r){const g=el('g',{},p);el('circle',{r:r,fill:RED,stroke:'#fff','stroke-width':r*.16},g);
 el('path',{d:`M${-r*.4} ${-r*.4} L${r*.4} ${r*.4} M${r*.4} ${-r*.4} L${-r*.4} ${r*.4}`,stroke:'#fff','stroke-width':r*.26,'stroke-linecap':'round'},g);return g;}
function lockG(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-38*s} ${-10*s} V${-50*s} a${38*s} ${38*s} 0 0 1 ${76*s} 0 V${-10*s}`,fill:'none',stroke:'#fff','stroke-width':16*s,'stroke-linecap':'round'},g);
 el('rect',{x:-58*s,y:-12*s,width:116*s,height:90*s,rx:20*s,fill:YEL,stroke:'#fff','stroke-width':7*s},g);el('circle',{cx:0,cy:30*s,r:12*s,fill:'#7A2A00'},g);return g;}
function bigArrow(p){return el('path',{d:'M-60 -90 H60 V0 H110 L0 110 L-110 0 H-60Z',fill:YEL,stroke:'#fff','stroke-width':8,'stroke-linejoin':'round',filter:'url(#g_sh2)'},p);}

function topLabelV(p,s){const fs=58,sp=8;const w=s.length*(fs*0.72+sp)+80;const t=el('g',{},p);
 el('polygon',{points:'-16,-16 0,-32 16,-16 0,0',fill:'#7FF0D2',transform:'translate('+(-w/2+18)+' 0)'},t);
 const x=txt(t,s,-w/2+64,fs*0.36,fs,'#7FF0D2','bold','start');x.setAttribute('letter-spacing',sp);return t;}
function capV(p,lines,fs){fs=fs||58;const mx=Math.max(...lines.map(l=>l.length));fs=Math.min(fs,(1000-130)/(mx*0.76));const w=Math.min(1000,mx*fs*0.76+130);const h=lines.length*(fs*1.42)+54;const c=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:Math.min(60,h/2),fill:'#06303A',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:Math.min(60,h/2),fill:'none',stroke:'#FFB020','stroke-width':6},c);
 lines.forEach((l,i)=>txt(c,l,0,-h/2+27+fs*1.08+i*fs*1.42,fs,'#FFFFFF','bold'));return c;}
const CAPY=1560;
// entrata dal basso con dissolvenza (lenta): nessun elemento entra da fuori quadro
function rise(t,a,d,n,y,dy,sc){const k=sl(t,a,d||.9);T(n,n._x,y+(1-k)*(dy||140),0,(sc||1));op(n,seg(t,a,a+(d||.9)*.6));}
const S=[
// Layout (regola n.7): titoletto in alto (y130), fascia y 520-760 LIBERA per la didascalia che l'utente mette in CapCut, grafica sopra e sotto.
// ---- 1: DUE COLLEGHI 64 vs 67 ----
{D:305/30,build(p){const o={};
 o.lab=topLabelV(p,'DUE COLLEGHI');
 o.pa=person(p,'#E8503A','#4A2F1F');o.pb=person(p,'#1B9F81','#2B2B2B');
 o.eq=el('g',{},p);ttl(o.eq,'=',240,YEL);
 o.q=el('g',{},p);ttl(o.q,'?',290,YEL);
 o.ca=circleN(p,112,'64','url(#g_red)');o.cb=circleN(p,112,'67','url(#g_badge)');
 o.aa=el('g',{},p);txt(o.aa,'ANNI',0,0,60,'#fff','bold');o.ab=el('g',{},p);txt(o.ab,'ANNI',0,0,60,'#fff','bold');
 o.l1=pillS(p,'STESSO STIPENDIO',940,64,'#0B4A50');o.l2=pillS(p,'STESSI CONTRIBUTI',940,64,'#0B4A50');
 o.l1._x=540;o.l2._x=540;
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  rise(t,2.7,.9,o.l1,290);rise(t,3.8,.9,o.l2,420);
  T(o.pa,260,960,0,1.6*pop(t,.3,.9));T(o.pb,820,960,0,1.6*pop(t,.9,.9));
  const sw=sl(t,7.3,.6);T(o.eq,540,1080,0,pop(t,2.0,.8)*(1-sw));T(o.q,540,1090,0,pop(t,7.9,.9));
  T(o.ca,170,1290,0,pop(t,4.8,.9));T(o.aa,170,1455,0,pop(t,4.8,.9));
  T(o.cb,910,1290,0,pop(t,6.2,.9));T(o.ab,910,1455,0,pop(t,6.2,.9));}},
// ---- 2: TRE NUMERI ----
{D:186/30,build(p){const o={};
 o.lab=topLabelV(p,'TRE NUMERI');
 o.s=stamp(p,'TI SBAGLI!',900,112,RED);
 o.c=[1,2,3].map(n=>circleN(p,140,String(n),n==3?'url(#g_red)':'url(#g_badge)'));
 o.q=[1,2,3].map(()=>{const g=el('g',{},p);ttl(g,'?',190,YEL);return g;});
 o.eye=eye(p);
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  const s=seg(t,.1,1.0);T(o.s,540,330,-4,s>0?lerp(.6,1,eo3(s)):0);op(o.s,clamp(s*2.5));
  [0,1,2].forEach(i=>{const a=2.3+i*.5;T(o.c[i],[175,540,905][i],900,0,pop(t,a,.8));T(o.q[i],[175,540,905][i],1190,0,pop(t,a+.2,.8));});
  T(o.eye,540,1480,0,1.5*pop(t,4.1,.8));}},
// ---- 3: UN SOLO ANNO SENZA CONTRIBUTI ----
{D:222/30,build(p){const o={};
 o.lab=topLabelV(p,'UN ANNO DI BUCO');
 o.tag=pillS(p,'ESEMPIO SEMPLIFICATO',900,58,'#0B4A50');o.tag._x=540;
 o.bx=[];for(let i=0;i<6;i++){const g=el('g',{},p);const gap=i==3;
  el('rect',{x:-62,y:-88,width:124,height:176,rx:22,fill:gap?'rgba(255,255,255,.14)':'url(#g_paper)',stroke:gap?RED:'#fff','stroke-width':gap?8:5,'stroke-dasharray':gap?'16 12':'',filter:'url(#g_sh2)'},g);
  txt(g,'ANNO',0,-46,30,gap?'#FFB3A3':'#0D5158','bold');
  if(gap){txt(g,'0 €',0,40,54,'#FFB3A3','bold');}else{el('path',{d:'M-30 18 l22 24 l40 -48',fill:'none',stroke:'#1B9F81','stroke-width':16,'stroke-linecap':'round','stroke-linejoin':'round'},g);}
  o.bx.push(g);}
 o.ar=bigArrow(p);
 o.coins=el('g',{},p);for(let i=0;i<4;i++){const c=goldCoin(o.coins,0,-i*30,100,32,24);if(i==3)o.top=c;}
 o.pl=el('g',{},p);plateRect(o.pl,-330,-150,660,300,56);txt(o.pl,'−50 €',0,52,150,RED,'bold');txt(o.pl,'AL MESE · LORDI',0,122,52,INK,'bold');o.pl._x=620;
 o.v=pillS(p,'PER TUTTA LA VITA!',900,68,'url(#g_badge)');o.v._x=540;
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  rise(t,2.6,.8,o.tag,330,100);
  o.bx.forEach((g,i)=>{T(g,108+168*i,900,0,1.2*pop(t,.3+i*.3,.7));});
  T(o.ar,612,1065,0,.8*pop(t,3.3,.8));
  rise(t,3.7,.9,o.pl,1320,200,1.15);
  T(o.coins,120,1380,0,1.15*pop(t,3.9,.8));
  const f=seg(t,4.6,5.5);o.top.setAttribute('transform','translate('+(f*220)+' '+(-f*160)+')');op(o.top,1-f);
  rise(t,6.0,.8,o.v,1600,100);}},
// ---- 4: IL CONTO FINALE ----
{D:257/30,build(p){const o={};
 o.lab=topLabelV(p,'IL CONTO FINALE');
 o.a=circleN(p,140,'64','url(#g_red)');o.b=circleN(p,140,'67','url(#g_badge)');
 o.aa=el('g',{},p);txt(o.aa,'ANNI',0,0,64,'#fff','bold');o.ab=el('g',{},p);txt(o.ab,'ANNI',0,0,64,'#fff','bold');
 o.ar=el('path',{d:'M-90 -22 H40 V-62 L120 0 L40 62 V22 H-90Z',fill:YEL,stroke:'#fff','stroke-width':8,'stroke-linejoin':'round',filter:'url(#g_sh2)'},p);
 o.pl=el('g',{},p);plateRect(o.pl,-420,-130,840,260,56);txt(o.pl,'??? €',0,50,150,'#C99700','bold');
 o.lk=lockG(p,1.2);
 o.pill=pillS(p,'ALLA FINE DEL VIDEO',860,60,'#0B4A50');o.pill._x=540;
 o.bar=el('g',{},p);el('rect',{x:-430,y:-22,width:860,height:44,rx:22,fill:'rgba(255,255,255,.25)',stroke:'#fff','stroke-width':4},o.bar);
 o.fill=el('rect',{x:-430,y:-22,width:0,height:44,rx:22,fill:YEL},o.bar);
 el('path',{d:'M-405 -14 L-381 0 L-405 14Z',fill:'#fff'},o.bar);
 o.flag=el('g',{},o.bar);el('rect',{x:396,y:-62,width:8,height:78,fill:'#fff'},o.flag);el('path',{d:'M404 -62 h54 l-14 20 l14 20 h-54Z',fill:RED,stroke:'#fff','stroke-width':3},o.flag);
 o.mk=el('circle',{r:32,fill:YEL,stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},p);
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  T(o.a,215,330,0,pop(t,.5,.9));T(o.aa,215,538,0,pop(t,.5,.9));
  T(o.b,865,330,0,pop(t,1.4,.9));T(o.ab,865,538,0,pop(t,1.4,.9));
  T(o.ar,540,330,0,1.2*pop(t,2.3,.9));
  T(o.pl,540,1010,0,1.1*pop(t,3.3,.9));T(o.lk,935,860,12,pop(t,3.9,.8));
  rise(t,5.0,.8,o.pill,1290,100);
  T(o.bar,540,1430,0,pop(t,5.2,.8));
  const m=eio(seg(t,6.3,7.7));const x=lerp(-405,405,m);o.fill.setAttribute('width',Math.max(0,x+430));T(o.mk,540+x,1430,0,pop(t,5.4,.8));}},
// ---- 5: COSA TROVI NEL VIDEO ----
{D:238/30,build(p){const o={};
 o.lab=topLabelV(p,'COSA TROVI');
 o.t=el('g',{},p);ttl(o.t,'NEL VIDEO:',130,YEL);
 const defs=[['CALCOLO','PASSO PASSO'],['TEST','VERO O FALSO'],['CONTROLLO','SU MAI INPS']];
 o.c=defs.map((d,i)=>{const g=el('g',{},p);plateRect(g,-480,-140,960,280,56);
  const ic=el('g',{},g);ic.setAttribute('transform','translate(-345 0) scale(1.15)');
  el('circle',{r:84,fill:'url(#g_badge)',stroke:'#fff','stroke-width':7},ic);
  if(i==0){el('rect',{x:-40,y:-52,width:80,height:104,rx:12,fill:'#fff'},ic);el('rect',{x:-30,y:-42,width:60,height:24,rx:6,fill:'#0B4A50'},ic);for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('circle',{cx:-20+c*20,cy:-4+r*22,r:6,fill:'#1B9F81'},ic);}
  if(i==1){const a=check(ic,34);a.setAttribute('transform','translate(-26 -4)');const b=crossC(ic,34);b.setAttribute('transform','translate(30 24)');}
  if(i==2){el('rect',{x:-44,y:-52,width:64,height:84,rx:10,fill:'#fff'},ic);[-30,-12,6].forEach(y=>el('rect',{x:-32,y:y,width:40,height:8,rx:4,fill:'#9FB4B9'},ic));el('circle',{cx:14,cy:14,r:26,fill:'none',stroke:YEL,'stroke-width':10},ic);el('line',{x1:32,y1:34,x2:52,y2:56,stroke:YEL,'stroke-width':12,'stroke-linecap':'round'},ic);}
  txt(g,d[0],-215,-8,78,INK,'bold','start');txt(g,d[1],-215,78,78,'#1B9F81','bold','start');g._x=540;return g;});
 o.k=defs.map(()=>check(p,46));
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));T(o.t,540,330,0,pop(t,.2,.9));
  [.8,2.8,4.6].forEach((a,i)=>{rise(t,a,.9,o.c[i],[900,1200,1500][i],160);});
  [5.4,5.8,6.2].forEach((a,i)=>T(o.k[i],975,[785,1085,1385][i],0,pop(t,a,.7)));}},
// ---- 6: GUARDALO ADESSO ----
{D:150/30,build(p){const o={};
 o.lab=topLabelV(p,'VIDEO COMPLETO');
 o.t1=el('g',{},p);ttl(o.t1,'GUARDALO',130,'#fff');o.t2=el('g',{},p);ttl(o.t2,'ADESSO!',130,YEL);
 o.pb=playBtn(p);o.pill=pillS(p,'VIDEO CORRELATO',940,76,'#0B4A50');o.pill._x=540;
 o.r1=el('circle',{r:40,fill:'none',stroke:'#fff','stroke-width':10},p);o.r2=el('circle',{r:40,fill:'none',stroke:'#fff','stroke-width':10},p);
 o.ar=bigArrow(p);
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  T(o.t1,540,290,0,pop(t,.1,.9));T(o.t2,540,430,0,pop(t,.4,.9));
  T(o.pb,540,980,0,1.15*pop(t,.7,.9));
  rise(t,1.4,.8,o.pill,1330,100);
  [[o.r1,1.8],[o.r2,2.3]].forEach(([r,a])=>{const k=seg(t,a,a+.9);T(r,615,1010,0,k>0?lerp(.6,4.0,eo3(k)):0);op(r,k>0?(1-k)*.9:0);});
  T(o.ar,540,1540,0,1.1*pop(t,2.6,.8));}},
];
S.forEach(s=>{s.sb=[{s:0,e:s.D}];});
