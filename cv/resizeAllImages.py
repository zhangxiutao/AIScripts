import os
import cv2 
import os.path
srcDir = "..\\..\\data\\dataset\\cropped_autobahn"
dstDir = "..\\..\\data\\dataset\\cropped_autobahn64_128"
for filename in os.listdir(os.path.join(".",srcDir)):
    print (filename)
    image=cv2.imread(os.path.join(srcDir,filename))
    res=cv2.resize(image,(64,128),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(dstDir,filename), res)

