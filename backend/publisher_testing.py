import json
import paho.mqtt.client as mqtt
import time
List = [[{'course':'python','fee':4000}], [{'duration':'60days', 'discount':1200}]]
jsonList = json.dumps(List)
#print(jsonList)

List_2=json.loads(jsonList)
#print(List_2)

client=mqtt.Client("Random")


def show_message(client,userdata,message):
    message_decoded=str(message.payload.decode("utf-8"))
    if message_decoded.startswith("Subscriber: "):
        print(message_decoded)

client.on_message=show_message

def disconnect(client,userdata,flags,rc=0):
    print("bye")

def connect(client,userdata,flags,rc):
    if(rc==0):
        print("Connected")

client.on_connect=connect
client.on_disconnect=disconnect


for i in range(2):
    client.connect("mqtt.eclipseprojects.io")
    client.loop_start()
    client.publish("Random","Publisher: "+input())
    client.subscribe("Random")
    time.sleep(10)
    client.loop_stop()

    client.disconnect()





