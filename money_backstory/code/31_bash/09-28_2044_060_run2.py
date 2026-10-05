import sys, os, time
sys.path.insert(0,'/home/claude/slides')
from scenes2 import *
os.makedirs('/mnt/user-data/outputs', exist_ok=True)
log='/tmp/render2.log'
open(log,'w').write('start\n')
for n in [1,2,3,4,5,6]:
    fn, nf = SCENES[n]
    t0=time.time()
    render_seq(fn, nf, f'/mnt/user-data/outputs/short2-0{n}.mp4', log=log)
    open(log,'a').write(f'DONE {n} in {time.time()-t0:.0f}s\n')
open(log,'a').write('ALL DONE\n')