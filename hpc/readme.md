# hpc
[好用的电风扇使用手册](#好用的电风扇使用手册)  
[作业1](#作业1)  
[作业2](#作业2)
[作业3](#作业3)
[作业4](#作业4)
[作业5](#作业5)

---
# 好用的电风扇使用手册

## 基本信息

这是一个非常好用的**电风扇**，具体好用的方面我不知道，下面细说

## 功能

- 好看
- 便宜
- 能用

## 产品对比

我们的产品和某友商待参电风扇的对比

| 功能 | 好用的电风扇 | 待参的电风扇 |
| ---- | ------------ | ------------ |
| 颜值 | 好看         | 不好看       |
| 价格 | 便宜         | 不便宜       |
| 功能 | 能用         | 也能用       |
| 趣味 | 有趣         | 好无趣       |
## 如何获取我们的产品

[点这里有好用的电风扇可以白嫖](www.bilibili.com)

![meme](https://img1.imgtp.com/2023/10/10/3hXM67u2.jpeg)

---
# 作业1
code:
```python
import cv2
import numpy as np
img = cv2.imread('rabbit.jpg',1)
for i in range(0,3):
    for j in range(0,3):
        img[(0+j*50):(50+j*50),(0+i*50):(50+i*50)]=img[80:130,200:250]
        cv2.rectangle(img,(0+i*50,0+j*50),(50+i*50,50+j*50),(0,255,0),2)
cv2.imshow('image',img)
cv2.imwrite('9eye_rabbit.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows
```
![rabbit](https://github.com/ophwsjtu18/ohw23f/blob/main/hpc/9eye_rabbit.jpg)

# 作业2
code:
```python
import random
import time
import serial
from paho.mqtt import client as mqtt_client

ser = serial.Serial("COM5", 9600)

broker = 'mqtt.16302.com'
port = 1883
topic = "1017"
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
    a = msg.payload.decode()
    if ser.isOpen():
        print("打开成功")
        time.sleep(2)
        write_len = ser.write(a.encode("utf-8"))
        print(write_len)
        time.sleep(write_len*1.5)
    else:
        print("打开失败")
    

client.subscribe(topic)
client.on_message = on_message
client.loop_forever()

```
# 作业3
mixly image:
![mixly](https://github.com/ophwsjtu18/ohw23f/blob/main/hpc/mixly.png)

# 作业4
[python codes](https://github.com/ophwsjtu18/ohw23f/edit/main/hpc/buildhous.py)
```python
from mcpi.minecraft import Minecraft

mc=Minecraft.create()
pos=mc.player.getTilePos()
mc.postToChat("250, 100, 200")

# 外墙
mc.setBlocks(250, 100, 200, 270, 120, 220, 1)

# 掏空
mc.setBlocks(252, 100, 202, 268, 120, 218, 0)

# 门
mc.setBlocks(258, 100, 200, 262, 105, 202, 0)

# 地板
mc.setBlocks(252, 100, 202, 268, 100, 218, 57)

# 天花板
mc.setBlocks(248, 121, 198, 272, 121, 222, 29)

# 灯
mc.setBlocks(252, 119, 202, 268, 119, 218, 20)
mc.setBlocks(252, 120, 202, 268, 120, 218, 11)

# 窗户
mc.setBlocks(250, 105, 205, 251, 115, 215, 20)
mc.setBlocks(269, 105, 205, 270, 115, 215, 20)
```

# 作业5
[python codes](https://github.com/ophwsjtu18/ohw23f/edit/main/hpc/control_minecraft_movement.py)
```python
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
```
