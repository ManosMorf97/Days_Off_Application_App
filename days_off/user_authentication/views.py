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
            email=form.cleaned_data['email']
            password=form.cleaned_data['password1']
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            user=authenticate(username=email,password=password)
            login(request,user)
            return redirect('account/login')
    else:
        form=UserCreationForm()
        
        context={'form':form}
        return render(request,'registration/register.html',context)