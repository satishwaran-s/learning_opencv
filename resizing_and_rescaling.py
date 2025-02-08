#!/usr/bin/env python3

import cv2 as cv

# resize video to 75%
# this method will work for images, videos and live videos
def rescale_frame(frame, scale =  0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# only works for live videos
def change_resolution(width, height):
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('videos/dog_video.mp4')

img = cv.imread('photos/dog1.jpeg')
resized_img = rescale_frame(img)

while True:
    # capture.read reads the video frame by frame
    # it returns the frame and a boolean whether the frame was read successfully or not
    isTrue ,frame = capture.read()

    frame_resized = rescale_frame(frame)

    cv.imshow('video', frame) # capture each frame using imshow()
    cv.imshow('video_resized', frame_resized)

    cv.imshow('dog', img)
    cv.imshow('dog_resized', resized_img)

    # if letter key is pressed, break out of the loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.waitKey(0) 