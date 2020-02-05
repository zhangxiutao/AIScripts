from __future__ import division
import cv2
import numpy as np
def red_mask(img_cv2):

    img_hsv = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2HSV)
    #red mask0
    lower_red = np.array([0, 100, 0]) #0, 43, 46
    upper_red = np.array([0, 255, 255]) #10, 255, 255
    mask0 = cv2.inRange(img_hsv,lower_red,upper_red)
    #red mask1
    lower_red = np.array([156, 43, 0]) #156, 43, 46
    upper_red = np.array([180, 255, 200]) #180, 255, 255
    mask1 = cv2.inRange(img_hsv,lower_red,upper_red)

    mask_red = mask0+mask1
    res_red = cv2.bitwise_and(img_cv2, img_cv2, mask=mask_red)

    #erosion
    # kernel = np.ones((1,1),np.uint8)
    # res_red = cv2.erode(res_red,kernel)
    h,s,red_gray=cv2.split(res_red)

    return red_gray
img_origin = cv2.imread("../dataSet/playground/tuning.png")
img = red_mask(img_origin)
contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
ret,thresh=cv2.threshold(img,0,255,0)
for contour in contours:
    if cv2.contourArea(contour)>30 or cv2.contourArea(contour)<3:
        thresh = cv2.drawContours(thresh, [contour], -1, 0, thickness=cv2.FILLED)
cv2.imshow("contourfiltered",thresh)
#lines = cv2.HoughLines(thresh, 10, np.pi / 180, 116)
lines = cv2.HoughLinesP(thresh, 1, np.pi / 180, threshold = 1,minLineLength = 10000,maxLineGap = 500)
lines = np.squeeze(lines)
#nonzero = np.squeeze(cv2.findNonZero(thresh))
# print(lines)
# for line in lines:
#     rho, theta = line[0]
#     print(theta*180/np.pi)
#     if theta*180/np.pi < 100 and theta*180/np.pi > 80:
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         x1 = int(x0 + 1000 * (-b))
#         y1 = int(y0 + 1000 * (a))
#         x2 = int(x0 - 1000 * (-b))
#         y2 = int(y0 - 1000 * (a))

#         cv2.line(img_origin, (x1, y1), (x2, y2), (0, 0, 255))


if lines[()] is not None:
    print(lines)
    print(type(lines))
    for x1,y1,x2,y2 in lines:

        cv2.line(img_origin,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("",img_origin)
cv2.waitKey(0)
