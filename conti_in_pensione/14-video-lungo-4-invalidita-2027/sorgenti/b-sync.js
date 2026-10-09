// ===== V3: motore sincronizzato sulla voce (blocchi 6-30) =====
function bnW(s,fs,sub,minw){return Math.max(minw||360,s.length*fs*0.64+90,sub?sub.length*36*0.74+90:0);}
function bigNum(p,s,fs,fill,sub,subfill,minw){const g=el('g',{},p);
 const w=bnW(s,fs,sub,minw);const paper=(!fill||fill==='url(#g_paper)');const h=fs*1.55+(sub?58:0);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:h,rx:34,fill:fill||'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:h,rx:34,fill:'none',stroke:'#fff','stroke-opacity':.8,'stroke-width':4},g);
 txt(g,s,0,fs*0.3,fs,paper?INK:(fill===AMB?'#5A3300':'#fff'),'900');
 if(sub)txt(g,sub,0,fs*0.3+62,36,subfill||(paper?GRN:(fill===AMB?'#5A3300':'#fff')),'bold');
 return g;}
// ---- tempi del parlato: ogni frase ha il suo istante, calcolato sul testo e sulla durata ----
function speech(text,dur){const lead=0.35,tail=0.5;text=text.replace(/’/g,"'");
 // modello calibrato su 69 blocchi reali: 0,145 s per sillaba + pause alla punteggiatura (virgola 0,13; due punti 0,36; punto 0,34; !? 0,47; ... 0,56)
 const T=new Array(text.length+1).fill(0);let t=0;let i=0;
 while(i<text.length){const ch=text[i];
  if(/[A-Za-zàèéìòùÀÈÉÌÒÙ]/.test(ch)){let j=i;while(j<text.length&&/[A-Za-zàèéìòùÀÈÉÌÒÙ]/.test(text[j]))j++;
   const w=text.slice(i,j);const sy=Math.max(1,(w.toLowerCase().match(/[aeiouàèéìòù]+/g)||[]).length);const d=0.145*sy;
   for(let k=i;k<j;k++)T[k]=t+d*(k-i)/(j-i);t+=d;i=j;continue;}
  T[i]=t;
  if(ch===',')t+=0.129;else if(ch===':'||ch===';')t+=0.363;else if(ch==='!'||ch==='?')t+=0.467;
  else if(ch==='.'){t+=(text[i+1]==='.'||text[i-1]==='.')?0.187:0.336;}
  i++;}
 T[text.length]=t;const tot=t;
 return function(p){let off=0;if(typeof p==='number')return p;if(Array.isArray(p)){off=p[1];p=p[0];}p=p.replace(/’/g,"'");
  const k=text.indexOf(p);if(k<0)throw new Error('frase non trovata: '+p);
  return lead+(T[k]/tot)*(dur-lead-tail)+off;};}
const I=(k,a,x,y,at,s,r)=>({k,a,x,y,at,s,r});
function EQ(y,parts,fs0,minw0){fs0=fs0||76;minw0=minw0||280;const gap=34;
 const ws=parts.map(p=>p[0]=='op'?100:bnW(p[1],(p[3]&&p[3].fs)||fs0,p[3]&&p[3].sub,minw0));
 const tot=ws.reduce((a,b)=>a+b,0)+gap*(parts.length-1);let x=960-tot/2;const out=[];
 parts.forEach((p,i)=>{const cx=x+ws[i]/2;x+=ws[i]+gap;const o=p[3]||{};
  if(p[0]=='op')out.push(I('op',[p[1]],cx,y,p[2]));
  else{const fs=o.fs||fs0;out.push(I('num',[p[1],fs,o.fill||'url(#g_paper)',o.sub,o.subfill,minw0],cx,y+0.125*fs-(o.sub?29:0),p[2]));}});
 return out;}
