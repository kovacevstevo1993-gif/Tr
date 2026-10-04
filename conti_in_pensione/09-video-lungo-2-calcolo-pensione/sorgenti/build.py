import sys
n=sys.argv[1]
h=open('head.html',encoding='utf-8').read();hp=open('helpers.js',encoding='utf-8').read();cm=open('common.js',encoding='utf-8').read()
lib=open('lib.js',encoding='utf-8').read();b=open('b%s.js'%n,encoding='utf-8').read();rg=open('regia.js',encoding='utf-8').read()
open('blocco%d.html'%int(n),'w',encoding='utf-8').write(h+'\n'+hp+'\n'+cm+'\n'+lib+'\n'+b+'\n'+rg+'\n</script></body></html>')
