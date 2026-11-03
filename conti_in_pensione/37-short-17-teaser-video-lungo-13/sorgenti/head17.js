// ===== SHORT 17 - teaser video lungo 13 (pensione di reversibilita') (1080x1920, 30 fps) =====
// Regole N.15/N.18: comparsa 0.9 s, elementi che restano fino a fine scena, distanza >= 0,45 s, ultimo completo entro l'80 %, poi tutto FERMO.
// Look NUOVO rispetto agli short 12-16 (N.47): titoletto a LINGUETTA DI FASCICOLO (niente numeri, N.50), schede a CARTELLINA / SCHEDA ANAGRAFICA,
// didascalia a STRISCIA DI CEDOLINO dentellata, sfondo con SCALINATE e RIGHE DI CEDOLINO che salgono piano.
const eob2=x=>{const c1=1.0,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2);};
const pop=(t,a,d)=>Math.max(0,eob2(seg(t,a,a+(d||.9))));
const sl=(t,a,d)=>eo3(seg(t,a,a+(d||.9)));
const GRN='#13805F',DK='#0B4A50',ORG='#E8832A',AMB='#FFB020',NAVY='#06303A',SKIN='#F3C9A5';
function fade(t,n,x,y,a,dy){T(n,x,y+(1-sl(t,a,.9))*(dy===undefined?60:dy),0,1);op(n,seg(t,a,a+.55));}
function slideX(t,n,x,y,a,dx,r){T(n,x+(1-sl(t,a,.9))*dx,y,r||0,1);op(n,seg(t,a,a+.55));}
function rise(t,a,d,n,y,dy){const k=sl(t,a,d||.9);T(n,n._x,y+(1-k)*(dy||140),0,1);op(n,seg(t,a,a+(d||.9)*.6));}
function fit(p,s,x,y,fs,fill,maxW,anchor){const t=txt(p,s,x,y,fs,fill,'bold',anchor||'middle');const L=t.getComputedTextLength();if(L>maxW)t.setAttribute('font-size',fs*maxW/L);return t;}
// titoletto: linguetta di fascicolo (etichetta dell'argomento) + corpo con il tema
function head(p,o,label){o.lab=el('g',{},p);
 el('rect',{x:-490,y:-34,width:980,height:80,rx:16,fill:NAVY,stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},o.lab);
 el('path',{d:'M-490 -34 V-52 Q-490 -78 -464 -78 H-196 Q-170 -78 -160 -52 L-146 -34 Z',fill:AMB,stroke:'#fff','stroke-width':4,'stroke-linejoin':'round'},o.lab);
 fit(o.lab,label,-318,-44,31,NAVY,296);
 fit(o.lab,'PENSIONE DI REVERSIBILITÀ',60,26,38,'#fff',600);
 el('path',{d:'M430 -30 V30 a14 14 0 0 0 28 0 V-20 a8 8 0 0 0 -16 0 V24',fill:'none',stroke:'#C9D6D8','stroke-width':5,'stroke-linecap':'round'},o.lab);}
function headU(t,o){T(o.lab,540,190,0,1);op(o.lab,seg(t,0,.9));}
// cartellina: corpo centrato in 0,0, linguetta sopra a sinistra
function folder(p,w,h,tab,col,fill){const g=el('g',{},p);const tw=Math.min(w*.5,330);
 el('path',{d:`M${-w/2} ${-h/2+4} V${-h/2-34} Q${-w/2} ${-h/2-58} ${-w/2+24} ${-h/2-58} H${-w/2+tw-28} Q${-w/2+tw-12} ${-h/2-58} ${-w/2+tw} ${-h/2-34} L${-w/2+tw+16} ${-h/2+4}Z`,fill:col,stroke:'#fff','stroke-width':4,'stroke-linejoin':'round'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:24,fill:fill||'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh)'},g);
 fit(g,tab,-w/2+tw/2-2,-h/2-18,32,'#fff',tw-44);return g;}
// scheda anagrafica: banda con il nome, riquadro foto con sagoma neutra, righe, badge "? %"
function idCard(p,w,h,label,col,kind){const g=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:24,fill:'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh)'},g);
 el('path',{d:`M${-w/2} ${-h/2+78} V${-h/2+24} Q${-w/2} ${-h/2} ${-w/2+24} ${-h/2} H${w/2-24} Q${w/2} ${-h/2} ${w/2} ${-h/2+24} V${-h/2+78}Z`,fill:col},g);
 fit(g,label,0,-h/2+52,38,'#fff',w-60);
 el('rect',{x:-w/2+24,y:-h/2+100,width:140,height:150,rx:14,fill:'#D6F5EC',stroke:'#9FB4B9','stroke-width':3},g);
 const ps=[];if(kind==='x2'){ps.push([-w/2+70,-h/2+190,.62],[-w/2+120,-h/2+190,.62]);}else if(kind==='old'){ps.push([-w/2+94,-h/2+196,.95]);}else if(kind==='kid'){ps.push([-w/2+94,-h/2+210,.62]);}else{ps.push([-w/2+94,-h/2+196,.95]);}
 ps.forEach(([x,y,s])=>{const q=personI(g,s,'#0B4A50');q.setAttribute('transform','translate('+x+' '+y+')');});
 [[196,190],[196,150],[196,110]].forEach(([wd,yy],k)=>0);
 [[200,-h/2+126],[160,-h/2+160],[120,-h/2+194]].forEach(([wd,yy])=>el('rect',{x:-w/2+190,y:yy,width:wd,height:12,rx:6,fill:'#B5C6C9'},g));
 const b=el('g',{transform:'translate('+(w/2-76)+' '+(h/2-62)+')'},g);el('circle',{r:48,fill:ORG,stroke:'#fff','stroke-width':5},b);fit(b,'? %',0,13,36,'#fff',58);
 return g;}
