import cv2, numpy as np
from PIL import Image
D="assets/v/mani"
src=cv2.imread(f"{D}/R.png"); h,w=src.shape[:2]
mask=np.zeros((h,w),np.uint8); rect=(105,0,260,545)
bg=np.zeros((1,65),np.float64); fg=np.zeros((1,65),np.float64)
cv2.grabCut(src,mask,rect,bg,fg,6,cv2.GC_INIT_WITH_RECT)
m=np.where((mask==1)|(mask==3),255,0).astype(np.uint8)
m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((5,5),np.uint8)); m=cv2.GaussianBlur(m,(5,5),0)
rgba=cv2.cvtColor(src,cv2.COLOR_BGR2RGBA); rgba[...,3]=m
Image.fromarray(cv2.cvtColor(rgba,cv2.COLOR_RGBA2BGRA)[...,[2,1,0,3]]).save(f"{D}/bunny_cut.png")
