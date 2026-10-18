#!/usr/bin/env python3
"""Pose dei personaggi GRATIS (Pollinations flux-2-dev-free): seed fisso + descrizione identica del personaggio + solo la posa cambia.
UNA immagine alla volta (pausa tra le richieste), ritaglio sulla chiave colore -> assets/pose/<chi>_<posa>.png (768x1376, piedi in basso).
Uso: python3 pose_free.py <chi> [posa ...] [--rifai]"""
import base64, io, os, sys, time, requests
import numpy as np
from PIL import Image
from oggetti_pollinations import ritaglia

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = "community/scriptsnsenses-sys/flux-2-dev-free"
SEED = 42
STYLE = ", 3D Pixar animation style, full body from head to feet, centered, the same size in the frame, plain flat pure {} background, no shadow, no ground, no text"
CHARS = {
    "volpe": ("a cute cartoon fox boy character, orange-brown fur, cream white face and chest, big bright green eyes, black nose, big pointy ears with pink inside, "
              "wearing a short-sleeved bright green polo shirt and brown trousers and brown shoes, bushy orange tail with white tip", "magenta #FF00FF"),
    "rana": ("a cute cartoon baby frog character, bright lime green skin with a pale yellow belly, big round shiny dark eyes on top of the head, wide happy mouth, small red cheeks, "
             "wearing a small red and white striped t-shirt and blue shorts, long legs with big webbed feet", "magenta #FF00FF"),
    "coniglio": ("a cute cartoon baby bunny girl character, soft white fur, very long upright ears with pink inside, big blue eyes, pink nose, small round fluffy tail, "
                 "wearing a yellow dress with white polka dots and a small pink bow on one ear", "green #00FF00"),
    "orso": ("a cute cartoon baby brown bear cub character, soft chocolate brown fur, round small ears, light tan muzzle and belly, big friendly black eyes, "
             "wearing a red t-shirt with a yellow star and blue overalls shorts", "green #00FF00"),
}
POSES = {
    "neutro": "standing relaxed facing the viewer, arms down along the body, friendly smile",
    "saluta": "standing facing the viewer, waving hello with one hand raised high, big smile",
    "saluta_m": "standing facing the viewer, waving hello with the OTHER hand (left hand) raised high, big smile",
    "su": "standing facing the viewer, both arms raised straight up high above the head, very happy, mouth open",
    "mani": "standing facing the viewer, clapping the hands together in front of the chest, eyes happy, mouth open",
    "salto": "jumping high in the air facing the viewer, arms and legs spread wide like a star, laughing",
    "accovacciato": "crouching down facing the viewer ready to jump, knees bent, arms back, determined smile",
    "ride": "standing facing the viewer, laughing with eyes closed, hands on the belly",
    "sorpreso": "standing facing the viewer, surprised with mouth open in a round O, both hands on the cheeks",
    "balla": "dancing facing the viewer, hips to one side, one arm up and one arm down, one knee lifted, joyful",
    "balla_m": "dancing facing the viewer, hips to the other side, the other arm up, the other knee lifted, joyful",
    "cammina1": "walking toward the viewer, the right leg stepping forward, the left arm swinging forward, smiling",
    "cammina2": "walking toward the viewer, the left leg stepping forward, the right arm swinging forward, smiling",
    "indica": "standing facing the viewer, pointing to the side with one arm stretched out, excited",
    "gira": "standing seen from the back, turned away from the viewer, tail visible",
    "lato": "standing seen from the side in profile facing right, smiling",
    "parla": "standing facing the viewer, talking with the mouth wide open, one hand slightly raised, explaining",
    "triste": "standing facing the viewer, sad, head down, arms hanging",
    "cammina3": "walking toward the viewer, passing position: legs together, one foot lifted, arms close to the body, smiling",
    "cammina4": "walking toward the viewer, passing position on the other foot, legs together, arms close to the body, smiling",
    "corre": "running fast toward the viewer, leaning forward, one knee high, arms pumping, big smile",
    "corre2": "running fast toward the viewer, leaning forward, the OTHER knee high, the other arm forward, big smile",
    "salto_su": "jumping up straight facing the viewer, feet off the ground, arms stretched up, happy",
    "atterra": "landing from a jump facing the viewer, knees bent, arms out to the sides for balance",
    "seduto": "sitting on the ground facing the viewer, legs crossed, hands on the knees, smiling",
    "inchino": "bowing politely toward the viewer, one arm across the belly, the other arm out to the side",
    "lato_sx": "standing seen from the side in profile facing left, smiling",
    "tre_quarti": "standing in three-quarter view turned slightly to the right, looking at the viewer, smiling",
    "tre_quarti_sx": "standing in three-quarter view turned slightly to the left, looking at the viewer, smiling",
    "abbraccia": "standing facing the viewer, arms wide open ready for a hug, big warm smile",
    "occhi_chiusi": "standing facing the viewer, eyes closed happily, gentle smile, arms down",
    "guarda_su": "standing facing the viewer, looking up at the sky with amazed open mouth, one hand pointing up",
    "piega": "bending forward to pick something up from the ground, one hand reaching down",
    "balla2": "dancing facing the viewer, both arms up waving, swinging the hips, one foot raised behind",
    "pensa": "standing facing the viewer, thinking with one finger on the chin, looking up",
}


