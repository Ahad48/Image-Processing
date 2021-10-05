import cv2 as cv
import os

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,"cat.jpg"))

cv.imshow('cat',img)

# Convert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)


# # Blur
# blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# Edge cascade
# canny = cv.Canny(blur, 125,175)
# cv.imshow('canny', canny)

# # Dialating the image
# dilated = cv.dilate(canny, (3,3), iterations=3)
# cv.imshow('dialated',dilated)

# # Erosion
# erode = cv.erode(dilated, (3,3), iterations=3)
# cv.imshow('erode',erode)

# Resize
# resized = cv.resize(img, (500,500))
# cv.imshow('resize',resized)

# Cropping
cropped = img[50:200,200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)