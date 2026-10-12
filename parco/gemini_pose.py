"""Genera una posa del personaggio con Gemini (immagine di riferimento -> nuova posa su verde).
Uso: python3 gemini_pose.py <riferimento.png> <out.png> "<descrizione posa>"
"""
import sys, base64, json, io, urllib.request
from PIL import Image

MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

def to_green(path):
    im = Image.open(path).convert("RGBA")
    bg = Image.new("RGBA", im.size, (0, 255, 0, 255))
    bg.alpha_composite(im)
    buf = io.BytesIO(); bg.convert("RGB").save(buf, "PNG")
    return base64.b64encode(buf.getvalue()).decode()

def gen(ref, out, pose):
    prompt = (
        "Use the attached character exactly as it is (same face, fur, clothes, colors, proportions, 3D Pixar style, "
        "same camera angle and same size in the frame). Only change the pose: " + pose +
        ". Plain flat pure green #00FF00 background, no ground, no shadow, no text, no watermark, "
        "full body visible, feet at the same height as in the reference. Vertical 9:16 image."
    )
    body = {"contents": [{"parts": [
        {"text": prompt},
        {"inline_data": {"mime_type": "image/png", "data": to_green(ref)}}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]}}
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=180))
    for p in r["candidates"][0]["content"]["parts"]:
        d = p.get("inlineData") or p.get("inline_data")
        if d:
            open(out, "wb").write(base64.b64decode(d["data"])); print("salvato", out, Image.open(out).size); return
    print(json.dumps(r)[:600])

if __name__ == "__main__":
    gen(*sys.argv[1:4])
