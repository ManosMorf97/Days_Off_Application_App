from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django import forms
import paho.mqtt.client as mqtt
from secretP import *
import time
import json
# Create your views here.
@login_required(login_url="/accounts/login")
def welcome_manager(request):


    inbox=[False]
    message_array=[None]

    client=mqtt.Client("mqttf")

    def on_message(client,userdate,message):
        print("Incoming Message")
        message_json=str(message.payload.decode("utf-8","ignore"))
        message_dict=json.loads(message_json)
        #print(message_dict['results'])
        if 'reciever' in message_dict.keys() and message_dict['reciever']=='boss':
            message_array[0]=message_dict['results']
            print(message_array[0])
            inbox[0]=True



    
    client.on_message=on_message

    request_to_server={'sender':'boss','function':'activate_tables','params':None}

    client.connect("10.0.59.134",port=1883)
    client.loop_start()
    client.subscribe("home/frontend"+broker_pwd)
    json_request_to_server=json.dumps(request_to_server)
    client.publish("home/backend"+broker_pwd,json_request_to_server)
    while not inbox[0]:
        pass
    client.loop_stop()
    client.disconnect()
    inbox[0]=False

    return render(request,'welcome_manager.html')


@login_required(login_url="/accounts/login")
def answer_requests(request):
    if request.method=="GET":

        inbox=[False]
        rows=[None]

        client=mqtt.Client("mqttf")

        def on_message(client,userdate,message):
            print("Incoming Message")
            message_json=str(message.payload.decode("utf-8","ignore"))
            message_dict=json.loads(message_json)
            #print(message_dict['results'])
            if 'reciever' in message_dict.keys() and message_dict['reciever']=='boss':
                rows[0]=message_dict['results']
                print(rows[0])
                inbox[0]=True
        
        client.on_message=on_message

        request_to_server={'sender':'boss','function':'see_Requests','params':None}

        client.connect("10.0.59.134",port=1883)
        client.loop_start()
        client.subscribe("home/frontend"+broker_pwd)
        json_request_to_server=json.dumps(request_to_server)
        client.publish("home/backend"+broker_pwd,json_request_to_server)
        while not inbox[0]:
            pass
        client.loop_stop()
        client.disconnect()
        inbox[0]=False


        return render(request,'answer_requests.html',{'rows':rows[0]})
    else:


        accepted_ids=[int(id) for id in request.POST.getlist('ids')]
        print(accepted_ids)

        inbox=[False]
        complete=[None]
        client=mqtt.Client("mqttf")

        def on_message(client,userdate,message):
            print("Incoming Message")
            message_json=str(message.payload.decode("utf-8","ignore"))
            message_dict=json.loads(message_json)
            #print(message_dict['results'])
            if 'reciever' in message_dict.keys() and message_dict['reciever']=='boss':
                complete[0]=message_dict['results']
                print(complete[0])
                inbox[0]=True
        
        client.on_message=on_message

        params={'accepted_requests_ids':accepted_ids}
        request_to_server={'sender':'boss','function':'Accept_Reject','params':params}

        client.connect("10.0.59.134",port=1883)
        client.loop_start()
        client.subscribe("home/frontend"+broker_pwd)
        json_request_to_server=json.dumps(request_to_server)
        client.publish("home/backend"+broker_pwd,json_request_to_server)
        while not inbox[0]:
            pass
        client.loop_stop()
        client.disconnect()
        inbox[0]=False

        return render(request,'answer_requests.html',{'rows':[],'message':True,'success':complete[0]})


