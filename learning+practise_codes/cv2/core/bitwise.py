import numpy as np
import cv2 as cv

img1 = np.zeros((300, 300, 3), dtype = np.uint8)
cv.rectangle(img1, (100, 100), (250, 250), (0, 0, 255),-1)
cv.imshow('image_1', img1)

img2 = np.zeros((300, 300, 3), dtype= np.uint8)
cv.circle(img2, (150, 150), 90, 255,-1)
cv.imshow('image_2', img2)


and_bitwise = cv.bitwise_and(img1, img2)
cv.imshow('image_3', and_bitwise)

or_bitwise = cv.bitwise_or(img1, img2)
cv.imshow('bitwise_or', or_bitwise)

xor_bitwise = cv.bitwise_xor(img1, img2)
cv.imshow('bitwise_xor', xor_bitwise)

cv.waitKey(0)

