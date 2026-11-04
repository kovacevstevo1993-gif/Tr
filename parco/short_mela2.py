#!/usr/bin/env python3
"""Short 'Chi ha mangiato il mela2': montaggio delle 7 clip Wan 2.2 (animazione vera) a 1080x1920 30 fps + pulsante ISCRIVITI finale,
poi mix audio (voci audioV, musica, effetti) -> short_la_mela_di_spike.mp4. Niente sottotitoli.
    python3 short_palloncino.py info | video | mix | finale"""
import json, os, subprocess, sys
import numpy as np
from PIL import Image
from short_razzo import subscribe_button

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "assets", "v", "mela2")
W, H, FPS = 1080, 1920, 30
LENS = [2.5, 2.5, 3.0, 3.6]          # durata di ogni clip (s)
N = 4
DUR = sum(LENS)
DV = json.load(open(os.path.join(HERE, "audioV", "durate.json")))
# battute: (chiave, inizio)
VOICES = [("c1", 0.3), ("s1", 2.8), ("s2", 5.3)]
T_SUB = 9.0
TMP = os.path.join(D, "tmp")


def clip_frames(n):
    CLIP = LENS[n - 1]
    """Frame della clip n a 1080x1920 e 30 fps esatti (CLIP s): ricampionamento temporale + scala lanczos."""
    src = os.path.join(D, f"clip{n}.mp4")
    cmd = ["ffmpeg", "-loglevel", "error", "-i", src, "-vf",
           f"minterpolate=fps={FPS}:mi_mode=blend,scale={W}:{H}:flags=lanczos,setsar=1", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
    need = int(round(CLIP * FPS))
    idx = np.clip(np.round(np.linspace(0, len(fr) - 1, need)).astype(int), 0, len(fr) - 1)
    return fr[idx]


def video(out):
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "17", "-preset", "medium", out], stdin=subprocess.PIPE)
    i = 0
    for n in range(1, N + 1):
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
    for t in (0.0, 2.5, 5.0, 8.0): M.pop(fol, t, 520, 0.25)                                    # stacchetto a ogni taglio
    M.shimmer(fol, 0.2, 0.4); M.bloop(fol, 4.6, 600, 0.3); M.shimmer(fol, 7.4, 0.5)           # idea!
    for k in range(7): M.tonk(fol, 8.3 + k * 0.4, 0.45)                                       # sgranocchiano la mela
    M.shimmer(fol, T_SUB, 0.9, (1568, 2093, 2637, 3136, 3951))
    dr = []
    for k, t0 in VOICES:
        M.put(voc, M.load_voice(f"audioV/{k}.wav"), t0, 1.0); dr.append((t0, t0 + DV[k] + 0.15))
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
                               "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", os.path.join(HERE, "short_la_mela_di_spike.mp4")])
