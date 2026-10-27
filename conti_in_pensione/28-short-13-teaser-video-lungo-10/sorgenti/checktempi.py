"""Controllo tempi short 11 (regole N.15/N.18): ultimo elemento completo entro 80 %, distanza >= 0,45 s, comparsa 0,9 s. Uso: python3 checktempi.py"""
import os
from playwright.sync_api import sync_playwright
here=os.path.dirname(os.path.abspath(__file__));bad=0
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox']);pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.on('pageerror',lambda e:print('ERR',e));pg.goto('file://'+here+'/index.html')
    for i in range(6):
        pg.evaluate('draw(%d,0.1)'%i);a=sorted(pg.evaluate('PL[%d]'%i));D=pg.evaluate('S[%d].D'%i)
        last=a[-1]+0.9;gaps=[round(a[k+1]-a[k],2) for k in range(len(a)-1)];fermo=D-last
        ok=D>=5 and last<=0.8*D+0.02 and min(gaps)>=0.45 and a[0]>=0.9
        bad+=0 if ok else 1
        print('B%d D=%.2f s elementi=%d avvio=%s ultimo completo %.2f s (%.0f%% di %.2f) fermo %.2f s gap min %.2f %s'%(i+1,D,len(a),[round(x,2) for x in a],last,100*last/D,D,fermo,min(gaps),'OK' if ok else '<<< ERRORE'))
    b.close()
print('ERRORI TEMPI:',bad)
