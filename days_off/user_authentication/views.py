from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse

def home(request):
    return HttpResponse('HOME')
# Create your views here.

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if(form.is_valid()):
            form.save()
            email=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(usename=email,password=password)
            login(request,user)
            return redirect('home/')
    else:
        form=UserCreationForm()
        
        context={'form':form}
        return render(request,'registration/register.html',context)