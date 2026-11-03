// ===== VIDEO 15 (Carta Dedicata a te e aiuti per i pensionati): SFONDO IN MOVIMENTO nuovo (diverso dai video 7-14, stessi colori):
// carte prepagate trasparenti che scorrono piano in diagonale, fasci di luce che oscillano da in alto a destra,
// anelli che si espandono da in basso a sinistra, puntini di luce.
const bok=document.getElementById('bok');
function mkCard15(w){const g=el('g',{},bok);const h=w*0.63;
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:w*0.06,fill:'#BFFBEA','fill-opacity':0.05,stroke:'#BFFBEA','stroke-width':3},g);
 el('rect',{x:-w*0.38,y:-h*0.22,width:w*0.17,height:h*0.2,rx:w*0.02,fill:'#BFFBEA','fill-opacity':0.5},g);
 el('rect',{x:-w*0.38,y:h*0.18,width:w*0.5,height:h*0.06,rx:h*0.03,fill:'#BFFBEA','fill-opacity':0.45},g);
 el('circle',{cx:w*0.3,cy:h*0.2,r:h*0.16,fill:'none',stroke:'#FFE7B0','stroke-width':3,'stroke-opacity':0.6},g);
 el('circle',{cx:w*0.36,cy:h*0.2,r:h*0.16,fill:'none',stroke:'#BFFBEA','stroke-width':3,'stroke-opacity':0.6},g);
 return g;}
const CARDS15=[];for(let i=0;i<11;i++){const w=170+((i*53)%210);const g=mkCard15(w);g.setAttribute('opacity',(0.07+((i*7)%4)*0.018).toFixed(3));CARDS15.push([g,(i*371)%2300,(i*211)%1200,7+(i*5)%11,((i*37)%50)-25]);}
const BEAMS15=[0,1,2,3,4].map(k=>el('polygon',{points:'1960,-80 1500,1160 1380,1160',fill:'#BFFBEA',opacity:0.03+0.008*k},bok));
const RINGS15=[0,1,2].map(k=>el('circle',{cx:0,cy:1080,r:100,fill:'none',stroke:'#BFFBEA','stroke-width':3},bok));
const LT15=[];for(let i=0;i<30;i++){const c=el('circle',{r:2.5+((i*7)%5),fill:i%3?'#DFFFF6':'#FFE7B0',opacity:.08+((i*13)%5)*0.022},bok);LT15.push([c,(i*277)%2000,(i*163)%1080,7+(i*11)%13]);}
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
 CARDS15.forEach(([g,x,y,sp,rot])=>{const xx=((x+G*sp)%2500)-300,yy=((y-G*sp*0.55)%1300+1300)%1300-110;g.setAttribute('transform','translate('+xx.toFixed(1)+' '+yy.toFixed(1)+') rotate('+(rot+6*Math.sin(G*0.12+x)).toFixed(2)+')');});
 BEAMS15.forEach((p,k)=>p.setAttribute('transform','rotate('+(6*Math.sin(G*0.1+k*1.3)+k*3.5).toFixed(2)+' 1960 -80)'));
 RINGS15.forEach((c,k)=>{const rr=(G*55+k*300)%900;c.setAttribute('r',rr.toFixed(1));c.setAttribute('opacity',(0.14*(1-rr/900)).toFixed(3));c.setAttribute('cx','0');});
 LT15.forEach(([c,x,y,sp])=>{const xx=((x+G*sp)%2000+2000)%2000-40;c.setAttribute('cx',xx.toFixed(1));c.setAttribute('cy',(y+18*Math.sin(G*0.25+x)).toFixed(1));});
 const z=1.012+0.018*(t/TOT);camG.setAttribute('transform','translate('+(960+5*Math.sin(G*0.15)).toFixed(1)+' '+(540+4*Math.sin(G*0.11)).toFixed(1)+') scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
window.__OVL=function(){const out=[];const R=n=>{const r=n.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height};};
 for(let k=0;k<SB.length;k++){drawBlock(SB[k].e-0.45);const o=SB[k].o;const its=o.items.map(({n,it})=>({r:R(n),it}));const top=R(o.top),cp=R(o.cap);
  const yMax=(N===19)?700:(cp.h>0?cp.y-6:1074);
  its.forEach(a=>{if(a.r.x<10||a.r.y<top.y+top.h+8||a.r.x+a.r.w>1910||a.r.y+a.r.h>yMax)out.push([k+1,'FUORI ZONA',a.it.k,String(a.it.at),Math.round(a.r.x),Math.round(a.r.y),Math.round(a.r.x+a.r.w),Math.round(a.r.y+a.r.h)]);});
  for(let i=0;i<its.length;i++)for(let j=i+1;j<its.length;j++){const a=its[i],b=its[j];if(a.it.ov||b.it.ov)continue;
   const ix=Math.min(a.r.x+a.r.w,b.r.x+b.r.w)-Math.max(a.r.x,b.r.x),iy=Math.min(a.r.y+a.r.h,b.r.y+b.r.h)-Math.max(a.r.y,b.r.y);
   if(ix>2&&iy>2)out.push([k+1,'SOVRAPPOSTI',a.it.k+' @'+a.it.at,b.it.k+' @'+b.it.at,Math.round(ix),Math.round(iy)]);}}
 curS=-1;return out;};
