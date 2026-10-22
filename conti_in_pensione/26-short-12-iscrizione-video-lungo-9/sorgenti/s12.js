// ===== SHORT 12: attira iscritti + teaser video lungo 9 (dicembre). Composizioni NUOVE in ogni blocco =====
// varianti rispetto agli short 8-11 (N.47: ogni short sembra diverso a colpo d'occhio, stessi colori): schede con LINGUETTA in alto (non filetto verde),
// avanzamento a righello con segnalino, didascalia con calendarietto DIC, blocchi affiancati / cerchi / righello del limite / telefono.
const AMB='#C98500',GRN='#13805F';
function calBadge(p,s,num){const g=el('g',{transform:'scale('+s+')'},p);
 el('rect',{x:-40,y:-44,width:80,height:88,rx:12,fill:'#fff',stroke:RED,'stroke-width':5},g);
 el('rect',{x:-40,y:-44,width:80,height:30,rx:10,fill:RED},g);el('rect',{x:-40,y:-30,width:80,height:16,fill:RED},g);
 txt(g,'DIC',0,-21,22,'#fff','bold');txt(g,num||'',0,30,44,INK,'bold');return g;}
function topLabelC(p,s){const fs=46,sp=4;const w=s.length*(fs*0.76+sp)+110;const g=el('g',{},p);
 const c=el('g',{transform:'translate('+(-w/2+36)+' 0)'},g);calBadge(c,.62,'');
 const x=txt(g,s,-w/2+90,fs*0.36,fs,'#7FF0D2','bold','start');x.setAttribute('letter-spacing',sp);return g;}
function head(p,o,s,i){o.lab=topLabelC(p,s);o.pr=prog(p,i);}
function headU(t,o){T(o.lab,540,130,0,1);op(o.lab,seg(t,0,.9));T(o.pr,540,215,0,1);op(o.pr,seg(t,0,.9));}
// avanzamento a righello: 5 tacche, segnalino giallo sulla tacca del blocco
function prog(p,i){const g=el('g',{},p);el('rect',{x:-240,y:-3,width:480,height:6,rx:3,fill:'#fff','fill-opacity':.3},g);
 el('rect',{x:-240,y:-3,width:120*i,height:6,rx:3,fill:'#FFB020'},g);
 for(let k=0;k<5;k++)el('rect',{x:-240+k*120-2+(k==4?-2:0),y:-16,width:4,height:32,rx:2,fill:k<=i?'#FFB020':'#fff','fill-opacity':k<=i?1:.45},g);
 el('path',{d:'M-14 -34 L14 -34 L0 -14Z',fill:'#FFB020',stroke:'#fff','stroke-width':3,'stroke-linejoin':'round',transform:'translate('+(-240+i*120)+' 0)'},g);return g;}
// didascalia con calendarietto DIC a sinistra
function capV(p,lines,fs){fs=fs||58;const mx=Math.max(...lines.map(l=>l.length));fs=Math.min(fs,(1000-210)/(mx*0.76));const w=Math.min(1000,mx*fs*0.76+210);const h=lines.length*(fs*1.42)+54;const c=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:34,fill:'#06303A',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:34,fill:'none',stroke:'#FFB020','stroke-width':5},c);
 const cb=el('g',{transform:'translate('+(-w/2+80)+' 0)'},c);calBadge(cb,.95,'');
 lines.forEach((l,i)=>txt(c,l,60,-h/2+27+fs*1.08+i*fs*1.42,fs,'#FFFFFF','bold'));return c;}
// scheda con linguetta in alto
function tabCard(p,w,h,label,col){const g=el('g',{},p);plateRect(g,-w/2,-h/2,w,h,46);
 const tw=Math.min(w-80,label.length*19+56);
 el('rect',{x:-w/2+34,y:-h/2-24,width:tw,height:48,rx:24,fill:col||'#1B9F81',stroke:'#fff','stroke-width':4},g);
 txt(g,label,-w/2+34+tw/2,-h/2+9,25,'#fff','bold');return g;}
