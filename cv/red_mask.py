import glob
import cv2
import os
import numpy as np
import shapeDetection

sample_path = "../dataSet/baustelle_dataset/baustelle"
def red_mask(img):

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
    shapeDetection.shape_detection(res_red)
    gray = cv2.cvtColor(res_red,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    #erosion
    erosionKernel = np.ones((5,5),np.uint8)
    erosion_red = cv2.erode(res_red,erosionKernel)
    bw_image_red = cv2.cvtColor(cv2.cvtColor(erosion_red, cv2.COLOR_HSV2BGR), cv2.COLOR_RGB2GRAY)

    #white mask 
    lower_white = np.array([0,0,0], dtype=np.uint8)
    upper_white = np.array([40,40,255], dtype=np.uint8)
    mask_white = cv2.inRange(img_hsv, lower_white, upper_white)

    res_white = cv2.bitwise_and(img, img, mask=mask_white)
    # cv2.imshow("res_red",res_red)
    # cv2.waitKey(0)

    #black mask0
    lower_black = np.array([0,0,0]) 
    upper_black = np.array([180,255,46]) 
    mask_black = cv2.inRange(img_hsv,lower_black,upper_black)
    res_black = cv2.bitwise_and(img, img, mask=mask_black)
    res_black = cv2.cvtColor(res_black, cv2.COLOR_BGR2GRAY)
    #erosionimgfor im_path in glob.glob(os.path.join(pos_im_path, "*")):
    
    # cv2.imshow("",bw_image_red)
    # cv2.waitKey(0)


for im_path in glob.glob(os.path.join(sample_path, "baustelle_6.jpg")):
    print(im_path)
    img = cv2.imread(im_path)
    red_mask(img)
