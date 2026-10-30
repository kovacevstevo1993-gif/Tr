"""voce/bN.wav -> voce/bN_pad.wav con durata esatta = fotogrammi/30 (fotogrammi = ceil(durata voce*30), quindi solo silenzio aggiunto, voce intatta)."""
import subprocess, sys
fin = [int(x) for x in open('fine_blocchi.txt') if x.strip()]
for n in [int(x) for x in sys.argv[1].split(',')]:
    fr = fin[n-1] - (fin[n-2] if n > 1 else 0); T = fr / 30
    d = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'voce/b{n}.wav'],capture_output=True,text=True).stdout)
    assert d <= T + 0.001, (n, d, T)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'voce/b{n}.wav','-af','apad','-t',f'{T:.5f}','-ar','24000','-ac','1',f'voce/b{n}_pad.wav'],check=True)
    print(n, fr, round(T,3), 'voce', round(d,2))
