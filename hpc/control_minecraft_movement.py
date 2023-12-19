import numpy as np
from mcpi.minecraft import Minecraft
import cv2
def move(x,y,w,h):
    
    pos = mc.player.getPos()
    
    center_x = x + w / 2
    center_y = y + h / 2
    weithavg = ( w + h ) / 2
    
    flagx = 0
    flagy = 0
    flagz = 0
    if y < 140:
        flagx = 0.5
    elif y > 240:
        flagx = -0.5
        
    if x < 220:
        flagz = 0.5
    elif x >320:
        flagz = -0.5
        
    if weithavg > 170:
        flagy = 0.5
    elif weithavg < 130:
        flagy = -0.5
        
    mc.player.setPos(pos.x + flagx, pos.y + flagy, pos.z + flagz)
    #mc.player.setPos(pos.x+1,pos.y+1,pos.z+1)
    

cap = cv2.VideoCapture(0)

mc = Minecraft.create()

while(True):
    
    
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    face_cascade = cv2.CascadeClassifier('C:/Users/41640/miniconda3/envs/DIP2023/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        move(x,y,w,h)
    #print(frame.shape)
    cv2.imshow('controler',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()