import cv2 as cv
import numpy as np
import os

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,'cats.jpg'))
cv.imshow('cats',img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
# cv.imshow('blank',blank)

# mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2),100,255,-1)
# cv.imshow('mask',mask)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

mask = cv.bitwise_and(rectangle,circle)

masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Masked Image',masked)

cv.waitKey(0)