from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


from .models import *


# Create your views here.

def home(request):
    return render(request,"scheduling/home.html")

def registerPage(request):
    return render(request,"scheduling/Sign up.html")
