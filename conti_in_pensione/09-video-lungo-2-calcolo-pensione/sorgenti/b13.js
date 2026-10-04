// ===== BLOCCO 13 (428 fotogrammi = 14,27 s): la risposta e' 33 =====
const SB=[];const TOT=428/30;
function donut(p,R,w){const g=el('g',{},p);
 el('circle',{r:R,fill:'none',stroke:'#0A3F45','stroke-width':w},g);
 const arc=el('path',{fill:'none',stroke:MINT,'stroke-width':w,'stroke-linecap':'butt'},g);
 const c=txt(g,'33%',0,36,110,'#fff','900');return {g,arc,R};}
function setDonut(d,f){const a=f*Math.PI*2;d.arc.setAttribute('d',f<=0.001?'':`M0 ${-d.R} A${d.R} ${d.R} 0 ${f>.5?1:0} 1 ${d.R*Math.sin(a)} ${-d.R*Math.cos(a)}`);}
SB[0]={s:0,e:4.1,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'LA RISPOSTA');
 o.b=el('g',{},g);el('circle',{r:210,fill:'url(#g_badge)',stroke:'#fff','stroke-width':12,filter:'url(#g_sh)'},o.b);txt(o.b,'33',0,70,220,'#fff','900');
 o.st=el('g',{},g);stamp(o.st,'LAVORATORE DIPENDENTE',820,'#127F70',52);
 o.cap=el('g',{},g);cap(o.cap,'LA RISPOSTA, PER UN DIPENDENTE: 33!',56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.b,560,520,0,pop(t,0.2,0.8));
 T(o.st,1330,520,-3,t>1.2?lerp(1.25,1,eo3(seg(t,1.2,1.6))):0);op(o.st,clamp(seg(t,1.2,1.5)*2));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:4.1,e:7.4,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ALIQUOTA DEL 33%');
 o.d=donut(g,170,64);
 o.t1=el('g',{},g);tag(o.t1,"ALIQUOTA DI COMPUTO",720,AMB,'#5A3300',46);
 o.t2=el('g',{},g);tag(o.t2,'INPS',320,'#0B4A50','#fff',50);
 o.cap=el('g',{},g);cap(o.cap,"L'INPS USA UN'ALIQUOTA DEL 33%",56);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.d.g,640,520,0,pop(t,0.1,0.6));setDonut(o.d,0.33*eio(seg(t,0.4,1.6)));
 T(o.t1,1400,450,0,pop(t,1.3,1.8));T(o.t2,1400,580,0,pop(t,1.6,2.1));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[2]={s:7.4,e:11.8,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'SU OGNI 100 EURO LORDI');
 o.gr=el('g',{},g);o.sq=[];for(let i=0;i<100;i++){o.sq.push(el('rect',{x:(i%10)*48-240,y:Math.floor(i/10)*48-240,width:40,height:40,rx:8,fill:'#2B6F77'},o.gr));}
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.p=el('g',{},g);piggy(o.p);
 o.tg=el('g',{},g);tag(o.tg,'33 € NEL MONTANTE',620,MINT,'#07302A',48);
 o.cap=el('g',{},g);cap(o.cap,'SU OGNI 100 € LORDI, 33 € NEL MONTANTE',52);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.gr,560,500,0,pop(t,0.1,0.6));
 const n=Math.floor(clamp((t-0.7)/0.05,0,33));o.sq.forEach((r,i)=>r.setAttribute('fill',i<n?AMB2:'#2B6F77'));
 T(o.ar,1010,500,0,0.9*pop(t,2.5,3.0));
 T(o.p,1430,540,0,0.8*pop(t,2.8,3.4));
 T(o.tg,1430,790,0,pop(t,3.2,3.7));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
SB[3]={s:11.8,e:14.27,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'COME UN SALVADANAIO');
 o.p=el('g',{},g);piggy(o.p);
 o.c=el('g',{},g);coinS(o.c,46);
 o.tg=el('g',{},g);tag(o.tg,'MONTANTE CONTRIBUTIVO',820,MINT,'#07302A',50);
 o.cap=el('g',{},g);cap(o.cap,'SÌ, PROPRIO COME UN SALVADANAIO!',58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.p,960,540,0,pop(t,0.1,0.6));
 const f=seg(t,0.4,1.0);T(o.c,lerp(930,930,f),lerp(200,360,eo3(f)),0,1);op(o.c,t<0.4?0:(t<0.95?1:0));
 T(o.tg,960,810,0,pop(t,1.0,1.5));
 T(o.cap,960,950,0,pop(t,0.1,0.6));
 }};
