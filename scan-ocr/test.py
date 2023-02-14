# https://digi.bib.uni-mannheim.de/tesseract/
# 配置环境变量如  C:\Program Files\Tesseract-OCR
# tesseract -v进行测试
# tesseract XXX.png 得到结果

# pip install Pillow
# pip install pytesseract

# 修改：C:\Users\haitong\.conda\envs\opencv3_\Lib\site-packages\pytesseract\pytesseract.py
# tesseract_cmd 修改为绝对路径即可
# tesseract_cmd = 'C://Program Files//Tesseract-OCR//tesseract.exe'
from PIL import Image
import pytesseract
import cv2
import os

preprocess = 'blur' #thresh

image = cv2.imread('scan.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if preprocess == "thresh":
    gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

if preprocess == "blur":
    gray = cv2.medianBlur(gray, 3)
    
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
    
text = pytesseract.image_to_string(Image.open(filename))
print(text)
os.remove(filename)

cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)                                   
