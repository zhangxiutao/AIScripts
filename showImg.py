import cv2
img = cv2.imread("img.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("",hsv)
cv2.waitKey(0)
