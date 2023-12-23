import os
from PIL import Image

image_name = input("Enter image name: ")
if os.path.isfile(image_name) == True:
    im = Image.open(image_name)
    im.show()
elif ("." in image_name) == False:
    print("Please include a valid file type")
else:
    print("no")