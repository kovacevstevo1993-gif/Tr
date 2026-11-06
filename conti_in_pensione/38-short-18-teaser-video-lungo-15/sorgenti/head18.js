// ===== SHORT 18 - teaser video lungo 15 (Carta Dedicata a te e pensionati) (1080x1920, 30 fps) =====
// Regole N.15/N.18: comparsa 0.9 s, elementi che restano fino a fine scena, distanza >= 0,45 s, ultimo completo entro l'80 %, poi tutto FERMO.
// Look NUOVO rispetto a S17 (N.47): titoletto a PILLOLA BIANCA con mini carta + chip ambra (niente numeri, N.50), schede a TICKET con tacche, didascalia a COUPON con talloncino ambra,
// sfondo con CARTE PREPAGATE in trasparenza che salgono piano.
const eob2=x=>{const c1=1.0,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const pop=(t,a,d)=>Math.max(0,eob2(seg(t,a,a+(d||.9))));
const sl=(t,a,d)=>eo3(seg(t,a,a+(d||.9)));
const GRN='#13805F',DK='#0B4A50',ORG='#E8832A',AMB='#FFB020',NAVY='#06303A',SKIN='#F3C9A5';
document.querySelector('defs').insertAdjacentHTML('beforeend','<linearGradient id="gcA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2BCB9C"/><stop offset="1" stop-color="#0B6B58"/></linearGradient><linearGradient id="gcB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3B8FA0"/><stop offset="1" stop-color="#0B3F4C"/></linearGradient>');
function fade(t,n,x,y,a,dy){T(n,x,y+(1-sl(t,a,.9))*(dy===undefined?60:dy),0,1);op(n,seg(t,a,a+.55));}
function slideX(t,n,x,y,a,dx,r){T(n,x+(1-sl(t,a,.9))*dx,y,r||0,1);op(n,seg(t,a,a+.55));}
function rise(t,a,d,n,y,dy){const k=sl(t,a,d||.9);T(n,n._x,y+(1-k)*(dy||140),0,1);op(n,seg(t,a,a+(d||.9)*.6));}
function fit(p,s,x,y,fs,fill,maxW,anchor){const t=txt(p,s,x,y,fs,fill,'bold',anchor||'middle');const L=t.getComputedTextLength();if(L>maxW)t.setAttribute('font-size',fs*maxW/L);return t;}
function personI(p,s,col){const g=el('g',{},p);col=col||'#0B4A50';el('circle',{cx:0,cy:-30*s,r:20*s,fill:col},g);el('path',{d:`M${-34*s} ${40*s} Q${-34*s} ${-4*s} 0 ${-4*s} Q${34*s} ${-4*s} ${34*s} ${40*s}Z`,fill:col},g);return g;}
// carta prepagata: corpo con gradiente, chip, onde contactless, titolo, importo grande
function cardI(p,w,h,gid,title,big,sub){const g=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:34,fill:'url(#'+gid+')',stroke:'#fff','stroke-width':5,filter:'url(#g_sh)'},g);
 el('path',{d:`M${-w/2+34} ${-h/2} H${w/2-34} Q${w/2} ${-h/2} ${w/2} ${-h/2+34} V${-h/2+h*.22} Q0 ${-h/2+h*.34} ${-w/2} ${-h/2+h*.2} V${-h/2+34} Q${-w/2} ${-h/2} ${-w/2+34} ${-h/2}Z`,fill:'#fff','fill-opacity':.13},g);
 const cw=Math.min(96,w*.13),ch=cw*.76;
 el('rect',{x:-w/2+44,y:-h/2+h*.34,width:cw,height:ch,rx:14,fill:AMB,stroke:'#fff','stroke-width':3},g);
 el('line',{x1:-w/2+44,y1:-h/2+h*.34+ch/2,x2:-w/2+44+cw,y2:-h/2+h*.34+ch/2,stroke:'#C98300','stroke-width':3},g);el('line',{x1:-w/2+44+cw/2,y1:-h/2+h*.34,x2:-w/2+44+cw/2,y2:-h/2+h*.34+ch,stroke:'#C98300','stroke-width':3},g);
 [1,2,3].forEach(k=>el('path',{d:`M${-w/2+44+cw+22+k*14} ${-h/2+h*.34+ch/2-10-k*5} q${8+k*3} ${10+k*5} 0 ${20+k*10}`,fill:'none',stroke:'#fff','stroke-width':5,'stroke-linecap':'round','stroke-opacity':.8},g));
 fit(g,title,-w/2+44,-h/2+Math.min(66,h*.2),40,'#fff',w-100,'start');
 if(big)fit(g,big,w/2-44,h/2-52,h*.3,'#fff',w*.5,'end');
 if(sub)fit(g,sub,-w/2+44,h/2-44,30,'#D6F5EC',w*.36,'start');
 return g;}