// didascalia: striscia di cedolino con bordo dentellato
function strip(p,lines,fs){fs=fs||46;const c=el('g',{},p);const w=900,h=lines.length*fs*1.3+64;
 const n=Math.round(w/30),st=w/n;let d='M'+(-w/2)+' '+(-h/2);
 for(let k=0;k<n;k++)d+=' L'+(-w/2+k*st+st/2)+' '+(-h/2-12)+' L'+(-w/2+(k+1)*st)+' '+(-h/2);
 d+=' V'+(h/2);
 for(let k=n;k>0;k--)d+=' L'+(-w/2+k*st-st/2)+' '+(h/2+12)+' L'+(-w/2+(k-1)*st)+' '+(h/2);
 d+='Z';
 el('path',{d:d,fill:'#fff',stroke:AMB,'stroke-width':5,'stroke-linejoin':'round',filter:'url(#g_sh2)'},c);
 el('line',{x1:-w/2+60,y1:-h/2+16,x2:w/2-30,y2:-h/2+16,stroke:'#9FB4B9','stroke-width':3,'stroke-dasharray':'8 10'},c);
 el('line',{x1:-w/2+60,y1:h/2-16,x2:w/2-30,y2:h/2-16,stroke:'#9FB4B9','stroke-width':3,'stroke-dasharray':'8 10'},c);
 el('rect',{x:-w/2+4,y:-h/2+4,width:34,height:h-8,rx:4,fill:GRN},c);
 const longest=lines.reduce((a,b)=>a.length>b.length?a:b);
 lines.forEach((l,i)=>fit(c,l,24,-h/2+32+fs*0.98+i*fs*1.3,fs,NAVY,780));
 c._x=540;return c;}
// sfondo: righe di cedolino e scalinate che salgono piano
let BGX=null;
function bgx(t){if(!BGX){const b=document.getElementById('bok');BGX={r:[],s:[]};
 for(let k=0;k<9;k++){const g=el('g',{},b);const w1=300+((k*97)%260),w2=90+((k*53)%110);
  el('rect',{x:0,y:0,width:w1,height:12,rx:6,fill:'#9BF0DB','fill-opacity':.1+(k%3)*.02},g);el('rect',{x:w1+30,y:0,width:w2,height:12,rx:6,fill:'#9BF0DB','fill-opacity':.14},g);
  BGX.r.push([g,(k*173)%700-120,(k*241)%2100,10+(k*3)%9]);}
 for(let k=0;k<3;k++){let d='M0 0';for(let j=0;j<9;j++)d+=' h70 v-52';const g=el('path',{d:d,fill:'none',stroke:'#9BF0DB','stroke-opacity':.13,'stroke-width':7,'stroke-linejoin':'round'},b);
  BGX.s.push([g,[80,560,300][k],[1500,950,1900][k],[1.5,1.1,.8][k],7+k*2]);}}
 BGX.r.forEach(([g,x,y,sp])=>{g.setAttribute('transform','translate('+(x+20*Math.sin(t*.2+x))+' '+((((y-t*sp)%2100)+2100)%2100-60)+')');});
 BGX.s.forEach(([g,x,y,sc,sp],k)=>{const yy=((((y-t*sp)%2300)+2300)%2300)-150;g.setAttribute('transform','translate('+(x+t*sp*.5)+' '+yy+') scale('+sc+')');});}
/*DUR*/
/*TX*/
// tempi: proporzionali ai caratteri, con pause piu' lunghe a virgole/due punti e a punti/domande
function vt(i,frag){const s=TX[i];const k=s.indexOf(frag);if(k<0)throw new Error('frag '+frag);
 const wt=c=>/[,:;]/.test(c)?7:/[.?!]/.test(c)?12:1;let tot=0,acc=0;for(let j=0;j<s.length;j++){const w=wt(s[j]);tot+=w;if(j<k)acc+=w;}
 return (DUR[i]-0.6)*acc/tot;}
const GAP=0.7;
function plan(i,frags){const n=frags.length+1,lim=0.8*DUR[i]-0.9;let t=frags.map(f=>vt(i,f)).concat([99]);
 t[0]=Math.max(t[0],1.0);for(let k=1;k<n;k++)t[k]=Math.max(t[k],t[k-1]+GAP);
 for(let k=n-1;k>=0;k--){const m=lim-(n-1-k)*GAP;if(t[k]>m)t[k]=m;}
 return t;}
const PL=[];
