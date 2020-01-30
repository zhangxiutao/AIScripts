from __future__ import division
import numpy as np
import cv2
def red_mask(img_cv2):

    img_hsv = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2HSV)
    #red mask0
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(img_hsv,lower_red,upper_red)
    #red mask1
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv,lower_red,upper_red)

    mask_red = mask0 + mask1
    res_red = cv2.bitwise_and(img_cv2, img_cv2, mask=mask_red)

    #erosion
    #kernel = np.ones((5,5),np.uint8)
    #res_red = cv2.erode(res_red,kernel)
    h,s,red_gray=cv2.split(res_red)

    return red_gray
img_origin = cv2.imread("../dataSet/test/back.png")
img = red_mask(img_origin)
ret,thresh=cv2.threshold(img,127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
c = np.array(max(contours, key = cv2.contourArea))
img_origin = cv2.drawContours(img_origin, [c], -1, (0,255,0), 3)
print(img.shape[0])
print(img.shape[1])
area = img.shape[0]*img.shape[1]
nonZeros = cv2.findNonZero(img)
numNonZero = cv2.countNonZero(img)
print("red ratio",numNonZero/area)
print("area",area)
print("nonZero",numNonZero)
print(nonZeros)
print(np.mean(img))
cv2.imshow("gray",img)
cv2.imshow("contours",img_origin)
cv2.waitKey(0)
