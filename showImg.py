import cv2
from skimage.transform import pyramid_expand
img = cv2.imread("dataSet/baustelle_dataset/baustelle/baustelle_3.jpg")
#expanded = pyramid_expand(img,upscale=2)
img = img[img.shape[0]/2:,:]
cv2.imshow("",img)
cv2.waitKey(0)
