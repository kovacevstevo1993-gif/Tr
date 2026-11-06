"""Un MP4 per blocco: slide in fila + voce del blocco (taglio esatto ai confini dei blocchi). Uso: unisci.py 4-30"""
import sys, subprocess, glob, os
LIST = [int(x) for x in sys.argv[1].split(',')]; fin = [int(x) for x in open('fine_blocchi.txt') if x.strip()]
os.makedirs('consegna', exist_ok=True)
for n in LIST:
    fs = sorted(glob.glob(f'slide/v13-b{n}-*.mp4')); lst = f'/tmp/c13_{n}.txt'
    open(lst, 'w').write(''.join(f"file '{os.path.abspath(f)}'\n" for f in fs))
    out = f'consegna/V13-blocco{n:02d}.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', lst, '-i', f'voce/b{n}_pad.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-profile:v', 'main', '-crf', '16', '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], check=True)
    nf = int(subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', out], capture_output=True, text=True).stdout)
    att = fin[n - 1] - (fin[n - 2] if n > 1 else 0)
    print(n, nf, att, 'OK' if nf == att else 'DIVERSO', flush=True)
