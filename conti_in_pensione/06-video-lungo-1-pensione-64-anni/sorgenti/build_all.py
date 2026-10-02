a=open('blocks.js',encoding='utf-8').read();b=open('blocks_b.js',encoding='utf-8').read();c=open('blocks_c.js',encoding='utf-8').read()+'\n'+open('blocks_d.js',encoding='utf-8').read()+'\n'+open('blocks_e.js',encoding='utf-8').read()
marker='// =================== regia ==================='
a=a.replace(marker,b+'\n'+c+'\n'+marker)
open('blocks_all.js','w',encoding='utf-8').write(a)
h=open('head.html',encoding='utf-8').read();hp=open('helpers.js',encoding='utf-8').read();cm=open('common.js',encoding='utf-8').read()
open('blocchi.html','w',encoding='utf-8').write(h+'\n'+hp+'\n'+cm+'\n'+a+'\n</script></body></html>')
