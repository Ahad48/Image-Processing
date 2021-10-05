import cv2 as cv
import numpy as np
import os

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,'cats.jpg'))
cv.imshow('cats',img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur',average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), sigmaX = 0)
cv.imshow('Gauss Blur',gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur',median)

# Bilateral Blur
bilaterBlur = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilaterBlur)
cv.waitKey(0)