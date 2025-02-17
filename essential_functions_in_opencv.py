#!/usr/bin/env python3

import cv2 as cv

img = cv.imread('photos/dog1.jpeg')
cv.imshow('original image', img)

# converting image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray image', gray_img)

# blurring an image
# to increase the blur, can increase the kernel size (7,7) but must be odd numbers
blur_image = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur image', blur_image)

# how to create an edge cascade
# 125 and 175 atr the threshold values
canny_image = cv.Canny(img, 125, 175)
cv.imshow('canny image', canny_image)

# how to dilate the image, uses the canny image
# can increase the kernel or the iterations
dilated_image = cv.dilate(canny_image, (7,7), iterations=3)
cv.imshow('dilated image', dilated_image)

# how to erode the image, uses dilated image
eroded_image = cv.erode(dilated_image,(3,3), iterations=3)
cv.imshow('eroded image', eroded_image)

# how to resize image
resized_image = cv.resize(img, (500, 500))
cv.imshow('resized image', resized_image)

# how to crop image
cropped_image = img[50:200, 200:400]
cv.imshow('cropped image', cropped_image)

cv.waitKey(0)