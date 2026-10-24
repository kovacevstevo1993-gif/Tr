// ===== SHORT 13: teaser video lungo 10 (casalinghe). Composizioni NUOVE in ogni blocco (ordine utente 24/10: "un po' piu diverse, piu professionali") =====
// Varianti rispetto agli short 8-12 (N.47, alla lettera "un po' diverse"): tema CASA (tetto, finestra), schede con TESTATA SCURA (non filetto, non linguetta),
// titoletto a SINISTRA con casetta, avanzamento a 6 casette, didascalia CHIARA con moneta (non scura), bilancia, scale che scendono, tessere dei mesi, telefono.
const AMB='#C98500',GRN='#13805F',DK='#0B4A50';
// ---- casetta (tetto + corpo) ----
function houseI(p,s,fill,stroke){const g=el('g',{transform:'scale('+s+')'},p);
 el('path',{d:'M-30 -4 L0 -34 L30 -4 H22 V28 H-22 V-4Z',fill:fill,stroke:stroke||'none','stroke-width':4,'stroke-linejoin':'round'},g);
 el('rect',{x:-7,y:6,width:14,height:22,rx:3,fill:stroke&&stroke!=='none'?'#fff':'#0B3A3F','fill-opacity':.55},g);return g;}
function head(p,o,s,i){o.lab=el('g',{},p);
 const c=el('g',{transform:'translate(34 0)'},o.lab);el('circle',{r:44,fill:'url(#g_badge)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},c);houseI(c,1.05,'#fff','none');
 const x=txt(o.lab,s,96,17,48,'#7FF0D2','bold','start');x.setAttribute('letter-spacing',5);
 o.pr=el('g',{},p);for(let k=0;k<6;k++){const h=el('g',{transform:'translate('+(k*58)+' 0)'},o.pr);houseI(h,.78,k<=i?'#FFB020':'#FFFFFF');if(k>i)h.setAttribute('opacity',.32);}}
function headU(t,o){T(o.lab,80,130,0,1);op(o.lab,seg(t,0,.9));T(o.pr,110,222,0,1);op(o.pr,seg(t,0,.9));}
// ---- didascalia chiara con moneta a sinistra ----
function capV(p,lines,fs){fs=fs||56;const mx=Math.max(...lines.map(l=>l.length));fs=Math.min(fs,(1000-230)/(mx*0.76));const w=Math.min(1010,mx*fs*0.76+230);const h=lines.length*(fs*1.42)+60;const c=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:36,fill:'#F5FBFA',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:h/2-16,width:w,height:16,rx:8,fill:'#FFB020'},c);
 el('rect',{x:-w/2,y:h/2-30,width:w,height:18,fill:'#FFB020'},c);
 const cn=el('g',{},c);coin(cn,-w/2+82,-8,50);
 lines.forEach((l,i)=>txt(c,l,60,-h/2+32+fs*1.0+i*fs*1.42,fs,INK,'bold'));return c;}
// ---- scheda con testata scura ----
function hCard(p,w,h,label,col){const g=el('g',{},p);plateRect(g,-w/2,-h/2,w,h,40);
 el('path',{d:`M${-w/2} ${-h/2+66} V${-h/2+40} a40 40 0 0 1 40 -40 H${w/2-40} a40 40 0 0 1 40 40 V${-h/2+66}Z`,fill:col||DK},g);
 txt(g,label,-w/2+36,-h/2+44,30,'#fff','bold','start').setAttribute('letter-spacing',3);return g;}
function fade(t,n,x,y,a){T(n,x,y+(1-sl(t,a,.9))*60,0,1);op(n,seg(t,a,a+.55));}
function bust(p,x,y,s,shirt,hair){const g=el('g',{transform:'translate('+x+' '+y+') scale('+s+')'},p);person(g,shirt,hair);return g;}
function avatar(p,col){const g=el('g',{},p);el('circle',{r:46,fill:col,stroke:'#fff','stroke-width':6},g);el('circle',{cy:-10,r:16,fill:'#fff'},g);el('path',{d:'M-26 30 Q0 -4 26 30Z',fill:'#fff'},g);return g;}
function bell(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
function lockBig(p,s){const g=el('g',{transform:'scale('+s+')'},p);
 el('path',{d:'M-46 -20 V-70 a46 46 0 0 1 92 0 V-20',fill:'none',stroke:'#fff','stroke-width':20,'stroke-linecap':'round'},g);
 el('rect',{x:-70,y:-22,width:140,height:112,rx:24,fill:YEL,stroke:'#fff','stroke-width':8},g);el('circle',{cx:0,cy:30,r:15,fill:'#7A2A00'},g);return g;}
function note(p,w,h,s1,s2){const g=el('g',{},p);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:16,fill:'#EAF7EC',stroke:GRN,'stroke-width':6},g);
 el('rect',{x:-w/2+14,y:-h/2+14,width:w-28,height:h-28,rx:10,fill:'none',stroke:GRN,'stroke-width':3,'stroke-dasharray':'10 8'},g);
 return g;}
