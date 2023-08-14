from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from code_.connection import *
from .forms import UserRegistrationForm


def home(request):
    return HttpResponse('HOME')
# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)

        if(form.is_valid()):
            form.save()
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            firstname=form.cleaned_data['FirstName']
            lastname=form.cleaned_data['LastName']
            user=authenticate(username=email,password=password)
            db,cursor=connect()
            sql_statement="Insert into Employee values(%s,%s,%s,25,25,120)"
            details=(email,firstname,lastname)
            cursor.execute(sql_statement,details)
            disconnect(db,cursor)
            login(request,user)
            return redirect('account/login')
    else:
        form=UserRegistrationForm()
        
        context={'form':form}
        return render(request,'registration/register.html',context)