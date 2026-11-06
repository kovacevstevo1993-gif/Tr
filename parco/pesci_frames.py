#!/usr/bin/env python3
"""Fotogrammi di partenza 'Contiamo i pesci' con il numero GIUSTO di pesci sul ghiaccio: pesce ritagliato (GrabCut) dall'ultimo fotogramma di clip1 e incollato k volte su R.png -> assets/v/pesci/fk1..fk4.png (720x1280)"""
import cv2, numpy as np
from PIL import Image, ImageFilter
D = "assets/v/pesci"
def fish():
    im = cv2.imread(f"{D}/last1.png"); mask = np.full(im.shape[:2], cv2.GC_BGD, np.uint8); bg = np.zeros((1, 65)); fg = np.zeros((1, 65))
    mask[640:755, 70:430] = cv2.GC_PR_BGD
    cv2.ellipse(mask, (250, 684), (172, 32), 8, 0, 360, cv2.GC_PR_FGD, -1)        # corpo del pesce (probabile primo piano)
    cv2.ellipse(mask, (240, 684), (125, 16), 8, 0, 360, cv2.GC_FGD, -1)             # nucleo sicuro
    cv2.ellipse(mask, (112, 662), (30, 22), 8, 0, 360, cv2.GC_FGD, -1)             # testa col muso e l'occhio
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV); water = (hsv[..., 0] > 100) & (hsv[..., 0] < 130) & (hsv[..., 1] > 150) & (hsv[..., 2] > 130)
    mask[(mask != cv2.GC_FGD) & water] = cv2.GC_BGD                                # acqua blu saturata = sfondo
    cv2.grabCut(im, mask, None, bg, fg, 12, cv2.GC_INIT_WITH_MASK)
    m = np.where((mask == 1) | (mask == 3), 255, 0).astype(np.uint8); m[:630] = 0
    m = cv2.GaussianBlur(cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)), (5, 5), 0)
    rgba = cv2.cvtColor(im, cv2.COLOR_BGR2RGBA); rgba[..., 3] = m
    out = Image.fromarray(rgba); print("bbox", out.getbbox()); return out.crop(out.getbbox())
POS = [(70, 1010), (360, 1010), (70, 1140), (360, 1140)]      # angolo in alto a sinistra di ogni pesce
if __name__ == "__main__":
    f = fish(); W = 270; f = f.resize((W, int(f.height * W / f.width)), Image.LANCZOS); f.save(f"{D}/fish_cut.png")
    base = Image.open(f"{D}/R.png").convert("RGB").resize((720, 1280), Image.LANCZOS)
    for k in range(1, 5):
        im = base.copy()
        for (x, y) in POS[:k]:
            sh = Image.new("RGBA", (f.width, f.height), (0, 0, 0, 0)); sh.paste((20, 40, 80, 90), (0, 0), f.split()[3]); sh = sh.filter(ImageFilter.GaussianBlur(6))
            im.paste(sh, (x + 8, y + 12), sh); im.paste(f, (x, y), f)
        im.save(f"{D}/fk{k}.png"); print("fk", k)
    Image.open(f"{D}/fk4.png").resize((360, 640)).save("/tmp/fk4.png")
