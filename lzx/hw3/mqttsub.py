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

