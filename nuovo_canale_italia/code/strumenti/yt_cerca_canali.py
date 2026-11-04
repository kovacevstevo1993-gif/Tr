import sys,re,json,urllib.request,urllib.parse
for q in sys.argv[1:]:
    u="https://www.youtube.com/results?search_query="+urllib.parse.quote(q)+"&sp=EgIQAg%253D%253D&hl=it&gl=IT"
    h=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0","Accept-Language":"it-IT,it"}),timeout=40).read().decode('utf8','ignore')
    d=json.loads(re.search(r'var ytInitialData = (\{.*?\});</script>',h,re.S).group(1));out=[]
    def w(o):
        if isinstance(o,dict):
            if 'channelRenderer' in o:
                c=o['channelRenderer'];t=c['title']['simpleText'];hd=(c.get('subscriberCountText') or {}).get('simpleText','');h2=(c.get('longBylineText') or {}).get('runs',[{}])[0].get('text','');out.append((t,hd,c.get('videoCountText',{}).get('simpleText','') if isinstance(c.get('videoCountText'),dict) else ''))
            for x in o.values(): w(x)
        elif isinstance(o,list):
            for x in o: w(x)
    w(d);print('##',q,'->',out[:6])
