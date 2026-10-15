"""voce/bN.wav -> voce/bN_pad.wav con durata esatta = fotogrammi/30. Voce piu' lunga di (fotogrammi/30-0,25): atempo (max 1,08)."""
import subprocess, sys
fin = [int(x) for x in open('fine_blocchi.txt') if x.strip()]
a, b = map(int, sys.argv[1].split('-'))
for n in range(a, b + 1):
    fr = fin[n-1] - (fin[n-2] if n > 1 else 0); T = fr / 30; tgt = T - 0.25
    d = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'voce/b{n}.wav'],capture_output=True,text=True).stdout)
    r = d / tgt; af = []
    if r > 1: af.append(f'atempo={r:.4f}')
    af.append('apad'); af = ','.join(af)
    if r > 1.08: print('!! blocco', n, 'rapporto', round(r, 3), 'OLTRE 1,08')
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'voce/b{n}.wav','-af',af,'-t',f'{T:.5f}','-ar','24000','-ac','1',f'voce/b{n}_pad.wav'],check=True)
    print(n, fr, round(T,3), 'voce', round(d,2), 'rapporto', round(r,3))
