// ===== VIDEO 13 (reversibilita'): regia con SFONDO IN MOVIMENTO nuovo (diverso dai video 7-12, stessi colori):
// tre linee di soglia tratteggiate con le cifre della tabella F che scorrono piano, scalinata che SALE a destra (0 / 25 / 40 / 50 %),
// onde di luce lente e luci che vanno piano verso destra.
const bok=document.getElementById('bok');
const GR=el('g',{opacity:0.045},bok);
for(let i=0;i<=16;i++)el('line',{x1:0,y1:i*70,x2:1920,y2:i*70,stroke:'#BFFBEA','stroke-width':1.5},GR);
for(let i=0;i<=28;i++)el('line',{x1:i*70,y1:0,x2:i*70,y2:1080,stroke:'#BFFBEA','stroke-width':1.5},GR);
const THR=el('g',{opacity:0.10},bok);
const THRL=[[300,'23.862,15 €'],[560,'31.816,20 €'],[820,'39.770,25 €']];
const THRG=THRL.map(([y,s])=>{const g=el('g',{},THR);el('line',{x1:-400,y1:y,x2:2400,y2:y,stroke:'#BFFBEA','stroke-width':3,'stroke-dasharray':'22 18'},g);
 for(let k=0;k<4;k++){const t=txt(g,s,200+k*700,y-16,34,'#BFFBEA','bold','start');}return g;});
const UP=el('g',{opacity:0.085},bok);
{const S={fill:'none',stroke:'#BFFBEA','stroke-width':10,'stroke-linejoin':'round','stroke-linecap':'round'};
 el('path',Object.assign({d:'M-380 240 H-230 V130 H-80 V20 H70 V-90 H220 V-200 H380'},S),UP);
 [[-305,240],[-155,130],[-5,20],[145,-90],[295,-200]].forEach(([x,y])=>el('circle',{cx:x,cy:y,r:16,fill:'#BFFBEA'},UP));
 el('path',Object.assign({d:'M-380 260 L380 -240','stroke-dasharray':'4 24'},S),UP);}
const WAVE=el('rect',{x:0,y:0,width:1920,height:170,fill:'#BFFBEA',opacity:0.032},bok);
const LT10=[];for(let i=0;i<40;i++){const c=el('circle',{r:2.5+((i*7)%5),fill:i%3?'#DFFFF6':'#FFE7B0',opacity:.08+((i*13)%5)*0.022},bok);LT10.push([c,(i*277)%2000,(i*163)%1080,7+(i*11)%13]);}
const sceneG=document.getElementById('scene');const camG=document.getElementById('cam');
let curS=-1;
function drawBlock(t){
 let i=SB.length-1;for(let k=0;k<SB.length;k++){if(t<SB[k].e){i=k;break;}}
 const S0=SB[i];
 if(curS!==i){sceneG.innerHTML='';S0.build(sceneG);curS=i;}
 const lt=t-S0.s;
 S0.update(lt);
 if(S0.o){S0.o.items.forEach(({n,it})=>n.setAttribute('opacity',clamp(pop(lt,it._a,it._a+0.9)/0.35).toFixed(3)));S0.o.cap.setAttribute('opacity',clamp((lt-0.15)/0.3).toFixed(3));}
 const fin=eo3(seg(lt,0,0.3)),fout=(i<SB.length-1)?1-eio(seg(t,S0.e-0.3,S0.e)):1;
 sceneG.setAttribute('opacity',Math.min(fin,fout));
 const G=OFF+t;
 THRG.forEach((g,k)=>g.setAttribute('transform','translate('+(-((G*(14+4*k))%700)).toFixed(1)+' '+(10*Math.sin(G*0.1+k)).toFixed(1)+')'));
 UP.setAttribute('transform','translate('+(1500+16*Math.sin(G*0.09)).toFixed(1)+' '+(610+14*Math.sin(G*0.12)).toFixed(1)+')');
 WAVE.setAttribute('transform','translate(0 '+(-200+((G*60)%1300)).toFixed(1)+')');
 LT10.forEach(([c,x,y,sp])=>{const xx=((x+G*sp)%2000+2000)%2000-40;c.setAttribute('cx',xx.toFixed(1));c.setAttribute('cy',(y+18*Math.sin(G*0.25+x)).toFixed(1));});
 const z=1.012+0.018*(t/TOT);camG.setAttribute('transform','translate('+(960+5*Math.sin(G*0.15)).toFixed(1)+' '+(540+4*Math.sin(G*0.11)).toFixed(1)+') scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
window.__OVL=function(){const out=[];const R=n=>{const r=n.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height};};
 for(let k=0;k<SB.length;k++){drawBlock(SB[k].e-0.45);const o=SB[k].o;const its=o.items.map(({n,it})=>({r:R(n),it}));const top=R(o.top),cp=R(o.cap);
  const yMax=(N===22)?700:(cp.h>0?cp.y-6:1074);
  its.forEach(a=>{if(a.r.x<10||a.r.y<top.y+top.h+8||a.r.x+a.r.w>1910||a.r.y+a.r.h>yMax)out.push([k+1,'FUORI ZONA',a.it.k,String(a.it.at),Math.round(a.r.x),Math.round(a.r.y),Math.round(a.r.x+a.r.w),Math.round(a.r.y+a.r.h)]);});
  for(let i=0;i<its.length;i++)for(let j=i+1;j<its.length;j++){const a=its[i],b=its[j];if(a.it.ov||b.it.ov)continue;
   const ix=Math.min(a.r.x+a.r.w,b.r.x+b.r.w)-Math.max(a.r.x,b.r.x),iy=Math.min(a.r.y+a.r.h,b.r.y+b.r.h)-Math.max(a.r.y,b.r.y);
   if(ix>2&&iy>2)out.push([k+1,'SOVRAPPOSTI',a.it.k+' @'+a.it.at,b.it.k+' @'+b.it.at,Math.round(ix),Math.round(iy)]);}}
 curS=-1;return out;};
