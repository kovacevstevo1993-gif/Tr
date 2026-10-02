const NS='http://www.w3.org/2000/svg';
function el(tag,attrs,parent){const e=document.createElementNS(NS,tag);for(const k in (attrs||{}))e.setAttribute(k,attrs[k]);if(parent)parent.appendChild(e);return e;}
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const lerp=(a,b,t)=>a+(b-a)*t;
const seg=(t,a,b)=>clamp((t-a)/(b-a));
const eo3=x=>1-Math.pow(1-x,3);
const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const eob=x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
function T(n,x,y,r,s){r=r||0;s=(s===undefined?1:s);n.setAttribute('transform','translate('+x+' '+y+') rotate('+r+') scale('+s+')');}
function op(n,o){n.setAttribute('opacity',o);}
const FONT='DejaVu Sans, Liberation Sans, Arial, sans-serif';
function txt(p,s,x,y,size,fill,weight,anchor){const t=el('text',{x:x,y:y,'font-size':size,fill:fill,'font-family':FONT,'font-weight':weight||'bold','text-anchor':anchor||'middle'},p);t.textContent=s;return t;}
function euro(p,cx,cy,s,color,sw){const g=el('g',{fill:'none',stroke:color,'stroke-width':(sw||17)*s,'stroke-linecap':'round'},p);
 el('path',{d:`M${cx+37*s} ${cy-37*s} A${54*s} ${54*s} 0 1 0 ${cx+37*s} ${cy+37*s}`},g);
 el('line',{x1:cx-48*s,y1:cy-12*s,x2:cx+18*s,y2:cy-12*s},g);
 el('line',{x1:cx-48*s,y1:cy+14*s,x2:cx+18*s,y2:cy+14*s},g);return g;}
function coin(p,cx,cy,r){const g=el('g',{},p);
 el('circle',{cx:cx,cy:cy,r:r,fill:'url(#g_rim)'},g);
 el('circle',{cx:cx,cy:cy,r:r,fill:'none',stroke:'#fff','stroke-opacity':.55,'stroke-width':r*0.027},g);
 el('circle',{cx:cx,cy:cy,r:r*0.84,fill:'url(#g_disc)'},g);
 el('circle',{cx:cx,cy:cy,r:r*0.71,fill:'none',stroke:'#B5F5E4','stroke-opacity':.55,'stroke-width':r*0.022,'stroke-dasharray':(r*.03)+' '+(r*.06)},g);
 el('path',{d:`M${cx-r*.6} ${cy-r*.28} A${r*.7} ${r*.7} 0 0 1 ${cx+r*.16} ${cy-r*.6}`,fill:'none',stroke:'#fff','stroke-opacity':.4,'stroke-width':r*.06,'stroke-linecap':'round'},g);
 euro(g,cx,cy,r/112,'#fff',17);return g;}
function silverCoin(p,cx,cy,rx,ry,h){ // flat stacked coin (ellipse) with thickness
 const g=el('g',{},p);
 el('ellipse',{cx:cx,cy:cy+h,rx:rx,ry:ry,fill:'#6F878C'},g);
 el('rect',{x:cx-rx,y:cy,width:rx*2,height:h,fill:'#8AA1A6'},g);
 el('ellipse',{cx:cx,cy:cy,rx:rx,ry:ry,fill:'url(#g_silver)'},g);
 el('ellipse',{cx:cx,cy:cy,rx:rx*.68,ry:ry*.68,fill:'none',stroke:'#5B7378','stroke-width':2,opacity:.6},g);
 return g;}
function goldCoin(p,cx,cy,rx,ry,h){const g=el('g',{},p);
 el('ellipse',{cx:cx,cy:cy+h,rx:rx,ry:ry,fill:'#127F70'},g);
 el('rect',{x:cx-rx,y:cy,width:rx*2,height:h,fill:'#1A9C86'},g);
 el('ellipse',{cx:cx,cy:cy,rx:rx,ry:ry,fill:'url(#g_rim)'},g);
 el('ellipse',{cx:cx,cy:cy,rx:rx*.68,ry:ry*.68,fill:'none',stroke:'#0B5A55','stroke-width':2,opacity:.5},g);
 return g;}
function paper(p,w,h,shadow){const g=el('g',{},p);
 el('rect',{x:-w/2,y:0,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:shadow===false?'':'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:0,width:w,height:h,rx:26,fill:'none',stroke:'#fff','stroke-opacity':.7,'stroke-width':3},g);
 return g;}
function metalRing(p,x,y,w,h){const g=el('g',{filter:'url(#g_sh3)'},p);
 el('rect',{x:x-w/2,y:y,width:w,height:h,rx:w/2,fill:'url(#g_metal)'},g);
 el('rect',{x:x-w*.2,y:y+h*.15,width:w*.4,height:h*.7,rx:w*.2,fill:'#0A3F45',opacity:.85},g);return g;}
// cedolino rows
function rows(p,labels,w,y0,gap,ink){const out=[];labels.forEach((l,i)=>{const y=y0+i*gap;
 el('rect',{x:-w/2+40,y:y+gap-22,width:w-80,height:3,fill:'#C9D6D8'},p);
 txt(p,l,-w/2+50,y+gap-38,32,ink||'#0B4A50','bold','start');
 el('rect',{x:w/2-250,y:y+gap-66,width:200,height:30,rx:15,fill:'#BFD0D3'},p);out.push(y);});return out;}
