import cv2
import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Tesseract-OCR\tesseract'

image = cv2.imread("C:\\image1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename), lang = 'eng')
os.remove(filename)

print(text)
