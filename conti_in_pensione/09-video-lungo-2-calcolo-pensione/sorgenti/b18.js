// ===== BLOCCO 18 (397 fotogrammi = 13,23 s): 2025-2026, 67 anni -> 5,608%, 462.000 x 5,608% =====
const SB=[];const TOT=397/30;
SB[0]={s:0,e:6.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PENSIONE NEL 2025 E 2026');
 o.c1=calendarPage(g,'ANNO','2025',150,'');o.c2=calendarPage(g,'ANNO','2026',150,'');
 o.plate=el('g',{},g);plate(o.plate,'67','ANNI');
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.k=el('g',{},g);el('rect',{x:-290,y:-120,width:580,height:240,rx:36,fill:'url(#g_badge)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},o.k);
 txt(o.k,'5,608%',0,34,120,'#fff','900');txt(o.k,'COEFFICIENTE',0,-66,34,'#D6F5EC','bold');
 o.cap=el('g',{},g);cap(o.cap,'A 67 ANNI IL COEFFICIENTE È 5,608%',56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.c1.g,190,lerp(-700,210,eo3(seg(t,0.2,0.9))),0,0.7);T(o.c2.g,560,lerp(-700,210,eo3(seg(t,0.5,1.2))),0,0.7);
 T(o.plate,980,520,0,0.9*pop(t,1.6,2.2));
 T(o.ar,1290,520,0,0.8*pop(t,2.4,2.9));
 T(o.k,1660,520,0,0.8*pop(t,2.7,3.3));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:6.2,e:13.23,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL CONTO');
 function bx(label,sub,w,fill,col,fs){const c=el('g',{},g);el('rect',{x:-w/2,y:-100,width:w,height:200,rx:32,fill:fill,filter:'url(#g_sh)'},c);txt(c,label,0,18,fs,col,'900');txt(c,sub,0,-48,30,col==='#fff'?'#D6F5EC':GRN,'bold');return c;}
 o.a=bx('462.000 €','MONTANTE',560,'url(#g_paper)',INK,76);
 o.x=el('g',{},g);el('circle',{r:46,fill:'#0B4A50',stroke:'#fff','stroke-width':6},o.x);txt(o.x,'×',0,22,64,'#fff','900');
 o.b=bx('5,608%','COEFFICIENTE A 67 ANNI',560,'url(#g_head)','#fff',84);
 o.e=el('g',{},g);el('circle',{r:50,fill:'#fff',stroke:AMB,'stroke-width':8},o.e);txt(o.e,'=',0,22,70,INK,'900');
 o.q=el('g',{},g);qBubble(o.q,110);
 o.tg=el('g',{},g);tag(o.tg,'QUANTO FA?',420,AMB,'#5A3300',52);
 o.cap=el('g',{},g);cap(o.cap,'462.000 € PER 5,608%...',58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.a,360,470,0,0.85*pop(t,0.2,0.8));T(o.x,720,470,0,pop(t,0.7,1.2));T(o.b,1080,470,0,0.85*pop(t,1.0,1.6));
 T(o.e,1420,470,0,pop(t,1.8,2.3));T(o.q,1640,470,8*Math.sin(t*4),pop(t,2.2,2.8)*(t>2.8?1+0.05*Math.sin(t*6):1));
 T(o.tg,960,720,0,pop(t,3.2,3.8));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
