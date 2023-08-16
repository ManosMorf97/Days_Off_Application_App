from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from code_.connection import *
from code_.employee import *
from django import forms

# Create your views here.

@login_required(login_url="/accounts/login")
def welcome_employee(request):
    unreaded=unseen_answers(request.user.username)
    print(request.user.username)
    return render(request,'welcome_employee.html',{'unreaded':unreaded})

@login_required(login_url="/accounts/login")
def request_days(request):
    message=False
    if request.method=='GET':
        return render(request,'new_request.html',{'message':message})
    else:
        message=True
        category=request.POST.get('category')
        days=request.POST['days']
        answer=create_request(request.user.username,category,int(days))
        success=False
        if answer.startswith('Your request'):
            success=True
        return render(request,'new_request.html',{'message':message,'success':success,'answer':answer})

@login_required(login_url="/login")
def left_days_off(request):
    days_off={}
    types=["NormalDaysOff","ParentialDaysOff","DiseaseDaysOff"]
    for type_ in types:
        days_off[type_]=get_left_days_off(request.user.username,type_)
    return render(request,'left_days_off.html',{'days_off':days_off})


@login_required(login_url="/login")
def decisions(request):
    decisions=results(request.user.username)
    return render(request,'decisions.html',{'decisions':decisions})



def test(request):
    print(request.user)
    return render(request,'welcome_employee_2.html')