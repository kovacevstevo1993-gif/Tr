// ===== VIDEO 14: regia con SFONDO IN MOVIMENTO nuovo (diverso dai video 7-12, stessi colori):
// tre linee di soglia tratteggiate con le cifre della tabella F che scorrono piano, scalinata che SALE a destra (0 / 25 / 40 / 50 %),
// onde di luce lente e luci che vanno piano verso destra.
const bok=document.getElementById('bok');
// ===== VIDEO 14 (manovra e pensionati): SFONDO IN MOVIMENTO nuovo (diverso dai video 7-13, stessi colori):
// bande di luce diagonali che scorrono, simboli % € § che salgono piano, quadrante che gira lentamente, puntini di luce.
const GR=el('g',{opacity:0.05},bok);
for(let i=-6;i<=30;i++)el('line',{x1:i*80,y1:0,x2:i*80+500,y2:1080,stroke:'#BFFBEA','stroke-width':1.5},GR);
const BANDS=[0,1,2].map(k=>el('polygon',{points:'0,0 190,0 -70,1080 -260,1080',fill:'#BFFBEA',opacity:0.035+0.01*k},bok));
const GLY=[];{const S=['%','€','§','%','€','§','%'];for(let i=0;i<22;i++){const t=txt(bok,S[i%7],0,0,70+((i*37)%90),'#BFFBEA','900');t.setAttribute('opacity',(0.05+((i*11)%5)*0.012).toFixed(3));GLY.push([t,(i*331)%1900+30,(i*197)%1300,10+(i*7)%15]);}}
const DIAL=el('g',{opacity:0.09},bok);
{el('circle',{r:300,fill:'none',stroke:'#BFFBEA','stroke-width':6},DIAL);el('circle',{r:220,fill:'none',stroke:'#BFFBEA','stroke-width':3,'stroke-dasharray':'3 16'},DIAL);
 for(let i=0;i<36;i++){const a=i*Math.PI/18,L=(i%3==0)?44:22;el('line',{x1:Math.cos(a)*(300-L),y1:Math.sin(a)*(300-L),x2:Math.cos(a)*300,y2:Math.sin(a)*300,stroke:'#BFFBEA','stroke-width':(i%3==0)?7:4},DIAL);}
 el('path',{d:'M0 0 L0 -250',stroke:'#FFE7B0','stroke-width':9,'stroke-linecap':'round'},DIAL);el('circle',{r:14,fill:'#FFE7B0'},DIAL);}
const LT10=[];for(let i=0;i<30;i++){const c=el('circle',{r:2.5+((i*7)%5),fill:i%3?'#DFFFF6':'#FFE7B0',opacity:.08+((i*13)%5)*0.022},bok);LT10.push([c,(i*277)%2000,(i*163)%1080,7+(i*11)%13]);}
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
 BANDS.forEach((p,k)=>p.setAttribute('transform','translate('+(((G*(48+16*k)+k*700)%2700)-400).toFixed(1)+' 0)'));
 GLY.forEach(([t,x,y,sp])=>{const yy=1180-(((y+G*sp)%1300+1300)%1300);t.setAttribute('x',(x+16*Math.sin(G*0.2+x)).toFixed(1));t.setAttribute('y',yy.toFixed(1));});
 DIAL.setAttribute('transform','translate('+(1560+10*Math.sin(G*0.09)).toFixed(1)+' '+(560+8*Math.sin(G*0.13)).toFixed(1)+') rotate('+(G*3.2).toFixed(2)+')');
 LT10.forEach(([c,x,y,sp])=>{const xx=((x+G*sp)%2000+2000)%2000-40;c.setAttribute('cx',xx.toFixed(1));c.setAttribute('cy',(y+18*Math.sin(G*0.25+x)).toFixed(1));});
 const z=1.012+0.018*(t/TOT);camG.setAttribute('transform','translate('+(960+5*Math.sin(G*0.15)).toFixed(1)+' '+(540+4*Math.sin(G*0.11)).toFixed(1)+') scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
window.__OVL=function(){const out=[];const R=n=>{const r=n.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height};};
 for(let k=0;k<SB.length;k++){drawBlock(SB[k].e-0.45);const o=SB[k].o;const its=o.items.map(({n,it})=>({r:R(n),it}));const top=R(o.top),cp=R(o.cap);
  const yMax=(N===15)?700:(cp.h>0?cp.y-6:1074);
  its.forEach(a=>{if(a.r.x<10||a.r.y<top.y+top.h+8||a.r.x+a.r.w>1910||a.r.y+a.r.h>yMax)out.push([k+1,'FUORI ZONA',a.it.k,String(a.it.at),Math.round(a.r.x),Math.round(a.r.y),Math.round(a.r.x+a.r.w),Math.round(a.r.y+a.r.h)]);});
  for(let i=0;i<its.length;i++)for(let j=i+1;j<its.length;j++){const a=its[i],b=its[j];if(a.it.ov||b.it.ov)continue;
   const ix=Math.min(a.r.x+a.r.w,b.r.x+b.r.w)-Math.max(a.r.x,b.r.x),iy=Math.min(a.r.y+a.r.h,b.r.y+b.r.h)-Math.max(a.r.y,b.r.y);
   if(ix>2&&iy>2)out.push([k+1,'SOVRAPPOSTI',a.it.k+' @'+a.it.at,b.it.k+' @'+b.it.at,Math.round(ix),Math.round(iy)]);}}
 curS=-1;return out;};
