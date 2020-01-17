import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import shutil
copyFile = False
def checkIfWanted(img):

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #red mask0
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(img_hsv,lower_red,upper_red)
    #red mask1
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv,lower_red,upper_red)

    mask_red = mask0 + mask1
    res_red = cv2.bitwise_and(img, img, mask=mask_red)

    #erosion
    erosionKernel = np.ones((5,5),np.uint8)
    erosion_red = cv2.erode(res_red,erosionKernel)
    bw_image_red = cv2.cvtColor(cv2.cvtColor(erosion_red, cv2.COLOR_HSV2BGR), cv2.COLOR_RGB2GRAY)

    #black mask0
    lower_black = np.array([0,0,0]) 
    upper_black = np.array([180,255,46]) 
    mask_black = cv2.inRange(img_hsv,lower_black,upper_black)
    res_black = cv2.bitwise_and(img, img, mask=mask_black)
    res_black = cv2.cvtColor(res_black, cv2.COLOR_BGR2GRAY)
    #erosionimg
    #erosionKernel = np.ones((5,5),np.uint8)
    #erosion_black = cv2.erode(res_black,erosionKernel)
    #bw_image_black = cv2.cvtColor(cv2.cvtColor(erosion_black, cv2.COLOR_HSV2BGR), cv2.COLOR_RGB2GRAY)
    
    print(cv2.countNonZero(res_black))
    # cv2.imshow("",bw_image_red)
    # cv2.waitKey(0)
    
    if cv2.countNonZero(bw_image_red) < 100 or cv2.countNonZero(res_black) > 5:
        print("False")
        return False
    else:
        print("True")
        return True

img = cv2.imread("../dataSet/playground/baustelle_1.jpg")
checkIfWanted(img)
