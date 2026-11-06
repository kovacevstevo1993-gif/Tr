// ===== motore slide: ogni scena = riga di oggetti + riga di etichette + didascalia, con disposizione automatica =====
const FILL={p:['url(#g_paper)',INK,GRN],g:['url(#g_badge)','#fff','#D6F5EC'],r:['url(#g_red)','#fff','#FFE3DE'],d:['#0B4A50','#fff',LT],a:[AMB,'#5A3300','#5A3300'],m:[MINT,'#07302A','#07302A']};
const TFILL={a:[AMB,'#5A3300'],g:[MINT,'#07302A'],r:[RED_,'#fff'],d:['#0B4A50','#fff'],w:['url(#g_badge)','#fff']};
const C=(t,b,s,f,w)=>({k:'card',t,b,s,f,w}),OP=s=>({k:'op',s}),PG=()=>({k:'piggy'}),W_=()=>({k:'warn'}),K=()=>({k:'check'}),Q=()=>({k:'q'}),AR=()=>({k:'ar'}),AD=()=>({k:'ad'}),CA=()=>({k:'calc'}),MG=()=>({k:'mag'}),CO=()=>({k:'coin'});
const PE=f=>({k:'person',f}),DR=(n,f)=>({k:'door',n,f}),CAL=(h,b,s,bs)=>({k:'cal',h,b,s,bs}),BR=(url,rows,w,h)=>({k:'br',url,rows,w,h}),DC=(t,lines,w,h,hc)=>({k:'doc',t,lines,w,h,hc}),BA=(n,hl)=>({k:'bars',n,hl}),DOT=n=>({k:'dots',n}),DN=p=>({k:'donut',p}),ST=(s,col)=>({k:'stamp',s,col});
const STK=(n,s)=>({k:'stack',n,s}),TL=(a,b,hl,lab,step,w)=>({k:'tl',a,b,hl,lab,step,w}),NT=(n,s)=>({k:'notes',n,s}),BAL=(l,r,tilt)=>({k:'balance',l,r,tilt}),STP=(labels,on)=>({k:'steps',labels,on}),PIE=(p,s,col)=>({k:'pie',p,s,col}),CLK=s=>({k:'clock',s}),PPL=n=>({k:'people',n}),MB=(n,slope,hi,s)=>({k:'minibars',n,slope,hi,s});
const T_=(s,f,w,fs)=>({s,f:f||'a',w,fs});
function wlen(s,fs){return s.length*fs*0.86;}
function mkItem(p,o){
 const g=el('g',{},p);let w=100,h=100,oy=0,ox=0,upd=null;
 switch(o.k){
 case 'card':{w=o.w||440;const lines=String(o.b).split('|');const hasT=!!o.t,hasS=!!o.s;const h0=o.h||((hasT?300:250)+(lines.length>1?60:0));h=h0;
  const [bg,fg,sg]=FILL[o.f||'p'];
  el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:bg,filter:'url(#g_sh)'},g);
  let y0=-h/2;
  if(hasT){const th=o.th||GRN;el('rect',{x:-w/2,y:-h/2,width:w,height:68,rx:30,fill:th},g);el('rect',{x:-w/2,y:-h/2+38,width:w,height:30,fill:th},g);
   txt(g,o.t,0,-h/2+46,Math.min(36,(w-70)/(o.t.length*0.86)),'#fff','bold');y0+=68;}
  const room=h-(hasT?68:0)-(hasS?64:0)-30;const ml=Math.max.apply(null,lines.map(x=>x.length));
  const fs=Math.min(o.fs||100,(w-70)/(ml*0.86),room/(lines.length*1.25));
  const cy=(y0+(h/2-(hasS?64:0)))/2;
  lines.forEach((ln,i)=>txt(g,ln,0,cy+(i-(lines.length-1)/2)*fs*1.2+fs*0.34,fs,fg,'900'));
  if(hasS)txt(g,o.s,0,h/2-26,Math.min(30,(w-70)/(o.s.length*0.86)),sg,'bold');
  break;}
 case 'op':{w=100;h=100;el('circle',{r:50,fill:'#0B4A50',stroke:'#fff','stroke-width':6},g);txt(g,o.s,0,20,54,'#fff','900');break;}
 case 'piggy':{piggy(g);w=440;h=370;ox=-15;oy=9;break;}
 case 'warn':{warn(g);w=370;h=310;oy=0;break;}
 case 'check':{checkBadge(g,90);w=200;h=200;break;}
 case 'q':{qBubble(g,100);w=210;h=210;break;}
 case 'ar':{arrowRight(g,AMB);w=160;h=160;break;}
 case 'ad':{arrowDown(g,AMB);w=170;h=160;break;}
 case 'calc':{calc(g);w=230;h=310;break;}
 case 'mag':{magnifier(g);w=240;h=240;ox=-26;oy=-26;break;}
 case 'coin':{coinS(g,55);w=120;h=120;break;}
 case 'person':{medal(g,!!o.f);w=390;h=390;break;}
 case 'door':{doorN(g,o.n,o.f||['url(#g_red)','url(#g_badge)','url(#g_head)'][o.n-1]);w=440;h=730;oy=48;break;}
 case 'cal':{calendarPage(g,o.h,o.b,o.bs||250,o.s||'');w=480;h=640;oy=-256;break;}
 case 'br':{w=o.w||900;h=o.h||520;browser(g,o.url,w,h);(o.rows||[]).forEach((r,i)=>row(g,r,0,-h/2+170+i*96,w-90,true));break;}
 case 'doc':{w=o.w||560;h=o.h||430;docCard(g,o.t,w,h,o.hc||GRN,Math.min(38,(w-70)/(o.t.length*0.86)));
  (o.lines||[]).forEach((l,i)=>{const y=-h/2+130+i*62;el('rect',{x:-w/2+30,y:y-26,width:w-60,height:48,rx:14,fill:'#D6F5EC'},g);txt(g,l,0,y+10,Math.min(30,(w-100)/(l.length*0.86)),INK,'bold');});break;}
 case 'bars':{const b=bars(g,o.n);w=1150;h=520;oy=160;
  upd=(t,a)=>{for(let i=0;i<o.n;i++){const k=eo3(seg(t,a+i*0.06,a+0.5+i*0.06));let col=DIM;
   (o.hl||[]).forEach((hl,gi)=>{if(i>=hl[0]&&i<hl[1]&&t>a+0.5+gi*0.7)col=hl[2]==='a'?AMB2:MINT;});setBar(b,i,k,col);}};break;}
 case 'dots':{const d=dotsRow(g,o.n,0);w=o.n*42;h=40;upd=(t,a)=>{const nd=Math.floor(clamp((t-a-0.3)/0.06,0,o.n));d.a.forEach((c,i)=>lightDot(c,i<nd,0.5));};break;}
 case 'donut':{const d=donut(g,170,64);w=420;h=420;upd=(t,a)=>setDonut(d,(o.p||0.33)*eio(seg(t,a+0.2,a+1.2)));break;}

 case 'stack':{const n=o.n||5;w=Math.max(260,n*0+300);h=60+n*34+70;
  for(let i=0;i<n;i++){const yy=h/2-60-i*34;goldCoin(g,0,yy-70,120,36,26);}
  coinS(g,48).setAttribute('transform','translate(0 '+(-h/2+30)+')');if(o.s)txt(g,o.s,0,h/2-8,36,'#fff','bold');break;}
 case 'tl':{const a=o.a,b=o.b,W=o.w||1500;w=W+80;h=170;
  el('rect',{x:-W/2,y:-8,width:W,height:16,rx:8,fill:'#0A3F45',stroke:LT,'stroke-width':3},g);
  const n=b-a;for(let i=0;i<=n;i++){const x=-W/2+i*W/n;const hi=(o.hl||[]).some(r=>i+a>=r[0]&&i+a<=r[1]);
   el('circle',{cx:x,cy:0,r:hi?20:12,fill:hi?AMB:'#2B6F77',stroke:'#fff','stroke-width':3},g);
   if(i%(o.step||1)===0)txt(g,String(a+i),x,66,Math.min(36,W/(n+1)*0.5),hi?AMB:'#fff','bold');}
  if(o.lab)txt(g,o.lab,0,-56,38,LT,'bold');break;}
 case 'notes':{const n=o.n||3;w=n*250+40;h=210;for(let i=0;i<n;i++){const b=bill(g,o.s||'€');b.setAttribute('transform','translate('+((i-(n-1)/2)*250)+' '+(i%2?-12:12)+') scale(0.62) rotate('+((i-1)*5)+')');}break;}
 case 'balance':{w=760;h=330;el('rect',{x:-12,y:-120,width:24,height:260,rx:8,fill:'#8FA3A8'},g);el('rect',{x:-110,y:120,width:220,height:24,rx:10,fill:'#0B4A50'},g);
  const bm=el('g',{},g);el('rect',{x:-330,y:-8,width:660,height:16,rx:8,fill:'#fff'},bm);
  [[-330,o.l||'?'],[330,o.r||'?']].forEach(([x,l],i)=>{el('line',{x1:x,y1:0,x2:x,y2:90,stroke:'#fff','stroke-width':6},bm);el('rect',{x:x-110,y:90,width:220,height:70,rx:18,fill:i?'url(#g_red)':'url(#g_badge)',stroke:'#fff','stroke-width':5},bm);txt(bm,l,x,142,Math.min(40,190/Math.max(1,l.length*0.86)),'#fff','900');});
  bm.setAttribute('transform','rotate('+(o.tilt||0)+')');break;}
 case 'steps':{const n=o.labels.length;const sw_=260;w=n*sw_+(n-1)*60;h=190;
  o.labels.forEach((l,i)=>{const x=(i-(n-1)/2)*(sw_+60);circN(g,46,String(i+1),i==o.on?'url(#g_red)':'url(#g_badge)').setAttribute('transform','translate('+x+' -50)');
   el('rect',{x:x-sw_/2,y:14,width:sw_,height:64,rx:32,fill:'#fff'},g);txt(g,l,x,56,Math.min(30,(sw_-30)/(l.length*0.86)),INK,'bold');
   if(i<n-1)el('path',{d:'M'+(x+sw_/2+8)+' -50 h34',stroke:AMB,'stroke-width':10,'stroke-linecap':'round'},g);});break;}
 case 'pie':{w=360;h=360;const R=130;el('circle',{r:R,fill:'#2B6F77',stroke:'#fff','stroke-width':6},g);
  const f=o.p||0.33,a=f*Math.PI*2;el('path',{d:`M0 0 L0 ${-R} A${R} ${R} 0 ${f>.5?1:0} 1 ${R*Math.sin(a)} ${-R*Math.cos(a)} Z`,fill:o.col||AMB2,stroke:'#fff','stroke-width':4},g);
  if(o.s)txt(g,o.s,0,R+60,40,'#fff','900');h=R*2+80;break;}
 case 'clock':{w=300;h=300;el('circle',{r:130,fill:'#fff',stroke:'#0B4A50','stroke-width':12,filter:'url(#g_sh2)'},g);
  for(let i=0;i<12;i++){const a=i*Math.PI/6;el('line',{x1:Math.sin(a)*104,y1:-Math.cos(a)*104,x2:Math.sin(a)*120,y2:-Math.cos(a)*120,stroke:INK,'stroke-width':6},g);}
  el('line',{x1:0,y1:0,x2:0,y2:-86,stroke:INK,'stroke-width':10,'stroke-linecap':'round'},g);el('line',{x1:0,y1:0,x2:60,y2:20,stroke:RED_,'stroke-width':10,'stroke-linecap':'round'},g);
  if(o.s)txt(g,o.s,0,176,40,'#fff','900');h=340;break;}
 case 'people':{const n=o.n||3;w=n*150;h=190;for(let i=0;i<n;i++){const m=el('g',{},g);medal(m,i%2===0);m.setAttribute('transform','translate('+((i-(n-1)/2)*150)+' 0) scale(0.36)');}break;}
 case 'minibars':{w=620;h=300;const n=o.n||6;for(let i=0;i<n;i++){const hh=60+i*(o.slope||30);el('rect',{x:-w/2+i*(w/n)+8,y:130-hh,width:w/n-16,height:hh,rx:8,fill:(o.hi||[]).includes(i)?AMB2:MINT},g);}
  el('rect',{x:-w/2,y:130,width:w,height:8,rx:4,fill:'#fff'},g);if(o.s)txt(g,o.s,0,186,36,LT,'bold');h=340;break;}
 case 'stamp':{const col=o.col||RED_;const ww=o.s.length*52*0.86+80;stamp(g,o.s,ww,col,52);w=ww;h=100;break;}
 }
 return {g,w,h,oy,ox,upd};
}
function mk(spec,SB,TOT){
 const sw=spec.scenes.reduce((a,s)=>a+(s.w||1),0);let acc=0;
 spec.scenes.forEach((sc,si)=>{
  const s0=acc/sw*TOT;acc+=(sc.w||1);const e0=(si===spec.scenes.length-1)?TOT:acc/sw*TOT;
  SB.push({s:s0,e:e0,build(g){const o={};
   o.top=el('g',{},g);topLabel(o.top,sc.lab);
   o.items=(sc.items||[]).map(it=>mkItem(g,it));
   o.tags=(sc.tags||[]).map(tg=>{const f=TFILL[tg.f||'a'];const gg=el('g',{},g);const fs=tg.fs||44;const w=Math.max(tg.w||0,wlen(tg.s,fs)+90);tag(gg,tg.s,w,f[0],f[1],fs);return {g:gg,w:w};});
   o.cap=el('g',{},g);cap(o.cap,sc.cap,sc.cs||52);
   // disposizione automatica
   o.items2=(sc.items2||[]).map(it=>mkItem(g,it));const two=o.items2.length>0;
   const hasT=o.tags.length>0;const cy=two?345:(hasT?(o.items.length?490:520):540);const gap=36;
   const CAP1=two?300:430;
   o.items.forEach(it=>{it.sc=Math.min(1.5,CAP1/it.h);});
   if(two){let t2=o.items2.reduce((a,it)=>{it.sc=Math.min(1.2,200/it.h);return a+it.w*it.sc;},0)+gap*Math.max(0,o.items2.length-1);const k2=Math.min(1,1760/Math.max(t2,1));t2*=k2;let x2=960-t2/2;
    o.items2.forEach(it=>{it.s=it.sc*k2;it.x=x2+it.w*it.s/2;x2+=it.w*it.s+gap*k2;it.y=640;});}
   let tot=o.items.reduce((a,it)=>a+it.w*it.sc,0)+gap*Math.max(0,o.items.length-1);const k=Math.min(1,1760/Math.max(tot,1));
   tot*=k;let x=960-tot/2;
   o.items.forEach(it=>{it.s=it.sc*k;it.x=x+it.w*it.s/2;x+=it.w*it.s+gap*k;it.y=cy;});
   let tt=o.tags.reduce((a,t)=>a+t.w,0)+44*Math.max(0,o.tags.length-1);const tk=Math.min(1,1740/Math.max(tt,1));tt*=tk;let tx=960-tt/2;
   o.tags.forEach(t=>{t.s=tk;t.x=tx+t.w*tk/2;tx+=t.w*tk+44*tk;t.y=two?832:(o.items.length?790:520);});
   this.o=o;},
   update(t){const o=this.o;const dur=e0-s0;const n=o.items.length+o.tags.length;const Wd=Math.max(0.3,dur-1.7);
    T(o.top,960,100,0,1);
    const at=(i,f)=>0.3+(f!==undefined?f:(n>1?i/(n-1):0))*Wd;
    o.items.forEach((it,i)=>{const a=at(i,spec.scenes[si].items[i].at);const p=pop(t,a,a+0.45);
     T(it.g,it.x+it.ox*it.s,it.y+it.oy*it.s,0,it.s*p);if(it.upd)it.upd(t,a);});
    o.items2.forEach((it,i2)=>{const a=0.3+0.35*(o.items.length+i2)*Wd/Math.max(1,(n-1))*0+Math.min(Wd,0.9+i2*0.5);const p=pop(t,a,a+0.45);T(it.g,it.x+it.ox*it.s,it.y+it.oy*it.s,0,it.s*p);if(it.upd)it.upd(t,a);});
    o.tags.forEach((tg,j)=>{const i=o.items.length+j;const f=spec.scenes[si].tags[j].at;const a=at(i,f);T(tg.g,tg.x,tg.y,0,tg.s*pop(t,a,a+0.45));});
    T(o.cap,960,950,0,pop(t,0.2,0.8));
   }});
 });
}
function donut(p,R,w){const g=el('g',{},p);
 el('circle',{r:R,fill:'none',stroke:'#0A3F45','stroke-width':w},g);
 const arc=el('path',{fill:'none',stroke:MINT,'stroke-width':w},g);txt(g,'33%',0,36,110,'#fff','900');return {g,arc,R};}
function setDonut(d,f){const a=f*Math.PI*2;d.arc.setAttribute('d',f<=0.001?'':`M0 ${-d.R} A${d.R} ${d.R} 0 ${f>.5?1:0} 1 ${d.R*Math.sin(a)} ${-d.R*Math.cos(a)}`);}
