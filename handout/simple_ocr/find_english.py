import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open("english_test.jpg")
result = pytesseract.image_to_string(img, lang="eng")
print(result)

