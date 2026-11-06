// ===== SHORT 19: composizioni NUOVE (titolo + forbice + scalini + persona, articolo + parlamento + barra + pensione, intero/non intero + confine + regola, atto + calcolatrice + intervallo + mistero, video correlato + iscriviti + mi piace) =====
const SX=540;
function titleCard(p){const g=el('g',{},p);sheet(g,760,330);el('rect',{x:-380,y:-165,width:700,height:78,fill:GRN},g);
 fit(g,'RIVALUTAZIONE',-20,-108,50,'#fff',620);fit(g,'PENSIONI',-20,24,140,INK,640);fit(g,'DAL 2027',-20,112,76,ORG,520);return g;}
function cutCard(p){const g=el('g',{},p);sheet(g,860,210,'#fff',RED);
 const s=scissorsI(g,1.0,RED);s.setAttribute('transform','translate(-300 0)');
 fit(g,'OLTRE 1.000 €',90,-6,86,RED,560);fit(g,'IN UN ANNO',90,66,52,INK,460);return g;}
function docI(p,w,h,band,l1,l2,bc){const g=el('g',{},p);sheet(g,w,h);
 el('path',{d:`M${-w/2} ${-h/2} H${w/2-44} L${w/2-44} ${-h/2+60} H${-w/2}Z`,fill:bc||GRN},g);fit(g,band,-w/2+30,-h/2+44,34,'#fff',w-130,'start');
 fit(g,l1,-10,-h/2+60+(h-60)*.5,56,INK,w-70);if(l2)fit(g,l2,-10,-h/2+60+(h-60)*.85,46,'#1B9F81',w-70);return g;}
