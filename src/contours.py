import cv2 as cv
import os
import numpy as np

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,'cats.jpg'))
cv.imshow('cats',img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray cats',gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny',canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh',thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank,contours, -1, (0,0,255),1)
cv.imshow('countours_drawn',blank)

print(str(len(contours))+" number of contours")

cv.waitKey(0)