import cv2
import random
import os
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
    
dataDir="dataSet"
srcDir="playground/traffic_jam_src"
dstDir="playground/traffic_jam_dst"

imgs = []
for x in os.listdir(os.path.join("..",dataDir,srcDir)):
    imgs.append(x)
selected_imgs = random.sample(imgs,10)

h=95
w=35

for fileName in os.listdir(os.path.join("..",dataDir,srcDir)):
    if fileName in selected_imgs:
        print(fileName)
        img = cv2.imread(os.path.join("..",dataDir,srcDir,fileName))
        count=1
        while 1:
            if type(img) is not None:
                y = random.randint(0, img.shape[0]-h)
                x = random.randint(0, img.shape[1]-w)
                cropImg = img[(y):(y + h), (x):(x + w)]
		cropImg_flip = cv2.flip(cropImg, 1)
                cv2.imwrite(os.path.join("..",dataDir,dstDir,fileName+str(count)+".jpg"), cropImg)
		cv2.imwrite(os.path.join("..",dataDir,dstDir,fileName+"flip"+str(count)+".jpg"), cropImg_flip)
                count+=1
                if count==30:
                    break
            else:
                break
