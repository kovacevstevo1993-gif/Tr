import re
old=open('/home/user/Tr/conti_in_pensione/03-sorgenti-grafica/index.html',encoding='utf-8').read().split('\n')
head='\n'.join(old[:73])
cta='\n'.join(old[384:439]).replace('S[6]=','S[7]=',1)
tail='\n'.join(old[439:])
new=open('scenes2.js',encoding='utf-8').read()
warp="\nS[7].D=4.767;{const u=S[7].update;S[7].update=function(t){return u.call(this,t*5.4/4.767)};}\n"
open('index.html','w',encoding='utf-8').write(head+'\n'+new+'\n'+cta+warp+tail)
