import cv2 as cv
import numpy as np
import os

path = "Image-Processing/Resources/Photos/"

img = cv.imread(os.path.join(path,'park.jpg'))
cv.imshow('park',img)

# Transalaion
def translate(img, x, y):
    # -x left +x right
    # -y up +y down
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# translated = translate(img,-100,100)
# cv.imshow('Transalated',translated)

# Rotation
def rotate(img,angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

# rotation = rotate(img, -45)
# cv.imshow('rotation',rotation)

# rotated_rotated = rotate(rotation, 45)
# cv.imshow('rotated rotated', rotated_rotated)

# Resize
# resized = cv.resize(img, (img.shape[1]*2,img.shape[0]*2), interpolation= cv.INTER_CUBIC)
# cv.imshow('resized',resized)

# Flipping
# flip = cv.flip(img, 1)
# cv.imshow('flip',flip)
#  0 --> vertically
#  1 --> horizontal
# -1 --> both

# Cropping
cropped = img[100:300,100:300]
cv.imshow('cropped',cropped)

cv.waitKey(0)