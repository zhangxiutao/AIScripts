(b, g, r) = cv2.split(img_cv2)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
img_cv2 = cv2.merge((bH, gH, rH))

