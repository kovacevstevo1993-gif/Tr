"""CONTROLLO TEMPI (obbligatorio PRIMA del render, regola N.18). Uso: cd <cartella sorgenti del video>; python3 ../../qa/qa_tempi.py
Per ogni blocco: durata di ogni scena (>= 5 s), ultimo elemento completo entro l80 %, tempo fermo >= 1 s, distanza tra elementi. Stampa ERRORE se qualcosa non va."""
import os,sys
from playwright.sync_api import sync_playwright
bad=0
with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox']);pg=br.new_page(viewport={'width':1920,'height':1080})
    for n in range(1,38):
        pg.goto('file://'+os.path.abspath('blocco%02d.html'%n));pg.evaluate('draw(0,0.1)')
        sc=pg.evaluate('window.__SC');it=pg.evaluate('window.__IT')
        msgs=[]
        for (s,e),a in zip(sc,it):
            L=e-s;a=sorted(a);last=a[-1]+0.9
            gaps=[round(a[i+1]-a[i],2) for i in range(len(a)-1)]
            ming=min(gaps) if gaps else 9
            vis=L-last  # fermo alla fine
            first_vis=L-(a[-1])  # visibile dall'inizio comparsa dell'ultimo
            ok=(L>=5.0 and last<=0.8*L+0.02 and vis>=1.0)
            if not ok: bad+=1
            msgs.append('L=%.1f n=%d ultimo completo a %.1f (%.0f%%) fermo %.1fs, vis.min %.1fs, gap min %.2f %s'%(L,len(a),last,100*last/L,vis,first_vis,ming,'' if ok else '<<< ERRORE'))
        print(n,' | '.join(msgs))
    br.close()
print('errori',bad)
