// ===== BLOCCO 15 (448 fotogrammi = 14,93 s): quarant'anni -> 462.000, niente rivalutazione, nella realta' si rivaluta =====
const SB=[];const TOT=448/30;
SB[0]={s:0,e:4.1,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,"QUARANT'ANNI DI LAVORO");
 o.gr=el('g',{},g);o.d=[];for(let i=0;i<40;i++){o.d.push(el('circle',{cx:(i%20)*70-665,cy:Math.floor(i/20)*90-45,r:26,fill:'#2B6F77',stroke:'#fff','stroke-opacity':.3,'stroke-width':2},o.gr));}
 o.t1=el('g',{},g);tag(o.t1,'40 ANNI',380,AMB,'#5A3300',56);
 o.t2=el('g',{},g);tag(o.t2,"11.550 € L'ANNO",620,'#0B4A50','#fff',48);
 o.cap=el('g',{},g);cap(o.cap,'SE BRUNO LAVORA 40 ANNI CON LO STESSO STIPENDIO',48);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.gr,960,450,0,pop(t,0.1,0.6));
 const n=Math.floor(clamp((t-0.5)/0.05,0,40));o.d.forEach((c,i)=>c.setAttribute('fill',i<n?AMB2:'#2B6F77'));
 T(o.t1,960,660,0,pop(t,2.4,2.9));T(o.t2,960,770,0,pop(t,2.7,3.2));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:4.1,e:8.1,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL SALVADANAIO ARRIVA A');
 o.p=el('g',{},g);piggy(o.p);
 o.n=el('g',{},g);
 el('rect',{x:-370,y:-150,width:740,height:300,rx:40,fill:'url(#g_badge)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},o.n);
 txt(o.n,'462.000 €',0,38,108,'#fff','900');txt(o.n,'40 × 11.550 €',0,112,42,'#D6F5EC','bold');
 o.cap=el('g',{},g);cap(o.cap,'IL SALVADANAIO ARRIVA A 462.000 €',56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.p,520,540,0,0.95*pop(t,0.2,0.8));
 T(o.n,1350,520,0,pop(t,1.0,1.7));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[2]={s:8.1,e:10.9,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PER SEMPLICITÀ');
 o.st=el('g',{},g);stamp(o.st,'NIENTE RIVALUTAZIONE',1020,RED_,70);
 o.ar=el('g',{},g);arrowDown(o.ar,'#8FA3A8');
 o.x=el('g',{},g);el('path',{d:'M-90 -90 L90 90 M90 -90 L-90 90',stroke:RED_,'stroke-width':26,'stroke-linecap':'round'},o.x);
 o.cap=el('g',{},g);cap(o.cap,'PER SEMPLICITÀ NON CONTO LA RIVALUTAZIONE',52);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.st,960,400,-3,t>0.3?lerp(1.6,1,eo3(seg(t,0.3,0.7))):0);op(o.st,clamp(seg(t,0.3,0.6)*2));
 T(o.ar,960,700,180,1.2*pop(t,0.9,1.4));
 T(o.x,960,700,0,pop(t,1.2,1.6));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[3]={s:10.9,e:14.93,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'NELLA REALTÀ');
 o.bs=bars(g,5);
 o.ar=[0,1,2,3,4].map(i=>{const a=el('g',{},g);arrowDown(a,AMB);return a;});
 o.t1=el('g',{},g);tag(o.t1,'SI RIVALUTA OGNI ANNO',700,MINT,'#07302A',48);
 o.t2=el('g',{},g);tag(o.t2,'PIL NOMINALE · ULTIMI 5 ANNI',900,'#0B4A50','#fff',42);
 o.cap=el('g',{},g);cap(o.cap,'NELLA REALTÀ IL MONTANTE SI RIVALUTA OGNI ANNO',50);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.bs.g,960,712,0,0.88);
 for(let i=0;i<5;i++){setBar(o.bs,i,eo3(seg(t,0.2+i*0.15,0.7+i*0.15)),MINT);}
 o.ar.forEach((a,i)=>T(a,960+o.bs.r[i].x,712-0.88*o.bs.r[i].h-60,180,0.42*pop(t,1.1+i*0.18,1.5+i*0.18)));
 T(o.t1,960,168,0,pop(t,2.0,2.5));T(o.t2,960,838,0,pop(t,2.3,2.8));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
