import paho.mqtt.client as mqtt
import time

# MQTT配置
broker_address = "mqtt.16302.com" 
port = 1883
topic = "ZHS2023" 

# 创建MQTT客户端实例
client = mqtt.Client("MQTT_Publisher")

# 连接到MQTT代理
client.connect(broker_address, port)

# 发送消息
def send_message(message):
    client.publish(topic, message)
    print("Message Sent: ", message)

numbers = "12345"
send_message(numbers)

time.sleep(2)
client.disconnect()