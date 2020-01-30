import cv2
img = cv2.imread("./dataSet/baustelle_dataset/baustelle/baustelle_10.jpg")
img = img[int(img.shape[0]/2):int(img.shape[0]),:]
cv2.imshow("",img)
cv2.waitKey(0)
