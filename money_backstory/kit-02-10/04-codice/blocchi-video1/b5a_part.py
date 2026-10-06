import sys,os
sys.argv=['x','0']
exec(open('b5.py').read().split('import shutil,sys')[0])
a,b=int(os.environ['A']),int(os.environ['B'])
os.makedirs('/home/claude/_f5',exist_ok=True)
for fn in range(a,min(b,int(round(30*29.45)))):
    drawA(fn/30).convert('RGB').save(f'/home/claude/_f5/{fn:04d}.png')
