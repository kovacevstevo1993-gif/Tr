// ---------- helper short 2 ----------
let UID=0;
const AMB='#FFB838',INK='#0B4A50',GRN='#1B9F81',LT='#7FF0D2';
function calendarPage(p,headTxt,bigTxt,bigSize,subTxt){
 const g=el('g',{},p);const id='cc'+(++UID);
 el('rect',{x:-232,y:6,width:464,height:566,rx:34,fill:'#C9D6D8'},g);
 el('rect',{x:-230,y:0,width:460,height:560,rx:34,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 const cp=el('clipPath',{id:id},g);el('rect',{x:-230,y:0,width:460,height:560,rx:34},cp);
 const hg=el('g',{'clip-path':'url(#'+id+')'},g);
 el('rect',{x:-230,y:0,width:460,height:130,fill:'url(#g_head)'},hg);
 el('rect',{x:-230,y:0,width:460,height:10,fill:'#fff',opacity:.35},hg);
 el('rect',{x:-230,y:128,width:460,height:8,fill:INK,opacity:.15},hg);
 const head=txt(g,headTxt,0,86,46,'#FFFFFF');
 const big=txt(g,bigTxt,0,bigSize>200?400:376,bigSize,INK);
 const sub=txt(g,subTxt||'',0,478,46,GRN);
 for(let i=0;i<14;i++)el('rect',{x:-200+i*30,y:512,width:16,height:4,rx:2,fill:'#B7C7CA'},g);
 metalRing(g,-120,-44,36,92);metalRing(g,120,-44,36,92);
 return {g,head,big,sub};}
function plate(p,big,small){
 const g=el('g',{},p);
 el('rect',{x:-210,y:-150,width:420,height:300,rx:44,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-210,y:-150,width:420,height:300,rx:44,fill:'none',stroke:'#fff','stroke-opacity':.8,'stroke-width':4},g);
 const b=txt(g,big,0,48,230,INK);
 const s=txt(g,small,0,118,38,GRN);
 return {g,b,s};}
function dotsRow(p,n,y){const g=el('g',{},p);const a=[];
 for(let i=0;i<n;i++){const c=el('circle',{cx:(i-(n-1)/2)*42,cy:y,r:15,fill:'#0A3F45',opacity:.55,stroke:'#7FF0D2','stroke-width':2},g);a.push(c);}
 return {g,a};}
function lightDot(d,on,k){ // k = pop 0..1
 d.setAttribute('fill',on?AMB:'#0A3F45');d.setAttribute('opacity',on?1:.55);d.setAttribute('r',15+(on?9*Math.sin(clamp(k)*Math.PI):0));}
function chip(p,label,w){w=w||300;const g=el('g',{},p);
 el('rect',{x:-w/2,y:-46,width:w,height:92,rx:46,fill:AMB,filter:'url(#g_sh2)'},g);
 el('rect',{x:-w/2,y:-46,width:w,height:92,rx:46,fill:'none',stroke:'#fff','stroke-width':5,'stroke-opacity':.85},g);
 const t=txt(g,label,0,19,54,'#5A3300');return {g,t};}
function warn(p){const g=el('g',{},p);
 el('path',{d:'M0 -150 L170 130 Q182 152 158 152 L-158 152 Q-182 152 -170 130 Z',fill:'#fff',stroke:'#E4412C','stroke-width':28,'stroke-linejoin':'round',filter:'url(#g_sh)'},g);
 txt(g,'!',0,104,210,'#0B2E33');return g;}
function qBubble(p,r){const g=el('g',{},p);
 el('circle',{cx:0,cy:0,r:r,fill:'url(#g_badge)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},g);
 txt(g,'?',0,r*.38,r*1.25,'#fff');return g;}
function medal(p,female){const g=el('g',{},p);
 el('circle',{cx:0,cy:0,r:190,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('circle',{cx:0,cy:0,r:190,fill:'none',stroke:'#fff','stroke-width':6,'stroke-opacity':.8},g);
 const cp='mc'+(++UID);const c=el('clipPath',{id:cp},g);el('circle',{cx:0,cy:0,r:176},c);
 const ig=el('g',{'clip-path':'url(#'+cp+')'},g);
 el('circle',{cx:0,cy:0,r:176,fill:'#E4F5F1'},ig);
 if(female){
  el('circle',{cx:0,cy:-52,r:84,fill:'#0B4A50'},ig); // capelli
  el('path',{d:'M-84 -52 L-96 70 Q0 96 96 70 L84 -52 Z',fill:'#0B4A50'},ig);
  el('path',{d:'M-60 176 L-46 40 L46 40 L60 176 Z',fill:GRN},ig);
  el('path',{d:'M-150 176 L-60 60 L60 60 L150 176 Z',fill:GRN},ig);
  el('rect',{x:-22,y:20,width:44,height:34,fill:'#F2C9A5'},ig);
  el('circle',{cx:0,cy:-42,r:60,fill:'#F7D5B5'},ig);
  el('path',{d:'M-62 -52 Q-10 -120 62 -52 Q20 -80 -62 -52 Z',fill:'#0B4A50'},ig);
  el('circle',{cx:-20,cy:-38,r:5,fill:'#0B4A50'},ig);el('circle',{cx:20,cy:-38,r:5,fill:'#0B4A50'},ig);
  el('path',{d:'M-14 -14 Q0 -4 14 -14',fill:'none',stroke:'#C0583F','stroke-width':5,'stroke-linecap':'round'},ig);
 }else{
  el('path',{d:'M-140 176 Q-140 50 0 50 Q140 50 140 176 Z',fill:INK},ig);
  el('polygon',{points:'-34,50 34,50 0,110',fill:'#fff'},ig);
  el('polygon',{points:'-12,66 12,66 8,150 -8,150',fill:'#E4412C'},ig);
  el('rect',{x:-24,y:20,width:48,height:40,fill:'#F2C9A5'},ig);
  el('circle',{cx:0,cy:-30,r:62,fill:'#F7D5B5'},ig);
  el('path',{d:'M-62 -40 Q-50 -100 0 -96 Q50 -100 62 -40 Q40 -70 0 -66 Q-40 -70 -62 -40 Z',fill:'#6F878C'},ig);
  el('circle',{cx:-20,cy:-28,r:5,fill:INK},ig);el('circle',{cx:20,cy:-28,r:5,fill:INK},ig);
  el('path',{d:'M-16 -4 Q0 8 16 -4',fill:'none',stroke:'#C0583F','stroke-width':5,'stroke-linecap':'round'},ig);
 }
 return g;}
function hardhat(p){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:'M-135 40 A135 135 0 0 1 135 40 Z',fill:'#FFC21F'},g);
 el('rect',{x:-30,y:-100,width:60,height:140,rx:18,fill:'#FFD65A'},g);
 el('rect',{x:-170,y:34,width:340,height:40,rx:20,fill:'#F2A900'},g);
 el('path',{d:'M-100 20 A110 110 0 0 1 -50 -70',fill:'none',stroke:'#fff','stroke-width':12,'stroke-linecap':'round',opacity:.6},g);
 return g;}
function shield(p){const g=el('g',{filter:'url(#g_sh)'},p);
 el('path',{d:'M0 -200 L170 -135 L170 30 Q170 150 0 220 Q-170 150 -170 30 L-170 -135 Z',fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,'stroke-linejoin':'round'},g);
 el('path',{d:'M0 -170 L140 -118 L140 28 Q140 128 0 188 Q-140 128 -140 28 L-140 -118 Z',fill:'none',stroke:'#fff','stroke-width':3,opacity:.5},g);
 return g;}
function progress(p){const g=el('g',{},p);
 const W=760,S=W/45;
 el('rect',{x:-W/2,y:0,width:W,height:46,rx:23,fill:'#0A3F45',opacity:.7},g);
 el('rect',{x:-W/2,y:0,width:W,height:46,rx:23,fill:'none',stroke:LT,'stroke-width':3,opacity:.6},g);
 const fill=el('rect',{x:-W/2,y:0,width:10,height:46,rx:23,fill:'url(#g_badge)'},g);
 for(let k=0;k<=40;k+=10){el('rect',{x:-W/2+k*S-1.5,y:56,width:3,height:16,fill:'#fff',opacity:.7},g);txt(g,''+k,-W/2+k*S,112,34,'#E9FBF6','bold','middle');}
 const cnt=txt(g,'',0,-52,70,'#fff');
 const lab=txt(g,'ANNI DI CONTRIBUTI',0,176,36,LT);
 function set(v){fill.setAttribute('width',Math.max(0,v*S));const Y=Math.floor(v+1e-6),M=Math.round((v-Y)*12);cnt.textContent=Y+' anni e '+M+' mesi';}
 return {g,set};}
function pill(p,label,w,fs,fill){const g=el('g',{},p);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:fs*1.8,rx:fs*0.9,fill:fill||AMB,filter:'url(#g_sh2)'},g);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:fs*1.8,rx:fs*0.9,fill:'none',stroke:'#fff','stroke-width':4,'stroke-opacity':.85},g);
 txt(g,label,0,fs*0.36,fs,fill?'#fff':'#5A3300');return g;}
