import numpy as np
import cv2
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)             

ret, frame = cap.read()
frame = cv2.flip(frame,1) 
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    x0 = x
    y0 = y
    w0 = w
    h0 = h
    s0 = h0 * w0

while True:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    pos=mc.player.getTilePos()
    pos_x = pos.x
    pos_y = pos.y
    pos_z = pos.z
    
    for (x,y,w,h) in faces:
        if(x < x0):
            pos_x -= 1
        elif(x > x0):
            pos_x += 1
            
        if(y < y0):
            pos_z -= 1
        elif(y > y0):
            pos_z += 1
        
        s = w * h
        
        if(s < s0):
            pos_y -= 1
        elif(s > s0):
            pos_y += 1
            
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.imshow('xiaogu',frame)
            
        mc.player.setTilePos(pos_x, pos_y, pos_z)
        x0 = x
        y0 = y
        s0 = h0 * w0    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()