from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from code_.connection import *

# Create your views here.


def welcome_employee(request):
    print(request.user)
    return render(request,'welcome_employee.html')

def test(request):
    print(request.user)
    return render(request,'welcome_employee_2.html')