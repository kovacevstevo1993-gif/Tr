from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"

def draw(img, lines, box, colors):
    """box = (x, y, w) area in pixel; testo centrato dentro la larghezza w"""
    d = ImageDraw.Draw(img)
    x, y, w = box
    # trova la size che fa stare la riga piu lunga dentro w
    longest = max(lines, key=len)
    size = 10
    while True:
        f = ImageFont.truetype(FONT, size + 2)
        if d.textlength(longest, font=f) > w:
            break
        size += 2
    f = ImageFont.truetype(FONT, size)
    stroke = max(3, size // 12)
    line_h = int(size * 1.08)
    for i, (line, col) in enumerate(zip(lines, colors)):
        tw = d.textlength(line, font=f)
        lx = x + (w - tw) / 2
        ly = y + i * line_h
        d.text((lx, ly), line, font=f, fill=col,
               stroke_width=stroke, stroke_fill=(0, 0, 0))
    return img

LINES = ["21 KILLED BY", "MOLASSES"]
COLORS = [(255, 255, 255), (245, 196, 42)]

# A - faccia grande + onda, scritta in alto a destra
a = Image.open("/mnt/user-data/uploads/IMG_20260927_201206.png").convert("RGB")
W, H = a.size
draw(a, LINES, (int(W*0.50), int(H*0.05), int(W*0.46)), COLORS)
a.save("/mnt/user-data/outputs/miniatura_A_faccia_onda.jpg", quality=92)

# B - campo lungo, scritta in alto a sinistra
b = Image.open("/mnt/user-data/uploads/IMG_20260927_200856.png").convert("RGB")
W, H = b.size
draw(b, LINES, (int(W*0.03), int(H*0.04), int(W*0.45)), COLORS)
b.save("/mnt/user-data/outputs/miniatura_B_campo_lungo.jpg", quality=92)

print("ok")
