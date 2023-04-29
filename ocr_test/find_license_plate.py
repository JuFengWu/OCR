import cv2
import pytesseract
from PIL import Image
img = cv2.imread('car.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img, (21,21), 0)
img_canny = cv2.Canny(img, 30, 150)

contours, hierarchy = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

for item in contours:
    rect = cv2.boundingRect(item)
    x = rect[0]
    y = rect[1]
    weight = rect[2]
    height = rect[3]
    if weight / height > 4:
        cv2.rectangle(img, (x, y), (x+weight, y+height), (0, 0, 255), 3)
        crop_img = gray[y:y+height,x:x+weight]
        
        cv2.imshow("crop img",crop_img)
        cv2.waitKey(0)
        
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        img2 = Image.fromarray(cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB))
        print(pytesseract.image_to_string(img2, lang="eng"))