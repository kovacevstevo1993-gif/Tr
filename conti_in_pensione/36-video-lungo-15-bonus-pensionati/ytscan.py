import json, re, subprocess, sys, urllib.parse, collections

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def fetch(url):
    r = subprocess.run(["curl", "-s", "-m", "50", "-A", UA, "-H", "Accept-Language: it-IT,it;q=0.9", url],
                       capture_output=True, text=True)
    return r.stdout

def initial(html):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    return json.loads(m.group(1)) if m else None

def walk_videos(data):
    out = []
    def walk(o):
        if isinstance(o, dict):
            if "videoRenderer" in o:
                v = o["videoRenderer"]
                t = "".join(r.get("text", "") for r in v.get("title", {}).get("runs", []))
                vc = v.get("viewCountText", {}).get("simpleText", "") or "".join(r.get("text", "") for r in v.get("viewCountText", {}).get("runs", []))
                pub = v.get("publishedTimeText", {}).get("simpleText", "")
                own = (v.get("ownerText") or v.get("longBylineText") or {}).get("runs", [{}])
                ch = own[0].get("text", "")
                cid = own[0].get("navigationEndpoint", {}).get("browseEndpoint", {}).get("browseId", "")
                handle = own[0].get("navigationEndpoint", {}).get("browseEndpoint", {}).get("canonicalBaseUrl", "")
                out.append(dict(views=vc, pub=pub, ch=ch, cid=cid, handle=handle, title=t, id=v.get("videoId", "")))
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk(data)
    return out

def search(q, sp):
    u = "https://www.youtube.com/results?hl=it&gl=IT&search_query=" + urllib.parse.quote(q) + "&sp=" + sp
    d = initial(fetch(u))
    return walk_videos(d) if d else []

if __name__ == "__main__":
    sp = sys.argv[1]
    allv = {}
    for q in sys.argv[2:]:
        for v in search(q, sp):
            allv[v["id"]] = v
    json.dump(list(allv.values()), open("scan_out.json", "w"), ensure_ascii=False)
    print("video unici:", len(allv))