const BUILD={
 num:(g,...a)=>bigNum(g,...a),
 tag:(g,s,fill,col,fs)=>tag(g,s,0,fill,col,fs),
 op:(g,sym)=>{el('circle',{r:52,fill:'#fff',stroke:AMB,'stroke-width':8,filter:'url(#g_sh2)'},g);txt(g,sym,0,22,60,INK,'900');},
 cal:(g,h,b,bs,sub)=>{const w=el('g',{transform:'translate(0 -250) scale(0.9)'},g);calendarPage(w,h,b,bs,sub);},
 pay:(g,t,a)=>payslip(g,t,a),
 med:(g)=>medal(g,true),
 arR:(g)=>arrowRight(g,AMB),arD:(g)=>arrowDown(g,AMB),
 warn:(g)=>warn(g),chk:(g,r)=>checkBadge(g,r||100),q:(g,r)=>qMark(g,r||90),
 stamp:(g,s,col,fs)=>stamp(g,s,0,col,fs),
 doc:(g,t,w,h,hc,fs)=>{docCard(g,t,w,h,hc,fs);for(let i=0;i<3;i++)el('rect',{x:-w/2+50,y:-h/2+120+i*50,width:i%2?w*0.5:w*0.7,height:16,rx:8,fill:'#C3D3D7'},g);},
 circ:(g,n,fill)=>circN(g,64,n,fill||'url(#g_badge)'),
 cross:(g,w,h)=>el('path',{d:`M${-w} ${-h} L${w} ${h} M${w} ${-h} L${-w} ${h}`,stroke:RED_,'stroke-width':30,'stroke-linecap':'round',opacity:.92},g),
 seg:(g,w,h,fill,label,sub)=>{el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:20,fill:fill,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  if(label)txt(g,label,0,15,44,fill===AMB?'#5A3300':'#fff','900');if(sub)txt(g,sub,0,h/2+52,34,LT,'bold');},
 step:(g,w,h,fill,label)=>{el('rect',{x:-w/2,y:-h,width:w,height:h,rx:18,fill:fill,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);txt(g,label,0,-h+66,56,fill===AMB?'#5A3300':'#fff','900');},
 trow:(g,w,label,pct,fill)=>{el('rect',{x:-w/2,y:-55,width:w,height:110,rx:30,fill:'url(#g_paper)',filter:'url(#g_sh2)'},g);
  txt(g,label,-w/2+60,14,38,INK,'bold','start');
  el('rect',{x:w/2-310,y:-47,width:290,height:94,rx:26,fill:fill},g);txt(g,pct,w/2-165,18,50,fill===AMB?'#5A3300':'#fff','900');},
 basket:(g)=>{el('path',{d:'M-170 -40 L170 -40 L130 110 L-130 110 Z',fill:AMB,stroke:'#fff','stroke-width':8,'stroke-linejoin':'round',filter:'url(#g_sh)'},g);
  el('path',{d:'M-120 -40 Q0 -190 120 -40',fill:'none',stroke:'#fff','stroke-width':14,'stroke-linecap':'round'},g);
  [[-90,-70,'#E4412C'],[-30,-95,'#2FBF9B'],[35,-75,'#FFFFFF'],[90,-65,'#7FF0D2']].forEach(d=>el('circle',{cx:d[0],cy:d[1],r:36,fill:d[2],stroke:'#0B4A50','stroke-width':4},g));},
 shield:(g)=>shield(g),
 mbars:(g)=>{const h=[60,70,80,95,105,120,135,150,300];const m='GFMAMGLAS';
  el('rect',{x:-430,y:0,width:860,height:8,rx:4,fill:LT},g);
  h.forEach((v,i)=>{const x=-400+i*100;el('rect',{x:x-32,y:-v,width:64,height:v,rx:10,fill:i==8?RED_:'#2B6F77',stroke:'#fff','stroke-width':3},g);txt(g,m[i],x,52,32,'#fff','bold');});},
 avg:(g)=>{el('line',{x1:-450,y1:0,x2:450,y2:0,stroke:AMB,'stroke-width':8,'stroke-dasharray':'26 14','stroke-linecap':'round'},g);},
};
function mkBlk(text,dur,scenes){const sp=speech(text,dur);
 const st=scenes.map((sc,i)=>i==0?0:Math.max(0.8,sp(sc.at)-0.3+(sc.sh||0)));
 scenes.forEach((sc,i)=>{const s=st[i],e=(i<scenes.length-1)?st[i+1]:dur;
  sc.items.forEach(it=>{const a=Math.max(0.5,sp(it.at)-0.2-s);
   if(a+0.6>e-s-0.5)console.warn('TARDI blocco: '+JSON.stringify(it.at)+' compare a '+(a+s).toFixed(2)+' fine scena '+e.toFixed(2));});
  SB.push({s,e,build(g){const o={items:[]};
   o.top=el('g',{},g);topLabel(o.top,sc.top);
   o.cap=el('g',{},g);cap(o.cap,sc.cap,sc.capSize||44);
   sc.items.forEach(it=>{const n=el('g',{},g);BUILD[it.k](n,...it.a);o.items.push({n,it});});
   this.o=o;},
  update(t){const o=this.o;T(o.top,960,100,0,1);T(o.cap,960,950,0,pop(t,0.2,0.8));
   o.items.forEach(({n,it})=>{const a=Math.max(0.5,sp(it.at)-0.2-s);T(n,it.x,it.y,it.r||0,(it.s||1)*pop(t,a,a+0.55));});}});});
 window.__SC=scenes.map((sc,i)=>[st[i],(i<scenes.length-1)?st[i+1]:dur]);}
Object.assign(BUILD,{
 calc:(g)=>calc(g),
 vf:(g,v)=>vf(g,v),
 br:(g,url,w,h)=>browser(g,url,w,h),
 row:(g,label,w,ok)=>row(g,label,0,0,w,ok),
 medm:(g)=>medal(g,false),
 bubble:(g,w,h)=>{el('path',{d:`M${-w/2+40} ${-h/2} H${w/2-40} Q${w/2} ${-h/2} ${w/2} ${-h/2+40} V${h/2-40} Q${w/2} ${h/2} ${w/2-40} ${h/2} H-60 L-130 ${h/2+60} L-120 ${h/2} H${-w/2+40} Q${-w/2} ${h/2} ${-w/2} ${h/2-40} V${-h/2+40} Q${-w/2} ${-h/2} ${-w/2+40} ${-h/2} Z`,fill:'url(#g_paper)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh)'},g);
  [-1,0,1].forEach(i=>el('rect',{x:-w/2+60,y:-h/2+50+i*58+58,width:i==1?w*0.4:w*0.7,height:18,rx:9,fill:'#C3D3D7'},g));},
 btn:(g,s)=>{el('rect',{x:-260,y:-60,width:520,height:120,rx:60,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh)'},g);txt(g,s,0,20,56,'#fff','900');},
 bell:(g)=>{el('path',{d:'M0 -120 Q-100 -120 -100 -20 V50 L-130 90 H130 L100 50 V-20 Q100 -120 0 -120 Z',fill:AMB,stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},g);el('circle',{cx:0,cy:120,r:26,fill:AMB,stroke:'#fff','stroke-width':6},g);el('circle',{cx:0,cy:-140,r:16,fill:AMB},g);},
 hl:(g,s,fill)=>{const w=s.length*38*0.7+110;el('rect',{x:-w/2,y:-70,width:w,height:140,rx:24,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);el('rect',{x:-w/2,y:-70,width:w,height:44,rx:24,fill:fill||RED_},g);el('rect',{x:-w/2,y:-48,width:w,height:22,fill:fill||RED_},g);txt(g,'TITOLO',0,-40,28,'#fff','bold');txt(g,s,0,40,56,INK,'900');},
});
Object.assign(BUILD,{
 dbg:(g,w,h)=>{el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'#0B4A50',filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2,y:-h/2,width:w,height:74,rx:26,fill:GRN},g);el('rect',{x:-w/2,y:-h/2+44,width:w,height:30,fill:GRN},g);txt(g,'DISCLAIMER',0,-h/2+50,38,'#fff','bold');},
 dline:(g,s,col,fs)=>txt(g,s,0,0,fs,col,'bold'),
});