function checkBadge(p,r){const g=el('g',{},p);
 el('circle',{cx:0,cy:0,r:r,fill:'url(#g_badge)',stroke:'#fff','stroke-width':r*0.12,filter:'url(#g_sh2)'},g);
 el('path',{d:`M${-r*.42} ${r*.02} L${-r*.1} ${r*.34} L${r*.46} ${-r*.3}`,fill:'none',stroke:'#fff','stroke-width':r*.22,'stroke-linecap':'round','stroke-linejoin':'round'},g);return g;}
function ring(p,r){return el('circle',{cx:0,cy:0,r:r,fill:'none',stroke:LT,'stroke-width':6,opacity:0},p);}

const S=[];
// ---------- 1 : hook "Aspetta!" ----------
S[0]={D:4.633,build(g){const o={};
 o.cal=calendarPage(g,'GENNAIO','2027',150,'');
 o.cal.sub.textContent='';
 o.warn=el('g',{},g);warn(o.warn);
 o.rg=el('g',{},g);o.rg1=ring(o.rg,150);o.rg2=ring(o.rg,150);
 this.o=o;},
 update(t){const o=this.o;
 const p=eob(seg(t,0.05,0.85));const y=lerp(-900,130,p);
 const tt=Math.max(0,t-0.8);const ang=t>0.8?8*Math.exp(-2.4*tt)*Math.sin(8*tt):0;
 T(o.cal.g,540,y,ang,1.25);
 const pw=eob(seg(t,0.85,1.5));
 const rot=t>1.5?4*Math.sin((t-1.5)*9)*Math.exp(-(t-1.5)*0.6):0;
 T(o.warn,540,1450,rot,Math.max(0,pw)*1.7*(t>1.5?1+0.04*Math.sin((t-1.5)*8):1));
 T(o.rg,540,1450,0,1);
 [o.rg1,o.rg2].forEach((c,i)=>{const k=((t-1.5-i*0.45)%1.1+1.1)%1.1/1.1;if(t>1.5){c.setAttribute('r',230+k*230);c.setAttribute('opacity',(1-k)*0.8);}});
 }};
