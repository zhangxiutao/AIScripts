pil2opencv
pil_image = PIL.Image.open('Image.jpg').convert('RGB') 
open_cv_image = numpy.array(pil_image) 
# Convert RGB to BGR 
open_cv_image = open_cv_image[:, :, ::-1].copy() 



opencv2pil
cv2_im = cv2.cvtColor(cv2_im,cv2.COLOR_BGR2RGB)
pil_im = Image.fromarray(cv2_im)
