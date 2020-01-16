import cv2
import random
import os
import shutil

dataDir="dataSet"
srcDir="background"
dstDir="neg"
shutil.rmtree(os.path.join("..",dataDir,dstDir))
os.mkdir(os.path.join("..",dataDir,dstDir))
imgs = []

for x in os.listdir(os.path.join("..",dataDir,srcDir)):
    imgs.append(x)
selected_imgs = random.sample(imgs,5000)
for fileName in os.listdir(os.path.join("..",dataDir,srcDir)):
    if fileName in selected_imgs:
        shutil.copy(os.path.join("..",dataDir,srcDir,fileName),os.path.join("..",dataDir,dstDir))

dataDir="dataSet"
srcDir="combined"
dstDir="pos"
shutil.rmtree(os.path.join("..",dataDir,dstDir))
os.mkdir(os.path.join("..",dataDir,dstDir))
imgs = []
for x in os.listdir(os.path.join("..",dataDir,srcDir)):
    imgs.append(x)
selected_imgs = random.sample(imgs,5000)
for fileName in os.listdir(os.path.join("..",dataDir,srcDir)):
    if fileName in selected_imgs:
        shutil.copy(os.path.join("..",dataDir,srcDir,fileName),os.path.join("..",dataDir,dstDir))
