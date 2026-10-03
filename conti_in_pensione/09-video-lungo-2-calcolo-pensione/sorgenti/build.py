h=open('head.html',encoding='utf-8').read();hp=open('helpers.js',encoding='utf-8').read();cm=open('common.js',encoding='utf-8').read();b=open('b01.js',encoding='utf-8').read()
open('blocco1.html','w',encoding='utf-8').write(h+'\n'+hp+'\n'+cm+'\n'+b+'\n</script></body></html>')
