// ===== VIDEO 7: regia con SFONDO IN MOVIMENTO (regola N.37, come gli short) =====
// bolle di luce che salgono piano + raggi chiari che ruotano lentissimi; tempo globale (OFF + t) cosi' il movimento continua da un blocco all'altro.
const bok=document.getElementById('bok');
const RAYS=el('g',{opacity:0.05},bok);
for(let i=0;i<12;i++){const a=i*30*Math.PI/180,b=a+0.13;el('path',{d:`M0 0 L${1500*Math.cos(a)} ${1500*Math.sin(a)} L${1500*Math.cos(b)} ${1500*Math.sin(b)} Z`,fill:'#BFFBEA'},RAYS);}
const BK=[];
for(let i=0;i<18;i++){const c=el('circle',{r:26+((i*37)%74),fill:'#8FF5DC',opacity:.05+((i*13)%7)*0.01},bok);BK.push([c,(i*271)%1920,(i*197)%1080,14+(i*7)%22]);}
const sceneG=document.getElementById('scene');const camG=document.getElementById('cam');
let curS=-1;
function drawBlock(t){
 let i=SB.length-1;for(let k=0;k<SB.length;k++){if(t<SB[k].e){i=k;break;}}
 const S0=SB[i];
 if(curS!==i){sceneG.innerHTML='';S0.build(sceneG);curS=i;}
 const lt=t-S0.s;
 S0.update(lt);
 const fin=eo3(seg(lt,0,0.3)),fout=(i<SB.length-1)?1-eio(seg(t,S0.e-0.3,S0.e)):1;
 sceneG.setAttribute('opacity',Math.min(fin,fout));
 const G=OFF+t;
 RAYS.setAttribute('transform','translate(960 420) rotate('+(G*1.2)%360+')');
 BK.forEach(([c,x,y,sp])=>{const yy=((y-G*sp)%1240+1240)%1240-80;c.setAttribute('cx',x+28*Math.sin(G*0.25+x));c.setAttribute('cy',yy);});
 const z=1+0.02*(t/TOT);camG.setAttribute('transform','translate(960 540) scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
