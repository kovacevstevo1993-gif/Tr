// ===== V3 BLOCCO 5 (405 fotogrammi = 13,50 s): la percentuale ufficiale non esiste ancora =====
const SB=[];const TOT=405/30;
SB[0]={s:0,e:4.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'UNA COSA IMPORTANTE');
 o.w=el('g',{},g);warn(o.w);
 o.big=el('g',{},g);bigNum(o.big,'2027 : ? %',150,'url(#g_paper)','LA PERCENTUALE UFFICIALE','#E4412C');
 o.tg=el('g',{},g);tag(o.tg,'NON ESISTE ANCORA',620,RED_,'#fff',50);
 o.cap=el('g',{},g);cap(o.cap,'LA PERCENTUALE UFFICIALE DEL DUEMILAVENTISETTE NON ESISTE ANCORA',46);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.w,330,430,0,0.85*pop(t,0.2,0.8));
 T(o.big,1210,420,0,pop(t,0.9,1.6));
 T(o.tg,1210,760,0,pop(t,2.0,2.6));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:4.4,e:9.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ARRIVA A NOVEMBRE');
 o.cal=el('g',{},g);calendarPage(o.cal,'NOVEMBRE','DECRETO',78,'DEI MINISTERI');
 o.doc=el('g',{},g);docCard(o.doc,'DECRETO',420,360,GRN,40);
 o.l=[0,1,2].map(i=>{const r=el('rect',{x:-150,y:-70+i*50,width:i%2?200:300,height:16,rx:8,fill:'#C3D3D7'});o.doc.appendChild(r);return r;});
 o.st=el('g',{},g);stamp(o.st,'IL % VERO',460,GRN,50);
 o.cap=el('g',{},g);cap(o.cap,'ARRIVA CON UN DECRETO, A NOVEMBRE',52);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.cal,560,190,0,0.95*pop(t,0.2,0.9));
 T(o.doc,1320,430,0,pop(t,1.2,1.9));
 T(o.st,1320,730,-4,pop(t,2.4,3.0));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[2]={s:9.0,e:13.5,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL METODO È GIÀ GIUSTO');
 o.e1=el('g',{},g);bigNum(o.e1,'3 %',170,'url(#g_paper)','ESEMPIO',GRN);
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.ck=el('g',{},g);checkBadge(o.ck,150);
 o.tg=el('g',{},g);tag(o.tg,'ESEMPI, NUMERI TONDI',640,AMB,'#5A3300',36);
 o.tg2=el('g',{},g);tag(o.tg2,'IL METODO È GIÀ GIUSTO',640,'url(#g_badge)','#fff',36);
 o.cap=el('g',{},g);cap(o.cap,'OGNI CIFRA È UN ESEMPIO, CON NUMERI TONDI. MA IL METODO È GIÀ QUELLO GIUSTO!',40);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.e1,480,400,0,pop(t,0.3,1.0));
 T(o.tg,480,700,0,pop(t,1.2,1.8));
 T(o.ar,960,400,0,0.85*pop(t,1.8,2.3));
 T(o.ck,1430,400,0,pop(t,2.3,3.0));
 T(o.tg2,1430,700,0,pop(t,3.0,3.6));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
