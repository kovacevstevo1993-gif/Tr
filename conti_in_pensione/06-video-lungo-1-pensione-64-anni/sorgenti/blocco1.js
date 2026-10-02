// ===== BLOCCO 1 - video lungo 1 (1920x1080) =====
const FW=1920,FH=1080;
function topLabel(g,s){const t=el('g',{},g);
 el('polygon',{points:'0,-14 14,0 0,14 -14,0',fill:'#7FF0D2'},t);
 const x=txt(t,s,28,12,36,'#7FF0D2','bold','start');x.setAttribute('letter-spacing','9');
 const w=s.length*36*0.72+s.length*9+60;t.setAttribute('data-w',w);return t;}
function cap(g,s,size){size=size||62;const w=Math.min(1780,s.length*size*0.70+120);const c=el('g',{},g);
 el('rect',{x:-w/2,y:-62,width:w,height:124,rx:62,fill:'#06303A',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:-62,width:w,height:124,rx:62,fill:'none',stroke:AMB,'stroke-width':6},c);
 txt(c,s,0,size*0.36,size,'#FFFFFF','bold');return c;}
function headline(g,s,w,fs){w=w||560;fs=fs||50;const c=el('g',{},g);
 el('rect',{x:-w/2,y:-80,width:w,height:160,rx:22,fill:'url(#g_paper)',filter:'url(#g_sh)'},c);
 el('rect',{x:-w/2,y:-80,width:w,height:46,rx:22,fill:'#E4412C'},c);
 el('rect',{x:-w/2,y:-52,width:w,height:18,fill:'#E4412C'},c);
 txt(c,'ULTIM’ORA',0,-44,30,'#fff','bold');
 txt(c,s,0,46,fs,'#0B4A50','900');return c;}
function door(g){const d=el('g',{},g);
 // luce dietro la porta
 el('rect',{x:-190,y:-300,width:380,height:600,rx:14,fill:'#FFF3C4'},d);
 const rays=el('g',{opacity:.9},d);
 el('rect',{x:-190,y:-300,width:380,height:600,rx:14,fill:'url(#g_spot)'},rays);
 // stipite
 el('rect',{x:-216,y:-326,width:432,height:640,rx:22,fill:'none',stroke:'#0B4A50','stroke-width':26},d);
 el('rect',{x:-216,y:-326,width:432,height:640,rx:22,fill:'none',stroke:'#fff','stroke-opacity':.45,'stroke-width':4},d);
 return d;}
const SB=[];
// --- Scena 1: l'età sale ---
SB[0]={s:0,e:3.25,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PENSIONE 2027');
 o.cal=calendarPage(g,'ANNO','2027',150,'');
 o.gau=el('g',{},g);
 el('rect',{x:-70,y:-330,width:140,height:660,rx:70,fill:'#0A3F45',opacity:.8,stroke:LT,'stroke-width':5},o.gau);
 o.fill=el('rect',{x:-58,y:300,width:116,height:20,rx:58,fill:'url(#g_badge)'},o.gau);
 for(let i=0;i<6;i++)el('rect',{x:80,y:-300+i*115,width:36,height:6,rx:3,fill:'#fff',opacity:.7},o.gau);
 o.lab=txt(g,'ETÀ PENSIONABILE',0,0,64,'#fff','900');
 o.arr=el('g',{},g);el('path',{d:'M-90 60 L0 -70 L90 60 L38 60 L38 170 L-38 170 L-38 60 Z',fill:AMB,stroke:'#fff','stroke-width':8,'stroke-linejoin':'round',filter:'url(#g_sh2)'},o.arr);
 o.cap=el('g',{},g);cap(o.cap,"NEL 2027 L'ETÀ PER LA PENSIONE SALE!",58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 const p=eob(seg(t,0.1,0.9));T(o.cal.g,520,lerp(-700,220,p),t>0.9?6*Math.exp(-2.4*(t-0.9))*Math.sin(8*(t-0.9)):0,1.1);
 T(o.gau,1380,590,0,Math.max(0,eob(seg(t,0.4,1.0))));
 const f=eio(seg(t,0.9,3.0));o.fill.setAttribute('y',300-f*600);o.fill.setAttribute('height',20+f*600);
 o.lab.setAttribute('transform','translate(1380 175)');
 const a=eob(seg(t,0.9,1.5));T(o.arr,1690,lerp(820,430,eio(seg(t,0.9,3.0))),0,Math.max(0,a));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,1.5,2.1))));
 }};
// --- Scena 2: tutti parlano di 64 anni ---
SB[1]={s:3.25,e:8.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TUTTI NE PARLANO');
 o.h=[headline(g,'PENSIONE A 64 ANNI!',700,48),headline(g,'QUOTA 41!',520,70),headline(g,'STOP ALL’AUMENTO!',700,48)].map(x=>{const w=el('g',{},g);w.appendChild(x);return w;});
 o.q=el('g',{},g);qBubble(o.q,130);
 o.cap=el('g',{},g);cap(o.cap,"TUTTI PARLANO DI 64 ANNI... COM'È POSSIBILE?",56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 const pos=[[420,360,-6],[1500,330,5],[960,700,-2]];
 o.h.forEach((h,i)=>{const p=eob(seg(t,0.2+i*0.7,0.8+i*0.7));const w=t>0.8+i*0.7?3*Math.sin((t-i)*2.5):0;T(h,pos[i][0],pos[i][1],pos[i][2]+w*0.4,Math.max(0,p)*1.1);});
 const q=eob(seg(t,3.0,3.7));T(o.q,960,340,10*Math.sin(t*4),Math.max(0,q)*(1+0.06*Math.sin(t*6)));
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.6,1.2))));
 }};
