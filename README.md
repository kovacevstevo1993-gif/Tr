# 🐭 Video Educativo: Topolino Insegna a Contare

Un progetto Python che genera automaticamente un video educativo di 20 secondi in cui un simpatico topolino insegna ai bambini a contare da 1 a 10, con **voce narrante italiana naturale**.

## 📋 Caratteristiche

- ✨ **Animazione semplice e colorata** - Ideale per bambini
- 🎙️ **Voce italiana naturale** - Usa Google Text-to-Speech
- 🐭 **Topolino protagonista** - Guida i bambini nel conteggio
- 🔴 **Pallini visivi** - Aiuta la comprensione visiva dei numeri
- ⏱️ **Durata perfetta** - Circa 20 secondi, ideale per l'attenzione dei bambini
- 🎬 **Video ad alta qualità** - Risoluzione 1280x720p

## 🎯 Contenuto del Video

### Sezioni:
1. **INTRO** (2 secondi)
   - Titolo: "Impariamo a contare!"
   - Voce: "Ciao bambini! Oggi impariamo a contare da uno a dieci!"
   - Topolino che saluta

2. **NUMERI 1-10** (18 secondi)
   - Ogni numero (1.8 secondi):
     - Numero grande al centro
     - Pallini rossi per contare
     - Voce che pronuncia il numero
     - Topolino che insegna

3. **OUTRO** (2 secondi)
   - Titolo: "Bravissimo!"
   - Voce: "Complimenti! Bravo! Arrivederci!"
   - Topolino che balla con stelle

## 🚀 Installazione

### Requisiti:
- Python 3.7+
- pip (package manager di Python)

### Passo 1: Installa le dipendenze
```bash
pip install moviepy gtts
```

**Nota**: Se su Mac/Linux hai problemi, potrebbe servirti installare ffmpeg:
```bash
# Su macOS con Homebrew
brew install ffmpeg

# Su Ubuntu/Debian
sudo apt-get install ffmpeg

# Su Windows con Chocolatey
choco install ffmpeg
```

## 📖 Come Usare

### Esecuzione semplice:
```bash
python video_topolino.py
```

### Il processo:
1. Lo script genera i file audio in italiano (gTTS)
2. Crea i frame visivi dell'animazione
3. Unisce audio e video
4. Salva il file finale: `video_topolino_conta.mp4`

### Output:
```
🎬 Creazione video educativo con voce italiana...
📝 Generazione audio in corso (può richiedere alcuni secondi)...

1️⃣  Creazione INTRO...
🎙️  Generazione audio: 'Ciao bambini! Oggi impariamo a contare da uno a dieci!'...
2️⃣  Creazione frame numero 1...
🎙️  Generazione audio: 'Numero 1'...
...
✅ Video creato con successo!
📁 File: video_topolino_conta.mp4
⏱️  Durata: ~20 secondi
📊 Risoluzione: 1280x720p
🎙️  Audio: Voce italiana naturale
```

## 📁 File Generati

Dopo l'esecuzione, troverai:
- `video_topolino_conta.mp4` - **Il video finale** ⭐
- `intro_audio.mp3` - Audio intro
- `numero_1_audio.mp3` - Audio numero 1
- `numero_2_audio.mp3` - Audio numero 2
- ... (fino a numero 10)
- `outro_audio.mp3` - Audio outro

**Puoi cancellare i file audio .mp3 dopo la creazione del video.**

## 🎨 Personalizzazione

### Cambiare i colori:
Nel file `video_topolino.py`, modifica queste variabili:
```python
BG_COLOR = (135, 206, 235)  # Azzurro cielo (R, G, B)
TEXT_COLOR = (255, 255, 255)  # Bianco (R, G, B)
```

### Cambiare la durata:
```python
DURATION_PER_NUMERO = 1.8  # Secondi per numero
INTRO_DURATION = 2  # Secondi intro
OUTRO_DURATION = 2  # Secondi outro
```

### Cambiare il testo narrato:
Modifica le funzioni:
```python
create_audio("Tuo testo personalizzato", "file.mp3")
```

## ⚠️ Troubleshooting

### Errore: "ModuleNotFoundError: No module named 'moviepy'"
```bash
pip install --upgrade moviepy
```

### Errore: "ffmpeg not found"
Installa ffmpeg (vedi sezione Installazione sopra)

### Il video è troppo lento a generarsi
È normale! La prima volta genera gli audio da internet. Le volte successive sarà più veloce.

### Problemi con la voce italiana
Assicurati di avere una connessione internet (gTTS scarica da Google)

## 📚 Dipendenze Utilizzate

- **MoviePy** - Creazione e editing di video
- **gTTS** (Google Text-to-Speech) - Generazione voce italiana
- **FFmpeg** - Codifica video

## 💡 Idee per Estensioni

- [ ] Aggiungere musica di sottofondo
- [ ] Animazioni del topolino (spostamenti)
- [ ] Colori diversi per ogni numero
- [ ] Diversi livelli di difficoltà
- [ ] Video in altre lingue
- [ ] Interattività con domande

## 📄 Licenza

Libero da usare per scopi educativi.

## 👨‍👩‍👧‍👦 Perfetto per:

- 🎓 Lezioni scolastiche
- 👶 Bambini in età prescolare (2-5 anni)
- 📱 Piattaforme educative online
- 📺 Canali YouTube educativi
- 🏠 Homeschooling

---

**Creato con ❤️ per insegnare ai bambini a contare!** 🐭✨
