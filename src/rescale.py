import cv2 as cv

# img = cv.imread('Resources/Photos/cat_large.jpg')

# cv.imshow('cat',img)
# cv.waitKey(0)

def rescaleFrame(frame, scale:float = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,width)

img = cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('cat',img)
cv.imshow('cat_resize',rescaleFrame(img))
cv.waitKey(0)

# Read Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('video_resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
