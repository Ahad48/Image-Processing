import numpy as np
import os
import cv2 as cv

DIR = "Image-Processing/Resources/Faces/val"

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Mindy Kaling', 'Madonna']

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

features = np.load('Image-Processing/src/features.npy',allow_pickle= True)
labels = np.load('Image-Processing/src/labels.npy', allow_pickle= True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Image-Processing/src/face_trained.yml')

img = cv.imread(os.path.join(DIR,'ben_afflek/2.jpg'))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow('person',gray)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0),1)
    cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),1)

cv.imshow('person',img)


cv.waitKey(0)
