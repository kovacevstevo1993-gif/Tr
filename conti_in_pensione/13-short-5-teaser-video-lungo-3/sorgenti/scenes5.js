// ===== SHORT 5 - teaser video lungo 3 (1080x1920, 30 fps) =====
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

function thumb(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-96*s,y:-8*s,width:44*s,height:96*s,rx:10*s,fill:'#0B4A50',stroke:'#fff','stroke-width':6*s},g);
 el('path',{d:`M${-40*s} ${-4*s} L${-6*s} ${-78*s} Q${20*s} ${-96*s} ${32*s} ${-64*s} L${24*s} ${-26*s} H${86*s} Q${112*s} ${-24*s} ${104*s} ${8*s} L${92*s} ${62*s} Q${86*s} ${88*s} ${60*s} ${88*s} H${-40*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);return g;}
function bell(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
function card(p,x,y,w,h,r){const g=el('g',{},p);plateRect(g,-w/2,-h/2,w,h,r||50);return g;}
const S=[
// ---- 1: 4.000 EURO, +3% = 120? ----
{D:317/30,build(p){const o={};
 o.lab=topLabelV(p,'RIVALUTAZIONE');
 o.pl=card(p,0,0,820,340);txt(o.pl,'4.000 €',0,40,130,INK,'bold');txt(o.pl,'PENSIONE LORDA AL MESE',0,118,40,'#1B9F81','bold');
 o.pc=pillS(p,'+3%',300,92,'url(#g_badge)');
 o.calc=card(p,0,0,940,200,50);txt(o.calc,'4.000 × 3% = 120 €?',0,22,64,INK,'bold');o.calc._x=540;
 o.st=stamp(p,'SBAGLIATO!',800,104,RED);
 o.pill=pillS(p,'NE ARRIVANO MENO',900,64,'url(#g_red)');o.pill._x=540;
 o.cap=capV(p,['LA PERCENTUALE È LA STESSA,','MA IL CONTO CAMBIA']);
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  T(o.pl,540,560,0,pop(t,.3,.9));T(o.pc,850,360,6,pop(t,1.9,.9));
  rise(t,3.6,.9,o.calc,900,120);
  const s=seg(t,5.6,6.4);T(o.st,540,1130,-5,s>0?lerp(1.5,1,eo3(s)):0);op(o.st,clamp(s*3));
  rise(t,6.7,.8,o.pill,1320,100);
  T(o.cap,540,CAPY,0,pop(t,7.7,.8));}},
// ---- 2: LE FASCE ----
{D:293/30,build(p){const o={};
 o.lab=topLabelV(p,'LE FASCE');
 o.a=card(p,0,0,440,200,44);txt(o.a,'2.000 €',0,26,76,INK,'bold');
 o.b=card(p,0,0,440,200,44);txt(o.b,'4.000 €',0,26,76,INK,'bold');
 o.pa=pillS(p,'+3%',260,60,'url(#g_badge)');o.pb=pillS(p,'+3%',260,60,'url(#g_badge)');
 o.st=stamp(p,'NON PER TUTTI!',800,76,RED);
 o.stairs=[0,1,2].map(i=>{const h=[130,260,390][i];const g=el('g',{},p);
  el('rect',{x:-135,y:-h,width:270,height:h,rx:22,fill:['#1B9F81','#E0A100','#D23A25'][i],stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},g);g._h=h;return g;});
 o.lb=['100%','90%','75%'].map((s,i)=>{const g=el('g',{},p);txt(g,s,0,0,74,'#fff','bold');return g;});
 o.cap=capV(p,['PIÙ SALI,','MENO TI RIVALUTANO']);
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  T(o.a,290,420,0,pop(t,.3,.8));T(o.b,790,420,0,pop(t,.7,.8));
  T(o.pa,290,610,0,pop(t,1.0,.7));T(o.pb,790,610,0,pop(t,1.4,.7));
  const s=seg(t,1.8,2.5);T(o.st,540,800,-4,s>0?lerp(1.5,1,eo3(s)):0);op(o.st,clamp(s*3));
  [3.5,4.8,6.0].forEach((a,i)=>{const k=eo3(seg(t,a,a+.9));const x=[255,540,825][i];
   o.stairs[i].setAttribute('transform','translate('+x+' 1420) scale(1 '+Math.max(.001,k)+')');
   T(o.lb[i],x,1420-o.stairs[i]._h+80,0,pop(t,a+.5,.7));});
  T(o.cap,540,CAPY,0,pop(t,7.0,.8));}},
// ---- 3: SOGLIE 2026 ----
{D:292/30,build(p){const o={};
 o.lab=topLabelV(p,'NEL 2026 · INPS');
 const rows=[['FINO A','~2.400 €','100%','url(#g_badge)'],['DA ~2.400 A','~3.000 €','90%','url(#g_amber)'],['OLTRE','~3.000 €','75%','url(#g_red)']];
 o.r=rows.map(d=>{const g=card(p,0,0,940,210,50);
  txt(g,d[0],-420,-12,40,'#1B9F81','bold','start');txt(g,d[1],-420,64,70,INK,'bold','start');
  const b=el('g',{},g);el('rect',{x:120,y:-80,width:290,height:160,rx:80,fill:d[3],stroke:'#fff','stroke-width':6},b);txt(b,d[2],265,28,84,'#fff','bold');g._x=540;return g;});
 o.cap=capV(p,['PIÙ SALI,','MENO TI RIVALUTANO']);
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  [.9,4.1,5.7].forEach((a,i)=>rise(t,a,.9,o.r[i],[520,790,1060][i],140));
  T(o.cap,540,CAPY,0,pop(t,7.6,.8));}},
// ---- 4: ESEMPIO AL 3% ----
{D:305/30,build(p){const o={};
 o.lab=topLabelV(p,'ESEMPIO AL 3%');
 o.pl=card(p,0,0,800,260);txt(o.pl,'4.000 €',0,34,112,INK,'bold');txt(o.pl,'LORDI AL MESE',0,100,40,'#1B9F81','bold');
 o.ok=card(p,0,0,860,280,56);txt(o.ok,'+111 €',0,44,150,'#13805F','bold');txt(o.ok,'CIRCA, AL MESE',0,110,40,INK,'bold');
 o.no=el('g',{},p);o.no.appendChild(pillS(o.no,'NON 120 €',620,64,'url(#g_red)'));
 o.st=stamp(p,'SOLO UN ESEMPIO',900,64,RED);
 o.ar=bigArrow(p);
 o.cap=capV(p,['PERCENTUALE VERA:','A NOVEMBRE']);
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  T(o.pl,540,420,0,pop(t,.9,.9));
  T(o.ar,540,680,0,.8*pop(t,2.5,.8));
  T(o.ok,540,940,0,pop(t,3.5,.9));
  T(o.no,540,1170,0,pop(t,5.1,.8));
  const s=seg(t,6.4,7.2);T(o.st,540,1345,-3,s>0?lerp(1.5,1,eo3(s)):0);op(o.st,clamp(s*3));
  T(o.cap,540,CAPY,0,pop(t,8.0,.8));}},
// ---- 5: SECONDA TRAPPOLA ----
{D:328/30,build(p){const o={};
 o.lab=topLabelV(p,'SECONDA TRAPPOLA');
 o.w=tri(p,110);
 o.pl=card(p,0,0,780,330);txt(o.pl,'4,2%',0,36,170,RED,'bold');txt(o.pl,'INFLAZIONE GENERALE',0,118,44,INK,'bold');
 o.ne=el('g',{},p);el('circle',{r:78,fill:RED,stroke:'#fff','stroke-width':9,filter:'url(#g_sh2)'},o.ne);txt(o.ne,'≠',0,34,110,'#fff','bold');
 o.pe=card(p,0,0,860,240,50);txt(o.pe,'% DELLA TUA PENSIONE',0,24,52,INK,'bold');
 o.p1=pillS(p,'CALCOLO PASSO PASSO',940,64,'url(#g_badge)');o.p1._x=540;
 o.p2=pillS(p,'TEST VERO O FALSO',940,64,'#0B4A50');o.p2._x=540;
 o.pb=playBtn(p);o.c1=capV(p,['4,2% NON È LA','TUA PERCENTUALE']);o.c2=capV(p,['NEL VIDEO COMPLETO']);
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  const ex=1-eio(seg(t,6.8,7.4));
  T(o.w,540,430,-6,pop(t,.4,.9)*ex);
  T(o.pl,540,800,0,pop(t,2.0,.9)*ex);
  T(o.ne,540,1070,0,pop(t,4.2,.8)*ex);
  T(o.pe,540,1290,0,pop(t,4.7,.9)*ex);
  rise(t,7.4,.8,o.p1,700,100);rise(t,8.5,.8,o.p2,900,100);T(o.pb,540,1210,0,.6*pop(t,9.2,.8));
  T(o.c1,540,CAPY,0,pop(t,5.3,.8)*ex);T(o.c2,540,CAPY,0,pop(t,7.5,.8));}},
// ---- 6: GUARDA, ISCRIVITI, MI PIACE ----
{D:239/30,build(p){const o={};
 o.lab=topLabelV(p,'GUARDALO ORA');
 o.pb=playBtn(p);o.pill=pillS(p,'VIDEO CORRELATO',900,70,'#0B4A50');o.pill._x=540;
 o.sub=pillS(p,'ISCRIVITI',440,72,'url(#g_red)');o.bl=bell(p,.7);o.lk=thumb(p,1.0);
 o.nov=pillS(p,'A NOVEMBRE: % UFFICIALE',960,58,'#0B4A50');o.nov._x=540;
 o.cap=capV(p,['GUARDA, ISCRIVITI','E METTI MI PIACE']);
 return o;},
 update(t,o){T(o.lab,540,130,0,pop(t,0,.8));
  T(o.pb,540,540,0,.95*pop(t,.2,.8));
  rise(t,.9,.7,o.pill,860,90);
  T(o.sub,290,1090,0,pop(t,2.7,.8));T(o.bl,590,1090,0,pop(t,3.2,.7));
  T(o.lk,830,1090,0,pop(t,4.4,.8));
  rise(t,5.3,.7,o.nov,1320,90);
  T(o.cap,540,CAPY,0,pop(t,5.9,.7));}},
];
S.forEach(s=>{s.sb=[{s:0,e:s.D}];});
function playBtn(p){const g=el('g',{filter:'url(#g_sh)'},p);el('rect',{x:-330,y:-205,width:660,height:410,rx:90,fill:'url(#g_red)',stroke:'#fff','stroke-width':10},g);el('path',{d:'M-70 -110 L130 0 L-70 110Z',fill:'#fff','stroke-linejoin':'round',stroke:'#fff','stroke-width':26},g);return g;}
document.querySelector('defs').insertAdjacentHTML('beforeend','<linearGradient id="g_amber" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC93B"/><stop offset="1" stop-color="#C98500"/></linearGradient>');
