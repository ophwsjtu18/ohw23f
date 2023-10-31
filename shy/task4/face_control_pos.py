from mcpi.minecraft import Minecraft
import time
import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
mc=Minecraft.create()

cap = cv2.VideoCapture(0)

pos=mc.player.getTilePos()
print((pos.x,pos.y,pos.z)) # initial player position
#mc.player.setPos(0,0,0)

center_y = 240 # camera vision center
center_x = 320

first_flag = 1


while(True):
    
    # cv processing and face detecting
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cv2.rectangle(frame,(center_x-5,center_y-5),(center_x+5,center_y+5),(0,255,0),2)

    for (x,y,w,h) in faces:
        # record the width and height of face at the initial status
        if first_flag==1:
            init_w = w
            init_h = h
            first_flag = 0
        # print((x,y,w,h))
        
        # draw rectangles around face and eyes
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey ,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        # face center (for comparing with vision center)
        mid_x = x+w//2
        mid_y = y+h//2
        
        cv2.rectangle(frame,(mid_x-5,mid_y-5),(mid_x+5,mid_y+5),(255,0,0),2)
        # print(mid_x,mid_y)
        # print((w,h))

        # moving along x-axis
        if mid_x-center_x>50:
            print("moving rightwards")
            pos=mc.player.getTilePos()
            mc.player.setPos(pos.x+1,pos.y,pos.z)
        elif center_x-mid_x>50:
            print("moving leftwards")
            pos=mc.player.getTilePos()
            mc.player.setPos(pos.x-1,pos.y,pos.z)
            
        # moving along y-axis
        if mid_y-center_y>30:
            print("moving downwards")
            pos=mc.player.getTilePos()
            mc.player.setPos(pos.x,pos.y-2,pos.z)
        elif center_y-mid_y>20:
            print("moving upwards")
            pos=mc.player.getTilePos()
            mc.player.setPos(pos.x,pos.y+2,pos.z)
        
            
        if w-init_w>50:
            print("moving closer")
            pos=mc.player.getTilePos()
            mc.player.setPos(pos.x,pos.y,pos.z-1)
        elif init_w-w>20:
            print("moving away")
            pos=mc.player.getTilePos()
            mc.player.setPos(pos.x,pos.y,pos.z+1)
  
            
    # print(frame.shape)
    # cv2.line(frame,(0,0),(480, 640),(255,0,0),5)
    cv2.imshow('xiaogu',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

