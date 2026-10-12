"""Mix audio: voci + musica (corde pizzicate, marimba, shaker) + foley (passi, whoosh, cestini) + cinguettii."""
import numpy as np, wave, sys
from scipy.signal import lfilter, butter, sosfilt
import render4 as R
SR = 44100; N = int(R.DUR*SR); rng = np.random.default_rng(7)

def put(buf, sig, t0, g=1.0):
    i = int(t0*SR)
    if i >= N or i < -len(sig): return
    j = min(N, i+len(sig)); k0 = max(0, -i)
    buf[max(0, i):j] += sig[k0:k0+(j-max(0, i))]*g

def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], btype="band", fs=SR, output="sos"), x)
def lp(x, f): return sosfilt(butter(2, f, btype="low", fs=SR, output="sos"), x)
def env(n, a=0.005, d=4.0):
    t = np.arange(n)/SR; return np.minimum(1, t/a)*np.exp(-d*t/(n/SR))

def pluck(f, dur=1.0, decay=0.996, bright=0.5):
    n = int(dur*SR); P = int(SR/f); x = np.zeros(n); x[:P] = rng.uniform(-1, 1, P)
    a = np.zeros(P+2); a[0] = 1; a[P] -= decay*(1-bright); a[P+1] -= decay*bright
    y = lfilter([1], a, x); return y/np.max(np.abs(y)+1e-9)

def marimba(f, dur=0.5):
    t = np.arange(int(dur*SR))/SR
    return (np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*f*4*t)*np.exp(-18*t))*np.exp(-7*t)

def shaker(dur=0.07):
    n = int(dur*SR); return bp(rng.normal(size=n), 5500, 11000)*np.exp(-np.arange(n)/SR*55)

def nf(name): return {"C": 261.63, "D": 293.66, "E": 329.63, "F": 349.23, "G": 392.0, "A": 440.0, "B": 493.88}[name[0]]*(2**(int(name[1])-4)) if len(name) == 2 else None

# ---------------- musica
mus = np.zeros(N); bpm = 108; beat = 60/bpm
chords = [("C", [261.63, 329.63, 392.0], 65.41), ("G", [246.94, 293.66, 392.0], 98.0), ("A", [261.63, 329.63, 440.0], 110.0), ("F", [261.63, 349.23, 440.0], 87.31)]
melo = [(659.25, .5), (783.99, .5), (880, 1), (783.99, 1), (659.25, 1),     # C
        (587.33, .5), (659.25, .5), (783.99, 1), (659.25, 1), (587.33, 1),   # G
        (659.25, .5), (783.99, .5), (880, 1), (1046.5, 1), (880, 1),         # Am
        (783.99, .5), (698.46, .5), (659.25, 1), (587.33, 1), (523.25, 1)]   # F
t = 0.0; bar = 0
while t < R.DUR:
    ch = chords[bar % 4]
    for k, f in enumerate(ch[1]): put(mus, pluck(f, 1.2, 0.994, 0.45), t+k*0.025, 0.25)                # accordo arpeggiato
    put(mus, marimba(ch[2]*2, 0.9), t, 0.55); put(mus, marimba(ch[2]*2, 0.6), t+2*beat, 0.4)           # basso
    for k, f in enumerate(ch[1]): put(mus, pluck(f*2, 0.7, 0.993, 0.5), t+beat*(1+k*0.5), 0.12)
    tm = t
    for f, b in melo[(bar % 4)*5:(bar % 4)*5+5]:
        put(mus, pluck(f, 0.9, 0.997, 0.5), tm, 0.30); tm += b*beat
    for q in range(8): put(mus, shaker(), t+q*beat/2, 0.14 if q % 2 else 0.07)
    t += 4*beat; bar += 1
mus *= 1.0/np.max(np.abs(mus)); mus *= np.minimum(1, (R.DUR-np.arange(N)/SR)/2.0)

