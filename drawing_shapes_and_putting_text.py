#!/usr/bin/env python3

import cv2 as cv
import numpy as np

# blank image to draw on it
# 500, 500, 3 is the height, width and channel for rgb
blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('blank', blank)

# paint the full image a certain colour, green in this case
blank[:] = 0, 255, 0
cv.imshow('green', blank)

# paint some portions of the image a certain colour, red in this case
# 200:350 is the height meaning use pixels from 200 to 350-1
# and 350:400 is the width meaning use pixels from 350 to 400-1
blank[200:350, 350:400] = 0, 0, 255
cv.imshow('red', blank)

# draw a rectangle
cv.rectangle(blank, (10,10), (100, 100), (0, 100, 0), thickness=2)
cv.imshow('rectangle', blank)

# draw a rectangle and fill it with the colour with blue
# can use cv.FILLED or -1
cv.rectangle(blank, (150,150), (250, 250), (100, 0, 0), thickness=cv.FILLED)
cv.imshow('rectangle', blank)

# draw a circle
# to fill the circle is the same as above
cv.circle(blank, (250,250), 40, (10, 10, 10), thickness=3)
cv.imshow('circle', blank)

# draw a line that is white in colour
cv.line(blank, (35,50), (200, 125), (255, 255, 255), thickness=4)
cv.imshow('line', blank)

# how to write a text
cv.putText(blank, "hello there", (255, 400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 0), 2)
cv.imshow('text', blank)
cv.waitKey(0)