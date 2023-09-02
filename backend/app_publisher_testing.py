import paho.mqtt.client as mqtt
import time
import json

client=mqtt.Client("Frontend")

#request={'sender':"johnd@gmail.com",'function':"insert_new_user",'params':{'email':'johnd@gmail.com','firstname':'John','lastname':'Doe'}}
request={'sender':"",'function':"activate_tables",'params':None}

message_array=['e']

def on_message(client,userdate,message):
    print("Incoming Message")
    message_json=str(message.payload.decode("utf-8","ignore"))
    message_dict=json.loads(message_json)
    #print(message_dict['results'])
    if 'reciever' in message_dict.keys():
        message_array[0]=message_dict['results']


client.on_message=on_message
client.connect("localhost",port=1883)
client.loop_start()
client.subscribe("App")
json_request=json.dumps(request)
client.publish("App",json_request)
time.sleep(10)
client.loop_stop()
client.disconnect()


print(message_array[0])
