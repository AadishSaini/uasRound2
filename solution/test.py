import cv2 as cv
import numpy as np
from consts import *



image = cv.imread('./images/1.png')
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

red_mask = cv.inRange(hsv_image, np.array([0, 100, 50]), np.array([0, 255,255]))

result_red_mask = cv.bitwise_and(image, image, mask=red_mask)



gray_image = cv.cvtColor(result_red_mask, cv.COLOR_BGR2GRAY)
_, thresholded_image = cv.threshold(gray_image, 0, 255, cv.THRESH_BINARY)

contours, _ = cv.findContours(thresholded_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
contour_image = cv.drawContours(result_red_mask.copy(), contours, -1, (0, 255, 0), 2)

cv.imshow('masked', result_red_mask)
cv.waitKey(0)
cv.destroyAllWindows()
