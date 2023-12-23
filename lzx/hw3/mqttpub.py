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

