import pytesseract



pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

from PIL import Image




text = pytesseract.image_to_string(Image.open('images/b.png'))
print(text)