// ===== BLOCCO 5 (305 fotogrammi = 10,17 s): errore comune, i tre sistemi =====
const SB=[];const TOT=305/30;
function equation(g){const o={};
 o.b1=el('g',{},g);el('rect',{x:-210,y:-90,width:420,height:180,rx:30,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.b1);txt(o.b1,'ULTIMO',0,-8,52,INK,'900');txt(o.b1,'STIPENDIO',0,52,46,GRN,'bold');
 o.op=tag(g,'× %',190,'#0B4A50','#fff',54);
 o.eq=el('g',{},g);el('circle',{r:56,fill:'#fff',stroke:AMB,'stroke-width':8},o.eq);txt(o.eq,'=',0,24,76,INK,'900');
 o.b2=el('g',{},g);el('rect',{x:-210,y:-90,width:420,height:180,rx:30,fill:'url(#g_badge)',filter:'url(#g_sh)'},o.b2);txt(o.b2,'PENSIONE',0,24,62,'#fff','900');
 return o;}
function placeEq(o,y,k,a){T(o.b1,340,y,0,k*a);T(o.op,700,y,0,k*a);T(o.eq,880,y,0,k*a);T(o.b2,1180,y,0,k*a);}
SB[0]={s:0,e:6.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,"L'ERRORE PIÙ COMUNE");
 o.w=el('g',{},g);warn(o.w);
 o.q=equation(g);
 o.tg=el('g',{},g);tag(o.tg,'LO FANNO QUASI TUTTI',720,RED_,'#fff',48);
 o.cap=el('g',{},g);cap(o.cap,"PENSARE CHE LA PENSIONE SIA UN % DELL'ULTIMO STIPENDIO",44);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.w,1620,520,6,0.8*pop(t,0.2,0.8));
 T(o.tg,960,300,0,pop(t,0.7,1.2));
 const a=[pop(t,1.8,2.3),pop(t,2.1,2.6),pop(t,2.4,2.9),pop(t,2.7,3.2)];
 T(o.q.b1,340,560,0,a[0]);T(o.q.op,700,560,0,a[1]);T(o.q.eq,880,560,0,a[2]);T(o.q.b2,1180,560,0,a[3]);
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:6.0,e:10.17,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'NON È COSÌ');
 o.q=equation(g);
 o.x=el('g',{},g);el('path',{d:'M-300 -120 L300 120 M300 -120 L-300 120',stroke:RED_,'stroke-width':34,'stroke-linecap':'round',opacity:.92},o.x);
 o.st=el('g',{},g);stamp(o.st,'NON SEMPRE',460,RED_,50);
 o.c=[['1','RETRIBUTIVO','url(#g_red)'],['2','CONTRIBUTIVO','url(#g_badge)'],['3','MISTO','url(#g_head)']].map(d=>{const c=el('g',{},g);circN(c,70,d[0],d[2]);
  el('rect',{x:-190,y:96,width:380,height:68,rx:34,fill:'#fff'},c);txt(c,d[1],0,142,38,INK,'bold');return c;});
 o.cap=el('g',{},g);cap(o.cap,'DIPENDE DAL SISTEMA DI CALCOLO: CE NE SONO TRE',48);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.q.b1,340,310,0,0.55);T(o.q.op,700,310,0,0.55);T(o.q.eq,880,310,0,0.55);T(o.q.b2,1180,310,0,0.55);
 T(o.x,760,310,0,0.58*pop(t,0.3,0.8));
 T(o.st,1610,310,5,t>0.5?lerp(1.2,1,eo3(seg(t,0.5,0.9))):0);op(o.st,clamp(seg(t,0.5,0.8)*2));
 o.c.forEach((c,i)=>T(c,[460,960,1460][i],620,0,pop(t,1.6+i*0.4,2.1+i*0.4)));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
