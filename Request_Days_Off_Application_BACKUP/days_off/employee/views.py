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
def welcome_employee(request):

    unreaded=[None]
    inbox=[False]

    client=mqtt.Client("mqttf")

    def on_message(client,userdate,message):
        print("Incoming Message")
        message_json=str(message.payload.decode("utf-8","ignore"))
        message_dict=json.loads(message_json)
        #print(message_dict['results'])
        if 'reciever' in message_dict.keys() and message_dict['reciever']==request.user.username:
            unreaded[0]=message_dict['results']
            print(unreaded[0])
            inbox[0]=True

    

    client.on_message=on_message

    params={'email':request.user.username}
    request_to_server={'sender':request.user.username,'function':'unseen_answers','params':params}

    client.connect("localhost",port=1883)
    client.loop_start()
    client.subscribe("home/frontend"+broker_pwd)
    json_request_to_server=json.dumps(request_to_server)
    client.publish("home/backend"+broker_pwd,json_request_to_server)
    while not inbox[0]:
        pass
    client.loop_stop()
    client.disconnect()
    inbox[0]=False

    print(request.user.username)
    return render(request,'welcome_employee.html',{'unreaded':unreaded[0]})

@login_required(login_url="/accounts/login")
def request_days(request):
    message=False

    if request.method=='GET':

        inbox=[False]
        message_array=[None]

        client=mqtt.Client("mqttf")

        def on_message(client,userdate,message):
            print("Incoming Message")
            message_json=str(message.payload.decode("utf-8","ignore"))
            message_dict=json.loads(message_json)
            #print(message_dict['results'])
            if 'reciever' in message_dict.keys() and message_dict['reciever']==request.user.username:
                message_array[0]=message_dict['results']
                print(message_array[0])
                inbox[0]=True

    

        client.on_message=on_message

        request_to_server={'sender':request.user.username,'function':'activate_tables','params':None}

        client.connect("localhost",port=1883)
        client.loop_start()
        client.subscribe("home/frontend"+broker_pwd)
        json_request_to_server=json.dumps(request_to_server)
        client.publish("home/backend"+broker_pwd,json_request_to_server)
        while not inbox[0]:
            pass
        client.loop_stop()
        client.disconnect()
        inbox[0]=False

        return render(request,'new_request.html',{'message':message})
    
    else:
        message=True
        category=request.POST.get('category')
        days=request.POST['days']

        inbox=[False]
        answer=[None]

        client=mqtt.Client("mqttf")

        def on_message(client,userdate,message):
            print("Incoming Message")
            message_json=str(message.payload.decode("utf-8","ignore"))
            message_dict=json.loads(message_json)
            #print(message_dict['results'])
            if 'reciever' in message_dict.keys() and message_dict['reciever']==request.user.username:
                answer[0]=message_dict['results']
                print(answer[0])
                inbox[0]=True

    

        client.on_message=on_message
        params={'email':request.user.username,'category_double_quote':category,'request_days_off':int(days)}
        request_to_server={'sender':request.user.username,'function':'create_request','params':params}

        client.connect("localhost",port=1883)
        client.loop_start()
        client.subscribe("home/frontend"+broker_pwd)
        json_request_to_server=json.dumps(request_to_server)
        client.publish("home/backend"+broker_pwd,json_request_to_server)
        while not inbox[0]:
            pass
        client.loop_stop()
        client.disconnect()
        inbox[0]=False


        success=False
        if answer[0].startswith('Your request'):
            success=True
        
        return render(request,'new_request.html',{'message':message,'success':success,'answer':answer[0]})

@login_required(login_url="/login")
def left_days_off(request):
    days_off={}
    types=["NormalDaysOff","ParentialDaysOff","DiseaseDaysOff"]
    inbox=[False]
    for type_ in types:
        days_off[type_]=None
        client=mqtt.Client("mqttf")

        def on_message(client,userdate,message):
            print("Incoming Message")
            message_json=str(message.payload.decode("utf-8","ignore"))
            message_dict=json.loads(message_json)
            #print(message_dict['results'])
            if 'reciever' in message_dict.keys() and message_dict['reciever']==request.user.username:
                days_off[type_]=message_dict['results']
                print(days_off[type_])
                inbox[0]=True

    

        client.on_message=on_message
        params={'email':request.user.username,'category_double_quote':type_}
        request_to_server={'sender':request.user.username,'function':'get_left_days_off','params':params}
        
        client.connect("localhost",port=1883)
        client.loop_start()
        client.subscribe("home/frontend"+broker_pwd)
        json_request_to_server=json.dumps(request_to_server)
        client.publish("home/backend"+broker_pwd,json_request_to_server)
        while not inbox[0]:
            pass
        client.loop_stop()
        client.disconnect()
        inbox[0]=False
        
        #days_off[type_]=get_left_days_off(request.user.username,type_)
    return render(request,'left_days_off.html',{'days_off':days_off})


@login_required(login_url="/login")
def decisions(request):

    inbox=[False]
    decisions=[None]

    client=mqtt.Client("mqttf")

    def on_message(client,userdate,message):
        print("Incoming Message")
        message_json=str(message.payload.decode("utf-8","ignore"))
        message_dict=json.loads(message_json)
        #print(message_dict['results'])
        if 'reciever' in message_dict.keys() and message_dict['reciever']==request.user.username:
            decisions[0]=message_dict['results']
            print(decisions[0])
            inbox[0]=True
            


    client.on_message=on_message
    params={'email':request.user.username}
    request_to_server={'sender':request.user.username,'function':'results','params':params}

    client.connect("localhost",port=1883)
    client.loop_start()
    client.subscribe("home/frontend"+broker_pwd)
    json_request_to_server=json.dumps(request_to_server)
    client.publish("home/backend"+broker_pwd,json_request_to_server)
    while not inbox[0]:
        pass
    client.loop_stop()
    client.disconnect()
    inbox[0]=False


    return render(request,'decisions.html',{'decisions':decisions[0]})



def test(request):
    print(request.user)
    return render(request,'welcome_employee_2.html')