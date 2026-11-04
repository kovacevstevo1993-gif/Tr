import sys,urllib.request,urllib.error,socket,re,concurrent.futures as cf
names=sys.argv[1:]
def get(u):
    try:
        r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0","Accept-Language":"it-IT,it"})
        x=urllib.request.urlopen(r,timeout=25); return x.status,x.read(400000).decode('utf8','ignore')
    except urllib.error.HTTPError as e: return e.code,''
    except Exception as e: return 0,str(e)[:40]
def dns(d):
    try: socket.gethostbyname(d); return 'preso'
    except socket.gaierror: return 'libero?'
    except Exception: return '?'
def chk(n):
    yt=get("https://www.youtube.com/@"+n)[0]
    st,body=get("https://www.facebook.com/"+n)
    fbt=re.search(r'<title[^>]*>(.*?)</title>',body,re.S); fbt=(fbt.group(1)[:40] if fbt else '')
    return n,yt,st,fbt,dns(n+'.it'),dns(n+'.com')
with cf.ThreadPoolExecutor(6) as ex:
    for r in ex.map(chk,names): print(r)
