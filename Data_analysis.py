import pytesseract



pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

from PIL import Image
import threading

text =""
text2=""
def f():
    text = pytesseract.image_to_string(Image.open('images/b.png'))
    print "text: ",text
def f2():
    text2 = pytesseract.image_to_string(Image.open('images/c.png'))
    print "text2: ", text2

t1 = threading.Thread(target=f)
t2 = threading.Thread(target=f2)

t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread' 2 is completely executed
t2.join()

array1 = []
array2=[]

print("Done!")