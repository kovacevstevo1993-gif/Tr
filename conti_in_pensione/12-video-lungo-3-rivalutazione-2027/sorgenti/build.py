import sys,re,json,os
n=int(sys.argv[1]);D=os.path.dirname(os.path.abspath(__file__))
fr=json.load(open(D+'/durate.json'))
h=open('head.html',encoding='utf-8').read()
cop=open(D+'/../copione-blocchi.txt',encoding='utf-8').read()
m=re.search(r'BLOCCO %d \(\d+ car\.\)\n(.+)'%n,cop);txt=m.group(1).strip()
if n<=5:
    parts=[open(f,encoding='utf-8').read() for f in ['helpers.js','common.js','lib.js','gen.js','specs.js','specs2.js','b-common.js','b%02d.js'%n,'regia.js']]
else:
    spec=open('specs-v3.js',encoding='utf-8').read()
    parts=[open(f,encoding='utf-8').read() for f in ['helpers.js','common.js','lib.js','gen.js','specs.js','specs2.js','b-common.js','b-sync.js']]
    parts.append('const SB=[];const N=%d;const TOT=%d/30;const TXT=%s;\n'%(n,fr[str(n)],json.dumps(txt,ensure_ascii=False)))
    parts.append(spec)
    parts.append('SPECS[N]();')
    parts.append(open('regia.js',encoding='utf-8').read())
open('blocco%02d.html'%n,'w',encoding='utf-8').write(h+'\n'+'\n'.join(parts)+'\n</script></body></html>')
