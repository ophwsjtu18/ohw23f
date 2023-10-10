# ohw23f/shy🌱

This folder is a collection of assignments and projects from SJTU Open Hardware course.

## 目录

- Week5 | 2023-10-10
  - Markdown Syntax:  [陆游器/陆地游泳器产品说明书](#陆游器/陆地游泳器产品说明书)
  - Introduction to OpenCV:  [作业一_兔子](#作业一_兔子)

------



## 陆游器/陆地游泳器产品说明书

<img src="https://5b0988e595225.cdn.sohucs.com/q_70,c_zoom,w_640/images/20180809/7c1d68ba8ee548f8b01839bcadfca18c.jpeg" alt="Rabbit_2" style="zoom:50%;" />

1. [产品概述](#1-产品概述)
2. [技术规格](#2-技术规格)
3. [特色功能](#3-特色功能)
4. [使用说明](#4-使用说明)
5. [注意事项](#5-注意事项)
7. [保修政策](#6-保修政策)

### 1. 产品概述

陆地游泳器，是一种颠覆性的运动工具，产品采用最尖端的虚拟现实技术和气垫浮力系统，让您体验前所未有的陆地游泳之旅。

### 2. 技术规格

| 技术规格           | 描述              |
|-------------------|-------------------|
| 游泳速度           | 1米/100秒          |
| 气垫浮力系统       | 永不下沉            |
| 备用氧气罐         | 用于提供清新空气     |

### 3. 特色功能
- 欣赏沿岸美丽的室内景观。
- 定制海水口味。

### 4. 使用说明


### 5. 注意事项

- 不适合使用于真实水域。
- 不要试图进食虚拟海洋生物。
- 若您对虚拟现实产生幻觉，请停止使用并咨询虚拟现实医生。

### 6. 保修政策

我们提供无条件的终身保修，除非产品被用于真实水中，被海豚盗走。



## 作业一_兔子

### 1.代码


```python
for i in range(3):
    for j in range(3):
        img[i*15:(i+1)*15,j*15:(j+1)*15]=img[85:100,155:170]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('9eyes.jpg',img)
```

```python
for i in range(3):
    for j in range(3):
        cv2.rectangle(img,(i*15,j*15),((i+1)*15,(j+1)*15),(102,205,170),1) #左上角顶点,右下角顶点,颜色，线宽
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('9rectangles.jpg',img)
```

### 2.结果

![Rabbit_2](9rectangles.jpg)

