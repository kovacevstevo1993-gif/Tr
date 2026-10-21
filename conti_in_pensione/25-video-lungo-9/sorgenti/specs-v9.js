// ===== VIDEO 8 (pensione all'estero) - motore b-sync-80: tempi calcolati su testo + durata del blocco =====
// Regole: scene >= 5 s, comparsa 0,9 s, nessun elemento sparisce nella scena, tutto completo entro l'80 %, poi fermo.
// Novita' del video 8 (N.37, non in serie): bandiere disegnate, passaporto, aereo e rotte, barre dell'Irpef,
// colonna della pensione che perde l'integrazione, barra verso i 1.000 iscritti, sfondo con rotte e mappamondo.
const SPECS={};
const GF_='url(#g_badge)',RF_='url(#g_red)',PF_='url(#g_paper)',DF_='#0B4A50';
const VT=(s,x,y,at,fill,fs)=>I('tag',[s,fill||AMB,(fill&&fill!==AMB)?'#fff':'#5A3300',fs||44],x,y,at);
const VN=(s,x,y,at,o)=>{o=o||{};return I('num',[s,o.fs||76,o.fill||PF_,o.sub,o.subfill,o.minw],x,y,at);};
BUILD.calS=(g,h,b,bs,sub,sc)=>{const w=el('g',{transform:'translate(0 '+(-250*sc)+') scale('+sc+')'},g);calendarPage(w,h,b,bs,sub);};
// larghezza stimata del testo (DejaVu Sans Bold)
const tw=(s,fs)=>{let w=0;for(const c of s){if(/[A-ZÀÈÉÌÒÙ0-9€%]/.test(c))w+=0.76;else if(c===' ')w+=0.34;else if(/[.,:;'’!·\-\/]/.test(c))w+=0.38;else w+=0.64;}return w*fs;};
// pillola con testo: il testo ha sempre il suo riquadro
function lab(g,s,x,y,fs,fill,col,minw){const w=Math.max(minw||0,tw(s,fs)+76);const h=fs*1.75;
 el('rect',{x:x-w/2,y:y-h/2,width:w,height:h,rx:h/2,fill:fill,stroke:'#fff','stroke-width':4,filter:'url(#g_sh3)'},g);
 txt(g,s,x,y+fs*0.36,fs,col||'#fff','bold');return w;}
function star5(p,cx,cy,r,fill){let d='';for(let i=0;i<10;i++){const a=-Math.PI/2+i*Math.PI/5,rr=i%2?r*0.42:r;d+=(i?'L':'M')+(cx+rr*Math.cos(a)).toFixed(1)+' '+(cy+rr*Math.sin(a)).toFixed(1)+' ';}
 return el('path',{d:d+'Z',fill:fill},p);}
// bandiere disegnate (stilizzate)
function flag(p,code,w,h){const g=el('g',{},p);const id='fc'+(++UID);const cp=el('clipPath',{id:id},g);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:12},cp);
 const f=el('g',{'clip-path':'url(#'+id+')'},g);const R=(x,y,ww,hh,c)=>el('rect',{x:x,y:y,width:ww,height:hh,fill:c},f);const x0=-w/2,y0=-h/2;
 if(code=='IT'){R(x0,y0,w/3+1,h,'#1F9A4B');R(x0+w/3,y0,w/3+1,h,'#F7F7F2');R(x0+2*w/3,y0,w/3+1,h,'#D7322B');}
 else if(code=='FR'){R(x0,y0,w/3+1,h,'#2340A0');R(x0+w/3,y0,w/3+1,h,'#F7F7F2');R(x0+2*w/3,y0,w/3+1,h,'#D7322B');}
 else if(code=='PT'){R(x0,y0,w*0.4+1,h,'#0B6E3B');R(x0+w*0.4,y0,w*0.6+1,h,'#D52B1E');el('circle',{cx:x0+w*0.4,cy:0,r:h*0.21,fill:'#F4C430',stroke:'#fff','stroke-width':3},f);el('circle',{cx:x0+w*0.4,cy:0,r:h*0.1,fill:'#D52B1E'},f);}
 else if(code=='ES'){R(x0,y0,w,h,'#C8102E');R(x0,y0+h/4,w,h/2,'#F6C700');}
 else if(code=='TN'){R(x0,y0,w,h,'#D21F2A');el('circle',{cx:0,cy:0,r:h*0.31,fill:'#fff'},f);el('circle',{cx:0,cy:0,r:h*0.23,fill:'#D21F2A'},f);el('circle',{cx:h*0.07,cy:0,r:h*0.19,fill:'#fff'},f);star5(f,h*0.06,0,h*0.13,'#D21F2A');}
 else if(code=='AL'){R(x0,y0,w,h,'#E41E20');const s=h/220;const e=el('g',{transform:'scale('+s+')',fill:'#111'},f);
  el('path',{d:'M0 -45 L20 0 L0 62 L-20 0 Z'},e);
  el('path',{d:'M-16 -30 L-92 -66 L-80 -34 L-104 -22 L-78 -4 L-96 14 L-66 18 L-74 36 L-16 22 Z'},e);
  el('path',{d:'M16 -30 L92 -66 L80 -34 L104 -22 L78 -4 L96 14 L66 18 L74 36 L16 22 Z'},e);
  el('circle',{cx:-15,cy:-58,r:12},e);el('circle',{cx:15,cy:-58,r:12},e);el('path',{d:'M-14 58 L0 92 L14 58 Z'},e);}
 else if(code=='EU'){R(x0,y0,w,h,'#1D3F9A');for(let i=0;i<12;i++){const a=i*Math.PI/6;star5(f,h*0.32*Math.cos(a),h*0.32*Math.sin(a),h*0.06,'#FFD319');}}
 el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:12,fill:'none',stroke:'#fff','stroke-width':6},g);g.setAttribute('filter','url(#g_sh2)');return g;}
function globe(p,r){const g=el('g',{filter:'url(#g_sh2)'},p);el('circle',{r:r,fill:'#1E9096',stroke:'#fff','stroke-width':6},g);
 [0.35,0.7].forEach(k=>el('ellipse',{rx:r*k,ry:r,fill:'none',stroke:'#BFFBEA','stroke-width':4,opacity:.8},g));el('line',{x1:0,y1:-r,x2:0,y2:r,stroke:'#BFFBEA','stroke-width':4,opacity:.8},g);
 [-0.5,0,0.5].forEach(k=>{const yy=r*k,xx=Math.sqrt(r*r-yy*yy);el('line',{x1:-xx,y1:yy,x2:xx,y2:yy,stroke:'#BFFBEA','stroke-width':4,opacity:.8},g);});return g;}
function planeIco(p,s,col){const g=el('g',{transform:'scale('+s+')',filter:'url(#g_sh2)'},p);
 el('path',{d:'M-110 0 Q-110 -16 -90 -16 L90 -16 Q130 -16 140 0 Q130 16 90 16 L-90 16 Q-110 16 -110 0 Z',fill:'#fff'},g);
 el('path',{d:'M-10 -14 L-60 -110 L-30 -110 L40 -14 Z M-10 14 L-60 110 L-30 110 L40 14 Z',fill:col||AMB},g);
 el('path',{d:'M-95 -12 L-120 -55 L-102 -55 L-75 -12 Z M-95 12 L-120 55 L-102 55 L-75 12 Z',fill:col||AMB},g);return g;}
// titoletto in alto CENTRATO con due rombi (variante del video 8)
function topLabel(g,s){const t=el('g',{},g);const w=tw(s,36)+s.length*9;
 el('polygon',{points:'0,-14 14,0 0,14 -14,0',fill:'#7FF0D2',transform:'translate('+(-w/2-30)+' 0)'},t);
 el('polygon',{points:'0,-14 14,0 0,14 -14,0',fill:'#7FF0D2',transform:'translate('+(w/2+30)+' 0)'},t);
 const x=txt(t,s,0,12,36,'#7FF0D2','bold','middle');x.setAttribute('letter-spacing','9');return t;}
