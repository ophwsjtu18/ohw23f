import cv2
from mcpi.minecraft import Minecraft
import time

# 初始化 Minecraft 连接
mc = Minecraft.create()

# 初始化 OpenCV 的人脸检测
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 启动视频捕获
cap = cv2.VideoCapture(0)

def move_player(dx, dy, dz):
    current_pos = mc.player.getTilePos()
    mc.player.setTilePos(current_pos.x + dx, current_pos.y + dy, current_pos.z + dz)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            # 根据人脸位置移动玩家
            center_x = x + w // 2
            center_y = y + h // 2
            
            # 根据人脸在画面中的位置，控制左右移动
            if center_x < frame.shape[1] / 3:
                move_player(-1, 0, 0)  # 向左移动
            elif center_x > 2 * frame.shape[1] / 3:
                move_player(1, 0, 0)  # 向右移动
            
            # 根据人脸在画面中的位置，控制前后移动
            if center_y < frame.shape[0] / 3:
                move_player(0, 0, -1)  # 向前移动
            elif center_y > 2 * frame.shape[0] / 3:
                move_player(0, 0, 1)  # 向后移动

            # 根据人脸大小控制上升或下降
            face_area = w * h
            if face_area > (frame.shape[0] * frame.shape[1]) / 6:
                move_player(0, 1, 0)  # 上升
            elif face_area < (frame.shape[0] * frame.shape[1]) / 10:
                move_player(0, -1, 0)  # 下降

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.1) 
finally:
    cap.release()
    cv2.destroyAllWindows()