// ticket (scheda con tacche semicircolari ai lati)
function ticket(p,w,h,col,stroke){const g=el('g',{},p);const r=26,n=26;
 el('path',{d:`M${-w/2+r} ${-h/2} H${w/2-r} Q${w/2} ${-h/2} ${w/2} ${-h/2+r} V${-n} A${n} ${n} 0 0 0 ${w/2} ${n} V${h/2-r} Q${w/2} ${h/2} ${w/2-r} ${h/2} H${-w/2+r} Q${-w/2} ${h/2} ${-w/2} ${h/2-r} V${n} A${n} ${n} 0 0 0 ${-w/2} ${-n} V${-h/2+r} Q${-w/2} ${-h/2} ${-w/2+r} ${-h/2}Z`,fill:col||'url(#g_paper)',stroke:stroke||'#fff','stroke-width':5,'stroke-linejoin':'round',filter:'url(#g_sh)'},g);return g;}
// titoletto: pillola bianca, mini carta a sinistra, titolo fisso e chip ambra con l'argomento
function head(p,o,label){o.lab=el('g',{},p);
 el('rect',{x:-490,y:-44,width:980,height:88,rx:44,fill:'#fff',stroke:GRN,'stroke-width':6,filter:'url(#g_sh2)'},o.lab);
 const mc=el('g',{transform:'translate(-428 0) rotate(-10)'},o.lab);el('rect',{x:-36,y:-24,width:72,height:48,rx:9,fill:'url(#gcA)',stroke:NAVY,'stroke-width':3},mc);el('rect',{x:-26,y:-8,width:20,height:15,rx:3,fill:AMB},mc);
 fit(o.lab,'CARTA DEDICATA A TE',-368,13,34,NAVY,470,'start');
 el('rect',{x:130,y:-31,width:344,height:62,rx:31,fill:AMB,stroke:NAVY,'stroke-width':3},o.lab);fit(o.lab,label,302,10,29,NAVY,300);}
function headU(t,o){T(o.lab,540,190,0,1);op(o.lab,seg(t,0,.9));}
// didascalia: coupon con tacche laterali e talloncino ambra con l'euro
function strip(p,lines,fs){fs=fs||46;const c=el('g',{},p);const w=900,h=lines.length*fs*1.3+64;
 ticket(c,w,h,'#fff',AMB);
 const sx=-w/2+150;
 el('path',{d:`M${-w/2+26} ${-h/2+5} H${sx} V${h/2-5} H${-w/2+26} Q${-w/2+5} ${h/2-5} ${-w/2+5} ${h/2-26} V26 A26 26 0 0 0 ${-w/2+5} -26 V${-h/2+26} Q${-w/2+5} ${-h/2+5} ${-w/2+26} ${-h/2+5}Z`,fill:AMB},c);
 el('line',{x1:sx,y1:-h/2+14,x2:sx,y2:h/2-14,stroke:NAVY,'stroke-width':4,'stroke-dasharray':'10 10'},c);
 euro(c,-w/2+82,0,.62,NAVY,15);
 lines.forEach((l,i)=>fit(c,l,sx+(w/2-sx)/2,-h/2+32+fs*0.98+i*fs*1.3,fs,NAVY,w/2-sx-50));
 c._x=540;return c;}
// sfondo: carte prepagate trasparenti che salgono piano
let BGX=null;
function bgx(t){if(!BGX){const b=document.getElementById('bok');BGX={r:[]};
 for(let k=0;k<9;k++){const g=el('g',{},b);const s=.8+(k%3)*.35;
  el('rect',{x:-110*s,y:-70*s,width:220*s,height:140*s,rx:22*s,fill:'#9BF0DB','fill-opacity':.09+(k%3)*.02},g);
  el('rect',{x:-80*s,y:-30*s,width:46*s,height:34*s,rx:8*s,fill:'#fff','fill-opacity':.15},g);el('rect',{x:-80*s,y:30*s,width:120*s,height:10*s,rx:5*s,fill:'#fff','fill-opacity':.12},g);
  BGX.r.push([g,(k*197)%900,(k*271)%2200,8+(k*3)%8,-14+(k%5)*7]);}}
 BGX.r.forEach(([g,x,y,sp,rot])=>{g.setAttribute('transform','translate('+(x+30*Math.sin(t*.15+x))+' '+((((y-t*sp)%2300)+2300)%2300-150)+') rotate('+rot+')');});}
/*DUR*/
/*TX*/
function vt(i,frag){const s=TX[i];const k=s.indexOf(frag);if(k<0)throw new Error('frag '+frag);
 const wt=c=>/[,:;]/.test(c)?7:/[.?!]/.test(c)?12:1;let tot=0,acc=0;for(let j=0;j<s.length;j++){const w=wt(s[j]);tot+=w;if(j<k)acc+=w;}
 return (DUR[i]-0.6)*acc/tot;}
const GAP=0.7;
function plan(i,frags){const n=frags.length+1,lim=0.8*DUR[i]-0.9;let t=frags.map(f=>vt(i,f)).concat([99]);
 t[0]=Math.max(t[0],1.0);for(let k=1;k<n;k++)t[k]=Math.max(t[k],t[k-1]+GAP);
 for(let k=n-1;k>=0;k--){const m=lim-(n-1-k)*GAP;if(t[k]>m)t[k]=m;}
 return t;}
const PL=[];
