import pytesseract

from PIL import Image

print("By Tanishka Mishra")
img = Image.open(r"E:\prototype\Assignment7\output.png")
text = pytesseract.image_to_string(img) 

print("Extracted text from image:", text)

print("Tanishka Mishra")
