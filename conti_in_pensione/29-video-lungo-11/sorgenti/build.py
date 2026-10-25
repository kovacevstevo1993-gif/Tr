import sys,re,json,os
n=int(sys.argv[1]);D=os.path.dirname(os.path.abspath(__file__))
fr=json.load(open(D+'/durate.json'))
h=open(D+'/head.html',encoding='utf-8').read()
txt={int(l.split('|',1)[0]):l.rstrip('\n').split('|',1)[1] for l in open(D+'/../copione-blocchi.txt',encoding='utf-8') if '|' in l}[n]
parts=[open(D+'/'+f,encoding='utf-8').read() for f in ['helpers.js','common.js','lib.js','gen.js','specs.js','specs2.js','b-common.js','b-sync-80.js']]
parts.append('const SB=[];const N=%d;const TOT=%d/30;const OFF=%d/30;const TXT=%s;\n'%(n,fr[str(n)],sum(v for k,v in fr.items() if int(k)<n),json.dumps(txt,ensure_ascii=False)))
for f in ['specs-v9-base.js','specs-v9-new.js','specs-v10-new.js','specs-v11.js']:parts.append(open(D+'/'+f,encoding='utf-8').read())
parts.append('SPECS[N]();')
parts.append(open(D+'/regia11.js',encoding='utf-8').read())
open(D+'/blocco%02d.html'%n,'w',encoding='utf-8').write(h+'\n'+'\n'.join(parts)+'\n</script></body></html>')
