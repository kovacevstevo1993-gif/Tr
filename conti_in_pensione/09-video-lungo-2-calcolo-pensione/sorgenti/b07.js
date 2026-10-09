// ===== BLOCCO 7 (262 fotogrammi = 8,73 s): quale vale per te? la data del 31/12/1995 / tre porte =====
const SB=[];const TOT=262/30;
SB[0]={s:0,e:5.3,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'QUALE VALE PER TE?');
 o.q=el('g',{},g);qBubble(o.q,130);
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.cal=calendarPage(g,'DICEMBRE','31',270,'1995');
 o.tg=el('g',{},g);tag(o.tg,'UNA DATA CHE DECIDE',720,AMB,'#5A3300',46);
 o.cap=el('g',{},g);cap(o.cap,'DIPENDE DA UNA DATA: 31 DICEMBRE 1995',56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.q,440,480,8*Math.sin(t*4),pop(t,0.2,0.8)*(t>0.8?1+0.05*Math.sin(t*6):1));
 T(o.ar,780,480,0,0.9*pop(t,1.2,1.7));
 T(o.cal.g,1150,190,0,pop(t,1.4,2.0));
 T(o.tg,440,720,0,pop(t,2.4,3.0));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:5.3,e:8.73,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TRE CASI, TRE PORTE');
 o.d=[1,2,3].map(i=>{const d=el('g',{},g);doorN(d,i,['url(#g_red)','url(#g_badge)','url(#g_head)'][i-1]);return d;});
 o.cap=el('g',{},g);cap(o.cap,'TRE CASI, TRE PORTE. SCEGLI LA TUA!',56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 o.d.forEach((d,i)=>T(d,[460,960,1460][i],560,0,0.62*pop(t,0.2+i*0.4,0.7+i*0.4)));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
