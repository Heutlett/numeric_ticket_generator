# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def generate_imgs(img,n):
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    
    # Custom font style and font size
    myFont = ImageFont.truetype("OpenSans-Light.ttf",65)

    # Add Text to an image
    I1.text((180, 900), n, font=myFont, fill=(0, 0, 0))
    
    # Save the edited image
    ruta = "Boletas/" +n + ".png"
    img.save(ruta)

for i in range(0,100):

    # Open an Image
    img = Image.open('img.jpg')

    if (i<10):
        num = "00" + str(i)
    elif (i<100):
        num = "0" + str(i)
    else:
        num = str(i)
    generate_imgs(img,num)
 
