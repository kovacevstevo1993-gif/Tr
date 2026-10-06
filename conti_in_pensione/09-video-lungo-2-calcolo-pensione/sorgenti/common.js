// ===== BLOCCO 1 - video lungo 1 (1920x1080) =====
const FW=1920,FH=1080;
function topLabel(g,s){const t=el('g',{},g);
 el('polygon',{points:'0,-14 14,0 0,14 -14,0',fill:'#7FF0D2'},t);
 const x=txt(t,s,28,12,36,'#7FF0D2','bold','start');x.setAttribute('letter-spacing','9');
 const w=s.length*36*0.72+s.length*9+60;t.setAttribute('data-w',w);return t;}
function cap(g,s,size){size=size||62;size=Math.min(size,1700/(s.length*0.76));const w=Math.min(1800,s.length*size*0.76+110);const c=el('g',{},g);
 el('rect',{x:-w/2,y:-62,width:w,height:124,rx:62,fill:'#06303A',filter:'url(#g_sh2)'},c);
 el('rect',{x:-w/2,y:-62,width:w,height:124,rx:62,fill:'none',stroke:AMB,'stroke-width':6},c);
 txt(c,s,0,size*0.36,size,'#FFFFFF','bold');return c;}
function headline(g,s,w,fs){w=w||560;fs=fs||50;const c=el('g',{},g);
 el('rect',{x:-w/2,y:-80,width:w,height:160,rx:22,fill:'url(#g_paper)',filter:'url(#g_sh)'},c);
 el('rect',{x:-w/2,y:-80,width:w,height:46,rx:22,fill:'#E4412C'},c);
 el('rect',{x:-w/2,y:-52,width:w,height:18,fill:'#E4412C'},c);
 txt(c,'ULTIM’ORA',0,-44,30,'#fff','bold');
 txt(c,s,0,46,fs,'#0B4A50','900');return c;}
function door(g){const d=el('g',{},g);
 // luce dietro la porta
 el('rect',{x:-190,y:-300,width:380,height:600,rx:14,fill:'#FFF3C4'},d);
 const rays=el('g',{opacity:.9},d);
 el('rect',{x:-190,y:-300,width:380,height:600,rx:14,fill:'url(#g_spot)'},rays);
 // stipite
 el('rect',{x:-216,y:-326,width:432,height:640,rx:22,fill:'none',stroke:'#0B4A50','stroke-width':26},d);
 el('rect',{x:-216,y:-326,width:432,height:640,rx:22,fill:'none',stroke:'#fff','stroke-opacity':.45,'stroke-width':4},d);
 return d;}
