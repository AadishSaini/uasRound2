import cv2 as cv

img1 = cv.imread('./cat.jpeg')
img2 = cv.imread('./starry_night.png')
cv.resize(img1, (640, 480))
cv.resize(img2, (640, 480))

blended = cv.addWeighted(img1,0.7,img2,0.3,0)

cv.namedWindow('window')

cv.imshow('window', dst)

cv.waitKey(0)
cv.destroyAllWindows()
