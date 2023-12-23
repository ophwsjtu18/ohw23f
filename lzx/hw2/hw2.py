import numpy as np
import cv2

img = cv2.imread('rabbit.jpg')


eye = img[330:400, 520:610]

#draw the rectangles
for i in range(1, 4):
    cv2.rectangle(img,(13*(i-1),13*(i-1)),(13*(3-i)+90*3+44, 13*(3-i)+70*3+44),(0,255,0),3)

#move the eye
for i in range(1, 4):
    for j in range(1, 4):
        img[35+70*(j-1):35+70*j, 35+90*(i-1):35+90*i] = eye
    

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destoryAllWindows()
