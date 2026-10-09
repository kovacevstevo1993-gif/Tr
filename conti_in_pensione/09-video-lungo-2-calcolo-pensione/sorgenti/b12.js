// ===== BLOCCO 12 (346 fotogrammi = 11,53 s): su cento euro quanti vanno nel salvadanaio? =====
const SB=[];const TOT=346/30;
SB[0]={s:0,e:6.3,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'E ORA UNA DOMANDA');
 o.q=el('g',{},g);qBubble(o.q,95);
 o.b=el('g',{},g);bill(o.b,'100');
 o.bt=el('g',{},g);tag(o.bt,'STIPENDIO LORDO',470,'#0B4A50','#fff',40);
 o.ar=el('g',{},g);arrowRight(o.ar,AMB);
 o.p=el('g',{},g);piggy(o.p);
 o.pt=el('g',{},g);tag(o.pt,'SALVADANAIO PENSIONE',560,'#0B4A50','#fff',40);
 o.cap=el('g',{},g);cap(o.cap,'SU 100 EURO LORDI, QUANTI VANNO NEL SALVADANAIO?',46);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 T(o.q,1400,235,8*Math.sin(t*4),pop(t,0.2,0.8)*(t>0.8?1+0.05*Math.sin(t*6):1));
 T(o.b,500,500,-3,pop(t,1.5,2.0));T(o.bt,500,690,0,pop(t,1.9,2.4));
 T(o.ar,930,500,0,0.9*pop(t,2.2,2.7));
 T(o.p,1400,540,0,0.9*pop(t,2.6,3.2));T(o.pt,1400,780,0,pop(t,3.2,3.7));
 T(o.cap,960,950,0,pop(t,0.3,0.9));
 }};
SB[1]={s:6.3,e:11.53,build(g){const o={};
 o.top=el('g',{},g);topLabel(o.top,'DIECI? VENTI? TRENTATRÉ?');
 o.c=[['10 €','DIECI?'],['20 €','VENTI?'],['33 €','TRENTATRÉ?']].map(d=>{const c=el('g',{},g);
  el('rect',{x:-190,y:-130,width:380,height:260,rx:32,fill:'url(#g_paper)',filter:'url(#g_sh)'},c);
  txt(c,d[0],0,24,100,INK,'900');txt(c,'SU 100 EURO',0,92,34,GRN,'bold');return c;});
 o.ck=el('g',{},g);el('circle',{r:80,fill:'#fff',stroke:'#0B4A50','stroke-width':10},o.ck);o.n=txt(o.ck,'3',0,34,100,INK,'900');
 o.pr=el('g',{},g);tag(o.pr,'PRONTO?',460,AMB,'#5A3300',58);
 o.cap=el('g',{},g);cap(o.cap,'PENSACI UN SECONDO...',58);
 this.o=o;},
 update(t){const o=this.o;
 T(o.top,960,100,0,1);
 o.c.forEach((c,i)=>T(c,[460,960,1460][i],440,[-2,0,2][i],0.95*pop(t,0.3+i*0.6,0.8+i*0.6)));
 const k=t<2.4?0:(t<3.0?3:(t<3.6?2:(t<4.0?1:0)));
 o.n.textContent=String(k||'');
 T(o.ck,960,760,0,(t>=2.4&&t<4.0)?pop(t,2.4,2.8):0);
 T(o.pr,960,760,0,pop(t,4.0,4.4));
 T(o.cap,960,950,0,pop(t,0.2,0.8));
 }};
