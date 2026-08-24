#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script di esecuzione: Genera il video educativo con topolino che insegna a contare
"""

import subprocess
import sys

# Installa le dipendenze necessarie
print("📦 Installazione dipendenze in corso...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "moviepy", "gtts"])

# Importa e esegui lo script principale
print("\n🎬 Avvio generazione video...\n")
exec(open('video_topolino.py').read())
