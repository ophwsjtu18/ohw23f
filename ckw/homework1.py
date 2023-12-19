import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('rabbit.jpg')
for i in range(3):
    for j in range(3):
        img[i*50:i*50+50,j*60:j*60+60]=img[160:210,250:310]
#print(img.shape)
cv2.imshow('image',img)
print(img.shape)
cv2.waitKey(10000)
cv2.destroyAllWindows()
