!pip install moviepy gtts -q
print("✅ Dipendenze installate!")

from moviepy.editor import (
    TextClip, ColorClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip
)
from gtts import gTTS

# Configurazione
WIDTH, HEIGHT = 1280, 720
FPS = 30
DURATION_PER_NUMERO = 1.8
INTRO_DURATION = 2
OUTRO_DURATION = 2

# Colori
BG_COLOR = (135, 206, 235)
TEXT_COLOR = (255, 255, 255)

def create_audio(text, filename, lang="it"):
    print(f"🎙️  Audio: '{text}'...")
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)
    return filename

def create_intro():
    bg = ColorClip(size=(WIDTH, HEIGHT), color=BG_COLOR).set_duration(INTRO_DURATION)
    
    title = TextClip(
        "Impariamo a contare!",
        fontsize=70,
        color=TEXT_COLOR,
        font="Arial-Bold",
        method="caption",
        size=(WIDTH-100, None)
    ).set_position("center").set_duration(INTRO_DURATION)
    
    topolino = TextClip(
        "🐭",
        fontsize=150,
        font="Arial"
    ).set_position(("center", 500)).set_duration(INTRO_DURATION)
    
    audio_intro = create_audio("Ciao bambini! Oggi impariamo a contare da uno a dieci!", "intro_audio.mp3")
    audio_clip = AudioFileClip(audio_intro).set_duration(INTRO_DURATION)
    
    video = CompositeVideoClip([bg, title, topolino])
    return video.set_audio(audio_clip)

def create_numero_frame(numero):
    bg = ColorClip(size=(WIDTH, HEIGHT), color=BG_COLOR).set_duration(DURATION_PER_NUMERO)
    
    numero_text = TextClip(
        str(numero),
        fontsize=200,
        color=TEXT_COLOR,
        font="Arial-Bold"
    ).set_position(("center", 250)).set_duration(DURATION_PER_NUMERO)
    
    numero_label = TextClip(
        f"Numero {numero}",
        fontsize=60,
        color=TEXT_COLOR,
        font="Arial",
        method="caption",
        size=(WIDTH-100, None)
    ).set_position(("center", 150)).set_duration(DURATION_PER_NUMERO)
    
    pallini = "🔴 " * numero
    pallini_text = TextClip(
        pallini,
        fontsize=40,
        color=TEXT_COLOR,
        font="Arial",
        method="caption",
        size=(WIDTH-100, None)
    ).set_position(("center", 500)).set_duration(DURATION_PER_NUMERO)
    
    topolino = TextClip(
        "🐭",
        fontsize=100,
        font="Arial"
    ).set_position((100, 100)).set_duration(DURATION_PER_NUMERO)
    
    audio_file = f"numero_{numero}_audio.mp3"
    create_audio(f"Numero {numero}", audio_file)
    audio_clip = AudioFileClip(audio_file).set_duration(DURATION_PER_NUMERO)
    
    video = CompositeVideoClip([bg, numero_label, numero_text, pallini_text, topolino])
    return video.set_audio(audio_clip)

def create_outro():
    bg = ColorClip(size=(WIDTH, HEIGHT), color=BG_COLOR).set_duration(OUTRO_DURATION)
    
    text = TextClip(
        "Bravissimo!",
        fontsize=70,
        color=TEXT_COLOR,
        font="Arial-Bold",
        method="caption",
        size=(WIDTH-100, None)
    ).set_position(("center", 250)).set_duration(OUTRO_DURATION)
    
    subtext = TextClip(
        "Hai imparato a contare!",
        fontsize=50,
        color=TEXT_COLOR,
        font="Arial",
        method="caption",
        size=(WIDTH-100, None)
    ).set_position(("center", 400)).set_duration(OUTRO_DURATION)
    
    topolino = TextClip(
        "🐭 ⭐ 🐭",
        fontsize=100,
        font="Arial"
    ).set_position(("center", 550)).set_duration(OUTRO_DURATION)
    
    audio_outro = create_audio("Complimenti! Bravo! Arrivederci!", "outro_audio.mp3")
    audio_clip = AudioFileClip(audio_outro).set_duration(OUTRO_DURATION)
    
    video = CompositeVideoClip([bg, text, subtext, topolino])
    return video.set_audio(audio_clip)

print("🎬 Creazione video in corso...\n")

clips = []

print("1️⃣  Creazione INTRO...")
clips.append(create_intro())

for numero in range(1, 11):
    print(f"{numero+1}️⃣  Numero {numero}...")
    clips.append(create_numero_frame(numero))

print("1️⃣2️⃣  Creazione OUTRO...")
clips.append(create_outro())

print("\n🎞️  Unione frame...")
video = concatenate_videoclips(clips)

output_file = "video_topolino_conta.mp4"
print(f"\n💾 Salvataggio video...\n")
video.write_videofile(
    output_file,
    fps=FPS,
    codec="libx264",
    audio_codec="aac",
    verbose=False,
    logger=None
)

print(f"\n✅ Video creato!")
print(f"📁 File: {output_file}")
print(f"⏱️  Durata: ~20 secondi")
print(f"📊 Risoluzione: 1280x720p")
print(f"🎙️  Audio: Voce italiana naturale")
