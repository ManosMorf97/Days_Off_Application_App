from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from code_.connection import *

# Create your views here.


def employee(request):
    return HttpResponse('EMPLOYEE')