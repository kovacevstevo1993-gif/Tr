import sys, os, json, subprocess
sys.argv = ["x", "/home/user/Tr/nuovo_canale_italia/pratica001"]
sys.path.insert(0, "/home/user/Tr/nuovo_canale_italia/code")
import render_v3 as V, render_pratica as R
from multiprocessing import Pool
PR = V.PR; T = json.load(open(os.path.join(PR, "tempi.json"))); NF = T["frames"]; bl = T["blocchi"]; passo = (NF + 15) // 16
R.Scene = V.V3
f0, f1 = 1 * passo, 2 * passo; sub = [(100 + j, f0 + j * (passo // 4 + 1), min(f1, f0 + (j + 1) * (passo // 4 + 1))) for j in range(4)]
with Pool(4, initializer=R.init, initargs=(bl,)) as pool: files = pool.map(R.lavora, sub)
tmp = os.path.join(PR, "_tmp"); open(os.path.join(tmp, "l1.txt"), "w").write("".join(f"file '{f}'\n" for f in files))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "l1.txt"), "-c", "copy", os.path.join(tmp, "parte01.mp4")], check=True)
allf = [os.path.join(tmp, f"parte{k:02d}.mp4") for k in range(16)]; open(os.path.join(tmp, "lista.txt"), "w").write("".join(f"file '{f}'\n" for f in allf))
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(tmp, "lista.txt"), "-i", os.path.join(PR, "_voce.wav"), "-i", os.path.join(PR, "_fx.wav"),
                "-filter_complex", "[1:a]loudnorm=I=-15:TP=-1.5[v];[2:a]volume=1.0[f];[v][f]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]",
                "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", os.path.join(PR, "video.mp4")], check=True)
print("fatto")
