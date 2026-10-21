// ===== VIDEO 9: regia con SFONDO IN MOVIMENTO di DICEMBRE (diverso dal 7 e dall'8, stessi colori) =====
// raggi chiari lentissimi + piccole luci che scendono piano (come neve leggera) + grande calendario in trasparenza a destra.
// Tempo globale (OFF + t): il movimento continua da un blocco all'altro.
const bok=document.getElementById('bok');
const RAYS=el('g',{opacity:0.04},bok);
for(let i=0;i<12;i++){const a=i*30*Math.PI/180,b=a+0.12;el('path',{d:`M0 0 L${1500*Math.cos(a)} ${1500*Math.sin(a)} L${1500*Math.cos(b)} ${1500*Math.sin(b)} Z`,fill:'#BFFBEA'},RAYS);}
const CALB=el('g',{opacity:0.06,transform:'translate(1580 640) rotate(-8)'},bok);
el('rect',{x:-300,y:-320,width:600,height:640,rx:60,fill:'none',stroke:'#BFFBEA','stroke-width':8},CALB);
el('rect',{x:-300,y:-320,width:600,height:150,rx:60,fill:'#BFFBEA',opacity:.5},CALB);
[-150,0,150].forEach(x=>el('rect',{x:x-14,y:-360,width:28,height:90,rx:14,fill:'#BFFBEA'},CALB));
for(let r=0;r<4;r++)for(let c=0;c<5;c++)el('rect',{x:-250+c*104,y:-130+r*104,width:80,height:80,rx:14,fill:'none',stroke:'#BFFBEA','stroke-width':5},CALB);
const SN=[];for(let i=0;i<46;i++){const c=el('circle',{r:3+((i*7)%6),fill:'#DFFFF6',opacity:.10+((i*13)%5)*0.025},bok);SN.push([c,(i*263)%1920,(i*151)%1080,10+(i*11)%18]);}
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
 RAYS.setAttribute('transform','translate(960 380) rotate('+((G*1.0)%360)+')');
 CALB.setAttribute('transform','translate(1580 '+(640+14*Math.sin(G*0.12))+') rotate('+(-8+2*Math.sin(G*0.07))+')');
 SN.forEach(([c,x,y,sp])=>{const yy=((y+G*sp)%1160+1160)%1160-40;c.setAttribute('cx',(x+22*Math.sin(G*0.3+x)).toFixed(1));c.setAttribute('cy',yy.toFixed(1));});
 const z=1+0.02*(t/TOT);camG.setAttribute('transform','translate(960 540) scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
