import numpy as np
import cv2 as cv

def givecords(event, x, y, flags, params):
	# print(x, y)
	pass

img = cv.imread('cat.jpeg')
b, g, r = cv.split(img)

catMouth = img[44:97, 61:103]
img[0:53, 0:42] = catMouth

cv.namedWindow('window')
cv.namedWindow('window1')
cv.namedWindow('window2')
cv.namedWindow('window3')

cv.setMouseCallback('window',givecords)

while True:
	cv.imshow('window', img)
	cv.imshow('window1', b)
	cv.imshow('window2', g)
	cv.imshow('window3', r)
	
	if cv.waitKey(0) == ord('q'):
		break

cv.destroyAllWindows()