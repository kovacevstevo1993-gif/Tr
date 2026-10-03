"""Controllo OBBLIGATORIO di ogni clip/slide, su TUTTI i fotogrammi (non a campione).
Uso: python3 qa_slide.py <file.html> <indice_blocco> <n_frame> [larghezza altezza]
Controlla, per ogni fotogramma:
 1) testo che esce dal fotogramma
 2) testo che esce dal riquadro/pillola/scheda che lo contiene (lettere tagliate)
 3) testi visibili che si sovrappongono tra loro
 4) animazioni non finite prima della dissolvenza di fine scena (finestra 'ferma')
Esce con codice 1 se trova problemi."""
import sys,os,json
from playwright.sync_api import sync_playwright
html=os.path.abspath(sys.argv[1]);blk=int(sys.argv[2]);N=int(sys.argv[3])
W=int(sys.argv[4]) if len(sys.argv)>4 else 1920;Hh=int(sys.argv[5]) if len(sys.argv)>5 else 1080
JS="""()=>{
 const out=[];const svg=document.getElementById('svg');
 function eff(n){let o=1;while(n&&n!==document){if(n.getAttribute){const a=n.getAttribute('opacity');if(a!==null&&a!=='')o*=parseFloat(a);}n=n.parentNode;}return o;}
 const texts=[...svg.querySelectorAll('text')];
 for(const t of texts){
  const s=(t.textContent||'').trim();if(!s)continue;
  const r=t.getBoundingClientRect();if(r.width<3||r.height<3)continue;
  const o=eff(t);if(o<0.35)continue;
  // contenitore (in coordinate locali, indipendenti dalla rotazione): forma più piccola dello stesso gruppo che circonda il testo
  let best=null,ba=1e18;const tb=t.getBBox();const tcx=tb.x+tb.width/2,tcy=tb.y+tb.height/2;const th=tb.height*0.72;
  for(const c of t.parentNode.children){if(c===t||!['rect','circle','path','ellipse'].includes(c.tagName))continue;
   const b=c.getBBox();if(b.width<10||b.height<th*0.9)continue;
   if(Math.abs(tcx-(b.x+b.width/2))<=0.3*b.width&&Math.abs(tcy-(b.y+b.height/2))<=0.3*b.height){const a=b.width*b.height;if(a<ba){ba=a;best={x:b.x,y:b.y,w:b.width,h:b.height};}}}
  const loc={x:tb.x,y:tb.y+tb.height*0.14,w:tb.width,h:th};
  out.push({s,x:r.x,y:r.y+r.height*0.14,w:r.width,h:r.height*0.72,o,c:best,l:loc});
 }
 return out;}"""
issues={};
def add(f,m):issues.setdefault(m,[]).append(f)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':W,'height':Hh});pg.on('pageerror',lambda e:print('ERR',e))
    pg.goto('file://'+html)
    scenes=pg.evaluate("(typeof SB!=='undefined')?SB.map(s=>[s.s,s.e]):[]")
    data=[]
    for f in range(N):
        pg.evaluate('draw(%d,%f)'%(blk,f/30));data.append(pg.evaluate(JS))
    for f,items in enumerate(data):
        for i,a in enumerate(items):
            sc=[k for k,(s0,e0) in enumerate(scenes) if s0<=f/30<e0]
            entering=bool(sc) and (f/30-scenes[sc[0]][0])<1.0   # oggetti che entrano da fuori all'inizio della scena
            if (not entering) and (a['x']<-2 or a['y']<-2 or a['x']+a['w']>W+2 or a['y']+a['h']>Hh+2):add(f,'FUORI DAL FOTOGRAMMA: "%s"'%a['s'])
            c=a['c'];l=a['l']
            if c and (l['x']<c['x']-3 or l['x']+l['w']>c['x']+c['w']+3 or l['y']<c['y']-3 or l['y']+l['h']>c['y']+c['h']+3):
                add(f,'TESTO TAGLIATO/FUORI DAL RIQUADRO: "%s"'%a['s'])
            for bb in items[i+1:]:
                ix=min(a['x']+a['w'],bb['x']+bb['w'])-max(a['x'],bb['x']);iy=min(a['y']+a['h'],bb['y']+bb['h'])-max(a['y'],bb['y'])
                if ix>4 and iy>4 and ix*iy>0.04*min(a['w']*a['h'],bb['w']*bb['h']):add(f,'SOVRAPPOSTI: "%s" e "%s"'%(a['s'],bb['s']))
    # animazioni finite prima della dissolvenza
    TOT=N/30
    for k,(s,e) in enumerate(scenes):
        last=(k==len(scenes)-1)
        t1=(TOT if last else e)-0.75;t2=(TOT if last else e)-0.32
        f1=int(max(0,t1*30));f2=int(min(N-1,t2*30))
        A={x['s']:x for x in data[f1]};B={x['s']:x for x in data[f2]}
        for s_,a in B.items():
            if s_ not in A:add(f2,'NON ANCORA COMPARSO nella finestra ferma (scena %d): "%s"'%(k+1,s_))
            elif abs(A[s_]['x']-a['x'])>25 or abs(A[s_]['y']-a['y'])>25 or abs(A[s_]['w']-a['w'])>25:add(f2,'ANCORA IN MOVIMENTO nella finestra ferma (scena %d): "%s"'%(k+1,s_))
    b.close()
if not issues:print('QA OK: %d fotogrammi controllati, nessun problema'%N);sys.exit(0)
print('QA: PROBLEMI TROVATI su %d fotogrammi'%N)
for m,fs in issues.items():
    print(' -',m,'| fotogrammi %d-%d (%d)'%(min(fs),max(fs),len(fs)))
sys.exit(1)
