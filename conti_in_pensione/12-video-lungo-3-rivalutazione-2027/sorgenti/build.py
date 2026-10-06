import sys
n=int(sys.argv[1]);h=open('head.html',encoding='utf-8').read()
parts=[open(f,encoding='utf-8').read() for f in ['helpers.js','common.js','lib.js','gen.js','specs.js','specs2.js','b-common.js','b%02d.js'%n,'regia.js']]
open('blocco%02d.html'%n,'w',encoding='utf-8').write(h+'\n'+'\n'.join(parts)+'\n</script></body></html>')