const S=[
// ---- 1: titolo + forbice + sei scalini + "tu" sullo scalino ----
{D:DUR[0],build(p){const o={};head(p,o,0);
 o.t=titleCard(p);o.c=cutCard(p);
 o.st=el('g',{},p);stairsI(o.st,6,760,240,null);
 o.pl=pillS(p,'6 SCALINI',420,42,NAVY);
 o.me=el('g',{},p);{const b=el('g',{},o.me);el('circle',{r:44,fill:ORG,stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},b);fit(b,'?',0,20,64,'#fff',50);
  const pr=personI(o.me,.8,NAVY);pr.setAttribute('transform','translate(0 88)');T(b,0,0,0,1);}
 o.q=pillS(p,'SU QUALE SEI TU?',700,40,ORG);
 o.cap=strip(p,['TAGLIO A SEI SCALINI','SU QUALE SEI TU?']);return o;},
 update(t,o){const a=plan(0,['Rivalutazione pensioni','per qualcuno il taglio','La manovra la divide','Su quale scalino']);PL[0]=a;headU(t,o);bgx(t);
  fade(t,o.t,540,450,a[0]);fade(t,o.c,540,745,a[1]);
  fade(t,o.st,540,1170,a[2],0);T(o.pl,540,1250,0,pop(t,a[2]+.5));
  const k=sl(t,a[3],.9);T(o.me,540-380+2.5*126.7,1170-240*3/6-110+(1-k)*-60,0,1);op(o.me,seg(t,a[3],a[3]+.55));
  T(o.q,540,1370,0,pop(t,a[3]));rise(t,a[4],.9,o.cap,1560,100);}},
// ---- 2: articolo 55 + parlamento + disegno di legge + barra "quanta parte" + tua pensione + importo ----
{D:DUR[1],build(p){const o={};head(p,o,1);
 o.ar=el('g',{},p);docI(o.ar,470,300,'LA MANOVRA','ARTICOLO','55',GRN);
 o.pa=el('g',{},p);buildingI(o.pa,1.1);
 o.dl=el('g',{},p);{const s=pillS(o.dl,'DISEGNO DI LEGGE',640,46,'#0B4A50');T(s,0,-60,0,1);const s2=pillS(o.dl,'ANCORA DA VOTARE',640,46,ORG);T(s2,0,56,0,1);}
 o.ba=el('g',{},p);{fit(o.ba,'AUMENTO DI GENNAIO',0,-50,46,'#fff',700);el('rect',{x:-400,y:-18,width:800,height:64,rx:32,fill:'#DCE7EA',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},o.ba);
  el('rect',{x:-400,y:-18,width:480,height:64,rx:32,fill:'url(#g_head)'},o.ba);fit(o.ba,'QUANTA PARTE?',240,25,30,NAVY,290);}
 o.pe=el('g',{},p);sheet(o.pe,760,150,'#fff',GRN);{const cn=coin(o.pe,-300,0,50);fit(o.pe,'LA TUA PENSIONE',50,18,54,INK,520);}
 o.ar2=el('path',{d:'M-46 -50 H46 V0 H100 L0 100 L-100 0 H-46Z',fill:YEL,stroke:'#fff','stroke-width':7,'stroke-linejoin':'round',filter:'url(#g_sh2)'},p);
 o.im=el('g',{},p);{const pl=pillS(o.im,'',900,40,GRN);fit(o.im,'DIPENDE DA QUANTO PRENDI AL MESE',0,13,40,'#fff',840);}
 o.cap=strip(p,['ARTICOLO 55 DELLA MANOVRA','QUANTO AUMENTA LA TUA PENSIONE?']);return o;},
 update(t,o){const a=plan(1,['L\'articolo cinquantacinque','un disegno di legge','stabilisce quanta parte','arriva alla tua pensione','Dipende da quanto prendi']);PL[1]=a;headU(t,o);bgx(t);
  fade(t,o.ar,330,500,a[0]);fade(t,o.pa,820,490,a[0]+.45);fade(t,o.dl,540,775,a[1]);
  fade(t,o.ba,540,1030,a[2]);fade(t,o.pe,540,1240,a[3]);T(o.ar2,540,1135,0,pop(t,a[3])*.55);fade(t,o.im,540,1400,a[4]);
  rise(t,a[5],.9,o.cap,1600,100);}},
// ---- 3: intero / non intero + confine + chi supera di poco + regola apposta ----
{D:DUR[2],build(p){const o={};head(p,o,2);
 o.a=el('g',{},p);sheet(o.a,860,200,'#fff','#1E9C6E');{const ck=checkI(o.a,56,'#1E9C6E');ck.setAttribute('transform','translate(-340 0)');fit(o.a,'AUMENTO INTERO',70,18,60,INK,560);}
 o.b=el('g',{},p);sheet(o.b,860,200,'#fff',RED);{const sc=scissorsI(o.b,.8,RED);sc.setAttribute('transform','translate(-300 0)');fit(o.b,'NON INTERO',70,18,60,RED,560);}
 o.cf=el('g',{},p);{el('line',{x1:-480,y1:0,x2:480,y2:0,stroke:YEL,'stroke-width':8,'stroke-dasharray':'26 16','stroke-linecap':'round'},o.cf);const pl=pillS(o.cf,'IL CONFINE?',420,36,NAVY);}
 o.pr=el('g',{},p);{el('circle',{cx:-330,cy:0,r:72,fill:'#fff',stroke:YEL,'stroke-width':8,filter:'url(#g_sh2)'},o.pr);const pe=personI(o.pr,1.1,NAVY);pe.setAttribute('transform','translate(-330 14)');el('path',{d:'M-220 -14 H-110 V-44 L-40 6 L-110 56 V26 H-220Z',fill:YEL,stroke:'#fff','stroke-width':5,'stroke-linejoin':'round'},o.pr);
  fit(o.pr,'SUPERA DI POCO',235,20,50,'#fff',440);}
 o.rg=el('g',{},p);docI(o.rg,760,230,'LA REGOLA APPOSTA','CAMBIA I CONTI',null,ORG);
 o.cap=strip(p,['AUMENTO INTERO O NO?','DOVE PASSA IL CONFINE?']);return o;},
 update(t,o){const a=plan(2,['Per qualcuno l\'aumento arriva intero','per qualcuno no','Dove passa il confine','Per chi lo supera di poco','nel testo c\'è una regola apposta']);PL[2]=a;headU(t,o);bgx(t);
  fade(t,o.a,540,500,a[0]);fade(t,o.b,540,830,a[1]);T(o.cf,540,665,0,pop(t,a[2]));op(o.cf,seg(t,a[2],a[2]+.55));
  fade(t,o.pr,540,1050,a[3]);fade(t,o.rg,540,1290,a[4]);rise(t,a[5],.9,o.cap,1590,100);}},
// ---- 4: atto della Camera + calcolatrice con scalino + intervallo di esempi + "dove l'abbiamo gia vista?" ----
{D:DUR[3],build(p){const o={};head(p,o,3);
 o.at=el('g',{},p);docI(o.at,760,230,'ATTO DELLA CAMERA','TESTO UFFICIALE',null,GRN);
 o.co=el('g',{},p);{const cl=calcI(o.co,1.2);cl.setAttribute('transform','translate(-330 0)');const st=el('g',{transform:'translate(120 90)'},o.co);stairsI(st,5,520,240,2);fit(o.co,'UNO SCALINO ALLA VOLTA',120,-200,38,'#fff',560);}
 o.ra=el('g',{},p);{const l=pillS(o.ra,'1.500 €',280,46,GRN);T(l,-300,0,0,1);const r=pillS(o.ra,'7.000 €',280,46,RED);T(r,300,0,0,1);
  el('path',{d:'M-130 0 H90 M60 -30 L100 0 L60 30',fill:'none',stroke:YEL,'stroke-width':14,'stroke-linecap':'round','stroke-linejoin':'round'},o.ra);fit(o.ra,'LORDI AL MESE',0,92,40,'#fff',520);}
 o.mi=el('g',{},p);sheet(o.mi,820,210,'#fff',ORG);{const st=el('g',{transform:'translate(-330 60)'},o.mi);stairsI(st,4,200,110,null,'#9FB4B9');fit(o.mi,'?',-150,30,120,ORG,90);fit(o.mi,'DOVE L\'ABBIAMO GIÀ VISTA?',170,16,44,INK,460);}
 o.cap=strip(p,['UN CONTO PER OGNI SCALINO','ESEMPI DA 1.500 A 7.000 EURO']);return o;},
 update(t,o){const a=plan(3,['l\'atto della Camera','il conto uno scalino','con esempi da millecinquecento','dove abbiamo già visto']);PL[3]=a;headU(t,o);bgx(t);
  fade(t,o.at,540,470,a[0]);fade(t,o.co,540,840,a[1]);fade(t,o.ra,540,1120,a[2]);fade(t,o.mi,540,1370,a[3]);
  rise(t,a[4],.9,o.cap,1610,100);}},
// ---- 5: video correlato + risposta e conti + testo ufficiale + iscriviti + mi piace ----
{D:DUR[4],build(p){const o={};head(p,o,4);
 o.vc=el('g',{},p);{el('rect',{x:-260,y:-150,width:520,height:300,rx:50,fill:'url(#g_red)',stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},o.vc);el('path',{d:'M-50 -80 L100 0 L-50 80Z',fill:'#fff','stroke-linejoin':'round',stroke:'#fff','stroke-width':22},o.vc);}
 o.vp=pillS(p,'VIDEO CORRELATO QUI SOTTO',760,36,NAVY);
 o.rc=el('g',{},p);{[[-210,'LA RISPOSTA','#1E9C6E'],[210,'I CONTI',ORG]].forEach(([x,s,c])=>{const g=el('g',{transform:'translate('+x+' 0)'},o.rc);sheet(g,380,150,'#fff',c);fit(g,s,-12,18,46,INK,300);});}
 o.tu=el('g',{},p);sheet(o.tu,760,150,'#fff',GRN);{const ck=checkI(o.tu,48,'#1E9C6E');ck.setAttribute('transform','translate(-300 0)');fit(o.tu,'SUL TESTO UFFICIALE',50,18,48,INK,500);}
 o.is=el('g',{},p);el('rect',{x:-250,y:-80,width:500,height:160,rx:40,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.is);fit(o.is,'ISCRIVITI',-40,2,60,'#fff',300);fit(o.is,'A CONTI IN PENSIONE',-40,52,28,'#fff',340);{const be=bellI(o.is,.5);T(be,190,-4,0,1);}
 o.lk=el('g',{},p);el('rect',{x:-190,y:-80,width:380,height:160,rx:40,fill:NAVY,stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.lk);{const th=thumbI(o.lk,.55);th.setAttribute('transform','translate(-140 4)');}fit(o.lk,'MI PIACE',62,18,50,'#fff',190);
 o.cap=strip(p,['I CONTI SONO NEL VIDEO CORRELATO','ISCRIVITI E METTI MI PIACE']);return o;},
 update(t,o){const a=plan(4,['Nel video correlato qui sotto','trovi la risposta e i conti','Se vuoi conti fatti sul testo ufficiale','iscriviti a Conti in Pensione','metti mi piace']);PL[4]=a;headU(t,o);bgx(t);
  fade(t,o.vc,540,470,a[0]);T(o.vp,540,700,0,pop(t,a[0]+.25));fade(t,o.rc,540,880,a[1]);fade(t,o.tu,540,1090,a[2]);
  fade(t,o.is,310,1310,a[3]);fade(t,o.lk,810,1310,a[4]);
  rise(t,a[5],.9,o.cap,1590,100);}},
];
