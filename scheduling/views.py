from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse

from .models import *


# Create your views here.

def homePage(request):
    return render(request,"scheduling/home.html")

def registerPage(request):
    if request.method == "POST":
        username=request.POST['Name']
        email=request.POST['UserEmail']
        pass1=request.POST['UserPassword']
        pass2=request.POST['ConfirmPassword']
        mobile_number=request.POST['Mobile']
        if pass1==pass2:
            messages.success(request,pass1,pass2)
            my_user=user_detail(username=username,email=email,password=pass1,mobile_number=mobile_number)
            #user_obj=User.objects.create_user(name=fname+" "+lname,gender=gender,dob=dob,height=height,weight=weight,email=email)
            
            my_user.save()
            messages.success(request,"your details had been stored succesfully")
            return redirect(loginPage)
            
        else:
            messages.success(request,"password not matched")
            # return redirect(request,"scheduling/Sign up.html")

    return render(request,"scheduling/Sign up.html")

def loginPage(request):

    return render(request,"scheduling/Login.html")


def booking_details(request):
    messages.success(request,"password not matched")
    
    return render(request,"scheduling/booking details.html")

