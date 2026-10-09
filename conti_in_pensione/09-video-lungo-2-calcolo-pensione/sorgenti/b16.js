// ===== BLOCCO 16 (329 fotogrammi = 10,97 s): il salvadanaio non diventa pensione da solo / coefficiente di trasformazione =====
const SB=[];const TOT=329/30;
SB[0]={s:0,e:4.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'BENE, MA NON BASTA');
 o.p=el('g',{},g);piggy(o.p);
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.q=el('g',{},g);el('rect',{x:-190,y:-120,width:380,height:240,rx:34,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.q);txt(o.q,'PENSIONE?',0,18,46,INK,'900');
 o.x=el('g',{},g);el('path',{d:'M-60 -60 L60 60 M60 -60 L-60 60',stroke:RED_,'stroke-width':22,'stroke-linecap':'round'},o.x);
 o.tg=el('g',{},g);tag(o.tg,'NON DIVENTA PENSIONE DA SOLO',900,RED_,'#fff',44);
 o.cap=el('g',{},g);cap(o.cap,'IL SALVADANAIO NON DIVENTA PENSIONE DA SOLO',52);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.p,520,500,0,0.9*pop(t,0.2,0.8));
 T(o.ar,930,500,0,0.9*pop(t,0.8,1.3));
 T(o.q,1400,500,0,pop(t,1.1,1.7));T(o.x,1400,500,0,pop(t,1.8,2.2));
 T(o.tg,960,760,0,pop(t,2.2,2.8));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:4.2,e:7.7,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'UN ULTIMO PASSAGGIO');
 o.s=[0,1,2].map(i=>{const s=el('g',{},g);el('rect',{x:-190,y:-60,width:380,height:120,rx:20,fill:i==2?'url(#g_badge)':'url(#g_paper)',filter:'url(#g_sh2)'},s);txt(s,['MONTANTE','PASSAGGIO','PENSIONE'][i],0,14,40,i==2?'#fff':INK,'900');return s;});
 o.ar=[0,1].map(i=>{const a=el('g',{},g);arrowRight(a,AMB);return a;});
 o.tg=el('g',{},g);tag(o.tg,'ULTIMO PASSAGGIO',620,AMB,'#5A3300',50);
 o.cap=el('g',{},g);cap(o.cap,'SERVE UN ULTIMO PASSAGGIO...',58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 o.s.forEach((s,i)=>T(s,[400,960,1520][i],lerp(520,520,0),0,pop(t,0.2+i*0.3,0.7+i*0.3)*(i==1?1.15:1)));
 o.ar.forEach((a,i)=>T(a,[690,1230][i],520,0,0.8*pop(t,0.6+i*0.3,1.0+i*0.3)));
 T(o.tg,960,720,0,pop(t,1.6,2.2));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[2]={s:7.7,e:10.97,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'NESSUNO LO GUARDA');
 o.card=el('g',{},g);docCard(o.card,'COEFFICIENTE DI TRASFORMAZIONE',1100,420,'#0B4A50',42);
 txt(o.card,'%',0,70,160,AMB2,'900');
 [-90,-40].forEach(y=>el('rect',{x:-480,y:y+20,width:240,height:14,rx:7,fill:'#C3D3D7'},o.card));
 o.mag=el('g',{},g);magnifier(o.mag);
 o.tg=el('g',{},g);tag(o.tg,'QUASI NESSUNO LO GUARDA',720,AMB,'#5A3300',46);
 o.cap=el('g',{},g);cap(o.cap,'SI CHIAMA COEFFICIENTE DI TRASFORMAZIONE',52);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.card,960,470,0,pop(t,0.2,0.8));
 T(o.mag,lerp(1500,1300,eo3(seg(t,1.0,1.7))),lerp(300,520,eo3(seg(t,1.0,1.7))),0,pop(t,0.9,1.4));
 T(o.tg,960,770,0,pop(t,1.8,2.4));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
