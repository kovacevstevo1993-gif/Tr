// ===== VIDEO 2 - BLOCCO 1 (1920x1080) - hook: due colleghi =====
function payslip(p,title){const g=el('g',{},p);
 el('rect',{x:-130,y:-170,width:260,height:340,rx:18,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-130,y:-170,width:260,height:52,rx:18,fill:GRN},g);el('rect',{x:-130,y:-140,width:260,height:22,fill:GRN},g);
 txt(g,title,0,-130,28,'#fff','bold');
 [-90,-50,-10,30].forEach((y,i)=>{el('rect',{x:-100,y:y,width:i%2?130:190,height:14,rx:7,fill:'#C3D3D7'},g);});
 el('circle',{cx:70,cy:110,r:34,fill:AMB,stroke:'#fff','stroke-width':4},g);txt(g,'€',70,124,44,'#5A3300','900');
 return g;}
function tag(p,s,w,fill,col,fs){fs=fs||40;const g=el('g',{},p);
 el('rect',{x:-w/2,y:-38,width:w,height:76,rx:38,fill:fill,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
 txt(g,s,0,fs*0.36,fs,col||'#fff','bold');return g;}
function calc(p){const g=el('g',{filter:'url(#g_sh)'},p);
 el('rect',{x:-110,y:-150,width:220,height:300,rx:30,fill:'#0B4A50',stroke:'#fff','stroke-width':6},g);
 el('rect',{x:-86,y:-124,width:172,height:62,rx:12,fill:'#D6F5EC'},g);txt(g,'=',60,-76,48,INK,'900','end');
 for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('rect',{x:-86+c*62,y:-40+r*58,width:48,height:42,rx:10,fill:c==2&&r==2?AMB:'#2FBF9B'},g);
 return g;}
const SB=[];
// --- Scena 1 (0 - 3.4): i due colleghi ---
SB[0]={s:0,e:3.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'DUE COLLEGHI');
 o.a=el('g',{},g);medal(o.a,false);o.b=el('g',{},g);medal(o.b,true);
 o.ta=el('g',{},g);tag(o.ta,'COLLEGA A',300,'url(#g_badge)');o.tb=el('g',{},g);tag(o.tb,'COLLEGA B',300,'url(#g_red)');
 o.pa=el('g',{},g);payslip(o.pa,'BUSTA PAGA');o.pb=el('g',{},g);payslip(o.pb,'BUSTA PAGA');
 o.eq=el('g',{},g);el('circle',{r:78,fill:'#fff',stroke:AMB,'stroke-width':10,filter:'url(#g_sh)'},o.eq);txt(o.eq,'=',0,34,110,INK,'900');
 o.da=dotsRow(g,12,0);o.db=dotsRow(g,12,0);
 o.la=txt(g,'CONTRIBUTI VERSATI',0,0,30,LT,'bold');o.lb=txt(g,'CONTRIBUTI VERSATI',0,0,30,LT,'bold');
 o.r1=el('g',{},g);tag(o.r1,'STESSO STIPENDIO',560,AMB,'#5A3300',44);
 o.r2=el('g',{},g);tag(o.r2,'STESSI CONTRIBUTI',560,AMB,'#5A3300',44);
 o.cap=el('g',{},g);cap(o.cap,'DUE COLLEGHI. STESSO STIPENDIO, STESSI CONTRIBUTI.',54);
 this.o=o;},
 update(t,o){o=this.o;
 T(o.top,960,100,0,1);
 T(o.a,560,340,0,0.85*Math.max(0,eob(seg(t,0.1,0.6))));T(o.b,1360,340,0,0.85*Math.max(0,eob(seg(t,0.3,0.8))));
 T(o.ta,560,540,0,Math.max(0,eob(seg(t,0.5,0.9))));T(o.tb,1360,540,0,Math.max(0,eob(seg(t,0.7,1.1))));
 T(o.pa,250,340,-5,0.9*Math.max(0,eob(seg(t,1.0,1.5))));T(o.pb,1670,340,5,0.9*Math.max(0,eob(seg(t,1.1,1.6))));
 T(o.eq,960,340,0,Math.max(0,eob(seg(t,0.9,1.4)))*(1+0.05*Math.sin(t*6)));
 T(o.r1,960,770,0,Math.max(0,eob(seg(t,1.2,1.7))));
 T(o.da.g,560,640,0,1);T(o.db.g,1360,640,0,1);T(o.la,560,700,0,1);T(o.lb,1360,700,0,1);
 op(o.la,seg(t,1.4,1.7));op(o.lb,seg(t,1.4,1.7));
 const nd=Math.floor(clamp((t-1.6)/0.05,0,12));
 o.da.a.forEach((d,i)=>lightDot(d,i<nd,0.5));o.db.a.forEach((d,i)=>lightDot(d,i<nd,0.5));
 op(o.da.g,seg(t,1.4,1.7));op(o.db.g,seg(t,1.4,1.7));
 T(o.r2,960,840,0,Math.max(0,eob(seg(t,2.0,2.5))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.4,1.0))));
 }};
