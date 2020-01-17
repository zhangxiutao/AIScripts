#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os
import shutil
import argparse as ap

if __name__ == "__main__":
    # Parse the command line arguments
    parser = ap.ArgumentParser()
    parser.add_argument('-O', "--objDir", help="Path to the srcDir", required=True)
    parser.add_argument('-B','--backgroundDir', help="Path to the dstDir", required=True)
    parser.add_argument('-D', "--dstDir", help="Path to the srcDir", required=True)
    args = vars(parser.parse_args())

    objDir = args["objDir"]
    backgroundDir = args["backgroundDir"]
    dstDir = args["dstDir"]

    count = 1

    if os.path.exists(dstDir):
        shutil.rmtree(dstDir)
        os.mkdir(dstDir)
    else:
        os.mkdir(dstDir)

    for obj in os.listdir(objDir):
        for background in os.listdir(backgroundDir):
            # Read images : src image will be cloned into dst
            backgroundimg=cv2.imread(os.path.join(backgroundDir,background))
            objimg=cv2.imread(os.path.join(objDir,obj))

            # Create an all white mask
            mask = 255 * np.ones(objimg.shape, objimg.dtype)

            # The location of the center of the src in the dst
            width, height, channels = backgroundimg.shape
            center = (int(round(height/2)), int(round(width/2)))

            # Seamlessly clone src into dst and put the results in output
            normal_clone = cv2.seamlessClone(objimg, backgroundimg, mask, center, cv2.NORMAL_CLONE)
            #mixed_clone = cv2.seamlessClone(objimg, backgroundimg, mask, center, cv2.MIXED_CLONE)

            # Write results
            cv2.imwrite(os.path.join(dstDir,str(count)+".jpg"),normal_clone)
            #cv2.imwrite("./opencv-mixed-clone-example.jpg", mixed_clone)
            count=count+1
