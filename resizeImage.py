import PIL
from PIL import Image
import os.path
img = Image.open(os.path.join(".","National_Highway.jpg"))
resizedImg = img.resize((512,256), PIL.Image.ANTIALIAS)
resizedImg.save("resized_autobahn.jpeg")