// --- Scena 2 (3.4 - 8.0): 64 contro 67 ---
SB[1]={s:3.4,e:8.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'DUE USCITE');
 o.ruler=el('g',{},g);
 el('rect',{x:-720,y:-12,width:1440,height:24,rx:12,fill:'#0A3F45',stroke:LT,'stroke-width':3},o.ruler);
 o.ticks=[];for(let i=0;i<7;i++){const x=-600+i*200;const tk=el('g',{},o.ruler);
  el('rect',{x:x-3,y:-34,width:6,height:68,rx:3,fill:'#fff',opacity:.85},tk);txt(tk,String(62+i),x,92,46,(62+i==64||62+i==67)?AMB:'#fff','bold');o.ticks.push(tk);}
 txt(o.ruler,'ETÀ DI USCITA',-640,-130,38,LT,'bold');
 o.pA=el('g',{},g);o.pB=el('g',{},g);
 [[o.pA,'COLLEGA A','64 ANNI','url(#g_badge)'],[o.pB,'COLLEGA B','67 ANNI','url(#g_red)']].forEach(([p,a,b,f])=>{
  el('path',{d:'M0 0 L-26 -50 L26 -50 Z',fill:'#fff'},p);
  el('rect',{x:-190,y:-230,width:380,height:180,rx:28,fill:f,stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},p);
  txt(p,a,0,-182,34,'#fff','bold');txt(p,b,0,-100,76,'#fff','900');});
 o.br=el('g',{},g);
 el('path',{d:'M-200 0 V40 H200 V0',fill:'none',stroke:AMB,'stroke-width':10,'stroke-linecap':'round','stroke-linejoin':'round'},o.br);
 o.chip=el('g',{},g);tag(o.chip,'3 ANNI DI DIFFERENZA',620,AMB,'#5A3300',46);
 o.cap=el('g',{},g);cap(o.cap,"UNO ESCE A 64 ANNI, L'ALTRO A 67",56);
 this.o=o;},
 update(t,o){o=this.o;
 T(o.top,960,100,0,1);
 const rp=eio(seg(t,0.05,0.6));T(o.ruler,960,600,0,rp);op(o.ruler,rp);
 const x64=960-600+2*200-0, x67=960-600+5*200;
 const dA=eob(seg(t,0.5,1.0));T(o.pA,x64,lerp(200,566,eo3(seg(t,0.5,1.0))),0,Math.max(0,dA)*0.9);
 const dB=eob(seg(t,2.4,2.9));T(o.pB,x67,lerp(200,566,eo3(seg(t,2.4,2.9))),0,Math.max(0,dB)*0.9);
 const bb=eob(seg(t,3.0,3.5));T(o.br,(x64+x67)/2,710,0,1);op(o.br,seg(t,3.0,3.4));
 o.br.setAttribute('transform','translate('+((x64+x67)/2)+' 735) scale('+(Math.max(0,bb)*1.5)+' 1)');
 T(o.chip,(x64+x67)/2,835,0,Math.max(0,eob(seg(t,3.2,3.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));
 }};
// --- Scena 3 (8.0 - 11.0): quanto cambia l'assegno ---
SB[2]={s:8.0,e:11.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA DOMANDA');
 function card(p,who,age,f){const c=el('g',{},p);
  el('rect',{x:-290,y:-210,width:580,height:420,rx:34,fill:'url(#g_paper)',filter:'url(#g_sh)'},c);
  el('rect',{x:-290,y:-210,width:580,height:84,rx:34,fill:f},c);el('rect',{x:-290,y:-160,width:580,height:34,fill:f},c);
  txt(c,who+' · '+age,0,-150,42,'#fff','bold');
  txt(c,'ASSEGNO AL MESE',0,-70,34,GRN,'bold');
  txt(c,'€',-170,70,120,INK,'900');
  [-100,-38,24,86,170,232].forEach(x=>el('circle',{cx:x,cy:42,r:19,fill:INK},c));txt(c,',',128,72,100,INK,'900');
  el('rect',{x:-240,y:110,width:480,height:60,rx:30,fill:'#FFE3DE'},c);txt(c,'LORDO · 13 MENSILITÀ',0,150,30,'#B23A28','bold');return c;}
 o.cA=el('g',{},g);card(o.cA,'COLLEGA A','64 ANNI','url(#g_badge)');
 o.cB=el('g',{},g);card(o.cB,'COLLEGA B','67 ANNI','url(#g_red)');
 o.q=el('g',{},g);qBubble(o.q,130);
 o.vs=el('g',{},g);tag(o.vs,'QUANTO CAMBIA?',470,AMB,'#5A3300',46);
 o.cap=el('g',{},g);cap(o.cap,"QUANTO CAMBIA L'ASSEGNO OGNI MESE?",58);
 this.o=o;},
 update(t,o){o=this.o;
 T(o.top,960,100,0,1);
 T(o.cA,lerp(-400,500,eo3(seg(t,0.1,0.8))),520,-2,0.95);T(o.cB,lerp(2300,1420,eo3(seg(t,0.3,1.0))),520,2,0.95);
 T(o.q,960,420,10*Math.sin(t*4),Math.max(0,eob(seg(t,0.7,1.2)))*(1+0.07*Math.sin(t*6)));
 T(o.vs,960,810,0,Math.max(0,eob(seg(t,1.2,1.7))));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));
 }};