def chiedi(prompt, wait=15):
    for n in range(10):
        time.sleep(wait if n else 2)
        try:
            r = requests.post("https://gen.pollinations.ai/v1/images/generations", json={"model": MODEL, "prompt": prompt, "size": "1024x1024", "n": 1, "seed": SEED}, timeout=300)
            if r.status_code == 200: return Image.open(io.BytesIO(base64.b64decode(r.json()["data"][0]["b64_json"]))).convert("RGB")
            print("   HTTP", r.status_code)
        except requests.RequestException as e: print("   rete:", e)
    raise RuntimeError("Pollinations non risponde")


def salva(raw, chi, posa, magenta):
    os.makedirs(os.path.join(HERE, "assets", "pose", "raw"), exist_ok=True)
    raw.save(os.path.join(HERE, "assets", "pose", "raw", f"{chi}_{posa}.jpg"), quality=93)
    o = ritaglia(raw, lo=20, span=60, magenta=magenta)
    o = o.crop(o.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox())
    k = 1.15                                                                 # scala FISSA: tutte le pose restano della stessa grandezza
    if o.width * k > 760 or o.height * k > 1330: k = min(760 / o.width, 1330 / o.height)
    o = o.resize((int(o.width * k), int(o.height * k)), Image.LANCZOS)
    c = Image.new("RGBA", (768, 1376), (0, 0, 0, 0)); c.paste(o, ((768 - o.width) // 2, 1376 - o.height - 40), o)
    c.save(os.path.join(HERE, "assets", "pose", f"{chi}_{posa}.png"))


def rifai_ritaglio(chi):
    for f in os.listdir(os.path.join(HERE, "assets", "pose", "raw")):
        if f.startswith(chi + "_") and f.endswith(".jpg"):
            salva(Image.open(os.path.join(HERE, "assets", "pose", "raw", f)), chi, f[len(chi) + 1:-4], "FF00FF" in CHARS[chi][1])


if __name__ == "__main__":
    if sys.argv[1] == "--ritaglia": rifai_ritaglio(sys.argv[2]); sys.exit()
    chi = sys.argv[1]; desc, bgc = CHARS[chi]
    for posa in [a for a in sys.argv[2:] if not a.startswith("--")] or list(POSES):
        f = os.path.join(HERE, "assets", "pose", f"{chi}_{posa}.png")
        if os.path.exists(f) and "--rifai" not in sys.argv: print("salto", posa); continue
        print("genero", chi, posa, flush=True)
        salva(chiedi(desc + ", pose: " + POSES[posa] + STYLE.format(bgc)), chi, posa, "FF00FF" in bgc)
