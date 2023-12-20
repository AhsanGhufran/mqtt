from http import client
import paho.mqtt.client as mqtt


def on_connect(client,userdata,flag,rc):
    print(f"Connected with result code {rc}")
    client.subscribe("your/command/channel")


def on_messege(client,userdata,msg):
    print(f"Received message on topic {msg.topic} : {msg.payload}")



client =mqtt.Client()
client.on_connect=on_connect
client.on_message=on_messege

client.connect("broker.hivemq.com",1883,60)
print("Listening Forever")
try:
    client.loop_forever()

except:
    print("Something Happened Connecting to the Broker!")