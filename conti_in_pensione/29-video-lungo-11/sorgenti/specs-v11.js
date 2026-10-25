// ===== VIDEO 11 (aumento pensioni gennaio 2027, tabella netta) - elementi nuovi + 14 blocchi =====
// Un po' diverso dai video 8-10 (N.37, N.47 alla lettera), stessi colori e stessa impostazione del canale:
// titoletto con moneta e 14 barre che salgono, didascalia con filo giallo a sinistra e moneta, sfondo con grafico a barre in trasparenza,
// tabelle a righe, colonne "tieni / tasse", barre a fasce, linea del tempo, schede con testata scura.
const NB11=14;
const OV=it=>{it.ov=1;return it;};
const P=(s,x,y,at,fill,fs,icon,o)=>I('pill',[s,fs||34,fill||DF_,(fill===AMB)?'#5A3300':'#fff',icon,o],x,y,at);
const LIGHT='#D6F5EC';
const TXTC=(a,b)=>[a,b];
// ---------- titoletto: moneta + titolo a sinistra, 14 barre che salgono a destra ----------
function topLabel(g,s){const t=el('g',{transform:'translate(-840 0)'},g);
 el('rect',{x:-40,y:-38,width:80,height:76,rx:20,fill:'#06303A',stroke:'#7FF0D2','stroke-width':3,filter:'url(#g_sh3)'},t);
 const cg=el('g',{},t);el('circle',{r:27,fill:AMB,stroke:'#fff','stroke-width':4},cg);euro(cg,0,0,0.3,'#5A3300',16);
 const x=txt(t,s,70,12,36,'#7FF0D2','bold','start');x.setAttribute('letter-spacing','6');
 let w=tw(s,36)+s.length*6;try{w=x.getBBox().width;}catch(e){}
 el('rect',{x:70,y:30,width:Math.min(w,150),height:5,rx:2.5,fill:AMB},t);
 const X0=1500,DX=20;const l0=70+w+28,l1=X0-26;if(l1>l0+20)el('line',{x1:l0,y1:0,x2:l1,y2:0,stroke:'#7FF0D2','stroke-width':3,opacity:.32,'stroke-dasharray':'3 12'},t);
 for(let i=0;i<NB11;i++){const on=(i+1)===N;const h=12+i*2.4+(on?10:0);el('rect',{x:X0+i*DX-5,y:18-h,width:10,height:h,rx:3,fill:on?AMB:'#7FF0D2',opacity:on?1:((i+1)<N?.75:.28)},t);}
 return t;}
// ---------- didascalia: riquadro scuro, filo giallo a sinistra, moneta ----------
function cap(g,s,size){size=size||44;const c=el('g',{},g);if(!s)return c;
 const t=txt(c,s,0,0,size,'#FFFFFF','bold');let tl=mw(t,s,size);
 const maxT=1540;if(tl>maxT){size=size*maxT/tl;t.setAttribute('font-size',size.toFixed(1));tl=mw(t,s,size);}
 const padL=130,padR=60;const w=tl+padL+padR;
 t.setAttribute('x',(-w/2+padL+tl/2).toFixed(1));t.setAttribute('y',(size*0.36).toFixed(1));
 const ins=e=>{c.insertBefore(e,t);return e;};
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:22,fill:'#06303A',filter:'url(#g_sh2)'}));
 ins(el('rect',{x:-w/2,y:-56,width:w,height:112,rx:22,fill:'none',stroke:'#7FF0D2','stroke-width':2.5,opacity:.45}));
 ins(el('rect',{x:-w/2,y:-40,width:8,height:80,rx:4,fill:AMB}));
 const hb=el('g',{transform:'translate('+(-w/2+68)+' 0)'},c);el('circle',{r:32,fill:AMB,stroke:'#fff','stroke-width':4},hb);euro(hb,0,0,0.36,'#5A3300',16);
 return c;}
