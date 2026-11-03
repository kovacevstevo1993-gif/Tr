import json, re, sys
sys.path.insert(0, ".")
from ytscan import fetch, initial

def lockups(d):
    out = []
    def texts(o, acc):
        if isinstance(o, dict):
            if "content" in o and isinstance(o["content"], str):
                acc.append(o["content"])
            for x in o.values():
                texts(x, acc)
        elif isinstance(o, list):
            for x in o:
                texts(x, acc)
    def walk(o):
        if isinstance(o, dict):
            if "lockupViewModel" in o:
                l = o["lockupViewModel"]
                cid = l.get("contentId", "")
                md = l.get("metadata", {}).get("lockupMetadataViewModel", {})
                title = md.get("title", {}).get("content", "")
                acc = []
                texts(md.get("metadata", {}), acc)
                out.append(dict(id=cid, title=title, meta=" | ".join(acc)))
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk(d)
    return out

def latest(cid, tab="videos"):
    h = fetch("https://www.youtube.com/channel/%s/%s?hl=it&gl=IT" % (cid, tab))
    d = initial(h)
    return lockups(d) if d else None
