import numpy as np
import cv2

def shape_detection(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#filtered = cv2.bilateralFilter(src=gray, d=0, sigmaColor=100, sigmaSpace=15)
	ret,thresh = cv2.threshold(gray,0,255,0)
	print(thresh)

	#erosion
	erosionKernel = np.ones((5,5),np.uint8)
	erosion_red = cv2.erode(thresh,erosionKernel)
	

	_,contours,_ = cv2.findContours(erosion_red,1,2)
	 
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
		print (len(approx))
		if len(approx)==5:
			print ("pentagon")
			cv2.drawContours(img,[cnt],0,(255,0,0),-1)
		elif len(approx)==3:
			print ("triangle")
			cv2.drawContours(img,[cnt],0,(0,255,0),-1)
		elif len(approx)==4:
			print ("square")
			cv2.drawContours(img,[cnt],0,(0,0,255),-1)
			# elif len(approx) == 9:
			#     print ("half-circle")
			#     cv2.drawContours(img,[cnt],0,(255,255,0),-1)
			# elif len(approx) > 15:
			#     print ("circle")
			#     cv2.drawContours(img,[cnt],0,(0,255,255),-1)
	 
	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
