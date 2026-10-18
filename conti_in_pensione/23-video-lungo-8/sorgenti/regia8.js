// ===== VIDEO 8: regia con SFONDO IN MOVIMENTO NUOVO (rotte d'aereo + mappamondo, diverso dal video 7) =====
// meridiani di un grande mappamondo che ruotano piano a destra, rotte tratteggiate che scorrono, un aereo che attraversa lo sfondo.
// Tempo globale (OFF + t): il movimento continua da un blocco all'altro.
const bok=document.getElementById('bok');
const GLB=el('g',{opacity:0.07,transform:'translate(1560 560)'},bok);
el('circle',{r:620,fill:'none',stroke:'#BFFBEA','stroke-width':4},GLB);
const MER=[];for(let i=0;i<6;i++)MER.push(el('ellipse',{rx:10,ry:620,fill:'none',stroke:'#BFFBEA','stroke-width':3},GLB));
[-0.66,-0.33,0,0.33,0.66].forEach(k=>{const y=620*k,x=Math.sqrt(620*620-y*y);el('line',{x1:-x,y1:y,x2:x,y2:y,stroke:'#BFFBEA','stroke-width':3},GLB);});
const ROUTES=[];[['M-100 760 Q700 120 1500 380',0],['M200 1150 Q900 520 2050 640',1],['M-80 260 Q900 -120 2000 180',2]].forEach(([d,k])=>{
 ROUTES.push(el('path',{d:d,fill:'none',stroke:'#8FF5DC','stroke-width':4,'stroke-dasharray':'18 22',opacity:0.10},bok));});
const PL=el('g',{opacity:0.13},bok);planeIco(PL,0.35,'#8FF5DC');
const sceneG=document.getElementById('scene');const camG=document.getElementById('cam');
let curS=-1;
function bez(t,p0,p1,p2){const u=1-t;return [u*u*p0[0]+2*u*t*p1[0]+t*t*p2[0],u*u*p0[1]+2*u*t*p1[1]+t*t*p2[1]];}
function drawBlock(t){
 let i=SB.length-1;for(let k=0;k<SB.length;k++){if(t<SB[k].e){i=k;break;}}
 const S0=SB[i];
 if(curS!==i){sceneG.innerHTML='';S0.build(sceneG);curS=i;}
 const lt=t-S0.s;
 S0.update(lt);
 const fin=eo3(seg(lt,0,0.3)),fout=(i<SB.length-1)?1-eio(seg(t,S0.e-0.3,S0.e)):1;
 sceneG.setAttribute('opacity',Math.min(fin,fout));
 const G=OFF+t;
 MER.forEach((m,k)=>{const a=((G*0.08+k/6)%1)*Math.PI;m.setAttribute('rx',Math.abs(620*Math.cos(a)).toFixed(1));});
 ROUTES.forEach((r,k)=>r.setAttribute('stroke-dashoffset',(-G*(22+k*6)).toFixed(1)));
 const u=(G/38)%1;const p=bez(u,[-200,820],[760,120],[2120,420]);const p2=bez(Math.min(1,u+0.01),[-200,820],[760,120],[2120,420]);
 const ang=Math.atan2(p2[1]-p[1],p2[0]-p[0])*180/Math.PI;PL.setAttribute('transform','translate('+p[0].toFixed(1)+' '+p[1].toFixed(1)+') rotate('+ang.toFixed(1)+')');
 const z=1+0.02*(t/TOT);camG.setAttribute('transform','translate(960 540) scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
