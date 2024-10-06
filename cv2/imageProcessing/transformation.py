import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
path = '/mnt/windows/Users/Aadish/Desktop/uasr2/cv2/imageProcessing/cat.jpg'

img = cv.imread(path)
size = img.shape
print(size)

res = cv.resize(img, None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)

cv.imshow('window', img)
cv.imshow('res', res)


cv.waitKey(0)
import numpy as np
import cv2 as cv
 
img = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)
rows,cols = img.shape
 
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
 
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()



img = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols = img.shape
 
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('rotated', dst)

cv.waitKey(0)
cv.destroyAllWindows()


img = cv.imread('cat.jpg')
rows,cols,ch = img.shape
 
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
 
M = cv.getAffineTransform(pts1,pts2)
 
dst = cv.warpAffine(img,M,(cols,rows))
 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
