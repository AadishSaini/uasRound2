import cv2 as cv
import sys

cap = cv.VideoCapture(0)

if not (cap.isOpened()):
    sys.exit('cant open camera')


while True:
    ret, frame = cap.read()

    if not ret:
        print('cant get fram')

    gray = cv.cvtColor(frame, cv.COLOR_BAYER_BG2GRAY)

    cv.imshow('window', gray)
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()