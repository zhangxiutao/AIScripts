import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import shutil
copyFile = False
def checkIfWanted(img,fileName):

    #桔黄色也会被提取
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 区间1
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(img_hsv,lower_red,upper_red)
    # 区间2
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv,lower_red,upper_red)
    # 拼接两个区间
    mask = mask0 + mask1
    res = cv2.bitwise_and(img, img, mask= mask)
     
    #averaging filter
    # averagingKernel = np.ones((5,5),np.float32)/100
    # averaging = cv2.filter2D(res,-1,averagingKernel)

    #erosion
    erosionKernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(res,erosionKernel)
    bw_image = cv2.cvtColor(cv2.cvtColor(erosion, cv2.COLOR_HSV2BGR), cv2.COLOR_RGB2GRAY)

    if fileName == "17.Balise_J13.JPG":   
        print(cv2.countNonZero(bw_image))
        cv2.imshow("mask",mask)
        cv2.imshow("res",res)
        cv2.imshow("bw_img",bw_image)
        cv2.waitKey(0)

    if cv2.countNonZero(bw_image) < 10:
        return False,bw_image
    else:
        return True,None

srcDir = "Leitbake"
dstDir = "wantedLeitbake"

fig = plt.figure(figsize=(8, 8))

idx = 0
wantedSamples = []



for fileName in os.listdir(os.path.join(".",srcDir)):
    img=cv2.imread(os.path.join(srcDir,fileName))
    wanted,bw_img = checkIfWanted(img,fileName)
    if copyFile:
        os.mkdir(dstDir)
        if wanted:
            print(fileName)
            wantedSamples.append(fileName) 
            shutil.copy(os.path.join(".",srcDir,fileName),os.path.join(".",dstDir))     

    #     fig.add_subplot(2,25,idx+1)
    #     plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # idx = idx + 1
    # if idx == 50:
    #     plt.show()
    #     break
