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
        print('POP')
        form=UserRegistrationForm(request.POST)

        if(form.is_valid()):
            #print('POP')
            form.save()
            email=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            firstname=form.cleaned_data['FirstName']
            lastname=form.cleaned_data['LastName']
            user=authenticate(username=email,password=password)
            print("OK")
            db,cursor=connect()
            sql_statement="Insert into Employee values(%s,%s,%s,25,25,120)"
            details=(email,firstname,lastname)
            cursor.execute(sql_statement,details)
            db.commit()
            disconnect(db,cursor)
            login(request,user)
            return redirect('/accounts/login')
    else:
        form=UserRegistrationForm()
        
    context={'form':form}
    print(form.errors)
    return render(request,'registration/register.html',context)