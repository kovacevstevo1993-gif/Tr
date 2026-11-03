import json, re, subprocess, sys, urllib.parse

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def fetch(url):
    r = subprocess.run(["curl", "-s", "-m", "40", "-A", UA, "-H", "Accept-Language: it-IT,it;q=0.9", url],
                       capture_output=True, text=True)
    return r.stdout

def suggest(q):
    u = "https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&hl=it&gl=IT&q=" + urllib.parse.quote(q)
    try:
        return json.loads(fetch(u))[1]
    except Exception as e:
        return ["ERR " + str(e)]

def search(q, sp):
    u = "https://www.youtube.com/results?hl=it&gl=IT&search_query=" + urllib.parse.quote(q) + "&sp=" + sp
    html = fetch(u)
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not m:
        return None, len(html)
    data = json.loads(m.group(1))
    out = []
    def walk(o):
        if isinstance(o, dict):
            if "videoRenderer" in o:
                v = o["videoRenderer"]
                try:
                    t = v["title"]["runs"][0]["text"]
                except Exception:
                    t = "?"
                vc = v.get("viewCountText", {}).get("simpleText", "") or "".join(r.get("text", "") for r in v.get("viewCountText", {}).get("runs", []))
                pub = v.get("publishedTimeText", {}).get("simpleText", "")
                ch = "".join(r.get("text", "") for r in v.get("ownerText", {}).get("runs", []))
                ln = v.get("lengthText", {}).get("simpleText", "")
                out.append((vc, pub, ch, ln, t, v.get("videoId", "")))
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk(data)
    return out, len(html)

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "sug":
        for q in sys.argv[2:]:
            print("##", q, "->", " | ".join(suggest(q)[:10]))
    else:
        sp = sys.argv[2]
        for q in sys.argv[3:]:
            res, n = search(q, sp)
            print("##", q, "[sp=%s]" % sp, "html", n)
            if res is None:
                print("  NESSUN DATO (pagina senza ytInitialData)")
                continue
            for r in res[:6]:
                print("  %-22s | %-14s | %-26s | %-8s | %s" % (r[0][:22], r[1][:14], r[2][:26], r[3], r[4][:95]))
