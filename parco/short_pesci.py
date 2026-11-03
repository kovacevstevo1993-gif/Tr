#!/usr/bin/env python3
"""Short 'Chi ha mangiato il mela2': montaggio delle 7 clip Wan 2.2 (animazione vera) a 1080x1920 30 fps + pulsante ISCRIVITI finale,
poi mix audio (voci audioAC, musica, effetti) -> short_contiamo_i_pesci.mp4. Niente sottotitoli.
    python3 short_palloncino.py info | video | mix | finale"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image
from short_razzo import subscribe_button

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "assets", "v", "pesci")
W, H, FPS = 1080, 1920, 30
ORDER = [1, 2, 3, 4, 5]
LENS = [3.5, 3.5, 3.5, 3.5, 5.0]
N = 5
DUR = sum(LENS)
DV = json.load(open(os.path.join(HERE, "audioAC", "durate.json")))
# battute: (chiave, inizio)
VOICES = [("n1", 1.5), ("n2", 5.0), ("n3", 8.5), ("n4", 12.0), ("n5", 14.3)]
T_SUB = 16.5
TMP = os.path.join(D, "tmp")


def clip_frames(n):
    CLIP = LENS[ORDER.index(n)]
    """Frame della clip n a 1080x1920 e 30 fps esatti (CLIP s): ricampionamento temporale + scala lanczos."""
    src = os.path.join(D, f"clip{n}.mp4")
    cmd = ["ffmpeg", "-loglevel", "error", "-i", src, "-vf",
           f"fps={FPS},scale={W}:{H}:flags=lanczos,setsar=1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
    need = int(round(CLIP * FPS))
    idx = np.clip(np.round(np.linspace(0, len(fr) - 1, need)).astype(int), 0, len(fr) - 1)
    return fr[idx]


def video(out):
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "medium", out], stdin=subprocess.PIPE)
    i = 0
    for n in ORDER:
        for f in clip_frames(n):
            t = i / FPS
            if t >= T_SUB:
                img = Image.fromarray(f); subscribe_button(img, t, T_SUB, cy=1780); f = np.asarray(img)
            ff.stdin.write(np.ascontiguousarray(f).tobytes()); i += 1
    ff.stdin.close(); ff.wait(); print("frame", i)


def mix(out):
    import mixlib as M
    n = int(DUR * M.SR); voc = np.zeros(n); fol = np.zeros(n); bird = M.birds(DUR) if hasattr(M, "birds") else np.zeros(n)
    mus = M.music(DUR, bpm=124)
    for t in (3.5, 7.0, 10.5, 14.0): M.pop(fol, t, 520, 0.25)                                  # stacchetto a ogni taglio
    for t in (1.2, 4.7, 8.2, 11.7): M.bloop(fol, t, 600, 0.3); M.thud(fol, t + 0.4, 0.4)       # il pesce salta fuori e cade
    M.shimmer(fol, T_SUB, 0.9, (1568, 2093, 2637, 3136, 3951))
    dr = []
    for k, t0 in VOICES:
        M.put(voc, M.load_voice(f"audioAC/{k}.wav"), t0, 1.0); dr.append((t0, t0 + DV[k] + 0.15))
    print("picco dB", M.finish(np.zeros(n), out, voc, mus, fol, bird, dr, mg=0.15, fg=0.32))


if __name__ == "__main__":
    os.makedirs(TMP, exist_ok=True)
    cmd = sys.argv[1]
    if cmd == "info":
        for k, t0 in VOICES: print(k, t0, round(t0 + DV[k], 2))
        print("DUR", DUR)
    elif cmd == "video": video(os.path.join(TMP, "muto.mp4"))
    elif cmd == "mix": mix(os.path.join(TMP, "mix.wav"))
    elif cmd == "finale":
        subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(TMP, "muto.mp4"), "-i", os.path.join(TMP, "mix.wav"),
                               "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", os.path.join(HERE, "short_contiamo_i_pesci.mp4")])
