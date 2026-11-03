// ===== SHORT 17: composizioni NUOVE in ogni blocco (pensione+forbici, 4 schede anagrafiche, reddito+scalinata, scudo, 3 situazioni, commento+telefono) =====
function personI(p,s,col){const g=el('g',{},p);col=col||'#0B4A50';el('circle',{cx:0,cy:-30*s,r:20*s,fill:col},g);el('path',{d:`M${-34*s} ${40*s} Q${-34*s} ${-4*s} 0 ${-4*s} Q${34*s} ${-4*s} ${34*s} ${40*s}Z`,fill:col},g);return g;}
function thumbI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('rect',{x:-96*s,y:-8*s,width:44*s,height:96*s,rx:10*s,fill:'#0B4A50',stroke:'#fff','stroke-width':6*s},g);
 el('path',{d:`M${-40*s} ${-4*s} L${-6*s} ${-78*s} Q${20*s} ${-96*s} ${32*s} ${-64*s} L${24*s} ${-26*s} H${86*s} Q${112*s} ${-24*s} ${104*s} ${8*s} L${92*s} ${62*s} Q${86*s} ${88*s} ${60*s} ${88*s} H${-40*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);return g;}
function bellI(p,s){const g=el('g',{filter:'url(#g_sh2)'},p);
 el('path',{d:`M${-70*s} ${50*s} Q${-60*s} ${30*s} ${-60*s} ${-10*s} Q${-60*s} ${-70*s} 0 ${-76*s} Q${60*s} ${-70*s} ${60*s} ${-10*s} Q${60*s} ${30*s} ${70*s} ${50*s}Z`,fill:YEL,stroke:'#fff','stroke-width':7*s,'stroke-linejoin':'round'},g);
 el('circle',{cx:0,cy:68*s,r:16*s,fill:YEL,stroke:'#fff','stroke-width':5*s},g);return g;}
// forbici (puntano a destra, perno in 0,0): due meta' che si aprono/chiudono
function scissorsI(p){const g=el('g',{filter:'url(#g_sh2)'},p);const mk=()=>{const h=el('g',{},g);
 el('path',{d:'M0 -10 L205 -1 L205 3 L0 12 Z',fill:'url(#g_silver)',stroke:'#5B7378','stroke-width':3,'stroke-linejoin':'round'},h);
 el('line',{x1:-34,y1:0,x2:0,y2:0,stroke:ORG,'stroke-width':13,'stroke-linecap':'round'},h);
 el('circle',{cx:-68,cy:0,r:34,fill:'none',stroke:ORG,'stroke-width':13},h);return h;};
 const a=mk(),b=mk();el('circle',{r:11,fill:'#33464A',stroke:'#fff','stroke-width':3},g);return {g,a,b};}
function snip(sc,th){sc.a.setAttribute('transform','rotate('+th+')');sc.b.setAttribute('transform','rotate('+(-th)+')');}
function shieldI(p,s){const g=el('g',{filter:'url(#g_sh)'},p);
 el('path',{d:`M0 ${-145*s} L${125*s} ${-100*s} V${15*s} Q${125*s} ${105*s} 0 ${155*s} Q${-125*s} ${105*s} ${-125*s} ${15*s} V${-100*s}Z`,fill:'url(#g_badge)',stroke:'#fff','stroke-width':9,'stroke-linejoin':'round'},g);
 el('path',{d:`M${-52*s} ${5*s} L${-14*s} ${45*s} L${58*s} ${-40*s}`,fill:'none',stroke:'#fff','stroke-width':22*s,'stroke-linecap':'round','stroke-linejoin':'round'},g);return g;}
function gearI(p,R){const g=el('g',{},p);const n=10;let d='';
 for(let k=0;k<n;k++){const a0=k*2*Math.PI/n,w=Math.PI/n*.55,w2=Math.PI/n*.8;
  [[a0-w2,R*.76],[a0-w,R],[a0+w,R],[a0+w2,R*.76]].forEach(([a,r],j)=>{d+=(k+j==0?'M':'L')+(r*Math.cos(a)).toFixed(1)+' '+(r*Math.sin(a)).toFixed(1)+' ';});}
 el('path',{d:d+'Z',fill:AMB,stroke:'#fff','stroke-width':6,'stroke-linejoin':'round',filter:'url(#g_sh2)'},g);el('circle',{r:R*.32,fill:'#0D5158',stroke:'#fff','stroke-width':5},g);return g;}
function lockI(p,s){const g=el('g',{},p);el('path',{d:`M${-24*s} ${-6*s} V${-26*s} a${24*s} ${24*s} 0 0 1 ${48*s} 0 V${-6*s}`,fill:'none',stroke:'#fff','stroke-width':10*s,'stroke-linecap':'round'},g);
 el('rect',{x:-36*s,y:-8*s,width:72*s,height:56*s,rx:12*s,fill:AMB,stroke:NAVY,'stroke-width':4},g);el('circle',{cx:0,cy:18*s,r:7*s,fill:NAVY},g);return g;}
function handI(p){const g=el('g',{filter:'url(#g_sh2)'},p);const st={fill:SKIN,stroke:'#C9946B','stroke-width':4};
 el('rect',Object.assign({x:-50,y:30,width:100,height:100,rx:30},st),g);
 [[28,0,'rect'],[-50,20,'rect']].forEach(()=>0);
 el('rect',Object.assign({x:24,y:20,width:26,height:64,rx:13},st),g);el('rect',Object.assign({x:-50,y:24,width:26,height:56,rx:13},st),g);el('rect',Object.assign({x:-10,y:14,width:26,height:70,rx:13},st),g);
 el('rect',Object.assign({x:-26,y:-62,width:34,height:140,rx:17},st),g);return g;}
const hid=(g,k)=>g;
const S=[
// ---- 1: cedolino di pensione con pezzo tagliato dalle forbici (INPS) + coppia (uno spento) + due domande + modulo "domanda" ----
{D:DUR[0],build(p){const o={};head(p,o,'IL TAGLIO');
 o.pc=el('g',{},p);plateRect(o.pc,-430,-115,760,230,26);coin(o.pc,-310,0,78);
 fit(o.pc,'PENSIONE DI',60,-22,38,GRN,360);fit(o.pc,'REVERSIBILITÀ',60,50,58,INK,400);
 el('line',{x1:335,y1:-120,x2:335,y2:120,stroke:RED,'stroke-width':6,'stroke-dasharray':'14 10'},o.pc);
 o.pp=el('g',{},p);el('rect',{x:-45,y:-115,width:90,height:230,rx:18,fill:'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh)'},o.pp);
 el('line',{x1:-45,y1:-115,x2:-45,y2:115,stroke:RED,'stroke-width':6,'stroke-dasharray':'14 10'},o.pp);
 el('rect',{x:-22,y:-70,width:44,height:14,rx:7,fill:'#B5C6C9'},o.pp);el('rect',{x:-22,y:-30,width:30,height:14,rx:7,fill:'#B5C6C9'},o.pp);
 o.sw=el('g',{},p);o.sc=scissorsI(o.sw);o.sc.g.setAttribute('transform','rotate(90)');
 o.ip=pillS(p,'INPS',220,40,RED);
 o.cp=el('g',{},p);[-150,150].forEach((x,k)=>{const g=el('g',{transform:'translate('+x+' 0)'},o.cp);
  el('circle',{r:92,fill:k?'#fff':'#9FB4B9',stroke:k?'#fff':'#5B7378','stroke-width':6,'stroke-dasharray':k?'':'12 9',filter:'url(#g_sh2)'},g);
  const q=personI(g,1.5,k?'#0B4A50':'#5B7378');q.setAttribute('transform','translate(0 12)');});
 {const pl=pillS(o.cp,'DOPO LA MORTE DEL CONIUGE',820,32,NAVY);T(pl,0,150,0,1);}
 o.q1=pillS(p,'IN QUALI CASI?',470,42,ORG);o.q2=pillS(p,'DI QUANTO?',420,42,GRN);
 o.fm=el('g',{},p);el('rect',{x:-380,y:-120,width:760,height:240,rx:22,fill:'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh)'},o.fm);
 el('path',{d:'M-380 -50 V-98 Q-380 -120 -358 -120 H358 Q380 -120 380 -98 V-50Z',fill:GRN},o.fm);fit(o.fm,'DOMANDA',0,-62,44,'#fff',500);
 [[-340,-18,260],[-340,22,200]].forEach(([x,y,w])=>el('rect',{x:x,y:y,width:w,height:14,rx:7,fill:'#B5C6C9'},o.fm));
 el('rect',{x:-340,y:70,width:36,height:36,rx:8,fill:'none',stroke:'#9FB4B9','stroke-width':4},o.fm);el('line',{x1:-280,y1:96,x2:-60,y2:96,stroke:'#9FB4B9','stroke-width':4},o.fm);
 {const rb=pillS(o.fm,'SAPERLO PRIMA',380,32,ORG);T(rb,170,50,0,1);}
 o.cap=strip(p,['PUÒ ESSERE TAGLIATA DALL\'INPS','IN QUALI CASI? DI QUANTO?']);return o;},
 update(t,o){const a=plan(0,['La pensione di reversibilità','dopo la morte del coniuge','può essere tagliata','In quali casi','e di quanto','Meglio saperlo']);PL[0]=a;headU(t,o);bgx(t);
  fade(t,o.pc,540,470,a[0]);
  const k=sl(t,a[2],1.2),y0=(1-sl(t,a[0],.9))*60;T(o.pp,925+12*k,470+y0+16*k,7*k,1);op(o.pp,seg(t,a[0],a[0]+.55));
  op(o.pc.lastChild,seg(t,a[2],a[2]+.5));
  T(o.sw,875,352,0,pop(t,a[2]));const A=Math.max(0,1-(t-a[2])/3.0);snip(o.sc,5+(t>a[2]?A*11*(.5+.5*Math.sin((t-a[2])*8)):0));
  T(o.ip,690,300,0,pop(t,a[2]+.1));
  T(o.cp,540,770,0,pop(t,a[1]));
  T(o.q1,290,1050,0,pop(t,a[3]));T(o.q2,800,1050,0,pop(t,a[4]));
  fade(t,o.fm,540,1290,a[5]);rise(t,a[6],.9,o.cap,1560,100);}},
// ---- 2: quattro schede anagrafiche (coniuge, figli, genitori, fratelli e sorelle) con "? %" + percentuale + condizioni ----
{D:DUR[1],build(p){const o={};head(p,o,'CHI HA DIRITTO');
 o.qb=pillS(p,'QUANTO SPETTA A CHI RESTA?',900,40,GRN);
 o.cd=[['CONIUGE',GRN,'one'],['FIGLI',ORG,'kid'],['GENITORI','#2A7A82','x2'],['FRATELLI E SORELLE','#6B5BB0','x2']].map(d=>idCard(p,450,320,d[0],d[1],d[2]));
 o.pc=el('g',{},p);el('rect',{x:-460,y:-65,width:920,height:130,rx:24,fill:NAVY,stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},o.pc);
 {const pie=el('g',{transform:'translate(-390 0)'},o.pc);el('circle',{r:42,fill:'#fff'},pie);el('path',{d:'M0 0 L0 -42 A42 42 0 1 1 -42 0Z',fill:ORG},pie);}
 fit(o.pc,'LA PERCENTUALE CAMBIA',40,-6,46,'#fff',700);fit(o.pc,'A SECONDA DI CHI SEI',40,38,32,AMB,700);
 o.cn=el('g',{},p);{const pl=pillS(o.cn,'A QUALI CONDIZIONI?',640,44,ORG);T(pl,110,0,0,1);
  const ck=el('g',{transform:'translate(-330 0)'},o.cn);el('rect',{x:-48,y:-56,width:96,height:112,rx:12,fill:'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},ck);
  [-24,22].forEach(y=>{el('path',{d:`M-30 ${y} l9 10 l17 -20`,fill:'none',stroke:GRN,'stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'},ck);el('rect',{x:0,y:y-6,width:30,height:10,rx:5,fill:'#B5C6C9'},ck);});}
 o.cap=strip(p,['NON SOLO IL CONIUGE','CHI HA DIRITTO, E A QUANTO?']);return o;},
 update(t,o){const a=plan(1,['E quanto spetta','Il coniuge','anche i figli','i genitori','i fratelli','La percentuale','Quali percentuali']);PL[1]=a;headU(t,o);bgx(t);
  T(o.qb,540,330,0,pop(t,a[0]));
  const P=[[285,570,-70],[795,570,70],[285,930,-70],[795,930,70]];
  o.cd.forEach((c,k)=>slideX(t,c,P[k][0],P[k][1],a[1+k],P[k][2]));
  fade(t,o.pc,540,1180,a[5]);fade(t,o.cn,540,1345,a[6]);rise(t,a[7],.9,o.cap,1560,100);}},
// ---- 3: cartellina reddito (voci che contano / non contano) + "quali?" + scalinata di soglie "? €" + riduzione + calendario gennaio + 2026 ----
{D:DUR[2],build(p){const o={};head(p,o,'IL REDDITO');
 o.fo=el('g',{},p);folder(o.fo,880,400,'REDDITO',GRN);
 o.rw=[];for(let k=0;k<5;k++){const y=-150+k*75;const r={y};
  el('circle',{cx:-390,cy:y,r:16,fill:AMB},o.fo);el('rect',{x:-350,y:y-9,width:250+(k%3)*40,height:18,rx:9,fill:'#B5C6C9'},o.fo);el('rect',{x:20,y:y-9,width:130,height:18,rx:9,fill:'#B5C6C9'},o.fo);
  if(k<4)el('line',{x1:-410,y1:y+37,x2:410,y2:y+37,stroke:'#DCE7EA','stroke-width':3},o.fo);
  r.tick=el('g',{transform:'translate(320 '+y+')'},o.fo);el('circle',{r:22,fill:'#25C48A'},r.tick);el('path',{d:'M-10 0 l8 9 l14 -17',fill:'none',stroke:'#fff','stroke-width':6,'stroke-linecap':'round','stroke-linejoin':'round'},r.tick);
  if(k==1||k==3){r.st=el('line',{x1:-410,y1:y,x2:-410,y2:y,stroke:RED,'stroke-width':8,'stroke-linecap':'round'},o.fo);r.tag=pillS(o.fo,'NON CONTA',230,27,RED);T(r.tag,310,y,0,0);}
  o.rw.push(r);}
 o.qu=pillS(p,'QUALI?',250,40,ORG);
 o.sg=el('g',{},p);[[-280,110,'#2A7A82'],[0,220,GRN],[280,330,DK]].forEach(([x,h,c])=>{const b=el('g',{},o.sg);
  el('rect',{x:x-140,y:-h,width:280,height:h,rx:14,fill:c,stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},b);fit(b,'? €',x,-h+78,58,'#fff',200);});
 o.rd=pillS(p,'RIDUZIONE ▼',340,36,RED);
 o.cl=el('g',{},p);el('rect',{x:-150,y:-100,width:300,height:200,rx:20,fill:'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh)'},o.cl);
 el('path',{d:'M-150 -40 V-80 Q-150 -100 -130 -100 H130 Q150 -100 150 -80 V-40Z',fill:RED},o.cl);fit(o.cl,'GENNAIO',0,-52,38,'#fff',250);
 for(let r=0;r<2;r++)for(let c=0;c<6;c++)el('rect',{x:-112+c*40,y:-14+r*40,width:26,height:26,rx:6,fill:(r==0&&c==0)?ORG:'#DCE7EA'},o.cl);
 el('path',{d:'M-90 74 H70 M50 58 L70 74 L50 90',fill:'none',stroke:GRN,'stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'},o.cl);
 o.yr=el('g',{},p);el('rect',{x:-260,y:-100,width:520,height:200,rx:24,fill:AMB,stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.yr);fit(o.yr,'2026',0,10,100,NAVY,400);fit(o.yr,'NEL VIDEO',0,72,38,NAVY,400);
 o.cap=strip(p,['QUALI REDDITI CONTANO?','LE SOGLIE CAMBIANO A GENNAIO']);return o;},
 update(t,o){const a=plan(2,['un reddito','alcune voci','Quali?','da quali cifre','la riduzione','ogni gennaio','del duemilaventisei']);PL[2]=a;headU(t,o);bgx(t);
  fade(t,o.fo,540,570,a[0]);
  const e1=seg(t,a[1],a[1]+.9);o.rw.forEach((r,k)=>{if(r.st){r.st.setAttribute('x2',-410+830*eo3(e1));op(r.tick,1-seg(t,a[1]+.2,a[1]+.5));T(r.tag,310,r.y,0,pop(t,a[1]+.35));}});
  T(o.qu,820,305,0,pop(t,a[2]));
  fade(t,o.sg,540,1190,a[3]);o.sg.setAttribute('opacity',seg(t,a[3],a[3]+.55));
  T(o.rd,300,912,0,pop(t,a[4]));
  fade(t,o.cl,270,1335,a[5]);slideX(t,o.yr,700,1335,a[6],90);rise(t,a[7],.9,o.cap,1560,100);}},
// ---- 4: scudo che ferma le forbici + reddito alto + caso nascosto "?" + ingranaggio "cambia i conti" + "alla fine del video" ----
{D:DUR[3],build(p){const o={};head(p,o,'NIENTE TAGLIO');
 o.sh=el('g',{},p);shieldI(o.sh,1.1);{const sc=scissorsI(o.sh);o.sx=sc;sc.g.setAttribute('transform','translate(400 0) rotate(180)');
  const x=el('g',{transform:'translate(190 -70)'},o.sh);el('circle',{r:34,fill:RED,stroke:'#fff','stroke-width':5},x);el('path',{d:'M-14 -14 L14 14 M14 -14 L-14 14',stroke:'#fff','stroke-width':8,'stroke-linecap':'round'},x);}
 {const pl=pillS(o.sh,'IL TAGLIO NON SCATTA',640,34,GRN);T(pl,60,215,0,1);}
 o.ch=el('g',{},p);el('rect',{x:-440,y:-125,width:880,height:250,rx:24,fill:'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh)'},o.ch);fit(o.ch,'REDDITO ALTO',-200,14,50,INK,420);
 el('line',{x1:90,y1:80,x2:410,y2:80,stroke:'#9FB4B9','stroke-width':5},o.ch);
 [[130,60,'#B5C6C9'],[230,110,'#7FB3BA'],[330,190,ORG]].forEach(([x,h,c])=>el('rect',{x:x,y:80-h,width:70,height:h,rx:8,fill:c},o.ch));
 el('path',{d:'M365 -70 V-112 M349 -96 L365 -112 L381 -96',fill:'none',stroke:ORG,'stroke-width':7,'stroke-linecap':'round','stroke-linejoin':'round'},o.ch);
 o.cs=el('g',{},p);el('rect',{x:-440,y:-65,width:880,height:130,rx:24,fill:NAVY,stroke:'#fff','stroke-width':4,filter:'url(#g_sh2)'},o.cs);
 {const bx=el('g',{transform:'translate(-370 0)'},o.cs);el('rect',{x:-45,y:-45,width:90,height:90,rx:16,fill:AMB,stroke:'#fff','stroke-width':4},bx);fit(bx,'?',0,28,84,NAVY,70);}
 fit(o.cs,'QUALE CASO?',60,18,56,'#fff',620);
 o.gr=el('g',{},p);{const ge=gearI(o.gr,72);o.ge=ge;ge.setAttribute('transform','translate(-330 0)');const pl=pillS(o.gr,'CAMBIA I CONTI',560,46,GRN);T(pl,100,0,0,1);}
 o.fi=pillS(p,'ALLA FINE DEL VIDEO',720,40,ORG);
 o.cap=strip(p,['UN CASO SENZA TAGLIO','UN MECCANISMO CHE CAMBIA I CONTI']);return o;},
 update(t,o){const a=plan(3,['Esiste un caso','anche con un reddito alto','Quale?','meccanismo','alla fine del video']);PL[3]=a;headU(t,o);bgx(t);
  fade(t,o.sh,420,500,a[0]);const A=Math.max(0,1-(t-a[0])/2.5);snip(o.sx,5+(t>a[0]?A*8*(.5+.5*Math.sin((t-a[0])*7)):0));
  fade(t,o.ch,540,895,a[1]);fade(t,o.cs,540,1095,a[2]);
  fade(t,o.gr,540,1255,a[3]);{const A2=Math.max(0,1-(t-a[3])/3);o.ge.setAttribute('transform','translate(-330 0) rotate('+(A2*A2*50)+')');}
  T(o.fi,540,1390,0,pop(t,a[4]));rise(t,a[5],.9,o.cap,1560,100);}},
// ---- 5: tre situazioni delicate su tre schede orizzontali, ognuna con la regola sigillata ----
{D:DUR[4],build(p){const o={};head(p,o,'CASI DELICATI');
 o.bn=pillS(p,'TRE SITUAZIONI DELICATE',900,40,NAVY);
 const defs=[['SE TI RISPOSI',null],['SE C\'È ANCHE','UN EX CONIUGE'],['SE NON ERAVATE','SPOSATI']];
 o.sit=defs.map((d,i)=>{const g=el('g',{},p);el('rect',{x:-450,y:-125,width:900,height:250,rx:26,fill:'url(#g_paper)',stroke:'#fff','stroke-width':4,filter:'url(#g_sh)'},g);
  el('rect',{x:-450,y:-125,width:20,height:250,rx:8,fill:[GRN,'#2A7A82',ORG][i]},g);
  const ill=el('g',{transform:'translate(-290 6)'},g);
  if(i==0){[-95,95].forEach((x,k)=>{const q=personI(ill,1.25,k?'#0B4A50':GRN);q.setAttribute('transform','translate('+x+' 0)');});
   [-14,14].forEach(x=>el('circle',{cx:x,cy:10,r:22,fill:'none',stroke:AMB,'stroke-width':8},ill));}
  else if(i==1){[[-115,'#7F9AA0'],[0,ORG],[115,'#0B4A50']].forEach(([x,c],k)=>{const q=personI(ill,1.05,c);q.setAttribute('transform','translate('+x+' 0)');});
   el('rect',{x:-10-50,y:-62,width:100,height:130,rx:16,fill:'none',stroke:ORG,'stroke-width':4,'stroke-dasharray':'10 8'},ill);}
  else{[-105,105].forEach((x,k)=>{const q=personI(ill,1.25,'#0B4A50');q.setAttribute('transform','translate('+x+' 0)');});
   el('circle',{cx:0,cy:12,r:24,fill:'none',stroke:'#9FB4B9','stroke-width':8,'stroke-dasharray':'9 7'},ill);el('line',{x1:-26,y1:38,x2:26,y2:-14,stroke:RED,'stroke-width':8,'stroke-linecap':'round'},ill);}
  if(d[1]===null)fit(g,d[0],70,12,50,INK,380);else{fit(g,d[0],70,-14,46,INK,380);fit(g,d[1],70,48,46,INK,380);}
  const rg=el('g',{transform:'translate(365 0)'},g);g.rg=rg;el('rect',{x:-80,y:-85,width:160,height:170,rx:18,fill:NAVY,stroke:AMB,'stroke-width':5},rg);
  const lk=lockI(rg,1.1);lk.setAttribute('transform','translate(0 -22)');fit(rg,'REGOLA',0,62,30,'#fff',130);
  return g;});
 o.vd=el('g',{},p);el('rect',{x:-420,y:-48,width:840,height:96,rx:48,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.vd);
 el('path',{d:'M-380 -24 L-340 0 L-380 24Z',fill:'#fff',stroke:'#fff','stroke-width':8,'stroke-linejoin':'round'},o.vd);fit(o.vd,'LA SPIEGHIAMO NEL VIDEO',30,15,42,'#fff',700);
 o.cap=strip(p,['TRE SITUAZIONI DELICATE','PER OGNUNA UNA REGOLA PRECISA']);return o;},
 update(t,o){const a=plan(4,['tre situazioni','se ti risposi','un ex coniuge','se non eravate','la regola è precisa','la spieghiamo']);PL[4]=a;headU(t,o);bgx(t);
  T(o.bn,540,305,0,pop(t,a[0]));
  [[1,550],[2,830],[3,1110]].forEach(([e,y],k)=>slideX(t,o.sit[k],540,y,a[e],k%2?80:-80));
  o.sit.forEach((g,k)=>T(g.rg,365,0,0,pop(t,a[4]+k*.0)));
  fade(t,o.vd,540,1345,a[5]);rise(t,a[6],.9,o.cap,1560,100);}},
// ---- 6: commento con tre scelte (60 / 80 / 100 %) + telefono "video correlato" con dito + mi piace + iscriviti ----
{D:DUR[5],build(p){const o={};head(p,o,'TOCCA A TE');
 o.cm=el('g',{},p);el('rect',{x:-450,y:-65,width:900,height:130,rx:30,fill:NAVY,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},o.cm);
 {const av=el('g',{transform:'translate(-380 0)'},o.cm);el('circle',{r:42,fill:'#7FF0D2'},av);const q=personI(av,.8,NAVY);q.setAttribute('transform','translate(0 6)');}
 el('rect',{x:-310,y:-40,width:740,height:80,rx:40,fill:'#fff'},o.cm);fit(o.cm,'Scrivi nei commenti…',-280,16,40,'#5B7378',560,'start');el('rect',{x:300,y:-24,width:5,height:48,fill:ORG},o.cm);
 o.sf=el('g',{},p);{const q=personI(o.sf,1.0,'#fff');q.setAttribute('transform','translate(-370 0)');const pl=pillS(o.sf,'CONIUGE SENZA FIGLI',680,40,ORG);T(pl,60,0,0,1);}
 o.bb=['60 %','80 %','100 %'].map((s,k)=>{const g=el('g',{},p);
  el('path',{d:'M-100 80 L-124 128 L-50 82Z',fill:'#fff',stroke:'#fff','stroke-width':4,'stroke-linejoin':'round'},g);
  el('rect',{x:-130,y:-80,width:260,height:162,rx:34,fill:'#fff',stroke:[GRN,'#2A7A82',ORG][k],'stroke-width':8,filter:'url(#g_sh2)'},g);fit(g,s,0,26,84,INK,200);return g;});
 o.ph=el('g',{},p);el('rect',{x:-170,y:-260,width:340,height:520,rx:50,fill:'#0A1C1F',stroke:'#fff','stroke-width':6,filter:'url(#g_sh)'},o.ph);
 el('rect',{x:-146,y:-232,width:292,height:464,rx:30,fill:'#E9F6F4'},o.ph);
 el('rect',{x:-130,y:-222,width:260,height:62,rx:14,fill:'#fff'},o.ph);fit(o.ph,'VIDEO CORRELATO',0,-180,26,NAVY,208);
 el('rect',{x:-130,y:-140,width:260,height:160,rx:16,fill:'url(#g_red)'},o.ph);el('path',{d:'M-28 -98 L48 -60 L-28 -22Z',fill:'#fff','stroke-linejoin':'round',stroke:'#fff','stroke-width':12},o.ph);
 [[-130,50,200],[-130,82,150],[-130,114,220],[-130,146,120]].forEach(([x,y,w])=>el('rect',{x:x,y:y,width:w,height:12,rx:6,fill:'#B5C6C9'},o.ph));
 o.fg=el('g',{},p);o.rip=[0,1].map(()=>el('circle',{r:30,fill:'none',stroke:'#fff','stroke-width':6},o.fg));o.hd=el('g',{},o.fg);handI(o.hd);
 o.td=pillS(p,'TOCCALO ADESSO',560,42,RED);
 o.lk=el('g',{},p);el('rect',{x:-200,y:-62,width:400,height:124,rx:62,fill:NAVY,stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.lk);{const th=thumbI(o.lk,.5);th.setAttribute('transform','translate(-135 4)');}fit(o.lk,'MI PIACE',55,16,46,'#fff',230);
 o.is=el('g',{},p);el('rect',{x:-200,y:-72,width:400,height:144,rx:36,fill:'url(#g_red)',stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},o.is);fit(o.is,'ISCRIVITI',-16,4,50,'#fff',280);fit(o.is,'A CONTI IN PENSIONE',-16,46,25,'#fff',310);{const be=bellI(o.is,.42);T(be,148,-4,0,1);}
 o.cap=strip(p,['60, 80 O 100 PER CENTO?','SCRIVILO NEI COMMENTI']);return o;},
 update(t,o){const a=plan(5,['Scrivi nei commenti','al coniuge senza figli','il sessanta','l\'ottanta','il cento','video correlato','toccalo adesso','Metti mi piace','iscriviti']);PL[5]=a;headU(t,o);bgx(t);
  fade(t,o.cm,540,335,a[0]);fade(t,o.sf,540,495,a[1],40);
  [170,540,910].forEach((x,k)=>T(o.bb[k],x,690,(k-1)*2.5,pop(t,a[2+k])));
  fade(t,o.ph,310,1050,a[5]);
  const k6=a[6],e=seg(t,k6,k6+.9);T(o.fg,360,1000,0,1);op(o.fg,seg(t,k6,k6+.5));T(o.hd,34,lerp(260,60,eo3(e)),-25,1);
  const tp=t-(k6+.9);o.rip.forEach((c,j)=>{const u=tp>0&&tp<3?((tp*0.9+j*.5)%1):0;c.setAttribute('r',30+u*70);c.setAttribute('opacity',tp>0&&tp<3?(1-u)*.9:0);});
  T(o.td,310,1365,0,pop(t,k6+.2));
  T(o.lk,770,960,0,pop(t,a[7]));T(o.is,770,1130,0,pop(t,a[8]));rise(t,a[9],.9,o.cap,1560,100);}},
];