// ---------- barra a fasce (segmenti colorati con testo dentro) ----------
function zbarB(g,W,segs,o){o=o||{};const H=o.h||96;const id='zb'+(++UID);const cp=el('clipPath',{id:id},g);el('rect',{x:-W/2,y:-H/2,width:W,height:H,rx:H/2},cp);
 el('rect',{x:-W/2-6,y:-H/2-6,width:W+12,height:H+12,rx:H/2+6,fill:'#06303A',filter:'url(#g_sh2)'},g);
 const bg=el('g',{'clip-path':'url(#'+id+')'},g);let x=-W/2;
 segs.forEach((s,i)=>{const w=s.f*W;el('rect',{x:x,y:-H/2,width:w,height:H,fill:s.fill},bg);if(i>0)el('rect',{x:x-2,y:-H/2,width:4,height:H,fill:'#fff',opacity:.85},bg);
  if(s.mid)fitT(g,s.mid,x+w/2,0,s.fs||34,s.col||'#fff','900',w-34);x+=w;});
 el('rect',{x:-W/2,y:-H/2,width:W,height:H,rx:H/2,fill:'none',stroke:'#fff','stroke-width':4,opacity:.85},g);
 return g;}
// ---------- colonna "100 euro di aumento": sopra le tasse (rosso), sotto quello che resta (verde) ----------
function col100(g,w,h,keep,o){o=o||{};const kh=h*keep/100,th=h-kh;const id='c1'+(++UID);
 const cp=el('clipPath',{id:id},g);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26},cp);
 el('rect',{x:-w/2-6,y:-h/2-6,width:w+12,height:h+12,rx:30,fill:'#06303A',filter:'url(#g_sh)'},g);
 const bg=el('g',{'clip-path':'url(#'+id+')'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:th,fill:'url(#g_red)'},bg);
 el('rect',{x:-w/2,y:-h/2+th,width:w,height:kh,fill:o.keepfill||'url(#g_badge)'},bg);
 el('rect',{x:-w/2,y:-h/2+th-2,width:w,height:4,fill:'#fff',opacity:.9},bg);
 fitT(g,'TASSE '+(100-keep),0,-h/2+th/2,o.fs||40,'#fff','900',w-30);
 fitT(g,'TIENI '+keep,0,-h/2+th+kh/2-22,(o.fs||40)+14,'#fff','900',w-30);
 fitT(g,'SU 100 €',0,-h/2+th+kh/2+34,30,'#E9FBF6','bold',w-30);
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'none',stroke:o.stroke||'#fff','stroke-width':o.stroke?8:4,opacity:.9},g);
 return g;}
// ---------- riga di tabella: celle colorate affiancate ----------
function trow2(g,w,cells,o){o=o||{};const h=o.h||88;let x=-w/2;
 el('rect',{x:-w/2-5,y:-h/2-5,width:w+10,height:h+10,rx:h/2*0.62+5,fill:o.hl?AMB:'#06303A',filter:'url(#g_sh2)'},g);
 cells.forEach((c,i)=>{const cw=c[3]*w;
  el('rect',{x:x+(i==0?0:2),y:-h/2,width:cw-(i==0?0:2),height:h,rx:i==0?h/2*0.62:(i==cells.length-1?h/2*0.62:0),fill:c[1]},g);
  if(i>0&&i<cells.length-1)el('rect',{x:x,y:-h/2,width:cw,height:h,fill:c[1]},g);
  fitT(g,c[0],x+cw/2,0,c[4]||o.fs||38,c[2]||'#fff','900',cw-26);x+=cw;});
 return g;}
// ---------- linea del tempo a tre tappe ----------
function tl3B(g,W,nodes){const n=nodes.length;
 el('line',{x1:-W/2,y1:0,x2:W/2,y2:0,stroke:'#7FF0D2','stroke-width':8,'stroke-linecap':'round',opacity:.5,'stroke-dasharray':'2 18'},g);
 nodes.forEach((nd,i)=>{const x=-W/2+i*(W/(n-1));const ng=el('g',{transform:'translate('+x+' 0)'},g);
  el('circle',{r:62,fill:nd.fill||DF_,stroke:'#fff','stroke-width':6,filter:'url(#g_sh2)'},ng);ico(ng,nd.icon,1.2,nd.icol||'#fff');
  fitT(ng,nd.top,0,-112,32,'#fff','900',380);fitT(ng,nd.sub,0,112,26,'#7FF0D2','bold',380);});
 return g;}
// ---------- scatola disclaimer ----------
function dbox11(g,w,h,lines){el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'#06303A',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:70,rx:26,fill:GRN},g);el('rect',{x:-w/2,y:-h/2+40,width:w,height:30,fill:GRN},g);
 el('rect',{x:-w/2,y:-h/2+65,width:w,height:5,fill:AMB},g);
 fitT(g,'DISCLAIMER',0,-h/2+36,32,'#fff','900');
 lines.forEach((L,i)=>fitT(g,L[0],0,-h/2+70+(h-70)*(i+0.5)/lines.length,L[1],L[2]||'#fff','bold',w-60));}
