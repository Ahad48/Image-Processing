import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')

# blank[:] = 0,0,255
# cv.imshow('red',blank)
# cv.waitKey(0)


# img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat',img)

# Draw rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness=cv.FILLED)
# cv.imshow('rectangle',blank)

# Draw Circle
cv.circle(blank,(250,250), 40, (0,0,255), thickness= -1)
# cv.imshow('Circle',blank)

# Draw line
cv.line(blank,(100,0),(255,255), (255,255,255), thickness=3)
# cv.imshow('line', blank)

# Put text
cv.putText(blank,"HelloWorld", (255,255),cv.FONT_HERSHEY_TRIPLEX,1.0, (255,255,255),2)
cv.imshow("text",blank)
cv.waitKey(0)