// --- Scena 4 (11.0 - 14.1333): tieni a mente, alla fine il conto ---
SB[3]={s:11.0,e:14.1334,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TIENI A MENTE');
 o.note=el('g',{},g);
 el('rect',{x:-250,y:-210,width:500,height:420,rx:26,fill:'#FFF3C4',filter:'url(#g_sh)'},o.note);
 el('rect',{x:-250,y:-210,width:500,height:70,rx:26,fill:AMB},o.note);el('rect',{x:-250,y:-170,width:500,height:30,fill:AMB},o.note);
 txt(o.note,'LA TUA RISPOSTA',0,-160,38,'#5A3300','bold');
 [-80,-20,40,100].forEach(y=>el('rect',{x:-200,y:y,width:400,height:8,rx:4,fill:'#E0C58A'},o.note));
 txt(o.note,'€ ?',0,160,64,'#B23A28','900');
 o.pen=el('g',{},g);el('rect',{x:-14,y:-160,width:28,height:260,rx:10,fill:'#E4412C',stroke:'#fff','stroke-width':4},o.pen);el('polygon',{points:'-14,100 14,100 0,140',fill:'#F2C9A5'},o.pen);
 o.bar=el('g',{},g);
 el('rect',{x:-420,y:-18,width:840,height:36,rx:18,fill:'#0A3F45',stroke:LT,'stroke-width':3},o.bar);
 o.fill=el('rect',{x:-414,y:-12,width:12,height:24,rx:12,fill:'url(#g_badge)'},o.bar);
 txt(o.bar,'ORA',-420,-50,34,LT,'bold','middle');txt(o.bar,'FINE',420,-50,34,LT,'bold','middle');
 o.calc=el('g',{},g);calc(o.calc);
 o.lab=el('g',{},g);tag(o.lab,'ALLA FINE: IL CONTO',560,AMB,'#5A3300',46);
 o.sp=ring(g,100);
 o.cap=el('g',{},g);cap(o.cap,'TIENI A MENTE LA TUA RISPOSTA... ALLA FINE FACCIAMO IL CONTO!',48);
 this.o=o;},
 update(t,o){o=this.o;
 T(o.top,960,100,0,1);
 T(o.note,500,520,-3,Math.max(0,eob(seg(t,0.1,0.7))));
 T(o.pen,600+20*Math.sin(t*5),610+10*Math.cos(t*5),30,Math.max(0,eob(seg(t,0.4,0.9)))*0.7);
 T(o.bar,1330,640,0,Math.max(0,eob(seg(t,0.3,0.8))));
 const f=eio(seg(t,0.7,1.8));o.fill.setAttribute('width',12+828*f);
 T(o.calc,1700,400,0,Math.max(0,eob(seg(t,1.4,1.9)))*0.9);
 T(o.lab,1330,780,0,Math.max(0,eob(seg(t,1.6,2.1))));
 const rr=seg(t,1.8,2.4);o.sp.setAttribute('r',lerp(40,220,rr));o.sp.setAttribute('opacity',t>1.8?(1-rr)*0.8:0);T(o.sp,1700,400,0,1);
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.2,0.8))));
 }};
const TOT=14.1333;
const bok=document.getElementById('bok');
for(let i=0;i<16;i++){el('circle',{cx:(i*271)%1920,cy:(i*197)%1080,r:30+((i*37)%80),fill:'#8FF5DC',opacity:.06+((i*13)%7)*0.01},bok);}
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
 const z=1+0.02*(t/TOT);camG.setAttribute('transform','translate(960 540) scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
