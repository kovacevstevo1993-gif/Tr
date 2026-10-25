// ===== VIDEO 11: regia con SFONDO IN MOVIMENTO (un po' diverso dai video 7-9, stessi colori) =====
// fasci di luce diagonali che scorrono piano + grande casa in trasparenza a destra + piccole luci che vanno piano verso destra.
// Tempo globale (OFF + t): il movimento continua da un blocco all'altro.
const bok=document.getElementById('bok');
const BEAM=el('g',{opacity:0.045},bok);
for(let i=0;i<8;i++)el('rect',{x:-1500+i*420,y:-400,width:170,height:1900,fill:'#BFFBEA',transform:'rotate(22)'},BEAM);
const HB=el('g',{opacity:0.075},bok);
{const S={fill:'none',stroke:'#BFFBEA','stroke-width':9,'stroke-linejoin':'round','stroke-linecap':'round'};
 const hs=[110,170,230,300,380,470,560];
 el('line',Object.assign({x1:-330,y1:260,x2:330,y2:260},S),HB);
 hs.forEach((h,i)=>el('rect',Object.assign({x:-300+i*92,y:260-h,width:62,height:h,rx:10},S),HB));
 el('path',Object.assign({d:'M-300 120 L-208 40 L-116 70 L-24 -60 L68 -110 L160 -230 L252 -300','stroke-dasharray':'4 22'},S),HB);
 el('path',Object.assign({d:'M236 -330 L276 -300 L236 -270'},S),HB);
 el('circle',Object.assign({cx:-250,cy:-250,r:88},S),HB);euro(HB,-250,-250,0.9,'#BFFBEA',12);}
const LT10=[];for(let i=0;i<42;i++){const c=el('circle',{r:2.5+((i*7)%5),fill:i%3?'#DFFFF6':'#FFE7B0',opacity:.08+((i*13)%5)*0.022},bok);LT10.push([c,(i*277)%2000,(i*163)%1080,7+(i*11)%13]);}
const sceneG=document.getElementById('scene');const camG=document.getElementById('cam');
let curS=-1;
function drawBlock(t){
 let i=SB.length-1;for(let k=0;k<SB.length;k++){if(t<SB[k].e){i=k;break;}}
 const S0=SB[i];
 if(curS!==i){sceneG.innerHTML='';S0.build(sceneG);curS=i;}
 const lt=t-S0.s;
 S0.update(lt);
 // comparsa: l'elemento diventa visibile mentre cresce (niente testi minuscoli nei primi fotogrammi)
 if(S0.o){S0.o.items.forEach(({n,it})=>n.setAttribute('opacity',clamp(pop(lt,it._a,it._a+0.9)/0.35).toFixed(3)));S0.o.cap.setAttribute('opacity',clamp((lt-0.15)/0.3).toFixed(3));}
 const fin=eo3(seg(lt,0,0.3)),fout=(i<SB.length-1)?1-eio(seg(t,S0.e-0.3,S0.e)):1;
 sceneG.setAttribute('opacity',Math.min(fin,fout));
 const G=OFF+t;
 BEAM.setAttribute('transform','translate('+((G*14)%420).toFixed(1)+' 0)');
 HB.setAttribute('transform','translate('+(1500+14*Math.sin(G*0.1)).toFixed(1)+' '+(700+14*Math.sin(G*0.13)).toFixed(1)+') rotate('+(-3+1.2*Math.sin(G*0.07)).toFixed(2)+')');
 LT10.forEach(([c,x,y,sp])=>{const xx=((x+G*sp)%2000+2000)%2000-40;c.setAttribute('cx',xx.toFixed(1));c.setAttribute('cy',(y+18*Math.sin(G*0.25+x)).toFixed(1));});
 const z=1+0.02*(t/TOT);camG.setAttribute('transform','translate(960 540) scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
// controllo sovrapposizioni (render.py): riquadri degli elementi a fine scena, tutti completi
window.__OVL=function(){const out=[];const R=n=>{const r=n.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height};};
 for(let k=0;k<SB.length;k++){drawBlock(SB[k].e-0.45);const o=SB[k].o;const its=o.items.map(({n,it})=>({r:R(n),it}));const top=R(o.top),cp=R(o.cap);
  const yMax=(N===14)?700:(cp.h>0?cp.y-6:1074);
  its.forEach(a=>{if(a.r.x<10||a.r.y<top.y+top.h+8||a.r.x+a.r.w>1910||a.r.y+a.r.h>yMax)out.push([k+1,'FUORI ZONA',a.it.k,String(a.it.at),Math.round(a.r.x),Math.round(a.r.y),Math.round(a.r.x+a.r.w),Math.round(a.r.y+a.r.h)]);});
  for(let i=0;i<its.length;i++)for(let j=i+1;j<its.length;j++){const a=its[i],b=its[j];if(a.it.ov||b.it.ov)continue;
   const ix=Math.min(a.r.x+a.r.w,b.r.x+b.r.w)-Math.max(a.r.x,b.r.x),iy=Math.min(a.r.y+a.r.h,b.r.y+b.r.h)-Math.max(a.r.y,b.r.y);
   if(ix>2&&iy>2)out.push([k+1,'SOVRAPPOSTI',a.it.k+' @'+a.it.at,b.it.k+' @'+b.it.at,Math.round(ix),Math.round(iy)]);}}
 curS=-1;return out;};
