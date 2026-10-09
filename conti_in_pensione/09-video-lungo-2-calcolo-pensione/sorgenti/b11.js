// ===== BLOCCO 11 (405 fotogrammi = 13,50 s): hai scelto la tua porta? / in tutte e tre compare il contributivo / serve a tutti =====
const SB=[];const TOT=405/30;
const DC=['url(#g_red)','url(#g_badge)','url(#g_head)'];
SB[0]={s:0,e:7.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'HAI SCELTO LA TUA PORTA?');
 o.d=[1,2,3].map(i=>{const d=el('g',{},g);doorN(d,i,DC[i-1]);return d;});
 o.q=el('g',{},g);qBubble(o.q,80);
 o.t1=el('g',{},g);tag(o.t1,'PIÙ AVANTI TI MOSTRO DOVE SI SCOPRE',1060,AMB,'#5A3300',44);
 o.t2=el('g',{},g);tag(o.t2,'IN 2 MINUTI',380,'#0B4A50','#fff',44);
 o.cap=el('g',{},g);cap(o.cap,'SE NON SEI SICURO, NIENTE PAURA',58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 o.d.forEach((d,i)=>T(d,[460,960,1460][i],570,0,0.62*pop(t,0.2+i*0.3,0.7+i*0.3)));
 T(o.q,960,215,8*Math.sin(t*4),pop(t,1.0,1.5));
 T(o.t1,960,820,0,pop(t,2.4,3.0));
 T(o.t2,1560,215,0,pop(t,3.6,4.1));
 T(o.cap,960,950,0,pop(t,1.6,2.2));
 }};
SB[1]={s:7.2,e:11.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IN TUTTE E TRE LE PORTE');
 o.d=[1,2,3].map(i=>{const d=el('g',{},g);doorN(d,i,DC[i-1]);return d;});
 o.t=[0,1,2].map(i=>{const t=el('g',{},g);tag(t,'CONTRIBUTIVO',360,MINT,'#07302A',40);return t;});
 o.cap=el('g',{},g);cap(o.cap,'IN TUTTE E TRE LE PORTE COMPARE IL CONTRIBUTIVO',50);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 o.d.forEach((d,i)=>T(d,[460,960,1460][i],520,0,0.62));
 o.t.forEach((x,i)=>T(x,[460,960,1460][i],790,0,pop(t,0.3+i*0.5,0.8+i*0.5)));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[2]={s:11.0,e:13.5,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'CAPIRLO SERVE A TUTTI');
 o.m1=el('g',{},g);medal(o.m1,false);o.m2=el('g',{},g);medal(o.m2,true);
 o.ch=el('g',{},g);checkBadge(o.ch,100);
 o.tg=el('g',{},g);tag(o.tg,'SERVE A TUTTI',560,AMB,'#5A3300',52);
 o.cap=el('g',{},g);cap(o.cap,'QUINDI CAPIRLO SERVE A TUTTI!',58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.m1,560,470,0,0.8*pop(t,0.1,0.5));T(o.m2,1360,470,0,0.8*pop(t,0.2,0.6));
 T(o.ch,960,470,0,pop(t,0.4,0.9));
 T(o.tg,960,740,0,pop(t,0.8,1.3));
 T(o.cap,960,950,0,pop(t,0.1,0.6));
 }};