// riga con spunta (o croce) e testo dentro la sua pillola
function rwW(label,fs){return tw(label,fs)+190;}
// ---- elementi nuovi ----
Object.assign(BUILD,{
 flg:(g,code,w,name,fs)=>{const h=w*2/3;flag(g,code,w,h);if(name)lab(g,name,0,h/2+(fs||40)*1.25,fs||40,DF_,'#fff');},
 cty:(g,code,name,line,fill,w)=>{w=w||640;const h=230;{const fw0=170;const need=60+fw0+40+Math.max(tw(name,44)+76,line?tw(line,32)+76:0)+40;if(need>w)w=need;}el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  const fw=170;const fg=el('g',{transform:'translate('+(-w/2+30+fw/2)+' 0)'},g);if(code=='GL')globe(fg,72);else flag(fg,code,fw,fw*2/3);
  const cx=(-w/2+60+fw+w/2-30)/2;lab(g,name,cx,line?-42:0,44,DF_,'#fff');if(line)lab(g,line,cx,52,32,fill||GF_,fill===AMB?'#5A3300':'#fff');},
 pass:(g,s)=>{s=s||1;const b=el('g',{transform:'scale('+s+')',filter:'url(#g_sh)'},g);
  el('rect',{x:-150,y:-210,width:300,height:420,rx:26,fill:'#0E4F3A',stroke:'#fff','stroke-width':6},b);el('rect',{x:-150,y:-210,width:30,height:420,rx:12,fill:'#0A3A2B'},b);
  el('circle',{cx:15,cy:10,r:70,fill:'none',stroke:'#E9C46A','stroke-width':8},b);star5(b,15,10,44,'#E9C46A');
  el('rect',{x:-75,y:-150,width:180,height:16,rx:8,fill:'#E9C46A'},b);el('rect',{x:-55,y:-118,width:140,height:12,rx:6,fill:'#E9C46A',opacity:.7},b);
  el('rect',{x:-60,y:120,width:150,height:40,rx:8,fill:'none',stroke:'#E9C46A','stroke-width':5},b);},
 suit:(g)=>{const b=el('g',{filter:'url(#g_sh)'},g);el('rect',{x:-60,y:-170,width:120,height:60,rx:24,fill:'none',stroke:'#0B4A50','stroke-width':16},b);
  el('rect',{x:-170,y:-120,width:340,height:250,rx:30,fill:AMB,stroke:'#fff','stroke-width':6},b);[-90,90].forEach(x=>el('rect',{x:x-12,y:-120,width:24,height:250,fill:'#E39A1C'},b));
  el('circle',{cx:-30,cy:10,r:34,fill:'#D21F2A',stroke:'#fff','stroke-width':4},b);el('rect',{x:20,y:-20,width:80,height:54,rx:8,fill:'#1F9A4B',stroke:'#fff','stroke-width':4},b);},
 plane:(g,s,col)=>planeIco(g,s||1,col),
 globe:(g,r)=>globe(g,r||150),
 goal:(g,W,frac)=>{W=W||1300;el('rect',{x:-W/2,y:-34,width:W,height:68,rx:34,fill:'#06303A',stroke:LT,'stroke-width':4,filter:'url(#g_sh2)'},g);
  el('rect',{x:-W/2+8,y:-26,width:(W-16)*frac,height:52,rx:26,fill:'url(#g_badge)'},g);
  for(let k=1;k<10;k++)el('rect',{x:-W/2+k*W/10-2,y:40,width:4,height:18,fill:'#fff',opacity:.6},g);
  const mx=-W/2+8+(W-16)*frac;el('path',{d:`M${mx-18} -62 L${mx+18} -62 L${mx} -38 Z`,fill:AMB},g);
  lab(g,'SIAMO QUI',mx,-104,34,AMB,'#5A3300');lab(g,'OBIETTIVO: 1.000 ISCRITTI',W/2-300,-104,34,GRN,'#fff');lab(g,'0',-W/2+40,100,30,DF_,'#fff');lab(g,'1.000',W/2-70,100,30,GRN,'#fff');},
 clock:(g,r)=>{r=r||120;const b=el('g',{filter:'url(#g_sh)'},g);el('circle',{r:r,fill:'url(#g_paper)',stroke:AMB,'stroke-width':12},b);
  for(let i=0;i<12;i++){const a=i*Math.PI/6;el('line',{x1:r*0.78*Math.cos(a),y1:r*0.78*Math.sin(a),x2:r*0.9*Math.cos(a),y2:r*0.9*Math.sin(a),stroke:INK,'stroke-width':6,'stroke-linecap':'round'},b);}
  el('line',{x1:0,y1:0,x2:0,y2:-r*0.62,stroke:INK,'stroke-width':12,'stroke-linecap':'round'},b);el('line',{x1:0,y1:0,x2:r*0.45,y2:r*0.2,stroke:RED_,'stroke-width':10,'stroke-linecap':'round'},b);el('circle',{r:12,fill:INK},b);},
 ico:(g,kind,label,w,h)=>{w=w||270;h=h||270;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  const ig=el('g',{transform:'translate(0 '+(-h*0.12)+')'},g);const C=INK;
  if(kind=='stato'){el('path',{d:'M-80 -30 L0 -80 L80 -30 Z',fill:C},ig);[-55,-20,15,50].forEach(x=>el('rect',{x:x-8,y:-25,width:16,height:70,fill:GRN},ig));el('rect',{x:-85,y:45,width:170,height:16,fill:C},ig);}
  else if(kind=='comune'){el('rect',{x:-70,y:-40,width:140,height:100,fill:GRN},ig);el('rect',{x:-20,y:-90,width:40,height:50,fill:C},ig);el('circle',{cx:0,cy:-65,r:12,fill:'#fff'},ig);[-40,0,40].forEach(x=>el('rect',{x:x-12,y:-15,width:24,height:30,fill:'#fff'},ig));el('rect',{x:-15,y:25,width:30,height:35,fill:C},ig);}
  else if(kind=='scuola'){el('path',{d:'M0 -40 Q-50 -70 -95 -50 L-95 50 Q-50 30 0 60 Q50 30 95 50 L95 -50 Q50 -70 0 -40 Z',fill:GRN,stroke:C,'stroke-width':6},ig);el('line',{x1:0,y1:-40,x2:0,y2:60,stroke:C,'stroke-width':6},ig);}
  else if(kind=='forze'){el('path',{d:'M0 -85 L70 -55 L70 10 Q70 60 0 90 Q-70 60 -70 10 L-70 -55 Z',fill:C},ig);star5(ig,0,0,42,AMB);}
  else if(kind=='casa'){el('path',{d:'M-90 0 L0 -80 L90 0 Z',fill:RED_},ig);el('rect',{x:-65,y:0,width:130,height:80,fill:GRN},ig);el('rect',{x:-15,y:25,width:30,height:55,fill:C},ig);}
  else if(kind=='sanita'){el('rect',{x:-30,y:-85,width:60,height:170,rx:10,fill:RED_},ig);el('rect',{x:-85,y:-30,width:170,height:60,rx:10,fill:RED_},ig);}
  else if(kind=='cuore'){el('path',{d:'M0 80 C-120 0 -80 -90 0 -40 C80 -90 120 0 0 80 Z',fill:RED_},ig);}
  else if(kind=='spesa'){el('path',{d:'M-90 -40 L90 -40 L65 70 L-65 70 Z',fill:AMB,stroke:C,'stroke-width':6},ig);el('path',{d:'M-55 -40 Q0 -120 55 -40',fill:'none',stroke:C,'stroke-width':10},ig);}
  else if(kind=='banca'){el('path',{d:'M-90 -30 L0 -85 L90 -30 Z',fill:C},ig);[-60,-20,20,60].forEach(x=>el('rect',{x:x-9,y:-25,width:18,height:75,fill:GRN},ig));el('rect',{x:-95,y:50,width:190,height:18,fill:C},ig);}
  lab(g,label,0,h/2-46,Math.min(34,(w-80)/Math.max(1,tw(label,1))),DF_,'#fff');},
 rw:(g,label,ok,fs,left)=>{fs=fs||36;const w=rwW(label,fs);if(left){g=el('g',{transform:'translate('+(w/2)+' 0)'},g);}el('rect',{x:-w/2,y:-42,width:w,height:84,rx:42,fill:'#D6F5EC',stroke:ok?'#1B9F81':RED_,'stroke-width':5,filter:'url(#g_sh3)'},g);
  const ix=-w/2+48;el('circle',{cx:ix,cy:0,r:28,fill:ok?'#1B9F81':RED_},g);
  if(ok)el('path',{d:'M'+(ix-14)+' 1 l9 10 l18 -20',fill:'none',stroke:'#fff','stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'},g);
  else el('path',{d:'M'+(ix-11)+' -11 l22 22 M'+(ix+11)+' -11 l-22 22',stroke:'#fff','stroke-width':8,'stroke-linecap':'round'},g);
  txt(g,label,-w/2+96,fs*0.36,fs,INK,'bold','start');},
 hbar:(g,label,frac,val,fill,W)=>{W=W||1500;const L=330,V=420;const A=W-L-V-40;
  el('rect',{x:-W/2,y:-62,width:W,height:124,rx:30,fill:'#06303A',opacity:.55},g);
  lab(g,label,-W/2+L/2+10,0,38,DF_,'#fff',L-20);
  el('rect',{x:-W/2+L+20,y:-30,width:A,height:60,rx:30,fill:'#0A3F45'},g);
  el('rect',{x:-W/2+L+20,y:-30,width:Math.max(60,A*frac),height:60,rx:30,fill:fill||RF_,stroke:'#fff','stroke-width':4},g);
  lab(g,val,W/2-V/2-10,0,40,'#fff',RED_,V-20);},
 pie5:(g,r)=>{r=r||170;const b=el('g',{filter:'url(#g_sh)'},g);for(let i=0;i<5;i++){const a0=-Math.PI/2+i*2*Math.PI/5,a1=a0+2*Math.PI/5;
   el('path',{d:`M0 0 L${r*Math.cos(a0)} ${r*Math.sin(a0)} A${r} ${r} 0 0 1 ${r*Math.cos(a1)} ${r*Math.sin(a1)} Z`,fill:i==0?AMB:'#2B6F77',stroke:'#fff','stroke-width':6},b);}
  lab(g,'TASSATO: SOLO 1/5',0,r+60,38,AMB,'#5A3300');},
 vb2:(g)=>{const H1=360,H2=70;el('rect',{x:-330,y:0,width:660,height:8,rx:4,fill:LT},g);
  el('rect',{x:-240,y:-H1,width:180,height:H1,rx:16,fill:'url(#g_red)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  el('rect',{x:60,y:-H2,width:180,height:H2,rx:16,fill:'url(#g_badge)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  lab(g,'IRPEF ITALIA',-150,60,32,DF_,'#fff');lab(g,'TUNISIA',150,60,32,DF_,'#fff');
  const f1=el('g',{transform:'translate(-150 '+(-H1-70)+')'},g);flag(f1,'IT',90,60);const f2=el('g',{transform:'translate(150 '+(-H2-70)+')'},g);flag(f2,'TN',90,60);},
 stack:(g,head,out)=>{const w=380;lab(g,head,0,-300,36,out?RF_:GF_,'#fff');
  el('rect',{x:-w/2,y:-30,width:w,height:250,rx:22,fill:'url(#g_badge)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);txt(g,'PENSIONE',0,108,44,'#fff','900');
  if(!out){el('rect',{x:-w/2,y:-220,width:w,height:170,rx:22,fill:AMB,stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);txt(g,'INTEGRAZIONE',0,-126,38,'#5A3300','900');txt(g,'AL MINIMO',0,-80,32,'#5A3300','bold');}
  else{el('rect',{x:-w/2,y:-220,width:w,height:170,rx:22,fill:'#06303A',stroke:RED_,'stroke-width':6,'stroke-dasharray':'22 14'},g);txt(g,'NON TI SEGUE',0,-122,36,'#FF8A75','900');}},
 years:(g)=>{const W=1400;el('rect',{x:-W/2,y:-8,width:W,height:16,rx:8,fill:LT},g);
  el('rect',{x:-W/2,y:-8,width:W/2,height:16,rx:8,fill:'#2FD0A8'},g);el('rect',{x:0,y:-8,width:W/2,height:16,rx:8,fill:RED_},g);el('circle',{r:26,fill:AMB,stroke:'#fff','stroke-width':6},g);
  lab(g,'FINO AL 2023',-W/4,-60,36,DF_,'#fff');lab(g,'ESENZIONE',-W/4,62,36,GRN,'#fff');lab(g,'DAL 2024',W/4,-60,36,DF_,'#fff');lab(g,'CHIUSO PER CHI ARRIVA',W/4,62,36,RED_,'#fff');},
 stairs:(g)=>{const hs=[80,150,220,290];hs.forEach((h,i)=>el('rect',{x:-260+i*130,y:-h,width:120,height:h,rx:12,fill:i==3?RED_:'#2B6F77',stroke:'#fff','stroke-width':4,filter:'url(#g_sh3)'},g));
  el('path',{d:'M-230 -120 L190 -330',stroke:AMB,'stroke-width':12,'stroke-linecap':'round'},g);el('path',{d:'M150 -340 L200 -335 L175 -290 Z',fill:AMB},g);
  lab(g,'IMPOSTA A SCAGLIONI',-5,60,36,DF_,'#fff');},
 env:(g,line)=>{const b=el('g',{filter:'url(#g_sh)'},g);el('rect',{x:-200,y:-130,width:400,height:260,rx:20,fill:'url(#g_paper)',stroke:'#fff','stroke-width':5},b);
  el('path',{d:'M-200 -120 L0 20 L200 -120',fill:'none',stroke:'#9FB4B9','stroke-width':8},b);el('circle',{cx:0,cy:20,r:30,fill:RED_},b);
  lab(g,line,0,190,32,DF_,'#fff');},
 lock:(g)=>{const b=el('g',{filter:'url(#g_sh)'},g);el('path',{d:'M-70 -20 V-80 Q-70 -150 0 -150 Q70 -150 70 -80 V-20',fill:'none',stroke:'url(#g_metal)','stroke-width':30},b);
  el('rect',{x:-110,y:-30,width:220,height:180,rx:26,fill:RED_,stroke:'#fff','stroke-width':6},b);el('circle',{cx:0,cy:45,r:24,fill:'#5A0E05'},b);el('rect',{x:-9,y:50,width:18,height:50,rx:9,fill:'#5A0E05'},b);},
 crow:(g,code,name,verdict,fill,W)=>{W=W||1500;el('rect',{x:-W/2,y:-56,width:W,height:112,rx:30,fill:'#06303A',opacity:.6},g);
  const fg=el('g',{transform:'translate('+(-W/2+90)+' 0)'},g);flag(fg,code,110,74);lab(g,name,-W/2+380,0,40,DF_,'#fff',300);
  lab(g,verdict,W/2-430,0,40,fill,fill===AMB?'#5A3300':'#fff',780);},
 xbig:(g,w)=>{el('path',{d:`M${-w} ${-w} L${w} ${w} M${w} ${-w} L${-w} ${w}`,stroke:RED_,'stroke-width':26,'stroke-linecap':'round'},g);},
});
// ===== VIDEO 9 (pensioni di dicembre: tredicesima, bonus 154,94, quattordicesima) =====
// Un po' diverso dai video 7-8 (N.37, N.47): titoletto a sinistra con calendarietto DIC e filetto, didascalia con bordo sottile,
// barra gialla e moneta €, personaggi disegnati (Franco, Anna, Lucia), cedolino di dicembre, righello della soglia,
// barra di coppia, striscia dei mesi, tabella della quattordicesima, griglia finale, telefono My Inps, sfondo di dicembre.
function topLabel(g,s){const t=el('g',{transform:'translate(-840 0)'},g);
 el('rect',{x:-34,y:-38,width:68,height:74,rx:12,fill:'url(#g_paper)',filter:'url(#g_sh3)'},t);
 el('rect',{x:-34,y:-38,width:68,height:26,rx:10,fill:RED_},t);el('rect',{x:-34,y:-22,width:68,height:10,fill:RED_},t);
 txt(t,'DIC',0,-18,17,'#fff','bold');txt(t,'1',0,28,34,INK,'900');
 const x=txt(t,s,62,12,36,'#7FF0D2','bold','start');x.setAttribute('letter-spacing','6');
 const w=tw(s,36)+s.length*6;el('line',{x1:62+w+30,y1:0,x2:1680,y2:0,stroke:'#7FF0D2','stroke-width':3,opacity:.35},t);
 el('circle',{cx:1680,cy:0,r:7,fill:'#7FF0D2',opacity:.6},t);return t;}
function cap(g,s,size){size=size||44;size=Math.min(size,1540/Math.max(1,tw(s,1)));const w=Math.min(1820,tw(s,size)+230);const c=el('g',{},g);
 el('rect',{x:-w/2,y:-56,width:w,height:112,rx:26,fill:'#06303A',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:-56,width:w,height:112,rx:26,fill:'none',stroke:'#7FF0D2','stroke-width':3,opacity:.55},c);
 el('rect',{x:-w/2,y:-56,width:18,height:112,rx:9,fill:AMB},c);
 el('circle',{cx:-w/2+78,cy:0,r:32,fill:AMB,stroke:'#fff','stroke-width':4},c);txt(c,'€',-w/2+78,13,38,'#5A3300','900');
 txt(c,s,(-w/2+125+w/2-30)/2,size*0.36,size,'#FFFFFF','bold');return c;}
// personaggio disegnato (stilizzato, nessuna persona reale)
function person(p,kind,col,r){r=r||110;const g=el('g',{filter:'url(#g_sh)'},p);
 const id='pc'+(++UID);const cp=el('clipPath',{id:id},g);el('circle',{r:r},cp);
 el('circle',{r:r,fill:'#0E5A60'},g);const f=el('g',{'clip-path':'url(#'+id+')'},g);
 const SK='#F1D9C4';
 el('path',{d:`M${-r*0.9} ${r} Q${-r*0.85} ${r*0.3} 0 ${r*0.26} Q${r*0.85} ${r*0.3} ${r*0.9} ${r} Z`,fill:col},f);
 el('rect',{x:-r*0.12,y:r*0.02,width:r*0.24,height:r*0.28,fill:SK},f);
 if(kind=='A')el('circle',{cx:0,cy:-r*0.6,r:r*0.19,fill:'#6B4A3A'},f);
 el('ellipse',{cx:0,cy:-r*0.18,rx:r*0.3,ry:r*0.35,fill:SK},f);
 if(kind=='A')el('path',{d:`M${-r*0.33} ${-r*0.1} Q${-r*0.38} ${-r*0.58} 0 ${-r*0.58} Q${r*0.38} ${-r*0.58} ${r*0.33} ${-r*0.1} Q${r*0.22} ${-r*0.42} 0 ${-r*0.42} Q${-r*0.22} ${-r*0.42} ${-r*0.33} ${-r*0.1} Z`,fill:'#6B4A3A'},f);
 if(kind=='L')el('path',{d:`M${-r*0.38} ${r*0.06} Q${-r*0.44} ${-r*0.62} 0 ${-r*0.58} Q${r*0.44} ${-r*0.62} ${r*0.38} ${r*0.06} L${r*0.27} ${r*0.06} Q${r*0.27} ${-r*0.38} 0 ${-r*0.38} Q${-r*0.27} ${-r*0.38} ${-r*0.27} ${r*0.06} Z`,fill:'#D5DBDE'},f);
 if(kind=='F'||kind=='M'){const hc=kind=='F'?'#C9D3D6':'#5B4A42';
  [-1,1].forEach(s=>el('path',{d:`M${s*r*0.31} ${-r*0.16} Q${s*r*0.34} ${-r*0.46} ${s*r*0.16} ${-r*0.5}`,fill:'none',stroke:hc,'stroke-width':r*0.1,'stroke-linecap':'round'},f));
  if(kind=='M')el('path',{d:`M${-r*0.28} ${-r*0.36} Q0 ${-r*0.66} ${r*0.28} ${-r*0.36} Q0 ${-r*0.5} ${-r*0.28} ${-r*0.36} Z`,fill:hc},f);}
 if(kind=='F'){[-1,1].forEach(s=>el('circle',{cx:s*r*0.13,cy:-r*0.2,r:r*0.09,fill:'none',stroke:INK,'stroke-width':r*0.035},f));el('line',{x1:-r*0.04,y1:-r*0.2,x2:r*0.04,y2:-r*0.2,stroke:INK,'stroke-width':r*0.035},f);}
 [-1,1].forEach(s=>el('circle',{cx:s*r*0.12,cy:-r*0.2,r:r*0.032,fill:INK},f));
 el('path',{d:`M${-r*0.1} ${-r*0.01} Q0 ${r*0.07} ${r*0.1} ${-r*0.01}`,fill:'none',stroke:INK,'stroke-width':r*0.032,'stroke-linecap':'round'},f);
 el('circle',{r:r,fill:'none',stroke:'#fff','stroke-width':r*0.07},g);el('circle',{r:r*1.08,fill:'none',stroke:col,'stroke-width':r*0.06},g);return g;}
const PCOL={F:'#2B8FA0',A:'#1B9F81',L:'#E39A1C',M:'#5C7C86'};
const RX=v=>-700+(v-7700)/600*1400;
const MESI='GFMAMGLASOND';
Object.assign(BUILD,{
 per:(g,kind,name,sub,r,subfill)=>{r=r||110;person(g,kind,PCOL[kind],r);if(name)lab(g,name,0,r+48,Math.min(40,r*0.42),DF_,'#fff');
  if(sub)lab(g,sub,0,r+48+Math.min(40,r*0.42)*1.9,30,subfill||GF_,subfill===AMB?'#5A3300':'#fff');},
 coin:(g,big,r,col,fs)=>{r=r||95;col=col||AMB;const b=el('g',{filter:'url(#g_sh2)'},g);el('circle',{r:r,fill:col,stroke:'#fff','stroke-width':8},b);
  el('circle',{r:r*0.8,fill:'none',stroke:'#fff','stroke-width':3,opacity:.6},b);txt(g,big,0,(fs||44)*0.36,fs||44,col===AMB?'#5A3300':'#fff','900');},
 ced:(g,title,rows,w)=>{w=w||600;const rh=78,h=118+rows.length*rh+24;const b=el('g',{filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:24,fill:'url(#g_paper)'},b);
  el('rect',{x:-w/2,y:-h/2,width:w,height:86,rx:24,fill:GRN},b);el('rect',{x:-w/2,y:-h/2+52,width:w,height:34,fill:GRN},b);
  txt(g,title,0,-h/2+56,32,'#fff','bold');
  rows.forEach((r,i)=>{const y=-h/2+112+i*rh+rh/2;if(i)el('line',{x1:-w/2+30,y1:y-rh/2,x2:w/2-30,y2:y-rh/2,stroke:'#C3D3D7','stroke-width':3,'stroke-dasharray':'8 8'},g);
   txt(g,r[0],-w/2+36,y+11,32,INK,'bold','start');txt(g,r[1],w/2-36,y+12,36,r[2]||INK,'900','end');});},
 rul:(g)=>{const W=1400;const id='rc'+(++UID);const cp=el('clipPath',{id:id},g);el('rect',{x:-W/2,y:-26,width:W,height:52,rx:26},cp);
  const z=el('g',{'clip-path':'url(#'+id+')'},g);const Z=(a,b,c)=>el('rect',{x:RX(a),y:-26,width:RX(b)-RX(a),height:52,fill:c},z);
  Z(7700,7954.05,'#2FD0A8');Z(7954.05,8108.99,AMB);Z(8108.99,8300,RED_);
  el('rect',{x:-W/2,y:-26,width:W,height:52,rx:26,fill:'none',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  [7954.05,8108.99].forEach(v=>el('line',{x1:RX(v),y1:-40,x2:RX(v),y2:126,stroke:'#fff','stroke-width':5,'stroke-dasharray':'10 8'},g));},
 mk:(g,s,col,h,fs)=>{h=h||130;fs=fs||32;col=col||AMB;el('line',{x1:0,y1:-26,x2:0,y2:-h+28,stroke:'#fff','stroke-width':5},g);
  el('circle',{cx:0,cy:-26,r:14,fill:col,stroke:'#fff','stroke-width':5},g);lab(g,s,0,-h,fs,col,col===AMB?'#5A3300':'#fff');},
 sbar:(g,a,b,ok,la,lb)=>{const W=1400,M=26000;const X=v=>-W/2+v/M*W;const lim=23862.15;
  el('rect',{x:-W/2,y:-42,width:W,height:84,rx:22,fill:'#06303A',stroke:LT,'stroke-width':3},g);
  el('rect',{x:X(0)+8,y:-32,width:X(a)-X(0)-8,height:64,rx:16,fill:AMB},g);
  el('rect',{x:X(a)+4,y:-32,width:X(a+b)-X(a)-4,height:64,rx:16,fill:ok?'#2FD0A8':RED_},g);
  txt(g,la,(X(0)+X(a))/2,11,30,'#5A3300','900');txt(g,lb,(X(a)+X(a+b))/2,11,30,ok?'#06303A':'#fff','900');
  el('line',{x1:X(lim),y1:-74,x2:X(lim),y2:74,stroke:'#fff','stroke-width':6,'stroke-dasharray':'14 10'},g);
  lab(g,'LIMITE DI COPPIA 23.862,15 €',X(lim)-250,-112,30,DF_,'#fff');
  lab(g,'TOTALE '+(a+b).toLocaleString('it-IT',{minimumFractionDigits:0,maximumFractionDigits:0})+' €',X(lim)-250,112,32,ok?GF_:RF_,'#fff');},
 mon:(g,ranges,W,fs)=>{W=W||1320;fs=fs||38;const cw=W/12;
  for(let i=0;i<12;i++){const x=-W/2+i*cw;let col=null;ranges.forEach(r=>{if(i>=r[0]&&i<=r[1])col=r[2];});
   el('rect',{x:x+4,y:-40,width:cw-8,height:80,rx:14,fill:col||'#0A3F45',stroke:col?'#fff':'#2B6F77','stroke-width':3},g);
   txt(g,MESI[i],x+cw/2,fs*0.36,fs,col?(col===AMB?'#5A3300':'#fff'):'#7FA8AE','900');}
  ranges.forEach(r=>{if(r[3])lab(g,r[3],-W/2+(r[0]+r[1]+1)*cw/2,-92,30,r[2],r[2]===AMB?'#5A3300':'#fff');});},
 qtab:(g)=>{const W=1500,c0=440,c1=(W-c0)/2,rh=92,H=rh*4;el('rect',{x:-W/2,y:-H/2,width:W,height:H,rx:24,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  el('rect',{x:-W/2,y:-H/2,width:W,height:rh,rx:24,fill:GRN},g);el('rect',{x:-W/2,y:-H/2+rh-30,width:W,height:30,fill:GRN},g);
  const hx=[-W/2+c0/2,-W/2+c0+c1/2,-W/2+c0+c1*1.5];
  txt(g,'ANNI DI CONTRIBUTI',hx[0],-H/2+58,28,'#fff','bold');txt(g,'REDDITO FINO A 11.931 €',hx[1],-H/2+58,28,'#fff','bold');txt(g,'DA 11.931 A 15.908 €',hx[2],-H/2+58,28,'#fff','bold');
  el('line',{x1:-W/2+c0,y1:-H/2+rh,x2:-W/2+c0,y2:H/2-16,stroke:'#C3D3D7','stroke-width':3},g);el('line',{x1:-W/2+c0+c1,y1:-H/2+rh,x2:-W/2+c0+c1,y2:H/2-16,stroke:'#C3D3D7','stroke-width':3},g);
  ['FINO A 15','DA 15 A 25','OLTRE 25'].forEach((s,i)=>{const y=-H/2+rh*(i+1)+rh/2;if(i)el('line',{x1:-W/2+20,y1:y-rh/2,x2:W/2-20,y2:y-rh/2,stroke:'#C3D3D7','stroke-width':3},g);txt(g,s,hx[0],y+11,32,INK,'bold');});},
 tv:(g,s,col,fs)=>txt(g,s,0,(fs||46)*0.36,fs||46,col||GRN,'900'),
 ghead:(g)=>{const W=1500;el('rect',{x:-W/2,y:-44,width:W,height:88,rx:22,fill:GRN,filter:'url(#g_sh2)'},g);
  [['VICINO',-W/2+190],['TREDICESIMA',-W/2+560],['BONUS 154,94 €',-W/2+900],['QUATTORDICESIMA',-W/2+1260]].forEach(([s,x])=>txt(g,s,x,11,30,'#fff','bold'));},
 grow:(g,kind,name,cells)=>{const W=1500;el('rect',{x:-W/2,y:-56,width:W,height:112,rx:22,fill:'url(#g_paper)',filter:'url(#g_sh2)'},g);
  const pg=el('g',{transform:'translate('+(-W/2+90)+' 0)'},g);person(pg,kind,PCOL[kind],42);txt(g,name,-W/2+150,12,34,INK,'900','start');
  [-W/2+560,-W/2+900,-W/2+1260].forEach((x,i)=>{const c=cells[i];
   if(c=='si'){el('circle',{cx:x,cy:0,r:30,fill:'#1B9F81'},g);el('path',{d:`M${x-15} 1 l10 11 l20 -22`,fill:'none',stroke:'#fff','stroke-width':8,'stroke-linecap':'round','stroke-linejoin':'round'},g);}
   else if(c=='no'){el('circle',{cx:x,cy:0,r:30,fill:RED_},g);el('path',{d:`M${x-12} -12 l24 24 M${x+12} -12 l-24 24`,stroke:'#fff','stroke-width':8,'stroke-linecap':'round'},g);}
   else lab(g,c,x,0,30,AMB,'#5A3300');});},
 phone:(g,rows)=>{const w=380,h=640;const b=el('g',{filter:'url(#g_sh)'},g);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:48,fill:'#06303A',stroke:'#fff','stroke-width':6},b);
  el('rect',{x:-w/2+18,y:-h/2+60,width:w-36,height:h-120,rx:18,fill:'url(#g_paper)'},b);el('rect',{x:-40,y:-h/2+24,width:80,height:12,rx:6,fill:'#2B6F77'},b);
  el('rect',{x:-w/2+18,y:-h/2+60,width:w-36,height:86,rx:18,fill:GRN},b);el('rect',{x:-w/2+18,y:-h/2+120,width:w-36,height:26,fill:GRN},b);
  txt(g,'MY INPS',0,-h/2+114,34,'#fff','900');txt(g,'CEDOLINO DI DICEMBRE',0,-h/2+190,24,INK,'bold');
  rows.forEach((r,i)=>{const y=-h/2+250+i*84;el('rect',{x:-w/2+38,y:y-30,width:w-76,height:62,rx:14,fill:'#D6F5EC',stroke:'#1B9F81','stroke-width':3},g);txt(g,r,-w/2+58,y+10,26,INK,'bold','start');});},
 stp:(g,n,s1,s2,w)=>{w=w||330;const h=250;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:26,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  circN(g,40,n,'url(#g_badge)').setAttribute('transform','translate(0 '+(-h/2)+')');
  txt(g,s1,0,10,32,INK,'900');if(s2)txt(g,s2,0,56,28,GRN,'bold');},
 lim:(g,title,two,val,sub)=>{const w=640,h=470;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:28,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  el('rect',{x:-w/2,y:-h/2,width:w,height:84,rx:28,fill:GRN},g);el('rect',{x:-w/2,y:-h/2+54,width:w,height:30,fill:GRN},g);txt(g,title,0,-h/2+56,34,'#fff','bold');
  if(two){const a=el('g',{transform:'translate(-70 -55)'},g);person(a,'A',PCOL.A,70);const m=el('g',{transform:'translate(70 -55)'},g);person(m,'M',PCOL.M,70);}
  else{const a=el('g',{transform:'translate(0 -55)'},g);person(a,'A',PCOL.A,70);}
  txt(g,val,0,100,64,INK,'900');txt(g,sub,0,158,28,GRN,'bold');},
 crowd:(g,cols,rowsN,col)=>{const b=el('g',{},g);for(let r=0;r<rowsN;r++)for(let c=0;c<cols;c++){const x=(c-(cols-1)/2)*58,y=(r-(rowsN-1)/2)*70;
   el('circle',{cx:x,cy:y-18,r:14,fill:col||LT,opacity:.9},b);el('path',{d:`M${x-22} ${y+24} Q${x-22} ${y-2} ${x} ${y-2} Q${x+22} ${y-2} ${x+22} ${y+24} Z`,fill:col||LT,opacity:.9},b);}},
 vid:(g,s1,s2)=>{const w=480,h=290;const b=el('g',{filter:'url(#g_sh)'},g);el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:24,fill:'#06303A',stroke:'#fff','stroke-width':6},b);
  el('rect',{x:-w/2+20,y:h/2-34,width:w-40,height:10,rx:5,fill:'#2B6F77'},b);el('rect',{x:-w/2+20,y:h/2-34,width:(w-40)*0.62,height:10,rx:5,fill:RED_},b);
  el('circle',{cx:0,cy:-30,r:56,fill:RED_,stroke:'#fff','stroke-width':5},b);el('path',{d:'M-16 -58 L30 -30 L-16 -2 Z',fill:'#fff'},b);
  txt(g,s1,0,72,34,'#fff','900');if(s2)txt(g,s2,0,108,24,LT,'bold');},
 tax2:(g)=>{const base=0;el('rect',{x:-330,y:0,width:660,height:8,rx:4,fill:LT},g);
  el('rect',{x:-230,y:-150,width:170,height:150,rx:16,fill:'#2B6F77',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  el('rect',{x:60,y:-290,width:170,height:290,rx:16,fill:'url(#g_red)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
  txt(g,'TASSE',-145,-170,28,LT,'bold');txt(g,'TASSE',145,-310,28,'#FFB4A6','bold');
  lab(g,'RATA NORMALE',-145,60,30,DF_,'#fff');lab(g,'TREDICESIMA',145,60,30,DF_,'#fff');},
 posta:(g,label)=>{const w=270,h=270;el('rect',{x:-w/2,y:-h/2,width:w,height:h,rx:30,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
  const ig=el('g',{transform:'translate(0 -32)'},g);el('rect',{x:-90,y:-60,width:180,height:120,rx:12,fill:AMB,stroke:INK,'stroke-width':6},ig);
  el('path',{d:'M-90 -56 L0 10 L90 -56',fill:'none',stroke:INK,'stroke-width':6},ig);lab(g,label,0,h/2-46,32,DF_,'#fff');},
});
const GN=(s,x,y,at,col,fs)=>I('tv',[s,col,fs],x,y,at);
// ---------- BLOCCO 1 (619 f = 20,6 s) ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'DICEMBRE: TRE VICINI DI CASA',cap:'QUASI LA STESSA PENSIONE, MA TRE DICEMBRI DIVERSI',items:[
  I('per',['F','FRANCO',null,105],460,330,'Franco'),
  I('per',['A','ANNA',null,105],960,330,'Anna'),
  I('per',['L','LUCIA',null,105],1460,330,'Lucia'),
  I('calS',['DICEMBRE','1',150,'MARTEDÌ',0.42],700,760,'Martedì primo dicembre'),
  VT('LA RATA ARRIVA A TUTTI E TRE',1180,690,'arriva a tutti e tre',GF_,38)]},
 {at:'Ma uno troverà',top:'COSA TROVERANNO NELLA RATA',cap:'ALLA FINE CAPISCI QUALE DEI TRE SEI TU',items:[
  I('q',[56],330,290,'Ma uno troverà'),I('coin',['13ª',70],560,290,['solo la tredicesima',-0.3]),
  VT('SOLO LA TREDICESIMA',1180,290,'solo la tredicesima',DF_,38),
  I('q',[56],330,490,'Una troverà anche'),I('coin',['13ª',70],560,490,['Una troverà anche',0.1]),I('coin',['BONUS',70,GRN,28],740,490,'un bonus'),
  VT('+ BONUS DI 154,94 €',1180,490,'centocinquantaquattro euro',GF_,38),
  I('q',[56],330,690,'E una troverà'),I('coin',['13ª',70],560,690,['E una troverà',0.1]),I('coin',['BONUS',70,GRN,28],740,690,['tre soldi',-0.2]),I('coin',['14ª',70,RED_],920,690,'tre soldi'),
  VT('TRE PAGAMENTI NELLA STESSA RATA',1260,690,'nella stessa rata',AMB,36)]},
]);
// ---------- BLOCCO 2 (618 f = 20,6 s) ----------
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUELLO CHE HANNO IN COMUNE',cap:'LA PENSIONE SI PAGA IL PRIMO GIORNO BANCABILE DEL MESE',items:[
  I('per',['F',null,null,62],760,250,'Partiamo da quello'),I('per',['A',null,null,62],960,250,['Partiamo da quello',0.15]),I('per',['L',null,null,62],1160,250,['Partiamo da quello',0.3]),
  I('calS',['DICEMBRE 2026','1',170,'MARTEDÌ',0.5],460,690,'martedì primo dicembre'),
  I('ico',['banca','IN BANCA',280,280],1060,600,'in banca'),
  I('posta',['ALLE POSTE'],1440,600,'alle Poste')]},
 {at:'In quella rata',top:'NELLA RATA DI DICEMBRE',cap:'NIENTE ADDIZIONALI E IN PIÙ LA TREDICESIMA, SENZA DOMANDA',items:[
  I('mon',[[[0,10,RED_,'ADDIZIONALI: 11 RATE, GENNAIO-NOVEMBRE'],[11,11,GRN]],900,32],600,330,'trattenute delle addizionali'),
  VT('DICEMBRE: NESSUNA TRATTENUTA',600,500,'non ci sono più',GF_,36),
  I('ced',['CEDOLINO DI DICEMBRE',[['Addizionali','0 €',GRN],['Tredicesima','+1 RATA',GRN]],560],1400,400,'E c\'è la tredicesima'),
  VT('13ª: UNA RATA IN PIÙ, LORDA',600,660,'una rata in più',AMB,38),
  I('chk',[60],1180,700,'senza fare domanda'),VT('SENZA DOMANDA',1450,700,['senza fare domanda',0.15],GF_,38)]},
]);
// ---------- BLOCCO 3 (709 f = 23,6 s) ----------
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA TREDICESIMA E LE TASSE',cap:'IL NETTO PENSIONE PER PENSIONE: C\'È UN VIDEO INTERO SUL CANALE',items:[
  I('tax2',[],560,560,'le tasse pesano più'),
  VT('PIÙ TASSE CHE SU UNA RATA NORMALE',560,240,'che su una rata normale',RF_,34),
  I('vid',['TREDICESIMA: IL NETTO','PENSIONE PER PENSIONE'],1360,430,'in un video intero'),
  VT('LO TROVI SUL CANALE',1360,700,'che trovi sul canale',GF_,38)]},
 {at:'Oggi guardiamo',top:'IL SECONDO PAGAMENTO: IL BONUS',cap:'L\'ANNO SCORSO L\'IMPORTO AGGIUNTIVO È ANDATO A OLTRE 400.000 PENSIONATI',items:[
  VT('OGGI: GLI ALTRI DUE PAGAMENTI',560,220,'Oggi guardiamo',DF_,34),
  VN('154,94 €',560,400,'centocinquantaquattro euro',{fs:92,sub:'IMPORTO AGGIUNTIVO',minw:560}),
  I('doc',['PREVISTO PER LEGGE',440,230,GRN,34],560,700,'previsto per legge'),
  VT('L\'ANNO SCORSO',1380,230,'L\'anno scorso',AMB,36),
  I('crowd',[9,4,LT],1380,450,'l\'hanno ricevuto'),
  VN('OLTRE 400.000',1380,700,'più di quattrocentomila',{fs:62,sub:'PENSIONATI',fill:GF_,minw:520})]},
]);
// ---------- BLOCCO 4 (642 f = 21,4 s) ----------
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'FRANCO',cap:'SEMBRA IL CANDIDATO PERFETTO PER IL BONUS. INVECE: ZERO',items:[
  I('per',['F','FRANCO','630 € AL MESE',130],430,370,'Franco prende'),
  VN('630 €',1000,290,'seicentotrenta euro',{fs:84,sub:'PENSIONE AL MESE',minw:440}),
  I('rw',['È solo',true,38,true],760,520,'È solo'),
  I('rw',['Nessun altro reddito',true,38,true],760,640,'non ha altri redditi'),
  VT('CANDIDATO PERFETTO?',1480,300,'candidato perfetto',AMB,36),
  I('stamp',['BONUS: 0 €',RED_,56],1480,600,'prenderà zero')]},
 {at:'Il motivo',top:'CONDIZIONE 1: LA PENSIONE',cap:'TRATTAMENTO MINIMO 2026: 611,85 € AL MESE, CIOÈ 7.954,05 € L\'ANNO',items:[
  I('circ',['1'],300,250,'Il motivo'),VT('PRIMA CONDIZIONE: LA PENSIONE',820,250,'la prima condizione',AMB,38),
  VN('611,85 €',560,520,'seicentoundici euro',{fs:84,sub:'TRATTAMENTO MINIMO AL MESE',minw:560}),
  I('arR',[],960,520,'cioè'),
  VN('7.954,05 €',1360,520,'settemilanovecentocinquantaquattro',{fs:84,sub:'ALL\'ANNO',fill:GF_,minw:560}),
  VT('ANNO 2026',960,740,'del duemilaventisei',DF_,34)]},
]);
// ---------- BLOCCO 5 (685 f = 22,8 s) ----------
const ZL=(s,v,at,fill)=>I('tag',[s,fill,fill===AMB?'#5A3300':'#fff',30],960+RX(v),620,at);
const BP=(s,v,at)=>I('tag',[s,DF_,'#fff',30],960+RX(v),710,at);
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA SOGLIA DELLA PENSIONE',cap:'FINO A 7.954,05 € INTERO, FINO A 8.108,99 € UNA PARTE, SOPRA NIENTE',items:[
  VT('PENSIONE DI UN ANNO',960,260,'in un anno',DF_,36),
  I('rul',[],960,540,'non supera questa cifra'),
  ZL('INTERO',7827,'può essere intero','url(#g_badge)'),BP('7.954,05 €',7954.05,['può essere intero',0.3]),
  ZL('UNA PARTE',8031.5,'se ne prende una parte',AMB),BP('8.108,99 €',8108.99,'fino a ottomilacentootto'),
  ZL('NIENTE',8204,['se ne prende una parte',0.5],RF_),
  VT('IL BONUS SCENDE PIANO PIANO FINO A ZERO',960,380,['se ne prende una parte',0.9],AMB,32)]},
 {at:'Franco, in un anno',top:'FRANCO E LA SOGLIA',cap:'PER DIECI EURO AL MESE IN PIÙ, IL BONUS SPARISCE',items:[
  I('rul',[],960,540,'Franco, in un anno'),
  ZL('INTERO',7827,['Franco, in un anno',0.1],'url(#g_badge)'),ZL('UNA PARTE',8031.5,['Franco, in un anno',0.2],AMB),ZL('NIENTE',8204,['Franco, in un anno',0.3],RF_),
  I('mk',['FRANCO: 8.190 €',RED_,140],960+RX(8190),540,'ottomilacentonovanta'),
  I('mk',['620 € AL MESE = 8.060 €',AMB,230],960+RX(8060),540,'Con seicentoventi'),
  VN('48,99 €',470,300,'quarantotto euro',{fs:72,sub:'AVREBBE PRESO',fill:GF_,minw:420}),
  BP('7.954,05 €',7954.05,['Per dieci euro',-0.2]),BP('8.108,99 €',8108.99,['Per dieci euro',0])]},
]);
// ---------- BLOCCO 6 (613 f = 20,4 s) - richiesta di iscrizione dopo il primo conto ----------
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PRIMA DI ANDARE AVANTI',cap:'CONTI FATTI CON I LIMITI VERI DELL\'INPS: ORE DI LAVORO PER OGNI VIDEO',items:[
  I('per',['F','FRANCO',null,110],380,380,'Franco resta senza bonus'),
  VT('SENZA BONUS PER 10 € AL MESE',380,640,'per dieci euro al mese',RF_,32),
  I('clock',[115],960,420,'ci prendono ore'),VT('ORE PER OGNI VIDEO',960,640,['ci prendono ore',0.2],AMB,36),
  I('doc',['LIMITI UFFICIALI INPS',420,300,GRN,30],1500,450,'i limiti veri')]},
 {at:'Se ti sono serviti',top:'ISCRIVITI: È GRATIS',cap:'VOGLIAMO ARRIVARE A 1.000 ISCRITTI: CI SERVE IL TUO AIUTO',items:[
  I('btn',['ISCRIVITI'],560,270,'iscriviti adesso'),
  VT('GRATIS, BASTA UN TOCCO',560,420,'è gratis',GF_,36),
  I('per',['A','ANNA',null,72],1260,270,'prima di vedere Anna'),I('per',['L','LUCIA',null,72],1560,270,['prima di vedere Anna',0.2]),
  VT('I PROSSIMI CONTI NELLA PAGINA INIZIALE',1180,500,'pagina iniziale',AMB,30),
  I('goal',[1300,0.25],960,730,'Vogliamo arrivare a mille')]},
]);
// ---------- BLOCCO 7 (732 f = 24,4 s) ----------
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ANNA',cap:'ANNA PRENDE IL MINIMO: LA SUA PENSIONE VA BENE',items:[
  I('per',['A','ANNA','611,85 € AL MESE',130],430,370,'Anna prende il minimo'),
  VN('611,85 €',1050,290,'seicentoundici euro',{fs:84,sub:'IL MINIMO',minw:440}),
  I('rw',['Condizione 1: la pensione',true,36,true],790,520,'la sua pensione va bene'),
  I('circ',['2'],830,690,'la seconda condizione'),VT('CONDIZIONE 2: IL REDDITO',1250,690,'il reddito',AMB,38)]},
 {at:'Se sei solo',top:'CONDIZIONE 2: IL REDDITO',cap:'SE SEI SPOSATO, OLTRE AL LIMITE DI COPPIA RESTA ANCHE QUELLO PERSONALE',items:[
  I('lim',['SE SEI SOLO',false,'11.931,08 €','REDDITO IRPEF, PENSIONE COMPRESA'],560,450,'Se sei solo'),
  I('lim',['SE SEI SPOSATO',true,'23.862,15 €','LIMITE DI COPPIA'],1360,450,'Se sei sposato'),
  VT('+ RESTA IL LIMITE PERSONALE',1360,770,'resta anche il limite personale',AMB,34)]},
]);
// ---------- BLOCCO 8 (721 f = 24,0 s) ----------
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ANNA E IL MARITO',cap:'INSIEME SONO SOTTO IL LIMITE: ANNA PRENDE IL BONUS INTERO',items:[
  I('per',['A','ANNA',null,85],300,290,'Il marito di Anna'),I('per',['M','MARITO',null,85],560,290,['Il marito di Anna',0.2]),
  VN('1.200 €',1240,280,'milleduecento euro',{fs:76,sub:'AL MESE = 15.600 € L\'ANNO',minw:520}),
  I('sbar',[7954.05,15600,true,'ANNA 7.954 €','MARITO 15.600 €'],960,620,'Insieme fanno'),
  I('stamp',['BONUS INTERO',GRN,44],1580,780,'prende il bonus intero')]},
 {at:'Se il marito prendesse',top:'E SE IL MARITO PRENDESSE 50 € IN PIÙ?',cap:'CINQUANTA EURO DEL MARITO, E IL BONUS SPARIREBBE',items:[
  VT('+ 50 € AL MESE',360,280,'Se il marito prendesse',AMB,40),
  VN('1.250 €',1050,280,'milleduecentocinquanta',{fs:76,sub:'AL MESE = 16.250 € L\'ANNO',minw:520}),
  I('sbar',[7954.05,16250,false,'ANNA 7.954 €','MARITO 16.250 €'],960,620,'la coppia arriverebbe'),
  I('stamp',['BONUS: 0 €',RED_,44],1580,780,'bonus zero')]},
]);
// ---------- BLOCCO 9 (631 f = 21,0 s) ----------
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'ANNA NON DEVE FARE NIENTE',cap:'L\'INPS LO PAGA DA SOLO, IN VIA PROVVISORIA, E POI VERIFICA I REDDITI',items:[
  I('per',['A','ANNA','NESSUNA DOMANDA',110],300,380,'Anna non deve fare niente'),
  I('stp',['1','PAGATO DA SOLO','RATA DI DICEMBRE',330],760,460,'lo paga da solo'),
  I('arR',[],1000,460,['in via provvisoria',-0.4]),
  I('stp',['2','PROVVISORIO','PAGAMENTO D\'UFFICIO',330],1220,460,'in via provvisoria'),
  I('arR',[],1460,460,['lo verifica',-0.4]),
  I('stp',['3','VERIFICA','SUI REDDITI DICHIARATI',330],1680,460,'redditi dichiarati')]},
 {at:'Non lo prende mai',top:'CHI NON LO PRENDE MAI',cap:'CHI HA SOLO TRATTAMENTI ASSISTENZIALI. E ORA, LUCIA',items:[
  VT('SOLO TRATTAMENTI ASSISTENZIALI',620,230,'trattamenti assistenziali',RF_,36),
  I('rw',['Assegno sociale',false,38,true],300,360,'assegno sociale'),
  I('rw',['Pensione sociale',false,38,true],300,480,'pensione sociale'),
  I('rw',['Prestazioni di invalidità civile',false,38,true],300,600,'invalidità civile'),
  I('per',['L','LUCIA',null,120],1480,380,'E ora Lucia'),
  VT('LEI TROVA TRE PAGAMENTI',1480,690,'trova tre soldi',AMB,36)]},
]);
// ---------- BLOCCO 10 (733 f = 24,4 s) ----------
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LUCIA',cap:'COME ANNA PRENDE IL BONUS. E PER LEI ARRIVA ANCHE LA QUATTORDICESIMA',items:[
  I('per',['L','LUCIA',null,130],380,380,'Lucia prende'),
  I('rw',['Prende il minimo',true,38,true],680,250,'anche lei il minimo'),
  I('rw',['È sola',true,38,true],680,370,'è sola'),
  I('rw',['64 anni a settembre',true,38,true],680,490,'sessantaquattro anni a settembre'),
  I('coin',['BONUS',95,GRN,34],1360,330,'Quindi il bonus'),
  I('coin',['14ª',95,RED_,56],1620,330,'la quattordicesima'),
  VT('IL TERZO PAGAMENTO: LA 14ª',1490,560,['la quattordicesima',0.2],AMB,36)]},
 {at:'Di solito si paga',top:'LA QUATTORDICESIMA DI DICEMBRE',cap:'L\'ANNO SCORSO, A DICEMBRE, L\'HANNO PRESA QUASI 150.000 PENSIONATI',items:[
  I('mon',[[[6,6,GRN,'DI SOLITO: LUGLIO']]],960,330,'Di solito si paga a luglio'),
  I('mon',[[[7,11,AMB,'64 ANNI DOPO LUGLIO: PAGATA A DICEMBRE']]],960,560,'dopo luglio'),
  VT('O PENSIONE INIZIATA NEL 2026',520,720,'va in pensione durante l\'anno',GF_,34),
  VN('QUASI 150.000',1380,730,'quasi centocinquantamila',{fs:56,sub:'DICEMBRE SCORSO',fill:GF_,minw:500})]},
]);
// ---------- BLOCCO 11 (780 f = 26,0 s) ----------
const QX=[960-750+440+(1500-440)/4,960-750+440+(1500-440)*3/4];const QY=r=>440-184+92*(r+1)+46;
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANTO VALE LA QUATTORDICESIMA',cap:'IMPORTI ANNUI, LAVORATORI DIPENDENTI (AUTONOMI: FINO A 18, 18-28, OLTRE 28 ANNI)',items:[
  I('qtab',[],960,440,'Dipende dagli anni'),
  GN('437 €',QX[0],QY(0),'quattrocentotrentasette'),GN('546 €',QX[0],QY(1),'cinquecentoquarantasei'),GN('655 €',QX[0],QY(2),'seicentocinquantacinque'),
  GN('336 €',QX[1],QY(0),'trecentotrentasei','#2B6F77'),GN('420 €',QX[1],QY(1),'quattrocentoventi','#2B6F77'),GN('504 €',QX[1],QY(2),'cinquecentoquattro','#2B6F77'),
  I('mon',[[[8,11,AMB,'LUCIA: SOLO DA SETTEMBRE = UNA PARTE']],900,32],960,780,'Ma Lucia')]},
]);
// ---------- BLOCCO 12 (701 f = 23,4 s) ----------
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUATTORDICESIMA: COSA CAMBIA',cap:'LA 14ª NON È TASSATA E ARRIVA IN AUTOMATICO',items:[
  I('per',['L',null,null,85],330,320,'conta solo il tuo'),I('per',['M',null,null,85],600,320,'il reddito del coniuge'),
  I('cross',[70,70],600,320,'non conta'),
  VT('REDDITO DEL CONIUGE: NON CONTA',465,520,['non conta',0.2],GF_,32),
  VT('NON È TASSATA',1360,250,'non è tassata',GF_,42),
  I('rw',['Solo assegno sociale o invalidità civile: no',false,32,true],930,400,'non spetta'),
  I('rw',['Arriva in automatico',true,36,true],930,520,'arriva in automatico')]},
 {at:'Ecco il dicembre',top:'IL DICEMBRE DEI TRE VICINI',cap:'FRANCO: 13ª · ANNA: 13ª E BONUS · LUCIA: 13ª, BONUS E PARTE DI 14ª',items:[
  I('ghead',[],960,240,'Ecco il dicembre'),
  I('grow',['F','FRANCO',['si','no','no']],960,370,'Franco:'),
  I('grow',['A','ANNA',['si','si','no']],960,510,'Anna:'),
  I('grow',['L','LUCIA',['si','si','UNA PARTE']],960,650,'Lucia:')]},
]);
// ---------- BLOCCO 13 (531 f = 17,7 s) ----------
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'SE NON VEDI NIENTE',cap:'CONTROLLA IL CEDOLINO DI DICEMBRE SU MY INPS, APPENA È ONLINE',items:[
  I('per',['A','ANNA',null,80],330,300,'come Anna'),I('per',['L','LUCIA',null,80],330,620,'o Lucia'),
  I('phone',[['Tredicesima','Importo aggiuntivo','Quattordicesima']],960,480,'controlla il cedolino'),
  VT('OGNI VOCE HA LA SUA RIGA',1500,480,'ogni voce ha la sua riga',AMB,34)]},
 {at:'Se il bonus o',top:'SE MANCA QUALCOSA',cap:'DOMANDA DI RICOSTITUZIONE DELLA PENSIONE: ONLINE O CON UN PATRONATO',items:[
  VT('BONUS O 14ª MANCANO?',560,230,'Se il bonus o',RF_,40),
  I('doc',['RICOSTITUZIONE',460,330,GRN,34],560,540,'ricostituzione della pensione'),
  I('arR',[],1000,540,['online',-0.3]),
  I('br',['inps.it',520,200],1400,360,'online'),
  I('ico',['comune','PATRONATO',300,250],1400,660,'con un patronato')]},
]);
// ---------- BLOCCO 14 (780 f = 26,0 s) - ULTIMO: contenuti in alto, zona bassa libera per la schermata finale (N.22) ----------
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E TU CHI SEI?',cap:'',items:[
  I('per',['F','FRANCO',null,70],660,230,'Franco'),I('per',['A','ANNA',null,70],960,230,'Anna'),I('per',['L','LUCIA',null,70],1260,230,'Lucia'),
  VT('SCRIVI NEI COMMENTI: QUANTO PRENDI, SOLO O SPOSATO',960,440,'Scrivilo nei commenti',AMB,34),
  I('dbg',[1600,250],960,635,'I limiti del'),
  I('dline',['LIMITI 2026 SULL\'AUMENTO PROVVISORIO DELL\'1,4%: POSSONO CAMBIARE','#fff',32],960,632,'possono cambiare'),
  I('dline',['VERIFICA SEMPRE SU INPS.IT O CON UN PATRONATO','#fff',32],960,682,'Controlla sempre'),
  I('dline',['SOLO INFORMATIVO, NON AFFILIATO ALL\'INPS','#7FF0D2',32],960,730,'non è affiliato')]},
]);
