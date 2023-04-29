import pytesseract
from PIL import Image
import cv2

lowValue = 0
upValue = 255

def adjust_up(up):
    global lowValue, upValue, gray
    upValue = up
    ret, binary = cv2.threshold(gray, lowValue, upValue, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow('binary', binary)
def adjust_down(down):
    global lowValue, upValue, gray
    lowValue = down
    ret, binary = cv2.threshold(gray, lowValue, upValue, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow('binary', binary)  
def main():
    global gray
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread('num2.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    cv2.imshow("binary",binary)
    cv2.createTrackbar('binary adjust up ', 'binary', 0, 255, adjust_up)
    cv2.createTrackbar('binary adjust down ', 'binary', 0, 255, adjust_down)
    cv2.waitKey(0)
    img2 = Image.fromarray(cv2.cvtColor(binary, cv2.COLOR_BGR2RGB))
    print(pytesseract.image_to_string(img2, lang="eng"))


if __name__ == "__main__":
    main()