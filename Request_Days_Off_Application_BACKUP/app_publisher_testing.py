import paho.mqtt.client as mqtt
import time
import json
from secretP import *

client=mqtt.Client("mqttf")
client.username_pw_set("mqtt")

request={'sender':"johnd@gmail.com",'function':"insert_new_user",'params':{'email':'johnd@gmail.com','firstname':'John','lastname':'Doe'}}

message_array=['e']
inbox=[False]

def on_message(client,userdate,message):
    print("Incoming Message")
    message_json=str(message.payload.decode("utf-8","ignore"))
    message_dict=json.loads(message_json)
    #print(message_dict['results'])
    if 'reciever' in message_dict.keys():
        message_array[0]=message_dict['results']
        print(message_array[0])
        inbox[0]=True


client.on_message=on_message
client.connect('localhost',port=1883)
client.loop_start()
client.subscribe("home/frontend"+broker_pwd)
json_request=json.dumps(request)
client.publish("home/backend"+broker_pwd,json_request)
#time.sleep(10)
while not inbox[0]:
    pass
client.loop_stop()
client.disconnect()


print("bye")