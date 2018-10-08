import numpy as np
import pytesseract
import cv2
from PIL import Image
import threading
import re

Pri = []
Duo = []
Tri = []
Tet = []
Pen = []

failedPri = []
failedDuo = []
failedTri = []
failedTet = []
failedPen = []


regex = '(got|failed at)\s?.+?(PRI|DUO|TRI|TET|PEN):\s{1}(s?.+?)\s?(?:ll|Enhancement Failed|Enhancement Success)\s?.+?(\d+:\d+)'



pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'


text =""
text2=""
def f():

    text = pytesseract.image_to_string(Image.open('images/ff.png'))
    print text
def f2():
    text2 = pytesseract.image_to_string(Image.open('images/ff.png'))
    print  text2

#t1 = threading.Thread(target=f)
t2 = threading.Thread(target=f2)

#t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
#t1.join()
# wait until thread' 2 is completely executed
t2.join()

array1 = []
array2=[]

def parse(text):
    print"hi"




print("Done!")

