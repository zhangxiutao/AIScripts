#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
 
# Read images : src image will be cloned into dst
im = cv2.imread("./resized-texture.jpg")
obj= cv2.imread("./cropResizedLeitbake.jpg")
 
# Create an all white mask
mask = 255 * np.ones(obj.shape, obj.dtype)
 
# The location of the center of the src in the dst
width, height, channels = im.shape
center = (round(height/2), round(width/2))
 
print(center)
# Seamlessly clone src into dst and put the results in output
normal_clone = cv2.seamlessClone(obj, im, mask, center, cv2.NORMAL_CLONE)
mixed_clone = cv2.seamlessClone(obj, im, mask, center, cv2.MIXED_CLONE)
 
# Write results
cv2.imwrite("./opencv-normal-clone-example.jpg", normal_clone)
cv2.imwrite("./opencv-mixed-clone-example.jpg", mixed_clone)
