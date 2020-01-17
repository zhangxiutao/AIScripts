import cv2
import random
import os
import shutil
import argparse as ap

srcDir = "../dataSet/cropResizedLeitbake_without_background"
dstDir = "../dataSet/pos"

if __name__ == "__main__":
    # Parse the command line arguments

    if os.path.exists(dstDir):
        shutil.rmtree(dstDir)
        os.mkdir(dstDir)
    else:
        os.mkdir(dstDir)
    
    for fileName in os.listdir(srcDir):
        count = 1
        while True:
            shutil.copy(os.path.join(srcDir,fileName),os.path.join(dstDir,os.path.splitext(os.path.basename(fileName))[0]+str(count)+".jpg"))
            count = count+1
            if count == 1250:
                break