Object.assign(BUILD,{
 pill:(g,s,fs,fill,col,icon,o)=>pillB(g,s,fs,fill,col,icon,o),
 bign:(g,top,val,sub,o)=>bigN(g,top,val,sub,o),
 card:(g,title,w,h,o)=>cardB(g,title,w,h,o),
 stamp:(g,lines,col,fs,rot)=>stampB(g,lines,col,fs,rot),
 icoc:(g,k,r,fill,icol)=>icoC(g,k,r,fill,icol),
 icard:(g,w,h,icon,lines,o)=>{o=o||{};el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:o.fill||'url(#g_paper)',filter:'url(#g_sh)'},g);
  if(o.stroke)el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'none',stroke:o.stroke,'stroke-width':6},g);
  const ir=o.ir||Math.min(70,h*0.36);const ix=-w/2+ir+34;const ig=el('g',{transform:'translate('+ix+' 0)'},g);el('circle',{r:ir,fill:o.ibg||LIGHT},ig);ico(ig,icon,ir/54,o.icol||INK);
  const x0=ix+ir+26,x1=w/2-40,cx=(x0+x1)/2;const n=lines.length;const lh=o.lh||(lines[0][1]*1.32);
  lines.forEach((L,i)=>fitT(g,L[0],cx,(i-(n-1)/2)*lh+(o.dy||0),L[1],L[2]||INK,L[3]||'900',x1-x0));},
 zbar:(g,W,segs,o)=>zbarB(g,W,segs,o),
 col100:(g,w,h,keep,o)=>col100(g,w,h,keep,o),
 trow2:(g,w,cells,o)=>trow2(g,w,cells,o),
 tl3:(g,W,nodes)=>tl3B(g,W,nodes),
 dbox:(g,w,h,lines)=>dbox11(g,w,h,lines),
 mark:(g,s,col)=>{el('path',{d:'M0 -46 L-30 0 H30 Z',fill:col||AMB,stroke:'#fff','stroke-width':4,'stroke-linejoin':'round',filter:'url(#g_sh3)'},g);},
 goalbar:(g,w,frac)=>{el('rect',{x:-w/2,y:-26,width:w,height:52,rx:26,fill:'#06303A',stroke:'#7FF0D2','stroke-width':3},g);
  el('rect',{x:-w/2+6,y:-20,width:Math.max(30,(w-12)*frac),height:40,rx:20,fill:'url(#g_badge)'},g);
  for(let k=0;k<=4;k++)el('rect',{x:-w/2+6+(w-12)*k/4-2,y:30,width:4,height:14,fill:'#fff',opacity:.7},g);},
});
const DK='#06303A';
// ======================= BLOCCHI =======================
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'AUMENTO PENSIONI GENNAIO 2027',cap:'SU OGNI MILLE EURO LORDI, SUL CONTO NON ARRIVANO VENTINOVE',items:[
  P('STIMA PIÙ CITATA: 2,9%',960,225,'con la stima più citata',AMB,36,'up'),
  I('bign',['LORDO, SU OGNI 1.000 €','+29 €',null,{fs:124,fill:AMB,col:'#5A3300',subcol:'#5A3300',minw:600,tfs:28}],520,450,'ventinove euro ogni mille'),
  OV(I('cross',[96,26],520,478,'non arrivano ventinove')),
  I('arR',[],960,450,'Ma sul conto'),
  I('bign',['SUL CONTO ARRIVANO','≈ 20 €',null,{fs:124,fill:GF_,col:'#fff',subcol:'#fff',minw:600,tfs:28}],1400,450,'ne arrivano circa venti'),
  P('IN CERTI CASI ANCORA MENO',1400,655,'ancora meno',RF_,34,'down'),
  P('TABELLA NETTA: DA 600 A 3.000 €',520,790,'la tabella netta',DF_,34,'calc'),
  P('SORPRESA PER LA MINIMA, ALLA FINE',1400,790,'una sorpresa',AMB,34,'lock')]},
]);
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA PERCENTUALE: ANCORA DA DECIDERE',cap:'LA PERCENTUALE UFFICIALE NON ESISTE ANCORA: LA FISSA UN DECRETO',items:[
  I('stamp',[['NON ESISTE','ANCORA'],RED_,56,-5],520,330,'non esiste ancora'),
  I('icard',[740,200,'doc',[['DECRETO DEI MINISTERI',34],['ECONOMIA E LAVORO',34,GRN]],{lh:46}],1390,330,'La fissa un decreto'),
  I('icard',[560,160,'cal',[['DI SOLITO A',30],['NOVEMBRE',54,GRN]],{lh:56}],520,600,'di solito a novembre'),
  P('QUINDI: IPOTESI, NON CERTEZZE',1300,600,'Quindi parliamo di ipotesi',AMB,38,'q'),
  ]},
 {at:"Il sedici ottobre",top:'COSA HA DETTO L\'ISTAT',cap:'A SETTEMBRE I PREZZI PER OPERAI E IMPIEGATI +0,6% IN UN MESE',items:[
  P('16 OTTOBRE',420,270,'Il sedici ottobre',AMB,40,'cal'),
  I('icard',[780,210,'people',[["PREZZI PER FAMIGLIE",32],['DI OPERAI E IMPIEGATI',32],['(INDICE FOI)',30,GRN]],{lh:44}],1380,270,'i prezzi per operai e impiegati'),
  I('bign',['SETTEMBRE: IN UN MESE','+0,6 %',null,{fs:128,fill:RF_,col:'#fff',subcol:'#fff',minw:620,tfs:28}],520,560,'sono saliti dello zero virgola sei'),
  P("L'INDICE CHE CONTA PER LE PENSIONI",1360,560,"l'indice che conta per le pensioni",DF_,34,'ok',{icol:GRN}),
  P('PER QUESTO: ANCHE UNO SCENARIO ALTO',960,790,'Per questo aggiungiamo',AMB,38,'up')]},
]);
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO HA DUE PASSAGGI',cap:'PRIMO L\'AUMENTO LORDO, POI LE TASSE: IRPEF E DETRAZIONE CHE CALA',items:[
  I('icard',[740,190,'up',[['1 · AUMENTO LORDO',36],['LA PERCENTUALE SULLA PENSIONE',28,GRN]],{lh:46}],480,260,'Primo'),
  I('icard',[740,190,'stato',[['2 · LE TASSE',36],['IRPEF E DETRAZIONE',28,GRN]],{lh:46}],1440,260,'Secondo'),
  P('SU OGNI 100 € DI AUMENTO',960,450,'su ogni euro aggiunto',DF_,36,'coin'),
  I('bign',['IRPEF','− 23 €',null,{fs:110,fill:RF_,col:'#fff',subcol:'#fff',minw:420,tfs:30}],520,630,"L'Irpef si prende"),
  I('bign',['LA DETRAZIONE CALA','− 6 €',null,{fs:110,fill:'#E39A1C',col:'#4A2600',subcol:'#4A2600',minw:520,tfs:30}],1100,630,'la detrazione dei pensionati cala'),
  P('PIÙ SALE IL REDDITO, PIÙ CALA',1500,790,'man mano che il reddito sale',DF_,32,'down'),
  I('stamp',[['CIRCA 6','ALTRI EURO'],RED_,38,-5],1640,640,'portandosene via altri sei')]},
 {at:'Quindi, da circa',top:'DA CIRCA 650 A CIRCA 2.150 € LORDI',cap:'TI RESTANO CIRCA 71 EURO OGNI 100 DI AUMENTO',items:[
  P('≈ 650 € AL MESE',330,300,'da circa seicentocinquanta',DF_,38,'down'),
  P('≈ 2.150 € AL MESE',1590,300,'a circa duemilacentocinquanta',DF_,38,'down'),
  I('zbar',[1500,[{f:1,fill:'url(#g_badge)',mid:'LORDI AL MESE',fs:40}],{h:100}],960,470,'euro lordi al mese'),
  I('bign',['TI RESTANO','≈ 71 €',null,{fs:140,fill:AMB,col:'#5A3300',subcol:'#5A3300',minw:640,tfs:30}],960,710,'circa settantuno'),
  P('OGNI 100 € DI AUMENTO',1620,710,'ogni cento di aumento',GF_,30,'ok')]},
]);
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'1.000 € LORDI: TRE SCENARI',cap:'CON MILLE EURO LORDI: DA 26 A 31 € DI AUMENTO, DA 18 A 22 € IN TASCA',items:[
  P('PENSIONE LORDA: 1.000 €',960,222,'Prendiamo mille euro lordi',AMB,40,'coin'),
  I('trow2',[700,[['SCENARIO',DK,LT,0.5],['AUMENTO LORDO',DK,LT,0.5]],{h:64,fs:26}],640,330,'Le stime sui dati di agosto'),
  I('trow2',[700,[['BASSO 2,6%','#2B6F77','#fff',0.5],['+26 €',AMB,'#5A3300',0.5]],{h:90,fs:34}],640,440,'due virgola sei'),
  I('trow2',[700,[['DI MEZZO 2,9%',GRN,'#fff',0.5],['+29 €',AMB,'#5A3300',0.5]],{h:90,fs:34,hl:1}],640,550,'due virgola nove'),
  I('trow2',[700,[['ALTO 3,1%','#2B6F77','#fff',0.5],['+31 €',AMB,'#5A3300',0.5]],{h:90,fs:34}],640,660,'Scenario alto, tre virgola uno'),
  P('ALTO = SOLO UN RIFERIMENTO',640,790,'quindi solo un riferimento',DF_,28,'warn',{icol:AMB}),
  I('pill',['IN TASCA',36,GF_,'#fff','ok'],1450,330,'In tasca ti arrivano'),
  I('pill',['≈ 18 €',46,'#2B6F77','#fff'],1450,440,'circa diciotto'),
  I('pill',['≈ 20 €',46,GF_,'#fff'],1450,550,'venti e'),
  I('pill',['≈ 22 €',46,'#2B6F77','#fff'],1450,660,'ventidue euro'),
  I('bign',['IN UN ANNO, STIMA DI MEZZO','≈ 266 € NETTI',null,{fs:62,fill:AMB,col:'#5A3300',subcol:'#5A3300',minw:640,tfs:24}],1450,795,'In un anno la stima di mezzo')]},
]);
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ISCRIVITI AL CANALE',cap:'COSTA UN TOCCO E CI AIUTA AD ARRIVARE A MILLE ISCRITTI',items:[
  P('UN CONTO CHE I TITOLI NON FANNO',960,215,'un conto che i titoli non fanno',AMB,36,'bulb'),
  I('btn',['ISCRIVITI'],560,430,'iscriviti al canale'),
  P('COSTA UN TOCCO',560,570,'costa un tocco',GF_,34,'ok'),
  I('icard',[780,200,'people',[['OBIETTIVO: 1.000 ISCRITTI',34],['CI AIUTI AD ARRIVARCI',30,GRN]],{lh:46}],1380,430,'ci aiuta ad arrivare a mille iscritti'),
  I('goalbar',[640,0.28],1480,600,'a mille iscritti'),
  I('icard',[720,170,'doc',[['OGNI VIDEO: ORE DI CONTROLLI',30],['SULLE FONTI UFFICIALI',32,GRN]],{lh:44}],450,730,'ogni video nasce da ore di controlli'),
  I('bell',[],950,715,'Attiva anche la campanella'),
  I('icard',[640,170,'next',[['QUANDO ESCE IL DECRETO:',30],['TABELLA AGGIORNATA',34,GRN]],{lh:44}],1500,730,'quando esce il decreto')]},
]);
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'1.500 E 2.000 € LORDI',cap:'LA PROPORZIONE RESTA QUELLA DEL PRIMO ESEMPIO, MA OLTRE UNA CERTA CIFRA CAMBIA',items:[
  P('1.500 € LORDI',520,215,'Salendo a millecinquecento',AMB,42,'coin'),
  I('bign',["AUMENTO LORDO",'39 → 46,5 €',null,{fs:84,fill:AMB,col:'#5A3300',subcol:'#5A3300',minw:640,tfs:28}],520,355,'va da trentanove'),
  I('bign',['IN TASCA','27,5 → 33 €',null,{fs:84,fill:GF_,col:'#fff',subcol:'#fff',minw:640,tfs:28}],520,545,'restano da ventisette'),
  P('2.000 € LORDI',1400,215,'Con duemila lordi',AMB,42,'coin'),
  I('bign',["AUMENTO LORDO",'52 → 62 €',null,{fs:84,fill:AMB,col:'#5A3300',subcol:'#5A3300',minw:640,tfs:28}],1400,355,"l'incremento è da cinquantadue"),
  I('bign',['IN TASCA','37 → 44 €',null,{fs:84,fill:GF_,col:'#fff',subcol:'#fff',minw:640,tfs:28}],1400,545,'in tasca da trentasette'),
  P('LA PROPORZIONE NON CAMBIA: ≈ 71 SU 100',960,735,'La proporzione resta',DF_,36,'ok',{icol:GRN}),
  P('MA OLTRE UNA CERTA CIFRA, CAMBIA',960,825,'Ma oltre una certa cifra',RF_,40,'warn',{icol:RED_})]},
]);
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL GRADINO DELL\'IRPEF',cap:'OLTRE 28.000 € L\'ANNO: ALIQUOTA 33% E DETRAZIONI CHE CALANO',items:[
  P('IL GRADINO: 2.150 € AL MESE',520,200,'E adesso il gradino',AMB,38,'signs',{icol:'#5A3300'}),
  P('= 28.000 € ALL\'ANNO',1400,200,"ventottomila euro l'anno",DF_,34,'cal'),
  P('FINO AL GRADINO',340,278,'la soglia dei duemilacentocinquanta',GF_,28,'ok'),
  I('col100',[260,400,71,{fs:34}],340,570,'la soglia dei duemilacentocinquanta'),
  I('stamp',[['ALIQUOTA','33%'],RED_,44,-6],660,430,"scatta l'aliquota"),
  I('arR',[],660,630,'Oltre, scatta'),
  P('OLTRE IL GRADINO',980,278,'circa sessantaquattro',AMB,28,'down'),
  I('col100',[260,400,64,{fs:34,stroke:AMB}],980,570,'circa sessantaquattro'),
  P('LE DETRAZIONI CONTINUANO A CALARE',660,850,'le detrazioni continuano a calare',DF_,30,'down'),
  I('bign',['2.500 € LORDI: AUMENTO','+65 → +77 €',null,{fs:70,fill:AMB,col:'#5A3300',subcol:'#5A3300',minw:520,tfs:26}],1560,430,'incremento da sessantacinque'),
  I('bign',['IN TASCA','+41 → +49 €',null,{fs:70,fill:GF_,col:'#fff',subcol:'#fff',minw:520,tfs:26}],1560,620,'netto da quarantuno')]},
]);
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'3.000 € LORDI E LE FASCE',cap:'STESSA PERCENTUALE, AUMENTI DIVERSI: CAMBIANO LE FASCE E LE TASSE',items:[
  P('PENSIONE DA 3.000 € LORDI',960,215,'Per una pensione da tremila',AMB,40,'coin'),
  I('bign',["AUMENTO LORDO",'77 → 91 €',null,{fs:90,fill:AMB,col:'#5A3300',subcol:'#5A3300',minw:640,tfs:28}],520,380,"l'incremento sale da settantasette"),
  I('bign',['IN TASCA','49 → 58 €',null,{fs:90,fill:GF_,col:'#fff',subcol:'#fff',minw:640,tfs:28}],1400,380,'il netto da quarantanove'),
  I('zbar',[1500,[{f:0.46,fill:'url(#g_badge)',mid:'100% DELLA PERCENTUALE',fs:32},{f:0.54,fill:'#E39A1C',mid:'90% SULLA PARTE OLTRE',fs:32,col:'#4A2600'}],{h:92}],960,520,'la percentuale piena vale'),
  I('mark',[AMB],900,628,'Sopra circa duemilaquattrocentocinquanta'),
  P('≈ 2.450 € LORDI',900,690,['Sopra circa duemilaquattrocentocinquanta',0.2],DF_,30,'down'),
  P('GIÀ DENTRO IL CONTO',1400,690,'ed è già dentro il conto',GF_,32,'ok'),
  P('FASCE DIVERSE',560,800,'cambiano le fasce',DF_,38,'ruler'),
  P('TASSE DIVERSE',1360,800,'e cambiano le tasse',RF_,38,'stato')]},
]);
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA REGOLA DEL DECIMO',cap:'OGNI 0,1% IN PIÙ VALE 1 EURO OGNI MILLE LORDI: POI TOGLI LE TASSE',items:[
  P('LA REGOLA DEL DECIMO',960,215,'La regola del decimo',AMB,42,'bulb',{icol:'#5A3300'}),
  I('bign',['SE LA PERCENTUALE SALE DI','+ 0,1 %',null,{fs:96,minw:460,tfs:26}],380,400,'ogni zero virgola uno'),
  I('op',['='],760,400,'vale'),
  I('bign',['SU OGNI 1.000 € LORDI','+ 1 €',null,{fs:96,fill:AMB,col:'#5A3300',subcol:'#5A3300',minw:460,tfs:26}],1140,400,'un euro su mille lordi'),
  P('2.000 € → 2 €',1660,400,'A duemila',DF_,32,'coin'),
  I('bign',['IN TASCA, SOTTO IL GRADINO','≈ 70 cent',null,{fs:84,fill:GF_,col:'#fff',subcol:'#fff',minw:560,tfs:26}],520,610,'circa settanta centesimi'),
  I('bign',['IN TASCA, SOPRA','≈ 64 cent',null,{fs:84,fill:'#E39A1C',col:'#4A2600',subcol:'#4A2600',minw:560,tfs:26}],1200,610,'circa sessantaquattro sopra'),
  I('icard',[640,150,'calc',[['SE LA PERCENTUALE CAMBIA,',30],['RIFAI LA MOLTIPLICAZIONE',30,GRN]],{lh:40}],520,790,'rifai questa moltiplicazione'),
  I('icard',[760,150,'chat',[['SCRIVICI NEI COMMENTI',30],['IL TUO IMPORTO LORDO',34,GRN]],{lh:42}],1400,790,'Scrivici nei commenti')]},
]);
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA SORPRESA: LE PENSIONI AL MINIMO',cap:'SOTTO 8.500 € L\'ANNO NON C\'È IRPEF: L\'AUMENTO ARRIVA INTERO',items:[
  P('LA SORPRESA PROMESSA',960,215,'la sorpresa promessa',AMB,40,'lock'),
  I('bign',["SOTTO CIRCA",'8.500 € ALL\'ANNO',"= 654 € AL MESE",{fs:62,minw:700,tfs:28,sfs:30}],520,420,"Sotto circa ottomilacinquecento"),
  I('stamp',[['NIENTE','IRPEF'],GRN,56,-5],1180,420,"l'Irpef non c'è"),
  I('icard',[480,170,'ok',[["L'AUMENTO",32],['ARRIVA INTERO',36,GRN]],{lh:46}],1600,420,"l'aumento arriva intero"),
  I('bign',['TRATTAMENTO MINIMO OGGI','611,85 €',null,{fs:76,minw:340,tfs:24}],330,650,'trattamento minimo oggi'),
  I('op',['+'],645,650,"con l'extra"),
  I('bign',['EXTRA 1,3% (SOLO 2026)','+ 7,95 €',null,{fs:76,fill:AMB,col:'#5A3300',subcol:'#5A3300',minw:340,tfs:24}],960,650,"l'extra dell'uno virgola tre"),
  I('op',['='],1280,650,'chi ha la pensione al minimo'),
  I('bign',['ARRIVA A','619,80 €',null,{fs:76,fill:GF_,col:'#fff',subcol:'#fff',minw:340,tfs:24}],1590,650,'arriva a seicentodiciannove')]},
]);
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E NEL 2027? L\'EXTRA PUÒ SPARIRE',cap:'DA 8 A 11 EURO IN PIÙ, E NON DA 16 A 19 COME FA PENSARE LA PERCENTUALE',items:[
  P("L'EXTRA È PREVISTO SOLO FINO AL 2026",960,215,'fino al duemilaventisei',RF_,38,'cal'),
  I('icard',[760,170,'warn',[['SENZA UN NUOVO INTERVENTO',32],['DELLA MANOVRA',34,GRN]],{lh:44,icol:RED_,ibg:'#FFE3DE'}],480,370,'Senza un nuovo intervento'),
  P('MINIMO 2027 (3 SCENARI)',1300,330,'il minimo del duemilaventisette',DF_,34,'up'),
  I('pill',['≈ 628 €',44,'#2B6F77','#fff'],1090,430,'seicentoventotto'),
  I('pill',['≈ 630 €',44,GF_,'#fff'],1410,430,'seicentotrenta'),
  I('pill',['≈ 631 €',44,'#2B6F77','#fff'],1730,430,'seicentotrentuno'),
  I('bign',["OGGI, CON L'EXTRA",'619,80 €',null,{fs:84,minw:640,tfs:28}],480,590,'ai seicentodiciannove e ottanta di oggi'),
  I('bign',['DIFFERENZA VERA','+ 8 → + 11 €',null,{fs:84,fill:GF_,col:'#fff',subcol:'#fff',minw:680,tfs:28}],1260,620,'da otto a undici euro in più'),
  I('bign',['COME FA PENSARE LA PERCENTUALE','+ 16 → + 19 €',null,{fs:62,fill:'#fff',col:'#8A1F10',subcol:'#8A1F10',minw:760,tfs:26,stroke:RED_}],1260,800,'non da sedici a diciannove')]},
]);
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COSA MANCA NELLA TABELLA',cap:'ADDIZIONALI, ALTRI REDDITI, FAMILIARI A CARICO E L\'IRPEF DI OGGI',items:[
  I('icard',[560,330,'cal',[['ADDIZIONALI',38],['REGIONALI E COMUNALI',28,GRN],['SUL REDDITO',26],["DELL'ANNO PRIMA",26]],{lh:50,ir:62}],340,410,'Le addizionali regionali e comunali'),
  I('pill',["L'EFFETTO: L'ANNO DOPO",28,AMB,'#5A3300','next'],340,650,"l'effetto di questo aumento"),
  P('1–4 € OGNI 100 DI AUMENTO',340,745,'da uno a quattro euro su cento',DF_,26,'coin'),
  I('icard',[560,330,'people',[['ALTRI REDDITI',38],['E FAMILIARI A CARICO',30,GRN],['CON QUELLI',28],['IL NETTO CAMBIA',34,RED_]],{lh:52,ir:62}],960,410,'Mancano altri redditi'),
  I('icard',[560,330,'stato',[["L'IRPEF DI OGGI",38],["È QUELLA IN VIGORE",28,GRN],['SE LA MANOVRA LA CAMBIA:',26],['CAMBIA IL NETTO',34,RED_]],{lh:52,ir:62}],1580,410,"E l'Irpef è quella"),
  P("NON L'AUMENTO LORDO",1560,650,"non l'aumento lordo",GF_,28,'ok')]},
]);
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'COME CONTROLLI A GENNAIO',cap:'CONFRONTA LA PENSIONE LORDA DI GENNAIO CON QUELLA DI NOVEMBRE',items:[
  I('br',['inps.it · Mai Inps',860,390],470,410,'apri il cedolino su Mai Inps'),
  OV(I('row',['PENSIONE LORDA · GENNAIO',760,true],470,400,'la pensione lorda mensile')),
  OV(I('row',['PENSIONE LORDA · NOVEMBRE',760,true],470,500,'confrontata con quella di novembre')),
  P('LA DIFFERENZA = IL TUO AUMENTO',470,715,"ti dice l'aumento",AMB,34,'up'),
  I('icard',[640,170,'doc',[['UNA VOCE DI CONGUAGLIO?',32],['LEGGILA A PARTE',34,GRN]],{lh:46}],1420,330,'Una voce di conguaglio'),
  I('tl3',[500,[{icon:'doc',top:'DECRETO DI NOVEMBRE',sub:"L'ANNO SCORSO: 19 NOV",fill:DF_},{icon:'calc',top:'RIFACCIAMO IL CONTO',sub:'CON LA PERCENTUALE VERA',fill:'#1B9F81'}]],1370,640,'Il numero ufficiale arriva')]},
]);
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RIASSUMENDO',cap:'',items:[
  I('icard',[780,120,'up',[['LORDO = LA PERCENTUALE',34]],{lh:40,ir:46}],500,225,'Riassumendo'),
  I('icard',[780,120,'stato',[['NETTO = LE TASSE',36]],{lh:40,ir:46}],1420,225,'il netto dalle tasse'),
  I('pill',['FINO AL GRADINO: 7 € SU 10',30,GF_,'#fff','ok'],560,335,'Fino al gradino'),
  I('pill',['DOPO: QUASI 6,5 € SU 10',30,'#E39A1C','#4A2600','down'],1380,335,'dopo quasi sei e mezzo'),
  I('pill',["CON LA MINIMA: NIENTE IRPEF, MA L'EXTRA PUÒ SPARIRE",30,AMB,'#5A3300','warn'],960,405,'Con la minima'),
  I('pill',["L'ULTIMA PAROLA SPETTA AL DECRETO",30,DF_,'#fff','doc'],960,470,"L'ultima parola"),
  I('dbox',[1300,150,[["CANALE INFORMATIVO, NON CONSULENZA, NON AFFILIATO ALL'INPS",26,AMB],['VERIFICA SU INPS.IT O CON UN PATRONATO',28,'#fff']]],960,617,'Canale informativo')]},
]);
