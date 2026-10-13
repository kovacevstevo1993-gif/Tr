// ===== VIDEO 6 (cedolino di novembre) - motore b-sync-80: tempi calcolati su testo + durata del blocco =====
// Regole: scene >= 5 s, comparsa 0,9 s, nessun elemento sparisce nella scena, tutto completo entro l'80 %, poi fermo.
const SPECS={};
const GF_='url(#g_badge)',RF_='url(#g_red)',PF_='url(#g_paper)',DF_='#0B4A50';
const VT=(s,x,y,at,fill,fs)=>I('tag',[s,fill||AMB,(fill&&fill!==AMB)?'#fff':'#5A3300',fs||44],x,y,at);
const VN=(s,x,y,at,o)=>{o=o||{};return I('num',[s,o.fs||76,o.fill||PF_,o.sub,o.subfill,o.minw],x,y,at);};
// ---------- BLOCCO 1 (712 fotogrammi = 23,7 s) ----------
SPECS[1]=()=>mkBlk(TXT,TOT,[
 {at:0,top:'CEDOLINO DI NOVEMBRE',cap:'PER ALCUNI È PIÙ BASSA, MA NON È UN ERRORE',items:[
  I('cal',['NOVEMBRE','2026',110,''],330,560,'Novembre.'),
  I('pay',['CEDOLINO','? €'],840,540,['Apri il cedolino',0.6]),
  VT('PIÙ BASSA DI OTTOBRE?',1470,430,'più bassa di ottobre',RF_,40),
  I('stamp',['NON È UN ERRORE',GRN,48],1470,700,'non è un errore')]},
 {at:'Per altri, invece',top:'PER ALTRI: ULTIMO MESE',cap:'PRIMA IL CONTO VERO, POI L\'EQUIVOCO DEI TITOLI',items:[
  VT('PER ALTRI',480,225,'Per altri',GF_,44),
  VN('ULTIMO MESE',480,340,"l'ultimo mese",{fs:60,fill:RF_,sub:'SOLDI TOLTI',minw:620}),
  I('arR',[],960,340,'ti toglie dei soldi'),
  VN('DICEMBRE',1440,340,'da dicembre ti arrivano di più',{fs:60,fill:GF_,sub:'TI ARRIVA DI PIÙ',minw:560}),
  I('calc',[],250,650,'Ti faccio il conto vero'),
  VT('IL CONTO VERO',620,650,'il conto vero',GF_,38),
  I('hl',['AUMENTI E ARRETRATI'],1400,620,'quei titoli'),
  I('stamp',['UN EQUIVOCO',RED_,48],1400,790,"c'è un equivoco")]},
]);
