from time import sleep
import cv2
import mediapipe as mp
from math import sqrt

from sympy import false, true

from aip import AipSpeech
import os

import pygame

APP_ID = '43450933'
API_KEY = "vyhWypuSzrXCjzWxkFGAtFt6"
SECRET_KEY = "PYbwFmHwlDRMpfbbSIqv6nbshcgaQi4n" 

client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

x = [0]*22
y = [0]*22

for i in range(1, 10):
    voice=client.synthesis(i,'zh',6,{'vol':15,'per':3,'spd':5})
    fp = open(str(i)+".mp3",'wb')
    fp.write(voice)
    fp.close()

def getDis(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def straight(y1, y2, y3):
    if(y1 > y2 > y3):
        return 1 #straight upwards
    else:
        return 2
    
def horizontal(x1, x2, x3):
    if(x1 > x2 > x3):
        return 1
    elif(x1 < x2 < x3):
        return 2
    else:
        return 3

def ring(filename):   
    # 初始化pygame
    pygame.init()
    # 加载音频文件
    pygame.mixer.music.load(filename)
    # 播放音频文件
    pygame.mixer.music.play()
    # 关闭pygame
    sleep(0.3)
    pygame.quit()

def ring_num(num):
    ring(str(num)+".mp3")

while True:
    num = 0
    while(num == 0):
        img= cv2.flip(cap.read()[1],1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    
                    for i in range(0, 21):
                        if id == i:
                            x[i] = cx
                            y[i] = cy
                            #print("y[", i, "]=", y[i], " ")
                            
                    cv2.putText(img, str(int(id)), (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                    
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
        # cv2.imshow("image", img)
        
        status = [0]*5
        for i in range(1, 5):
            initial = 4*i + 1
            #print("y[", initial, "]=", y[initial], " ")
            status[i] = straight(y[initial+1], y[initial+2], y[initial+3])
            
        status_x = [0]*5
        for i in range(1, 5):
            initial = 4*1 + 1
            status_x[i] = horizontal(x[initial+3], x[initial+2], x[initial+1])
            
        four_fingers = horizontal(x[17], x[13], x[9])
        thumb = horizontal(x[4], x[3], x[2])
        if(four_fingers == 1 and thumb == 1 or four_fingers == 2 and thumb == 2):
            status[0] = 2 #大拇指朝外
        elif(four_fingers == 1 and thumb == 2 or four_fingers == 1 and thumb == 2):
            status[0] = 1 #大拇指朝里
            
        #print("status[0]=", status[0], " status[1]=", status[1], " status[2]=", status[2], " status[3]=", status[3], " status[4]=", status[4])
            
        #two
        if(status[1] == 1 and status[2] == 1 and status[3] == 2 and status[4] == 2):
            print("two")
            num = 2
            continue
            
        #three
        if(status[4] == 1 and status[2] == 1 and status[3] == 1 and status[1] == 2):
            print("three")
            num = 3
            continue
        if(status[1] == 1 and status[2] == 1 and status[3] == 1 and status[4] == 2):
            print("three")
            num = 3
            continue
            
        #four
        if(status[0] == 2 and status[1] == 1 and status[2] == 1 and status[3] == 1 and status[4] == 1):
            print("four")
            num = 4
            continue
            
        #five
        if(status[0] == 1 and status[1] == 1 and status[2] == 1 and status[3] == 1 and status[4] == 1):
            print("five")
            num = 5
            continue
        
        #eight
        if(thumb == 2 and status_x[1] == 1 ):#and status_x[2] == 2 and status_x[3] == 2 and status_x[4] == 2):
            print("eight")
            num = 8
            continue
        if(thumb == 1 and status_x[1] == 2 ):#and status_x[2] == 1 and status_x[3] == 1 and status_x[4] == 1):
            print("eight")
            num = 8
            continue
        
        #one
        if(status[1] == 1 and status[2] == 2 and status[3] == 2 and status[4] == 2):
            print("one")
            num = 1
            continue
            
        #six
        if(status[0] == 1 and status[1] == 2 and status[2] == 2 and status[3] == 2 and status[4] == 1):
            print("six")
            num = 6
            continue
            
        #nine
        flag = true
        for i in range(2, 5):
            if(y[4*i+4] > y[4] + 100 or y[4*i+4] < y[4] - 100):
                flag = false
        if(flag):
            if(y[8] < y[5] and y[8] > y[7]):
                print("nine")
                num = 9
                continue
                
        #seven
        flag = true
        for i in range(0, 4):
            if(y[4*i+8] > y[4*i + 4] + 100 or y[4*i+8] < y[4*i+4] - 100 or y[i] == 0):
                flag = false
        if(flag):
            print("seven")
            num = 7
            continue
    
    # voice=client.synthesis(num,'zh',6,{'vol':15,'per':3,'spd':5})
    #with open("playback.mp3",'wb') as fp:
    # fp = open("playback.mp3",'wb')
    # fp.write(voice)
    # fp.close()
    # ring("playback.mp3")
    if(num != 0):
        ring_num(num)

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()





