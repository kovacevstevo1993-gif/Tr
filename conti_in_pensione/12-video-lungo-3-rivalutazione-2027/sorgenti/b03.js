// ===== V3 BLOCCO 3 (436 fotogrammi = 14,53 s): esempi e le tre trappole =====
const SB=[];const TOT=436/30;
SB[0]={s:0,e:7.0,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'ESEMPI SUBITO');
 o.b=[1000,2000,3000,4000].map((v,i)=>{const c=el('g',{},g);bigNum(c,String(v).replace(/(\d)(\d{3})/,'$1.$2')+' €',76,i==3?'url(#g_badge)':'url(#g_paper)','LORDI AL MESE',i==3?'#fff':GRN);return c;});
 o.tg=el('g',{},g);tag(o.tg,'DI QUANTO SALE LA TUA PENSIONE',1000,AMB,'#5A3300',46);
 o.cap=el('g',{},g);cap(o.cap,'TI FACCIO VEDERE SUBITO DI QUANTO SALE LA TUA PENSIONE, DA MILLE A QUATTROMILA EURO',40);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 o.b.forEach((c,i)=>T(c,[285,735,1185,1635][i],[560,500,440,380][i],0,0.95*pop(t,0.6+i*0.8,1.2+i*0.8)));
 T(o.tg,960,760,0,pop(t,4.0,4.6));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:7.0,e:14.53,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'TRE TRAPPOLE');
 o.c=[['1','LE FASCE','RIDUCONO L’AUMENTO','url(#g_red)'],['2','LA PERCENTUALE','CHE LEGGI SUI TITOLI','url(#g_head)'],['3','IL CONGUAGLIO','DI GENNAIO','url(#g_badge)']].map(d=>{const c=el('g',{},g);
  el('rect',{x:-250,y:-150,width:500,height:420,rx:36,fill:'url(#g_paper)',filter:'url(#g_sh)'},c);
  const n=el('g',{},c);n.setAttribute('transform','translate(0 -225)');circN(n,62,d[0],d[3]);
  txt(c,d[1],0,70,42,INK,'900');txt(c,d[2],0,140,32,GRN,'bold');return c;});
 o.cap=el('g',{},g);cap(o.cap,'TRE TRAPPOLE: LE FASCE, LA PERCENTUALE DEI TITOLI E IL CONGUAGLIO',46);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 o.c.forEach((c,i)=>T(c,[420,960,1500][i],540,0,pop(t,0.5+i*1.9,1.2+i*1.9)));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