const S=[
// ---- 1: LA CASA con lei, "mai lavorato", ogni mese, senza tasse; poi lui + cifra nascosta ----
{D:DUR[0],build(p){const o={};head(p,o,'CASALINGHE',0);
 o.h=el('g',{},p);
 el('path',{d:'M-310 -40 L0 -310 L310 -40Z',fill:'url(#g_head)',stroke:'#fff','stroke-width':8,'stroke-linejoin':'round',filter:'url(#g_sh)'},o.h);
 el('rect',{x:-262,y:-40,width:524,height:392,rx:14,fill:'url(#g_paper)',stroke:'#fff','stroke-width':6},o.h);
 txt(o.h,'CASALINGHE',0,-92,52,'#fff','bold').setAttribute('letter-spacing',4);
 el('circle',{cx:0,cy:-190,r:34,fill:'#fff','fill-opacity':.28,stroke:'#fff','stroke-width':5},o.h);
 el('rect',{x:-180,y:60,width:150,height:150,rx:20,fill:'#D6F5EC',stroke:'#1B9F81','stroke-width':6},o.h);
 el('rect',{x:-198,y:60,width:186,height:14,rx:7,fill:'#1B9F81'},o.h);
 bust(o.h,-105,146,.42,'#1B9F81','#5A6E73');
 el('rect',{x:60,y:96,width:150,height:256,rx:18,fill:'#0B4A50'},o.h);el('circle',{cx:186,cy:226,r:9,fill:YEL},o.h);
 el('rect',{x:-262,y:316,width:524,height:36,rx:10,fill:'#C9D6D8'},o.h);o.h._x=540;
 o.mai=pillS(p,'MAI LAVORATO',440,40,'#0B4A50');
 o.mese=el('g',{},p);pillS(o.mese,'OGNI MESE',440,44,'url(#g_badge)');const cn=el('g',{transform:'translate(-190 0)'},o.mese);coin(cn,0,0,46);
 o.tasse=stamp(p,'SENZA TASSE',560,52,GRN);
 o.lui=hCard(p,470,250,'TUO MARITO');bust(o.lui,-150,10,.46,'#0B4A50','#9AA5A8');txt(o.lui,'PENSIONE',-50,2,38,INK,'bold','start');txt(o.lui,'NETTA',-50,52,34,'#5A6E73','bold','start');
 o.lk=hCard(p,470,250,'UNA CIFRA',RED);const lg=el('g',{transform:'translate(-132 38)'},o.lk);lockBig(lg,.72);txt(o.lk,'? €',92,64,92,RED,'bold');
 o.cap=capV(p,['UNA CIFRA DECIDE','QUANTO RICEVI']);return o;},
 update(t,o){const i=0;const a=plan(i,['Pensione alle casalinghe','non ha mai lavorato','ogni mese','senza pagare tasse','di tuo marito','una cifra','quanto ricevi']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.h,555,120);
  T(o.mai,285,965,0,pop(t,a[1]));T(o.mese,795,965,0,pop(t,a[2]));
  stampIn(t,o.tasse,a[3],540,1085,-3);
  T(o.lui,300,1290,0,pop(t,a[4]));T(o.lk,780,1290,0,pop(t,a[5]));
  T(o.cap,540,CAPY,0,pop(t,a[6]));}},
// ---- 2: coppia -> redditi di tutti e due -> netto -> BILANCIA ----
{D:DUR[1],build(p){const o={};head(p,o,'IN COPPIA',1);
 o.cp=hCard(p,940,300,'LE COPPIE');bust(o.cp,-360,-22,.46,'#C98500','#7A5230');txt(o.cp,'LEI',-360,134,30,INK,'bold');bust(o.cp,360,-22,.46,'#0B4A50','#9AA5A8');txt(o.cp,'LUI',360,134,30,INK,'bold');
 el('circle',{cx:0,cy:62,r:56,fill:'url(#g_badge)',stroke:'#fff','stroke-width':8},o.cp);txt(o.cp,'+',0,94,100,'#fff','bold');
 txt(o.cp,'I REDDITI DI TUTTI E DUE',0,-24,28,'#1B9F81','bold');o.cp._x=540;
 o.net=hCard(p,940,220,'QUELLO DI LUI');const nt=el('g',{transform:'translate(-300 34)'},o.net);note(nt,200,110);txt(nt,'PENSIONE',0,10,26,GRN,'bold');
 txt(o.net,'− TASSE',-60,44,64,RED,'bold','start');txt(o.net,'= AL NETTO',-60,92,38,INK,'bold','start');o.net._x=540;
 // bilancia
 o.sc=el('g',{},p);o.pole=el('g',{},o.sc);el('rect',{x:-14,y:-10,width:28,height:260,rx:10,fill:'url(#g_metal)'},o.pole);el('rect',{x:-130,y:238,width:260,height:26,rx:13,fill:'url(#g_metal)'},o.pole);
 o.beam=el('rect',{x:-330,y:-12,width:660,height:24,rx:12,fill:'url(#g_metal)',filter:'url(#g_sh2)'},o.sc);
 o.piv=el('circle',{r:26,fill:YEL,stroke:'#fff','stroke-width':6},o.sc);
 o.pl=[el('g',{},p),el('g',{},p)];
 o.pl.forEach((g,k)=>{el('line',{x1:-90,y1:0,x2:0,y2:-80,stroke:'#fff','stroke-width':4,'stroke-opacity':.8},g);el('line',{x1:90,y1:0,x2:0,y2:-80,stroke:'#fff','stroke-width':4,'stroke-opacity':.8},g);
  el('path',{d:'M-110 0 H110 Q100 44 0 44 Q-100 44 -110 0Z',fill:'url(#g_silver)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  txt(g,k==0?'LUI':'LEI',0,98,38,'#fff','bold');});
 o.c1=el('g',{},o.pl[0]);goldCoin(o.c1,0,-28,52,16,12);goldCoin(o.c1,-26,-14,52,16,12);
 o.cx=el('g',{},o.pl[0]);goldCoin(o.cx,26,-44,52,16,12);o.p1=pillS(o.pl[0],'+1 €',150,40,'url(#g_badge)');
 o.c2=el('g',{},o.pl[1]);goldCoin(o.c2,0,-28,52,16,12);goldCoin(o.c2,26,-14,52,16,12);
 o.m1=pillS(o.pl[1],'− 1 €',150,40,'url(#g_red)');
 o.cap=capV(p,['+1 € A LUI','= −1 € A TE']);return o;},
 update(t,o){const i=1;const a=plan(i,['per le coppie','di tutti e due','al netto delle tasse','ogni euro in più','un euro in meno']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.cp,470,110);rise(t,a[1]+.0,.9,o.net,790,100);
  const k=pop(t,a[2]);T(o.sc,540,1120,0,1);op(o.sc,seg(t,a[2],a[2]+.7));
  const tilt=8*eio(seg(t,a[3]+.3,a[3]+1.2))+6*eio(seg(t,a[4]+.3,a[4]+1.2));
  o.beam.setAttribute('transform','rotate('+(-tilt)+')');o.piv.setAttribute('transform','');
  const r=tilt*Math.PI/180,L=330;const lx=-L*Math.cos(r),ly=-L*Math.sin(r)*-1,rx=L*Math.cos(r),ry=L*Math.sin(r)*-1;
  o.pole.setAttribute('transform','');
  T(o.pl[0],540+lx,1120+ly+120,0,1);T(o.pl[1],540+rx,1120+ry+120,0,1);op(o.pl[0],seg(t,a[2]+.2,a[2]+.8));op(o.pl[1],seg(t,a[2]+.2,a[2]+.8));
  op(o.cx,seg(t,a[3],a[3]+.5));T(o.p1,0,-110,0,lerp(.4,1,sl(t,a[3]+.2)));op(o.p1,seg(t,a[3]+.2,a[3]+.6));T(o.m1,0,-110,0,lerp(.4,1,sl(t,a[4]+.2)));op(o.m1,seg(t,a[4]+.2,a[4]+.6));
  T(o.c2.children[1],0,0,0,1);op(o.c2.children[1],1-seg(t,a[4]+.2,a[4]+.8));
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 3: SCALE che scendono fino a zero, cifra nascosta ----
{D:DUR[2],build(p){const o={};head(p,o,'LA CIFRA',2);
 o.st=hCard(p,940,500,'L\'IMPORTO SCENDE');o.st._x=540;o.bars=[];
 [330,270,205,140,70].forEach((h,k)=>{const b=el('g',{},o.st);el('rect',{x:-370+k*150,y:210-h,width:130,height:h,rx:14,fill:k<3?'url(#g_head)':k<4?'url(#ty)':'url(#g_red)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh3)'},b);o.bars.push(b);});
 el('rect',{x:-390,y:206,width:780,height:8,rx:4,fill:'#C9D6D8'},o.st);
 o.zero=pillS(p,'0 €',190,60,'url(#g_red)');
 o.tu=el('g',{},p);pillS(o.tu,'TU: NESSUN ALTRO REDDITO',860,36,'#0B4A50');const avt=el('g',{transform:'translate(-392 0) scale(.5)'},o.tu);avatar(avt,'#C98500');
 o.lui=hCard(p,940,250,'QUANTO DEVE PRENDERE TUO MARITO');const lg=el('g',{transform:'translate(-300 40)'},o.lui);lockBig(lg,.8);txt(o.lui,'? €',60,76,130,RED,'bold');txt(o.lui,'NETTI',180,104,32,'#5A6E73','bold','start');o.lui._x=540;
 o.no=stamp(p,'NON LO DICIAMO QUI',760,44,RED);
 o.lin=el('g',{},p);el('line',{x1:0,y1:-215,x2:0,y2:215,stroke:RED,'stroke-width':8,'stroke-dasharray':'18 12','stroke-linecap':'round'},o.lin);
 o.cl=pillS(p,'LA CIFRA PRECISA',440,36,RED);
 o.cap=capV(p,['OLTRE QUELLA CIFRA','L\'AIUTO NON SPETTA PIÙ']);return o;},
 update(t,o){const i=2;const a=plan(i,['importo scende','a zero','altri redditi','quanto deve prendere','Non lo diciamo','una cifra precisa','oltre quella']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.st,520,100);o.bars.forEach((b,k)=>{const s=seg(t,a[0]+k*.18,a[0]+k*.18+.7);b.setAttribute('transform','translate(0 '+(210*(1-eo3(s)))+')');op(b,clamp(s*3));});
  T(o.zero,835,600,0,pop(t,a[1]));
  T(o.tu,540,950,0,pop(t,a[2]));rise(t,a[3],.9,o.lui,1140,90);
  stampIn(t,o.no,a[4],540,1345,-3);
  T(o.lin,760,560,0,1);op(o.lin,seg(t,a[5],a[5]+.9));T(o.cl,720,845,0,pop(t,a[5]));
  T(o.cap,540,CAPY,0,pop(t,a[6]));}},
// ---- 4: SPOSATA / VEDOVA affiancate ----
{D:DUR[3],build(p){const o={};head(p,o,'UN ALTRO CONTO',3);
 o.sp=hCard(p,450,470,'SPOSATA','#5A6E73');o.sp._x=290;bust(o.sp,-75,6,.5,'#C98500','#7A5230');bust(o.sp,75,6,.5,'#0B4A50','#9AA5A8');txt(o.sp,'IN DUE',0,205,34,'#5A6E73','bold');
 o.ve=hCard(p,450,470,'VEDOVA',GRN);o.ve._x=790;bust(o.ve,0,0,.62,'#3A4A4F','#9AA5A8');txt(o.ve,'DA SOLA',0,205,34,GRN,'bold');
 o.x=el('g',{},p);el('path',{d:'M-150 -150 L150 150 M150 -150 L-150 150',stroke:RED,'stroke-width':24,'stroke-linecap':'round',filter:'url(#g_sh2)'},o.x);
 o.ns=stamp(p,'NON PIÙ SPOSATA',560,44,RED);
 o.lim=hCard(p,940,230,'IL LIMITE');o.lim._x=540;const av=el('g',{transform:'translate(-370 32) scale(1.1)'},o.lim);avatar(av,GRN);
 txt(o.lim,'DI UNA PERSONA',-290,34,44,INK,'bold','start');txt(o.lim,'SOLA',-290,92,56,GRN,'bold','start');
 o.conta=el('g',{},p);pillS(o.conta,'CONTA COME REDDITO',640,38,'#0B4A50');const ck=el('g',{transform:'translate(-290 0)'},o.conta);check(ck,34,'#25D08C');
 o.noc=el('g',{},p);pillS(o.noc,'E COSA NO',460,38,RED);const cr=el('g',{transform:'translate(-190 0)'},o.noc);crossC(cr,34);
 o.cap=capV(p,['CAMBIA IL','RISULTATO?']);return o;},
 update(t,o){const i=3;const a=plan(i,['sei vedova','non sei più sposata','una persona sola','cosa conta','e cosa no','può cambiare']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.sp,540,100);rise(t,a[0]+.0,.9,o.ve,540,100);
  T(o.x,290,540,0,pop(t,a[1])*.9);stampIn(t,o.ns,a[1]+.1,540,880,-3);
  rise(t,a[2],.9,o.lim,1055,100);
  T(o.conta,540,1245,0,pop(t,a[3]));T(o.noc,540,1360,0,pop(t,a[4]));
  T(o.cap,540,CAPY,0,pop(t,a[5]));}},
// ---- 5: ASPETTARE costa: mesi, domanda, mesi non pagati ----
{D:DUR[4],build(p){const o={};head(p,o,'IL TEMPO',4);
 o.er=el('g',{},p);el('rect',{x:-470,y:-80,width:940,height:160,rx:40,fill:'#fff',stroke:RED,'stroke-width':8,filter:'url(#g_sh)'},o.er);
 const tr=el('g',{transform:'translate(-370 4)'},o.er);tri(tr,50);
 txt(o.er,'UN ERRORE CHE',-290,-8,42,INK,'bold','start');txt(o.er,'COSTA SOLDI: ASPETTARE',-290,48,46,RED,'bold','start');o.er._x=540;
 o.row=el('g',{},p);o.tiles=[];
 for(let k=0;k<6;k++){const g=el('g',{},o.row);const x=-450+k*150,w=138;
  const bg=el('rect',{x:x,y:-120,width:w,height:250,rx:26,fill:'#fff',stroke:'#9FB4B9','stroke-width':6,filter:'url(#g_sh2)'},g);
  el('rect',{x:x,y:-120,width:w,height:54,rx:22,fill:'#9FB4B9'},g);el('rect',{x:x,y:-90,width:w,height:24,fill:'#9FB4B9'},g);
  txt(g,'MESE',x+w/2,-82,30,'#fff','bold');const num=txt(g,String(k+1),x+w/2,34,88,'#9FB4B9','bold');
  const coinG=el('g',{opacity:0},g);const cc=el('g',{},coinG);coin(cc,x+w/2,86,30);
  const xx=el('g',{opacity:0},g);el('path',{d:`M${x+28} ${-20} L${x+w-28} ${90} M${x+w-28} ${-20} L${x+28} ${90}`,stroke:RED,'stroke-width':16,'stroke-linecap':'round'},xx);
  o.tiles.push({g,num,coinG,xx,bg});}
 o.row._x=540;
 o.br1=el('g',{},p);el('path',{d:'M-210 0 V26 H210 V0',fill:'none',stroke:'#FF8A75','stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'},o.br1);const l1=el('g',{transform:'translate(0 80)'},o.br1);pillL(l1,'PRIMA DELLA DOMANDA',440,26,RED);
 o.br2=el('g',{},p);el('path',{d:'M-210 0 V26 H210 V0',fill:'none',stroke:'#7FF0D2','stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'},o.br2);const l2=el('g',{transform:'translate(0 80)'},o.br2);pillL(l2,'DOPO LA DOMANDA',440,26,GRN);
 o.fl=el('g',{},p);el('rect',{x:-6,y:-170,width:12,height:330,rx:6,fill:'#0B3A3F'},o.fl);el('path',{d:'M6 -170 H266 L236 -126 L266 -82 H6Z',fill:'url(#g_red)',stroke:'#fff','stroke-width':5,'stroke-linejoin':'round'},o.fl);txt(o.fl,'DOMANDA',130,-111,34,'#fff','bold');
 o.pg=pillS(p,'DA QUI: PAGATO',400,38,'url(#g_badge)');
 o.np=stamp(p,'MESE NON PAGATO',460,40,RED);
 o.cap=capV(p,['OGNI MESE DI ATTESA','È UN MESE PERSO']);return o;},
 update(t,o){const i=4;const a=plan(i,['un errore che costa','dal mese dopo la domanda','ogni mese che passa','non ti viene pagato']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.er,470,100);
  rise(t,a[1]-.0,.9,o.row,830,100);
  o.tiles.forEach((tl,k)=>{const post=k>=3;const s=seg(t,a[1]+.3,a[1]+1.2);
   if(post){tl.bg.setAttribute('stroke',s>0.5?'#25D08C':'#9FB4B9');tl.num.setAttribute('fill',s>0.5?'#13805F':'#9FB4B9');op(tl.coinG,eo3(s));}
   else{const s2=seg(t,a[2],a[2]+.9);op(tl.xx,eo3(s2));tl.bg.setAttribute('stroke',s2>0.4?RED:'#9FB4B9');tl.num.setAttribute('fill',s2>0.4?RED:'#9FB4B9');}});
  T(o.fl,540-450+3*150-6,830-70,0,pop(t,a[1]+.2));
  T(o.br2,540+225,1010,0,pop(t,a[1]+.3));T(o.pg,540+240,1250,0,pop(t,a[1]+.3));
  T(o.br1,540-225,1010,0,pop(t,a[2]));stampIn(t,o.np,a[3],540-260,1250,-4);
  T(o.cap,540,CAPY,0,pop(t,a[4]));}},
// ---- 6: video correlato nel telefono, mi piace, iscriviti, manda a una donna ----
{D:DUR[5],build(p){const o={};head(p,o,'IL VIDEO',5);
 o.ph=el('g',{filter:'url(#g_sh)'},p);o.ph._x=540;
 el('rect',{x:-215,y:-370,width:430,height:740,rx:60,fill:'#0A1C1F',stroke:'#fff','stroke-width':8},o.ph);
 el('rect',{x:-190,y:-340,width:380,height:680,rx:40,fill:'url(#g_bg)'},o.ph);
 const hb=el('g',{},o.ph);el('rect',{x:-190,y:-340,width:380,height:210,rx:40,fill:'#0B4A50'},hb);el('rect',{x:-190,y:-230,width:380,height:100,fill:'#0B4A50'},hb);
 const lg=el('g',{transform:'translate(-110 -205)'},o.ph);lockBig(lg,.55);txt(o.ph,'? €',55,-172,84,YEL,'bold');
 const pl=el('g',{transform:'translate(0 -10)'},o.ph);el('rect',{x:-90,y:-60,width:180,height:120,rx:34,fill:'url(#g_red)',stroke:'#fff','stroke-width':7},pl);el('path',{d:'M-20 -30 L36 0 L-20 30Z',fill:'#fff'},pl);
 txt(o.ph,'VIDEO CORRELATO',0,150,32,'#fff','bold');el('rect',{x:-150,y:196,width:300,height:16,rx:8,fill:'#fff','fill-opacity':.5},o.ph);el('rect',{x:-150,y:240,width:210,height:16,rx:8,fill:'#fff','fill-opacity':.3},o.ph);
 o.ar=bigArrow(p);
 o.lk=el('g',{},p);el('rect',{x:-215,y:-46,width:430,height:92,rx:46,fill:'#0B4A50',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.lk);const th=el('g',{transform:'translate(-138 -4)'},o.lk);thumb(th,.34);txt(o.lk,'MI PIACE',40,15,42,'#fff','bold');
 o.sub=el('g',{},p);el('rect',{x:-215,y:-46,width:430,height:92,rx:46,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.sub);txt(o.sub,'ISCRIVITI',-20,15,42,'#fff','bold');const bb=el('g',{transform:'translate(150 -2)'},o.sub);bell(bb,.42);
 o.sh=hCard(p,940,190,'MANDALO A UNA DONNA');bust(o.sh,-340,-4,.4,'#C98500','#7A5230');
 el('path',{d:'M-210 40 H140 V6 L250 56 L140 106 V72 H-210Z',fill:YEL,stroke:'#fff','stroke-width':6,'stroke-linejoin':'round',transform:'translate(0 -6) scale(.9)'},o.sh);
 bust(o.sh,340,-4,.4,'#1B9F81','#5A6E73');o.sh._x=540;
 o.cap=capV(p,['MANDALO A UNA','DONNA CHE CONOSCI']);return o;},
 update(t,o){const i=5;const a=plan(i,['La cifra e il conto','qui sotto','Metti mi piace','iscriviti a','manda questo short']);PL[i]=a;headU(t,o);
  rise(t,a[0],.9,o.ph,628,110);
  T(o.ar,540,1055+14*Math.sin(t*5),0,pop(t,a[1])*.52);
  T(o.lk,290,1165,0,pop(t,a[2]));T(o.sub,790,1165,0,pop(t,a[3]));
  rise(t,a[4],.9,o.sh,1335,90);T(o.cap,540,CAPY,0,pop(t,a[5]));}},
];
S.forEach(s=>{s.sb=[{s:0,e:s.D}];});
