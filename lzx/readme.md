# 作业1
code:
```python
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
```
![rabbit](https://github.com/ophwsjtu18/ohw23f/blob/main/lzx/hw1/result1.jpg)

# 作业2
code:
```python
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
```
![rabbit](https://github.com/ophwsjtu18/ohw23f/blob/main/lzx/hw2/result2.jpg)
# 作业3
code:
```python
import random
import time
from paho.mqtt import client as mqtt_client

broker = 'mqtt.16302.com'       #服务器网址
port = 1883                     #连接端口
topic = "mqttNotePlayer"               #订阅频道
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()

while True:
    msg = "12313132344324"
    result = client.publish(topic, msg)
    time.sleep(2)
```
code:
```python
import random
import time
import serial
from paho.mqtt import client as mqtt_client



broker = 'mqtt.16302.com'
port = 1883
topic = "mqttNotePlayer"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!",client,userdata)
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)


def on_message(client, userdata, msg):
    print("Received from topic",topic,msg.payload.decode())
    write_len = ser.write(msg.payload.decode().encode( "utf-8"))
    time.sleep(write_len * 0.15)
    
ser = serial.Serial("COM6",9600)
if ser.isOpen():
    print("打开成功")
    time.sleep(2)
    
else:
    print("打开失败")

client.subscribe(topic)
client.on_message = on_message
client.loop_forever()
```
mixly image:
![mixly](https://github.com/ophwsjtu18/ohw23f/blob/main/lzx/hw3/mixly.png)

# 作业4
[python codes](https://github.com/ophwsjtu18/ohw23f/edit/main/hpc/buildhous.py)
```python
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)
mc.player.setTilePos(140,0,140)
for i in range(0,10):
    for j in range(0,10):
        mc.setBlock(120+i, 0, 120+j, 57)
        mc.setBlock(120 + i, 9, 120 + j, 152)
for k in range(1,9):
    for i in range(0, 10):
        mc.setBlock(120 + i, k, 129, 56)
        mc.setBlock(120 + i, k, 120, 56)
        mc.setBlock(120, k, 120 + i, 56)
        mc.setBlock(129, k, 120 + i, 56)
for k in range(1, 3):
    for i in range(4, 6):
        mc.setBlock(129, k, 120 + i, 0)
for k in range(5, 7):
    for i in range(4, 6):
        mc.setBlock(120 + i, k, 129, 0)
        mc.setBlock(120 + i, k, 120, 0)
        mc.setBlock(120, k, 120 + i, 0)
        mc.setBlock(129, k, 120 + i, 0)
```

# 作业5
```python
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
```
