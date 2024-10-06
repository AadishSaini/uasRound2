import numpy as np
import cv2 as cv
import sys

cap = cv.VideoCapture('./earth_rotating.mp4')
grayscale = False
while True:
    ret, frame = cap.read()

    if not ret:
        sys.exit('Can\'t reveive frame')

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if grayscale:
        cv.imshow('window', gray)
    if not grayscale:
        cv.imshow('window', frame)
    if cv.waitKey(1) == ord('q'):
        break
    if cv.waitKey(1) == ord('c'):
        grayscale = False
    if cv.waitKey(1) == ord('g'):
        grayscale = True
    

cap.release()
cv.destroyAllWindows()