// ---------- 2 : vecchiaia 67 -> 67 e 1 mese ----------
S[1]={D:9.933,build(g){const o={};
 o.cal=calendarPage(g,'GENNAIO','1',320,'2027');
 o.stairs=el('g',{},g);o.st=[0,1,2,3].map(i=>{const h=70+i*65;const r=el('rect',{x:-300+i*155,y:150-h,width:140,height:h,rx:16,fill:i==3?'url(#g_badge)':'#CFE9E3',stroke:'#fff','stroke-width':4},o.stairs);return {r,h,i};});
 o.arrow=el('g',{},o.stairs);el('path',{d:'M-60 40 L0 -40 L60 40 L25 40 L25 110 L-25 110 L-25 40 Z',fill:AMB,stroke:'#fff','stroke-width':6,'stroke-linejoin':'round',filter:'url(#g_sh2)'},o.arrow);
 o.pl=el('g',{},g);o.plate=plate(o.pl,'67','ANNI');
 o.dr=dotsRow(o.pl,12,225);
 o.chip=el('g',{},g);o.chipO=chip(o.chip,'+1 MESE',320);
 o.sp=ring(g,100);
 this.o=o;},
 update(t){const o=this.o;
 const p=eob(seg(t,0.1,0.9));T(o.cal.g,540,lerp(-900,120,p),t>0.9?6*Math.exp(-2.4*(t-0.9))*Math.sin(8*(t-0.9)):0,1.2);
 // scalini
 o.st.forEach((s,i)=>{const k=eob(seg(t,2.6+i*0.55,3.1+i*0.55));s.r.setAttribute('transform','translate(0 '+(s.h)+') scale(1 '+Math.max(0,k)+') translate(0 '+(-s.h)+')');
   s.r.setAttribute('transform','translate(0,150) scale(1,'+Math.max(0,k)+') translate(0,-150)');});
 const pa=eob(seg(t,4.5,5.1));
 T(o.arrow,232,lerp(-150,-235,pa),0,Math.max(0,pa));
 const out=eio(seg(t,5.35,5.9));
 T(o.stairs,540,1400+out*40,0,1.4*lerp(1,0.0,out));
 // plate
 const pp=eob(seg(t,5.5,6.2));T(o.pl,540,1440,0,1.5*Math.max(0,pp));
 const dp=seg(t,5.9,6.4);op(o.dr.g,dp);
 // chip
 const pc=eob(seg(t,7.3,8.0));const cy=lerp(900,1190,pc);
 T(o.chip,lerp(1000,850,eo3(seg(t,7.3,7.9))),cy,lerp(18,8,pc),Math.max(0,pc));
 const land=t>7.8;
 if(land){lightDot(o.dr.a[0],true,seg(t,7.9,8.4));o.plate.s.textContent='ANNI E 1 MESE';o.plate.s.setAttribute('font-size',34);}
 const rr=seg(t,7.9,8.5);o.sp.setAttribute('r',lerp(30,200,rr));o.sp.setAttribute('opacity',t>7.9?(1-rr)*0.8:0);T(o.sp,850,1200,0,1);
 if(t>8.6){const k=1+0.03*Math.sin((t-8.6)*6);T(o.pl,540,1440,0,1.5*k);}
 }};
