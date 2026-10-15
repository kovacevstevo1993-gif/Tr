// ===== VIDEO 7 (rivalutazione persa 2023-2026) - motore b-sync-80: tempi calcolati su testo + durata del blocco =====
// Regole: scene >= 5 s, comparsa 0,9 s, nessun elemento sparisce nella scena, tutto completo entro l'80 %, poi fermo.
// Novita' del video 7 (N.37, non in serie): SCONTRINO della pensione (carta con bordo a zig-zag) + sfondo in movimento.
const SPECS={};
const GF_='url(#g_badge)',RF_='url(#g_red)',PF_='url(#g_paper)',DF_='#0B4A50';
const VT=(s,x,y,at,fill,fs)=>I('tag',[s,fill||AMB,(fill&&fill!==AMB)?'#fff':'#5A3300',fs||44],x,y,at);
const VN=(s,x,y,at,o)=>{o=o||{};return I('num',[s,o.fs||76,o.fill||PF_,o.sub,o.subfill,o.minw],x,y,at);};
// scontrino: centro in (0,0); w x h; testata, righe [etichetta, importo, colore], totale
BUILD.rcpt=(g,w,h,head,lines,total,tsub)=>{const zz=22;let d=`M${-w/2} ${-h/2+20} Q${-w/2} ${-h/2} ${-w/2+20} ${-h/2} H${w/2-20} Q${w/2} ${-h/2} ${w/2} ${-h/2+20} V${h/2}`;
 const n=Math.round(w/zz);for(let i=0;i<n;i++){const x1=w/2-(i+0.5)*w/n,x2=w/2-(i+1)*w/n;d+=` L${x1} ${h/2-14} L${x2} ${h/2}`;}d+=' Z';
 el('path',{d:d,fill:'url(#g_paper)',filter:'url(#g_sh)'},g);
 el('rect',{x:-w/2,y:-h/2,width:w,height:84,rx:20,fill:GRN},g);el('rect',{x:-w/2,y:-h/2+50,width:w,height:34,fill:GRN},g);
 txt(g,head,0,-h/2+56,Math.min(38,(w-60)/(head.length*0.74)),'#fff','bold');
 let y=-h/2+140;(lines||[]).forEach(l=>{txt(g,l[0],-w/2+40,y,34,INK,'bold','start');txt(g,l[1],w/2-40,y,36,l[2]||INK,'900','end');
  el('line',{x1:-w/2+36,y1:y+22,x2:w/2-36,y2:y+22,stroke:'#B7C7CA','stroke-width':3,'stroke-dasharray':'10 8'},g);y+=72;});
 el('line',{x1:-w/2+30,y1:y-10,x2:w/2-30,y2:y-10,stroke:INK,'stroke-width':5},g);
 txt(g,total,0,y+88,Math.min(110,(w-60)/(total.length*0.62)),RED_,'900');
 if(tsub)txt(g,tsub,0,y+146,34,GRN,'bold');};
// ---------- BLOCCO 1 (841 fotogrammi = 28,0 s) ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'PENSIONI: QUANTO HAI PERSO?',cap:'4 ANNI DI RIVALUTAZIONE TAGLIATA: È SCRITTO NELLE LEGGI',items:[
  I('rcpt',[560,600,'SCONTRINO DELLA PENSIONE',[['Pensione 2022','3.000 €'],['Periodo','2023-2026'],['Rivalutazione','TAGLIATA',RED_]],'-9.400 €','LORDI IN 4 ANNI'],520,530,'novemilaquattrocento'),
  VN('3.000 €',1350,330,'chi a fine duemilaventidue',{fs:90,sub:'PENSIONE LORDA FINE 2022',minw:640}),
  VT('NÉ MULTA, NÉ ERRORE',1350,560,'Non per una multa',RF_,40),
  I('stamp',['LEGGE DI BILANCIO',GRN,52],1350,690,'per una regola scritta'),
  VT('IL BUCO NON SI RICHIUDE',1350,815,'E quel buco',AMB,40)]},
 {at:'Oggi facciamo un test',top:'IL TEST',cap:'IN POCHI MINUTI CAPISCI IN QUALE GRUPPO SEI',items:[
  VT('TU QUANTO HAI PERSO?',960,250,'Oggi facciamo un test',GF_,46),
  VN('NIENTE',420,480,'perso niente',{fs:84,fill:GF_,sub:'GRUPPO 1',minw:470}),
  VN('POCO',960,480,'poco',{fs:84,fill:AMB,sub:'GRUPPO 2',minw:470}),
  VN('TANTO',1500,480,'o tanto',{fs:84,fill:RF_,sub:'GRUPPO 3',minw:470}),
  VT('E POI: COSA SI DECIDE PER IL 2027?',960,760,'cosa si sta decidendo adesso',DF_,42)]},
]);
