// ===== BLOCCO 14 (381 fotogrammi = 12,70 s): Bruno guadagna 35.000, il 33% fa 11.550 =====
const SB=[];const TOT=381/30;
SB[0]={s:0,e:5.2,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'FACCIAMO UN ESEMPIO');
 o.a=el('g',{},g);medal(o.a,false);
 o.n=el('g',{},g);tag(o.n,'BRUNO',300,'url(#g_badge)','#fff',48);
 o.c=el('g',{},g);docCard(o.c,'BUSTA PAGA',620,430,GRN,42);
 txt(o.c,'35.000 €',0,40,92,INK,'900');txt(o.c,'STIPENDIO LORDO ANNUO',0,106,34,GRN,'bold');
 [-80].forEach(y=>{el('rect',{x:-240,y:y-60,width:240,height:14,rx:7,fill:'#C3D3D7'},o.c);});
 o.cap=el('g',{},g);cap(o.cap,"BRUNO GUADAGNA 35.000 € LORDI L'ANNO",54);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.a,520,450,0,0.95*pop(t,0.2,0.8));T(o.n,520,700,0,pop(t,0.6,1.1));
 T(o.c,1300,520,-2,pop(t,1.8,2.4));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:5.2,e:9.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL 33% DI 35.000 €');
 function bx(label,w,fill,col,fs){const c=el('g',{},g);el('rect',{x:-w/2,y:-110,width:w,height:220,rx:34,fill:fill,filter:'url(#g_sh)'},c);txt(c,label,0,fs*0.36,fs,col,'900');return c;}
 o.a=bx('35.000 €',440,'url(#g_paper)',INK,64);
 o.x=el('g',{},g);el('circle',{r:44,fill:'#0B4A50',stroke:'#fff','stroke-width':6},o.x);txt(o.x,'×',0,22,64,'#fff','900');
 o.b=bx('33%',300,'url(#g_paper)',INK,92);
 o.e=el('g',{},g);el('circle',{r:56,fill:'#fff',stroke:AMB,'stroke-width':8},o.e);txt(o.e,'=',0,24,76,INK,'900');
 o.r=bx('11.550 €',460,'url(#g_badge)','#fff',70);
 o.lab=el('g',{},g);tag(o.lab,'OGNI ANNO NEL SALVADANAIO',860,'#0B4A50','#fff',44);
 o.cap=el('g',{},g);cap(o.cap,'IL 33% DI 35.000 € FA 11.550 €',56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.a,280,500,0,pop(t,0.3,0.8));T(o.x,580,500,0,pop(t,0.7,1.1));T(o.b,790,500,0,pop(t,1.0,1.5));
 T(o.e,1030,500,0,pop(t,1.5,2.0));T(o.r,1400,500,0,pop(t,1.9,2.5));
 T(o.lab,1400,690,0,pop(t,2.5,3.0));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[2]={s:9.4,e:12.7,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'OGNI ANNO DI LAVORO');
 o.p=el('g',{},g);piggy(o.p);
 o.c=el('g',{},g);coinS(o.c,46);
 o.t1=el('g',{},g);tag(o.t1,'+ 11.550 €',560,MINT,'#07302A',60);
 o.t2=el('g',{},g);tag(o.t2,'OGNI ANNO',420,'#0B4A50','#fff',44);
 o.cap=el('g',{},g);cap(o.cap,'ECCO QUANTO ENTRA NEL SUO SALVADANAIO OGNI ANNO',48);
 this.o=o;},
 update(t){const o=this.o;
 T(o.p,720,540,0,0.95*pop(t,0.1,0.6));
 T(o.top,960,100,0,1);
 const f=seg(t,0.5,1.1);T(o.c,700,lerp(200,360,eo3(f)),0,1);op(o.c,t<0.5?0:(t<1.05?1:0));
 T(o.t1,1450,440,0,pop(t,1.2,1.8));T(o.t2,1450,580,0,pop(t,1.6,2.2));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
