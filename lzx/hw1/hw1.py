import numpy as np
import cv2

img = cv2.imread('rabbit.jpg')

eye = img[330:400, 520:610]

for i in range(1, 4):
    for j in range(1, 4):
        img[70*(j-1):70*j, 90*(i-1):90*i] = eye

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destoryAllWindows()
