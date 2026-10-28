# Costruisce index.html unendo base.html (motore comune) con head15.js + s15.js; DUR e TX letti dai file dell'utente (nessun testo a mano)
import os,re,json
here=os.path.dirname(os.path.abspath(__file__));d=os.path.dirname(here)
base=open(here+'/base.html').read()
a=base.index('const S=['); b=base.index('// defs aggiuntivi')
tx=[m.group(2) for m in (re.match(r'^(\d+)\|\s*(.+)$',l.strip()) for l in open(d+'/copione-blocchi.txt',encoding='utf-8')) if m]
dur=[int(l) for l in open(d+'/DURATE.txt') if re.match(r'^\d+$',l.strip())]
assert len(tx)==5 and len(dur)==5,(len(tx),len(dur))
head=open(here+'/head15.js').read().replace('/*DUR*/','const DUR=%s.map(x=>x/30);'%json.dumps(dur)).replace('/*TX*/','const TX=%s;'%json.dumps(tx,ensure_ascii=False))
scenes=head+'\n'+open(here+'/s15.js').read()
out=base[:a]+scenes+'\n'+base[b:]
out=out.replace("const z=1+0.03*(t/S[i].D);cam.setAttribute('transform','translate(540 960) scale('+z+') translate(-540 -960)');","")
out=out.replace('t*sp*0.6','t*sp*0.15').replace('(y-t*sp)','(y-t*sp*0.3)').replace('y-t*sp<0','y-t*sp*0.3<0')
open(here+'/index.html','w').write(out)
print('index.html ok',len(out),'DUR',dur)
