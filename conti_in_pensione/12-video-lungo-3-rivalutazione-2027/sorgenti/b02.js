// ===== V3 BLOCCO 2 (416 fotogrammi = 13,87 s): 2026 contro 2027 =====
const SB=[];const TOT=416/30;
SB[0]={s:0,e:5.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'RIVALUTAZIONE 2026');
 o.cal=el('g',{},g);calendarPage(o.cal,'GENNAIO','2026',150,'RIVALUTAZIONE');
 o.big=el('g',{},g);bigNum(o.big,'1,4 %',210,'url(#g_badge)','LA RIVALUTAZIONE DEL 2026','#fff');
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.cap=el('g',{},g);cap(o.cap,'NEL DUEMILAVENTISEI LA RIVALUTAZIONE È STATA UNO VIRGOLA QUATTRO PER CENTO',44);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.cal,480,190,0,0.95*pop(t,0.2,0.9));
 T(o.ar,880,450,0,0.8*pop(t,1.2,1.8));
 T(o.big,1330,430,0,pop(t,1.8,2.6));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:5.0,e:9.6,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'RIVALUTAZIONE 2027');
 o.cal=el('g',{},g);calendarPage(o.cal,'GENNAIO','2027',150,'STIME');
 o.a=el('g',{},g);bigNum(o.a,'1,4 %',120,'#0B4A50','2026','#7FF0D2');
 o.b=el('g',{},g);bigNum(o.b,'≈ 2 ×',170,'url(#g_red)','2027: QUASI IL DOPPIO','#fff');
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.tg=el('g',{},g);tag(o.tg,'STIMA, NON UFFICIALE',620,AMB,'#5A3300',44);
 o.cap=el('g',{},g);cap(o.cap,'PER IL DUEMILAVENTISETTE LE STIME PARLANO DI QUASI IL DOPPIO!',46);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.cal,230,190,0,0.85*pop(t,0.2,0.8));
 T(o.a,720,430,0,pop(t,0.8,1.4));
 T(o.ar,1020,430,0,0.6*pop(t,1.3,1.8));
 T(o.b,1450,430,0,pop(t,1.8,2.5));
 T(o.tg,1200,760,0,pop(t,2.8,3.4));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[2]={s:9.6,e:13.87,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ATTENZIONE');
 o.w=el('g',{},g);warn(o.w);
 o.p=[0,1,2].map(i=>{const c=el('g',{},g);payslip(c,'PENSIONE','+ ? €');return c;});
 o.tg=el('g',{},g);tag(o.tg,'NON ARRIVA UGUALE A TUTTI',900,RED_,'#fff',50);
 o.cap=el('g',{},g);cap(o.cap,'QUELLA PERCENTUALE NON ARRIVA UGUALE A TUTTI, E IL PERCHÉ CAMBIA I TUOI CONTI',40);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.w,380,420,0,0.75*pop(t,0.2,0.8));
 o.p.forEach((c,i)=>T(c,[820,1190,1560][i],440,[-4,0,4][i],0.9*pop(t,0.8+i*0.5,1.4+i*0.5)));
 T(o.tg,1190,760,0,pop(t,2.5,3.0));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
