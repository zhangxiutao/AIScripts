import numpy as np
import cv2
 
img = cv2.imread('baustelle23.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filtered = cv2.bilateralFilter(src=gray, d=0, sigmaColor=100, sigmaSpace=15)
ret,thresh = cv2.threshold(filtered,127,255,0)
print(thresh)
cv2.imshow("1",thresh)
#cv2.imshow("2",dst)
contours,h = cv2.findContours(thresh,1,2)
 
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print (len(approx))
    if len(approx)==5:
        print ("pentagon")
        cv2.drawContours(img,[cnt],0,(255,0,0),-1)
    elif len(approx)==3:
        print ("triangle")
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print ("square")
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    # elif len(approx) == 9:
    #     print ("half-circle")
    #     cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    # elif len(approx) > 15:
    #     print ("circle")
    #     cv2.drawContours(img,[cnt],0,(0,255,255),-1)
 
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()