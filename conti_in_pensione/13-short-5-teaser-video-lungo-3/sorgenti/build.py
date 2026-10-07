# Costruisce index.html unendo gli helper dello short 3 (common) con scenes5.js
import os,re
here=os.path.dirname(os.path.abspath(__file__))
base=open(here+'/base.html').read()
a=base.index('const S=['); b=base.index('// defs aggiuntivi')
scenes=open(here+'/scenes5.js').read()
out=base[:a]+scenes+'\n'+base[b:]
# regola n.5: niente movimento continuo della camera, sfondo quasi fermo
out=out.replace("const z=1+0.03*(t/S[i].D);cam.setAttribute('transform','translate(540 960) scale('+z+') translate(-540 -960)');","")
out=out.replace('t*sp*0.6','t*sp*0.15').replace('(y-t*sp)','(y-t*sp*0.3)').replace('y-t*sp<0','y-t*sp*0.3<0')
open(here+'/index.html','w').write(out)
print('index.html ok',len(out))
