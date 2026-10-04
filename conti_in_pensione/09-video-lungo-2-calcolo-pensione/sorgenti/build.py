import sys
n=sys.argv[1]
FR={21:429,22:330,23:464,24:334,25:340,26:460,27:404,28:346,29:458,30:428,31:358,32:370,33:364,34:416,35:334,36:330,37:380,38:404,39:416,40:422,41:424,42:358,43:392,44:406,45:410,46:288,47:392,48:466,49:340,50:334,51:404,52:372,53:376,54:436,55:298,56:251,57:215}
import os
if int(n)>=21 and not os.path.exists('b%s.js'%n):
    open('b%s.js'%n,'w').write('const SB=[];const TOT=%d/30;mk(BLK[%d],SB,TOT);\n'%(FR[int(n)],int(n)))
h=open('head.html',encoding='utf-8').read();hp=open('helpers.js',encoding='utf-8').read();cm=open('common.js',encoding='utf-8').read()
lib=open('lib.js',encoding='utf-8').read()+open('gen.js',encoding='utf-8').read()+open('specs.js',encoding='utf-8').read()+open('specs2.js',encoding='utf-8').read();b=open('b%s.js'%n,encoding='utf-8').read();rg=open('regia.js',encoding='utf-8').read()
open('blocco%d.html'%int(n),'w',encoding='utf-8').write(h+'\n'+hp+'\n'+cm+'\n'+lib+'\n'+b+'\n'+rg+'\n</script></body></html>')
