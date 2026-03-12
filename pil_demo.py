# Pillow library allows us to work with and manipulate images in Python, like displaying, resizing, rotating, modifying colors like converting to black and white, blur images, and saving back to machine
from PIL import Image, ImageFilter
import os

size_300 = (300, 300) # width and height we want. 

for f in os.listdir("."):
    if f.endswith(".jpg"):
        print(f)
        i = Image.open(f)
        filename, fileext = os.path.splitext(f) # split extension
        print(filename, fileext)
        i.save(f"pngs/{filename}.png")
        
        i.thumbnail(size_300) # Preserves aspect ratio and uses maximum of the 2
        # FIXME: For some reason, puppy1.jpg is 183x275. Why?
        i.save(f"300/{filename}_300.jpg")
        
image1 = Image.open("puppy1.jpg") # Create Image object
image1.rotate(90).save("puppy1_rotated.jpg")
image1.convert(mode="L").save("puppy1_greyscale.jpg")
# image1.show()
image1.filter(ImageFilter.GaussianBlur()).save("puppy1_gaussianblur.jpg")
image1.filter(ImageFilter.GaussianBlur(15)).save("puppy1_gaussianblur15.jpg")
image1.save("puppy1.png")
