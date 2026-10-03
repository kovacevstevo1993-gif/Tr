import numpy as np, wave, subprocess, sys
sys.path.insert(0, ".")
import render as R
SR = 44100; N = int(R.DUR*SR)
def tone(f, d, kind="tri", vol=1.0):
    t = np.arange(int(d*SR))/SR
    if kind == "tri": w = 2/np.pi*np.arcsin(np.sin(2*np.pi*f*t))
    elif kind == "sq": w = np.sign(np.sin(2*np.pi*f*t))*0.5
    else: w = np.sin(2*np.pi*f*t)
    env = np.minimum(1, t/0.01) * np.exp(-3.5*t/d)
    return w*env*vol
def put(buf, sig, t0):
    i = int(t0*SR); j = min(N, i+len(sig))
    if i < N: buf[i:j] += sig[:j-i]
# musica: giro di do maggiore, allegra
mus = np.zeros(N); bpm = 116; beat = 60/bpm
mel = [(523.25,1),(659.25,1),(783.99,1),(659.25,1),(880,1),(783.99,1),(659.25,2),
       (698.46,1),(659.25,1),(587.33,1),(523.25,1),(587.33,1),(659.25,1),(523.25,2)]
bass = [130.81,196.0,220.0,174.61]
t = 0; k = 0
while t < R.DUR:
    for f, b in mel:
        put(mus, tone(f, b*beat*0.9, "tri", 0.5), t); t += b*beat
        if t >= R.DUR: break
bt = 0; k = 0
while bt < R.DUR:
    put(mus, tone(bass[k % 4], beat*1.8, "sin", 0.6), bt); put(mus, tone(bass[k % 4]*2, beat*0.5, "sin", 0.25), bt+beat)
    bt += beat*2; k += 1
mus *= 0.16 / max(1e-9, np.abs(mus).max())
fade = np.minimum(1, (R.DUR-np.arange(N)/SR)/1.5); mus *= fade
# effetti
sfx = np.zeros(N)
for kind, x, y, who, tp, tl, b in R.ITEMS:
    put(sfx, tone(900, 0.12, "sin", 0.5)+tone(1200, 0.12, "sin", 0.3), tp)           # raccolta
    t2 = tl + R.FLY
    put(sfx, tone(220, 0.18, "sq", 0.6), t2)                                         # tonf nel cestino
    put(sfx, tone(1046.5, 0.25, "tri", 0.5), t2+0.08); put(sfx, tone(1568, 0.3, "tri", 0.4), t2+0.18)
for i, f in enumerate((523, 659, 784, 1046)): put(sfx, tone(f, 0.35, "tri", 0.5), 27.1+i*0.09)
sfx *= 0.45
# voci
voc = np.zeros(N)
for key, t0, who, txt, dur in R.VOICES:
    with wave.open(f"audio/{key}.wav") as w:
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)/32768
        if w.getnchannels() == 2: a = a[::2]
    put(voc, a*0.9, t0)
# ducking leggero: musica più bassa quando parla la voce
env = np.zeros(N)
for key, t0, who, txt, dur in R.VOICES: env[int(t0*SR):int((t0+dur)*SR)] = 1
env = np.convolve(env, np.ones(2000)/2000, mode="same")
mus *= (1 - 0.45*env)
mix = voc + mus + sfx
mix /= max(1.0, np.abs(mix).max()/0.89)
pcm = (mix*32767).astype(np.int16)
with wave.open("mix.wav", "w") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("peak", 20*np.log10(np.abs(mix).max()))
