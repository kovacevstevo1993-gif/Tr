#!/usr/bin/env python3
"""Crea la scheda base dell'ELEFANTINO (personaggio originale, stesso stile 3D del topolino/Chip/Spike).
Usa il topolino solo come riferimento di STILE (rendering, proporzioni testa grande, inquadratura).
Output: assets/s/ele.png (RGBA) + assets/pose/raw/ele_base.jpg"""
import base64, io, os, sys, time
import requests
from PIL import Image
import pose_pollinations as PP

PROMPT = (
    "Use the attached character ONLY as a style reference (same 3D Pixar render quality, soft lighting, big head and small body "
    "proportions, same camera angle, same size in the frame, standing upright like a little kid). Replace it with a COMPLETELY DIFFERENT character: "
    "a cute baby elephant standing upright on two legs, light blue-grey smooth skin, huge round floppy ears with pink inside, a short chubby curved trunk, "
    "big shiny dark friendly eyes with long eyelashes, small round rosy cheeks, gentle smile, wearing a coral-red t-shirt with a white star on the chest and small purple shorts, "
    "barefoot with round toes. Plain flat pure green #00FF00 background, no ground, no shadow, no text, no watermark, full body visible, feet near the bottom of the frame."
)

def main():
    ref = os.path.join(PP.HERE, "assets/topo/neutro_full.png")
    buf = io.BytesIO(); PP.su_verde(ref).save(buf, "PNG")
    for n in range(5):
        r = requests.post(PP.URL, data={"model": PP.MODEL, "size": "768x1376", "prompt": PROMPT},
                          files={"image": ("ref.png", buf.getvalue(), "image/png")}, timeout=240)
        if r.status_code == 200:
            raw = Image.open(io.BytesIO(base64.b64decode(r.json()["data"][0]["b64_json"]))).convert("RGB").resize((768, 1376)); break
        print("HTTP", r.status_code, r.text[:100]); 
        if r.status_code == 402: sys.exit("saldo finito")
        time.sleep(2 ** (n + 1))
    os.makedirs(os.path.join(PP.OUT, "raw"), exist_ok=True)
    raw.save(os.path.join(PP.OUT, "raw", "ele_base.jpg"), quality=93)
    PP.ritaglia(raw).save(os.path.join(PP.HERE, "assets/s/ele.png"))
    print("ok")

if __name__ == "__main__": main()
