// ===== BLOCCO 19 (399 fotogrammi = 13,30 s): 25.909 euro l'anno, diviso 13 = 1.993 lordi al mese, pensione di Bruno =====
const SB=[];const TOT=399/30;
SB[0]={s:0,e:4.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,"FA CIRCA 25.909 € L'ANNO");
 o.r=el('g',{},g);el('rect',{x:-520,y:-170,width:1040,height:340,rx:48,fill:'url(#g_badge)',stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},o.r);
 txt(o.r,'≈ 25.909 €',0,40,120,'#fff','900');txt(o.r,"LA PENSIONE DI UN ANNO",0,-92,38,'#D6F5EC','bold');
  o.cap=el('g',{},g);cap(o.cap,"...FA CIRCA 25.909 EURO L'ANNO!",58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.r,960,440,0,pop(t,0.2,0.9));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:4.4,e:9.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'13 MENSILITÀ');
 o.r=el('g',{},g);el('rect',{x:-260,y:-100,width:520,height:200,rx:34,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.r);txt(o.r,'25.909 €',0,24,92,INK,'900');
 o.d=el('g',{},g);el('circle',{r:56,fill:'#0B4A50',stroke:'#fff','stroke-width':6},o.d);txt(o.d,'÷',0,24,76,'#fff','900');
 o.n=el('g',{},g);el('circle',{r:100,fill:'url(#g_head)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh2)'},o.n);txt(o.n,'13',0,34,100,'#fff','900');
 o.dr=dotsRow(g,13,0);
 o.tg=el('g',{},g);tag(o.tg,'MENSILITÀ',380,AMB,'#5A3300',46);
 o.cap=el('g',{},g);cap(o.cap,'DIVISI PER TREDICI MENSILITÀ',58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.r,420,430,0,pop(t,0.2,0.8));T(o.d,820,430,0,pop(t,0.7,1.1));T(o.n,1130,430,0,pop(t,1.0,1.6));
 T(o.dr.g,960,640,0,1.8*seg(t,1.5,1.8));op(o.dr.g,seg(t,1.5,1.8));
 const nd=Math.floor(clamp((t-1.8)/0.12,0,13));o.dr.a.forEach((d,i)=>lightDot(d,i<nd,0.5));
 T(o.tg,1130,590,0,pop(t,3.4,3.9));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[2]={s:9.0,e:13.3,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA PENSIONE DI BRUNO');
 o.a=el('g',{},g);medal(o.a,false);
 o.n=el('g',{},g);tag(o.n,'BRUNO · 67 ANNI',480,'url(#g_badge)','#fff',44);
 o.r=el('g',{},g);el('rect',{x:-380,y:-170,width:760,height:340,rx:48,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.r);
 txt(o.r,'1.993 €',0,50,120,INK,'900');txt(o.r,'AL MESE',0,-90,40,GRN,'bold');
 o.l=el('g',{},g);tag(o.l,'LORDI · NEL NOSTRO ESEMPIO',760,AMB,'#5A3300',42);
 o.cap=el('g',{},g);cap(o.cap,'ECCO LA PENSIONE DI BRUNO A 67 ANNI',56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.a,360,440,0,0.8*pop(t,0.2,0.8));T(o.n,360,680,0,pop(t,0.6,1.1));
 T(o.r,1230,440,0,pop(t,1.0,1.7));
 T(o.l,1230,690,0,pop(t,1.8,2.4));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
