import os
import cv2 
import os.path
folderName = "Leitbake"
for filename in os.listdir(os.path.join(".",folderName)):
    print (filename)
    image=cv2.imread(os.path.join(folderName,filename))
    res=cv2.resize(image,(100,40),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(folderName,filename), res)

