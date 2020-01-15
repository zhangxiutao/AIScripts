import cv2
import random
import os
import shutil

srcDir="combined"
dstDir="pos"

imgs = []
for x in os.listdir(srcDir):
    imgs.append(x)
selected_imgs = random.sample(imgs,5000)
for fileName in os.listdir(srcDir):
    if fileName in selected_imgs:
        shutil.copy(os.path.join(".",srcDir,fileName),os.path.join(".",dstDir))
