// ===== BLOCCO 6 (401 fotogrammi = 13,37 s): i tre sistemi spiegati =====
const SB=[];const TOT=401/30;
SB[0]={s:0,e:4.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'1 · RETRIBUTIVO');
 o.bs=bars(g,10);
 o.tg=el('g',{},g);tag(o.tg,'ULTIMI ANNI DI STIPENDIO',700,AMB2,'#5A3300',46);
 o.cap=el('g',{},g);cap(o.cap,'RETRIBUTIVO: CONTANO GLI ULTIMI ANNI DI STIPENDIO',50);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.bs.g,960,700,0,1);
 for(let i=0;i<10;i++){setBar(o.bs,i,eo3(seg(t,0.1+i*0.07,0.6+i*0.07)),i>=7&&t>1.5?AMB2:DIM);}
 const lit=seg(t,1.4,1.9);
 for(let i=0;i<10;i++){if(i>=7&&t>1.4)o.bs.r[i].b.setAttribute('fill',AMB2);else o.bs.r[i].b.setAttribute('fill',t>1.4?'#1E4F55':DIM);}
 T(o.tg,960+1100/10*3.5,225,0,pop(t,1.6,2.2));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:4.4,e:9.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'2 · CONTRIBUTIVO');
 o.bs=bars(g,10);
 o.tg=el('g',{},g);tag(o.tg,'TUTTI GLI ANNI CONTANO',680,MINT,'#07302A',46);
 o.f=el('g',{},g);tag(o.f,'PRIMO GIORNO',330,'#0B4A50','#fff',34);
 o.l=el('g',{},g);tag(o.l,'ULTIMO GIORNO',360,'#0B4A50','#fff',34);
 o.cap=el('g',{},g);cap(o.cap,'CONTRIBUTIVO: CONTA TUTTO QUELLO CHE HAI VERSATO',50);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.bs.g,960,700,0,1);
 for(let i=0;i<10;i++){setBar(o.bs,i,1,t>0.6+i*0.15?MINT:DIM);}
 T(o.tg,960,225,0,pop(t,0.4,1.0));
 T(o.f,960-550,822,0,pop(t,2.3,2.8));T(o.l,960+550,822,0,pop(t,2.7,3.2));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[2]={s:9.0,e:13.37,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'3 · MISTO');
 o.bs=bars(g,10);
 o.t1=el('g',{},g);tag(o.t1,'RETRIBUTIVO',420,AMB2,'#5A3300',44);
 o.t2=el('g',{},g);tag(o.t2,'CONTRIBUTIVO',440,MINT,'#07302A',44);
 o.dv=el('g',{},g);el('line',{x1:0,y1:-470,x2:0,y2:10,stroke:'#fff','stroke-width':6,'stroke-dasharray':'16 12'},o.dv);
 o.cap=el('g',{},g);cap(o.cap,"MISTO: UN PO' DELL'UNO E UN PO' DELL'ALTRO",50);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.bs.g,960,700,0,1);
 for(let i=0;i<10;i++){setBar(o.bs,i,1,t>0.4?(i<5?AMB2:(t>1.8?MINT:DIM)):DIM);}
 T(o.t1,960-275,225,0,pop(t,0.5,1.0));T(o.t2,960+275,225,0,pop(t,1.7,2.2));
 T(o.dv,960,700,0,1);op(o.dv,seg(t,0.4,0.9));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
