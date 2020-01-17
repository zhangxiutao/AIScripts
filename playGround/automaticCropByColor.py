import numpy as np
import cv2
from random import randrange

obj_filename = '../dataSet/cropResizedLeitbake_without_background/cropResizedLeitbake1.jpg'

obj_img = cv2.imread(obj_filename)

lower_green = np.array([0,230,0]) 
upper_green = np.array([20,255,20]) 
mask_green = ~cv2.inRange(obj_img,lower_green,upper_green)
res = cv2.bitwise_and(obj_img, obj_img, mask=mask_green)

for i in range(obj_img.shape[0]):
    for j in range(obj_img.shape[1]):
            all_zero = not np.any(res[i][j]) #if all zero
            if all_zero:
                res[i][j] = (randrange(256),randrange(256),randrange(256))

cv2.imwrite(obj_filename, res)


