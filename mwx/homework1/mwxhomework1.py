import numpy as np
import cv2

img = cv2.imread('C:/Users/hp/Desktop/download.jpg')

img[0:50,0:60]=img[50:100,150:210]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