// ---------- 3 : 2028, +3 mesi ----------
S[2]={D:5.4,build(g){const o={};
 o.cal=calendarPage(g,'ANNO','2027',150,'');
 o.pl=el('g',{},g);o.plate=plate(o.pl,'67','ANNI E 1 MESE');o.plate.s.setAttribute('font-size',34);
 o.dr=dotsRow(o.pl,12,225);lightDot(o.dr.a[0],true,0);
 o.chip=el('g',{},g);o.chipO=chip(o.chip,'+1 MESE',320);
 o.sp=ring(g,100);
 this.o=o;},
 update(t){const o=this.o;
 const pc=eob(seg(t,0.0,0.5));
 T(o.cal.g,540,120,0,1.2);
 // flip 2027 -> 2028
 const f=seg(t,1.5,2.3);const sc=f<0.5?1-f*2:(f-0.5)*2;
 o.cal.big.textContent=f<0.5?'2027':'2028';
 o.cal.g.setAttribute('transform','translate(540 '+(120+336)+') scale(1.2 '+(1.2*Math.max(0.02,Math.abs(sc)))+') translate(0 -280)');
 T(o.pl,540,1440,0,1.5);op(o.pl,seg(t,0,0.3));
 // chip +1 -> +3
 const flip=seg(t,2.7,3.3);const cs=flip<0.5?1-flip*2:(flip-0.5)*2;
 o.chipO.t.textContent=flip<0.5?'+1 MESE':'+3 MESI';
 o.chip.setAttribute('transform','translate(850 1190) rotate(8) scale(1 '+Math.max(0.05,Math.abs(cs))+')');
 const k1=seg(t,3.5,4.0),k2=seg(t,3.9,4.4);
 lightDot(o.dr.a[1],t>3.5,k1);lightDot(o.dr.a[2],t>3.9,k2);
 if(t>3.5){o.plate.s.textContent='ANNI E 3 MESI';}
 const rr=seg(t,3.9,4.5);o.sp.setAttribute('r',lerp(30,200,rr));o.sp.setAttribute('opacity',t>3.9?(1-rr)*0.8:0);T(o.sp,850,1200,0,1);
 if(t>4.5){const k=1+0.03*Math.sin((t-4.5)*6);T(o.pl,540,1440,0,1.5*k);}
 }};
