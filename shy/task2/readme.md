# 作业二_MqttNotePlayer

- Python代码

  ```python
  # mqtt发送端
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
      msg = "3303013050000000"
      result = client.publish(topic, msg)
      print("Sending ",msg)
      time.sleep(2)
  ```

  ```python
  # mqtt接收端 / 串口发送
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
      write_len = ser.write(msg.payload.decode().encode( "utf-8")) # 发送音符
      time.sleep(write_len * 0.15)
      
  ser = serial.Serial("COM6",9600)
  if ser.isOpen():
      print("打开成功")
      time.sleep(2)
      
  else:
      print("打开失败")
  #ser.close()
  
  client.subscribe(topic)
  client.on_message = on_message
  client.loop_forever()
  ```

- Mixly代码

  ```c
  #include <Adafruit_NeoPixel.h>
  
  Adafruit_NeoPixel rgb_display_4 = Adafruit_NeoPixel(1,4,NEO_GRB + NEO_KHZ800);
  int tone2[7]={131,147,165,175,196,220,247};
  
  volatile char sub;
  
  void setup(){
    rgb_display_4.begin();
    sub = '0';
    Serial.begin(9600);
    pinMode(6, OUTPUT);
  }
  
  void loop(){
    if (Serial.available() > 0) {
      sub = Serial.read();
      rgb_display_4.setPixelColor((1)-1, (((0 & 0xffffff) << 16) | ((200 & 0xffffff) << 8) | 0));
      rgb_display_4.show();
  
    }
  
    switch (sub) {
     case '1':
      tone(6,262);
      delay(150);
      noTone(6);
      break;
     case '2':
      tone(6,294);
      delay(150);
      noTone(6);
      break;
     case '3':
      tone(6,330);
      delay(150);
      noTone(6);
      break;
     case '4':
      tone(6,349);
      delay(150);
      noTone(6);
      break;
     case '5':
      tone(6,392);
      delay(150);
      noTone(6);
      break;
     case '6':
      tone(6,440);
      delay(150);
      noTone(6);
      break;
     case '7':
      tone(6,494);
      delay(150);
      noTone(6);
      break;
     case '0':
      delay(160);
      rgb_display_4.setPixelColor((1)-1, (((0 & 0xffffff) << 16) | ((0 & 0xffffff) << 8) | 0));
      rgb_display_4.show();
      noTone(6);
      break;
    }
    sub = '0';
    rgb_display_4.setPixelColor((1)-1, (((0 & 0xffffff) << 16) | ((0 & 0xffffff) << 8) | 0));
    rgb_display_4.show();
  
  }
  ```

  

- 运行效果

  ![](https://github.com/ophwsjtu18/ohw23f/blob/main/shy/media/task2_display.png)

  [查看视频](https://github.com/ophwsjtu18/ohw23f/tree/main/shy/task2/效果展示.mp4)