import sys,glob
from PIL import Image
pre=sys.argv[1]
fs=sorted(glob.glob('prev/'+pre+'_*.png'))
ims=[Image.open(f).resize((270,480)) for f in fs]
cols=min(len(ims),6)
rows=(len(ims)+cols-1)//cols
W=Image.new('RGB',(cols*274,rows*484),'#222')
for k,im in enumerate(ims): W.paste(im,((k%cols)*274,(k//cols)*484))
W.save('prev/sheet_%s.png'%pre)
print(fs)
