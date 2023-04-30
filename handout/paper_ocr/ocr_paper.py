import pytesseract
from PIL import Image

def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open("paper.jpg")
    img.show()
    result = pytesseract.image_to_string(img, lang="eng")
    print(result)
    #print(type(result))
    everySingleWord = result.split()
    print(everySingleWord)
    
    
if __name__ == "__main__":
    main()