// ---------- 4 : anticipata uomini ----------
S[3]={D:8.2,build(g){const o={};
 o.med=el('g',{},g);o.medO=medal(o.med,false);
 o.q=el('g',{},g);qBubble(o.q,80);
 o.tag=el('g',{},g);pill(o.tag,'ANTICIPATA',520,54,'#E4412C');
 o.pr=el('g',{},g);o.prog=progress(o.pr);
 o.tag2=el('g',{},g);pill(o.tag2,'UOMINI',330,54);
 this.o=o;},
 update(t){const o=this.o;
 const pm=eob(seg(t,0.1,0.8));T(o.med,540,450,0,1.45*Math.max(0,pm));
 const pq=eob(seg(t,0.5,1.1));T(o.q,810,230,10*Math.sin(t*4),1.3*Math.max(0,pq)*(1+0.06*Math.sin(t*6)));op(o.q,t<2.6?1:1-seg(t,2.6,3.0));
 const pt=eob(seg(t,1.4,2.0));T(o.tag,540,800,0,1.15*Math.max(0,pt));
 const pb=eob(seg(t,2.3,2.9));T(o.pr,540,1400,0,1.15*Math.max(0,pb));
 const v=eio(seg(t,2.8,6.0))*42.9167;o.prog.set(Math.max(0.0001,v));
 const p2=eob(seg(t,6.1,6.7));
 T(o.tag2,540,800,0,0);
 // UOMINI sostituisce ANTICIPATA sul tag
 if(t>6.1){T(o.tag,540,800,0,1.15*Math.max(0,1-seg(t,6.1,6.4)));T(o.tag2,540,800,0,1.15*Math.max(0,p2));}
 if(t>6.7){const k=1+0.02*Math.sin((t-6.7)*7);T(o.pr,540,1400,0,1.15*k);}
 }};
// ---------- 5 : donne ----------
S[4]={D:3.6,build(g){const o={};
 o.med=el('g',{},g);o.medM=medal(o.med,false);
 o.medF=el('g',{},g);medal(o.medF,true);
 o.tag=el('g',{},g);pill(o.tag,'DONNE',330,54);
 o.pr=el('g',{},g);o.prog=progress(o.pr);
 o.arr=el('g',{},g);chip(o.arr,'-1 ANNO',320);
 o.ch=el('g',{},g);checkBadge(o.ch,64);
 this.o=o;},
 update(t){const o=this.o;
 // swap uomo -> donna con flip
 const f=seg(t,0.15,0.75);const s=f<0.5?1-f*2:(f-0.5)*2;
 const first=f<0.5;op(o.med,first?1:0);op(o.medF,first?0:1);
 o.med.setAttribute('transform','translate(540 450) scale('+(1.45*Math.max(0.02,s))+' 1.45)');o.medF.setAttribute('transform','translate(540 450) scale('+(1.45*Math.max(0.02,s))+' 1.45)');
 T(o.pr,540,1400,0,1.15);
 const v=lerp(42.9167,41.9167,eio(seg(t,0.4,1.4)));o.prog.set(v);
 const pt=eob(seg(t,0.9,1.5));T(o.tag,540,800,0,1.15*Math.max(0,pt));
 T(o.arr,540,1130,0,1.1*Math.max(0,eob(seg(t,0.45,0.95)))*(t<1.9?1:Math.max(0,1-seg(t,1.9,2.2))));
 const pc=eob(seg(t,1.5,2.1));T(o.ch,830,260,0,1.3*Math.max(0,pc));
 }};
