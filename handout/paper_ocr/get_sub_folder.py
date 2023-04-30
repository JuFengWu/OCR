import  os
import cv2

# get current path
currentPath = os.path.dirname(os.path.abspath(__file__))
print(currentPath)

# get all files in foler
for path, subdirs, files in os.walk("vs_paper"):
    for name in files:
        subFoilderFilePath = os.path.join(path, name)
        print(subFoilderFilePath)