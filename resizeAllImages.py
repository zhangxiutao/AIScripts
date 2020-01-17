import os
import cv2 
import os.path
srcDir = "dataSet/pos"
dstDir = "dataSet/pos"
for filename in os.listdir(os.path.join(".",srcDir)):
    print (filename)
    image=cv2.imread(os.path.join(srcDir,filename))
    res=cv2.resize(image,(35,95),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(dstDir,filename), res)

