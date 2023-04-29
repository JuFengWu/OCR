import cv2
import numpy as np
carplate_haar_cascade = cv2.CascadeClassifier("cascade.xml")
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
carplate_img = cv2.imread("car.jpg")
carplate_img_rgb = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
cv2.imshow("car_image",carplate_img_rgb)
cv2.waitKey(0)
def carplate_detect(image):
    carplate_overlay = image.copy()
    
    carplate_rects = carplate_haar_cascade.detectMultiScale(carplate_overlay, scaleFactor = 1.1, minNeighbors = 3)
    
    for x, y, w, h in carplate_rects:
        cv2.rectangle(carplate_overlay, (x, y), (x+w, y+h), (255, 0 ,0 ), 5)
       
        return carplate_overlay
detected_carplate_img = carplate_detect(carplate_img_rgb)
cv2.imshow("detected_carplate_img", detected_carplate_img)
cv2.waitKey(0)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img2 = Image.fromarray(cv2.cvtColor(detected_carplate_img, cv2.COLOR_BGR2RGB))
print(pytesseract.image_to_string(img2, lang="eng"))