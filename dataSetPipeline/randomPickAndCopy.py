import cv2
import random
import os
import shutil
import argparse as ap

if __name__ == "__main__":
    # Parse the command line arguments
    parser = ap.ArgumentParser()
    parser.add_argument('-PS', "--posSrcDir", help="Path to the srcDir", required=True)
    parser.add_argument('-PD','--posDstDir', help="Path to the dstDir", required=True)
    parser.add_argument('-NS', "--negSrcDir", help="Path to the srcDir", required=True)
    parser.add_argument('-ND','--negDstDir', help="Path to the dstDir", required=True)
    args = vars(parser.parse_args())

    posSrcDir=args["posSrcDir"]
    posDstDir=args["posDstDir"]

    if os.path.exists(posDstDir):
        shutil.rmtree(posDstDir)
        os.mkdir(posDstDir)
    else:
        os.mkdir(posDstDir)

    pos_files = []

    for x in os.listdir(posSrcDir):
        pos_files.append(x)
    pos_selected_files = random.sample(pos_files,5000)

    for fileName in os.listdir(posSrcDir):
        if fileName in pos_selected_files:
            shutil.copy(os.path.join(posSrcDir,fileName),posDstDir)

    negSrcDir=args["negSrcDir"]
    negDstDir=args["negDstDir"]

    if os.path.exists(negDstDir):
        shutil.rmtree(negDstDir)
        os.mkdir(negDstDir)
    else:
        os.mkdir(negDstDir)

    neg_files = []

    for x in os.listdir(negSrcDir):
        neg_files.append(x)
    neg_selected_files = random.sample(neg_files,5000)

    for fileName in os.listdir(negSrcDir):

        if fileName in neg_selected_files:

            shutil.copy(os.path.join(negSrcDir,fileName),negDstDir)


