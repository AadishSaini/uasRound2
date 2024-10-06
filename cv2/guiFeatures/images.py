import cv2 as cv
import sys

img = cv.imread('starryNight.jpg')

if img is None:
    sys.exit('null image')


cv.imshow('window', img)

k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite('starry_night.png', img)