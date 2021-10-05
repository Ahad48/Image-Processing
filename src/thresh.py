import cv2 as cv
import numpy as np
import os

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,'cats.jpg'))
cv.imshow('cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# simple hresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('threshold image',thresh)

# simple thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshold inv image',thresh_inv)

# adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('adaptive thresh', adaptive_thresh)
cv.waitKey(0)