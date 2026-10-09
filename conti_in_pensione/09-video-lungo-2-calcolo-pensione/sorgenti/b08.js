// ===== BLOCCO 8 (310 fotogrammi = 10,33 s): porta numero uno =====
const SB=[];const TOT=310/30;
SB[0]={s:0,e:6.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PORTA NUMERO UNO');
 o.d=el('g',{},g);doorN(o.d,1,'url(#g_red)');
 o.cal=calendarPage(g,'GENNAIO','1',320,'1996');
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.tg=el('g',{},g);tag(o.tg,'IN POI',250,AMB,'#5A3300',50);
 o.cap=el('g',{},g);cap(o.cap,'HAI INIZIATO A VERSARE DAL 1° GENNAIO 1996 IN POI',48);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.d,470,560,0,0.8*pop(t,0.2,0.8));
 T(o.cal.g,1050,210,0,0.9*pop(t,1.4,2.0));
 T(o.ar,1420,540,0,0.9*pop(t,2.4,2.9));
 T(o.tg,1670,540,0,pop(t,3.0,3.5));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:6.0,e:10.33,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'SOLO CONTRIBUTIVO');
 o.bs=bars(g,10);
 o.tg=el('g',{},g);tag(o.tg,'SISTEMA CONTRIBUTIVO',640,MINT,'#07302A',46);
 o.t2=el('g',{},g);tag(o.t2,'PER TUTTA LA CARRIERA',640,'#0B4A50','#fff',40);
 o.cap=el('g',{},g);cap(o.cap,'PER TE VALE SOLO IL SISTEMA CONTRIBUTIVO',52);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.bs.g,960,700,0,1);
 for(let i=0;i<10;i++){setBar(o.bs,i,eo3(seg(t,0.1+i*0.05,0.5+i*0.05)),t>0.6+i*0.1?MINT:DIM);}
 T(o.tg,960,225,0,pop(t,0.4,1.0));
 T(o.t2,960,825,0,pop(t,1.8,2.4));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
