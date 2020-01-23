import cv2
import os

srcDir = "dataSet/cropResizedLeitbake"
dstDir = "dataSet/cropResizedLeitbake_augumented"

for x in os.listdir(os.path.join(".",srcDir)):

    img = cv2.imread(os.path.join(".",srcDir,x))
    img_flip = cv2.flip(img, 1)
    cv2.imwrite(os.path.join(".",dstDir,os.path.splitext(os.path.basename(x))[0]+"_flip.jpg"), img_flip)
