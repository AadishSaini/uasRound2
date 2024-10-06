# import cv2 as cv

# img = cv.imread('./cat.jpg')

# if img is None:
#     print('Could not open or find the image.')
#     exit()

# img = cv.cvtColor(img, cv.COLOR_BGR2HSV)


# cv.namedWindow('window')
# cv.imshow('window', img)

# cv.waitKey(0)
# cv.destroyAllWindows()


import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)

    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)


    maskBlue = cv.inRange(hsv, lower_blue, upper_blue)
    maskGreen = cv.inRange(hsv, green_lower, green_upper)
    maskRed = cv.inRange(hsv, red_lower, red_upper)


    resblue = cv.bitwise_and(frame, frame, mask = maskBlue)
    resgreen = cv.bitwise_and(frame, frame, mask = maskGreen)
    resRed = cv.bitwise_and(frame, frame, mask = maskRed)


    cv.imshow('hsv', hsv)
    cv.imshow('blue', resblue)
    cv.imshow('green', resgreen)
    cv.imshow('red', resRed)

    cv.imshow('origional', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
