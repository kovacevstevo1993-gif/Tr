// ===== BLOCCO 9 (369 fotogrammi = 12,30 s): porta numero due (misto) =====
const SB=[];const TOT=369/30;
SB[0]={s:0,e:6.5,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'PORTA NUMERO DUE');
 o.d=el('g',{},g);doorN(o.d,2,'url(#g_badge)');
 o.t1=el('g',{},g);tag(o.t1,'AL 31 DICEMBRE 1995',620,'#0B4A50','#fff',46);
 o.dr=dotsRow(g,18,0);
 o.t2=el('g',{},g);tag(o.t2,'MENO DI 18 ANNI DI CONTRIBUTI',900,AMB,'#5A3300',46);
 o.cap=el('g',{},g);cap(o.cap,'A FINE 1995 AVEVI MENO DI 18 ANNI DI CONTRIBUTI',48);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.d,430,560,0,0.8*pop(t,0.2,0.8));
 T(o.t1,1230,380,0,pop(t,0.9,1.4));
 T(o.dr.g,1230,520,0,1.2*seg(t,1.4,1.8));op(o.dr.g,seg(t,1.4,1.8));
 const nd=Math.floor(clamp((t-1.8)/0.08,0,17));o.dr.a.forEach((d,i)=>lightDot(d,i<nd,0.5));
 T(o.t2,1230,660,0,pop(t,3.4,3.9));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:6.5,e:12.3,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'IL MISTO');
 o.bs=bars(g,10);
 o.t1=el('g',{},g);tag(o.t1,'RETRIBUTIVO',420,AMB2,'#5A3300',44);
 o.t2=el('g',{},g);tag(o.t2,'CONTRIBUTIVO',440,MINT,'#07302A',44);
 o.b1=el('g',{},g);tag(o.b1,'FINO AL 1995',400,'#0B4A50','#fff',38);
 o.b2=el('g',{},g);tag(o.b2,'DA LÌ IN POI',380,'#0B4A50','#fff',38);
 o.dv=el('g',{},g);el('line',{x1:0,y1:-470,x2:0,y2:10,stroke:'#fff','stroke-width':6,'stroke-dasharray':'16 12'},o.dv);
 o.cap=el('g',{},g);cap(o.cap,'MISTO: RETRIBUTIVO FINO AL 1995, POI CONTRIBUTIVO',48);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.bs.g,960,700,0,1);
 for(let i=0;i<10;i++){setBar(o.bs,i,eo3(seg(t,0.1+i*0.05,0.5+i*0.05)),i<5?(t>1.1?AMB2:DIM):(t>3.7?MINT:DIM));}
 T(o.dv,960,700,0,1);op(o.dv,seg(t,0.7,1.1));
 T(o.t1,685,225,0,pop(t,1.1,1.6));T(o.b1,685,825,0,pop(t,1.4,1.9));
 T(o.t2,1235,225,0,pop(t,3.7,4.2));T(o.b2,1235,825,0,pop(t,4.0,4.5));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
