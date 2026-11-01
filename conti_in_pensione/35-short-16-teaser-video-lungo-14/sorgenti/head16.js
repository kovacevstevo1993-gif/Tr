// ===== SHORT 16 - teaser video lungo 14 (manovra 2027 e pensionati) (1080x1920, 30 fps) =====
// Regole N.15/N.18: comparsa 0.9 s, elementi che restano fino a fine scena, distanza >= 1.0 s, ultimo completo entro l'80 %, poi tutto FERMO.
// Look NUOVO rispetto agli short 12-15 (N.47 "un po' piu diverse"): titoletto a STRISCIA NOTIZIE con tre pallini (niente numeri, N.50), schede con NASTRO ADESIVO,
// didascalia a FUMETTO con altoparlante (la voce), sfondo con FOGLI DI DOCUMENTO che salgono piano.
const eob2=x=>{const c1=1.0,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const pop=(t,a,d)=>Math.max(0,eob2(seg(t,a,a+(d||.9))));
const sl=(t,a,d)=>eo3(seg(t,a,a+(d||.9)));
const GRN='#13805F',DK='#0B4A50',ORG='#E8832A',AMB='#FFB020',NAVY='#06303A';
function fade(t,n,x,y,a){T(n,x,y+(1-sl(t,a,.9))*60,0,1);op(n,seg(t,a,a+.55));}
function rise(t,a,d,n,y,dy){const k=sl(t,a,d||.9);T(n,n._x,y+(1-k)*(dy||140),0,1);op(n,seg(t,a,a+(d||.9)*.6));}
function stampIn(t,o,a,x,y,r,s0){const s=seg(t,a,a+.9);T(o,x,y,r||-4,s>0?lerp(s0||1.4,1,eo3(s)):0);op(o,clamp(s*2.5));}
function fit(p,s,x,y,fs,fill,maxW,anchor){const t=txt(p,s,x,y,fs,fill,'bold',anchor||'middle');const L=t.getComputedTextLength();if(L>maxW)t.setAttribute('font-size',fs*maxW/L);return t;}
// scheda con nastro adesivo (centrata in 0,0)
function taped(p,w,h,fill,r){const g=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:r||16,fill:fill||'url(#g_paper)',stroke:'#fff','stroke-width':3,filter:'url(#g_sh)'},g);
 [[-w/2+46,-h/2+4,-9],[w/2-46,-h/2+4,9]].forEach(([x,y,rr])=>el('rect',{x:x-58,y:y-19,width:116,height:38,rx:4,fill:'#FFE7A0','fill-opacity':.9,stroke:'#E3C25E','stroke-width':2,transform:'rotate('+rr+' '+x+' '+y+')'},g));
 return g;}
// titoletto: striscia notizie + tre pallini (novita' accese man mano)
function head(p,o){o.lab=el('g',{},p);
 el('rect',{x:-470,y:-46,width:940,height:92,rx:18,fill:NAVY,stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},o.lab);
 el('rect',{x:-470,y:-46,width:300,height:92,rx:18,fill:AMB},o.lab);el('rect',{x:-200,y:-46,width:30,height:92,fill:AMB},o.lab);
 fit(o.lab,'MANOVRA 2027',-320,13,36,NAVY,260);
 fit(o.lab,'DISEGNO DI LEGGE',60,13,34,'#fff',380);
 o.dots=[0,1,2].map(k=>el('circle',{cx:330+k*50,cy:0,r:16,fill:'#fff','fill-opacity':.28,stroke:'#fff','stroke-width':3},o.lab));}
function headU(t,o,lit){T(o.lab,540,150,0,1);op(o.lab,seg(t,0,.9));o.dots.forEach((c,k)=>{const on=(typeof lit==='function'?lit(t):lit)>k;c.setAttribute('fill',on?AMB:'#fff');c.setAttribute('fill-opacity',on?1:.28);});}
// didascalia: fumetto bianco con altoparlante
function balloon(p,lines,fs){fs=fs||48;const c=el('g',{},p);
 const longest=lines.reduce((a,b)=>a.length>b.length?a:b);let tmp=txt(c,longest,0,0,fs,'#000');let w0=tmp.getComputedTextLength();tmp.remove();
 if(w0>800){fs=fs*800/w0;w0=800;}
 const w=w0+200,h=lines.length*fs*1.36+64;
 el('path',{d:'M'+(-w/2+80)+' '+(h/2-6)+' L'+(-w/2+46)+' '+(h/2+46)+' L'+(-w/2+150)+' '+(h/2-6)+'Z',fill:'#fff',stroke:AMB,'stroke-width':7,'stroke-linejoin':'round'},c);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:44,fill:'#fff',stroke:AMB,'stroke-width':7,filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2+66,y:h/2-12,width:92,height:16,fill:'#fff'},c);
 const sp=el('g',{transform:'translate('+(-w/2+78)+' 0)'},c);el('circle',{r:36,fill:NAVY},sp);
 el('path',{d:'M-16 -9 H-6 L8 -20 V20 L-6 9 H-16Z',fill:'#fff'},sp);
 el('path',{d:'M16 -10 Q24 0 16 10',fill:'none',stroke:AMB,'stroke-width':5,'stroke-linecap':'round'},sp);el('path',{d:'M22 -18 Q36 0 22 18',fill:'none',stroke:AMB,'stroke-width':5,'stroke-linecap':'round'},sp);
 lines.forEach((l,i)=>txt(c,l,46,-h/2+34+fs*0.98+i*fs*1.36,fs,NAVY,'bold'));c._x=540;return c;}
// sfondo: fogli di documento che salgono piano
let BGX=null;
function bgx(t){if(!BGX){const b=document.getElementById('bok');BGX=[];for(let k=0;k<9;k++){const g=el('g',{},b);const w=170+(k%3)*30,h=230+(k%2)*40;
  el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:10,fill:'#9BF0DB','fill-opacity':.06+(k%3)*.015,stroke:'#9BF0DB','stroke-opacity':.14,'stroke-width':2},g);
  for(let r=0;r<6;r++)el('rect',{x:-w/2+20,y:-h/2+30+r*((h-60)/6),width:w*(0.45+((r*7+k)%4)*.1),height:8,rx:4,fill:'#9BF0DB','fill-opacity':.16},g);
  BGX.push([g,(k*127+90)%1000+40,(k*229)%1920,8+(k*5)%12,(k%2?1:-1)*(6+k%5)]);}}
 BGX.forEach(([g,x,y,sp,rot],k)=>{g.setAttribute('transform','translate('+(x+26*Math.sin(t*.25+k))+' '+((((y-t*sp)%2100)+2100)%2100-90)+') rotate('+(rot+3*Math.sin(t*.2+k))+')');});}
/*DUR*/
/*TX*/
function vt(i,frag){const s=TX[i];const k=s.indexOf(frag);if(k<0)throw new Error('frag '+frag);return 0.15+(DUR[i]-0.6)*k/s.length-0.15;}
const GAP=1.0;
function plan(i,frags){const n=frags.length+1,lim=0.8*DUR[i]-0.9;let t=frags.map(f=>vt(i,f)).concat([99]);
 t[0]=Math.max(t[0],GAP);for(let k=1;k<n;k++)t[k]=Math.max(t[k],t[k-1]+GAP);
 for(let k=n-1;k>=0;k--){const m=lim-(n-1-k)*GAP;if(t[k]>m)t[k]=m;}
 return t;}
const PL=[];
