import cv2
import random
import os
import argparse as ap

srcDir="autobahn"
dstDir="cropped_autobahn"

imgs = []
for x in os.listdir(os.path.join(".",srcDir)):
    imgs.append(x)
selected_imgs = random.sample(imgs,18)

h=95
w=35

for fileName in os.listdir(os.path.join(".",srcDir)):
    if fileName in selected_imgs:
        print(fileName)
        img = cv2.imread(os.path.join(".",srcDir,fileName))
        count=1
        while 1:
            if type(img) is not None:
                y = random.randint(0, img.shape[0]-h)
                x = random.randint(0, img.shape[1]-w)
                cropImg = img[(y):(y + h), (x):(x + w)]
                cv2.imwrite(os.path.join(".",dstDir,os.path.splitext(os.path.basename(fileName))[0]+str(count)+".jpg"), cropImg)
                count+=1
                if count==20:
                    break
            else:
                break
