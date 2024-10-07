import cv2 as cv
import numpy as np

drawing = False

def nothing(x):
    pass
ix, iy = -1, -1
def draw_circles(event, x, y, flags, param):
    global ix, iy, drawing, mode
    colour = param[0]
    thickness = param[1]
    if event == cv.EVENT_LBUTTONDBLCLK:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(img,(x,y),1,colour,thickness)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img,(x,y),1,colour,thickness)

img = np.zeros((300, 512, 3), dtype=np.uint8)
cv.namedWindow('window')

cv.createTrackbar('R', 'window', 0, 255, nothing)
cv.createTrackbar('G', 'window', 0, 255, nothing)
cv.createTrackbar('B', 'window', 0, 255, nothing)
cv.createTrackbar('thickness', 'window', 0, 30, nothing)

param = [(255, 255, 255), -1]

cv.setMouseCallback('window',draw_circles, param)

while(True):
    cv.imshow('window', img)

    param[0] = (cv.getTrackbarPos('R','window'),  cv.getTrackbarPos('G','window'),cv.getTrackbarPos('B','window'))
    param[1] = cv.getTrackbarPos('thickness', 'window')
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
