import cv2
import random
import os

srcDir="autobahn"
dstDir="background"

imgs = []
for x in os.listdir(srcDir):
    imgs.append(x)
selected_imgs = random.sample(imgs,400)

h=95
w=35

for fileName in os.listdir(srcDir):
    if fileName in selected_imgs:
        print(fileName)
        img = cv2.imread(os.path.join(".",srcDir,fileName))
        count=1
        while 1:
            if type(img) is not None:
                y = random.randint(0, img.shape[0]-h)
                x = random.randint(0, img.shape[1]-w)
                cropImg = img[(y):(y + h), (x):(x + w)]
                cv2.imwrite(os.path.join(".",dstDir,fileName+str(count)+".jpg"), cropImg)
                count+=1
                if count==12:
                    break
            else:
                break