// ---------- 6 : lavori usuranti ----------
S[5]={D:6.167,build(g){const o={};
 o.sh=el('g',{},g);shield(o.sh);
 o.hat=el('g',{},g);hardhat(o.hat);
 o.chip=el('g',{},g);chip(o.chip,'+1 MESE',320);
 o.sp=ring(g,100);
 o.ch=el('g',{},g);checkBadge(o.ch,70);
 o.ex=el('g',{},g);pill(o.ex,'ESCLUSO',440,80,'#E4412C');
 o.w=el('g',{},g);warn(o.w);
 this.o=o;},
 update(t){const o=this.o;
 const ps=eob(seg(t,0.15,0.85));T(o.sh,540,440,0,1.5*Math.max(0,ps));
 // chip che rimbalza sullo scudo
 const a=seg(t,0.7,1.9);const b=seg(t,1.9,2.6);
 const cx=a<1?lerp(1100,700,eo3(a)):lerp(700,1000,eo3(b));
 const cy=a<1?lerp(1300,520,eo3(a)):lerp(520,1150,eo3(b));
 T(o.chip,cx,cy,lerp(0,-14,a),t<0.7||t>2.7?0:1.2);
 const rr=seg(t,1.85,2.4);o.sp.setAttribute('r',lerp(30,210,rr));o.sp.setAttribute('opacity',t>1.85?(1-rr)*0.9:0);T(o.sp,720,470,0,1);
 // avviso
 T(o.w,540,1450,0,Math.max(0,eob(seg(t,0.2,0.8)))*1.4*(t<2.6?1:Math.max(0,1-seg(t,2.6,3.0))));
 // elmetto
 const ph=eob(seg(t,2.7,3.4));T(o.hat,540,lerp(-250,400,ph),0,Math.max(0,ph)*1.4);
 const pc=eob(seg(t,5.0,5.6));T(o.ch,800,650,0,1.25*Math.max(0,pc));
 const pe=eob(seg(t,5.1,5.7));T(o.ex,540,1450,0,1.3*Math.max(0,pe));
 }};
// ---------- 7 : Mai Inps + patronato ----------
S[6]={D:6.4,build(g){const o={};
 o.ph=el('g',{},g);
 el('rect',{x:-210,y:0,width:420,height:700,rx:56,fill:'#0A2B30',filter:'url(#g_sh)'},o.ph);
 el('rect',{x:-210,y:0,width:420,height:700,rx:56,fill:'none',stroke:'#7FA9AE','stroke-width':5},o.ph);
 el('rect',{x:-186,y:26,width:372,height:648,rx:36,fill:'#EAF7F4'},o.ph);
 el('rect',{x:-186,y:26,width:372,height:100,rx:36,fill:'url(#g_head)'},o.ph);el('rect',{x:-186,y:90,width:372,height:36,fill:'url(#g_head)'},o.ph);
 txt(o.ph,'I TUOI CONTRIBUTI',0,92,32,'#fff');
 o.rw=[];['2022','2023','2024','2025','2026'].forEach((y,i)=>{const yy=170+i*100;
   txt(o.ph,y,-150,yy+32,30,INK,'bold','start');
   el('rect',{x:-50,y:yy+6,width:200,height:30,rx:15,fill:'#C9D6D8'},o.ph);
   const f=el('rect',{x:-50,y:yy+6,width:10,height:30,rx:15,fill:'url(#g_badge)'},o.ph);
   const c=el('g',{},o.ph);checkBadge(c,18);T(c,168,yy+21,0,0);
   o.rw.push({f,c});});
 o.q=el('g',{},g);qBubble(o.q,90);
 o.pt=el('g',{},g);
 el('rect',{x:-330,y:-130,width:660,height:260,rx:40,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.pt);
 const ic=el('g',{},o.pt);el('circle',{cx:-220,cy:-10,r:70,fill:'#E4F5F1'},ic);
 el('circle',{cx:-220,cy:-30,r:26,fill:GRN},ic);el('path',{d:'M-266 40 Q-266 -4 -220 -4 Q-174 -4 -174 40 Z',fill:GRN},ic);
 txt(o.pt,'PATRONATO',70,28,64,INK);
 o.ck=el('g',{},g);checkBadge(o.ck,70);
 this.o=o;},
 update(t){const o=this.o;
 const pp=eob(seg(t,0.1,0.8));T(o.ph,540,lerp(-900,110,pp),lerp(-6,0,pp),Math.max(0,pp)*1.1);
 o.rw.forEach((r,i)=>{const k=eo3(seg(t,0.5+i*0.45,1.1+i*0.45));r.f.setAttribute('width',Math.max(10,200*k));T(r.c,168,170+i*100+21,0,Math.max(0,eob(seg(t,1.0+i*0.45,1.3+i*0.45))));});
 const pq=eob(seg(t,2.9,3.5));T(o.q,540,1430,8*Math.sin(t*5),1.5*Math.max(0,pq)*(t<3.9?1:Math.max(0,1-seg(t,3.9,4.2))));
 const pt=eob(seg(t,3.9,4.5));T(o.pt,540,1430,0,1.25*Math.max(0,pt));
 const pc=eob(seg(t,5.3,5.8));T(o.ck,930,1290,0,1.2*Math.max(0,pc));
 }};
