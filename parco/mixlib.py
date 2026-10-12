import numpy as np, wave
from scipy.signal import lfilter, butter, sosfilt
SR = 44100; rng = np.random.default_rng(7)
def put(buf, sig, t0, g=1.0):
    i = int(t0*SR); N = len(buf)
    if i >= N or i < -len(sig): return
    j = min(N, i+len(sig)); k0 = max(0, -i); buf[max(0, i):j] += sig[k0:k0+(j-max(0, i))]*g
def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], btype="band", fs=SR, output="sos"), x)
def lp(x, f): return sosfilt(butter(2, f, btype="low", fs=SR, output="sos"), x)
def pluck(f, dur=1.0, decay=0.996, bright=0.5):
    n = int(dur*SR); P = int(SR/f); x = np.zeros(n); x[:P] = rng.uniform(-1, 1, P)
    a = np.zeros(P+2); a[0] = 1; a[P] -= decay*(1-bright); a[P+1] -= decay*bright
    y = lfilter([1], a, x); return y/np.max(np.abs(y)+1e-9)
def marimba(f, dur=0.5):
    t = np.arange(int(dur*SR))/SR; return (np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*f*4*t)*np.exp(-18*t))*np.exp(-7*t)
def shaker(dur=0.07):
    n = int(dur*SR); return bp(rng.normal(size=n), 5500, 11000)*np.exp(-np.arange(n)/SR*55)
def tone(f, dur, decay=6):
    t = np.arange(int(dur*SR))/SR; return np.sin(2*np.pi*f*t)*np.exp(-decay*t)
def music(dur, bpm=108):
    N = int(dur*SR); mus = np.zeros(N); beat = 60/bpm
    chords = [([261.63, 329.63, 392.0], 65.41), ([246.94, 293.66, 392.0], 98.0), ([261.63, 329.63, 440.0], 110.0), ([261.63, 349.23, 440.0], 87.31)]
    melo = [(659.25, .5), (783.99, .5), (880, 1), (783.99, 1), (659.25, 1), (587.33, .5), (659.25, .5), (783.99, 1), (659.25, 1), (587.33, 1),
            (659.25, .5), (783.99, .5), (880, 1), (1046.5, 1), (880, 1), (783.99, .5), (698.46, .5), (659.25, 1), (587.33, 1), (523.25, 1)]
    t = 0.0; bar = 0
    while t < dur:
        fs, bass = chords[bar % 4]
        for k, f in enumerate(fs): put(mus, pluck(f, 1.2, 0.994, 0.45), t+k*0.025, 0.25)
        put(mus, marimba(bass*2, 0.9), t, 0.55); put(mus, marimba(bass*2, 0.6), t+2*beat, 0.4)
        for k, f in enumerate(fs): put(mus, pluck(f*2, 0.7, 0.993, 0.5), t+beat*(1+k*0.5), 0.12)
        tm = t
        for f, b in melo[(bar % 4)*5:(bar % 4)*5+5]: put(mus, pluck(f, 0.9, 0.997, 0.5), tm, 0.30); tm += b*beat
        for q in range(8): put(mus, shaker(), t+q*beat/2, 0.14 if q % 2 else 0.07)
        t += 4*beat; bar += 1
    mus /= np.max(np.abs(mus)); return mus*np.minimum(1, (dur-np.arange(N)/SR)/1.5)
def birds(dur):
    N = int(dur*SR); b = np.zeros(N); tb = 1.0
    while tb < dur-1:
        for j in range(rng.integers(2, 5)):
            n = int(.09*SR); tt = np.arange(n)/SR; f0 = rng.uniform(2800, 3600)
            put(b, np.sin(2*np.pi*(f0*tt+700*tt**2/0.09))*np.sin(np.pi*tt/0.09)**2, tb+j*0.13, 0.5)
        tb += rng.uniform(3.2, 6.0)
    return b
def shimmer(buf, t0, g=1.0, notes=(1046.5, 1318.5, 1568, 2093, 2637)):
    for j, f in enumerate(notes):
        tt = np.arange(int(.9*SR))/SR; sig = np.sin(2*np.pi*f*tt)*np.exp(-5*tt)*(0.75+0.25*np.sin(2*np.pi*9*tt)); put(buf, sig, t0+j*0.06, 0.28*g)
    n = int(.6*SR); put(buf, bp(rng.normal(size=n), 5000, 11000)*np.exp(-np.arange(n)/SR*7), t0, 0.25*g)
def thud(buf, t, g=0.5):
    n = int(.06*SR); th = lp(rng.normal(size=n), 400)*np.exp(-np.arange(n)/SR*60); n2 = int(.07*SR)
    put(buf, th*2.5, t, g); put(buf, np.sin(2*np.pi*110*np.arange(n2)/SR)*np.exp(-np.arange(n2)/SR*50)*0.7, t, g)
def whoosh(buf, t, g=0.8, dur=0.45):
    n = int(dur*SR); put(buf, bp(rng.normal(size=n), 700, 3500)*np.sin(np.pi*np.arange(n)/n)**1.5, t, g)
def tonk(buf, t, g=0.9):
    n = int(.5*SR); tt = np.arange(n)/SR
    put(buf, np.sin(2*np.pi*180*tt)*np.exp(-12*tt)+0.6*np.sin(2*np.pi*310*tt)*np.exp(-16*tt)+lp(rng.normal(size=n), 1500)*np.exp(-60*tt)*1.2, t, g)
def pop(buf, t, f0=500, g=0.5):
    tt = np.arange(int(.12*SR))/SR; put(buf, np.sin(2*np.pi*(f0+2500*tt)*tt)*np.exp(-30*tt), t, g)
def bloop(buf, t, f0, g=0.35):
    tt = np.arange(int(.09*SR))/SR; put(buf, np.sin(2*np.pi*(f0*tt+f0*3*tt**2))*np.exp(-28*tt), t, g)
def finish(buf, path, voc, mus, fol, bird, duck_regions, mg=0.16, fg=0.30):
    N = len(buf); duck = np.zeros(N)
    for a, b in duck_regions: duck[int(a*SR):int(b*SR)] = 1
    duck = np.convolve(duck, np.ones(4000)/4000, mode="same")
    mix = voc + mus*mg*(1-0.5*duck) + fol*fg*(1-0.4*duck) + bird*0.035
    mix = np.tanh(mix*1.1)/np.tanh(1.1); mix *= 0.84/np.max(np.abs(mix))
    with wave.open(path, "w") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype(np.int16).tobytes())
    return 20*np.log10(np.max(np.abs(mix)))
def load_voice(path):
    with wave.open(path) as w: return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)/32768
