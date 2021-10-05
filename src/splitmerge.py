import cv2 as cv
import os
import numpy as np

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,'park.jpg'))
cv.imshow('park',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged img',merged)

cv.waitKey(0)