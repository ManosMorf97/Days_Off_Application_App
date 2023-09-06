# https://github.com/johntango/Mosquitto


import paho.mqtt.client as mqtt
import time
import json
from employee import *
from manager import *
from activation import *

client=mqtt.Client("mqttb",transport='tcp')
client.username_pw_set("mqtt")

func={}
func['insert_new_user']=insert_new_user
func['create_request']=create_request
func['unseen_answers']=unseen_answers
func['get_left_days_off']=get_left_days_off
func['results']=results
func['see_Requests']=see_Requests
func['Accept_Reject']=Accept_Reject
func['activate_tables']=activate_tables


def handle_Request(client,userdata,message):
    print("I heard something")
    message_decoded_json=message.payload.decode("utf-8","ignore")
    message_decoded=json.loads(message_decoded_json)
    if "sender" not in message_decoded:
        return
    sender=message_decoded['sender']
    params=message_decoded['params']
    func_name=message_decoded['function']
    results=""
    if params==None:
        results=func[func_name]()
    else:
        results=func[func_name](**params)
    message_to_reciever={'results':results,'reciever':sender}
    client.publish("home/frontend",json.dumps(message_to_reciever))



client.on_message=handle_Request
client.connect("localhost",port=1883)
client.subscribe("home/backend")

client.loop_forever()

client.disconnect()