function playI(p){const g=el('g',{filter:'url(#g_sh2)'},p);el('rect',{x:-70,y:-50,width:140,height:100,rx:26,fill:RED,stroke:'#fff','stroke-width':6},g);el('path',{d:'M-16 -24 L26 0 L-16 24Z',fill:'#fff'},g);return g;}
function avatar(p,col){const g=el('g',{},p);el('circle',{r:46,fill:col,stroke:'#fff','stroke-width':6},g);el('circle',{cy:-10,r:16,fill:'#fff'},g);el('path',{d:'M-26 30 Q0 -4 26 30Z',fill:'#fff'},g);return g;}
function docSeal(p){const g=el('g',{filter:'url(#g_sh2)'},p);el('rect',{x:-50,y:-66,width:100,height:132,rx:10,fill:'#fff',stroke:'#9FB4B9','stroke-width':4},g);
 [-44,-22,0].forEach(y=>el('rect',{x:-34,y:y,width:68,height:9,rx:4,fill:'#C9D6D8'},g));el('circle',{cx:16,cy:36,r:22,fill:AMB,stroke:'#fff','stroke-width':4},g);el('path',{d:'M6 36 l7 8 l14 -15',fill:'none',stroke:'#fff','stroke-width':6,'stroke-linecap':'round','stroke-linejoin':'round'},g);return g;}
function envI(p,s){const g=el('g',{transform:'scale('+s+')'},p);el('rect',{x:-50,y:-34,width:100,height:68,rx:10,fill:'#fff',stroke:'#9FB4B9','stroke-width':4},g);el('path',{d:'M-46 -28 L0 8 L46 -28',fill:'none',stroke:'#9FB4B9','stroke-width':5,'stroke-linejoin':'round'},g);return g;}
function fade(t,n,x,y,a){T(n,x,y+(1-sl(t,a,.9))*60,0,1);op(n,seg(t,a,a+.55));}
function bell(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
function bubble(p,w,h,fill){const g=el('g',{filter:'url(#g_sh)'},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:40,fill:fill,stroke:'#fff','stroke-width':4},g);
 el('path',{d:`M${-w/2+30} ${h/2-4} l40 0 l-60 34 Z`,fill:fill},g);return g;}
function bust(p,x,y,s,shirt,hair){const g=el('g',{transform:'translate('+x+' '+y+') scale('+s+')'},p);person(g,shirt,hair);return g;}
function circB(p,r,fill){const g=el('g',{},p);el('circle',{r:r,fill:fill,stroke:'#fff','stroke-width':10,filter:'url(#g_sh)'},g);
 el('path',{d:`M${-r*.62} ${-r*.2} A${r*.7} ${r*.7} 0 0 1 ${r*.1} ${-r*.66}`,fill:'none',stroke:'#fff','stroke-opacity':.4,'stroke-width':r*.05,'stroke-linecap':'round'},g);return g;}
const S=[
// ---- 1: due pensionati affiancati, bonus / zero ----
{D:DUR[0],build(p){const o={};head(p,o,'PENSIONI DI DICEMBRE',0);
 o.cards=el('g',{},p);o.cards._x=540;o.sl=[];
 [[-270,'PENSIONATO 1','#1B9F81','#5A6E73'],[270,'PENSIONATO 2',AMB,'#9AA5A8']].forEach(d=>{const c=tabCard(o.cards,470,400,d[1],'#1B9F81');c.setAttribute('transform','translate('+d[0]+' 0)');
  bust(c,0,-80,.75,d[2],d[3]);const l=el('g',{},c);txt(l,'SENZA ALTRI REDDITI',0,150,27,'#1B9F81','bold');o.sl.push(l);});
 o.eq=el('g',{},p);el('circle',{r:56,fill:'#06303A',stroke:'#FFB020','stroke-width':6,filter:'url(#g_sh2)'},o.eq);txt(o.eq,'≈',0,22,76,'#FFB020','bold');
 o.lq=pillL(p,'QUASI LA STESSA PENSIONE',720,30,'#0B4A50');o.lq._x=540;
 o.ra=pillL(p,'UNA PARTE DEL BONUS',470,32,GRN);o.rb=pillL(p,'ZERO',470,40,RED);
 o.df=pillL(p,'DIFFERENZA: 10 € AL MESE',820,40,'#0B4A50');o.df._x=540;
 o.st=stamp(p,'NON È UNO SBAGLIO',700,46,RED);
 o.cap=capV(p,['UN LIMITE SCRITTO','NELLA LEGGE']);return o;},
 update(t,o){const i=0;const a=plan(i,['due pensionati','senza altri redditi','quasi la stessa','una parte del bonus',"l'altro zero",'Dieci euro','Non è uno sbaglio']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.cards,690,120);o.sl.forEach(l=>inC(t,l,0,0,a[1]));
  T(o.eq,540,690,0,pop(t,a[2]));rise(t,a[2]+.1,.9,o.lq,955,90);
  T(o.ra,270,1055,0,pop(t,a[3]));T(o.rb,810,1055,0,pop(t,a[4]));
  rise(t,a[5],.9,o.df,1175,90);stampIn(t,o.st,a[6],540,1310,-3);
  T(o.cap,540,CAPY,0,pop(t,a[7]));}},
// ---- 2: calendario, due cerchi e pillola tratteggiata ----
{D:DUR[1],build(p){const o={};head(p,o,'TRE PAGAMENTI',1);
 o.cal=tabCard(p,900,230,'A DICEMBRE','#1B9F81');const cb=el('g',{transform:'translate(-340 6)'},o.cal);calBadge(cb,1.5,'');
 txt(o.cal,'POSSONO ARRIVARE',-230,-10,46,INK,'bold','start');txt(o.cal,'TRE PAGAMENTI',-230,64,56,'#1B9F81','bold','start');o.cal._x=540;
 o.c1=circB(p,185,'url(#g_badge)');coin(o.c1,0,-72,52);txt(o.c1,'TREDICESIMA',0,78,37,'#fff','bold');
 o.c2=circB(p,185,YEL);txt(o.c2,'BONUS',0,-14,60,INK,'bold');txt(o.c2,'154,94 €',0,72,54,'#7A2A00','bold');
 o.q=el('g',{},p);el('rect',{x:-350,y:-90,width:700,height:180,rx:90,fill:'#06303A',stroke:'#FFB020','stroke-width':6,'stroke-dasharray':'20 14',filter:'url(#g_sh2)'},o.q);
 txt(o.q,'QUATTORDICESIMA',0,-4,48,'#fff','bold');txt(o.q,'PER QUALCUNO',0,54,32,'#FFB020','bold');o.q._x=540;
 o.cap=capV(p,['OLTRE 400.000 PENSIONATI','HANNO AVUTO IL BONUS']);return o;},
 update(t,o){const i=1;const a=plan(i,['A dicembre','la tredicesima','un bonus di','e per qualcuno']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.cal,470,120);T(o.c1,290,880,0,pop(t,a[1]));T(o.c2,790,880,0,pop(t,a[2]));
  rise(t,a[3],.9,o.q,1260,100);T(o.cap,540,CAPY,0,pop(t,a[4]));}},
// ---- 3: regole, righello del limite, rata arrivata, tre vicini ----
{D:DUR[2],build(p){const o={};head(p,o,'ALLE REGOLE',2);
 o.rg=tabCard(p,940,200,'REGOLE','#1B9F81');[-350,-240,-130].forEach(x=>{const d=el('g',{transform:'translate('+x+' 0) scale(.8)'},o.rg);docSeal(d);});
 txt(o.rg,'OGNI PAGAMENTO',-40,-8,46,INK,'bold','start');txt(o.rg,'LE SUE REGOLE',-40,52,40,'#1B9F81','bold','start');o.rg._x=540;
 o.lm=tabCard(p,940,260,'IL LIMITE',RED);
 el('rect',{x:-380,y:10,width:760,height:40,rx:20,fill:'#DCE7EA'},o.lm);o.fill=el('rect',{x:-380,y:10,width:0,height:40,rx:20,fill:'#1B9F81'},o.lm);
 el('line',{x1:330,y1:-60,x2:330,y2:80,stroke:RED,'stroke-width':7,'stroke-dasharray':'12 9','stroke-linecap':'round'},o.lm);
 txt(o.lm,'LIMITE',330,-72,30,RED,'bold');
 o.av=el('g',{},o.lm);const av=el('g',{transform:'translate(290 -26) scale(.6)'},o.av);avatar(av,'#1B9F81');
 o.pas=el('g',{},o.lm);txt(o.pas,'A UN PASSO',312,100,30,AMB,'bold','end');o.lm._x=540;
 o.ra=el('g',{},p);el('rect',{x:-380,y:-48,width:760,height:96,rx:48,fill:'#0B4A50',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},o.ra);
 const e=el('g',{transform:'translate(-310 0)'},o.ra);envI(e,.8);txt(o.ra,'RATA GIÀ ARRIVATA',30,17,46,'#fff','bold');o.ra._x=540;
 o.tv=tabCard(p,940,300,'TRE VICINI','#1B9F81');
 [[-300,'FRANCO','#1B9F81','#5A6E73'],[0,'ANNA',AMB,'#7A5230'],[300,'LUCIA','#B5523B','#9AA5A8']].forEach(d=>{bust(o.tv,d[0],-58,.5,d[2],d[3]);txt(o.tv,d[1],d[0],134,40,INK,'bold');});o.tv._x=540;
 o.nb=pillL(p,'UNO RESTA SENZA BONUS',820,44,RED);
 o.cap=capV(p,['CHI DEI TRE','SEI TU?']);return o;},
 update(t,o){const i=2;const a=plan(i,['ogni pagamento','a un passo','la rata è già','tre vicini','Uno resta']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.rg,430,110);rise(t,a[1],.9,o.lm,680,110);
  o.fill.setAttribute('width',(690)*eo3(seg(t,a[1]+.4,a[1]+1.3)));inC(t,o.pas,0,0,a[1]+.4);
  rise(t,a[2],.9,o.ra,895,90);rise(t,a[3],.9,o.tv,1120,110);
  T(o.nb,540,1370,0,pop(t,a[4]));T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 4: tu, il canale, i conti, l'obiettivo, iscriviti ----
{D:DUR[3],build(p){const o={};head(p,o,'QUESTO CANALE',3);
 o.q=tabCard(p,940,190,'A DICEMBRE','#1B9F81');const cb=el('g',{transform:'translate(-380 4)'},o.q);calBadge(cb,1.25,'');
 txt(o.q,'ASPETTI QUALCOSA',-300,-6,50,INK,'bold','start');txt(o.q,'IN PIÙ?',-300,56,52,'#1B9F81','bold','start');o.q._x=540;
 o.ch=tabCard(p,940,190,'QUESTO CANALE','#1B9F81');const av=el('g',{transform:'translate(-370 4) scale(1.25)'},o.ch);avatar(av,'#1B9F81');
 txt(o.ch,'È PER TE',-270,36,76,GRN,'bold','start');o.ch._x=540;
 o.cn=tabCard(p,940,190,'CONTI IN EURO','#1B9F81');const cc=el('g',{},o.cn);coin(cc,-370,6,64);
 txt(o.cn,'CON I LIMITI',-270,-4,50,INK,'bold','start');txt(o.cn,'VERI DELL\'INPS',-270,58,50,'#1B9F81','bold','start');o.cn._x=540;
 o.gl=tabCard(p,940,230,'OBIETTIVO',AMB);
 el('rect',{x:-380,y:-6,width:760,height:44,rx:22,fill:'#DCE7EA'},o.gl);el('rect',{x:-380,y:-6,width:70,height:44,rx:22,fill:'#FFB020'},o.gl);
 txt(o.gl,'1.000 ISCRITTI',380,-26,46,INK,'bold','end');txt(o.gl,'ANCORA IN POCHI',-380,92,32,'#5A6E73','bold','start');o.gl._x=540;
 o.sub=el('g',{},p);const pg=el('g',{transform:'translate(40 0)'},o.sub);pillS(pg,'ISCRIVITI',520,60,'url(#g_red)');const bb=el('g',{transform:'translate(345 -2)'},o.sub);bell(bb,.5);
 const gp=el('g',{transform:'translate(-395 0)'},o.sub);pillL(gp,'GRATIS',210,36,GRN);
 o.cap=capV(p,['ISCRIVERSI È GRATIS,','BASTA UN TOCCO']);return o;},
 update(t,o){const i=3;const a=plan(i,['Se hai una pensione','questo canale è per te','Facciamo i conti','il nostro obiettivo','e iscriversi è gratis']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.q,450,110);rise(t,a[1],.9,o.ch,680,110);rise(t,a[2],.9,o.cn,890,110);
  rise(t,a[3],.9,o.gl,1130,110);T(o.sub,540,1365,0,pop(t,a[4]));
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 5: video correlato, iscriviti, mi piace, commento con i tre nomi ----
{D:DUR[4],build(p){const o={};head(p,o,'IL VIDEO',4);
 o.vc=tabCard(p,940,460,'VIDEO CORRELATO',RED);
 el('rect',{x:-410,y:-170,width:820,height:300,rx:26,fill:'#06303A',stroke:'#FFB020','stroke-width':5},o.vc);
 txt(o.vc,'IL DICEMBRE',-340,-60,58,'#fff','bold','start');txt(o.vc,'DEI TRE VICINI',-340,10,58,'#FFB020','bold','start');
 const pb=el('g',{transform:'translate(310 -20) scale(.95)'},o.vc);playI(pb);
 [-300,0,300].forEach((x,k)=>{});[[-340,'#1B9F81','#5A6E73'],[-250,AMB,'#7A5230'],[-160,'#B5523B','#9AA5A8']].forEach(d=>bust(o.vc,d[0],65,.22,d[1],d[2]));
 txt(o.vc,'TOCCALO QUI SOTTO',0,196,34,'#1B9F81','bold');o.vc._x=540;
 o.sub=el('g',{},p);pillS(o.sub,'ISCRIVITI',520,60,'url(#g_red)');const bb=el('g',{transform:'translate(330 -2)'},o.sub);bell(bb,.5);
 o.lk=el('g',{},p);pillS(o.lk,'METTI MI PIACE',760,50,'#0B4A50');const th=el('g',{transform:'translate(-320 -8)'},o.lk);thumb(th,.42);
 o.cm=tabCard(p,940,270,'SCRIVICI NEI COMMENTI',GRN);txt(o.cm,'CHI SEI TU?',0,-6,66,INK,'bold');
 [[-290,'FRANCO'],[0,'ANNA'],[290,'LUCIA']].forEach(d=>{const c=el('g',{transform:'translate('+d[0]+' 76)'},o.cm);pillL(c,d[1],250,32,'#0B4A50');});o.cm._x=540;
 o.cap=capV(p,['CHI SEI TU:','FRANCO, ANNA O LUCIA?']);return o;},
 update(t,o){const i=4;const a=plan(i,['Tocca il video correlato','Iscriviti a','metti mi piace','E scrivici']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.vc,580,110);T(o.sub,540,910,0,pop(t,a[1]));T(o.lk,540,1050,0,pop(t,a[2]));
  rise(t,a[3],.9,o.cm,1285,100);T(o.cap,540,CAPY,0,pop(t,a[4]));}},
];
S.forEach(s=>{s.sb=[{s:0,e:s.D}];});
