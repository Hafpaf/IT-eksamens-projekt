import numpy as np
import cv2 as cv

img1 = cv.imread('king_dedede.jpg') #read picture in BGR

px = img1[100,100] #pixel to look at
print(px)
cv.imshow('king_dedede', img1) #show image
cv.waitKey(0) #Wait for keypress: 0
cv.destroyAllAindows() #Close windows