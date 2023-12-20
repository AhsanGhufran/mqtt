import paho.mqtt.publish as publish


mqtt_broker_address="broker.hivemq.com"
mqtt_channel="your/command/channel"
message="Hello World"
mqtt_port=1883

publish.single(mqtt_channel,message,hostname=mqtt_broker_address,port=mqtt_port)