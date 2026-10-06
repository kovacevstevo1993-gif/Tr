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
function speech(text,dur){const lead=0.2,tail=0.35;const w=[];let tot=0;text=text.replace(/’/g,"'");
 for(const ch of text){let x=1;if(',:;'.includes(ch))x=5;else if('.!?'.includes(ch))x=9;w.push(x);tot+=x;}
 return function(p){let off=0;if(typeof p==='number')return p;if(Array.isArray(p)){off=p[1];p=p[0];}p=p.replace(/’/g,"'");
  const i=text.indexOf(p);if(i<0)throw new Error('frase non trovata: '+p);
  let c=0;for(let k=0;k<i;k++)c+=w[k];return lead+(c/tot)*(dur-lead-tail)+off;};}
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
