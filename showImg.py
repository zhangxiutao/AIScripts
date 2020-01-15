import cv2
from skimage.transform import pyramid_expand
img = cv2.imread("wood-texture.jpg")
expanded = pyramid_expand(img,upscale=2)
cv2.imshow("",expanded)
cv2.waitKey(0)
