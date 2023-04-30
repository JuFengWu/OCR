import pytesseract
from PIL import Image

def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open("tra_chinese.JPG")
    print(pytesseract.image_to_string(img, lang="chi_tra"))


if __name__ == "__main__":
    main()

