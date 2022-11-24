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
    if request.method=="POST":
        email=request.POST['UserEmail']
        password=request.POST['UserPassword']

        if user_detail.objects.filter(email=email,password=password):
            messages.success(request," you are Successfully logged in")
                
            # user=user_detail.objects.
            # print(user)
            # if user_detail.objects.filter(password=password):
            #     messages.success(request," you are Successfully logged in")
            #     return redirect(homePage)
            # else:
            #     messages.success(request,"Invalid Password")
            return redirect(homePage)
        else:
            messages.success(request,"Incorrect credintials")
            


    return render(request,"scheduling/Login.html")


def booking_details(request):
    if request.method == "POST":
        name=request.POST['firstName']
        date=request.POST['date']
        slot=request.POST['slot']
        stime=request.POST['stime']
        sparity=request.POST['sparity']
        etime=request.POST['etime']
        eparity=request.POST['eparity']
        description=request.POST['description']

        try:
            Book=Booking_detail(fullname=name,date=date,slot=slot,start=stime,start_parity=sparity,end=etime,end_parity=eparity,description=description)
            #user_obj=User.objects.create_user(name=fname+" "+lname,gender=gender,dob=dob,height=height,weight=weight,email=email)
            
            Book.save()
            messages.success(request,"Booking succesfully")
            return redirect(homePage)
        except:
            messages.success(request,"something happend try again after sometime")

    
    return render(request,"scheduling/booking details.html")

