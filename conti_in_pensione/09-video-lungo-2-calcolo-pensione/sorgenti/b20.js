// ===== BLOCCO 20 (341 fotogrammi = 11,37 s): lordo / netto, Irpef =====
const SB=[];const TOT=341/30;
SB[0]={s:0,e:4.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ATTENZIONE: LORDI');
 o.w=el('g',{},g);warn(o.w);
 o.r=el('g',{},g);el('rect',{x:-300,y:-120,width:600,height:240,rx:36,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.r);txt(o.r,'1.993 €',0,34,110,INK,'900');txt(o.r,'LORDI',0,-66,40,RED_,'bold');
 o.tg=el('g',{},g);tag(o.tg,'PRIMA DELLE TASSE',560,RED_,'#fff',46);
 o.cap=el('g',{},g);cap(o.cap,'SONO EURO LORDI, CIOÈ PRIMA DELLE TASSE',54);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.w,520,480,0,0.8*pop(t,0.2,0.8));
 T(o.r,1330,470,0,pop(t,0.8,1.4));
 T(o.tg,1330,700,0,pop(t,1.5,2.1));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:4.0,e:8.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'SUL CONTO ARRIVA IL NETTO');
 o.a=el('g',{},g);el('rect',{x:-260,y:-110,width:520,height:220,rx:34,fill:'url(#g_paper)',filter:'url(#g_sh)'},o.a);txt(o.a,'LORDO',0,-40,40,RED_,'bold');txt(o.a,'1.993 €',0,50,90,INK,'900');
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.t=el('g',{},g);tag(o.t,'IRPEF',280,'#0B4A50','#fff',46);
 o.b=el('g',{},g);el('rect',{x:-260,y:-110,width:520,height:220,rx:34,fill:'url(#g_badge)',filter:'url(#g_sh)'},o.b);txt(o.b,'NETTO',0,-40,40,'#D6F5EC','bold');txt(o.b,'PIÙ BASSO',0,50,76,'#fff','900');
 o.cap=el('g',{},g);cap(o.cap,"SUL CONTO ARRIVA IL NETTO: DIPENDE DALL'IRPEF",50);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.a,380,480,0,pop(t,0.2,0.8));T(o.ar,820,480,0,0.9*pop(t,0.7,1.2));T(o.t,820,360,0,pop(t,1.0,1.5));T(o.b,1280,480,0,pop(t,1.2,1.8));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[2]={s:8.0,e:11.37,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'SUL CEDOLINO');
 o.d=el('g',{},g);docCard(o.d,'CEDOLINO',620,430,GRN,44);
 [-70,-10,50,110].forEach((y,i)=>el('rect',{x:-250,y:y,width:i%2?300:420,height:14,rx:7,fill:'#C3D3D7'},o.d));
 o.tg=el('g',{},g);tag(o.tg,'LA CIFRA È PIÙ BASSA',620,AMB,'#5A3300',48);
 o.ar=el('g',{},g);arrowDown(o.ar,RED_);
 o.s=el('g',{},g);tag(o.s,'TASSE · SITUAZIONE PERSONALE',860,'#0B4A50','#fff',40);
 o.cap=el('g',{},g);cap(o.cap,'PER QUESTO LA CIFRA SUL CEDOLINO È PIÙ BASSA',50);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.d,560,490,-2,pop(t,0.2,0.8));
 T(o.ar,1230,380,0,0.9*pop(t,0.9,1.4));
 T(o.tg,1230,540,0,pop(t,1.3,1.9));
 T(o.s,1230,650,0,pop(t,1.7,2.3));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
