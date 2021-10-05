import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,'cats.jpg'))
cv.imshow('cats',img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# circle_mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100,255,-1)
# masked = cv.bitwise_and(gray, gray, mask = circle)

# cv.imshow('masked img', masked)

# # # Gray scale histogram
# gray_hist = cv.calcHist([mask],[0], circle_mask, [256], [0,256])

# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist, color = 'gray')
# plt.xlim([0,256])
# plt.show()

# Color Histogram
colors = ('b', 'g', 'r')

plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

circle_mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100,255,-1)
masked = cv.bitwise_and(img, img, mask = circle_mask)
cv.imshow('masked img', masked)

for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i], circle_mask, [256],[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)