#!/usr/bin/env python3

import cv2 as cv

# reading images
img = cv.imread('photos/dog1.jpeg') # since the image is in the same folder, don't need absolute path
cv.imshow('dog', img) # to display an image


# reading videos
# argument will be a file path or int
# if file path, put the file path
# if int like 0, it will use the webcam 
capture = cv.VideoCapture('videos/dog_video.mp4')

while True:
    # capture.read reads the video frame by frame
    # it returns the frame and a boolean whether the frame was read successfully or not
    isTrue ,frame = capture.read()
    cv.imshow('video', frame) # capture each frame using imshow()

    # if letter key is pressed, break out of the loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

