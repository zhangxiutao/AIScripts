import PIL
from PIL import Image
import os.path
img = Image.open(os.path.join(".","wood-texture.jpg"))
resizedImg = img.resize((35,95), PIL.Image.ANTIALIAS)
resizedImg.save("resized-texture.jpg")

