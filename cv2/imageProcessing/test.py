import cv2 as cv
import numpy as np


image = np.zeros((300, 300, 3), dtype=np.uint8)


image = cv.circle(
	image, # the image on which you want to draw a circle
	(120, 50), # centre coordinates
	10, # radius of circle
	(255, 0, 0), # color
	1 # thickness of circle
)

cv.imshow('window', image)

cv.waitKey(0)