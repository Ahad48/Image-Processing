import cv2 as cv
import numpy as np
import os

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,'group 1.jpg'))
cv.imshow('Person',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1)

print(str(len(faces_rect))+": number of faces found")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces', img)
cv.waitKey(0)