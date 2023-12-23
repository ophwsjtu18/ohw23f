from mcpi.minecraft import Minecraft
import time
import numpy as np
import cv2
mc=Minecraft.create()
cap = cv2.VideoCapture(0)
while(True):
    pos = mc.player.getTilePos()
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    img=frame
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        mc.player.setTilePos(pos.x+(240-y-h/2)/100, pos.y+(pow(h*w,0.5)-100)/5, pos.z+(320-x-w/2)/100)
        print(w,h,x,y)
    cv2.imshow('xiaogu', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break