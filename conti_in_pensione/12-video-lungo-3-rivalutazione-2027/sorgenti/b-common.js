// ===== VIDEO 3 - helper comuni (1920x1080) =====
function payslip(p,title,amount){const g=el('g',{},p);
 el('rect',{x:-150,y:-190,width:300,height:380,rx:20,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-150,y:-190,width:300,height:60,rx:20,fill:GRN},g);el('rect',{x:-150,y:-160,width:300,height:30,fill:GRN},g);
 txt(g,title,0,-148,30,'#fff','bold');
 [-90,-50,-10].forEach((y,i)=>{el('rect',{x:-115,y:y,width:i%2?140:210,height:14,rx:7,fill:'#C3D3D7'},g);});
 if(amount){el('rect',{x:-120,y:40,width:240,height:96,rx:22,fill:'#D6F5EC',stroke:GRN,'stroke-width':5},g);txt(g,amount,0,98,44,INK,'900');}
 return g;}
function bigNum(p,s,fs,fill,sub,subfill){const g=el('g',{},p);
 const w=Math.max(360,s.length*fs*0.64+90,sub?sub.length*36*0.74+90:0);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:fs*1.55+(sub?58:0),rx:34,fill:fill||'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-fs*0.9,width:w,height:fs*1.55+(sub?58:0),rx:34,fill:'none',stroke:'#fff','stroke-opacity':.8,'stroke-width':4},g);
 txt(g,s,0,fs*0.3,fs,(fill&&fill!=='url(#g_paper)')?'#fff':INK,'900');
 if(sub)txt(g,sub,0,fs*0.3+62,36,subfill||GRN,'bold');
 return g;}
function qMark(p,r,fill){const g=el('g',{},p);
 el('circle',{r:r,fill:fill||'url(#g_badge)',stroke:'#fff','stroke-width':r*0.1,filter:'url(#g_sh2)'},g);
 txt(g,'?',0,r*0.4,r*1.25,'#fff','900');return g;}
function vf(p,vero){const g=el('g',{},p);
 el('rect',{x:-86,y:-40,width:172,height:80,rx:40,fill:vero?'url(#g_badge)':'url(#g_red)',stroke:'#fff','stroke-width':5,filter:'url(#g_sh2)'},g);
 txt(g,vero?'VERO':'FALSO',0,15,40,'#fff','900');return g;}
