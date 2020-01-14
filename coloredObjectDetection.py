import cv2
import os.path
import numpy as np
img = cv2.imread(os.path.join(".","coloredImg.jpg"))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([170,70,50])
upper_red = np.array([180,255,255])
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img, img, mask= mask)
#averaging filter
averagingKernel = np.ones((5,5),np.float32)/100
averaging = cv2.filter2D(res,-1,averagingKernel)
#gaussian filter
gaussianBlur = cv2.GaussianBlur(res,(5,5),0)
#erosion
erosionKernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(res,erosionKernel)
cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('averaging',averaging)
cv2.imshow('gaussian',gaussianBlur)
cv2.imshow('erosion',erosion)
cv2.waitKey(0)
