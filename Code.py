from PIL import image
import pytesseract
import cv2
import numpy as np
'Store all the images in the path'
src_path = "C:/Temp"

def get_string(img_path)
img=cv2.imread(img_path)

If img <>"" then
    print "Image found in the path."
    cv2.imwrite(src_path+"image.png",img)
    result=pytesseract.image_to_string(Image.open(src_path+"image.png"))
    return result
else
    print "Image not found in the path"
End if

Print get_string(src_path+ "1.png")
