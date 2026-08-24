#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Video educativo: Un topolino insegna a contare da 1 a 10
Con voce narrante italiana naturale
Durata: 20 secondi
"""

from moviepy.editor import (
    TextClip, ColorClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip
)
from gtts import gTTS
import os

# Configurazione
WIDTH, HEIGHT = 1280, 720
FPS = 30
DURATION_PER_NUMERO = 1.8  # 1.8 secondi per numero (10 numeri = 18 secondi)
INTRO_DURATION = 2  # 2 secondi intro
OUTRO_DURATION = 2  # 2 secondi outro

# Colori
BG_COLOR = (135, 206, 235)  # Azzurro cielo
TEXT_COLOR = (255, 255, 255)  # Bianco

def create_audio(text, filename, lang="it"):
    """Crea un file audio con voce italiana naturale usando Google Text-to-Speech"""
    print(f"  🎙️  Generazione audio: '{text}'...")
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)
    return filename

def create_intro():
    """Crea l'intro con il topolino che dice ciao"""
    bg = ColorClip(size=(WIDTH, HEIGHT), color=BG_COLOR).set_duration(INTRO_DURATION)
    
    # Titolo grande
    title = TextClip(
        "Impariamo a contare!",
        fontsize=70,
        color=TEXT_COLOR,
        font="Arial-Bold",
        method="caption",
        size=(WIDTH-100, None)
    ).set_position("center").set_duration(INTRO_DURATION)
    
    # Topolino grande
    topolino = TextClip(
        "🐭",
        fontsize=150,
        font="Arial"
    ).set_position(("center", 500)).set_duration(INTRO_DURATION)
    
    # Audio intro
    audio_intro = create_audio("Ciao bambini! Oggi impariamo a contare da uno a dieci!", "intro_audio.mp3")
    audio_clip = AudioFileClip(audio_intro).set_duration(INTRO_DURATION)
    
    video = CompositeVideoClip([bg, title, topolino])
    return video.set_audio(audio_clip)

def create_numero_frame(numero):
    """Crea un frame per ogni numero con audio"""
    bg = ColorClip(size=(WIDTH, HEIGHT), color=BG_COLOR).set_duration(DURATION_PER_NUMERO)
    
    # Numero grande
    numero_text = TextClip(
        str(numero),
        fontsize=200,
        color=TEXT_COLOR,
        font="Arial-Bold"
    ).set_position(("center", 250)).set_duration(DURATION_PER_NUMERO)
    
    # Testo "Numero X"
    numero_label = TextClip(
        f"Numero {numero}",
        fontsize=60,
        color=TEXT_COLOR,
        font="Arial",
        method="caption",
        size=(WIDTH-100, None)
    ).set_position(("center", 150)).set_duration(DURATION_PER_NUMERO)
    
    # Pallini per contare
    pallini = "🔴 " * numero
    pallini_text = TextClip(
        pallini,
        fontsize=40,
        color=TEXT_COLOR,
        font="Arial",
        method="caption",
        size=(WIDTH-100, None)
    ).set_position(("center", 500)).set_duration(DURATION_PER_NUMERO)
    
    # Topolino emoji
    topolino = TextClip(
        "🐭",
        fontsize=100,
        font="Arial"
    ).set_position((100, 100)).set_duration(DURATION_PER_NUMERO)
    
    # Audio per il numero
    audio_file = f"numero_{numero}_audio.mp3"
    create_audio(f"Numero {numero}", audio_file)
    audio_clip = AudioFileClip(audio_file).set_duration(DURATION_PER_NUMERO)
    
    video = CompositeVideoClip([bg, numero_label, numero_text, pallini_text, topolino])
    return video.set_audio(audio_clip)

def create_outro():
    """Crea l'outro con complimenti"""
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
    
    # Topolino che balla
    topolino = TextClip(
        "🐭 ⭐ 🐭",
        fontsize=100,
        font="Arial"
    ).set_position(("center", 550)).set_duration(OUTRO_DURATION)
    
    # Audio outro
    audio_outro = create_audio("Complimenti! Bravo! Arrivederci!", "outro_audio.mp3")
    audio_clip = AudioFileClip(audio_outro).set_duration(OUTRO_DURATION)
    
    video = CompositeVideoClip([bg, text, subtext, topolino])
    return video.set_audio(audio_clip)

def create_video():
    """Crea il video completo con voce italiana"""
    print("🎬 Creazione video educativo con voce italiana...")
    print("📝 Generazione audio in corso (può richiedere alcuni secondi)...\n")
    
    # Crea tutti i clip
    clips = []
    
    # Intro
    print("1️⃣  Creazione INTRO...")
    clips.append(create_intro())
    
    # Aggiungi i numeri da 1 a 10
    for numero in range(1, 11):
        print(f"{numero+1}️⃣  Creazione frame numero {numero}...")
        clips.append(create_numero_frame(numero))
    
    # Outro
    print("1️⃣2️⃣  Creazione OUTRO...")
    clips.append(create_outro())
    
    # Concatena tutti i clip
    print("\n🎞️  Unione di tutti i frame...")
    video = concatenate_videoclips(clips)
    
    # Salva il video
    output_file = "video_topolino_conta.mp4"
    print(f"💾 Salvataggio video in '{output_file}'...\n")
    video.write_videofile(
        output_file,
        fps=FPS,
        codec="libx264",
        audio_codec="aac",
        verbose=False,
        logger=None
    )
    
    print(f"\n✅ Video creato con successo!")
    print(f"📁 File: {output_file}")
    print(f"⏱️  Durata: ~20 secondi")
    print(f"📊 Risoluzione: {WIDTH}x{HEIGHT}p")
    print(f"🎙️  Audio: Voce italiana naturale")

if __name__ == "__main__":
    create_video()
