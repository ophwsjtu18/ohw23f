import numpy as np
import cv2

# face_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
face_cascade = cv2.CascadeClassifier("cv/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("cv/haarcascade_eye.xml")
center_y = 240
center_x = 320

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cv2.rectangle(frame,(center_x-5,center_y-5),(center_x+5,center_y+5),(0,255,0),2)

    for (x,y,w,h) in faces:
        # print((x,y,w,h))
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey ,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        mid_x = x+w//2
        mid_y = y+h//2
        cv2.rectangle(frame,(mid_x-5,mid_y-5),(mid_x+5,mid_y+5),(255,0,0),2)
        # print(mid_x,mid_y)

        if mid_x-center_x>100:
            print("move leftwards")
        elif center_x-mid_x>100:
            print("move rightwards")
            
        if mid_y-center_y>100:
            print("move upwards")
        elif center_y-mid_y>100:
            print("move downwards")
            
    # print(frame.shape)
    # cv2.line(frame,(0,0),(480, 640),(255,0,0),5)
    cv2.imshow('xiaogu',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

