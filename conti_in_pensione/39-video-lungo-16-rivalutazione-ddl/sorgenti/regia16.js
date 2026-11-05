// ===== VIDEO 15 (Carta Dedicata a te e aiuti per i pensionati): SFONDO IN MOVIMENTO nuovo (diverso dai video 7-14, stessi colori):
// carte prepagate trasparenti che scorrono piano in diagonale, fasci di luce che oscillano da in alto a destra,
// anelli che si espandono da in basso a sinistra, puntini di luce.
const bok=document.getElementById('bok');
(function(){const st=document.querySelectorAll('#g_bg stop');['#1A8A93','#0B5560','#031F26'].forEach((c,i)=>st[i].setAttribute('stop-color',c));})();
const PT16=(function(){const d=document.querySelector('defs');
 const pt=el('pattern',{id:'g16_grid',width:96,height:96,patternUnits:'userSpaceOnUse'},d);
 el('path',{d:'M96 0 H0 V96',fill:'none',stroke:'#BFFBEA','stroke-width':1.6,'stroke-opacity':.55},pt);
 el('path',{d:'M48 0 V96 M0 48 H96',fill:'none',stroke:'#BFFBEA','stroke-width':0.8,'stroke-opacity':.25},pt);
 const lg=el('linearGradient',{id:'g16_scan',x1:0,y1:0,x2:1,y2:0},d);[[0,0],[0.5,0.09],[1,0]].forEach(([o,p])=>el('stop',{offset:o,'stop-color':'#DFFFF6','stop-opacity':p},lg));
 return pt;})();
el('rect',{x:-200,y:-200,width:2400,height:1500,fill:'url(#g16_grid)',opacity:0.11},bok);
function stairPath16(sw,sh,n){let d='M0 '+(n*sh);for(let i=0;i<n;i++)d+=' V'+((n-1-i)*sh)+' H'+((i+1)*sw);return d+' V'+(n*sh)+' Z';}
const STS16=[[1.5,560,11],[1.0,250,15],[2.1,800,8],[0.8,120,19]].map(([sc,y,sp],i)=>{const g=el('g',{},bok);
 el('path',{d:stairPath16(120,70,6),fill:'#BFFBEA','fill-opacity':0.05,stroke:'#BFFBEA','stroke-width':3,'stroke-opacity':0.16,'stroke-linejoin':'round'},g);return [g,sc,y,sp,i*610];});
const SCAN16=[0,1,2].map(k=>el('rect',{x:0,y:-100,width:190,height:1400,fill:'url(#g16_scan)'},bok));
const LT16=[];for(let i=0;i<28;i++){const c=el('circle',{r:2.5+((i*7)%5),fill:i%3?'#DFFFF6':'#FFE7B0',opacity:.09+((i*13)%5)*0.022},bok);LT16.push([c,(i*277)%2000,(i*163)%1180,5+(i*11)%9]);}
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
 PT16.setAttribute('patternTransform','translate('+(G*15).toFixed(1)+' '+(-G*10).toFixed(1)+')');
 STS16.forEach(([g,sc,y,sp,o])=>{const x=((o+G*sp)%3000)-700;g.setAttribute('transform','translate('+x.toFixed(1)+' '+(y-sc*210+ 18*Math.sin(G*0.2+o)).toFixed(1)+') scale('+sc+')');});
 SCAN16.forEach((r_,k)=>{const x=((G*42+k*820)%2700)-400;r_.setAttribute('transform','translate('+x.toFixed(1)+' 0) skewX(-14)');});
 LT16.forEach(([c,x,y,sp])=>{c.setAttribute('cx',(((x+G*sp)%2000+2000)%2000-40).toFixed(1));c.setAttribute('cy',((((y-G*sp*1.3)%1180)+1180)%1180-50).toFixed(1));});
 const z=1.012+0.018*(t/TOT);camG.setAttribute('transform','translate('+(960+5*Math.sin(G*0.15)).toFixed(1)+' '+(540+4*Math.sin(G*0.11)).toFixed(1)+') scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
window.__OVL=function(){const out=[];const R=n=>{const r=n.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height};};
 for(let k=0;k<SB.length;k++){drawBlock(SB[k].e-0.45);const o=SB[k].o;const its=o.items.map(({n,it})=>({r:R(n),it}));const top=R(o.top),cp=R(o.cap);
  const yMax=(N===16)?830:(cp.h>0?cp.y-6:1074);
  its.forEach(a=>{if(a.r.x<10||a.r.y<top.y+top.h+8||a.r.x+a.r.w>1910||a.r.y+a.r.h>yMax)out.push([k+1,'FUORI ZONA',a.it.k,String(a.it.at),Math.round(a.r.x),Math.round(a.r.y),Math.round(a.r.x+a.r.w),Math.round(a.r.y+a.r.h)]);});
  for(let i=0;i<its.length;i++)for(let j=i+1;j<its.length;j++){const a=its[i],b=its[j];if(a.it.ov||b.it.ov)continue;
   const ix=Math.min(a.r.x+a.r.w,b.r.x+b.r.w)-Math.max(a.r.x,b.r.x),iy=Math.min(a.r.y+a.r.h,b.r.y+b.r.h)-Math.max(a.r.y,b.r.y);
   if(ix>2&&iy>2)out.push([k+1,'SOVRAPPOSTI',a.it.k+' @'+a.it.at,b.it.k+' @'+b.it.at,Math.round(ix),Math.round(iy)]);}}
 curS=-1;return out;};
