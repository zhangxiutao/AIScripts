from __future__ import division
import cv2
import imutils
import random
import numpy as np
import math
import torchvision.ops as ops
import torch

def get_contours_center(cnts):

    centers = []
    for c in cnts:
        # compute the center of the contour
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # draw the contour and center of the shape on the image
            # cv2.drawContours(backtorgb, [c], -1, (0, 255, 0), 2)
            # cv2.circle(backtorgb, (cX, cY), 7, (0, 0, 255), -1)
            centers.append((cX,cY))

    return centers

img = cv2.imread("../dataSet/playground/masked.png", cv2.IMREAD_GRAYSCALE)
backtorgb = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
ret,thresh=cv2.threshold(img,0,255,0)


def windows_search_contourbased(img_binary_cv2, window_size):

    cnts = cv2.findContours(img_binary_cv2.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    detections = []
    scores = []
    contour_centers = get_contours_center(cnts)
    count = 0
    for (cX,cY) in contour_centers:
        img_window_mask = np.zeros_like(img_binary_cv2)
        count = count + 1
        p1 = (int(cX-math.floor(window_size[0]/2)),int(cY-math.floor(window_size[1]/2)))
        p2 = (int(cX+math.ceil(window_size[0]/2)),int(cY+math.ceil(window_size[1]/2)))
        print(p1)
        print(p2)
        #if p1[0] > 0 and p1[1] > 0 and p2[0] < img.shape[1] and p2[1] < img.shape[0]:
        cv2.rectangle(img_window_mask, p1, p2, 255, thickness=cv2.FILLED)
        img_window_masked = cv2.bitwise_and(img_binary_cv2, img_binary_cv2, mask=img_window_mask)
        cnts_window_masked = cv2.findContours(img_window_masked.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts_window_masked = imutils.grab_contours(cnts_window_masked)
        contour_centers_window_masked = get_contours_center(cnts_window_masked)
        if len(contour_centers_window_masked) >= 2:
            print("found!")
            #cv2.rectangle(img, (cX-18,cY-48), (cX+18,cY+48), 255, thickness=1)
            detections.append((p1[0], p1[1], p2[0], p2[1]))
            y_mean_centers = np.mean(contour_centers_window_masked,axis=0)[1].astype(np.int32)
            #cv2.circle(backtorgb, (cX, y_mean_centers), 3, (0, 0, 255), -1)
            score = 1/((y_mean_centers-cY)**2)
            scores.append(score)

    detections = torch.tensor(detections).double()
    scores = torch.tensor(scores).double()
    detections_nms_idx = ops.nms(detections,scores,0.2)
    detections_nms = [(detections[i][0],0,detections[i][2],window_size[1]) for i in detections_nms_idx]

    for (x1,y1,x2,y2) in detections_nms:
        cv2.rectangle(img_binary_cv2, (x1,y1), (x2,y2), 255, thickness=1)

    cv2.imshow("gray",img_binary_cv2)
    cv2.waitKey(0)
    return detections_nms


windows_search_contourbased(thresh,[35,95])
