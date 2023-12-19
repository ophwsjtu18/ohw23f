import numpy as np
import cv2
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

cap = cv2.VideoCapture(1)
x0=0
y0=0
w0=1
h0=1
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    #print(frame.shape)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        pos=mc.player.getTilePos()
        a=pos.x
        b=pos.z
        c=pos.y
        if x<x0:
            a-=1
        if x>x0:
            a+=1
        if y<y0:
            b+=1
        if y>y0:
            b-=1
        if w*h<w0*h0:
            c-=1
        if w*h>w0*h0:
            c+=1
        mc.player.setPos(a,c,b)
        print(w*h,w0*h0)
        x0=x
        y0=y
        w0=w
        h0=h
        

        #time.sleep(1)
        print(f"face pos is {x,y}")
        print("player pos is",pos)

        print(" ")
    
    cv2.imshow('she',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
