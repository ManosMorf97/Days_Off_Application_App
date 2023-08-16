from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from code_.connection import *
from code_.manager import *
from django import forms

# Create your views here.
@login_required(login_url="/accounts/login")
def welcome_manager(request):
    return render(request,'welcome_manager.html')


@login_required(login_url="/accounts/login")
def answer_requests(request):
    if request.method=="GET":
        rows=see_Requests()
        return render(request,'answer_requests.html',{'rows':rows})
    else:
        accepted_ids=[int(id) for id in request.POST.getlist('ids')]
        print(accepted_ids)
        complete=Accept_Reject(accepted_ids)
        return render(request,'answer_requests.html',{'rows':[],'message':True,'success':complete})


