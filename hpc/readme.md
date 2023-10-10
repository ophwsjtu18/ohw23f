# hpc
[好用的电风扇使用手册](#好用的电风扇使用手册)  
[作业1](#作业1)  

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
