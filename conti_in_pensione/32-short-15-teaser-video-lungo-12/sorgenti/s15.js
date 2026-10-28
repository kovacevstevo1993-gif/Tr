// ===== SHORT 15: composizioni NUOVE in ogni blocco (libretto+tabella+decreto, tabella 15 righe, linea 1996, strisce dei mesi+gradini, telefono) =====
function thumbI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-96*s,y:-8*s,width:44*s,height:96*s,rx:10*s,fill:'#0B4A50',stroke:'#fff','stroke-width':6*s},g);
 el('path',{d:`M${-40*s} ${-4*s} L${-6*s} ${-78*s} Q${20*s} ${-96*s} ${32*s} ${-64*s} L${24*s} ${-26*s} H${86*s} Q${112*s} ${-24*s} ${104*s} ${8*s} L${92*s} ${62*s} Q${86*s} ${88*s} ${60*s} ${88*s} H${-40*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);return g;}
function bellI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
function personI(p,s,col){const g=el('g',{},p);col=col||'#0B4A50';el('circle',{cx:0,cy:-48*s,r:26*s,fill:col},g);el('path',{d:`M${-44*s} ${52*s} Q${-44*s} ${-12*s} 0 ${-12*s} Q${44*s} ${-12*s} ${44*s} ${52*s}Z`,fill:col},g);return g;}
function arrowD(p,x,y,w,h,col){return el('path',{d:`M${x-w/4} ${y-h/2} H${x+w/4} V${y} H${x+w/2} L${x} ${y+h/2} L${x-w/2} ${y} H${x-w/4}Z`,fill:col||RED,stroke:'#fff','stroke-width':5,'stroke-linejoin':'round'},p);}
function calcI(p,s){const g=el('g',{},p);el('rect',{x:-40*s,y:-52*s,width:80*s,height:104*s,rx:12*s,fill:'#0B4A50',stroke:'#fff','stroke-width':4},g);el('rect',{x:-30*s,y:-42*s,width:60*s,height:26*s,rx:5*s,fill:'#D6F5EC'},g);
 for(let r=0;r<3;r++)for(let c=0;c<3;c++)el('circle',{cx:(-20+c*20)*s,cy:(0+r*18)*s,r:6*s,fill:(r==2&&c==2)?AMB:'#7FF0D2'},g);return g;}
function clockI(p,s){const g=el('g',{},p);el('circle',{r:40*s,fill:'#fff',stroke:AMB,'stroke-width':8},g);el('line',{x1:0,y1:0,x2:0,y2:-26*s,stroke:NAVY,'stroke-width':7,'stroke-linecap':'round'},g);el('line',{x1:0,y1:0,x2:20*s,y2:10*s,stroke:NAVY,'stroke-width':7,'stroke-linecap':'round'},g);return g;}
function lenteI(p,s){const g=el('g',{},p);el('circle',{r:34*s,fill:'#fff','fill-opacity':.2,stroke:AMB,'stroke-width':10},g);el('line',{x1:24*s,y1:24*s,x2:62*s,y2:62*s,stroke:AMB,'stroke-width':13,'stroke-linecap':'round'},g);return g;}
const S=[
// ---- 1: libretto contributi + tabella coefficienti + decreto (da gennaio) + assegno che scende + "? €" + "rientri anche tu?" ----
{D:DUR[0],build(p){const o={};head(p,o,'COEFFICIENTI 2027',0);
 o.lib=scard(p,760,150,'url(#g_paper)',34);coin(o.lib,-290,4,52);txt(o.lib,'CONTRIBUTI',60,2,58,INK,'bold');txt(o.lib,'VERSATI',60,52,40,GRN,'bold');
 o.tb=scard(p,900,340,'url(#g_paper)',36);txt(o.tb,'COEFFICIENTI DI',0,-78,56,INK,'bold');txt(o.tb,'TRASFORMAZIONE',0,-14,56,GRN,'bold');
 el('rect',{x:-330,y:22,width:660,height:50,rx:10,fill:NAVY},o.tb);txt(o.tb,'ETÀ',-220,58,34,'#fff','bold');txt(o.tb,'COEFFICIENTE',130,58,34,'#fff','bold');
 [0,1].forEach(k=>{el('rect',{x:-330,y:78+k*40,width:660,height:36,rx:8,fill:k?'#E6F0F2':'#F3F8F9',stroke:'#C9D6D8','stroke-width':2},o.tb);el('rect',{x:-290,y:90+k*40,width:90,height:12,rx:6,fill:'#9FB4B9'},o.tb);el('rect',{x:70,y:90+k*40,width:200,height:12,rx:6,fill:'#9FB4B9'},o.tb);});
 o.dc=scard(p,860,190,'url(#g_paper)',34);const dl=txt(o.dc,'DECRETO DI OTTOBRE',0,-16,62,INK,'bold');el('rect',{x:-390,y:16,width:780,height:70,rx:35,fill:'url(#g_red)',stroke:'#fff','stroke-width':5},o.dc);txt(o.dc,'LI ABBASSA DA GENNAIO',0,64,40,'#fff','bold');
 o.as=el('g',{},p);el('rect',{x:-290,y:-70,width:580,height:140,rx:30,fill:NAVY,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},o.as);txt(o.as,"L'ASSEGNO",-70,22,56,'#fff','bold');arrowD(o.as,200,0,86,96,RED);
 o.pe=scard(p,330,140,'url(#g_paper)',30);txt(o.pe,'? €',0,34,88,ORG,'bold');
 o.ri=pillS(p,'RIENTRI ANCHE TU?',760,46,'#0B4A50');
 o.cap=capN(p,['QUANTO POTRESTI PERDERE?','RIENTRI ANCHE TU?']);return o;},
 update(t,o){const i=0;const a=plan(i,['versato contributi','coefficienti di trasformazione','decreto di ottobre',"l'assegno",'Quanto potresti perdere','rientri anche tu']);PL[i]=a;headU(t,o);bgx(t);
  fade(t,o.lib,540,440,a[0]);fade(t,o.tb,540,745,a[1]);fade(t,o.dc,540,1055,a[2]);fade(t,o.as,330,1240,a[3]);fade(t,o.pe,800,1240,a[4]);T(o.ri,540,1385,0,pop(t,a[5]));rise(t,a[6],.9,o.cap,1590,100);}},
// ---- 2: decreto 16 ottobre + tabella di 15 righe (eta' 57-71) + barre prima/2027 + differenza in euro + due tuoi numeri ----
{D:DUR[1],build(p){const o={};head(p,o,'COEFFICIENTI 2027',1);
 o.dt=scard(p,780,110,'url(#g_paper)',30);txt(o.dt,'DECRETO · 16 OTTOBRE',0,22,50,INK,'bold');
 o.tb=scard(p,920,790,'url(#g_paper)',30);el('rect',{x:-440,y:-345,width:880,height:56,rx:12,fill:NAVY},o.tb);txt(o.tb,'ETÀ',-370,-306,32,'#fff','bold','start');el('rect',{x:-60,y:-333,width:28,height:28,rx:6,fill:'#25C48A'},o.tb);txt(o.tb,'PRIMA',-20,-306,30,'#fff','bold','start');
 o.rw=[];for(let k=0;k<15;k++){const y=-281+k*46;el('rect',{x:-440,y:y,width:880,height:44,rx:6,fill:k%2?'#E6F0F2':'#F8FBFB'},o.tb);txt(o.tb,String(57+k),-370,y+33,32,INK,'bold','start');el('rect',{x:-210,y:y+10,width:420+k*3,height:24,rx:12,fill:'#25C48A'},o.tb);}
 el('path',{d:'M452 -281 Q474 -281 474 -259 V 387 Q474 409 452 409',fill:'none',stroke:AMB,'stroke-width':8,'stroke-linecap':'round'},o.tb);txt(o.tb,'15',474,60,44,AMB,'bold');o.tb.setAttribute('data-x','1');
 o.hi=el('g',{},p);[0,14].forEach(k=>el('rect',{x:-450,y:-283+k*46,width:900,height:48,rx:12,fill:'none',stroke:AMB,'stroke-width':7},o.hi));
 o.l2=el('g',{},p);el('rect',{x:160,y:-333,width:28,height:28,rx:6,fill:ORG},o.l2);txt(o.l2,'2027',200,-306,30,'#fff','bold','start');for(let k=0;k<15;k++){const y=-281+k*46;el('rect',{x:-210,y:y+10,width:420+k*3-36-(k%4)*2,height:24,rx:12,fill:ORG,stroke:'#fff','stroke-width':2},o.l2);}
 o.eu=pillS(p,'QUANTO VALE IN EURO LA DIFFERENZA?',960,36,'#0B4A50');
 o.ch=el('g',{},p);[-250,250].forEach((x,k)=>{const c=pillS(o.ch,'TUO NUMERO '+(k+1)+'  ?',440,38,k?ORG:GRN);T(c,x,0,0,1);});
 o.cap=capN(p,['NUMERO PIÙ BASSO IN OGNI RIGA','QUANTO VALE? DIPENDE DA TE']);return o;},
 update(t,o){const i=1;const a=plan(i,['sedici ottobre','tabella di quindici righe','dai cinquantasette','più basso di prima','Quanto vale in euro','due tuoi numeri']);PL[i]=a;headU(t,o);bgx(t);
  fade(t,o.dt,540,395,a[0]);fade(t,o.tb,540,872,a[1]);
  T(o.hi,540,872,0,1);op(o.hi,seg(t,a[2],a[2]+.6));T(o.l2,540,872,0,1);op(o.l2,seg(t,a[3],a[3]+.9));
  T(o.eu,540,1335,0,pop(t,a[4]));T(o.ch,540,1425,0,pop(t,a[5]));rise(t,a[6],.9,o.cap,1610,100);}},
// ---- 3: non riguarda chiunque + gia' in pensione FUORI + linea 1996 con parte dei contributi + quale parte? + un dato da controllare ----
{D:DUR[2],build(p){const o={};head(p,o,'COEFFICIENTI 2027',2);
 o.ch=pillS(p,'NON RIGUARDA CHIUNQUE',860,48,'#0B4A50');
 o.pe=scard(p,880,230,'url(#g_paper)',34);const pi=personI(o.pe,1.5);T(pi,-350,6,0,1);txt(o.pe,'GIÀ IN',-250,-10,56,INK,'bold','start');txt(o.pe,'PENSIONE',-250,58,56,INK,'bold','start');
 o.fu=stamp(p,'FUORI',300,64,RED);
 o.tl=scard(p,940,350,'url(#g_paper)',34);txt(o.tl,'HAI INIZIATO A LAVORARE',0,-122,40,INK,'bold');
 el('rect',{x:-400,y:-20,width:400,height:70,rx:16,fill:'#9FB4B9'},o.tl);el('rect',{x:0,y:-20,width:400,height:70,rx:16,fill:'#25C48A'},o.tl);
 el('line',{x1:0,y1:-46,x2:0,y2:62,stroke:RED,'stroke-width':8},o.tl);const yy=pillS(o.tl,'1996',170,38,RED);T(yy,0,-72,0,1);txt(o.tl,'PRIMA',-200,28,40,'#fff','bold');txt(o.tl,'DOPO',200,28,40,'#fff','bold');
 o.un=el('g',{},p);el('rect',{x:-4,y:-38,width:410,height:98,rx:18,fill:'none',stroke:AMB,'stroke-width':8,'stroke-dasharray':'16 10'},o.un);const up=pillS(o.un,'UNA PARTE DEI CONTRIBUTI',640,32,GRN);T(up,140,118,0,1);
 o.qu=pillS(p,'QUALE PARTE?',520,50,ORG);
 o.da=el('g',{},p);const dp=pillS(o.da,'UN DATO DA CONTROLLARE',740,40,'#0B4A50');T(dp,30,0,0,1);const le=lenteI(o.da,.9);T(le,-400,-6,0,1);
 o.cap=capN(p,['COSA CONTA DEL TUO LAVORO?','UN DATO DA CONTROLLARE']);return o;},
 update(t,o){const i=2;const a=plan(i,['Non riguarda chiunque','già in pensione','resta fuori','prima del novantasei','una parte dei contributi','Quale parte','un dato che devi controllare']);PL[i]=a;headU(t,o);bgx(t);
  T(o.ch,540,420,0,pop(t,a[0]));fade(t,o.pe,540,640,a[1]);stampIn(t,o.fu,a[2],790,655,-6);
  fade(t,o.tl,540,985,a[3]);T(o.un,540,985,0,1);op(o.un,seg(t,a[4],a[4]+.7));T(o.qu,540,1275,0,pop(t,a[5]));T(o.da,540,1395,0,pop(t,a[6]));rise(t,a[7],.9,o.cap,1610,100);}},
// ---- 4: un conto + striscia dei mesi "?" + andare in pensione + gradino coefficiente (2027 -> di prima) + barre eta' per eta' + quasi lo stesso + nel video ----
{D:DUR[3],build(p){const o={};head(p,o,'COEFFICIENTI 2027',3);
 o.cn=scard(p,560,130,'url(#g_paper)',30);const ci=calcI(o.cn,1.1);T(ci,-190,0,0,1);txt(o.cn,'UN CONTO',60,24,58,INK,'bold');
 o.ms=el('g',{},p);el('rect',{x:-480,y:-62,width:960,height:124,rx:26,fill:NAVY,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},o.ms);
 for(let k=0;k<12;k++){el('rect',{x:-456+k*76,y:-40,width:68,height:80,rx:12,fill:k<6?'#F5FBFA':'#C9E6E0'},o.ms);txt(o.ms,'?',-422+k*76,22,54,k<6?ORG:'#6F878C','bold');}
 txt(o.ms,'MESI IN PIÙ',0,-80,38,AMB,'bold');
 o.pn=el('g',{},p);const pp=pillS(o.pn,'ANDARE IN PENSIONE',640,40,GRN);T(pp,0,0,0,1);el('path',{d:'M-26 -64 H26 L0 -96Z',fill:GRN,stroke:'#fff','stroke-width':4,'stroke-linejoin':'round'},o.pn);
 o.gr=scard(p,900,250,'url(#g_paper)',30);el('rect',{x:-380,y:30,width:300,height:70,rx:8,fill:ORG},o.gr);txt(o.gr,'2027',-230,80,40,'#fff','bold');el('rect',{x:80,y:-40,width:300,height:140,rx:8,fill:'#25C48A'},o.gr);txt(o.gr,'DI PRIMA',230,60,40,'#fff','bold');
 el('path',{d:'M-60 50 Q0 50 0 0 Q0 -54 52 -54',fill:'none',stroke:AMB,'stroke-width':10,'stroke-linecap':'round'},o.gr);el('path',{d:'M40 -78 L80 -54 L40 -30Z',fill:AMB},o.gr);txt(o.gr,'IL COEFFICIENTE',0,-70,34,INK,'bold');
 o.br=scard(p,900,230,'url(#g_paper)',30);for(let k=0;k<14;k++){const h=96+((k*7)%3)*5;el('rect',{x:-410+k*60,y:92-h,width:46,height:h,rx:8,fill:k%2?GRN:'#25C48A'},o.br);}txt(o.br,'ETÀ PER ETÀ',0,-52,36,INK,'bold');
 o.qs=pillS(p,'QUASI LO STESSO',560,46,ORG);
 o.vd=el('g',{},p);const vp=pillS(o.vd,'QUANTI MESI? NEL VIDEO',780,42,'#0B4A50');T(vp,30,0,0,1);el('circle',{cx:-400,cy:0,r:40,fill:RED,stroke:'#fff','stroke-width':5},o.vd);el('path',{d:'M-412 -18 L-382 0 L-412 18Z',fill:'#fff'},o.vd);
 o.cap=capN(p,['QUANTI MESI PER TORNARE','AL COEFFICIENTE DI PRIMA?']);return o;},
 update(t,o){const i=3;const a=plan(i,['un conto','quanti mesi in più','andare in pensione','tornare al coefficiente','età per età','quasi lo stesso','Lo scopri nel video']);PL[i]=a;headU(t,o);bgx(t);
  fade(t,o.cn,540,425,a[0]);fade(t,o.ms,540,595,a[1]);T(o.pn,540,745,0,pop(t,a[2]));fade(t,o.gr,540,940,a[3]);fade(t,o.br,540,1220,a[4]);T(o.qs,540,1340,0,pop(t,a[5]));T(o.vd,540,1430,0,pop(t,a[6]));rise(t,a[7],.9,o.cap,1620,100);}},
// ---- 5: telefono con il video correlato + 3 esempi + conto dei mesi + tocca + meno di 6 minuti + dal 2027 controlla + mi piace + iscriviti ----
{D:DUR[4],build(p){const o={};head(p,o,'COEFFICIENTI 2027',4);
 o.ph=el('g',{},p);el('rect',{x:-200,y:-350,width:400,height:700,rx:50,fill:'#0A1E22',stroke:'#fff','stroke-width':8,filter:'url(#g_sh)'},o.ph);el('rect',{x:-176,y:-310,width:352,height:620,rx:26,fill:'#12363C'},o.ph);
 el('rect',{x:-160,y:-280,width:320,height:200,rx:18,fill:'url(#g_red)'},o.ph);el('path',{d:'M-30 -240 L50 -180 L-30 -120Z',fill:'#fff'},o.ph);
 [0,1,2].forEach(k=>el('rect',{x:-160,y:-50+k*60,width:k==2?200:320,height:22,rx:11,fill:'#2A7A82'},o.ph));txt(o.ph,'VIDEO',0,170,44,AMB,'bold');txt(o.ph,'CORRELATO',0,222,44,AMB,'bold');
 o.c1=pillS(p,'3 ESEMPI IN EURO',460,38,GRN);o.c2=pillS(p,'CONTO DEI MESI',460,38,ORG);
 o.tp=el('g',{},p);el('rect',{x:-230,y:-80,width:460,height:160,rx:34,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.tp);txt(o.tp,'TOCCA IL VIDEO',0,-8,40,'#fff','bold');txt(o.tp,'QUI SOTTO ▼',0,46,44,'#fff','bold');
 o.tm=el('g',{},p);el('rect',{x:-230,y:-56,width:460,height:112,rx:30,fill:NAVY,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},o.tm);const ck=clockI(o.tm,.9);T(ck,-170,0,0,1);txt(o.tm,'MENO DI',60,-6,32,'#7FF0D2','bold');txt(o.tm,'6 MINUTI',60,36,44,'#fff','bold');
 o.ck=scard(p,940,130,'url(#g_paper)',30);el('circle',{cx:-405,cy:6,r:38,fill:'#25C48A',stroke:'#fff','stroke-width':4},o.ck);el('path',{d:'M-423 6 L-409 22 L-383 -10',fill:'none',stroke:'#fff','stroke-width':9,'stroke-linecap':'round','stroke-linejoin':'round'},o.ck);txt(o.ck,'DAL 2027: CONTROLLA SE RIENTRI',50,24,36,INK,'bold');
 o.li=el('g',{},p);el('circle',{r:62,fill:NAVY,stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.li);const th=thumbI(o.li,.55);th.setAttribute('transform','translate(-6 -2)');
 o.is=el('g',{},p);el('rect',{x:-250,y:-58,width:500,height:116,rx:58,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.is);txt(o.is,'ISCRIVITI',-20,19,52,'#fff','bold');const be=bellI(o.is,.55);T(be,196,0,0,1);
 o.cap=capN(p,['TOCCA IL VIDEO CORRELATO','METTI MI PIACE E ISCRIVITI']);return o;},
 update(t,o){const i=4;const a=plan(i,['tre esempi in euro','conto dei mesi','tocca il video correlato','meno di sei minuti','dal duemilaventisette','un mi piace','iscriviti a Conti']);PL[i]=a;headU(t,o);bgx(t);
  fade(t,o.ph,300,800,a[0]);T(o.c1,790,545,0,pop(t,a[0]));T(o.c2,790,675,0,pop(t,a[1]));
  T(o.tp,790,850,0,pop(t,a[2]));T(o.tm,790,1010,0,pop(t,a[3]));fade(t,o.ck,540,1250,a[4]);T(o.li,250,1390,0,pop(t,a[5]));T(o.is,700,1390,0,pop(t,a[6]));rise(t,a[7],.9,o.cap,1600,100);}},
];
