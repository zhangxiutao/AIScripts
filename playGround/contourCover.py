import numpy as np
import cv2
img = cv2.imread('../dataSet/cropResizedLeitbake_without_background/cropResizedLeitbake4.jpg')
img = cv2.bilateralFilter(src=img, d=0, sigmaColor=100, sigmaSpace=15)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(imgray, 127, 255, 0)
thresh = cv2.Canny(imgray, 128, 256)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
c = np.array(max(contours, key = cv2.contourArea))
#print(contours)
#c = np.squeeze(c)
#cv2.polylines(img,c,True,(255,0,0),2)

background_img = cv2.imread('../dataSet/background/1.Penguin-Highway-Frontpage-750x400.jpg1.jpg')

print(background_img.shape)
for i in range(background_img.shape[0]):
    for j in range(background_img.shape[1]):
        if cv2.pointPolygonTest(c,(j,i),False) > 0:
            background_img[i,j] = (0,0,0)

img = cv2.drawContours(background_img, [c], -1, (0,255,0), 3)
cv2.imshow("",thresh)
cv2.waitKey(0)
