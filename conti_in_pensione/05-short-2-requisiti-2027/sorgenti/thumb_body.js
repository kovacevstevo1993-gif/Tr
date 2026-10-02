const g=document.getElementById('scene');
const bok=document.getElementById('bok');
for(let i=0;i<14;i++){el('circle',{cx:(i*173)%1080,cy:(i*311)%1920,r:30+((i*37)%70),fill:'#8FF5DC',opacity:.06+((i*13)%7)*0.01},bok);}
function big(p,s,x,y,size,fill,sw){const t=txt(p,s,x,y,size,fill,'900');t.setAttribute('stroke','#04262B');t.setAttribute('stroke-width',sw||14);t.setAttribute('stroke-linejoin','round');t.setAttribute('paint-order','stroke');return t;}
// titolo
big(g,'PENSIONE 2027:',540,300,104,'#FFD43B',16);
big(g,'SALE L’ETÀ!',540,462,150,'#FFFFFF',18);
// carta
const c=el('g',{},g);
el('rect',{x:60,y:600,width:960,height:650,rx:50,fill:'url(#g_paper)',filter:'url(#g_sh)'},c);
el('rect',{x:60,y:600,width:960,height:650,rx:50,fill:'none',stroke:'#fff','stroke-opacity':.8,'stroke-width':5},c);
txt(c,'PENSIONE DI VECCHIAIA',540,700,44,'#1B9F81');
el('rect',{x:140,y:728,width:800,height:4,fill:'#C9D6D8'},c);
// 67 anni
txt(c,'67',280,1030,300,'#0B4A50','900');
txt(c,'ANNI',280,1135,66,'#1B9F81');
// +
const pl=el('g',{},c);txt(pl,'+',515,1005,150,'#E4412C','900');
// mistero
const mb=el('g',{filter:'url(#g_sh2)'},c);
el('circle',{cx:800,cy:945,r:170,fill:'#FFB838'},mb);
el('circle',{cx:800,cy:945,r:170,fill:'none',stroke:'#fff','stroke-width':10,'stroke-opacity':.9},mb);
el('circle',{cx:800,cy:945,r:144,fill:'none',stroke:'#fff','stroke-width':4,'stroke-opacity':.5,'stroke-dasharray':'6 14'},mb);
txt(mb,'???',800,975,130,'#5A3300','900');
txt(mb,'MESI',800,1065,58,'#5A3300','900');
// badge freccia su (rosso) in alto a destra
const bd=el('g',{transform:'translate(960 620)'},g);
el('circle',{r:92,fill:'url(#g_red)',stroke:'#fff','stroke-width':12,filter:'url(#g_sh2)'},bd);
el('path',{d:'M0 -48 L-46 6 L-18 6 L-18 50 L18 50 L18 6 L46 6 Z',fill:'#fff'},bd);
// badge calendario in alto a sinistra
const cb=el('g',{transform:'translate(120 620)'},g);
el('circle',{r:92,fill:'url(#g_badge)',stroke:'#fff','stroke-width':12,filter:'url(#g_sh2)'},cb);
txt(cb,'2027',0,18,50,'#fff','900');
// pill finale
const pg=el('g',{transform:'translate(540 1385)'},g);
el('rect',{x:-420,y:-82,width:840,height:164,rx:82,fill:'url(#g_red)',filter:'url(#g_sh)'},pg);
el('rect',{x:-420,y:-82,width:840,height:164,rx:82,fill:'none',stroke:'#fff','stroke-width':8,'stroke-opacity':.9},pg);
txt(pg,'TU CI RIENTRI?',0,30,84,'#fff','900');
