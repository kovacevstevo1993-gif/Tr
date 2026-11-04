import sys,re,json,urllib.request,urllib.parse
def search(q,sp):
    u="https://www.youtube.com/results?search_query="+urllib.parse.quote(q)+"&sp="+sp+"&hl=it&gl=IT"
    r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0","Accept-Language":"it-IT,it"})
    h=urllib.request.urlopen(r,timeout=40).read().decode('utf8','ignore')
    m=re.search(r'var ytInitialData = (\{.*?\});</script>',h,re.S)
    d=json.loads(m.group(1));out=[]
    def walk(o):
        if isinstance(o,dict):
            if 'videoRenderer' in o:
                v=o['videoRenderer'];t=''.join(x['text'] for x in v['title']['runs'])
                vc=v.get('viewCountText',{}).get('simpleText','');pub=v.get('publishedTimeText',{}).get('simpleText','')
                ch=''.join(x['text'] for x in v.get('ownerText',{}).get('runs',[]))
                out.append((vc,pub,ch,t))
            for x in o.values(): walk(x)
        elif isinstance(o,list):
            for x in o: walk(x)
    walk(d);return out
for q in sys.argv[2:]:
    print('##',q)
    try:
        for r in search(q,sys.argv[1])[:14]: print('  ',' | '.join(r))
    except Exception as e: print('  ERR',e)
