from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .forms import UserRegistrationForm
import paho.mqtt.client as mqtt
from secretP import *
import time
import json


def home(request):
    return HttpResponse('HOME')
# Create your views here.


def register(request):
    if request.method=='POST':
        print('POP')
        form=UserRegistrationForm(request.POST)

        if(form.is_valid()):

            message_array=[None]
            inbox=[False]

            client=mqtt.Client("mqttf")

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
            #print('POP')
            form.save()
            email=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            firstname=form.cleaned_data['FirstName']
            lastname=form.cleaned_data['LastName']
            params={'email':email,'firstname':firstname,'lastname':lastname}
            request_to_server={'sender':email,'function':'insert_new_user','params':params}


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

            user=authenticate(username=email,password=password)
            print("OK")
            
            login(request,user)
            return redirect('/accounts/login')
    else:
        form=UserRegistrationForm()
        
    context={'form':form}
    print(form.errors)
    return render(request,'registration/register.html',context)