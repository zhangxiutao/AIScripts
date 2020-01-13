import cv2
import numpy as np
img = np.zeros((100,100,3),np.uint8)
resized_img = cv2.resize(img,(300,300))
circleImage = cv2.circle(resized_img, (150,0), 150, (255,255,255), thickness=1)
cv2.imshow("",circleImage)
cv2.waitKey(0)
