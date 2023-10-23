#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install opencv-python


# In[2]:


import numpy as np
import cv2


# ## 读取&显示图像

# In[3]:


img = cv2.imread('rabbit.jpg')
#img = cv2.imread('rabbit.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[4]:


print(img.shape)


# ## 修改图像
# ### 像素赋值

# In[7]:


for i in range(3):
    for j in range(3):
        img[i*15:(i+1)*15,j*15:(j+1)*15]=img[85:100,155:170]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('9eyes.jpg',img)


# ### 绘制图形

# In[9]:


for i in range(3):
    for j in range(3):
        cv2.rectangle(img,(i*15,j*15),((i+1)*15,(j+1)*15),(102,205,170),1) #左上角顶点,右下角顶点,颜色，线宽
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('9rectangles.jpg',img)


# In[ ]:




