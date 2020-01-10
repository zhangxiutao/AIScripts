import PIL
from PIL import Image
import os.path
img = Image.open(os.path.join(".","test.jpeg"))
resizedImg = img.resize((1024,512), PIL.Image.ANTIALIAS)
resizedImg.save("resized_img.jpeg")

