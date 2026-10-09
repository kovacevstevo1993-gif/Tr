// ===== BLOCCO 17 (369 fotogrammi = 12,30 s): montante x coefficiente = pensione di un anno; cambia con l'eta'; Ministero del Lavoro ogni 2 anni =====
const SB=[];const TOT=369/30;
SB[0]={s:0,e:5.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'COME FUNZIONA');
 function bx(label,sub,w,fill,col){const c=el('g',{},g);el('rect',{x:-w/2,y:-95,width:w,height:190,rx:30,fill:fill,filter:'url(#g_sh)'},c);txt(c,label,0,0,50,col,'900');txt(c,sub,0,56,32,col==='#fff'?'#D6F5EC':GRN,'bold');return c;}
 o.a=bx('MONTANTE','IL SALVADANAIO',460,'url(#g_paper)',INK);
 o.x=el('g',{},g);el('circle',{r:46,fill:'#0B4A50',stroke:'#fff','stroke-width':6},o.x);txt(o.x,'×',0,22,64,'#fff','900');
 o.b=bx('COEFFICIENTE','PER ETÀ',480,'url(#g_head)','#fff');
 o.e=el('g',{},g);el('circle',{r:50,fill:'#fff',stroke:AMB,'stroke-width':8},o.e);txt(o.e,'=',0,22,70,INK,'900');
 o.r=bx('PENSIONE','DI UN ANNO',460,'url(#g_badge)','#fff');
 o.cap=el('g',{},g);cap(o.cap,'MONTANTE × COEFFICIENTE = PENSIONE DI UN ANNO',50);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.a,260,500,0,0.78*pop(t,0.2,0.7));T(o.x,520,500,0,pop(t,0.7,1.1));T(o.b,780,500,0,0.78*pop(t,1.0,1.5));
 T(o.e,1090,500,0,pop(t,1.6,2.0));T(o.r,1430,500,0,0.78*pop(t,2.0,2.6));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:5.2,e:9.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,"CAMBIA CON L'ETÀ");
 o.bs=bars(g,8);
 o.lab=[];for(let i=0;i<8;i++)o.lab.push(txt(g,String(60+i),0,0,34,'#fff','bold'));
 o.tg=el('g',{},g);tag(o.tg,"PIÙ ASPETTI, PIÙ SALE",640,MINT,'#07302A',46);
 o.cap=el('g',{},g);cap(o.cap,"IL COEFFICIENTE CAMBIA CON L'ETÀ IN CUI VAI IN PENSIONE",46);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.bs.g,960,700,0,1);
 for(let i=0;i<8;i++){setBar(o.bs,i,eo3(seg(t,0.1+i*0.1,0.6+i*0.1)),MINT);T(o.lab[i],960+o.bs.r[i].x,675,0,1);}
 T(o.tg,960,225,0,pop(t,1.4,2.0));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[2]={s:9.0,e:12.3,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'MINISTERO DEL LAVORO');
 o.b=el('g',{},g);
 el('path',{d:'M-220 -90 L0 -190 L220 -90Z',fill:'#0B4A50',stroke:'#fff','stroke-width':6,'stroke-linejoin':'round'},o.b);
 [-150,-50,50,150].forEach(x=>el('rect',{x:x-26,y:-70,width:52,height:170,rx:8,fill:'url(#g_paper)',stroke:'#C3D3D7','stroke-width':3},o.b));
 el('rect',{x:-240,y:100,width:480,height:36,rx:10,fill:'#0B4A50'},o.b);
 o.cal=calendarPage(g,'OGNI','2',250,'ANNI');
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.tg=el('g',{},g);tag(o.tg,'LO AGGIORNA OGNI DUE ANNI',760,AMB,'#5A3300',46);
 o.cap=el('g',{},g);cap(o.cap,'IL MINISTERO DEL LAVORO LO AGGIORNA OGNI DUE ANNI',50);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.b,520,500,0,0.95*pop(t,0.2,0.8));
 T(o.ar,880,500,0,0.9*pop(t,0.8,1.3));
 T(o.cal.g,1300,190,0,pop(t,1.1,1.7));
 T(o.tg,520,740,0,pop(t,1.8,2.4));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
