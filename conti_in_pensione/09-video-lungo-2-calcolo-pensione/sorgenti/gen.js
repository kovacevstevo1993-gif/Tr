// ===== motore slide: ogni scena = riga di oggetti + riga di etichette + didascalia, con disposizione automatica =====
const FILL={p:['url(#g_paper)',INK,GRN],g:['url(#g_badge)','#fff','#D6F5EC'],r:['url(#g_red)','#fff','#FFE3DE'],d:['#0B4A50','#fff',LT],a:[AMB,'#5A3300','#5A3300'],m:[MINT,'#07302A','#07302A']};
const TFILL={a:[AMB,'#5A3300'],g:[MINT,'#07302A'],r:[RED_,'#fff'],d:['#0B4A50','#fff'],w:['url(#g_badge)','#fff']};
const C=(t,b,s,f,w)=>({k:'card',t,b,s,f,w}),OP=s=>({k:'op',s}),PG=()=>({k:'piggy'}),W_=()=>({k:'warn'}),K=()=>({k:'check'}),Q=()=>({k:'q'}),AR=()=>({k:'ar'}),AD=()=>({k:'ad'}),CA=()=>({k:'calc'}),MG=()=>({k:'mag'}),CO=()=>({k:'coin'});
const PE=f=>({k:'person',f}),DR=(n,f)=>({k:'door',n,f}),CAL=(h,b,s,bs)=>({k:'cal',h,b,s,bs}),BR=(url,rows,w,h)=>({k:'br',url,rows,w,h}),DC=(t,lines,w,h,hc)=>({k:'doc',t,lines,w,h,hc}),BA=(n,hl)=>({k:'bars',n,hl}),DOT=n=>({k:'dots',n}),DN=p=>({k:'donut',p}),ST=(s,col)=>({k:'stamp',s,col});
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
   const hasT=o.tags.length>0;const cy=hasT?(o.items.length?490:520):540;const gap=36;
   o.items.forEach(it=>{it.sc=Math.min(1.5,430/it.h);});
   let tot=o.items.reduce((a,it)=>a+it.w*it.sc,0)+gap*Math.max(0,o.items.length-1);const k=Math.min(1,1760/Math.max(tot,1));
   tot*=k;let x=960-tot/2;
   o.items.forEach(it=>{it.s=it.sc*k;it.x=x+it.w*it.s/2;x+=it.w*it.s+gap*k;it.y=cy;});
   let tt=o.tags.reduce((a,t)=>a+t.w,0)+44*Math.max(0,o.tags.length-1);const tk=Math.min(1,1740/Math.max(tt,1));tt*=tk;let tx=960-tt/2;
   o.tags.forEach(t=>{t.s=tk;t.x=tx+t.w*tk/2;tx+=t.w*tk+44*tk;t.y=o.items.length?790:520;});
   this.o=o;},
   update(t){const o=this.o;const dur=e0-s0;const n=o.items.length+o.tags.length;const Wd=Math.max(0.3,dur-1.7);
    T(o.top,960,100,0,1);
    const at=(i,f)=>0.3+(f!==undefined?f:(n>1?i/(n-1):0))*Wd;
    o.items.forEach((it,i)=>{const a=at(i,spec.scenes[si].items[i].at);const p=pop(t,a,a+0.45);
     T(it.g,it.x+it.ox*it.s,it.y+it.oy*it.s,0,it.s*p);if(it.upd)it.upd(t,a);});
    o.tags.forEach((tg,j)=>{const i=o.items.length+j;const f=spec.scenes[si].tags[j].at;const a=at(i,f);T(tg.g,tg.x,tg.y,0,tg.s*pop(t,a,a+0.45));});
    T(o.cap,960,950,0,pop(t,0.2,0.8));
   }});
 });
}
function donut(p,R,w){const g=el('g',{},p);
 el('circle',{r:R,fill:'none',stroke:'#0A3F45','stroke-width':w},g);
 const arc=el('path',{fill:'none',stroke:MINT,'stroke-width':w},g);txt(g,'33%',0,36,110,'#fff','900');return {g,arc,R};}
function setDonut(d,f){const a=f*Math.PI*2;d.arc.setAttribute('d',f<=0.001?'':`M0 ${-d.R} A${d.R} ${d.R} 0 ${f>.5?1:0} 1 ${d.R*Math.sin(a)} ${-d.R*Math.cos(a)}`);}
