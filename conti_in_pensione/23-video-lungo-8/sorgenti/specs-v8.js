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
  else{el('rect',{x:-w/2,y:-220,width:w,height:170,rx:22,fill:'#06303A',stroke:RED_,'stroke-width':6,'stroke-dasharray':'22 14'},g);txt(g,'NON TI SEGUE',0,-122,40,'#FF8A75','900');}},
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
// ---------- BLOCCO 1 (680 f = 22,7 s) ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONE ALL\'ESTERO: CONVIENE?',cap:'CON 2.000 € LORDI IN ITALIA PAGHI PIÙ DI 5.000 € L\'ANNO DI IRPEF',items:[
  I('pass',[0.8],210,520,'Pensione all\'estero'),
  VN('2.000 €',830,300,'con duemila euro lordi',{fs:84,sub:'PENSIONE LORDA AL MESE',minw:560}),
  I('cty',['IT','ITALIA','OLTRE 5.000 € DI IRPEF',RF_,620],830,610,'in Italia paghi'),
  I('plane',[0.9],1560,290,'Se vai a vivere'),
  I('globe',[150],1560,560,'in certi paesi'),
  VT('L\'ITALIA NON TRATTIENE PIÙ',1440,800,'non te li trattiene',GF_,36)]},
 {at:'Ma chi parte',top:'PRIMA DI PARTIRE: 3 COSE',cap:'IL CONTO VERO CON 1.000, 1.500 E 2.000 € LORDI',items:[
  I('warn',[],330,500,'Ma chi parte'),
  I('circ',['1'],760,290,'tre cose'),I('circ',['2'],960,290,['tre cose',0.3]),I('circ',['3'],1160,290,['tre cose',0.6]),
  I('arD',[],760,470,'meno soldi'),VT('MENO SOLDI',760,620,['meno soldi',0.2],RF_,44),
  I('lock',[],1420,450,'pensione bloccata'),VT('PENSIONE BLOCCATA',1420,660,['pensione bloccata',0.2],RF_,40),
  VT('OGGI: IL CONTO VERO',1090,790,'Oggi facciamo il conto',GF_,40)]},
]);
// ---------- BLOCCO 2 (530 f = 17,7 s) ----------
SPECS[2]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PRIMA DI PARTIRE, UNA COSA VELOCE',cap:'ISCRIVERTI NON TI COSTA NIENTE: PER NOI VUOL DIRE ANDARE AVANTI',items:[
  I('goal',[1300,0.23],960,300,'vogliamo arrivare a mille'),
  I('doc',['FONTI UFFICIALI',380,300,GRN,34],330,630,'controlliamo leggi e fonti'),
  I('clock',[115],790,600,'ci vogliono ore'),VT('ORE DI RICERCHE',790,790,['ci vogliono ore',0.3],AMB,38),
  I('btn',['ISCRIVITI'],1430,570,'iscriviti'),
  VT('NON TI COSTA NIENTE',1430,720,'non ti costa niente',GF_,40)]},
]);
// ---------- BLOCCO 3 (655 f = 21,8 s) ----------
SPECS[3]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'LA REGOLA CHE DECIDE TUTTO',cap:'PENSIONE PRIVATA INPS: TASSE SOLO NEL PAESE DOVE VIVI DAVVERO',items:[
  I('doc',['ACCORDO FISCALE',440,400,GRN,36],400,480,'accordi contro la doppia tassazione'),
  VT('CONTRO LA DOPPIA TASSAZIONE',400,780,['doppia tassazione',0.2],DF_,30),
  VT('PENSIONE PRIVATA INPS',1180,220,'Per le pensioni del lavoro privato',GF_,42),
  I('flg',['PT',170,'PORTOGALLO',32],930,360,'Portogallo'),I('flg',['ES',170,'SPAGNA',32],1360,360,'Spagna'),
  I('flg',['TN',170,'TUNISIA',32],930,590,'Tunisia'),I('flg',['AL',170,'ALBANIA',32],1360,590,'Albania'),
  VT('TASSE SOLO DOVE VIVI',1130,800,'tasse soltanto',AMB,36)]},
 {at:'Lo ha confermato',top:'LO CONFERMA IL FISCO',cap:'NON VALE OVUNQUE: CON LA FRANCIA, PER ESEMPIO, È DIVERSO',items:[
  I('doc',['AGENZIA DELLE ENTRATE',600,300,GRN,34],560,420,'Lo ha confermato'),
  I('stamp',['RISPOSTA N. 35/2019',GRN,44],560,680,'pensionato Inps in Portogallo'),
  VT('NON VALE OVUNQUE',1400,250,'Non vale ovunque',AMB,42),
  I('flg',['FR',240,'FRANCIA',38],1400,480,'con la Francia'),
  VT('REGOLE DIVERSE',1400,740,'è diverso',RF_,42)]},
]);
// ---------- BLOCCO 4 (637 f = 21,2 s) ----------
SPECS[4]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TRAPPOLA 1: LA PENSIONE PUBBLICA',cap:'EX INPDAP: DI REGOLA RESTA TASSATA IN ITALIA, ANCHE SE VIVI ALL\'ESTERO',items:[
  VT('TRAPPOLA 1',960,220,'Prima trappola',RF_,46),
  I('ico',['stato','STATO',320],390,430,'per lo Stato'),I('ico',['comune','COMUNE',320],750,430,'per un comune'),
  I('ico',['scuola','SCUOLA',320],1110,430,'nella scuola pubblica'),I('ico',['forze','FORZE ARMATE',320],1470,430,'nelle forze armate'),
  I('cty',['IT','EX INPDAP','TASSE IN ITALIA',RF_,700],960,720,'resta tassata in Italia')]},
 {at:'Di solito cambia',top:'L\'ECCEZIONE',cap:'CON UNA PENSIONE PUBBLICA GRAN PARTE DI QUESTI CONTI NON VALE',items:[
  I('pass',[0.85],480,470,'cittadino di quel paese'),
  VT('SOLO SE DIVENTI CITTADINO',480,790,['cittadino di quel paese',0.3],AMB,36),
  VT('PENSIONE PUBBLICA',1330,280,'per chi ha una pensione pubblica',DF_,44),
  I('calc',[],1330,520,'gran parte di questi conti'),
  I('stamp',['QUESTI CONTI NON VALGONO',RED_,40],1330,760,['non vale',-0.2])]},
]);
// ---------- BLOCCO 5 (630 f = 21,0 s) ----------
SPECS[5]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'IL CONTO IN ITALIA',cap:'IRPEF DI UN ANNO SULLA PENSIONE LORDA (CONTI ARROTONDATI)',items:[
  VT('IRPEF IN UN ANNO',960,220,'in un anno paghi',AMB,44),
  I('hbar',['1.000 € LORDI',1325/5151,'CIRCA 1.300 €',AMB,1600],960,360,'milletrecento'),
  I('hbar',['1.500 € LORDI',3238/5151,'CIRCA 3.200 €',AMB,1600],960,520,'tremiladuecento'),
  I('hbar',['2.000 € LORDI',1,'CIRCA 5.100 €',RF_,1600],960,680,'cinquemilacento')]},
 {at:'Sono conti fatti',top:'COME È FATTO IL CONTO',cap:'LE ADDIZIONALI DI REGIONE E COMUNE SI AGGIUNGONO',items:[
  I('calc',[],380,500,'Sono conti fatti'),
  I('rw',['Aliquote e detrazioni 2026',true,36,true],700,300,'aliquote e le detrazioni'),
  I('rw',['Pensione lorda × 13 mensilità',true,36,true],700,430,'tredici mensilità'),
  I('rw',['Addizionali non comprese',false,36,true],700,560,'senza le addizionali'),
  VT('+ ADDIZIONALI REGIONE E COMUNE',1100,720,'che si aggiungono',RF_,38)]},
]);
// ---------- BLOCCO 6 (595 f = 19,8 s) ----------
SPECS[6]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'QUANDO TI TRASFERISCI',cap:'L\'ITALIA SMETTE DI TRATTENERE, MA IL NUOVO PAESE TI TASSA',items:[
  I('cty',['IT','ITALIA','SMETTE DI TRATTENERE',GF_,600],540,320,'Italia smette'),
  I('plane',[0.75],960,520,'Quando ti trasferisci'),
  I('cty',['GL','NUOVO PAESE','TI TASSA A MODO SUO',AMB,600],1420,700,'ti tassa con le sue regole'),
  VT('NESSUNO TE LI REGALA',420,700,'non te li regala nessuno',RF_,40)]},
 {at:'Quindi la domanda',top:'LA DOMANDA GIUSTA',cap:'VEDIAMO I 3 PAESI DI CUI SI PARLA DI PIÙ',items:[
  VT('NON: DOVE SI PAGA ZERO?',960,220,'non è dove si paga zero',RF_,42),
  VT('MA: QUANTO TI RESTA IN TASCA?',960,330,'quanto ti resta in tasca',GF_,46),
  I('flg',['PT',260,'PORTOGALLO',40],480,560,'Portogallo'),
  I('flg',['TN',260,'TUNISIA',40],960,560,'Tunisia'),
  I('flg',['AL',260,'ALBANIA',40],1440,560,'Albania')]},
]);
// ---------- BLOCCO 7 (678 f = 22,6 s) ----------
SPECS[7]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PAESE 1: PORTOGALLO',cap:'PER ANNI UN REGIME CHE ESENTAVA LE PENSIONI STRANIERE',items:[
  I('flg',['PT',420,'PORTOGALLO',48],520,440,'Portogallo'),
  VT('IL PARADISO DEI PENSIONATI',1340,300,'paradiso dei pensionati',AMB,42),
  I('suit',[],1340,540,'paradiso dei pensionati'),
  VT('PENSIONI STRANIERE ESENTI',1340,780,'esentava le pensioni',GF_,38)]},
 {at:'Ma, secondo',top:'DAL 2024 È CAMBIATO',cap:'SECONDO LE GUIDE FISCALI: OGGI SI PAGA L\'IMPOSTA PORTOGHESE',items:[
  I('years',[],960,270,'dal duemilaventiquattro'),
  I('stamp',['IL NUOVO NON VALE PER LE PENSIONI',RED_,36],560,520,'quello nuovo non vale'),
  VT('VA FATTO IL CONTO SUL TUO CASO',560,730,'va fatto il conto',GF_,36),
  I('stairs',[],1440,700,'imposta portoghese a scaglioni')]},
]);
// ---------- BLOCCO 8 (625 f = 20,8 s) ----------
SPECS[8]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PAESE 2: TUNISIA',cap:'SECONDO LE GUIDE FISCALI: TASSE SOLO SU UN QUINTO DELLA PENSIONE',items:[
  I('flg',['TN',300,'TUNISIA',44],300,420,'Tunisia'),
  I('pie5',[160],860,420,'un quinto della pensione'),
  I('rw',['Accredito su un conto in Tunisia',true,32,true],1060,360,'conto in Tunisia'),
  I('rw',['Ci vivi davvero',true,32,true],1060,500,'ci vivi davvero')]},
 {at:'Su quel quinto',top:'IL RISULTATO',cap:'CON UNA PENSIONE PRIVATA IL PRELIEVO È MOLTO PIÙ BASSO DELL\'IRPEF',items:[
  VT('LE ALIQUOTE PARTONO BASSE',560,270,'partono basse',AMB,36),
  I('pie5',[130],560,500,'Su quel quinto'),
  I('vb2',[],1360,700,'molto più basso'),
  VT('SOLO PENSIONE PRIVATA',1360,190,'con una pensione privata',DF_,36)]},
]);
// ---------- BLOCCO 9 (697 f = 23,2 s) ----------
SPECS[9]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PAESE 3: ALBANIA',cap:'SECONDO LE GUIDE FISCALI: OGGI NESSUNA TASSA SULLE PENSIONI PRIVATE',items:[
  I('flg',['AL',420,'ALBANIA',48],540,440,'Albania'),
  VT('OGGI',1320,240,"oggi l'Albania",AMB,44),
  VN('0 €',1320,470,'non tassa',{fs:130,fill:GF_,sub:'TASSE SULLA PENSIONE PRIVATA',minw:620})]},
 {at:"Quindi l'Irpef",top:'QUANTO TI TIENI IN PIÙ, OGNI ANNO',cap:'SI DISCUTE DI CAMBIARE LA REGOLA: OGGI C\'È, DOMANI FORSE NO',items:[
  VT("L'IRPEF ITALIANA TE LA TIENI",960,220,"te la tieni",GF_,42),
  VN('+1.300 €',390,440,'milletrecento',{fs:68,fill:GF_,sub:'CON 1.000 € LORDI',minw:520}),
  VN('+3.200 €',960,440,'tremiladuecento',{fs:68,fill:GF_,sub:'CON 1.500 € LORDI',minw:520}),
  VN('+5.100 €',1530,440,'cinquemilacento',{fs:68,fill:GF_,sub:'CON 2.000 € LORDI',minw:520}),
  VT('LA REGOLA PUÒ CAMBIARE',960,720,'si discute di cambiare',RF_,46)]},
]);
// ---------- BLOCCO 10 (619 f = 20,6 s) ----------
SPECS[10]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TRAPPOLA 2: CHI PRENDE POCO',cap:"IN UN PAESE DELL'UNIONE EUROPEA L'INTEGRAZIONE AL MINIMO NON TI SEGUE",items:[
  I('stack',['IN ITALIA',false],430,520,'integrata al minimo'),
  I('flg',['EU',260,'UNIONE EUROPEA',36],960,420,"Unione europea"),
  I('arR',[],960,660,"Unione europea"),
  I('stack',['NELL\'UE',true],1490,520,'non ti segue'),
  VT("LO DICE L'INPS",960,790,"lo dice l'Inps",GF_,38)]},
 {at:"E l'assegno sociale",top:"E L'ASSEGNO SOCIALE?",cap:'RISCHI DI PARTIRE PER RISPARMIARE E RITROVARTI CON MENO DI PRIMA',items:[
  I('doc',['ASSEGNO SOCIALE',460,300,GRN,36],520,430,"l'assegno sociale"),
  I('stamp',["FUORI DALL'ITALIA SI PERDE",RED_,36],500,700,'si perde'),
  VT('PARTI PER RISPARMIARE',1420,250,'Rischi di partire',GF_,40),
  I('arD',[],1420,420,['Rischi di partire',0.6]),
  VN('MENO DI PRIMA',1420,600,'con meno di prima',{fs:70,fill:RF_,minw:560})]},
]);
// ---------- BLOCCO 11 (714 f = 23,8 s) ----------
SPECS[11]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'TRAPPOLA 3: LA RESIDENZA DEVE ESSERE VERA',cap:"DI SOLITO BISOGNA VIVERE LÌ PIÙ DI METÀ DELL'ANNO",items:[
  I('rw',["Iscrizione all'Aire",true,36,true],180,290,"iscrizione all'Aire"),
  I('rw',['Certificato di residenza fiscale estera',true,36,true],180,420,'certificato di residenza'),
  I('rw',["Domanda all'Inps: niente Irpef italiana",true,36,true],180,550,"domanda all'Inps"),
  I('calS',['ALMENO','183',150,'GIORNI L\'ANNO',0.72],1530,560,'più di metà')]},
 {at:'E ogni anno',top:'OGNI ANNO: LA PROVA DI ESISTENZA IN VITA',cap:'SE NON RISPONDI IN TEMPO, LA PENSIONE VIENE SOSPESA',items:[
  I('ico',['banca','LA BANCA',320,300],420,450,'la banca che paga'),
  I('env',['PROVA DI ESISTENZA IN VITA'],960,420,'esistenza in vita'),
  I('lock',[],1500,420,'se non rispondi'),
  I('stamp',['PENSIONE SOSPESA',RED_,48],1440,720,'viene sospesa')]},
]);
// ---------- BLOCCO 12 (613 f = 20,4 s) ----------
SPECS[12]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E SE UN GIORNO VUOI TORNARE?',cap:'LA TASSA AL 7 % PER I PENSIONATI NEI PICCOLI COMUNI DEL SUD',items:[
  I('plane',[0.85,GRN],500,300,'vuoi tornare'),
  I('flg',['IT',300,'ITALIA',44],500,580,'vuoi tornare'),
  VN('7 %',1320,420,'sette per cento',{fs:140,fill:AMB,sub:'TASSA PER PENSIONATI',minw:560}),
  VT('PICCOLI COMUNI DEL SUD',1320,720,'piccoli comuni del Sud',GF_,40)]},
 {at:'Attenzione',top:'PER CHI VALE DAVVERO',cap:'CON LA PENSIONE INPS NON SI APPLICA',items:[
  I('rw',['Pensione pagata da un ente straniero',true,36,true],480,280,'ente straniero'),
  I('rw',["Fuori dall'Italia da almeno 5 anni",true,36,true],480,410,'cinque anni'),
  I('stamp',['PENSIONE INPS: NO',RED_,52],960,570,'Con la pensione Inps'),
  VT('NON È UNA SCORCIATOIA',960,740,'Non è una scorciatoia',RF_,46)]},
]);
// ---------- BLOCCO 13 (643 f = 21,4 s) ----------
SPECS[13]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'RICAPITOLIAMO: 2.000 € LORDI',cap:'PENSIONE PRIVATA INPS: LE TASSE DI UN ANNO, PAESE PER PAESE',items:[
  I('crow',['IT','ITALIA','CIRCA 5.100 € DI IRPEF',RF_],960,250,'in Italia lasci'),
  I('crow',['AL','ALBANIA','OGGI LI TIENI',GF_],960,390,'In Albania'),
  I('crow',['TN','TUNISIA','NE PAGHI UNA PICCOLA PARTE',AMB],960,530,'in Tunisia'),
  I('crow',['PT','PORTOGALLO','IMPOSTA PORTOGHESE',DF_],960,670,'in Portogallo')]},
 {at:'E non conta solo',top:'NON CONTA SOLO LA TASSA',cap:'CONTA ANCHE QUANTO COSTA VIVERE LÌ',items:[
  I('ico',['spesa','VIVERE LÌ',300,300],390,480,'quanto costa vivere'),
  I('ico',['casa','LA CASA',300,300],770,480,'la casa'),
  I('ico',['sanita','LA SANITÀ',300,300],1150,480,'la sanità'),
  I('ico',['cuore','CHI AMI',300,300],1530,480,'chi ami')]},
]);
// ---------- BLOCCO 14 (553 f = 18,4 s) - ULTIMO: contenuti in alto, zona bassa libera per la schermata finale (N.22) ----------
SPECS[14]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'E TU, DOVE ANDRESTI?',cap:'',items:[
  VT('DOVE ANDRESTI A VIVERE CON LA TUA PENSIONE?',960,210,'dove andresti',GF_,42),
  I('flg',['IT',120],560,345,'con la tua pensione'),I('flg',['PT',120],760,345,['con la tua pensione',0.2]),I('flg',['ES',120],960,345,['con la tua pensione',0.4]),
  I('flg',['TN',120],1160,345,['con la tua pensione',0.6]),I('flg',['AL',120],1360,345,['con la tua pensione',0.8]),
  VT('SCRIVILO NEI COMMENTI: TI RISPONDIAMO CON IL CONTO',960,470,'Scrivilo nei commenti',AMB,38),
  I('dbg',[1560,240],960,640,'Prima di trasferirti'),
  I('dline',['PRIMA DI TRASFERIRTI: PATRONATO O COMMERCIALISTA','#fff',34],960,638,'chiedi sempre a un patronato'),
  I('dline',['LE LEGGI CAMBIANO: VERIFICA SEMPRE','#fff',34],960,684,'le leggi cambiano'),
  I('dline',["SOLO INFORMATIVO, NON CONSULENZA, NON AFFILIATO ALL'INPS",'#7FF0D2',34],960,730,'non è affiliato')]},
]);
