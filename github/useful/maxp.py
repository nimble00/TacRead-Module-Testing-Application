import cv2
import numpy as np

im =  cv2.imread("fou2.jpg")
#im = cv2.resize(im,(640,512))
smallest = np.amin(im)
biggest = np.amax(im)
print smallest
print " "
print biggest