# ---------------- foley
fol = np.zeros(N)
for name, gain in (("mouse", 0.9), ("chip", 1.0), ("spike", 1.05)):
    for te in R.walk_events(name):
        th = lp(rng.normal(size=int(.06*SR)), 400)*np.exp(-np.arange(int(.06*SR))/SR*60)
        thud = np.sin(2*np.pi*110*np.arange(int(.07*SR))/SR)*np.exp(-np.arange(int(.07*SR))/SR*50)
        put(fol, th*2.5+np.pad(thud, (0, max(0, len(th)-len(thud))))[:len(th)]*0.7, te, 0.5*gain)
for kind, ix, iy, who, tp, tl, b in R.ITEMS:
    tt = np.arange(int(.12*SR))/SR; put(fol, np.sin(2*np.pi*(500+2500*tt)*tt)*np.exp(-30*tt), tp, 0.55)        # raccolta "pop"
    n = int(.45*SR); w = bp(rng.normal(size=n), 700, 3500)*np.sin(np.pi*np.arange(n)/n)**1.5; put(fol, w, tl-0.12, 0.9)  # whoosh
    ti = tl+R.FLY; n = int(.5*SR); tt = np.arange(n)/SR
    tonk = np.sin(2*np.pi*180*tt)*np.exp(-12*tt) + 0.6*np.sin(2*np.pi*310*tt)*np.exp(-16*tt) + lp(rng.normal(size=n), 1500)*np.exp(-60*tt)*1.2
    put(fol, tonk, ti, 0.9)                                                                                    # colpo sul cestino
    for j, f in enumerate((1318.5, 1760.0, 2349.3)): put(fol, np.sin(2*np.pi*f*tt[:int(.6*SR)] if False else 2*np.pi*f*np.arange(int(.6*SR))/SR)*np.exp(-6*np.arange(int(.6*SR))/SR), ti+0.05+j*0.07, 0.3)  # brillantini
put(fol, bp(rng.normal(size=int(.25*SR)), 800, 6000)*np.exp(-np.arange(int(.25*SR))/SR*14), R.CHEER_T, 0.8)       # scoppio coriandoli
for off, n_ in ((0.0, "mouse"), (0.3, "chip"), (0.55, "spike")):
    k = 0
    while R.CHEER_T+(k+off)*0.9 < 49.2:
        th = lp(rng.normal(size=int(.08*SR)), 500)*np.exp(-np.arange(int(.08*SR))/SR*45); put(fol, th*2.0, R.CHEER_T+(k+off)*0.9+0.9*0.0+0.9, 0.35); k += 1
# cinguettii di fondo
bird = np.zeros(N); tb = 1.0
while tb < R.DUR-1:
    for j in range(rng.integers(2, 5)):
        n = int(.09*SR); tt = np.arange(n)/SR; f0 = rng.uniform(2800, 3600)
        put(bird, np.sin(2*np.pi*(f0*tt + 1400*tt**2/0.09*0.5))*np.sin(np.pi*tt/0.09)**2, tb+j*0.13, 0.5)
    tb += rng.uniform(3.2, 6.0)

# ---------------- voci + ducking
voc = np.zeros(N); duck = np.zeros(N)
for key, t0, who, txt, dur in R.VOICES:
    with wave.open(f"audio3/{key}.wav") as w: a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)/32768
    put(voc, a, t0, 1.0); duck[int(t0*SR):int((t0+dur+0.15)*SR)] = 1
duck = np.convolve(duck, np.ones(4000)/4000, mode="same")
mix = voc*1.0 + mus*0.16*(1-0.5*duck) + fol*0.30*(1-0.4*duck) + bird*0.035
mix = np.tanh(mix*1.1)/np.tanh(1.1)
mix *= 0.84/np.max(np.abs(mix))
with wave.open("mix4.wav", "w") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype(np.int16).tobytes())
print("ok picco dB", 20*np.log10(np.max(np.abs(mix))))
