import pytesseract
from PIL import Image
import cv2
def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread('num4.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    img2 = Image.fromarray(cv2.cvtColor(binary, cv2.COLOR_BGR2RGB))
    img2.show()
    print(pytesseract.image_to_string(img2, lang="eng"))


if __name__ == "__main__":
    main()