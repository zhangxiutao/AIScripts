from __future__ import division
import cv2
import numpy as np
from PIL import Image, ImageDraw
import random
import math
def cv22PIL(img_cv2):

    img_cv2 = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_cv2)

    return img_pil

def PIL2cv2(img_pil):

    img_cv2 = np.array(img_pil.convert('RGB'))[:, :, ::-1].copy() 

    return img_cv2

def random_window(img_origin_pil, img_cv2, window_size):

    count = 0
    nonzeros = cv2.findNonZero(img_cv2)
    if nonzeros is None:
        return None
    windows_pil = []
    found = False
    for count in range(10):
        anchor_point = random.choice(nonzeros)[0]
        mid_p1 = (anchor_point[0]-math.floor(window_size[0]/2),anchor_point[1]-math.floor(window_size[1]/2))
        mid_p2 = (anchor_point[0]+math.ceil(window_size[0]/2),anchor_point[1]+math.ceil(window_size[1]/2))
        if mid_p1[0] > 0 and mid_p1[1] > 0 and mid_p2[0] < img_origin_pil.size[0] and mid_p2[1] < img_origin_pil.size[1]:
            found = True    
            break
    if not found:
        return None
    if mid_p1[1]+int(window_size[1]/2) < img_origin_pil.size[1]:
        lower_window_pil = img_origin_pil.crop((mid_p1[0],mid_p1[1]+int(window_size[1]/2),mid_p2[0],mid_p2[1]+int(window_size[1]/2)))
        lower_window_pil.show()
    else:
        lower_window_pil = None

    mid_window_pil = img_origin_pil.crop((mid_p1[0],mid_p1[1],mid_p2[0],mid_p2[1]))
    mid_window_pil.show()
    if mid_p1[1]-int(window_size[1]/2) > 0:
        upper_window_pil = img_origin_pil.crop((mid_p1[0],mid_p1[1]-int(window_size[1]/2),mid_p2[0],mid_p2[1]-int(window_size[1]/2)))
        upper_window_pil.show()
    else:
        upper_window_pil = None

    windows_pil.append(lower_window_pil)
    windows_pil.append(mid_window_pil)
    windows_pil.append(upper_window_pil)

    return (mid_p1[0],mid_p1[1],windows_pil)

def red_mask(img_cv2):
    
    img_hsv = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2HSV)
    #red mask0
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    mask0 = cv2.inRange(img_hsv,lower_red,upper_red)
    #red mask1
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    mask1 = cv2.inRange(img_hsv,lower_red,upper_red)

    mask_red = mask0 + mask1
    res_red = cv2.bitwise_and(img_cv2, img_cv2, mask=mask_red)

    #erosion
    # kernel = np.ones((5,5),np.uint8)
    # res_red = cv2.erode(res_red,kernel)
    h,s,red_gray=cv2.split(res_red)

    return red_gray

if __name__ == "__main__":

    img_origin = cv2.imread("../dataSet/playground/leitbakes.png")
    print(img_origin.shape)
    img_gray = red_mask(img_origin)
    ret,thresh=cv2.threshold(img_gray,0,255,0)
    lines = cv2.HoughLines(thresh, 10, np.pi / 180, 116)
    random_window(cv22PIL(img_origin),img_gray,(25,75))
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
    cv2.line(img_origin, (x1, y1), (x2, y2), (0, 0, 255))   
    #nonzero = np.squeeze(cv2.findNonZero(thresh))
    cv2.imshow("",img_gray)
    cv2.imshow("origin",img_origin)
    cv2.waitKey(0)