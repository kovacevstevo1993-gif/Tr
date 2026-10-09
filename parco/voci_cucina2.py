#!/usr/bin/env python3
"""Voci ITALIANE native (edge-tts) per lo Short v2 -> audioD/*.wav + durate.json.
Narratrice: Isabella (dolce). Bambini: tre timbri diversi (Diego/Elsa/Giuseppe) con tono alzato.
Uso: python3 voci_cucina2.py [chiave ...] [--rifai]"""
import certifi
certifi.where = lambda: "/root/.ccr/ca-bundle.crt"      # sandbox: serve il bundle del proxy (va tolto altrove)
import asyncio, json, os, subprocess, sys, wave
import edge_tts

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "audioD")

# voce edge-tts, rate, pitch (Hz), rialzo del tono in post (rapporto), guadagno
VOCE = {
    # tono alzato dal motore neurale (naturale) + solo un ritocco minimo in post: così non suona robotico
    "narr": ("it-IT-IsabellaNeural", "-4%", "+3Hz", 1.0),
    "mouse": ("it-IT-DiegoNeural", "+8%", "+34Hz", 1.07),
    "chip": ("it-IT-ElsaNeural", "+10%", "+40Hz", 1.05),
    "spike": ("it-IT-GiuseppeMultilingualNeural", "+2%", "+26Hz", 1.08),
}

RIGHE = [
    ("n1", "narr", "Zitti, zitti... sentite? Qualcosa bussa nel barattolo dei biscotti!"),
    ("t1", "mouse", "Toc toc? Chi c'è?"),
    ("n2", "narr", "Il topolino chiama i suoi amici."),
    ("t2", "mouse", "Chip! Spike! Venite!"),
    ("c1", "chip", "Arrivo!"),
    ("s1", "spike", "Aspettami!"),
    ("n3", "narr", "Ora tutti insieme... contiamo fino a tre!"),
    ("t3", "mouse", "Uno!"),
    ("c3", "chip", "Due!"),
    ("s3", "spike", "Tre!"),
    ("o1", "mouse", "Oooh!"),
    ("o2", "chip", "Oooh!"),
    ("n4", "narr", "Ma guarda! È una farfalla magica!"),
    ("c2", "chip", "Che bella!"),
    ("s2", "spike", "Prendiamola!"),
    ("n5", "narr", "Ma la farfalla è troppo veloce... e vola via dalla finestra."),
    ("t4", "mouse", "Ciao ciao, farfalla!"),
    ("n6", "narr", "Però lascia una magia: un biscotto per ognuno!"),
    ("c4", "chip", "Che buono!"),
    ("s4", "spike", "Mmm, delizioso!"),
    ("n7", "narr", "Condividere è sempre più bello."),
    ("end", "mouse", "Bambini Ciao Ciao! Iscrivetevi al canale!"),
]


async def sintetizza(testo, voce, rate, pitch, path):
    for n in range(5):
        try:
            await edge_tts.Communicate(testo, voce, rate=rate, pitch=pitch).save(path)
            if os.path.getsize(path) > 1000: return
        except Exception as e:
            print("   riprovo:", str(e)[:80]); await asyncio.sleep(2 * (n + 1))
    raise RuntimeError("edge-tts non risponde")


def post(mp3, wav, rialzo, pausa=0.18):
    filt = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.04,areverse,"
            "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.10,areverse")
    filt += f",silenceremove=stop_periods=-1:stop_duration=0.22:stop_threshold=-40dB:stop_silence={pausa}"   # accorcia le pause lunghe
    if rialzo != 1.0: filt += f",rubberband=pitch={rialzo}"
    filt += ",loudnorm=I=-16:TP=-1.5:LRA=7,aresample=44100"
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-af", filt, "-ac", "1", "-sample_fmt", "s16", wav])
    with wave.open(wav) as w: return w.getnframes() / w.getframerate()


async def main():
    os.makedirs(OUT, exist_ok=True)
    pj = os.path.join(OUT, "durate.json")
    dur = json.load(open(pj)) if os.path.exists(pj) else {}
    scelte = [a for a in sys.argv[1:] if not a.startswith("--")]
    for k, chi, txt in RIGHE:
        if scelte and k not in scelte: continue
        wav = os.path.join(OUT, f"{k}.wav")
        if os.path.exists(wav) and k in dur and "--rifai" not in sys.argv: continue
        v, rate, pitch, riz = VOCE[chi]
        print(f"🎙️  {k} ({chi}): {txt}")
        mp3 = os.path.join(OUT, f"{k}_raw.mp3")
        await sintetizza(txt, v, rate, pitch, mp3)
        dur[k] = round(post(mp3, wav, riz, 0.26 if chi == "narr" else 0.12), 3)
        os.remove(mp3)
        json.dump(dur, open(pj, "w"), indent=1)
    print("✅", dur)


if __name__ == "__main__":
    asyncio.run(main())
