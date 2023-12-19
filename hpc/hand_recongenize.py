import cv2
import mediapipe as mp
from math import sqrt 

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


def getDis(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

x4,y4 = x8,y8 = 0,0

# X1,Y1 = 100,100
# X2,Y2 = 100,300
# X3,Y3 = 100,500

while True:
    img= cv2.flip(cap.read()[1],1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                if id == 8:
                    x8, y8 = cx, cy
                if id == 6:
                    x6, y6 = cx, cy
                if id == 12:
                    x12, y12 = cx, cy
                if id == 10:
                    x10, y10 = cx, cy
                if id == 16:
                    x16, y16 = cx, cy
                if id == 14:
                    x14, y14 = cx, cy
                if id == 20:
                    x20, y20 = cx, cy
                if id == 18:
                    x18, y18 = cx, cy
                if id == 4:
                    x4, y4 == cx, cy
                
                
                # if id == 4:
                #     x4,y4 = cx, cy 
                # if id == 8:
                #     x8,y8 = cx, cy 

                # if getDis(x4,y4,x8,y8) >=50:
                #     print("OPEN")
                # else:
                #     print("CLOSE")
                #     if X1-100<=x8<=X1+100 and Y1-100 <=y8<=Y1+100:
                #         X1,Y1=x8,y8
                #     if X2-100<=x8<=X2+100 and Y2-100 <=y8<=Y2+100:
                #         X2,Y2=x8,y8
                #     if X3-100<=x8<=X3+100 and Y3-100 <=y8<=Y3+100:
                #         X3,Y3=x8,y8

                cv2.putText(img, str(int(id)), (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            # cv2.line(img,(x4,y4),(x8,y8),(100,100,200),2)
            if x6 > x8 and x12 > x10 :
                print("1")
            elif x6 > x8 and x10 > x12 and x16 > x14 :
                print("2")
            else:
                print('I do not konw')
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # cv2.circle(img,(X1,Y1),100,(100,100,200),-1)
    # cv2.circle(img,(X2,Y2),100,(100,200,200),-1)
    # cv2.circle(img,(X3,Y3),100,(200,100,200),-1)
            
    cv2.imshow("image", img)
    if cv2.waitKey(2) & 0xFF == 27:
        break

cap.release()