// --- Scena 3: vecchiaia 67 anni e 1 mese ---
SB[2]={s:8.4,e:14.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PENSIONE DI VECCHIAIA');
 o.cal=calendarPage(g,'GENNAIO','1',320,'2027');
 o.pl=el('g',{},g);o.plate=plate(o.pl,'67','ANNI');
 o.dr=dotsRow(o.pl,12,225);
 o.chip=el('g',{},g);chip(o.chip,'+1 MESE',340);
 o.sp=ring(g,100);
 o.cap=el('g',{},g);cap(o.cap,'DAL 1° GENNAIO 2027: 67 ANNI E 1 MESE',58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 const p=eob(seg(t,0.1,0.9));T(o.cal.g,500,lerp(-700,200,p),t>0.9?5*Math.exp(-2.4*(t-0.9))*Math.sin(8*(t-0.9)):0,1.1);
 const pp=eob(seg(t,1.3,2.0));T(o.pl,1360,500,0,1.45*Math.max(0,pp));
 op(o.dr.g,seg(t,1.8,2.3));
 const pc=eob(seg(t,3.5,4.2));T(o.chip,lerp(1800,1660,eo3(seg(t,3.5,4.0))),lerp(100,265,pc),lerp(18,8,pc),Math.max(0,pc));
 if(t>4.0){lightDot(o.dr.a[0],true,seg(t,4.0,4.5));o.plate.s.textContent='ANNI E 1 MESE';o.plate.s.setAttribute('font-size',34);}
 const rr=seg(t,4.0,4.6);o.sp.setAttribute('r',lerp(30,200,rr));o.sp.setAttribute('opacity',t>4.0?(1-rr)*0.8:0);T(o.sp,1660,275,0,1);
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.8,1.4))));
 }};
// --- Scena 4: a 64 anni esiste GIA' ---
SB[3]={s:14.4,e:18.8,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA SORPRESA');
 o.door=el('g',{},g);door(o.door);
 o.leaf=el('g',{},g);
 el('rect',{x:0,y:-300,width:380,height:600,rx:12,fill:'#0B4A50'},o.leaf);
 el('rect',{x:30,y:-262,width:140,height:240,rx:10,fill:'none',stroke:'#2FBF9B','stroke-width':6},o.leaf);
 el('rect',{x:210,y:-262,width:140,height:240,rx:10,fill:'none',stroke:'#2FBF9B','stroke-width':6},o.leaf);
 el('circle',{cx:340,cy:20,r:16,fill:AMB},o.leaf);
 o.sign=el('g',{},g);
 el('rect',{x:-190,y:-80,width:380,height:160,rx:26,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.sign);
 txt(o.sign,'64',-75,46,112,'#fff','900');txt(o.sign,'ANNI',88,34,44,'#fff','900');
 o.ch=el('g',{},g);checkBadge(o.ch,90);
 o.m1=el('g',{},g);medal(o.m1,false);o.m2=el('g',{},g);medal(o.m2,true);
 o.st=el('g',{},g);
 el('rect',{x:-300,y:-70,width:600,height:140,rx:18,fill:'none',stroke:'#2FBF9B','stroke-width':14},o.st);
 txt(o.st,'ESISTE GIÀ!',0,34,92,'#2FBF9B','900');
 o.sp=ring(g,100);
 o.cap=el('g',{},g);cap(o.cap,'PER ALCUNI, LA PENSIONE A 64 ANNI ESISTE GIÀ!',56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.door,640,590,0,Math.max(0,eob(seg(t,0.1,0.8))));
 const sg=eob(seg(t,0.4,1.1));T(o.sign,640,200,0,Math.max(0,sg));
 // anta che si apre (prospettiva con scaleX)
 const open=eio(seg(t,1.0,2.0));const sx=lerp(1,0.18,open);
 o.leaf.setAttribute('transform','translate('+(640-190)+' 590) scale('+Math.max(0.05,sx)+' 1)');op(o.leaf,seg(t,0.1,0.5));
 const c=eob(seg(t,2.0,2.6));T(o.ch,880,330,0,Math.max(0,c));
 T(o.m1,1290,320,0,0.8*Math.max(0,eob(seg(t,1.6,2.2))));T(o.m2,1590,320,0,0.8*Math.max(0,eob(seg(t,1.9,2.5))));
 const s=eob(seg(t,2.3,3.0));T(o.st,1440,680,-8,Math.max(0,s)*(t>3.0?1+0.03*Math.sin((t-3.0)*7):1));
 const rr=seg(t,2.3,3.0);o.sp.setAttribute('r',lerp(60,420,rr));o.sp.setAttribute('opacity',t>2.3?(1-rr)*0.7:0);T(o.sp,1440,680,0,1);
 T(o.cap,960,950,0,Math.max(0,eob(seg(t,0.3,0.9))));
 }};

// ===== regia =====
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
 const z=1+0.02*(t/18.8);camG.setAttribute('transform','translate(960 540) scale('+z+') translate(-960 -540)');
}
function draw(i,t){drawBlock(t);}
