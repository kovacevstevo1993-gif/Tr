# Costruisce index.html unendo gli helper dello short 3 (common) con head12.js+s12.js
import os,re
here=os.path.dirname(os.path.abspath(__file__))
base=open(here+'/base.html').read()
a=base.index('const S=['); b=base.index('// defs aggiuntivi')
scenes=open(here+'/head12.js').read()+'\n'+open(here+'/s12.js').read()
out=base[:a]+scenes+'\n'+base[b:]
# regola n.5: niente movimento continuo della camera, sfondo quasi fermo
out=out.replace("const z=1+0.03*(t/S[i].D);cam.setAttribute('transform','translate(540 960) scale('+z+') translate(-540 -960)');","")
out=out.replace('t*sp*0.6','t*sp*0.15').replace('(y-t*sp)','(y-t*sp*0.3)').replace('y-t*sp<0','y-t*sp*0.3<0')
# sfondo di dicembre (come il video 9): luci calde che scendono lente
out=out.replace('(y-t*sp*0.3)%2000+(y-t*sp*0.3<0?2000:0)','(y+t*sp*0.3)%2000').replace("fill:'#8FF5DC'","fill:'#FFE7A0'")
open(here+'/index.html','w').write(out)
print('index.html ok',len(out))
