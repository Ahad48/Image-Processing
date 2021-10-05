import cv2 as cv
import os
import matplotlib.pyplot as plt

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,'park.jpg'))
cv.imshow('park',img)

# plt.imshow(img)
# plt.show()

# # BGR to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# # BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)

# # BGR to lab
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab',lab)

# BGR to RGB
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
