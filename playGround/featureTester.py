import numpy as np
import cv2
img1 = cv2.imread("../dataSet/detectedWindows/8dac776ca643459ebd59aba27c8300dd.png")
img2 = cv2.imread("../dataSet/detectedWindows/4e49aeeb2a93482183014de1ae0f0b9c.png")
arr_std_p = np.std(img1,ddof=1)
arr_std_n = np.std(img2,ddof=1)
print(arr_std_p)
print(arr_std_n)
